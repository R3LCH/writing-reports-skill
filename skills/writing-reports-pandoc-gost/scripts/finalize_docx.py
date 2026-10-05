"""Update DOCX fields/TOC with LibreOffice UNO and render it independently.

Run with a Python interpreter providing uno (usually /usr/bin/python3).
"""
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import tempfile
import time
import uuid

import uno
from com.sun.star.beans import PropertyValue


def prop(name, value):
    result = PropertyValue()
    result.Name, result.Value = name, value
    return result


def finalize(path):
    path = path.resolve()
    if not path.is_file():
        raise ValueError('DOCX file does not exist')
    executable = shutil.which('libreoffice') or shutil.which('soffice')
    if not executable:
        raise ValueError('LibreOffice is not installed')
    pipe = 'guap_' + uuid.uuid4().hex
    with tempfile.TemporaryDirectory(prefix='guap-lo-') as profile:
        process = subprocess.Popen([executable, '-env:UserInstallation=' + Path(profile).as_uri(),
                                    '--headless', '--norestore', '--nodefault', '--nofirststartwizard',
                                    '--accept=pipe,name=' + pipe + ';urp;StarOffice.ComponentContext'],
                                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        document = None
        try:
            local = uno.getComponentContext()
            resolver = local.ServiceManager.createInstanceWithContext('com.sun.star.bridge.UnoUrlResolver', local)
            deadline = time.monotonic() + 30
            while True:
                try:
                    context = resolver.resolve('uno:pipe,name=' + pipe + ';urp;StarOffice.ComponentContext')
                    break
                except Exception:
                    if process.poll() is not None or time.monotonic() >= deadline:
                        raise RuntimeError('Private LibreOffice instance failed to start')
                    time.sleep(0.2)
            desktop = context.ServiceManager.createInstanceWithContext('com.sun.star.frame.Desktop', context)
            document = desktop.loadComponentFromURL(path.as_uri(), '_blank', 0,
                (prop('Hidden', True), prop('ReadOnly', False), prop('UpdateDocMode', 3),
                 prop('MacroExecutionMode', uno.getConstantByName('com.sun.star.document.MacroExecMode.NEVER_EXECUTE'))))
            if document is None:
                raise ValueError('LibreOffice could not load DOCX')
            document.TextFields.refresh()
            indexes = document.DocumentIndexes
            for _ in range(2):
                for index in range(indexes.Count):
                    indexes.getByIndex(index).update()
                document.refresh()
            if indexes.Count == 0:
                raise ValueError('DOCX has no TOC index to update')
            document.storeAsURL(path.as_uri(), (prop('FilterName', 'Office Open XML Text'), prop('Overwrite', True)))
            rendered = path.with_name(path.stem + '-word-layout.pdf')
            document.storeToURL(rendered.as_uri(), (prop('FilterName', 'writer_pdf_Export'), prop('Overwrite', True)))
            result = {'docx': str(path), 'rendered_docx': str(rendered), 'updated_indexes': indexes.Count,
                      'visual_review': 'required; this PDF is the Word layout, not the LaTeX PDF'}
            result['docx_sha256'] = hashlib.sha256(path.read_bytes()).hexdigest()
            result['rendered_sha256'] = hashlib.sha256(rendered.read_bytes()).hexdigest()
            manifest_path = path.parent / 'docx-manifest.json'
            if manifest_path.exists():
                manifest = json.loads(manifest_path.read_text())
                manifest['docx_sha256'] = result['docx_sha256']
                manifest['fields_updated'] = True
                manifest['word_layout_sha256'] = result['rendered_sha256']
                manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2)+'\n')
            path.with_suffix('.fields.json').write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n')
            print(json.dumps(result, ensure_ascii=False))
        finally:
            if document is not None:
                document.close(True)
            process.terminate()
            try:
                process.wait(timeout=10)
            except subprocess.TimeoutExpired:
                process.kill()
                process.wait()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('docx', type=Path)
    args = parser.parse_args()
    finalize(args.docx)
