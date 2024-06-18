from pathlib import Path
import hashlib
import shutil
import config
import os

gta_install = config.Config().fetchInstallLocation()

file_mem = []

# https://stackoverflow.com/a/16876405/14125122
for file in Path('game_files').rglob('*'):
    item = Path(gta_install, file.relative_to('game_files'))
    if not item.exists():
        print(f'{item} does not exist. The corresponding file is {file}. Skipping.')
        continue
    if item.is_dir(): continue
    new = hashlib.md5(open(file, 'rb').read()).hexdigest()
    old = hashlib.md5(open(item, 'rb').read()).hexdigest()
    if new != old:
        print(f"MD5 Mismatch! The currently installed file doesn't match the one in the installation folder! File: {file.name}")
        file_mem.append({'item': item, 'file': file, 'match': False})
    elif new == old:
        file_mem.append({'item': item, 'file': file, 'match': True})
        # shutil.copy(item, Path('backup'))
        # print(file.relative_to('files'))
        # print(item)

if all(x['match'] for x in file_mem):  # if all hashes match, uninstall
    print('Uninstalling all current modifications!')
    for entry in file_mem:
        backup = Path('backup', entry['file'].relative_to('game_files'))
        shutil.copy(backup, Path(gta_install, entry['file'].relative_to('game_files')))
else:  # if only some match, update the ones that dont match
    print('Installing modifications from the installation folder! If you have items currently installed, newer items were detected and are being installed. Run this again to uninstall.')
    for entry in file_mem:
        backup = Path('backup', entry['file'].relative_to('game_files'))
        if not backup.exists():
            os.makedirs(os.path.dirname(backup), exist_ok=True)
            shutil.copy(entry['item'], backup)
        if not entry['match']:
            shutil.copy(entry['file'], Path(gta_install, entry['file'].relative_to('game_files')))
