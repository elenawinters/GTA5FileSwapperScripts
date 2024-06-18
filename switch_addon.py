from pathlib import Path
import shutil
import config
import os

gta_install = config.Config().fetchInstallLocation()


if Path(gta_install, 'enbseries').exists() or Path(gta_install, 'reshade-shaders').exists():  # remove files from gta folder
    enb_files = [x.relative_to('addon_files') for x in Path('addon_files').glob('*')]

    for file in Path(gta_install).glob('*'):
        if file.relative_to(gta_install) in enb_files:
            if file.is_dir():
                shutil.rmtree(file.resolve())
            else:
                file.unlink()
            print(f'Deleted {file}')
    print('Uninstalled Addon Files')
else:  # copy files to gta folder
    enb_files = Path('addon_files').rglob('*')

    for file in enb_files:
        if file.is_file():
            shutil.copy(file, Path(gta_install, file.relative_to('addon_files')))
        else:
            Path(gta_install, file.relative_to('addon_files')).mkdir()

    print('Installed Addon Files')
