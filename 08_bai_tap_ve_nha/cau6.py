# 6. Viết chương trình thể hiện menu lựa chọn gồm các thể loại phim hiện đang có trong rạp chiếu phim ABC. 
# Yêu cầu người dùng nhập lựa chọn thể loại phim muốn xem (Phim tình cảm, Phim kinh dị, Phim hoạt hình, Phim khoa học viễn tưởng)
print("Chào mừng đến rạp chiếu phim ABC!")
print("Xin vui lòng chọn thể loại phim bạn muốn xem:")
print("1. Phim tình cảm")
print("2. Phim kinh dị")
print("3. Phim hoạt hình")
print("4. Phim khoa học viễn tưởng")
print("0. Thoát")
lua_chon = input("Nhập số tương ứng với lựa chọn của bạn: ")
if lua_chon == '1':
    print ("Bạn đã chọn: Phim tình cảm")
elif lua_chon == '2':
    print ("Bạn đã chọn: Phim kinh dị")
elif lua_chon== '3':
    print("Bạn đã chọn: Phim hoạt hình")
elif lua_chon=='4':
    print("Bạn đã chọn: Phim khoa học viễn tưởng.")
elif lua_chon == '0':
    print("Cảm ơn bạn đã đến rạp chiếu phim ABC. Hẹn gặp lại!")
else :
    print("Lựa chọn không hợp lệ, vui lòng thử lại")


