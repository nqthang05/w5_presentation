import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

@pytest.fixture
def driver():
    # Khởi tạo trình duyệt Chrome
    driver = webdriver.Chrome() 
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    # Dừng thêm 2 giây trước khi đóng hẳn trình duyệt để bạn nhìn kết quả cuối
    time.sleep(5)
    driver.quit()

def test_dropdown_default_state(driver):
    """Testcase 1: Kiểm tra trạng thái mặc định của Dropdown"""
    driver.get("https://the-internet.herokuapp.com/dropdown")
    
    dropdown_element = driver.find_element(By.ID, "dropdown")
    select_obj = Select(dropdown_element)
    
    assert len(select_obj.options) == 3
    default_option = select_obj.first_selected_option
    
    assert default_option.text == "Please select an option"
    assert default_option.is_enabled() is False
    
    # Delay 2 giây để quan sát màn hình mặc định
    time.sleep(2)
    
    # In ra terminal khi testcase pass hết các lệnh assert ở trên
    print("\n[PASS] Testcase 1: Kiểm tra trạng thái mặc định của Dropdown thành công!")


def test_dropdown_selection_methods(driver):
    """Testcase 2: Kiểm tra thao tác chọn các giá trị trong Dropdown"""
    driver.get("https://the-internet.herokuapp.com/dropdown")
    
    dropdown_element = driver.find_element(By.ID, "dropdown")
    select_obj = Select(dropdown_element)
    
    # Chọn Option 1 và dừng 1.5 giây để quan sát
    select_obj.select_by_value("1")
    assert select_obj.first_selected_option.text == "Option 1"
    time.sleep(1.5)
    
    # Chọn Option 2 và dừng 1.5 giây để quan sát
    select_obj.select_by_visible_text("Option 2")
    assert select_obj.first_selected_option.text == "Option 2"
    time.sleep(1.5)
    
    # Chọn lại Option 1 bằng index và dừng 1.5 giây để quan sát
    select_obj.select_by_index(1)
    assert select_obj.first_selected_option.text == "Option 1"
    time.sleep(1.5)
    
    print("\n[PASS] Testcase 2: Kiểm tra thao tác chọn các giá trị trong Dropdown thành công!")


def test_checkboxes_toggle(driver):
    """Testcase 3: Kiểm tra trạng thái và thao tác click của trang Checkboxes"""
    driver.get("https://the-internet.herokuapp.com/checkboxes")
    
    checkboxes = driver.find_elements(By.CSS_SELECTOR, "form#checkboxes input")
    assert len(checkboxes) == 2
    
    cb1 = checkboxes[0]
    cb2 = checkboxes[1]
    
    assert cb1.get_attribute("type") == "checkbox"
    assert cb2.get_attribute("type") == "checkbox"
    
    assert cb1.is_selected() is False
    assert cb2.is_selected() is True
    
    # Dừng 1.5 giây để nhìn trạng thái chưa click
    time.sleep(1.5)
    
    # Click Checkbox 1 và dừng 1.5 giây để quan sát nó được tick
    cb1.click()
    assert cb1.is_selected() is True
    time.sleep(1.5)
    
    # Click Checkbox 2 và dừng 1.5 giây để quan sát nó bị bỏ tick
    cb2.click()
    assert cb2.is_selected() is False
    time.sleep(1.5)
    
    print("\n[PASS] Testcase 3: Kiểm tra trạng thái và thao tác click Checkboxes thành công!")


if __name__ == "__main__":
    pytest.main(["-v", "-s", "test_internet_herokuapp.py"])    