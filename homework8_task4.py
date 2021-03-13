#-------------------------------------------------------------------------------#
# 4) Необходимо создать модели работы со складскими запасами товаров и процесса оформления заказа этих товаров
#-------------------------------------------------------------------------------#
class NoNegative:
    def __get__(self, instance, owner):
        if not instance:
            return self
        return instance.__dict__[self._label]

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError(f"{instance.__dict__[self._label]} не может быть отрицательным")
        instance.__dict__[self._label] = value

    def __delete__(self, instance):
        del instance.__dict__[self._label]

    def __set_name__(self, owner, label):
        self._label = label


class Price:
    def __get__(self, instance, owner):
        if not instance:
            return self
        return instance.__dict__[self._label]

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError(f"{instance.__dict__[self._label]} не может быть отрицательным")
        instance.__dict__[self._label] = value + value * 0.2

    def __delete__(self, instance):
        del instance.__dict__[self._label]

    def __set_name__(self, owner, label):
        self._label = label
    


class Product:
    _all_products = []
    _all_categories = set()
    quantity = NoNegative()
    price = Price()


    def __init__(self, name, price, quantity=0, description="нет описания", availability=True, category_name="No category"):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        self.availability = availability
        self.category_name = category_name
        Product._all_categories.add(category_name)
        Product._all_products.append(self)
        
    def add_item(self):
        self.quantity += 1

    def del_item(self):
        self.quantity -= 1

    @staticmethod
    def print_product_quantity(product_name):
        for product in Product._all_products:
            if product.name == product_name:
                print(f'количество товара "{product_name}" на складе:\t{product.quantity}')
        print()

    @staticmethod
    def print_all_products_quantity():
        for product in Product._all_products:
            print(f'{product.name}:\t{product.quantity}')
        print()

    @staticmethod
    def print_all_products_with_category(category_name):
        print(category_name)
        for product in Product._all_products:
            if product.category_name == category_name:
                print(f'\t{product.name}')
        print()



class Basket:
    def __init__(self, items=None):
        self._items = items or ()

    def get_items(self):
        return self._items

    @property
    def sum(self):
        return sum([item[0].price * item[1]  for item in self._items])
    
    def add_item(self, new_product, product_count):
        if new_product.availability:
            products = [item[0] for item in self._items]
            if new_product not in products:
                if new_product.quantity >= product_count:    
                    self._items.append((new_product, product_count))
            else:
                item_index = self._items.index(new_product)
                current_product_count = self._items[item_index][1]
                if current_product_count + product_count <= new_product.quantity:
                    self._items[item_index][1] += product_count

    def remove_item(self, product_name, product_count):
        if product_name in self._items:
            if self._items[product_name] <= product_count:
                del self._items[product_name]
            else:
                self._items[product_name] -= product_count

    def print_basket(self):
        for item in self._items:
            print(f'{item[0].name}:\t{item[1]}')
        print(f'Общая цена:\t{self.sum}')
    

class Customer:
    def __init__(self, name):
        self.name = name


class Order:
    all_orders = []

    def __init__(self, basket, custamer, date):
        self._date = date
        self._is_approved = False
        self._basket = basket
        self.custamer = custamer
        self.id = len(Order.all_orders) + 1
        Order.all_orders.append(self)
    
    def approve(self):
        for product, count in self._basket.get_items():
            product.quantity -= count
        self._is_approved = True

    @staticmethod
    def print_order(id):
        for order in Order.all_orders:
            if order.id == id:
                print(f'customer:\t{order.custamer.name}\napproved:\t{order._is_approved}\nid:\t{order.id}\ndate:\t{order.date}')
                order._basket.print_basket()



if __name__ == '__main__':
    macbook = Product('макбук', 5000, 20, "Это афигенный ноут, покупай!", category_name="гаджеты")
    smartphon = Product('смартфон', 2000, 200, "Это смартфон ноут, покупай!", category_name="гаджеты")
    mixer = Product('миксер', 300, 12, "Это афигенный миксер, покупай!", category_name="электротехника")
    multivarka = Product('мультиварка', 500, 4, "Это афигенная мультиварка, покупай!", category_name="электротехника")
    alarm_clock = Product('будитьник', 100, 10, "Это афигенный будитьник, покупай!", category_name="электротехника")

    print('Все товары из категории "гаджеты":')
    Product.print_all_products_with_category('гаджеты')
    #гаджеты
    #    макбук
    #    смартфон

    Product.print_product_quantity('макбук')
    #количество товара "макбук" на складе:   20

    print("количество всех товаров на складе")
    Product.print_all_products_quantity()
    #макбук:            20
    #смартфон:          200
    #миксер:            12
    #мультиварка:       4
    #будитьник:         10

    basket = Basket([(smartphon, 3), (mixer, 12)])
    basket.add_item(macbook, 2)

    print("корзина")
    basket.print_basket()
    #смартфон:          3
    #миксер:            12
    #макбук:            2
    #Общая цена:        23520.0

    order = Order(basket, Customer('valik'), '07:05:2020')
    order.approve()

    print("заказ")
    Order.print_order(order.id)
    #customer:          valik
    #approved:          True
    #id:                1
    #смартфон:          3
    #миксер:            12
    #макбук:            2
    #Общая цена:        23520.0
    
    print("количество всех товаров на складе")
    Product.print_all_products_quantity()
    #макбук:            18
    #смартфон:          197
    #миксер:            0
    #мультиварка:       4
    #будитьник:         10
