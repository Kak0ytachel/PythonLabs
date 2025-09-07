import time
import traceback


class MyCustomException(Exception):
    def __init__(self, *args):
        super().__init__(*args)
        print("Ахтунг! Ошибка!")


def solve():
    while True:
        print("Введите номер теста (1 или 2) или 0 для выхода")
        try:
            choice = int(input())
            if choice < 0 or choice > 2:
                raise ValueError
        except ValueError:
            print('Некорректный ввод')
            continue
        if choice == 0:
            break
        try:
            if choice == 1:
                test_1()
            else:
                test_2()
        except Exception as e:
            traceback.print_exc()
        time.sleep(1)


def only_odds(number: int):
    if number % 2 == 0:
        raise MyCustomException("Четное число")
    return number / ((number + 1) / 2 - 1)


def test_1():
    print(only_odds(15))
    print(only_odds(12))


def test_2():
    try:
        print('Введите число')
        value = int(input())
        print(only_odds(value))
    except ValueError:
        print('Некорректный ввод')
        return
    except Exception as e:
        print(f'Возникла ошибка: {e}')
    else:
        print('Выполнено успешно')
    finally:
        print('Тест завершен')


if __name__ == '__main__':
    solve()
