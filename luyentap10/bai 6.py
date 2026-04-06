    s = input("Nhập chuỗi: ")
    result = ""

    for i in range(len(s)-1, -1, -1):
        result += s[i]

    print("Chuỗi đảo:", result)