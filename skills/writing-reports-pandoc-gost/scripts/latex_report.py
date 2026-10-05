"""Prepare pinned G7-32 sources, then compile a private report project."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile

REPOSITORY = 'https://github.com/latex-g7-32/latex-g7-32'
REVISION = 'fa9f9a847c1074c0aee5895872403fb276e15a7b'
CLASS_REVISION = '1d9c51a8e4b38faa715ea8b3c7154bbadc8d8da1'
SKILL = Path(__file__).resolve().parents[1]


def run(args, cwd=None, env=None):
    return subprocess.run(args, cwd=cwd, env=env, check=True, text=True,
                          stdout=subprocess.PIPE, stderr=subprocess.STDOUT).stdout


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def prepare(project):
    if project.exists():
        raise ValueError('Preparation requires a new directory; existing work is never overwritten.')
    with tempfile.TemporaryDirectory(prefix='g7-32-') as directory:
        source = Path(directory) / 'upstream'
        run(['git', 'clone', REPOSITORY, str(source)])
        run(['git', 'checkout', '--detach', REVISION], cwd=source)
        run(['git', 'submodule', 'update', '--init', 'G7-32'], cwd=source)
        if run(['git', 'rev-parse', 'HEAD'], cwd=source / 'G7-32').strip() != CLASS_REVISION:
            raise ValueError('Unexpected upstream class revision')
        project.mkdir(parents=True)
        shutil.copytree(source / 'G7-32' / 'tex', project, dirs_exist_ok=True)
        shutil.copy2(source / 'G7-32' / 'license.md', project / 'UPSTREAM-LICENSE.md')
        upstream_files = {p.name: digest(p) for p in project.iterdir() if p.is_file()}
        shutil.copy2(SKILL / 'assets/latex/guap-report.sty', project)
        shutil.copy2(SKILL / 'assets/latex/report.tex', project)
        manifest = {'repository': REPOSITORY, 'revision': REVISION,
                    'class_revision': CLASS_REVISION,
                    'license': 'Upstream GPL; see UPSTREAM-LICENSE.md',
                    'files': upstream_files}
        (project / 'template-lock.json').write_text(json.dumps(manifest, indent=2) + '\n')
    print(f'Prepared {project}; replace demonstration content and title before delivery.')


def build(project, engine, offline):
    source = project / 'report.tex'
    if not source.is_file():
        raise ValueError('report.tex missing; prepare a project first')
    lock = json.loads((project / 'template-lock.json').read_text())
    for name, expected in lock['files'].items():
        if digest(project / name) != expected:
            raise ValueError(f'Pinned upstream file changed: {name}; use the local overlay instead')
    executable = shutil.which(engine)
    if executable is None:
        raise ValueError(f'{engine} missing; install XeLaTeX/TeX Live or Tectonic first')
    output = project / 'build'
    output.mkdir(exist_ok=True)
    env = dict(os.environ)
    env['TEXINPUTS'] = str(project) + os.pathsep
    if Path(executable).name == 'tectonic':
        command = [executable, '--untrusted', '--keep-logs', '--keep-intermediates',
                   '--outdir', str(output)]
        if offline:
            command.append('--only-cached')
        command.append(str(source))
        transcript = run(command, cwd=project, env=env)
    else:
        command = [executable, '-no-shell-escape', '-halt-on-error', '-interaction=nonstopmode',
                   '-file-line-error', '-output-directory=' + str(output), str(source)]
        transcript = ''
        previous = None
        for _ in range(6):
            transcript += run(command, cwd=project, env=env)
            state = tuple(p.read_bytes() if p.exists() else b''
                          for p in (output / 'report.aux', output / 'report.toc', output / 'report.out'))
            if state == previous:
                break
            previous = state
        else:
            raise ValueError('Cross-references did not converge after six passes')
    (output / 'compiler-output.txt').write_text(transcript)
    pdf = output / 'report.pdf'
    if not pdf.is_file() or pdf.stat().st_size == 0:
        raise ValueError('Compiler produced no PDF')
    log = (output / 'report.log').read_text(errors='replace')
    problems = [line for line in log.splitlines() if any(term in line for term in
                ('Overfull', 'Missing character:', 'undefined', 'Rerun to get', 'Label(s) may have changed'))]
    manifest = {'template': lock, 'engine': run([executable, '--version']).splitlines()[0],
                'source_sha256': digest(source), 'profile_sha256': digest(project / 'guap-report.sty'),
                'pdf_sha256': digest(pdf), 'layout_warnings': problems,
                'visual_review': 'required; compilation is not proof of compliance'}
    (output / 'build-manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')
    if problems:
        raise ValueError('PDF requires correction; see build/build-manifest.json for layout/reference warnings')
    print(f'Built {pdf}; inspect every page, content and bibliography before delivery.')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=['prepare', 'build'])
    parser.add_argument('project', type=Path)
    parser.add_argument('--engine', default='xelatex', help='xelatex or path to tectonic')
    parser.add_argument('--offline', action='store_true', help='Tectonic: use only prewarmed cache')
    args = parser.parse_args()
    try:
        project = args.project.resolve()
        if args.action == 'prepare':
            prepare(project)
        else:
            build(project, args.engine, args.offline)
    except subprocess.CalledProcessError as error:
        parser.exit(1, error.stdout or str(error))
    except (OSError, ValueError, KeyError) as error:
        parser.exit(1, str(error) + '\n')


if __name__ == '__main__':
    main()
