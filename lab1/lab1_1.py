def solve():
    print("Введите натуральное число")
    inputValue = input()
    try:
        int(inputValue)
    except ValueError:
        print("Некорректный ввод")
        return
    reversedNumber = inputValue[::-1]
    meetRequirement = True
    for firstDigitIndex in range(1, len(reversedNumber)-1):
        firstDigit = int(reversedNumber[firstDigitIndex])
        secondDigit = int(reversedNumber[firstDigitIndex+1])
        if secondDigit <= firstDigit:
            meetRequirement = False
    print("Да" if meetRequirement else "Нет")


if __name__ == '__main__':
    solve()