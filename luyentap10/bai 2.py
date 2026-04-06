chuoi = input("Nhập chuỗi: ")
ky_tu = input("Nhập ký tự cần đếm: ")

dem = 0

for i in chuoi:
    if i == ky_tu:
        dem += 1

print("Số lần xuất hiện:", dem)