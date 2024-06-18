# GTA5 File Swapper Scripts

All scripts are made for Python (tested on Windows, Python 3.11.2)

## Switch File Script

This script refers to a folder (`/game_files`), and will compare the hash to the file present there and the file present in the GTA5 installation folder. If the hashes mismatch, the file in the installation folder will be backed up to a backup folder (`/backup`) before being replaced by the relative file in the `/game_files` folder.

If the script is run and there are no mismatches between `/backup` and `/game_files`, the script will restore the files in the installation folder to those present in `/backup`

## Switch Addon Script

This script is intented to be used with things like Reshade and ENBSeries, although I'd discourage the latter.

This script just adds the contents of `/addon_files` to the installation path if `reshade-shaders` or `enbseries` are not present, and uninstalls them if they are.

## Fix All Archives

This is intended to be used with ArchiveFix. This script just iterates over all archive files in `/game_files` and launches a ArchiveFix subproccess on each one.