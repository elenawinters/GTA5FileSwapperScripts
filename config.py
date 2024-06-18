from pathlib import Path
import configparser

class Config():
    def __init__(self):
        self.config_file = 'config.ini'
        self.config = configparser.ConfigParser()
        self.config.read(self.config_file)

    def fetchInstallLocation(self):
        return Path(self.config['gta']['path']).resolve()
    
    def fetchArchiveFixLocation(self):
        return Path(self.config['archivefix']['path'], 'ArchiveFix.exe').resolve()