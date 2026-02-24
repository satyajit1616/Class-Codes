from playwright.sync_api import sync_playwright
from json_handel_in_python import return_test_data

url = "https://rahulshettyacademy.com/AutomationPractice/"

test_data = return_test_data()
expected_courses = test_data["courses"]   # assuming JSON is dictionary based

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(url)

    rows = page.locator("(//table[@id='product'])[1]//tr")
    rows_count = rows.count()

    # Validate row count (excluding header)
    assert rows_count - 1 == len(expected_courses), \
        "Mismatch in number of courses"

    # Single pass validation
    for i in range(1, rows_count):
        cols = rows.nth(i).locator("td")

        if cols.count() < 3:
            continue

        web_instructor = cols.nth(0).inner_text().strip()
        web_course = cols.nth(1).inner_text().strip()
        web_price = cols.nth(2).inner_text().strip()

        expected_course = expected_courses[i - 1]

        assert web_instructor == test_data["instructor"], \
            f"Instructor mismatch: {web_instructor}"

        assert web_course == expected_course["course_name"], \
            f"Course mismatch: {web_course}"

        assert web_price == str(expected_course["price"]), \
            f"Price mismatch: {web_price}"

    browser.close()