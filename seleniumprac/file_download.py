from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options
import os

download_dir= r"C:\Download"
chrome_options = Options()
pref = {"download.default_directory":download_dir,
        "download.prompt_for_download":False,
        "directory_upgrade": True}
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/download")
time.sleep(5)
chrome_options.add_experimental_option( "prefs",pref)
time.sleep(3)
driver.find_element(By.XPATH,"//a[text()='Jpeg_with_exif.jpeg']").click()
time.sleep(3)
file_pat = os.path.join(download_dir)
print('downloaded:',os.path.exists(file_pat))




