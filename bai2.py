# Bài 2: Tìm sản phẩm theo tên

products = [
    {"name": "Laptop", "price": 15000000},
    {"name": "Mouse", "price": 200000},
    {"name": "Keyboard", "price": 500000}
]

while True:
    # Nhập tên sản phẩm
    ten_san_pham = input("Nhập tên sản phẩm (hoặc 'thoát' để dừng): ")
    
    if ten_san_pham == "thoát":
        print("Thoát chương trình")
        break
    
    # Tìm sản phẩm
    tim_thay = False
    for i in range(len(products)):
        if products[i]["name"] == ten_san_pham:
            print("Giá của " + products[i]["name"] + ": " + str(products[i]["price"]) + " đồng")
            tim_thay = True
    
    if tim_thay == False:
        print("Không tìm thấy")
