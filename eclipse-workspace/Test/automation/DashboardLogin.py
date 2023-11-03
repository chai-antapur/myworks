from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import psycopg2
import bcrypt
from selenium.common.exceptions import NoSuchElementException


def login():
    chrome_driver_path = 'C:/Users/chaitra.antapur/Desktop/chaitra/chromedriver-win64 (1)/chromedriver-win64/chromedriver.exe'

    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service)

    url = "http://localhost:3000/login"
    driver.get(url)
    driver.maximize_window()

# get values from user to enter in the fields
    actual_name = input("Enter a username value")
    actual_pwd = input("Enter a password value") 


    time.sleep(5)
    driver.find_element(By.XPATH, "//input[@name='email']").send_keys(actual_name)
    driver.find_element(By.XPATH, "//input[@name='password']").send_keys(actual_pwd)
    username = actual_name
    password = actual_pwd
    
    time.sleep(10)

    db_params = {
        "host": "localhost",
        "user": "postgres",
        "password": "12345678",
        "database": "BestEx_Users",
        "port": 5432,
        }

# Establish a connection to the PostgreSQL database
    conn = psycopg2.connect(**db_params)    
    cursor = conn.cursor()

# Execute a query to retrieve the salted and hashed password for the specified user
    query = f"SELECT salted_hash_of_password FROM websocket_authentication_details WHERE email_id = %s and is_active = true"
    cursor.execute(query, (username,))
    result = cursor.fetchone()

    if result:
        stored_password_hash = result[0]
        user_input_password = password.encode('utf-8')
        
    # Verify the user's input password against the stored hash
        if bcrypt.checkpw(user_input_password, stored_password_hash.encode('utf-8')):
        # password correct      
            query1 = f"SELECT permissions_json FROM websocket_permissions_details where email_id = %s"
            cursor.execute(query1, (username,))
            rows = cursor.fetchall()
        
        # Check for the keys present in Db for password verified user
            unique_keys = set()
            for row in rows:
                json_data = row[0]
                if json_data:
                    unique_keys.update(json_data.keys())
            unique_keys_list = list(unique_keys)
        
            values_to_check = ["data_permissions", "permit_actions"]
            for value in values_to_check:
                if value in unique_keys_list:
                    try:
                        driver.find_element(By.XPATH, "//button[text()='Login']").click()
                        time.sleep(3)
                    except NoSuchElementException:
                        print(" ")
                else:
                    driver.close()
        else:
            print("wrong pass")
            driver.find_element(By.XPATH, "//button[text()='Login']").click()
            time.sleep(5)
    else:
        print("user details not found")
        driver.find_element(By.XPATH, "//button[text()='Login']").click()
        time.sleep(3)

    cursor.close()
    conn.close()

    if "Wrong email or password." in driver.page_source:
        print("Wrong pass or username. Retry with correct login creds")
        driver.refresh()
    else:
        print("Login successful")
    time.sleep(10)

    driver.close()
