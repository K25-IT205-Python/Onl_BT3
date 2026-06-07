# Bài 4: Tính tổng tiền giỏ hàng

cart = [
    {"name": "Sách", "price": 50000, "quantity": 2},
    {"name": "Bút", "price": 5000, "quantity": 10},
    {"name": "Vở", "price": 12000, "quantity": 5}
]

# Tính tổng tiền từng sản phẩm và tổng tiền giỏ
print("Chi tiết giỏ hàng:")
tong_tien_gio = 0

for i in range(len(cart)):
    tien_tung_san_pham = cart[i]["price"] * cart[i]["quantity"]
    print(cart[i]["name"] + ": " + str(cart[i]["price"]) + " x " + str(cart[i]["quantity"]) + " = " + str(tien_tung_san_pham) + " đồng")
    tong_tien_gio = tong_tien_gio + tien_tung_san_pham

print("\nTổng tiền giỏ hàng: " + str(tong_tien_gio) + " đồng")
