from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time


driver = webdriver.Chrome()


def test_droppable():
    driver.get("https://demoqa.com/droppable")
    driver.find_element(By.ID, "droppableExample-tab-accept").click()
    button = driver.find_element(By.ID, "acceptable")
    basket = driver.find_element(By.CSS_SELECTOR, "#acceptDropContainer #droppable")
    action = ActionChains(driver)
    action.drag_and_drop(button, basket).perform()
    time.sleep(1)
    result_text = basket.text
    assert "Dropped!" in result_text, f"Text after dropping is not as expected: {result_text}"
    print(f"Result is '{result_text}'.")


if __name__ == "__main__":
    test_droppable()
    driver.quit()
