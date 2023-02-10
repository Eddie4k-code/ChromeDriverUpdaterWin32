import configparser
import os

config = configparser.RawConfigParser()

config.read(".\\config\\config.ini")

class ReadConfig():
    """
    Gets properties from our config file such as operating system type, download directory, and where we want chromedriver.exe placed.
    """

    @staticmethod
    def getDownloadPath():
        path = config.get("common info", "downloadPath")

        return path

    @staticmethod
    def getZipFileName():
        name = config.get("common info", "zipFileName")

        return name

    @staticmethod
    def getNeededVersion():
        version = config.get("common info", "neededVersion")

        return version


    @staticmethod
    def getExtractToPath():
        path = config.get("common info", "extractToPath")

        return path

