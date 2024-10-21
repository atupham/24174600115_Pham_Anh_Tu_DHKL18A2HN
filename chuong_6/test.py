import math
x = input("Nhap gia tri x: ")
x = float(x)
if x <= 0 or x == 1:
    print("Biểu thức không hợp lệ")
else:
    f_x = math.log(x, 4) + math.log(2, x)
    print(f"Gia tri can tim f(x) = {f_x:.2f}")
