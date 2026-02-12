from playwright.sync_api import sync_playwright
import time


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page() # open a new page/tab in ur recommended browser

    #open a link and hit in api and call the url
    page.goto(r"https://rahulshettyacademy.com/AutomationPractice/")

    page.fill("#autocomplete","us")

    elements = page.locator("li[class='ui-menu-item'] div")
    time.sleep(5)
    count = elements.count()


    for i in range(count):
        print(elements.nth(i).inner_text())
        if "Australia" == elements.nth(i).inner_text():
            elements.nth(i).click()


    time.sleep(5)
    page.close()