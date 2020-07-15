from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(executable_path='C:/Users/Abdulrahman Abdul/Desktop/chromedriver')
driver.get("https://cas.rutgers.edu/login?service=https%3A%2F%2Fsims.rutgers.edu%2Fwebreg%2Fj_spring_cas_security_check%3Bjsessionid%3DCBB63456C1800BFE973E41E7B5806ACE.zdirect1-tc8")
#signing into sakai
elem = driver.find_element_by_name("username")
elem.clear()
#Sign in with username
elem.send_keys("")
elem.send_keys(Keys.TAB)
elem = driver.find_element_by_name("password")
elem.clear()
#Sign in with password
elem.send_keys("")
elem.send_keys(Keys.ENTER)
#choosing the semester
driver.find_element_by_id("semesterSelection3").click()
elem = driver.find_element_by_name("submit")
elem.send_keys(Keys.ENTER)
#Input index number
elem = driver.find_element_by_name("coursesToAdd[0].courseIndex")
elem.clear()
elem.send_keys("00011")

elem = driver.find_element_by_name("coursesToAdd[1].courseIndex")
elem.clear()
elem.send_keys("00283")

elem = driver.find_element_by_name("coursesToAdd[2].courseIndex")
elem.clear()
elem.send_keys("02769")

elem = driver.find_element_by_name("coursesToAdd[3].courseIndex")
elem.clear()
elem.send_keys("02770")

elem = driver.find_element_by_name("coursesToAdd[4].courseIndex")
elem.clear()
elem.send_keys("02774")

while True :
    driver.find_element_by_id("submit").click()
    time.sleep(15)
#no classes found
    if driver.find_element_by_name("operations[4].specialPermissionNumber") == None :
        driver.close()
    if ("WebReg | Additional Input" == driver.title) :
        driver.find_element_by_xpath("//input[@value='Cancel']").click()
        continue
    driver.close()


#driver.close()
