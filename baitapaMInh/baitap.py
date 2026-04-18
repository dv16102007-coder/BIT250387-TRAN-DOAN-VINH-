def so_dao(n):
    so_ban_dau = int(input("Nhập số n"))
    if n < 0:
      n = -n
    while n > 0:
      digit = n % 10
       so_dao = so_dao * 10 + digit
      n = n // 10
      return so_ban_dau == so_dao
print(so_dao(1123)) #false
print(so_dao(-121)) #true
print(so_dao(121))  #true

def bai_2():
    n = int(input("Nhập n: "))

    s = 0
    for i in range(1, n + 1):
        s = s + i

    print(s)

def bai_3():
    a = int(input("Nhập số a: "))
    b = int(input("Nhập số b: "))

    so_lon_nhat = max(a, b)

    while True:
        if so_lon_nhat % a == 0 and so_lon_nhat % b == 0:
            print(so_lon_nhat)
            break
        so_lon_nhat = so_lon_nhat + 1