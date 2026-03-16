def bai_tap1 ():
 a = 10
 b = 4
 z = (a ** 2 + b ** 2)
 c = (a - b)
 m = z / c
 print(m)


def bai_tap2 ():
 import math
 x = int(input("Nhập số thứ nhất"))
 y = int(input("Nhập số thứ hai"))
 print("Lũy thừa:",x**y)
 print("Căn bậc 2 của x:", math.sqrt(x))
 print("Chia lấy phần dư:",x//y)


def bai_tap3 ():
 n=int(input("Nhập số từ 1 đến 9:"))
 if 1 <= n <= 9:
  for i in range(1,10):
   print(n, "x", i, "=", n*i)
 else:
  print("Số không hợp lệ")


def bai_tap4 ():
 for i in range(1,101):
  if i % 3 == 0:
   print(i)


def bai_tap8 ():
 diem = float(input("Nhập điểm sinh viên"))
 if 0 <= diem <= 10:
  print("Điểm hợp lệ")
 else:
  print("Điểm không hợp lệ")


def bai_tap7 ():
 class Student:
  def __init__(self, ten, diem):
   self.ten = ten
   self.diem = diem
 sv1= Student("Vinh",10)
 sv2= Student("Minh",0)
 print(sv1.ten, sv1.diem)
 print(sv2.ten, sv2.diem)


def bai_tap9 ():
  class Student:
      def __init__(self, ten, diem):
        self.ten = ten
        self.diem = diem
      def display(self):
        print("Sinh viên", self.ten, "có điểm là", self.diem)
  sv1 = Student ("A",10)
  sv2 = Student ("B",8)

  sv1.display()
  sv2.display()


