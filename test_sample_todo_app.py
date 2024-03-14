from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import json
import time
url = os.getenv("LT_HUB_URL")
capabilities = {
    "build" : os.getenv("LT_BUILD_NAME"),
    "name" : "Quick Test",
    "platform" : "Windows 10",
    "browserName" : "Chrome",
    "version" : "88.0",
    "resolution" : "1920x1080",
    "tunnel" : False
}
driver = webdriver.Remote(
    desired_capabilities= capabilities,
    command_executor= url
)
driver.get("https://www.crestliner.com/")
time.sleep(2)
driver.find_element_by_id("modalCloseBtn").click()

//driver.find_element(By.LINK_TEXT, "Deep").click()
time.sleep(2)

driver.find_element(By.LINK_TEXT, "Bass/Bay").click()
time.sleep(2)

driver.find_element(By.LINK_TEXT, "Hunt/Utility").click()
time.sleep(2)

driver.quit()
#driver.get("https://sreiker.github.io/sample-todo-app.io/")
#driver.find_element_by_name("li3").click()

#textbox = driver.find_element_by_id("sampletodotext")
#textbox.send_keys("Testing")
#driver.find_element_by_id("addbutton").click()
#assert "No results found." not in driver.page_source
#driver.execute_script("lambda-status=passed")
#driver.quit()
