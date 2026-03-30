from playwright.sync_api import sync_playwright,expect
from json_handel_in_python import return_test_data

url = 'https://rahulshettyacademy.com/AutomationPractice/'
expecetd_web_instrctor = []
expeceted_web_course = []
expeected_web_price_text = []

test_data = return_test_data()

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(url)

    table = page.locator("(//table[@id='product'])[1]")
    rows = table.locator("tr")
    rows_count = rows.count()

    web_table_data = {}

    for i in range(1,rows_count):
        cols = rows.nth(i).locator("td")
        if cols.count()<3:
            continue

        expecetd_web_instrctor.append(cols.nth(0).inner_text().strip())
        expeceted_web_course.append(cols.nth(1).inner_text().strip())
        expeected_web_price_text.append(cols.nth(2).inner_text().strip())


    # print(expecetd_web_instrctor)
    # print(expeceted_web_course)
    # print(expeected_web_price_text)


    #instrctor validation
    '''for idx,value in enumerate(test_data):
        if idx==0:
            for j in expecetd_web_instrctor:
                assert j == value,f'{j} == {value} both are not match'
    '''

    #web course validation
    actaul_course = []
    for i in test_data[1]:
        actaul_course.append(i['course_name'])

    assert len(expeceted_web_course) == len(actaul_course)

    for i in range(len(expeceted_web_course)):
        assert expeceted_web_course[i] == actaul_course[i], f'{expeceted_web_course[i]} != {actaul_course[i]}'
    browser.close()

