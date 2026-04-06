students = {
    "An": 8,
    "Binh": 7,
    "Cuong": 9
}

# Hàm tính điểm trung bình
def average_score(students):
    total = sum(students.values())
    count = len(students)
    avg = total / count
    return avg
print("Điểm trung bình:", average_score(students))