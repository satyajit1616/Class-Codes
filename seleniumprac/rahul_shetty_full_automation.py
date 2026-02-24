from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
time.sleep(2)

wait = WebDriverWait(driver, 15)

input_box = driver.find_element(By.ID,"name")
input_box.send_keys("Satyajit")
time.sleep(2)

driver.find_element(By.ID,"alertbtn").click()
wait.until(EC.alert_is_present()).accept()
time.sleep(2)

driver.find_element(By.ID,"name").send_keys("Satyajit")
driver.find_element(By.ID,"confirmbtn").click()
wait.until(EC.alert_is_present()).accept()
time.sleep(2)

checkboxes = driver.find_elements(By.CSS_SELECTOR,"input[type='checkbox']")
for checkbox in checkboxes:
    checkbox.click()
time.sleep(2)

driver.find_element(By.XPATH,"//option[text()='Option1']").click()
time.sleep(2)

driver.find_element(By.ID,"autocomplete").send_keys("us")
time.sleep(2)
suggested_country = driver.find_elements(By.XPATH,"//li[@class='ui-menu-item']/div")

for i in suggested_country:
    if "Austria" == i.text:
        print(i.text)
        i.click()
time.sleep(2)

driver.find_element(By.XPATH,"//input[@value='radio1']").click()
time.sleep(2)

driver.find_element(By.ID,"displayed-text").send_keys("Satyajit")
time.sleep(1)
driver.find_element(By.ID,"hide-textbox").click()
time.sleep(1)
driver.find_element(By.ID,"show-textbox").click()

parent_w1 = driver.current_window_handle
old_handles = driver.window_handles

driver.find_element(By.ID,"openwindow").click()

wait.until(EC.new_window_is_opened(old_handles))

t_window = driver.window_handles
for window5 in t_window:
    if window5 != parent_w1:
        driver.switch_to.window(window5)
        break

driver.find_element(By.XPATH,"(//a[text()='Courses'])[1]").click()
time.sleep(2)

driver.close()
driver.switch_to.window(parent_w1)
time.sleep(2)


parent_w2 = driver.current_window_handle
all_window = driver.window_handles

driver.find_element(By.ID,"opentab").click()

wait.until(EC.new_window_is_opened(all_window))

s_window = driver.window_handles
for window4 in s_window:
    if window4 != parent_w2:
        driver.switch_to.window(window4)
        break

driver.find_element(By.XPATH,"(//a[text()='Courses'])[1]").click()
time.sleep(2)

driver.close()
driver.switch_to.window(parent_w2)
time.sleep(2)

driver.execute_script("window.scrollBy(0,500);")
mouse_hover = driver.find_element(By.ID,"mousehover")
action = ActionChains(driver)
action.move_to_element(mouse_hover).perform()
time.sleep(3)
top = driver.find_element(By.LINK_TEXT,"Top")
top.click()
print(top.is_enabled())
time.sleep(3)
driver.execute_script("window.scrollBy(0,1200);")
time.sleep(3)
driver.switch_to.frame("courses-iframe")
driver.find_element(By.XPATH,"(//a[text()='Learning paths'])[1]").click()
driver.switch_to.default_content()
time.sleep(3)

driver.execute_script("window.scrollBy(0,-1200);")

home = driver.find_element(By.XPATH, "//button[text()='Home']")
home.click()
time.sleep(3)


parent_w3 = driver.current_window_handle

driver.find_element(By.XPATH, "//a[text()='Sign Up']").click()
time.sleep(3)
all_windows = driver.window_handles
for window in all_windows:
    if window != parent_w3:
        driver.switch_to.window(window)
        break

driver.find_element(By.ID, "name").send_keys("Satya")
driver.find_element(By.ID,"email").send_keys("sks@gmail.com")
check_click = driver.find_element(By.XPATH,"//div[text()='I agree to receive promotional and instructional emails from Rahul Shetty Academy School']")
check_click.click()
send_code = driver.find_element(By.XPATH,"//span[text()='Send code']")
send_code.click()
time.sleep(4)
driver.quit()