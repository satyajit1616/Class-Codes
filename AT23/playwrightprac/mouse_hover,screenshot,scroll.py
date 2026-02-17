import time
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")

    # hover_btn = page.locator("#mousehover")
    # hover_btn.scroll_into_view_if_needed()
    # hover_btn.hover()
    # time.sleep(2)
    # print(page.locator("a[href='#top']").text_content())
    # page.click("a[href='#top']")
    # time.sleep(3)
    #
    #
    # #screenshot
    # page.screenshot(path=r"C:\Users\Srs61\PycharmProjects\PythonProject\Screenshot\full_page.png",full_page=True)
    #SCROLL DOWN & UP
    #WAY 1
    # page.mouse.wheel(0,1000)
    #WAY 2
    # page.evaluate("window.scrollTo(0,1000)")
    page.evaluate("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(2)
    page.mouse.wheel(0,-1000)
    time.sleep(5)
    browser.close()