import re


def solve():
    result = {}
    with open('F3.txt', 'r', encoding='utf-8') as file:
        for line in file:
            subject = re.findall('[A-ZА-Я][A-Za-zА-Яа-я]*:', line)[0]
            items = re.findall("[0-9]+[(][A-Za-zА-Яа-я]+[)]", line)
            hours = sum([int(i.split(sep='(')[0]) for i in items])
            result[subject[:-1]] = hours
    print(result)


if __name__ == '__main__':
    solve()
