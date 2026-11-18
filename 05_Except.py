# Якщо виняток не обробляється, робота програми
# завершується помилкою.
# Необхідність винятків - у зупинці роботи конструкторів,
# які іншим способом зупинити неможна. Для інших задач
# це зручність, яка може бути замінена іншими схемами.

def throw_value_error() :    # У Python поширеніше "Error"
    raise ValueError         # raise - створення виняткової ситуації


def throw_type_error() :
    raise TypeError("Something went wrong...")


def throw_exception() :
    raise Exception


def no_throw() :
    pass


def main() :
    try :                                     # Оброброблення винятків можливе
        # throw_value_error()                 # лише, якщо вони виникають у блоці
        no_throw()                            # try
        # throw_type_error()
        # throw_exception()
    except ValueError :                       # except - блок приймання винятку
        print("Value Error detected")         # у даному разі - ValueError
    except TypeError as err :                 # блоків except може бути декілька
        print("Type Error:", err)             # прийом винятку - as variable
    except :                                  # except без параметрів -
        print("Other error detected")         # оброблення усіх винятків;
        return                                # завершує main, але після finally
    else :                                    # else - виконується у разі успішного
        print("'Else' block executed")        # завершення блоку try, але без return
        # throw_type_error()                  # винятки в else не обробляються
    finally :                                 # finally - виконується у будь-якому разі
        print("Finally block executed")       # у т.ч. якщо викликається return
                                              # у т.ч. якщо виняток не "спійманий"
    print("Main finished")


if __name__ == '__main__' :
    main()

# Друга велика схема вжитку системи винятків полягає у задачі
