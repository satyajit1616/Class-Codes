from playwright.sync_api import sync_playwright
import  time
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("file:///C:/Users/Srs61/PycharmProjects/PythonProject/AT23/playwrightprac/xpath_prac.html")
    #1.using attribute (//tagname[@attribute='value'])

    username = page.locator("//input[@name='username']")
    username.fill("Satya1616")

    #2.using tagname (//tagname[text()='value'])

    login = page.locator("//button[text()='  Login   ']")
    login.click()
    print(login.text_content())

    password = page.locator("//input[@name='password']")
    password.fill("kanha@123")

    # otp = page.locator("//button[text()=' Login with OTP ']")
    # otp.click()
    # print(otp.text_content())

    #3.using conatins :- mostly doing the partial match. (//tagname[contains(@attribute/text(),'value')])
    # otp = page.locator("//button[contains(text(),'OTP ')]")
    # otp.click()
    # print(otp.text_content())

    para = page.locator("//section[contains(@id,'messages')]").is_visible()
    print(para)
    #4.using normalize-space :- remove the unauthorized space from the text (//tagname[normalize-space(text()='value')]
    otp = page.locator("//button[normalize-space()='Login']")
    otp.click()
    #5.start-with :- marching some first charcters, (//tagname[start-with(@attribute,'value')])
    # edit = page.locator("//a[starts-with(@href,'/edit')]")
    # edit.click()
    #6.and :- if both side condition should be True the locater hit on the DOM location
    #7.or :- atleast one them is correct.
    username = page.locator("//input[@ type = 'text' and @name ='username']")
    username = page.locator("//input[@ type = 'text' or @name ='khjkd']")

    #8.following-sibling " same hyrc up to down
    order = page.locator("//li[text()=' Order 1002 ']/following-sibling::li[2]").is_visible()
    print(order)
    #9.Preceding - Sibling
    order1 = page.locator("//li[text()=' Order 1004 ']/preceding-sibling::li[1]").is_visible()
    print(order1)
    #10. Parent
    order2= page.locator("//li[text()=' Order 1004 ']/parent::ul").is_visible()
    print(order2)
    #11. Child
    order3=page.locator("//section[@id='orders']/h2").is_visible()
    print(order3)

    #12.Ancestor
    order4= page.locator("//td[text()=' Alice ']/ancestor::tr/ancestor::tbody").is_visible()
    print(order4)




    time.sleep(3)









