from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("file:///C:/Users/Srs61/PycharmProjects/PythonProject/seleniumprac/class_auto_prac.html")
time.sleep(2)
title = driver.find_element(By.XPATH,"//h2")
print(title.text)
driver.find_element(By.ID,"name").send_keys("Satya")
rd_btn = driver.find_element(By.ID,"male")
rd_btn.click()
checkboxes = driver.find_elements(By.CSS_SELECTOR,"input[type='checkbox']")
for checkbox in checkboxes:
    checkbox.click()
country = driver.find_element(By.XPATH,"//select[@id='country']")
dp_down = Select(country)
dp_down.select_by_index(2)
auto_suggest = driver.find_element(By.ID,"country_suggest")
auto_suggest.send_keys("us")

all_suggested_country = driver.find_elements(By.XPATH,"//ul[@id='suggestions']/li")

for i in all_suggested_country:
    if "Australia" == i.text:
        print(i.text)
        i.click()
driver.find_element(By.ID,"dob").send_keys("13-02-2026")
time.sleep(1)
make_my_trip = driver.find_element(By.XPATH,"(//div[text()='6'])[1]")
make_my_trip.click()
file_path = r"C:\Users\Srs61\Documents\4TH SEM FEE.pdf"

file_u = driver.find_element(By.ID,"fileUpload")
file_u.send_keys(file_path)

# new_tab = driver.find_element(By.XPATH,"//button[text()='Open New Tab']")
# new_tab.click()
# print(new_tab.is_enabled())
#
# new_window = driver.find_element(By.XPATH,"//button[text()='Open New Window']")
# new_window.click()
# print(new_window.is_enabled())


driver.find_element(By.XPATH,"//button[text()='Alert']").click()
wait1 = WebDriverWait(driver, 5)
alert1 = wait1.until(EC.alert_is_present())
print(alert1.text)
alert1.accept()

driver.find_element(By.XPATH,"//button[text()='Confirm']").click()
wait2= WebDriverWait(driver, 5)
alert2= wait2.until(EC.alert_is_present())
print(alert2.text)
alert2.accept()

driver.find_element(By.XPATH,"//button[text()='Prompt']").click()
wait5 = WebDriverWait(driver,3)
alert3 = wait5.until(EC.alert_is_present())
print(alert3.text)
alert3.accept()


hover = driver.find_element(By.XPATH,"//section[@class='hover-box']")
# driver.execute_script('window.scrollBy(0,1000);')
# time.sleep(2)
action = ActionChains(driver)
action.move_to_element(hover).perform()
opt_1 = driver.find_element(By.XPATH,"//button[text()='Option 1']")
opt_1.click()
print(opt_1.text)

double_click = driver.find_element(By.XPATH,"//button[text()='Double Click Me']")
act2 = ActionChains(driver)
act2.double_click(double_click).perform()
wait3 = WebDriverWait(driver,5)
double_click = wait3.until(EC.alert_is_present())
double_click.accept()

# driver.switch_to.frame(driver.find_element(By.XPATH,"(//section)[13]"))
# time.sleep(3)
source = driver.find_element(By.ID,"drag")
target = driver.find_element(By.ID,"drop")
act3 = ActionChains(driver)
act3.drag_and_drop(source,target).perform()
time.sleep(10)
print(source,target)
# driver.switch_to.default_content()

r_click = driver.find_element(By.ID,"rightClickBox")
act5 = ActionChains(driver)
act5.context_click(r_click).perform()
# edit = driver.find_element(By.XPATH,"//button[text()='Edit']")
driver.find_element(By.ID,"contextMenu")
driver.find_element(By.XPATH,"//button[text()='Edit']").click()
wait6 = WebDriverWait(driver,5)
alert5 = wait6.until(EC.alert_is_present())
alert5.accept()




driver.switch_to.frame("frame1")
inside_btn = driver.find_element(By.ID,"btn1")
inside_btn.click()
print(inside_btn.is_enabled())
time.sleep(2)
driver.switch_to.default_content()

text_box1 = driver.find_element(By.ID,"keyboardField1")
text_box1.send_keys("Satyajit")
text_box1.send_keys(Keys.CONTROL+"a")
text_box1.send_keys(Keys.CONTROL+"c")
text_box2 = driver.find_element(By.ID,"keyboardField2")
text_box2.send_keys(Keys.CONTROL+"v")

submit = driver.find_element(By.XPATH,"//button[text()='Submit']")
submit.click()
res = driver.find_element(By.ID,"result")
print(res.text)

time.sleep(3)
driver.quit()