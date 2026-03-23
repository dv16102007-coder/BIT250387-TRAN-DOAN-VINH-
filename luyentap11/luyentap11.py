def bai_1():
    a = []
    for i in range(5):
        s = input(f"Nhập chuỗi {i + 1}: ")
        a.append(s)
    for i in range(1, 5):
        key = a[i]
        j = i - 1
        while j >= 0 and len(a[j]) < len(key):
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
        print(f"Bước {i}: {a}")

def bai_2():
    a = []
    for i in range(5):
        s = input(f"Nhập chuỗi {i + 1}: ")
        a.append(s)
    for i in range(1, 5):
        key = a[i]
        j = i - 1
        while j >= 0 and len(a[j]) < len(key):
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
        print(f"Bước {i}: {a}")

    def binary_search_custom(arr, target):
        target_len = len(target)
        left = 0
        right = len(arr) - 1

        while left <= right:
            mid = (left + right) // 2
            mid_len = len(arr[mid])
            if mid_len == target_len:
                if arr[mid] == target:
                    return mid
                else:
                    temp = mid - 1
                    while temp >= left and len(arr[temp]) == target_len:
                        if arr[temp] == target: return temp
                        temp -= 1
                    temp = mid + 1
                    while temp <= right and len(arr[temp]) == target_len:
                        if arr[temp] == target: return temp
                        temp += 1
                    return -1
            elif mid_len < target_len:
                right = mid - 1
            else:
                left = mid + 1
        return -1

    # danh_sach_tu_bai_1 = ['chuoixyz', 'chuoi1', 'chuoi2', 'abc', 'ab']
    print(f"Mảng hiện tại (đã sắp xếp theo độ dài giảm dần): {a}")
    chuoi_can_tim = input("Nhập chuỗi bạn muốn tìm kiếm: ")
    vi_tri = binary_search_custom(a, chuoi_can_tim)
    if vi_tri != -1:
        print(f"-> Đã tìm thấy chuỗi '{chuoi_can_tim}' tại vị trí index: {vi_tri}")
    else:
        print(f"-> Không tìm thấy chuỗi '{chuoi_can_tim}' trong danh sách.")
def bai_3():
    ds_so = [1, 4, 2, 6, 9, 8, 7, 99, 26, 2, 4, 19, 0, 8]

    def tim_so_chan():
        tong = 0
        print("có số chẵn trong danh sách là : ")
        for i in ds_so:
            if i % 2 == 0:
                print(i)
                tong += i
        print("tổng của các số chẵn là : ", tong)

    tim_so_chan()

def bai_4():
    def kiem_tra_nguyen_to(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    danh_sach = [5, 12, 7, 5, 2, 19, 8]
    print(f"1. Danh sách ban đầu: {danh_sach}")
    phan_tu_moi = int(input("nhập phần tử mới thêm vào : "))
    danh_sach.append(phan_tu_moi)
    print(f"2. Danh sách sau khi thêm {phan_tu_moi}: {danh_sach}")
    try:
        k = int(input("\nNhập giá trị k cần đếm: "))
        so_lan = danh_sach.count(k)
        print(f"3. Số {k} xuất hiện {so_lan} lần trong danh sách.")
    except ValueError:
        print("Vui lòng nhập một số nguyên hợp lệ!")
    tong_nguyen_to = sum(so for so in danh_sach if kiem_tra_nguyen_to(so))
    print(f"\n4. Tổng các số nguyên tố trong danh sách là: {tong_nguyen_to}")
    danh_sach.sort()
    print(f"5. Danh sách sau khi sắp xếp tăng dần: {danh_sach}")
    danh_sach.clear()
    print(f"6. Danh sách sau khi xóa: {danh_sach}")

def bai_5():
    my_dict = {
        "ten": "Nguyễn Văn A",
        "tuoi": 20,
        "nganh_hoc": "Công nghệ thông tin",
        "diem_tb": 5
    }

    def kiem_tra_key(tu_dien, key_can_tim):
        if key_can_tim in tu_dien:
            print(f"V Key '{key_can_tim}' CÓ tồn tại. Giá trị của nó là: {tu_dien[key_can_tim]}")
        else:
            print(f"X Key '{key_can_tim}' KHÔNG tồn tại trong dictionary.")

    print("Danh sách dictionary hiện tại:", my_dict)
    print("-" * 40)
    kiem_tra_key(my_dict, "tuoi")
    kiem_tra_key(my_dict, "diem_tb")

def bai_6():
    danh_sach_nguoi = {}
    print("--- CHƯƠNG TRÌNH NHẬP VÀ TÍNH TUỔI TRUNG BÌNH ---")
    print("(Gõ 'stop' hoặc 'dung' ở phần nhập tên để kết thúc)\n")
    while True:
        ten = input("Nhập tên: ")
        if ten.lower() in ['stop', 'dung']:
            break
        try:
            tuoi = int(input(f"Nhập tuổi của {ten}: "))
            danh_sach_nguoi[ten] = tuoi
            print(f"Đã thêm: {ten} - {tuoi} tuổi.\n")
        except ValueError:
            print("X Lỗi: Tuổi phải là một số nguyên. Vui lòng nhập lại!\n")
    print("-" * 40)
    if danh_sach_nguoi:
        print(f"Danh sách thông tin đã nhập: {danh_sach_nguoi}")
        tong_tuoi = sum(danh_sach_nguoi.values())
        so_luong = len(danh_sach_nguoi)
        tuoi_trung_binh = tong_tuoi / so_luong
        print(f"V Tuổi trung bình của {so_luong} người là: {tuoi_trung_binh:.2f}")
    else:
        print("Bạn chưa nhập thông tin nào!")


def bai_7():
    import csv
    def main():
        print("--- NHẬP THÔNG TIN NHÂN VIÊN ---")
        ten = input("Nhập tên nhân viên: ")
        tuoi = input("Nhập tuổi: ")
        id_nv = input("Nhập ID nhân viên: ")
        txt_filename = "nhan_vien.txt"
        csv_filename = "nhan_vien.csv"
        with open(txt_filename, "w", encoding="utf-8") as f_txt:
            f_txt.write(f"ID: {id_nv} | Tên: {ten} | Tuổi: {tuoi}")
        print(f"Đã lưu thành công vào: {txt_filename}")
        with open(csv_filename, "w", newline='', encoding="utf-8-sig") as f_csv:
            writer = csv.writer(f_csv)
            writer.writerow(["ID", "Tên", "Tuổi"])
            writer.writerow([id_nv, ten, tuoi])
        print(f"Đã lưu thành công vào: {csv_filename}")
        print("--- XEM TRƯỚC NỘI DUNG FILE TEXT ---")
        with open(txt_filename, "r", encoding="utf-8") as f_txt:
            print(f_txt.read())
        print("--- XEM TRƯỚC NỘI DUNG FILE CSV ---")
        with open(csv_filename, "r", encoding="utf-8") as f_csv:
            print(f_csv.read())

    main()

def bai_8():
    thong_tin_sinh_vien = ("Trần Doãn Vinh", 19, 9)
    ten, tuoi, diem_tb = thong_tin_sinh_vien
    print("--- THÔNG TIN SINH VIÊN ---")
    print(f"Tên: {ten}")
    print(f"Tuổi: {tuoi}")
    print(f"Điểm trung bình: {diem_tb}")

def bai_9():
    def nhap_ma_tran(hang, cot, ten):
        ma_tran = []
        print(f"Nhập ma trận {ten}:")
        for i in range(hang):
            dong = []
            for j in range(cot):
                while True:
                    gia_tri = input(f"Phần tử [{i}][{j}]: ")
                    if gia_tri.strip() == "":
                        print("Lỗi: Không được để trống! Vui lòng nhập lại.")
                        continue
                    try:
                        dong.append(float(gia_tri))
                        break
                    except ValueError:
                        print("Lỗi: Phải nhập số! Vui lòng nhập lại.")
            ma_tran.append(dong)
        return ma_tran

    def cong_ma_tran(A, B, hang, cot):
        C = []
        for i in range(hang):
            dong = []
            for j in range(cot):
                dong.append(A[i][j] + B[i][j])
            C.append(dong)
        return C

    def in_ma_tran(M):
        for dong in M:
            print("\t".join(map(str, dong)))

    while True:
        try:
            hang = int(input("Nhập số hàng: "))
            cot = int(input("Nhập số cột: "))
            break
        except ValueError:
            print("Lỗi: Phải nhập số nguyên!")
    A = nhap_ma_tran(hang, cot, "A")
    B = nhap_ma_tran(hang, cot, "B")
    C = cong_ma_tran(A, B, hang, cot)
    print("\nMa trận tổng:")
    in_ma_tran(C)