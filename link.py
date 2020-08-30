from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome('C:/Users/Karthik Naidu/Downloads/chromedriver')
browser.get('http://linkedin.com')
sleep(1)
browser.find_element_by_link_text('Sign in').click()
sleep(2)
browser.find_element_by_id('username').send_keys("heykarthiknaidu@gmail.com")
sleep(1)
browser.find_element_by_id('password').send_keys("python@1499")
sleep(1)
browser.find_element_by_xpath("//button[@type = 'submit']").click()
sleep(10)
browser.find_element_by_xpath("//input[@type = 'text']").send_keys('Ch Viharika')
browser.find_element_by_xpath("//input[@type = 'text']").send_keys(Keys.RETURN)
sleep(3)
browser.find_element_by_xpath("//button[text() = 'Message']").click()
message = 'Hi'
sleep(1)
browser.find_element_by_xpath("//div[@role = 'textbox']").send_keys(message)
sleep(1)
browser.find_element_by_xpath("//button[@type = 'submit']").click()
