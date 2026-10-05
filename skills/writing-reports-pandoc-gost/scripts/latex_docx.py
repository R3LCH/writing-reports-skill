"""Export the shared LaTeX source to editable DOCX, not from rendered PDF.

Pandoc handles semantic conversion; this script supplies the GUAP Word profile.
Inspect complex TeX constructs separately: this is not a TeX layout emulator.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess

from docx import Document
from docx.shared import Cm

from gost_docx import add_toc, format_body, number_equations


def bibliography(source):
    """Expose standard bibitem content/citations to Pandoc's semantic reader."""
    citations = {}
    def replace(match):
        parts = re.split(r'\\bibitem\{([^{}]+)\}', match.group(1))
        if len(parts) < 3 or parts[0].strip():
            raise ValueError('Use plain bibitem{key} entries or a separately verified bibliography export')
        entries = []
        for number, index in enumerate(range(1, len(parts), 2), 1):
            citations[parts[index]] = number
            entries.append('\\item ' + parts[index + 1])
        return '\\chapter*{Список использованных источников}\n\\begin{enumerate}\n' + ''.join(entries) + '\\end{enumerate}'
    source = re.sub(r'\\begin\{thebibliography\}\{[^{}]*\}(.*?)\\end\{thebibliography\}',
                    replace, source, flags=re.S)
    def cite(match):
        keys = [key.strip() for key in match.group(1).split(',')]
        if any(key not in citations for key in keys):
            raise ValueError('Unresolved citation in LaTeX source: ' + match.group(1))
        return '[' + ', '.join(str(citations[key]) for key in keys) + ']'
    return re.sub(r'\\cite\{([^{}]+)\}', cite, source)


def export(project):
    source = project / 'report.tex'
    parsed = subprocess.run(['pandoc', '-f', 'latex', '-t', 'json'], input=bibliography(source.read_text()),
                            text=True, capture_output=True, check=True, cwd=project)
    ast = json.loads(parsed.stdout)
    labels = {}
    equation_numbers = {}
    equation_labels = {}
    display_numbers = []
    for number, match in enumerate(re.finditer(
            r'\\begin\{equation\}(.*?)\\end\{equation\}', source.read_text(), re.S), 1):
        body = match.group(1)
        for key in re.findall(r'\\label\{([^{}]+)\}', body):
            equation_labels[key] = str(number)
        expression = re.sub(r'\\label\{[^{}]+\}', '', body)
        equation_numbers.setdefault(re.sub(r'\s+', '', expression), []).append(number)
    labels.update(equation_labels)
    numbered = [0] * 6
    tables = 0
    figures = 0
    structural = set()

    def visit(value):
        nonlocal tables, figures
        if isinstance(value, list):
            for child in value:
                visit(child)
        elif isinstance(value, dict):
            kind = value.get('t')
            data = value.get('c')
            if kind in ('RawBlock', 'RawInline'):
                raise ValueError('Unsupported raw TeX in DOCX export; use a semantic equivalent: ' + str(data))
            if kind == 'Header':
                level, attributes, text = data
                if 'unnumbered' in attributes[1]:
                    structural.add(''.join(v.get('c', ' ') if v['t']=='Str' else ' ' for v in text).strip())
                else:
                    numbered[level-1] += 1
                    numbered[level:] = [0] * (6-level)
                    prefix = '.'.join(str(n) for n in numbered[:level])
                    data[2] = [{'t': 'Str', 'c': prefix}, {'t': 'Space'}] + text
                    if attributes[0]:
                        labels[attributes[0]] = prefix
            if kind == 'Table':
                tables += 1
                caption = data[1][1]
                if caption:
                    caption[0]['c'] = [{'t': 'Str', 'c': f'Таблица {tables} —'}, {'t':'Space'}] + caption[0]['c']
                labels[data[0][0]] = str(tables)
            if kind == 'Div' and data[0][0] and any(b['t']=='Table' for b in data[1]):
                labels[data[0][0]] = str(tables + 1)
            if kind == 'Figure':
                figures += 1
                labels[data[0][0]] = str(figures)
                caption = data[1][1]
                if caption:
                    caption[0]['c'] = [{'t':'Str','c':f'Рисунок {figures} —'}, {'t':'Space'}] + caption[0]['c']
            if kind == 'Image' and data[2][1].startswith('fig:'):
                figures += 1
                labels[data[0][0]] = str(figures)
                data[1] = [{'t':'Str','c':f'Рисунок {figures} —'}, {'t':'Space'}] + data[1]
            if kind == 'Math' and data[0]['t'] == 'DisplayMath':
                data[1] = re.sub(r'\\label\{[^{}]+\}', '', data[1])
                candidates = equation_numbers.get(re.sub(r'\s+', '', data[1]), [])
                display_numbers.append(candidates.pop(0) if candidates else None)
            visit(data)
    visit(ast['blocks'])

    def references(value):
        if isinstance(value, list):
            for child in value:
                references(child)
        elif isinstance(value, dict):
            if value.get('t') == 'Link':
                attributes, text, target = value['c']
                attrs = dict(attributes[2])
                if 'reference' in attrs:
                    key = attrs['reference']
                    if key not in labels:
                        raise ValueError('Reference needs explicit DOCX support: ' + key)
                    value['c'][1] = [{'t':'Str','c':labels[key]}]
            references(value.get('c'))
    references(ast['blocks'])
    output = project / 'build'
    output.mkdir(exist_ok=True)
    path = output / 'report.docx'
    converted = subprocess.run(['pandoc', '-f', 'json', '-t', 'docx', '-o', str(path)],
                              input=json.dumps(ast), text=True, capture_output=True, check=True, cwd=project)
    if parsed.stderr.strip() or converted.stderr.strip():
        raise ValueError('Pandoc warnings require review: ' + parsed.stderr + converted.stderr)
    document = Document(path)
    cover_paragraphs = format_body(document, structural=structural, includes_cover=True)
    # Approximate the demonstration cover's three stretchable groups in Word.
    # A supplied institutional title page still needs its own layout verification.
    if len(cover_paragraphs) == 7:
        for index, distance in ((2, 6.5), (4, 6.5), (6, 6)):
            cover_paragraphs[index].paragraph_format.space_before = Cm(distance)
    number_equations(document, display_numbers)
    toc_title = add_toc(document)
    toc_title.paragraph_format.page_break_before = True
    document.save(path)
    manifest = {'source_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
                'docx_sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
                'editable': 'native paragraphs, tables and OMML equations',
                'required_review': ['Update TOC fields in Word/LibreOffice and verify page numbers',
                                    'Render DOCX independently; inspect title, figures, equations, bibliography and all pages',
                                    'Check complete source content against both output formats'],
                'pagination': 'Independent of the LaTeX PDF; identical page count is not guaranteed'}
    (output / 'docx-manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2)+'\n')
    print(f'Exported editable {path}; field update and visual review still required.')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('project', type=Path)
    args = parser.parse_args()
    try:
        export(args.project.resolve())
    except subprocess.CalledProcessError as error:
        parser.exit(1, error.stderr or str(error))
    except (OSError, ValueError) as error:
        parser.exit(1, str(error)+'\n')


if __name__ == '__main__':
    main()
