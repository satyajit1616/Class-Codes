from playwright.sync_api import sync_playwright
import time


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page() # open a new page/tab in ur recommended browser

    page.goto(r"https://rahulshettyacademy.com/AutomationPractice/")

    iframe = page.locator("#courses-iframe")
    iframe.scroll_into_view_if_needed()
#intercact with inside frame
    frame = page.frame_locator("#courses-iframe")
    frame.locator("(//a[text()='Courses'])[1]").click()
    time.sleep(3)
    print(frame.locator("//h2[text()='Browse products']").inner_text())

    page.locator("#name").fill("Satyajit")

    time.sleep(3)
    browser.close()