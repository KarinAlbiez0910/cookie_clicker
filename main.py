from selenium import webdriver
from time import time
chrome_driver_path = "C:/Users/49176/Pyrhon London/cookie-clicker-project/chromedriver.exe"

time_over = time() + 5
# 60 secs * 35
thirty_five_mins = time() + 2100

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element_by_css_selector("#cookie")

while time() < thirty_five_mins:
      cookie.click()
      if time() > time_over:
          available_cookies = driver.find_element_by_css_selector("#money").text
          store_elements = driver.find_elements_by_css_selector("#store b")
          store_elements = {item.text.strip().split(" - ")[0]: int(item.text.strip().split(" - ")[-1].replace(",", ""))\
                            for item in store_elements[0:-1]}
          sorted_store_elements = dict(sorted(store_elements.items(), key=lambda item: item[1], reverse=True))
          for key, value in sorted_store_elements.items():
              if int(available_cookies.replace(",","")) >= value:
                  driver.find_element_by_id("buy"+key).click()
                  time_over = time() + 5
                  break


