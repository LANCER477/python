# Робота з файлами
# При роботі з файлами розрізняють дві ситуації:
# - робота з файловою системою (пошук, копіювання,
#     видалення файлів та директорій тощо)
# - робота з даними, що зберігаються у файлах
# 
def write_file() :
    '''Приклад роботи з файлом без автоматичного
    управління ресурсами'''
    file = None
    try :
        file = open("data_1.txt", "w", encoding="utf-8")
        file.write("Latin charset data\n")
        file.write("Кириличні дані\n")
        file.flush()
    except OSError as err :
        print("write_file():", err)
    else :
        print("File write OK")
    finally :
        if file != None :
            file.close()


def write_file_2() :
    '''Ілюстрація роботи з ресурсним блоком, який
    автоматично звільняє ресурс після завершення'''
    try :
        with open("data_2.txt", "w", encoding="utf-8") as file :
            file.write('# Дані для підключення БД\n')
            file.write('host:localhost\n')
            file.write('port : 3306\n')
            file.write(' user :user_231 # логін\n')
            file.write(' pass: pass_231 # пароль\n')
            file.write('# БД за замовчанням\n')    # \n -> \r\n
            file.write('scheme: server_231\r\n')  # \r\n -> \r\r\n
    except OSError as err:
        print("write_file_2():", err)
    else :
        print("File write OK")


def read_file(filename:str) -> None :
    try :
        with open(filename, "r", encoding="utf-8") as file :
            # print( file.read() ) -- зчитування всього файлу
            i = 0
            res = {}
            for x in file :
                i += 1          # символ(и) переведення рядка - лишаються в х
                print(i, x)     # одинокий \r не сприймається роздільником
                parts = x.split("#")[0].split(":")
                if len(parts) == 2 :
                    res[parts[0].strip()] = parts[1].strip()
    except OSError as err:
        print("read_file():", err)
        return None
    else :
        return res


def read_file_2(filename:str) -> dict|None :
    try :
        with open(filename, "r", encoding="utf-8") as file :
            return { k:v for k, v in
                (   map(str.strip, line.split(":", 1))
                    for line in file
                    if ':' in line
                )
            }
    except OSError as err:
        print("read_file_2():", err)
        return None


def main() :
    # write_file()
    # write_file_2()
    # data = read_file("data_2.txt")
    data = read_file_2("data_2.txt")
    print('---------')
    print(data)


if __name__ == '__main__' :
    main()

