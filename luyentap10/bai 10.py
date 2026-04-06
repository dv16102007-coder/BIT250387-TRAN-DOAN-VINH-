arr = []

for i in range(5):
    s = input(f"Nhập chuỗi thứ {i + 1}: ")
    arr.append(s)

print("\nDanh sách ban đầu:", arr)

n = len(arr)

for i in range(n):
    print(f"\n--- Lượt {i + 1} ---")
    for j in range(0, n - i - 1):
        if len(arr[j]) < len(arr[j + 1]):
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            print("Hoán đổi:", arr)
        else:
            print("Giữ nguyên:", arr)

print("\nKết quả cuối cùng:", arr)