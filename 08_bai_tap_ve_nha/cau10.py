# 10. Viết chương trình nhập lương nhân viên, tính thuế thu nhập và lương ròng (số tiền
# lương thực sự mà nhân viên đó nhận được).
# Với các thông số giả sử như sau
# • 30% thuế thu nhập nếu lương là 15 triệu.
# • 20% thuế thu nhập nếu lương từ 7 đến 15 triệu.
# • 10% thuế thu nhập nếu lương dưới 7 triệu.
# Hàm tính thuế thu nhập và lương ròng
def calculate_net_salary(salary):
    if salary > 15000000:
        tax_rate = 0.30
    elif salary >= 7000000:
        tax_rate = 0.20
    else:
        tax_rate = 0.10

    # Tính thuế thu nhập
    tax = salary * tax_rate

    # Tính lương ròng
    net_salary = salary - tax

    return tax, net_salary

# Nhập lương từ người dùng
salary = float(input("Nhập lương của nhân viên (đồng): "))

# Tính thuế và lương ròng
tax, net_salary = calculate_net_salary(salary)

# In kết quả
print(f"Thuế thu nhập phải nộp: {tax:,.0f} đồng")
print(f"Lương ròng (số tiền thực sự nhận được): {net_salary:,.0f} đồng")
