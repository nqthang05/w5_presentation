import pytest  
import time  
from selenium import webdriver  
from selenium.webdriver.common.by import By  # Import By để xác định phương thức tìm kiếm phần tử trên trang web
from selenium.webdriver.support.ui import Select  # Import Select để thao tác với các phần tử HTML dạng dropdown <select>

@pytest.fixture  # Đánh dấu hàm driver() là fixture của pytest, cho phép các testcase sử dụng lại trình duyệt được khởi tạo
def driver():
    # Khởi tạo trình duyệt Chrome
    driver = webdriver.Chrome()  # Tạo đối tượng WebDriver và mở một cửa sổ trình duyệt Chrome
    driver.maximize_window()  # Phóng to cửa sổ trình duyệt để hiển thị trang web trên diện tích lớn nhất
    driver.implicitly_wait(5)  # Thiết lập thời gian chờ ngầm tối đa 5 giây khi Selenium tìm kiếm phần tử
    yield driver  # Trả đối tượng driver cho testcase sử dụng; phần code phía sau yield sẽ chạy sau khi testcase kết thúc
     # Giữ trình duyệt mở cho đến khi người dùng nhấn Enter
    input("\nNhấn Enter để đóng trình duyệt...")  # Tạm dừng chương trình và chờ người dùng nhấn Enter trong terminal
    driver.quit()  # Đóng trình duyệt Chrome và giải phóng tài nguyên WebDriver


def test_dropdown_default_state(driver):
    """Testcase 1: Kiểm tra trạng thái mặc định của Dropdown"""
    driver.get("https://the-internet.herokuapp.com/dropdown")  # Truy cập trang web chứa dropdown cần kiểm thử

    dropdown_element = driver.find_element(By.ID, "dropdown")  # Tìm phần tử dropdown thông qua thuộc tính HTML id="dropdown"
    select_obj = Select(dropdown_element)  # Chuyển phần tử dropdown thành đối tượng Select để sử dụng các phương thức thao tác dropdown

    assert len(select_obj.options) == 3  # Kiểm tra dropdown có đúng 3 lựa chọn; nếu điều kiện sai, testcase sẽ thất bại
    default_option = select_obj.first_selected_option  # Lấy đối tượng option đang được chọn mặc định trong dropdown

    assert default_option.text == "Please select an option"  # Kiểm tra nội dung hiển thị của option mặc định đúng với văn bản mong đợi
    assert default_option.is_enabled() is False  # Kiểm tra option mặc định đang bị vô hiệu hóa, không thể chọn như một lựa chọn thông thường

    # In ra terminal khi testcase pass hết các lệnh assert ở trên
    print("\n[PASS] Testcase 1: Kiểm tra trạng thái mặc định của Dropdown thành công!")  # In thông báo thành công nếu tất cả các lệnh assert phía trên đều vượt qua


def test_dropdown_selection_methods(driver):
    """Testcase 2: Kiểm tra thao tác chọn các giá trị trong Dropdown"""
    driver.get("https://the-internet.herokuapp.com/dropdown")  # Truy cập trang web chứa dropdown cần kiểm thử

    dropdown_element = driver.find_element(By.ID, "dropdown")  # Tìm phần tử dropdown theo id="dropdown"
    select_obj = Select(dropdown_element)  # Tạo đối tượng Select để thao tác chọn các option trong dropdown

    # Chọn Option 1 và dừng 1.5 giây để quan sát
    select_obj.select_by_value("1")  # Chọn option có thuộc tính HTML value="1"
    assert select_obj.first_selected_option.text == "Option 1"  # Kiểm tra option đang được chọn có nội dung "Option 1"
    time.sleep(1.5)  # Tạm dừng chương trình 1.5 giây để người kiểm thử quan sát kết quả chọn

    # Chọn Option 2 và dừng 1.5 giây để quan sát
    select_obj.select_by_visible_text("Option 2")  # Chọn option dựa trên nội dung văn bản hiển thị là "Option 2"
    assert select_obj.first_selected_option.text == "Option 2"  # Kiểm tra option đang được chọn có nội dung "Option 2"
    time.sleep(1.5)  # Tạm dừng chương trình 1.5 giây để quan sát trạng thái dropdown

    # Chọn lại Option 1 bằng index và dừng 1.5 giây để quan sát
    select_obj.select_by_index(1)  # Chọn option theo chỉ số index; index bắt đầu từ 0 nên index=1 tương ứng option thứ hai trong danh sách
    assert select_obj.first_selected_option.text == "Option 1"  # Kiểm tra option được chọn theo index có nội dung "Option 1"
    time.sleep(1.5)  # Tạm dừng chương trình 1.5 giây để quan sát kết quả chọn

    print("\n[PASS] Testcase 2: Kiểm tra thao tác chọn các giá trị trong Dropdown thành công!")  # In thông báo thành công nếu tất cả các lệnh assert phía trên đều vượt qua


def test_checkboxes_toggle(driver):
    """Testcase 3: Kiểm tra trạng thái và thao tác click của trang Checkboxes"""
    driver.get("https://the-internet.herokuapp.com/checkboxes")  # Truy cập trang web chứa các checkbox cần kiểm thử

    checkboxes = driver.find_elements(By.CSS_SELECTOR, "form#checkboxes input")  # Tìm tất cả phần tử input bên trong form có id="checkboxes" bằng CSS Selector
    assert len(checkboxes) == 2  # Kiểm tra trang có đúng 2 phần tử checkbox được tìm thấy

    cb1 = checkboxes[0]  # Gán phần tử checkbox đầu tiên trong danh sách vào biến cb1
    cb2 = checkboxes[1]  # Gán phần tử checkbox thứ hai trong danh sách vào biến cb2

    assert cb1.get_attribute("type") == "checkbox"  # Kiểm tra thuộc tính type của phần tử cb1 có giá trị "checkbox"
    assert cb2.get_attribute("type") == "checkbox"  # Kiểm tra thuộc tính type của phần tử cb2 có giá trị "checkbox"

    assert cb1.is_selected() is False  # Kiểm tra Checkbox 1 ban đầu chưa được tick
    assert cb2.is_selected() is True  # Kiểm tra Checkbox 2 ban đầu đã được tick

    # Dừng 1.5 giây để nhìn trạng thái chưa click
    time.sleep(1.5)  # Tạm dừng chương trình 1.5 giây để quan sát trạng thái ban đầu của hai checkbox

    # Click Checkbox 1 và dừng 1.5 giây để quan sát nó được tick
    cb1.click()  # Thực hiện thao tác click vào Checkbox 1 để chuyển trạng thái từ chưa tick sang đã tick
    assert cb1.is_selected() is True  # Kiểm tra Checkbox 1 đã được tick sau thao tác click
    time.sleep(1.5)  # Tạm dừng chương trình 1.5 giây để quan sát Checkbox 1 sau khi được tick

    # Click Checkbox 2 và dừng 1.5 giây để quan sát nó bị bỏ tick
    cb2.click()  # Thực hiện thao tác click vào Checkbox 2 để chuyển trạng thái từ đã tick sang chưa tick
    assert cb2.is_selected() is False  # Kiểm tra Checkbox 2 đã bị bỏ tick sau thao tác click
    time.sleep(1.5)  # Tạm dừng chương trình 1.5 giây để quan sát Checkbox 2 sau khi bị bỏ tick

    print("\n[PASS] Testcase 3: Kiểm tra trạng thái và thao tác click Checkboxes thành công!")  # In thông báo thành công nếu tất cả các lệnh assert phía trên đều vượt qua


if __name__ == "__main__":  
    pytest.main(["-v", "-s", "test_internet_herokuapp.py"])  # Khởi chạy pytest; -v hiển thị tên từng testcase, -s hiển thị output print() và chỉ định file chứa testcase