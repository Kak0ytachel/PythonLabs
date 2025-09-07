
def is_prime(number: int) -> bool:
    i = 2
    if number < i:
        return False
    while True:
        if i * i > number:
            return True
        if number % i == 0:
            return False
        i += 1


def solve():
    while True:
        try:
            number = int(input())
            if number == -1:
                return
            if number < 0 or number > 1000:
                raise ValueError
            print(is_prime(number))
        except ValueError:
            print("Некорректный ввод")


if __name__ == '__main__':
    solve()
