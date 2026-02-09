# import playwright's synchronous api
#sync_playwright() manage browser life cycle
from playwright.sync_api import sync_playwright
import time
#chromium launch
#headless= False --> browser visible
#with help of with statement open context manger of playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)

    page = browser.new_page()
    page.goto("https://www.facebook.com/login/")
    # open a link and hit in api and call the url


    email = page.locator("#email").fill("Satya@gmail.com") # open a new page/tab in ur chromium browser
    password = page.locator('#pass').fill("Satya@123")

    submit = page.locator("#loginbutton").click()

    time.sleep(5)

    browser.close() #