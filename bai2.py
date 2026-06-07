# Bài 2: Tìm sản phẩm theo tên
products = [
    {"name": "Laptop", "price": 15000000},
    {"name": "Mouse", "price": 200000},
    {"name": "Keyboard", "price": 500000}
]

while True:
    # Nhập tên sản phẩm
    t_sp = input("Nhập tên sản phẩm (hoặc 'thoát' để dừng): ")
    
    if t_sp == "thoát":
        print("Thoát chương trình")
        break  
    # Tìm sản phẩm
    tm = False
    for i in range(len(products)):
        if products[i]["name"] == t_sp:
            print("Giá của " + products[i]["name"] + ": " + str(products[i]["price"]) + " đồng")
            tm = True
    
    if tm == False:
        print("Không tìm thấy")
