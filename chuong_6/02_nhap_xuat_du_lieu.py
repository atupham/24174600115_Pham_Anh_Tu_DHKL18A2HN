chuoi_ky_tu = input("Nhap chuoi ky tu: ") #(input luôn trả về kiểu dữ liệu là chuỗi ký tự)
#print("In ra man hinh: ", chuoi_ky_tu)
print (f"in ra man hinh chuoi ky tu{chuoi_ky_tu}")


gia_tri_nhap = input("yeu cau nhap vao so tu nhien: ")#mang kiểu ký tự
bien_so_nguyen = int(gia_tri_nhap)#ép kiểu số nguyên int
bien_so_thuc = float(gia_tri_nhap)#ép kiểu số thực float
bien_chuoi_ky_tu = str(gia_tri_nhap)#ép kiểu ký tự
bien_boolean = bool(gia_tri_nhap)#ép kiểu boolean
print(bien_boolean)# khi ép kiểu boolean cho kiểu ký tự luôn trả về True

bien_so_nguyen = int(input("yeu cau nhap vao so tu nhien: "))

bien_boolean = bool(int(input("yeu cau nhap vao so tu nhien: ")))
