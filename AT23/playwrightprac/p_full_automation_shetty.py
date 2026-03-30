from playwright.sync_api import sync_playwright
import time
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    context = browser.new_context()
    url = "https://rahulshettyacademy.com/AutomationPractice/"
    page.goto(url)
    page.locator("input[value='radio2']").click()
    page.fill("#autocomplete","in")
    country_suggestion = page.locator("li[class='ui-menu-item'] div")
    time.sleep(3)
    count = country_suggestion.count()
    for country in range(count):
        print(country_suggestion.nth(country).inner_text())
        if "Benin" == country_suggestion.nth(country).inner_text():
            country_suggestion.nth(country).click()

    time.sleep(3)
    # page.locator("option[value='option2']").select_option("option2")
    dropdown = page.locator("#dropdown-class-example")
    dropdown.select_option("option2")
    checkboxes = page.locator("input[type='checkbox']")
    count = checkboxes.count()

    for i in range(count):
        checkboxes.nth(i).check()

    page.fill("#name","Satyajit")
    time.sleep(3)
    page.once("dialog",lambda dialog:(
        print("ALERT TEXT:-",dialog.message),
        dialog.accept()
    ))
    page.click("#alertbtn")
    page.fill("#name","Satyajit")
    page.once("dialog",lambda dialog:(
        print("ALERT CONFIRM TEXT:-",dialog.message),
        dialog.accept()
    ))
    page.click("#confirmbtn")
    time.sleep(4)
    with page.expect_popup() as new_page_info:
        page.locator("#openwindow").click()

    # new_page = new_page_info.value
    # new_page.wait_for_load_state()
    #
    # print('new_page.title()')
    # new_page.locator("(//a[text()='Contact'])[1]").click()
    # time.sleep(3)
    # new_page.fill("(//input[@type='text'])[2]","Satyajit")
    # time.sleep(2)
    # new_page.fill("input[type='email']","sks1616@outlook.com")
    # time.sleep(2)
    # new_page.fill("(//input[@type='text'])[3]","Automation")
    # new_page.fill("(//input[@type='text'])[4]","7856926630")
    # time.sleep(2)
    # new_page.get_by_placeholder("Messege").fill("Hi I want to join this course")
    # time.sleep(2)
    # new_page.locator("button[type='submit']").click()
    # new_page.close()
    # time.sleep(4)

    hover_btn = page.locator("#mousehover")
    hover_btn.scroll_into_view_if_needed()
    hover_btn.hover()
    time.sleep(2)
    print(page.locator("a[href='#top']").text_content())
    page.click("a[href='#top']")

    iframe = page.locator("#courses-iframe")
    iframe.scroll_into_view_if_needed()
    frame = page.frame_locator("#courses-iframe")
    frame.locator("(//a[text()='Mentorship'])[1]").click()
    heading = frame.locator("//h1").first
    print(heading.inner_text())
    time.sleep(3)




    time.sleep(3)
    browser.close()

