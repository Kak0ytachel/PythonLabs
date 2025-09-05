import random


class StoreManager:
    storeItems = {}
    cart = {}

    def __init__(self):
        item_names = ['Хлеб', 'Сыр', 'Колбаса', 'Кола', 'Мороженое', 'Вода', 'Банан', 'Йогурт']
        random.shuffle(item_names)
        available_item_names = item_names[:random.randint(1, len(item_names))]
        self.storeItems = {i: [round(random.uniform(0.01, 20.0), 2), random.randint(1, 10)] for i in available_item_names}

    def run(self):
        while True:
            print('Меню:\n1. Просмотр цены\n2. Просмотр количества\n3. Просмотр цены и количества\n4. Покупка\n5. Выход')
            choice = input_int()
            if choice == 1:
                self.show_price_menu()
            elif choice == 2:
                self.show_quantity_menu()
            elif choice == 3:
                self.show_both_menu()
            elif choice == 4:
                self.show_order_menu()
            elif choice == 5:
                print('До свидания')
                return
            else:
                print('Некорректный ввод, попробуйте снова')

    def show_item_list(self):
        print('Товары в наличии:')
        for i in self.storeItems.keys():
            print(' - ', i)

    def find_item(self, allow_exit = False) -> str:
        print("Введите название товара", "или пустую строку чтобы выйти" if allow_exit else "")
        item_name = input().capitalize()
        # print(f"\"{item_name}\"")
        if item_name in self.storeItems.keys():
            return item_name
        elif allow_exit and item_name == '':
            return ''
        else:
            print('Товар не найден. Попробуйте еще раз')
        return self.find_item()

    def show_quantity_menu(self):
        self.show_item_list()
        item_name = self.find_item()
        print(f"{item_name} - {self.storeItems[item_name][1]} в наличии")

    def show_price_menu(self):
        self.show_item_list()
        item_name = self.find_item()
        print(f"{item_name} - {self.storeItems[item_name][0]} руб / шт")

    def show_both_menu(self):
        self.show_item_list()
        item_name = self.find_item()
        print(f"{item_name} - {self.storeItems[item_name][0]} руб / шт, {self.storeItems[item_name][1]} в наличии")

    def show_cart(self):
        print("Ваша корзина: ")
        total = 0
        for item in self.cart.keys():
            price = self.storeItems[item][0]
            quantity = self.cart[item]
            print(f' - {item} - {price} руб * {quantity} = {price * quantity}')
            total += price * quantity
        if total == 0:
            print('Ваша корзина пуста')
        else:
            print(f'Итого: {total} pуб')

    def show_order_menu(self):
        print('Оформление заказа')
        while True:
            self.show_item_list()
            item = self.find_item(True)
            if item == "":
                break
            print("Введите количество")
            quantity = input_int()
            if quantity > 0 and quantity <= self.storeItems[item][1] - self.cart.get(item, 0):
                self.cart[item] = self.cart.get(item, 0) + quantity
                print('Успешно добавлено в корзину')
            elif quantity == 0:
                print('Невозможно добавить 0 товаров в корзину')
            else:
                print(f'Некорректное количество, повторите попытку и введите количество от 1 до '
                      f'{self.storeItems[item][1]}')
        print("Печать чека....")
        print('---------------------')
        print('КАССОВЫЙ ЧЕК')
        print("Магазин \"Продукты\"")
        self.show_cart()
        print('Спасибо за покупку!')
        for item, quantity in self.cart.items():
            self.storeItems[item][1] -= quantity
        self.cart.clear()


def input_int() -> int:
    try:
        return int(input())
    except ValueError:
        print('Некорректный ввод. Введите целое число')
        return input_int()


if __name__ == '__main__':
    StoreManager().run()