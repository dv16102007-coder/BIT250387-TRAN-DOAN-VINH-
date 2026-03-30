def bai_1():
    so = float(input("nhap so"))
    if so >= 0:
        phan_du = so % 2
        print(phan_du)
    else:
        raise ValueError("phải nhập số lớn hơn 0")

def bai_2():
    chuoi = input("nhập chuỗi")
    print("độ dài chuỗi = ", len(chuoi))
    print("chuỗi in hoa", chuoi.upper())

def bai_3():
    tong = 0
    i = 1
    print("các số lẻ:")
    while i <= 30:
        if i % 2 == 1:
            print(i)
            tong = tong + i
        i += 1
    print("tổng các số lẻ =", tong)

def bai_4():
    def tinh_tong(n):
        tong = 0
        for i in range(1, n + 1):
            tong = tong + i
        return tong

    print(tinh_tong(2))

def bai_5():
    class Flower:
        def __init__(self, color):
            self.__color = color

        def get_color(self):
            return self.__color

        def set_color(self, color):
            self.__color = color

    flower = Flower("Red")
    print(flower.get_color())
    flower.set_color("Blue")
    print(flower.get_color())

def bai_6():
    def selection_sort(arr):
        for i in range(len(arr)):
            min_idx = i
            for j in range(i + 1, len(arr)):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        return arr
    danh_sach = [2, 35, 234, 3, 4, 5]
    print(selection_sort(danh_sach))
bai_1()
bai_2()
bai_3()
bai_4()
bai_5()
bai_6()
