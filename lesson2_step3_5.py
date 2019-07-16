import math
import time 

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
  
from selenium import webdriver
  
link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)

button = browser.find_element_by_css_selector("button.btn")
button.click()

time.sleep(1)

new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

x_element = browser.find_element_by_id('input_value').text
y = calc(x_element)

# Ваш код, который заполняет обязательные поля
input1 = browser.find_element_by_id('answer')
input1.send_keys(y)

button1 = browser.find_element_by_css_selector("button.btn")
button1.click()
