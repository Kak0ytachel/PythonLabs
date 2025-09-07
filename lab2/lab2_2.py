def func(arg: int | str | tuple):
    if isinstance(arg, int):
        print(''.join(list(reversed(str(arg)))))
    elif isinstance(arg, str):
        counter = 0
        for i in arg:
            try:
                counter += int(i)
            except ValueError:
                pass
        print(counter)
    elif isinstance(arg, tuple):
        pre_letters = 'qwertyuiopasdfghjklzxcvbnm'
        letters_list = list(pre_letters + pre_letters.capitalize())
        letters_counter = 0
        numbers_counter = 0
        for i in arg:
            if i in letters_list:
                letters_counter += 1
            else:
                try:
                    float(i)
                    numbers_counter += 1
                except ValueError:
                    pass
        print(f'{letters_counter} букв, {numbers_counter} чисел')


def solve():
    while True:
        print('Выберите тип входных данных:\n1. Кортеж (tuple)\n2. Целое число \n3. Строка\n0. Выход')
        try:
            choice = int(input())
        except ValueError:
            print('Некорректный ввод')
            continue
        if choice == 0:
            print('Выход...')
            return
        elif choice == 1:
            print('Вводите строковые / числовые элементы кортежа в отдельных строках или пустую для выхода')
            obj = list()
            while True:
                element = input()
                if element == '':
                    break
                try:
                    element = float(element)
                    element = int(element)
                except ValueError:
                    pass
                obj.append(element)
            obj = tuple(obj)
        elif choice == 2:
            print('Введите целое число')
            try:
                obj = int(input())
            except ValueError:
                print("Некорректный ввод")
                continue
        elif choice == 3:
            print('Введите строку')
            obj = input()
        else:
            print('Некорректный ввод')
            continue
        func(obj)


if __name__ == '__main__':
    solve()

