class Fraction :
    def __init__(self, numerator: int = 1, denominator: int = 1):
        if denominator == 0:
            raise ValueError("Знаменник не може дорівнювати нулю")
        self.numerator = numerator
        self.denominator = denominator
        self.num = numerator
        self.den = denominator

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __repr__(self):
        return f"Fraction({self.numerator}, {self.denominator})"


def main():
    try:
        f1 = Fraction(3, 4)
        print(f"f1 = {f1} (чисельник: {f1.numerator}, знаменник: {f1.denominator})")

        f2 = Fraction(5, 7)
        print(f"f2 = {f2} (чисельник: {f2.num}, знаменник: {f2.den})")

        f3 = Fraction()
        print(f"f3 = {f3} (за замовчанням)")

        f_err = Fraction(5, 0)
    except ValueError as err:
        print(f"Помилка: {err}")


if __name__ == '__main__':
    main()
