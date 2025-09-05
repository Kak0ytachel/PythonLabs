def solve():
    print("Введите числа в строку через пробел")
    numbers = input().split(sep=' ')
    occurrences = {}
    for number in numbers:
        if number not in occurrences.keys():
            occurrences[number] = 0
        occurrences[number] += 1
    counter = 0
    for occurrence in occurrences.values():
        if occurrence >= 2:
            counter += occurrence * (occurrence - 1) // 2
    print("Количество пар повторяющихся чисел:", counter)


if __name__ == '__main__':
    solve()
