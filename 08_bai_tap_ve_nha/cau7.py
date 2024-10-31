# 7. Viết chương trình giải hệ phương trình 2 ẩn:
# 	    a_1*x + b_1*y = c_1
#       a_2*x + b_2*y = c_2
# Các hệ số a1, a2, b1, b2, c1, c2 nhập từ bàn phím. Xét tất cả các trường hợp cụ thể
# Công thức Cramer2 dùng tính hệ phương trình 2 ẩn
def cramer2(a1, b1, c1, a2, b2, c2):
    # Tính định thức D
    D = a1 * b2 - a2 * b1
    
    # Kiểm tra giá trị của D để xác định nghiệm
    if D == 0:
        # Tính Dx và Dy để kiểm tra khả năng vô số nghiệm
        Dx = c1 * b2 - c2 * b1
        Dy = a1 * c2 - a2 * c1
        if Dx == 0 and Dy == 0:
            return "Hệ phương trình có vô số nghiệm"
        else:
            return "Hệ phương trình vô nghiệm"
    else:
        # Nếu D khác 0, tính Dx và Dy
        Dx = c1 * b2 - c2 * b1
        Dy = a1 * c2 - a2 * c1
        
        # Tính nghiệm x và y
        x = Dx / D
        y = Dy / D
        return x, y

# Nhập hệ số từ bàn phím
a1 = float(input("Nhập hệ số a1: "))
b1 = float(input("Nhập hệ số b1: "))
c1 = float(input("Nhập hệ số c1: "))
a2 = float(input("Nhập hệ số a2: "))
b2 = float(input("Nhập hệ số b2: "))
c2 = float(input("Nhập hệ số c2: "))

# Giải hệ phương trình
result = cramer2(a1, b1, c1, a2, b2, c2)

# In kết quả
if isinstance(result, tuple):
    print("Nghiệm của hệ phương trình là:")
    print(f"x = {result[0]}")
    print(f"y = {result[1]}")
else:
    print(result)
