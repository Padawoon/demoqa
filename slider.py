from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()


def test_slider():
    driver.get("https://demoqa.com/slider")
    slider = driver.find_element(By.CLASS_NAME, "range-slider")
    slider_width = slider.size['width']
    target_position = slider_width * 0.8
    action = ActionChains(driver)
    action.click_and_hold(slider).move_by_offset(target_position - (slider_width / 2), 0).release().perform()
    final_value = int(slider.get_attribute("value"))
    print(f"Slider value set to: {final_value}")
    assert 70 <= final_value <= 99, f"Final value {final_value} is not in the range 70-99"


if __name__ == "__main__":
    test_slider()
    driver.quit()
