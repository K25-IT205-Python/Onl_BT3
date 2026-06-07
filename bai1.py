# Bài 1: List chứa nhiều Dictionary - Danh sách học sinh

students = [
    {"name": "An", "score": 8},
    {"name": "Bình", "score": 7},
    {"name": "Chi", "score": 9}
]

# Yêu cầu 1: In tên và điểm của từng học sinh
print("Danh sách học sinh:")
for i in range(len(students)):
    print(students[i]["name"] + ": " + str(students[i]["score"]) + " điểm")

# Yêu cầu 2: Tính điểm trung bình cả lớp
tong_diem = 0
for i in range(len(students)):
    tong_diem = tong_diem + students[i]["score"]

diem_trung_binh = tong_diem / len(students)
print("\nĐiểm trung bình lớp: " + str(diem_trung_binh))

# Yêu cầu 3: In học sinh có điểm cao nhất
max_score = students[0]["score"]
ten_hoc_sinh_cao_nhat = students[0]["name"]

for i in range(1, len(students)):
    if students[i]["score"] > max_score:
        max_score = students[i]["score"]
        ten_hoc_sinh_cao_nhat = students[i]["name"]

print("Học sinh có điểm cao nhất: " + ten_hoc_sinh_cao_nhat + " (" + str(max_score) + " điểm)")
