def is_symmetric(matrix: list[list]) -> bool:
    for i in range(len(matrix)):
        if len(matrix) != len(matrix[i]):
            return False
        for j in range(i+1, len(matrix[i])):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True


def solve():
    print('Введите измерения матрицы через пробел (высоту и длину)')
    h, l = [int(i) for i in input().split(sep=' ')]
    print('Построчно вводите элементы матрицы через пробел')
    matrix = []
    for i in range(h):
        matrix.append(input().split(sep=' ')[:l])
    print('Симметричная' if is_symmetric(matrix) else 'Не симметричная')


if __name__ == '__main__':
    solve()

