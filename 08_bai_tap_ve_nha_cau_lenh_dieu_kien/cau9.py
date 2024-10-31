# 9. Tính cước tacxi: 
# Viết chương trình tính cước taxi theo biểu phí cơ bản như sau:
# -	Loại xe 4 chỗ
#   Giá mở cửa			11.000 đồng/0.8km
#   Trong phạm vi 20km 	12.100đ/km
#   Từ km thứ 21 trở đi 		10.000 đồng/km
# -	Loại  xe 7 chỗ
#   Giá mở cửa			13.000 đồng/0.8km
#   Trong phạm vi 30km 	14.100đ/km
#   Từ km thứ 31 trở đi 		12.000 đồng/km
# Tiền chờ: 05 phút đầu được miễn phí, từ phút thứ sáu trở đi là 800đ/phút.
# Loại xe chỉ nhập 4 hoặc 7.
# Hàm tính cước taxi
# Hàm tính cước taxi
def calculate_taxi_fare(car_type, distance, waiting_time):
    if car_type == 4:
        # Xe 4 chỗ
        opening_price = 11000
        rate_within_limit = 12100
        rate_beyond_limit = 10000
        limit_km = 20
        opening_distance = 0.8
    elif car_type == 7:
        # Xe 7 chỗ
        opening_price = 13000
        rate_within_limit = 14100
        rate_beyond_limit = 12000
        limit_km = 30
        opening_distance = 0.8
    else:
        return "Loại xe không hợp lệ, vui lòng nhập 4 hoặc 7."

    # Tính phí di chuyển theo km
    if distance <= opening_distance:
        fare = opening_price
    elif distance <= limit_km:
        fare = opening_price + (distance - opening_distance) * rate_within_limit
    else:
        fare = (opening_price +
                (limit_km - opening_distance) * rate_within_limit +
                (distance - limit_km) * rate_beyond_limit)

    # Tính phí chờ
    waiting_fare = 0
    if waiting_time > 5:
        waiting_fare = (waiting_time - 5) * 800

    # Tổng cước
    total_fare = fare + waiting_fare
    return total_fare

# Nhập thông tin từ người dùng
car_type = int(input("Nhập loại xe (4 hoặc 7): "))
distance = float(input("Nhập quãng đường đã đi (km): "))
waiting_time = int(input("Nhập thời gian chờ (phút): "))

# Tính cước và hiển thị kết quả
fare = calculate_taxi_fare(car_type, distance, waiting_time)
if isinstance(fare, str):
    print(fare)
else:
    print(f"Cước taxi của bạn là: {fare} đồng")

