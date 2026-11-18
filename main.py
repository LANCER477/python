def say_hello():  # def - оголошення функції, традиція: snake_case
    # перший рядок (string) після оголошення є документуючим коментарем
    '''Demo function prints "Hello"'''
    print( "Hello" )


# Між оголошеннями функцій прийнято
# залишати 2 порожні рядки (принаймні)
def say_hi(name:str) -> None :  # None - аналог NULL / void / undefined
    print( "Hi,", name )


def print_xy(x:int=10, y:int=20) -> None :   # значення за замовчанням
    print(x, y)


def print_xy(x:int=10, y:int=20, t:int=30) -> None :   # перевантаження?
    print('x =', x, 'y =', y, 't =', t)    # Не перевантаження а переозначення
# У Python немає перевантаження функцій, у той же час немає помилки


def factorial(n: int) -> int:
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a


w = 10


def get_w():
    return w


def set_w(val):
    w = val


def set_gw(val):
    global w
    w = val


def show(*args):
    print(*args)


def show_kw(**kwargs):
    for k, v in kwargs.items():
        print(k, "=>", v)


# У Python діє модульний принцип - файли можуть підключатись
# до інших файлів як модулі (import), під час підключення
# код файлу виконується. Під час виконання в файл передається
# назва модуля __name__ з якою він підключається. Якщо файл
# викликається як самостійна програма, то її значення: __main__

def main():
    pass        # pass - порожня операція (замість порожнього блоку)
    # say_hello()
    # say_hi('User')  # обидві виконуються, хоча в оголошенні вказано :str
    # say_hi(123)     # - типізація є швидше підказкою, а не обмеженням
    # print_xy(1, 2)
    # print_xy(1)
    # print_xy(y=2)
    # print_xy(y=1, x=2)
    # print_xy(t=2, y=1)
    # print( factorial(5) )
    # print( factorial(6) )
    # print( gcd(16, 12) )  # 4
    # print( gcd(12, 15) )  # 3
    # print( gcd(12, 14) )  # 2
    # print( gcd(12, 13) )  # 1
    # print( gcd(12, 12) )  # 12

    # print( get_w() )    # 10
    # set_w(20)
    # print( get_w() )    # 10
    # set_gw(20)
    # print( get_w() )    # 20

    show(1)
    show(1, 2)
    show(1, 2, 'a')
    data = (4,5,6,'b')
    show(data)          # (4, 5, 6, 'b') - як один аргумент
    show(*data)         # 4 5 6 b - як перелік параметрів

    show_kw(x=10, y=20, name='User')

if __name__ == '__main__':
    main()
