import math


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

    def __add__(self, other):
        if isinstance(other, Fraction):
            n = self.numerator * other.denominator + other.numerator * self.denominator
            d = self.denominator * other.denominator
        elif isinstance(other, int):
            n = self.numerator + other * self.denominator
            d = self.denominator
        elif isinstance(other, (tuple, list)):
            if len(other) != 2:
                raise TypeError("invalid content: required size of 2")
            if not (isinstance(other[0], int) and isinstance(other[1], int)):
                raise TypeError("invalid content: elements must be integer")
            if other[1] == 0:
                raise ValueError("Знаменник не може дорівнювати нулю")
            n = self.numerator * other[1] + other[0] * self.denominator
            d = self.denominator * other[1]
        elif isinstance(other, dict):
            num = other.get('numerator', other.get('num'))
            den = other.get('denominator', other.get('den', 1))
            if num is None:
                raise TypeError("dict must contain 'numerator' key")
            if not (isinstance(num, int) and isinstance(den, int)):
                raise TypeError("invalid content: dictionary values must be integer")
            if den == 0:
                raise ValueError("Знаменник не може дорівнювати нулю")
            n = self.numerator * den + num * self.denominator
            d = self.denominator * den
        else:
            raise TypeError(f"unsupported operand type(s) for +: 'Fraction' and '{type(other).__name__}'")

        g = math.gcd(n, d)
        if d < 0:
            g = -g
        return Fraction(n // g, d // g)

    def __radd__(self, other):
        return self.__add__(other)


def main():
    f = Fraction(1, 2)
    print(f"Початковий дріб f = {f}")

    print("f + Fraction(1, 3) =", f + Fraction(1, 3))
    print("f + 2 =", f + 2)
    print("3 + f =", 3 + f)
    print("f + (1, 4) =", f + (1, 4))
    print("f + [2, 3] =", f + [2, 3])
    print("f + {'numerator': 1, 'denominator': 6} =", f + {'numerator': 1, 'denominator': 6})
    print("f + {'numerator': 2} =", f + {'numerator': 2})

    try:
        print(f + (1, 2, 3))
    except TypeError as err:
        print("Помилка кортежу (розмір != 2):", err)

    try:
        print(f + [1, 0])
    except ValueError as err:
        print("Помилка списку (знаменник 0):", err)

    try:
        print(f + {'x': 5})
    except TypeError as err:
        print("Помилка словника (немає 'numerator'):", err)

    try:
        print(f + "1/2")
    except TypeError as err:
        print("Помилка непідтримуваного типу:", err)


if __name__ == '__main__':
    main()
