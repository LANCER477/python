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

def main():
    pass


if __name__ == "__main__":
    main()
