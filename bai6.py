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
    
    choice = input("Chọn chức năng (1-5): ")
    
    match choice:
        case "1":
            print("\n=== Danh sách kho hàng ===")
            for i in range(len(inventory)):
                print("ID: " + str(inventory[i]["id"]) + ", Sản phẩm: " + inventory[i]["name"] + ", Số lượng: " + str(inventory[i]["quantity"]))
        
        case "2":
            print("\n--- Thêm sản phẩm mới ---")
            ten_san_pham_moi = input("Nhập tên sản phẩm: ")
            so_luong_moi = int(input("Nhập số lượng: "))
            id_moi = len(inventory) + 1
            inventory.append({"id": id_moi, "name": ten_san_pham_moi, "quantity": so_luong_moi})
            print("Thêm thành công!")
        
        case "3":
            print("\n--- Cập nhật số lượng ---")
            id_cap_nhat = int(input("Nhập ID sản phẩm cần cập nhật: "))
            so_luong_cap_nhat = int(input("Nhập số lượng mới: "))
            tim_thay = False
            for i in range(len(inventory)):
                if inventory[i]["id"] == id_cap_nhat:
                    inventory[i]["quantity"] = so_luong_cap_nhat
                    print("Cập nhật thành công!")
                    tim_thay = True
            if tim_thay == False:
                print("Không tìm thấy sản phẩm với ID này")
        
        case "4":
            print("\n--- Xóa sản phẩm ---")
            id_xoa = int(input("Nhập ID sản phẩm cần xóa: "))
            tim_thay = False
            for i in range(len(inventory)):
                if inventory[i]["id"] == id_xoa:
                    inventory.pop(i)
                    print("Xóa thành công!")
                    tim_thay = True
                    break
            if tim_thay == False:
                print("Không tìm thấy sản phẩm với ID này")
        
        case "5":
            print("Thoát chương trình")
            break
        
        case _:
            print("Lựa chọn không hợp lệ")
