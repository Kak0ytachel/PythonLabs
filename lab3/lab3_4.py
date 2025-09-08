import json


def solve():
    values = []
    profits = {}
    with open('F4.txt', "r") as file:
        for line in file:
            items = line.split(sep=' ')
            name = items[0]
            profit = int(items[2]) - int(items[3])
            profits[name] = profit
            if profit > 0:
                values.append(profit)
    average = sum(values) / len(values)
    result = [profits, {"average_profit": average}]
    with open("F4.json", 'w') as file:
        file.write(json.dumps(result))


if __name__ == '__main__':
    solve()

