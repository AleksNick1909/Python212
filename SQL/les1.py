# Введение в базу данных
# Система управления базами данных (СУБД)
# SQL (язык структурированных запросов)

# SQLite3

# *.db, *.SQLite, *.SQLite3, *.sdb, *.db2


# import sqlite3

# con = sqlite3.connect("profile.db")
# cur = con.cursor()
#
#
# con.close()

# with sqlite3.connect("profile.db") as con:
#     cur = con.cursor()
#     # cur.execute("""CREATE TABLE IF NOT EXISTS users(
#     # id INTEGER PRIMARY KEY AUTOINCREMENT,
#     # name TEXT NOT NULL,
#     # summa REAL,
#     # date TEXT
#     # )
#     # """)
#     cur.execute("DROP TABLE users")


# **** КОМАНДЫ
# select [ALL | DISTINCT] {* | столбец1 [, столбец2]} что хотим показать ALL - все, DISTINCT - без повторений
# FROM таблица_1[, таблица_2] от куда хотим достать инфу

# SELECT FName, ZP - какие столбы хотим увидеть
# FROM T1; - из какой таблицы
# WHERE условие
#     AND или OR
#     Операторы =, ==, <>, !=, <, <=, >, >=
#     выражение [NOT] BETWEEN начальное значение AND конечное значение
#     выражение [NOT] LIKE шаблон строки
#            % - любое количество символов
#            _ - один символ
#     выражение [NOT] GLOB регулярное выражение
#            * - любое количество
#            ? - элемент может не быть или быть только один раз
#            . - может быть один символ и один раз
#            [abc] [a-z] [^abc] - набор каких то символов или диапазон
#     выражение IS [NOT] NULL
# ***
# SELECT *
# FROM T1
# WHERE Doljnost='Директор' OR Doljnost="Менеджер";
#
# SELECT FName
# FROM T1
# WHERE Doljnost="Менеджер" AND ZP < 2000 AND ORab > 3;
#
# SELECT *
# FROM T1
# WHERE ZP BETWEEN 1000 AND 2100;
#
# SELECT *
# FROM T1
# WHERE ZP NOT BETWEEN 1000 AND 2100;
#
# SELECT *
# FROM T1
# WHERE FName LIKE 'Пе%';
#
# SELECT *
# FROM T1
# WHERE FName LIKE '%ов';
#
# SELECT *
# FROM T1
# WHERE FName GLOB '[ПЕ]*';
#
# SELECT *
# FROM T1
# WHERE FName GLOB '*[ПЕпе]*';
#
# SELECT FName AS Фамилия
# FROM T1
# WHERE FName GLOB '[А-Л]*';
#
# SELECT FName, ORab
# FROM T1
# WHERE ZP IS NULL;
#
# SELECT ZP
# FROM T1
# WHERE Doljnost="Оператор" AND ORab < 3;
#
# SELECT DISTINCT ZP
# FROM T1
# WHERE Doljnost="Менеджер";
#
# SELECT *
# FROM T1
# WHERE (Doljnost="Оператор" OR Doljnost="Секретарь") AND ORab > 2;
