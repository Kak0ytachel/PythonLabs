
def solve():
    lines = []
    while True:
        line = input()
        if line == '':
            break
        lines.append(line + '\n')
    with open('F1.txt', 'w') as file:
        file.writelines(lines)


if __name__ == '__main__':
    solve()
