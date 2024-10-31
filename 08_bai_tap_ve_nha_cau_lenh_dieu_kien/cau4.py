# 4. Viết chương trình nhập vào các số a, b, c, sau đó kiểm tra bộ ba số a, b, c vừa nhập vào 
# là bộ ba cạnh của tam giác thường, tam giác vuông, tam giác cân, tam giác vuông cân, tam giác đều 
# hay không phải là bộ ba cạnh của tam giác.
a = float(input("Nhập cạnh thứ nhất: "))
b = float(input("Nhập cạnh thứ hai: "))
c = float(input("Nhập cạnh thứ ba: "))
if a + b > c and a + c > b and b + c > a:
    print("Đây là bộ ba cạnh của tam giác.")
    if a == b == c:
        print("Đây là bộ ba cạnh của tam giác đều.")
    elif a == b or a == c or b == c:
        print("Đây là bộ ba của tam giác cân.")
    elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        print("Đây là bộ ba tam giác vuông.")
        if a == b or a == c or b == c:
            print("Đây là tam giác vuông cân.")
    else:
        print("Đây là tam giác thường.")
else:
    print("Đây không phải là bộ ba cạnh của tam giác.")                






    