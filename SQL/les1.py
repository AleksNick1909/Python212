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
#     выражение [NOT] IN (набор значений)

# ORDER BY имя поля | номер поля [ASC | DESC]- оператор сортировки
# LIMIT количество строк OFFSET смещение | LIMIT [смещение] кол строк

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

# *****
# ORDER BY имя поля | номер поля [ASC | DESC]- оператор сортировки

# SELECT NAME
# FROM ZAKAZ
# ORDER BY NAME DESC - сортировка в обратном порядке

# SELECT Prod, NAME
# FROM ZAKAZ
# ORDER BY Prod DESC, NAME

# SELECT NAME, Prod
# FROM ZAKAZ
# WHERE NAME GLOB '[С-Л]*'
# ORDER BY NAME DESC;

# SELECT NAME, Prod
# FROM ZAKAZ
# WHERE NAME BETWEEN 'Ле' AND 'Па' AND Prod != 'шкафы'
# ORDER BY NAME;

# SELECT NAME, SUM, KOD
# FROM ZAKAZ
# WHERE SUM > 4000 AND (KOD LIKE 1003 OR KOD LIKE 1010 OR KOD LIKE 1016)

# SELECT NAME, SUM, KOD
# FROM ZAKAZ
# WHERE SUM > 4000 AND KOD IN (1003, 1010, 1016)

# *******
# import sqlite3

# with sqlite3.connect("users.db") as con:
#     cur = con.cursor()
    # cur.execute("""CREATE TABLE IF NOT EXISTS person(
    # id INTEGER PRIMARY KEY AUTOINCREMENT,
    # name TEXT NOT NULL,
    # phone BLOB NOT NULL DEFAULT '+79090000000',
    # age INTEGER NOT NULL CHECK(age>0 AND age<100),
    # email TEXT UNIQUE
    # )""")
    # cur.execute("""
    # ALTER TABLE person
    # RENAME TO person_table;
    # """)

# *****
#
# with sqlite3.connect("users.db") as con:
#     cur = con.cursor()
    # cur.execute("""
    # ALTER TABLE person_table
    # ADD COLUMN address TEXT NOT NULL DEFAULT 'addr';  - добавили столбец
    # """)
    # cur.execute("""
    # ALTER TABLE person_table
    # RENAME COLUMN address TO home_address;  - переименовали столбец
    # """)
    # cur.execute("""
    # ALTER TABLE person_table
    # DROP COLUMN home_address;  - удалить столбец
    # """)

    # cur.execute("""
    # DROP TABLE person_table;  - удаление таблицы
    # """)


# ********** Добавление столбцов и ячеек

# INSERT INTO имя таблицы [(столбец1[, столбец_n])]
# VALUES (значение_1[, значение_n])
# *** добавление данных из другой таблицы
# INSERT INTO имя таблицы [(встраиваемый список столбцов)]
# SELECT список столбцов
# FROM список таблиц
# WHERE условие

# ***
# Вставить оставшиеся записи (ID>22), уменьшив зарплату на 10%, а опыт работы в 2 раза.
# INSERT INTO T1 (ID, FName, Doljnost, ORab, ZP)
# SELECT ID, FName, D, Orabot/2, Zp*0.9
# FROM T2
# WHERE ID > 22;
# ***
# Создать копию полученной таблицы с менеджерами и директорами (все данные)
# INSERT INTO T3 (ID, FName, Doljnost, ORab, ZP)
# SELECT ID, FName, Doljnost, ORab, ZP
# FROM T1
# WHERE Doljnost IN ('Менеджер', 'Директор');
# ***
# Создать копию таблицы, в которой будет зарплата <1000 и увеличить зарплату на 100 единиц.
# INSERT INTO T4 (ID, FName, Doljnost, ORab, ZP)
# SELECT ID, FName, Doljnost, ORab, ZP+100
# FROM T1
# WHERE ZP < 1000;

# ****** Изменение данных в таблице
# UPDATE имя таблицы
# SET столбец1 = выражение1[, столбец2=выражение2]
# [WHERE условие]

# В таблице Т1, если зарплата не определена  и опыт работы более 0, присвоить 900.
# UPDATE T1
# SET ZP=900
# WHERE ZP IS NULL AND ORab>0;

# ***** Удаление данных
# DELETE FROM имя таблицы
# WHERE условие
# ***
# Удалить записи с неопределенной зарплатой из Т1.
# DELETE FROM T1
# WHERE ZP IS NULL
# ***
# Удалить все записи из таблици Т2.
# DELETE FROM T2


# ********
import sqlite3

with sqlite3.connect("db_4.db") as con:
    cur = con.cursor()
    cur.execute("""
    SELECT *
    FROM Ware
    ORDER BY Price DESC
    LIMIT 2, 5;
    """)

    # res = cur.fetchall()  # возвращает все элементы
    # print(res)
    # for res in cur:
    #     print(res)

    res = cur.fetchone()  # возвращает первый элемент
    print(res)
    res2 = cur.fetchmany(2)  # возвращает заданное количество элементов
    print(res2)
