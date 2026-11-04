# BÁO CÁO KIỂM THỬ TỰ ĐỘNG

## Testcase 1: Kiểm tra trạng thái mặc định của trang Dropdown

### Mục đích
Xác nhận rằng khi vừa truy cập trang `/dropdown`, danh sách xổ xuống có chứa các tùy chọn (options), đồng thời tùy chọn đầu tiên (tùy chọn mặc định) không được phép chọn lại (disabled).

### Các bước thực hiện
1. Truy cập URL: [https://the-internet.herokuapp.com/dropdown](https://the-internet.herokuapp.com/dropdown).
2. Tìm element là thẻ `<select>` chứa dropdown.
3. Khởi tạo đối tượng `Select`.
4. Kiểm tra tổng số lượng các tùy chọn (options) trong dropdown.
5. Lấy tùy chọn đang được hiển thị mặc định bằng thuộc tính `first_selected_option`.
6. Kiểm tra xem tùy chọn mặc định có bị vô hiệu hóa hay không bằng phương thức `is_enabled()`.

### Kết quả mong đợi
- Dropdown có tổng cộng 3 tùy chọn.
- Tùy chọn mặc định có text là `"Please select an option"`.
- Trạng thái `is_enabled()` của tùy chọn mặc định trả về `False`.

---

## Testcase 2: Kiểm tra thao tác chọn các giá trị trong Dropdown

### Mục đích
Xác nhận rằng người dùng có thể chọn các tùy chọn khác nhau trong dropdown bằng nhiều phương thức khác nhau, bao gồm `visible text`, `value` và `index`.

### Các bước thực hiện
1. Truy cập URL: [https://the-internet.herokuapp.com/dropdown](https://the-internet.herokuapp.com/dropdown).
2. Khởi tạo đối tượng `Select` cho dropdown.
3. Chọn `"Option 1"` bằng thuộc tính `value` thông qua phương thức `select_by_value()`. Kiểm tra xem `"Option 1"` đã được chọn hay chưa.
4. Chọn `"Option 2"` bằng text hiển thị thông qua phương thức `select_by_visible_text()`. Kiểm tra xem `"Option 2"` đã được chọn hay chưa.
5. Trở lại `"Option 1"` bằng vị trí `index` thông qua phương thức `select_by_index()`. Kiểm tra kết quả sau khi chọn.

### Kết quả mong đợi
- Giá trị của `first_selected_option` thay đổi chính xác theo từng thao tác chọn.
- Các tùy chọn `"Option 1"` và `"Option 2"` được chọn thành công bằng các phương thức tương ứng.

---

## Testcase 3: Kiểm tra trạng thái và thao tác click của trang Checkboxes

### Mục đích
Xác nhận trạng thái mặc định của các checkbox và kiểm tra chức năng tick/bỏ tick khi người dùng thực hiện thao tác click chuột.

### Các bước thực hiện
1. Truy cập URL: [https://the-internet.herokuapp.com/checkboxes](https://the-internet.herokuapp.com/checkboxes).
2. Tìm tất cả các ô checkbox trên màn hình bằng cách sử dụng `find_elements()` kết hợp với `By.CSS_SELECTOR`.
3. Kiểm tra thuộc tính của element để đảm bảo element được tìm thấy là checkbox bằng phương thức `get_attribute()`.
4. Kiểm tra trạng thái mặc định của các checkbox bằng phương thức `is_selected()`:
   - Checkbox 1 chưa được tick.
   - Checkbox 2 đã được tick.
5. Thực hiện hành động `click()` vào Checkbox 1 và kiểm tra lại trạng thái để xác nhận checkbox đã được tick.
6. Thực hiện hành động `click()` vào Checkbox 2 và kiểm tra lại trạng thái để xác nhận checkbox đã được bỏ tick.

### Kết quả mong đợi
- Checkbox 1 mặc định chưa được tick.
- Checkbox 2 mặc định đã được tick.
- Sau khi thực hiện `click()` vào Checkbox 1, trạng thái chuyển từ chưa tick sang đã tick.
- Sau khi thực hiện `click()` vào Checkbox 2, trạng thái chuyển từ đã tick sang chưa tick.
- Trạng thái của mỗi checkbox thay đổi ngược lại so với trạng thái ban đầu sau khi thực hiện hàm `click()`.
    