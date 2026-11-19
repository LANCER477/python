# ООП продовження
# У попередньому дослідженні (08_OOP_1) встановлено, що
# оголошені у класі поля є статичними. Акцентуємо на
# роботі з динамічними полями

class Point :
    # замість оголошення полів у класі, їх задають в "конструкторі"
    # аналогічно до функцій, перевантаження не передбачено, вживаються
    # параметри за замовчанням
    def __init__(self,       # посилання на об'єкт (аналог this) передається явно
            x:float=10,
            y:float=20):
        self.x = x           # першим параметром і традиційно називається self
        self.y = y           # звернення через self - обов'язково
        w = 20               # без self - локальна змінна функції


    def __str__(self):       # аналог toString() - автоматично викликається
        return "(%.1f;%.1f)" % (  # коли вимагається рядкове представлення об'єкта
            self.x, self.y   # Звернення до полів - завжди з self
        )


    # перевантаження операцій - спеціальні методи
    # Python не має перевантаження за типами (сигнатурами)
    def __add__(self, other) :
        if isinstance(other, Point) :
            return Point(
                self.x + other.x,
                self.y + other.y
            )                 #
        elif isinstance(other, (int, float)) :
            return Point(     # тому їх тіла - це блоки if-elif-...
                self.x + other,#
                self.y + other# Point + 2.5
            )                 # Point + (1, 2)
        elif isinstance(other, (tuple, list)) :
            if len(other) != 2 :
                raise TypeError("invalid content: required size of 2")
            else :
                if isinstance(other[0], (int, float)) and \
                   isinstance(other[1], (int, float)) :
                    return Point(                 #
                        self.x + other[0],        # Point + (1, 2)
                        self.y + other[1]         # Point + [1, 2]
                    )                             #
                else :
                    raise TypeError("invalid content: only 'int' or 'float' available")
        elif isinstance(other, dict) : # задача: реалізувати додавання з {'x': 5}, {'y': 7}, {'x': 5, 'y': 7}
            if 'x' in other or 'y' in other :
                return Point(
                    self.x + other.get('x', 0),
                    self.y + other.get('y', 0)
                )
            else :
                raise TypeError("dict must have at least one from 'x' or 'y' keys")
        elif isinstance(other, complex) :  # (x,y) + a+jb = (x+a, y+b)
            return Point (
                self.x + other.real,
                self.y + other.imag
            )
        else :
            raise TypeError(f"unsupported operand type(s) for +: 'Point' and '{type(other).__name__}'")



def main() :
    p = Point()                 # __init__ запускається автоматично, self явно не передаємо
    print(p)
    p = Point(30)               # передача аргументів є аналогічною до функцій -
    print(p)                    # 30 20  як за позицією (без врахування self),
    p = Point(y=30)             # так і за іменем
    print(p)                    # 10 30
    print("p + p = ", p + p)
    print("p + 2 = ", p + 2)
    print("p + 2.5 = ", p + 2.5)
    print("p + (1,2) = ", p + (1,2))
    print("p + [1,2] = ", p + [1,2])
    try: print("p + [1,] = ", p + [1,])
    except TypeError as err: print(err)
    try: print("p + [1, 2, 3] = ", p + [1, 2, 3])
    except TypeError as err: print(err)
    try: print("p + [1, '2'] = ", p + [1, '2'])
    except TypeError as err: print(err)
    try: print("p + 'str' = ", p + 'str')
    except TypeError as err: print(err)
    print("p + {'y': 5} = ", p + {'y': 5})
    print("p + {'x': 5,'y': 5} = ", p + {'x': 5,'y': 5})
    try: print("p + {'z': 5} = ", p + {'z': 5})
    except TypeError as err: print(err)
    print("p + (3+5j) = ", p + (3+5j))


if __name__ == '__main__' :
    main()
