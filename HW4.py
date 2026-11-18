exceptions = {
    "1": TypeError,
    "2": ValueError,
    "3": OSError,
    "4": IndexError,
    "5": KeyError,
    "6": ZeroDivisionError,
}


def handle_exception(exc_type):
    try:
        raise exc_type
    except TypeError:
        print("У програмі оброблено TypeError")
    except ValueError:
        print("У програмі оброблено ValueError")
    except OSError:
        print("У програмі оброблено OSError")
    except IndexError:
        print("У програмі оброблено IndexError")
    except KeyError:
        print("У програмі оброблено KeyError")
    except ZeroDivisionError:
        print("У програмі оброблено ZeroDivisionError")


def main():
    while True:
        print("\nВиберіть тип винятку:")
        for key, exc in exceptions.items():
            print(f"{key} {exc.__name__}")
        print("0 Exit")

        choice = input("> ").strip()

        if choice == "0":
            break
        elif choice in exceptions:
            handle_exception(exceptions[choice])
        else:
            print("Невірний вибір, спробуйте ще раз")


if __name__ == '__main__':
    main()

