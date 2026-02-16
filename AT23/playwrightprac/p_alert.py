import time

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")

    time.sleep(3)
    page.fill("#name","Satya")
    #handle the alert
    page.once("dialog",lambda dialog:(
        print("ALERT TEXT:-",dialog.message),
        dialog.accept()
    ))
    page.click("#alertbtn")
    time.sleep(3)
    browser.close()