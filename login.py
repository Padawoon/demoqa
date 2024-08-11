from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()


def test_login():
    driver.get("https://demoqa.com/login")

    credentials = [
        ("admin", "admin"),
        ("test", "test"),
        ("user", "password"),
        ("Testuser0227", "TestPassword0227#")
    ]

    results = []

    for username, password in credentials:
        driver.find_element(By.ID, "userName").clear()
        driver.find_element(By.ID, "password").clear()
        driver.find_element(By.ID, "userName").send_keys(username)
        driver.find_element(By.ID, "password").send_keys(password)
        driver.find_element(By.ID, "login").click()
        time.sleep(1)
        if "Invalid username or password!" in driver.page_source:
            results.append((username, password, "Login Failed"))
        else:
            results.append((username, password, "Login Successful"))
        driver.get("https://demoqa.com/login")

    for result in results:
        print(f"Username: {result[0]}, Password: {result[1]} - {result[2]}")


if __name__ == "__main__":
    test_login()
    driver.quit()
