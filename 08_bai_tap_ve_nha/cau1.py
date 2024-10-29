# 1. Tính năm nhuận. Năm thứ n là nhuận nếu nó chia hết cho 4, nhưng không chia hết cho 100 hoặc chia hết 400. 
a = int(input("Năm nay là năm :"))
if a % 4 == 0 and (a % 100 != 0 or a % 400 !=0):
    print (f"{a} là năm nhuận")
else:
    print (f"{a} không phải là năm nhuận") 