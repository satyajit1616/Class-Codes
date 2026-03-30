from  playwright.sync_api import sync_playwright
import time
import json
url = "https://rahulshettyacademy.com/AutomationPractice/"
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(url)
    expected_instructor = "Rahul_Shetty"
    expected_sum = 0

    #web table on this page i typically
    table = page.locator("(//table[@id='product'])[1]")
    rows = table.locator("tr")
    row_count = rows.count()
    print(row_count)



    # for i in range(1,row_count):
    #     # print(i)
    #     row = rows.nth(i)
    #     print(row.text_content())
    #     cols = row.locator("td")
    #     print(cols.count())
    #     #if not a proper date row
    #     if cols.count()<3:
    #         continue
    #     instructor = cols.nth(0).inner_text().strip()
    #     price = cols.nth(2).inner_text().strip()
    # for j in  range(11):
    #     if expected_instructor == instructor:
    #         print(j,'pass')
    #     else:
    #         print(j,'fail')







    time.sleep(3)
    browser.close()
