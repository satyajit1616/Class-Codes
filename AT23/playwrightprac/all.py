from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()  # open a new page/tab in ur recommended browser

    #open a link and hit in api and call the url
    page.goto(r"file:///C:/Users/Srs61/PycharmProjects/PythonProject/AT23/playwrightprac/webpage.html")
    #print the title in playwright
    print(page.title())

    #form of input box
    first_name = page.locator("#fname")
    first_name.fill("satya")

    page.fill("#lname",'Prakash')
    page.fill("#email","satya@test.com")

    #radio button
    page.locator("input[name='gender']").nth(0).click()
    # page.locator("//input[@name='gender'][2]").click() # xpath 

    page.fill("#mobile","9876543210")

    page.fill("input[type='date']","1977-03-01")

    page.set_input_files("input[type='file']",r"C:\Users\Srs61\PycharmProjects\PythonProject\AT23\playwrightprac\webpage.html")

    page.select_option("select",label='Russia')

    # page.fill( "#countrySearch", "us")
    # #press thing using keyboard
    # page.keyboard.press("ArrowDown")
    # page.keyboard.press("Enter")


    time.sleep(10)

    browser.close()