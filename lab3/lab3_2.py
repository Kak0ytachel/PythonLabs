
def solve():
    with open('F2.txt', 'r', encoding='utf-8') as file:
        while True:
            line = file.readline()
            if line == '' or line == '\n':
                return
            elements = line.split(sep=' ')
            scores = [int(i) for i in elements[1:]]
            name = elements[0]
            average = sum(scores) / len(scores)
            if average < 6:
                print(name, average)


if __name__ == '__main__':
    solve()
