from playwright.sync_api import sync_playwright
import time


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page() # open a new page/tab in ur recommnede browser

    #open a link and hit in api and call the url
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")

    time.sleep(2)

    #wait for new window
    with context.expect_page() as new_page_info:
        page.locator("#opentab").click()


    new_page = new_page_info.value
    new_page.wait_for_load_state()

    print(new_page.title())

    course = new_page.locator("(//a[text()='Courses'])[1]")
    course.click()
    print(new_page.locator("//div[text()='959,200']").text_content())

    time.sleep(2)

    new_page.close()
    browser.close()