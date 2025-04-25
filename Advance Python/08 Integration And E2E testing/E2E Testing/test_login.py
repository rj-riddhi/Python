import os 
from selenium import webdriver 
from selenium.webdriver.common.by import By 
import time 


current_dir = os.path.dirname(os.path.abspath(__file__)) 
html_path = f"file://{os.path.join(current_dir, 'login.html')}" 
driver = webdriver.Chrome() 
driver.get(html_path) 

username_input = driver.find_element(By.ID, "username") 
password_input = driver.find_element(By.ID, "password") 
login_button = driver.find_element(By.ID, "login-btn") 

username_input.send_keys("admin") 
password_input.send_keys("1234") 

login_button.click() 
time.sleep(1) 

message = driver.find_element(By.ID, "message").text 
assert message == "Login Successful!" 
print("E2E Test Passed!") 
driver.quit() 
