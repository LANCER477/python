# Робота з базами даних
#
# mysql-connector-python
#
# pip install mysql-connector-python
import mysql.connector
# Підготовча робота з БД - створення бази даних,
# користувача для неї та надаємо йому доступ
# create database python_231;
# create user user_231p@localhost identified by 'pass_231';
# grant all privileges on python_231.* to user_231p@localhost;
db_ini = {
    "host": "localhost",
    "port": 3306,
    "user": "user_231p",
    "password": "pass_231",
    "database": "python_231",
    "charset": "utf8mb4",
    "collation": "utf8mb4_unicode_ci",
    "use_unicode": True
}
# Схема роботи з СУБД: підключення - команда - результати
# Підключення встановлюється один раз і замінюється тільки
# через розрив каналу (непланово)
# Команди (і результати) перестворюються. Не рекомендується
# повторно використовувати команду для нових задач.
# Через постійність підключення реалізується як статичне поле
# або глобальна змінна
db_connection = None

def connect_db() :
    global db_connection
    try :
        db_connection = mysql.connector.connect(**db_ini)
    except mysql.connector.Error as err :
        print(err)
    else :
        print("Connection OK")


def simple_query() :
    if db_connection is None :
        connect_db()
        if db_connection is None :
            print("simple_query() stopped due to no connection")
            return

    sql = "SELECT CURRENT_TIMESTAMP"    #
    cursor = None
    try :                               # з підключення формується курсор
        cursor = db_connection.cursor() # (аналог Statement у Java),
        cursor.execute(sql)             # не розрізняються команди (з/без рез-тів)
    except mysql.connector.Error as err : # Імена колонок та їх дані передаються окремо
        print(err)                      # Одержання даних - ітерація курсора
    else :                              #
        print(cursor.column_names)      # ('CURRENT_TIMESTAMP',)
        row = next(cursor)              # Дані автоматично типізуються
        print(row)                      # (datetime.datetime(2026, 11, 25, ...),)
    finally :                           #
        if cursor is not None :
            cursor.close()


def middle_query() :
    if db_connection is None :
        connect_db()
        if db_connection is None :
            print("middle_query() stopped due to no connection")
            return

    sql = "SELECT UUID() UNION SELECT UUID()" # Рекомендований спосіб роботи з
    try :                                     # ресурсами - with. Це, зокрема,
        with db_connection.cursor(            # дозволяє створити загальний try
            dictionary=True                   # до якого буде передаватись і
        ) as cursor:                          # виняток Unread result found
            cursor.execute(sql)               # Параметр dictionary=True
            for row in cursor:                # налаштовує курсор на формування
                print(row)                    # dict з іменами полів у запиті
    except mysql.connector.Error as err :     # Цикл for дозволяє повну ітерацію
        print(err)                            # результатів запиту


def name_conflicts() :
    '''Однаковість імен полів може спричинити проблеми, пов'язані з
    появою однакових ключів словника. Яка буде поведінка у цьому разі?'''
    pass


def main():
    # connect_db()
    simple_query()
    middle_query()


if __name__ == "__main__":
    main()
