can_nang = float(input("Nhập cân nặng:kg"))
chieu_cao = float(input("Nhập chiều cao:m"))
def tinh_bmi():
    bmi = (can_nang / chieu_cao**2)
    print(can_nang)
    print(chieu_cao)
    print(bmi)
tinh_bmi()