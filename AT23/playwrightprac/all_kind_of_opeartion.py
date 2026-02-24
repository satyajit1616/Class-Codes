from playwright.sync_api import sync_playwright,expect

url = ''
with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    #url
    page.goto(url)


    #locater
    page.locator("css_selector or xpath")
    page.get_by_text()
    page.get_by_role()
    page.get_by_placeholder()
    page.get_by_label()
    page.get_by_test_id()
    page.get_by_title()
    page.get_by_alt_text()


    #mouse click
    #left click
    page.locator().click()

    #double click
    page.locator().dblclick()

    #right click
    page.locator().click(button='right')

    #middle click
    page.locator().click(button='middle')


    #click with Modifiers(CTRL/SHIFT)
    page.locator().click(modifiers=["Control"])
    page.locator().click(modifiers=["Shift"])

    #Force click(Ignore visibility issues)
    page.locator().click(force=True)


    #Mouse action :- Playwright gives full constrol over the mouse

    #Move Mouse
    page.mouse.move(x=0,y=100)

    #Mouse down
    page.mouse.down()

    #Mouse up
    page.mouse.up()

    #drag and drop
    page.drag_and_drop("#source","#target")

    #hover
    page.locator("#target").hover()


    #scroll using the mouse wheel
    #scroll down
    page.mouse.wheel(0,500)
    #scroll up
    page.mouse.wheel(0,-500)

    #scoll down or up if it is needed
    page.locator().scroll_into_view_if_needed()

    #scroll with help java scripts
    page.evaluate("js scripts")



    #Keyboard intraction

    #Type Text
    page.locator().fill()

    #Type slowly in text box
    page.locator().type("name",delay=100)

    #Clear Text
    page.locator().clear()


    #Press key
    page.keyboard.press("Enter")
    page.keyboard.press("Tab")
    page.keyboard.press("Control+A")

    #check box
    #check
    page.locator().check()

    #uncheck
    page.locator().uncheck()

    #Radio
    page.locator().check()

    #Dropdown intraction
    #Select by Value
    page.locator().select_option("Value")

    #select by label
    page.locator().select_option(label='label name')

    #select by Index
    page.locator().select_option(index=2)

    #How to upload a file
    page.locator().set_input_files("file_name")

    #Alert and Pop
    page.once("dialog",lambda dialog:dialog.accept())
    page.once("dialog",lambda dialog:dialog.dismiss())

    def dialog_handel(dialog):
        dialog = dialog.accept()
        page.locator("")

    page.once("dialog",dialog_handel)

    #Frame Handel
    frame = page.frame(name='')
    frame.locator().click()
    #or
    page.frame_locator().locator().click()


    #wait commands
    page.wait_for_selector()
    page.wait_for_timeout(50000)
    page.wait_for_load_state("locater")

    #assertion in playwright(Very Import QA)
    expect(page).to_have_title("Dashboard") #title assertion
    expect(page.locator()).to_have_text("OK") # text assertion
    expect(page.locator()).to_be_visible()
    expect(page.locator()).to_be_checked()
    expect(page.locator())
