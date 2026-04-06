def count_vowels(s):
    count = 0
    vowels = "aeiou"

    for char in s.lower():
        if char in vowels:
            count += 1

    return count


# Test
text = input("Nhập chuỗi: ")
print("Số nguyên âm là:", count_vowels(text))