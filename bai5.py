# Bài 5: Thống kê số lượng sinh viên theo lớp

students = [
    {"name": "An", "class": "Python01"},
    {"name": "Bình", "class": "Python02"},
    {"name": "Chi", "class": "Python01"},
    {"name": "Dũng", "class": "Python03"},
    {"name": "Hà", "class": "Python02"}
]

# Thống kê sinh viên theo lớp
tk_lop = {}

for i in range(len(students)):
    t_lop = students[i]["class"]
    if t_lop in tk_lop:
        tk_lop[t_lop] = tk_lop[t_lop] + 1
    else:
        tk_lop[t_lop] = 1

# In kết quả
print("Thống kê sinh viên theo lớp:")
print(tk_lop)

print("")
for t_lop in tk_lop:
    print(t_lop + ": " + str(tk_lop[t_lop]) + " sinh viên")
