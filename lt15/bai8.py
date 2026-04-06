class Product:
    def __init__(self, price):
        self.__price = price   # private attribute

    # Getter
    def get_price(self):
        return self.__price

    # Setter
    def set_price(self, price):
        if price < 0:
            print("Lỗi: Giá không được nhỏ hơn 0")
        else:
            self.__price = price

# Test
p = Product(100)
print("Giá:", p.get_price())

p.set_price(-50)   # lỗi
p.set_price(200)   # hợp lệ

print("Giá mới:", p.get_price())