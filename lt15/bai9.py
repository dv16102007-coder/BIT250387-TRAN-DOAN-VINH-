text = input("Nhập chuỗi: ")

file = open("output.txt", "w", encoding="utf-8")
file.write(text)
file.close()

print("Đã lưu vào file")