from  playwright.sync_api import sync_playwright,expect
import time
url = "https://rahulshettyacademy.com/AutomationPractice/"
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(url)

    #web table on this page i typically
    table = page.locator("(//table[@id='product'])[1]")
    rows = table.locator("tr")
    row_count = rows.count()
    print(row_count)


    for i in range(0,row_count):
        # print(i)
        row = rows.nth(i)
        cols = row.locator("th")
        print(cols.count())
        # if cols.count() == 3:
        #     for i in range(co)

        # print(row.text_content())
        # if i == 0:
        #     col_th = row.locator("th")
        #     print(col_th.text_content())
        # else:
        #     break



    time.sleep(3)
    browser.close()
