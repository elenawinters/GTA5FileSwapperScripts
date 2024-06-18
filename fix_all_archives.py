from pathlib import Path
import subprocess
import config


archive_fix = config.Config().fetchArchiveFixLocation()

game_folder = Path('./game_files').resolve()


files = [file for file in Path(game_folder).rglob('*.rpf')]

for rpf in files:
    subprocess.run([archive_fix, 'fix', rpf])

# print(files)
print(len(files))
