import os.path
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from readProp import readProps
import zipfile

class GetChromedriver:
    """
    Contains functionality for getting the chrome driver along with element locations.
    """

    recent_repo_xpath = "/html/body/div[1]/div/div[2]/div[3]/div/div[1]/section[2]/div[2]/div/div/div/div/div/div/div/div/p[3]/a/span"
    win32_xpath = "/html/body/table/tbody/tr[7]/td[2]/a"

    def __init__(self):
        self.driver = webdriver.Chrome()

        self.driver.implicitly_wait(10)

    def go_to_repo(self):
        """
          Goes to repo link where download is present
        """

        self.driver.get("https://chromedriver.chromium.org/downloads")

        api_link = self.driver.find_element(By.XPATH, self.recent_repo_xpath)
        api_link.click()
        tabs = self.driver.window_handles
        print(tabs)
        self.driver.switch_to.window(tabs[1])

    def download_zip_file(self):
        """
        Downloads zip file.
        """
        download_link = self.driver.find_element(By.XPATH, self.win32_xpath)
        download_link.click()
        time.sleep(10)

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

    delete_old_driver()

    updater = GetChromedriver()
    updater.go_to_repo()
    updater.download_zip_file()
    updater.extract_driver_from_zip()


if __name__ == "__main__":
    update_driver()

