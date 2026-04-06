def giai_thua(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * giai_thua(n-1)

n = int(input("Nhập số: "))

print("Giai thừa là:", giai_thua(n))