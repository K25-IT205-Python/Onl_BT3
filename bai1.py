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
td = 0
for i in range(len(students)):
    td = td + students[i]["score"]

dtb = td / len(students)
print("\nĐiểm trung bình lớp: " + str(dtb))

# Yêu cầu 3: In học sinh có điểm cao nhất
ms = students[0]["score"]
hs_cn = students[0]["name"]

for i in range(1, len(students)):
    if students[i]["score"] > ms:
        ms = students[i]["score"]
        hs_cn = students[i]["name"]

print("Học sinh có điểm cao nhất: " + hs_cn + " (" + str(ms) + " điểm)")
