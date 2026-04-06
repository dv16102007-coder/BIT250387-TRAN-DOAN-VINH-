diem_1 = float(input("Nhập điểm môn 1"))
diem_2 = float(input("Nhập điểm môn 2"))
diem_3 = float(input("Nhập điểm môn 3"))
diem_tb = (diem_1 + diem_2 + diem_3)/3
if diem_tb >= 8:
    print("Xếp loại giỏi")
elif diem_tb >= 6.5 and diem_tb <= 7.9:
    print("Xếp loại khá")
elif diem_tb >= 5.0 and diem_tb <= 6.4:
    print("Xếp loại trung bình")
if diem_tb < 5:
    print("Xếp loai yếu")
    