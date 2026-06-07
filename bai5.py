# Bài 5: Thống kê số lượng sinh viên theo lớp

students = [
    {"name": "An", "class": "Python01"},
    {"name": "Bình", "class": "Python02"},
    {"name": "Chi", "class": "Python01"},
    {"name": "Dũng", "class": "Python03"},
    {"name": "Hà", "class": "Python02"}
]

# Thống kê sinh viên theo lớp
thong_ke_lop = {}

for i in range(len(students)):
    ten_lop = students[i]["class"]
    if ten_lop in thong_ke_lop:
        thong_ke_lop[ten_lop] = thong_ke_lop[ten_lop] + 1
    else:
        thong_ke_lop[ten_lop] = 1

# In kết quả
print("Thống kê sinh viên theo lớp:")
print(thong_ke_lop)

print("")
for ten_lop in thong_ke_lop:
    print(ten_lop + ": " + str(thong_ke_lop[ten_lop]) + " sinh viên")
