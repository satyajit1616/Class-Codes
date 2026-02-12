from playwright.sync_api import sync_playwright
import time



with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("file:///C:/Users/Srs61/PycharmProjects/PythonProject/AT23/playwrightprac/other_locator.html")
    #get by role (tagname, text)
    submit = page.get_by_role( "button",name="submit")
    submit.click()
    # print(submit.text_content())
    # time.sleep(3)
    # browser.close()
    Username= page.get_by_label( "Username")
    Username.fill("Satyajit")
    time.sleep(2)
    Password= page.get_by_label( "Password")
    Password.fill("Sa23")
    time.sleep(2)
    Email=page.get_by_placeholder( "Enter your email")
    Email.fill("Satya@gmail.com")
    time.sleep(2)
    Search=page.get_by_placeholder( "Search here")
    Search.fill("AT23")
    time.sleep(2)
    submit=page.get_by_role( "button",name="Login")
    submit.click()
    print(submit.text_content())

    Text1=page.get_by_text("Click here to learn Playwright").is_visible()
    print(Text1)
    text2=page.get_by_text(" Accept Terms and Conditions")
    text2.click()
    time.sleep(3)
    browser.close()

