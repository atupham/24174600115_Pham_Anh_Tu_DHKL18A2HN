# 2. Viết chương trình kiểm tra xem điểm M(x,y) có nằm trong hình tròn tâm I(a,b) và bán kính 
# R bằng cách xuất ra giá trị True nếu điểm M nằm trong hoặc trên hình tròn và False nếu nằm ngoài hình tròn, 
# với x, y, a, b, R nhập vào từ bàn phím?    
import math
x = float(input("Nhập tọa độ x của điểm M: "))
y = float(input("Nhập tọa độ y của điểm M: "))
a = float(input("Nhập tọa độ a của tâm I: "))
b = float(input("Nhập tọa độ b của tâm I: "))
R = float(input("Nhập bán kính R của hìn tròn: "))
khoang_cach = math.sqrt((x - a) ** 2 + (y - b) ** 2)
if khoang_cach <= R:
    print("True")
else:
    print("false")

     

