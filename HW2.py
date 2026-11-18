def custom_func(*args, **kwargs) -> None:
    if "name" in kwargs:
        print(f"Hello, {kwargs['name']}")

    numeric_sum = 0
    for item in args:
        if isinstance(item, (int, float)) and not isinstance(item, bool):
            numeric_sum += item

    print(f"Сумма числовых данных: {numeric_sum}")


def main():
    custom_func(10, "тест", 20.5, True, 5, name="Александр")
    custom_func(1, 2, 3, [1, 2], None, 4.5, age=25, city="Киев")
    custom_func(name="Анна")


if __name__ == '__main__':
    main()
