import math

mean_arithmetic = lambda x: sum(x) / len(x)
mean_geometric = lambda x: math.prod(x) ** (1 / len(x))
mean_harmonic = lambda x: len(x) / sum(1 / v for v in x)


def min_strategy(strategies, data):
    if isinstance(data, (tuple, list)) and len(data) > 0 and callable(data[0]):
        strategies, data = data, strategies

    best_index = 0
    min_value = strategies[0](data)

    for i in range(1, len(strategies)):
        value = strategies[i](data)
        if value < min_value:
            min_value = value
            best_index = i

    return best_index, min_value


def main():
    data = (1, 2, 3, 4, 5, 6, 7, 8)
    strategies = (mean_arithmetic, mean_geometric, mean_harmonic)

    result = min_strategy(strategies, data)
    print("Индекс минимальной стратегии:", result[0])
    print("Минимальное значение:", result[1])
    print("Результат в виде кортежа:", result)


if __name__ == '__main__':
    main()

