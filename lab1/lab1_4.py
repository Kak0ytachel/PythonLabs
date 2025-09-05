print(dict(zip(range(0, 10), [sum(i) for i in list(zip(*[[int(i == int(j)) for i in range(0, 10)] for j in list(input())]))])))
