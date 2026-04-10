def bai_1():
    def thong_ke_tuple(so_nguyen_tuple):
        tong = sum(so_nguyen_tuple)
        lon_nhat = max(so_nguyen_tuple)
        nho_nhat = min(so_nguyen_tuple)
        return tong, lon_nhat, nho_nhat

    my_tuple = (10, 25, -5, 40, 15)
    tong, max_val, min_val = thong_ke_tuple(my_tuple)
    print(f" Tuple: {my_tuple}")
    print(f"Tổng: {tong}, Lớn nhất: {max_val}, Nhỏ nhất: {min_val}\n")

def bai_2():
    def tinh_diem_trung_binh(danh_sach_sv):
        if not danh_sach_sv:
            return 0
        tong_diem = sum(danh_sach_sv.values())
        so_luong_sv = len(danh_sach_sv)
        return tong_diem / so_luong_sv

    sinh_vien = {"An": 8.5, "Bình": 9.0, "Châu": 7.5}
    diem_tb = tinh_diem_trung_binh(sinh_vien)
    print("Danh sách điểm:", sinh_vien)
    print(f"Điểm trung bình của lớp: {diem_tb:.2f}\n")

def bai_3():
    def kiem_tra_key(tu_dien, key_can_tim):
        if key_can_tim in tu_dien:
            print(f"Key '{key_can_tim}' CÓ tồn tại trong dictionary.")
        else:
            print(f"Key '{key_can_tim}' KHÔNG tồn tại trong dictionary.")

    my_dict = {"name": "Python", "year": 1991, "creator": "Guido van Rossum"}
    print(my_dict)
    kiem_tra_key(my_dict, "name")
    kiem_tra_key(my_dict, "version")
    print()

def bai_4():
    class Hoa:
        def __init__(self, ten, mau):
            self.ten = ten
            self.mau = mau

        def __str__(self):
            return f"Hoa {self.ten} có màu {self.mau}"

    hoa_hong = Hoa("Hồng", "Đỏ thắm")
    print(hoa_hong)
    print()

def bai_5():
    class Hoa:
        def __init__(self, ten, mau):
            self.ten = ten
            self.mau = mau

        def __str__(self):
            return f"Hoa {self.ten} có màu {self.mau}"

    hoa_hong = Hoa("Hồng", "Đỏ thắm")
    print(hoa_hong)
    print()
