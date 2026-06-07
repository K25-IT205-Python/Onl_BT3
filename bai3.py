# Bài 3: Lọc học sinh đạt yêu cầu

students = [
    {"name": "An", "score": 8.5},
    {"name": "Bình", "score": 6.0},
    {"name": "Chi", "score": 9.0},
    {"name": "Dũng", "score": 5.5}
]

# Tạo list mới chứa các học sinh có điểm từ 8.0 trở lên
passed_students = []
for i in range(len(students)):
    if students[i]["score"] >= 8.0:
        passed_students.append(students[i])

# In danh sách
print("Học sinh có điểm từ 8.0 trở lên:")
for i in range(len(passed_students)):
    print(passed_students[i]["name"] + ": " + str(passed_students[i]["score"]) + " điểm")

print("\nTổng số học sinh đạt yêu cầu: " + str(len(passed_students)))
