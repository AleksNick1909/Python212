import sqlite3

# cars = [
#     ("BMW", 54000),
#     ("Chevrolet", 46000),
#     ("Daewoo", 38000),
#     ("Citroen", 29000),
#     ("Honda", 33000)
# ]
#
# with sqlite3.connect("cars.db") as con:
#     cur = con.cursor()
#     cur.execute("""
#     CREATE TABLE IF NOT EXISTS cars(
#         car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         model TEXT,
#         price INTEGER
#     )""")

    # cur.executescript("""
    #     DELETE FROM cars WHERE model LIKE 'B%';
    #     UPDATE cars SET price = price + 100
    # """)

    # cur.execute("UPDATE cars SET price = :Price WHERE model LIKE 'B%'", {'Price': 0})

    # cur.executemany("INSERT INTO cars VALUES(NULL, ?, ?)", cars)

    # for car in cars:
    #     cur.execute("INSERT INTO cars VALUES(NULL, ?, ?)", car)

    # cur.execute("INSERT INTO cars VALUES(1, 'Renault', 22000)")
    # cur.execute("INSERT INTO cars VALUES(2, 'Volvo', 29000)")
    # cur.execute("INSERT INTO cars VALUES(3, 'Mercedes', 57000)")
    # cur.execute("INSERT INTO cars VALUES(4, 'Bentley', 35000)")
    # cur.execute("INSERT INTO cars VALUES(5, 'Audi', 52000)")

# ***
con = None
try:
    con = sqlite3.connect("cars.db")
    cur = con.cursor()
    cur.executescript("""
        CREATE TABLE IF NOT EXISTS cars(
        car_id INTEGER PRIMARY KEY AUTOINCREMENT,
        model TEXT,
        price INTEGER
    );
    BEGIN;
    INSERT INTO cars VALUES(NULL, 'Renault', 22000);
    UPDATE cars SET price = price + 100
    """)
    con.commit()  # сохранение в базу данных
except sqlite3.Error as e:
    if con:
        con.rollback()  # откат в исходное положение данные при ошибке
    print("Ошибка выполнения запроса", e)
finally:
    if con:
        con.close()


