import os.path
from readProp import readProps
import zipfile
import requests

class GetChromedriver:
    """
    Contains functionality for getting the chrome driver along with element locations.
    """

    recent_repo_xpath = "/html/body/div[1]/div/div[2]/div[3]/div/div[1]/section[2]/div[2]/div/div/div/div/div/div/div/div/p[3]/a/span"
    win32_xpath = "/html/body/table/tbody/tr[7]/td[2]/a"

    def __init__(self):
        self.download_link = f"https://chromedriver.storage.googleapis.com/{readProps.ReadConfig.getNeededVersion()}/chromedriver_win32.zip"

    def download_zip_file(self):
        """
        Downloads zip file using requests
        """

        response = requests.get(self.download_link)
        downloads_dir = os.path.expanduser(readProps.ReadConfig.getDownloadPath())

        with open(os.path.join(downloads_dir, readProps.ReadConfig.getZipFileName()), 'wb') as f:
            f.write(response.content)

    def extract_driver_from_zip(self):
        """
        Extracts the chromedriver.exe from the zip file.
        """
        downloads_dir = os.path.expanduser(readProps.ReadConfig.getDownloadPath())

        chromedriver_zip_path = os.path.join(downloads_dir, readProps.ReadConfig.getZipFileName())

        with zipfile.ZipFile(chromedriver_zip_path, 'r') as zip_ref:
            zip_ref.extract("chromedriver.exe", readProps.ReadConfig.getExtractToPath())


        os.remove(chromedriver_zip_path)


def delete_old_driver():
    """
    Deletes the old driver.
    """
    os.remove(readProps.ReadConfig.getExtractToPath() + "\chromedriver.exe")



def update_driver():
    """
    Updates the driver
    """
    try:

        delete_old_driver()
    except:
        pass

    updater = GetChromedriver()
    updater.download_zip_file()
    updater.extract_driver_from_zip()


if __name__ == "__main__":
    update_driver()

