# Bài 6: Quản lý kho hàng

inventory = [
    {"id": 1, "name": "Laptop", "quantity": 5},
    {"id": 2, "name": "Mouse", "quantity": 20},
    {"id": 3, "name": "Keyboard", "quantity": 10}
]

while True:
    print("\n=== MENU QUẢN LÝ KHO HÀNG ===")
    print("1. Xem danh sách kho hàng")
    print("2. Thêm sản phẩm mới")
    print("3. Cập nhật số lượng sản phẩm")
    print("4. Xóa sản phẩm")
    print("5. Thoát")
    
    ch = input("Chọn chức năng (1-5): ")
    
    match ch:
        case "1":
            print("\n=== Danh sách kho hàng ===")
            for i in range(len(inventory)):
                print("ID: " + str(inventory[i]["id"]) + ", Sản phẩm: " + inventory[i]["name"] + ", Số lượng: " + str(inventory[i]["quantity"]))
        
        case "2":
            print("\n--- Thêm sản phẩm mới ---")
            t_m = input("Nhập tên sản phẩm: ")
            sl_m = int(input("Nhập số lượng: "))
            id_m = len(inventory) + 1
            inventory.append({"id": id_m, "name": t_m, "quantity": sl_m})
            print("Thêm thành công!")
        
        case "3":
            print("\n--- Cập nhật số lượng ---")
            id_cn = int(input("Nhập ID sản phẩm cần cập nhật: "))
            sl_cn = int(input("Nhập số lượng mới: "))
            tm = False
            for i in range(len(inventory)):
                if inventory[i]["id"] == id_cn:
                    inventory[i]["quantity"] = sl_cn
                    print("Cập nhật thành công!")
                    tm = True
            if tm == False:
                print("Không tìm thấy sản phẩm với ID này")
        
        case "4":
            print("\n--- Xóa sản phẩm ---")
            id_x = int(input("Nhập ID sản phẩm cần xóa: "))
            tm = False
            for i in range(len(inventory)):
                if inventory[i]["id"] == id_x:
                    inventory.pop(i)
                    print("Xóa thành công!")
                    tm = True
                    break
            if tm == False:
                print("Không tìm thấy sản phẩm với ID này")
        
        case "5":
            print("Thoát chương trình")
            break
        
        case _:
            print("Lựa chọn không hợp lệ")
