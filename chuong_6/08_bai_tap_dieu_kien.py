# 1. Tính năm nhuận. Năm thứ n là nhuận nếu nó chia hết cho 4, nhưng không chia hết cho 100 hoặc chia hết 400. 
a = int(input("Năm nay là năm :"))
if a % 4 == 0 and (a % 100 != 0 or a % 400 !=0):
    print (f"{a} là năm nhuận")
else:
    print (f"{a} không phải là năm nhuận") 
# 2. Viết chương trình kiểm tra xem điểm M(x,y) có nằm trong hình tròn tâm I(a,b) và bán kính 
# R bằng cách xuất ra giá trị True nếu điểm M nằm trong hoặc trên hình tròn và False nếu nằm ngoài hình tròn, 
# với x, y, a, b, R nhập vào từ bàn phím?    
a,b = map(input("Nhập tọa độ tâm I:"))
x,y = map(input("Nhập tọa độ điểm M bất kì nằm trên đường tròn:"))
R = float(input("Nhập bán kính R:"))

