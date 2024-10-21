#BÀI 1
r = float(input("Nhập bán kính r: "))
h = float(input("Nhập chiều cao h: "))
pi = 3.14
if r>0 and h>0:
    dien_tich_xung_quanh = round(2*pi*r*h,2)
    dien_tich_toan_phan = round(2*pi*r*(r+h),2)
    the_tich = round(pi*r**2*h,2)
    print(f"Diện tích xung quanh: {dien_tich_xung_quanh}")
    print(f"Diện tích toàn phần: {dien_tich_toan_phan}")
    print(f"Thể tích:{the_tich}")
else:
    print("Giá trị không thỏa mãn")
print("Kết thúc chương trình")       
#Bài 2
#Tử Số = -x + (x**2+4)**(1/2)
#Mẫu só = (x**4+1)**(1/7)
#f_x= (-x + (x**2+4)**(1/2))/((x**4+1)**(1/7))
x = float(input("Nhập giá trị của x: "))
f_x = round((-x + (x**2+4)**(1/2))/((x**4+1)**(1/7)),2)
print(f"Giá trị của f(x) = {f_x}")
#không có điều kiện vì x ở mẫu mũ chẵn
#Bài 4
# Nhập thời gian sử dụng bóng đèn (tính bằng giây)
time_seconds = float(input("Nhập thời gian sử dụng bóng đèn (giây): "))

# Các hằng số
voltage = 220  # Hiệu điện thế (V)
current = 2.7  # Cường độ dòng điện (A)
price_per_kwh = 7000  # Giá tiền điện (đ/kWh)

# Kiểm tra tính hợp lệ của thời gian
if time_seconds <= 0:
    print("Thời gian sử dụng phải lớn hơn 0.")
else:
    # Tính công suất tiêu thụ (P = U * I)
    power = voltage * current  # Công suất (W)

    # Tính năng lượng tiêu thụ (E = P * t)
    energy_wh = power * time_seconds / 3600  # Đổi từ giây sang giờ (Wh)
    energy_kwh = energy_wh / 1000  # Đổi từ Wh sang kWh

    # Tính tiền điện
    cost = energy_kwh * price_per_kwh

    # In ra kết quả
    print(f"Tiền điện phải trả: {cost:.2f} đ")

#Bài 8
import math
x = input("Nhap gia tri x: ")
x = float(x)
if x <= 0 or x == 1:
    print("Biểu thức không hợp lệ")
else:
    f_x = math.log(x, 4) + math.log(2, x)
    print(f"Gia tri can tim f(x) = {f_x:.2f}")

