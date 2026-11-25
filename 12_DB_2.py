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


def parametrized_query() :
    if db_connection is None :
        connect_db()
        if db_connection is None :
            print("simple_query() stopped due to no connection")
            return
    # Параметризовані запити - це запити, в яких
    # розділяються текст запиту та параметри до нього.
    # Реалізація - на рівні мови програмування
    # Краще підходять для одиничних запитів з параметрами


def prepared_query() :
    if db_connection is None :
        connect_db()
        if db_connection is None :
            print("simple_query() stopped due to no connection")
            return
    # Підготовлені запити - це запити які виконуються
    # у два етапи: підготовка, та виконання з передачею параметрів.
    # Реалізація - на рівні СУБД


def main():
    pass


if __name__ == "__main__":
    main()
