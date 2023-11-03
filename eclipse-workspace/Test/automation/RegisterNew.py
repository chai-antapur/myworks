from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import psycopg2

chrome_driver_path = 'C:/Users/chaitra.antapur/Desktop/chaitra/chromedriver-win64 (1)/chromedriver-win64/chromedriver.exe'

service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

url = "http://localhost:3000/login"
driver.get(url)

fname,lname,org,email,pwd,repwd = input()

# Registering new client
driver.find_element(By.XPATH, "//button[text()='Register Now!']").click()
driver.find_element(By.NAME, "firstName").send_keys(fname)
driver.find_element(By.NAME,"lastName").send_keys(lname)
driver.find_element(By.NAME, "organisation").send.keys(org)
driver.find_element(By.NAME, "email").send.keys(email)
driver.find_element(By.NAME, "password").send.keys(pwd)
driver.find_element(By.NAME, "rePassword").send.keys(repwd)