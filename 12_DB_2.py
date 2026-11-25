# Параметризовані та підготовлені запити
import mysql.connector

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
db_connection = None


def connect_db() :
    global db_connection
    try :
        db_connection = mysql.connector.connect(**db_ini)
    except mysql.connector.Error as err :
        print(err)
    else :
        print("Connection OK")


def param_query() :
    if db_connection is None :
        connect_db()
        if db_connection is None :
            print("param_query() stopped due to no connection")
            return
    # Параметризовані запити - це запити, в яких
    # розділяються текст запиту та параметри до нього.
    # Реалізація - на рівні мови програмування
    # Краще підходять для одиничних запитів з параметрами
    # ненадійного походження
    sql = "SELECT DATEDIFF(CURRENT_DATE, %s) AS DAYS"
    try:
        with db_connection.cursor(dictionary=True) as cursor:
            cursor.execute(sql, ('2026-01-01',)) # ключ словника формується саме
            row = next(cursor)                   # так, як зазначено у запиті.
            print(row)                           # Перетворення case (розмір літер)
    except mysql.connector.Error as err :        # не здійснюється
        print(err)


def prepared_query() :
    if db_connection is None :
        connect_db()
        if db_connection is None :
            print("prepared_query() stopped due to no connection")
            return
    # Підготовлені запити - це запити які виконуються
    # у два етапи: підготовка, та виконання з передачею параметрів.
    # Реалізація - на рівні СУБД
    # Параметри - аналогічно у cursor.execute
    sql = "SELECT DATEDIFF(CURRENT_DATE, ?) AS DAYS"
    try:
        with db_connection.cursor(dictionary=True, prepared=True) as cursor:
            cursor.execute(sql, ('2026-01-01',)) #
            row = next(cursor)                   #
            print(row)                           #
            cursor.execute(sql, ('2026-11-01',)) #
            row = next(cursor)                   #
            print(row)                           #
    except mysql.connector.Error as err :        #
        print(err)


def main():
    param_query()
    print("--------")
    prepared_query()


if __name__ == "__main__":
    main()
