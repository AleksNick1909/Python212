# Разработка базы данных папка db3
# Разработчики логической базы данных
# Разработчики физической базы данных
# док db5
#
# Показать какие продавцы продают какие товары.
# SELECT s.Seller, sg.Goods
# FROM Seller AS s, SallerGoods AS sg
# WHERE s.INNSeller=sg.INNSeller

# Вывести продавцов и клиентов (пары), связанные м/у собой приобретенным товаром
# SELECT c.Client, s.Seller
# FROM Client c, Seller s, SallerGoods sg, ClientGoods cg
# WHERE s.INNSeller=sg.INNSeller AND cg.ID=sg.ID AND cg.INNClient=c.INNClient
#
# Вывести список товара, поставляемого производителями.
# SELECT sg.Goods, s.Status
# FROM Seller s, SallerGoods sg
# WHERE s.INNSeller=sg.INNSeller AND s.Status LIKE 'производитель'
#
# На какую сумму было продано каждого товара магазинам.
# SELECT cg.CostUnit * cg.Count AS Сумма
# FROM Client c, ClientGoods cg
# WHERE cg.INNClient=c.INNClient AND c.Status LIKE 'магазин'
#

# ФУНКЦИИ АГРЕГИРОВАНИЯ
# SUM - находить сумму в столбце (только с числовыми полями)
# AVG - среднее арифметическиое (только с числовыми полями)
# COUNT - количество
# MIN - мин значение
# MAX - макс значение

# Однострочные запросы: =, <,>,<>,<=,=> - возвращает из вложенной команды SELECT только одну строку
# Многострочные запросы: IN (NOT IN) - возвращает более одной строки (список значений) из подзапроса
# UNION - объединяет несколько запросов из разных таблиц в одну

# DB6
# 1.	Сосчитать количество клиентов, покупающих товар.
# SELECT COUNT(Client) AS [Количество клиентов]
# FROM Client

# 2.	Сколько посредников поставляют товар для фирмы.
# SELECT COUNT(Seller) AS [Количество посредников]
# FROM Seller
# WHERE Status = 'посредник'

# 3.	Вывести среднюю сумму сделки по проданному товару.
# SELECT AVG(CostUnit * Count) AS 'Сумма товара'
# FROM ClientGoods

# 4.	Посчитать на какую сумму было всего поставлено товара.
# SELECT SUM(CostUnit * Count) AS 'Сумма товара'
# FROM ClientGoods

# 5.	Определите максимальное количество закупленного товара шт.(кг)
# SELECT MAX(Count) AS 'Максимальное кол товара'
# FROM SallerGoods

# DB 7 документ
# 2.	Напишите запрос, который выбрал бы высший рейтинг в каждом городе.
# SELECT city, MAX(rating)
# FROM Customers
# GROUP BY city

# 3.	Подсчитать, на какую сумму было продано товаров в каждый город.
# SELECT city, SUM(o.amt)
# FROM Customers c, Orders o
# WHERE c.cnum=o.cnum
# GROUP BY c.city

# 5.	Выведите максимальный рейтинг заказчика для каждого продавца.
# SELECT s.sname, MAX(c.rating)
# FROM Customers c, Salespeople s
# WHERE c.snum=s.snum
# GROUP BY s.sname

# 6.	Напишите запрос, который получит максимальную сумму заказов каждого клиента, которая больше 3000
# SELECT snum, SUM(amt)
# FROM Orders
# GROUP BY snum
# HAVING SUM (amt) > 3000
#
# 11.	Напишите запрос, который выведет сумму продаж, которая больше 10000.
# SELECT snum, SUM(amt)
# FROM Orders
# GROUP BY snum
# HAVING SUM (amt) > 10000

# документ DB8
# Выведите перечень сумм заказов продавца Rifkin.
# SELECT o.amt, s.sname
# FROM Orders o, Salespeople s
# WHERE o.snum=s.snum AND s.sname LIKE 'Rifkin'
# 2 variant
# SELECT o.amt
# FROM Orders o
# WHERE o.snum =
#     (SELECT s.snum
#     FROM Salespeople s
#     WHERE s.sname LIKE 'Rifkin'
#     )
# ***

# Определите  комиссионные всех продавцов, обслуживающих заказчиков в Риме
# SELECT s.com
# FROM Salespeople s, Customers c
# WHERE s.snum=c.snum AND c.city LIKE 'Rome'
# Многострочные запросы
# SELECT com
# FROM Salespeople
# WHERE snum IN
#     (
#     SELECT snum
#     FROM Customers
#     WHERE city LIKE 'Rome'
#     )

# Определите города проживания заказчиков с наименьшим рейтингом.
# SELECT c.city, MIN(c.rating)
# FROM Customers c
# GROUP BY c.city
# HAVING MIN(c.rating) IN
#     (SELECT MIN(c.rating)
#     FROM Customers c)

# Напишите запрос, который выведет максимальный рейтинг заказчика
# для продавцов имеющих комиссионные больше 0,11%.
# SELECT MAX(c.rating)
# FROM Customers c
# WHERE c.snum IN
#     (SELECT s.snum
#     FROM Salespeople s
#     WHERE s.com>0.11
#     )


# DB 5
# док db9
# Выведите список студентов физико-математического факультета.
# SELECT FIO
# FROM Student
# WHERE "Group" IN
#     (SELECT "Group"
#     FROM G
#     WHERE Kafedra IN
#         (SELECT Kafedra
#         FROM Kafedra
#         WHERE Decanat LIKE 'Физико-математический')
#     )

# Студенты какой кафедры и факультета сдавали социологию.
# SELECT Kafedra, Decanat
# FROM Kafedra
# WHERE Kafedra IN
# (
# SELECT Kafedra
# FROM G
# WHERE "Group" IN
# (
# SELECT "Group"
# FROM Student
# WHERE Id_St IN
# (
# SELECT Id_St
# FROM Exzamen
# WHERE Predmet LIKE 'Социология'
# )
# )
# )

# Выведите кафедры, список студентов, список студентов в алфавитном порядке.
# SELECT s.FIO,
#     (SELECT g.Kafedra
#     FROM G g
#     WHERE s.'Group' = g.'Group') AS Кафедра
# FROM Student s
# ORDER BY s.FIO

# Выведите студентов физико-технического факультета сдавших иностранный язык на 5.
# SELECT FIO
# FROM Student
# WHERE ID_St IN
#     (SELECT id_St
#     FROM Exzamen
#     WHERE Predmet LIKE 'Иностр. язык' AND Ball LIKE '5'
#     ) AND 'Group' IN
#         (SELECT 'Group'
#         FROM G
#         WHERE Kafedra IN
#             (SELECT Kafedra
#             FROM Kafedra
#             WHERE Decanat LIKE 'Физико-технический')
#             )

# db7
# 1.	Необходимо решить извлекать ли некоторые данные из таблицы Заказчиков, если один и более
# заказчиков в этой таблице находятся в Берлине.
# SELECT *
# FROM Customers
# WHERE EXISTS
#     (SELECT *
#     FROM Customers
#     WHERE city = 'Berlin')
#
# 2.	Напишите запрос, который использовал бы подзапрос для получения всех заказов для заказчика с именем Cisneros.
# SELECT *
# FROM Orders o
# WHERE EXISTS
#     (SELECT c.cnum
#     FROM Customers c
#     WHERE c.cnum=o.cnum AND c.cname='Cisneros')

# 5.	Вывести всех продавцов и заказчиков, размещенных в Лондоне и вывести их как единое целое.
# SELECT snum, sname
# FROM Salespeople
# WHERE city='London'
# UNION
# SELECT cnum, cname
# FROM Customers
# WHERE city='London';

# 6.	Вывести номера и города продавцов.
#  SELECT snum, city
# FROM Customers
# UNION ALL
# SELECT snum, city
# FROM Salespeople

# 7.	Создайте объединение из двух запросов, которое показало бы имена, города и оценки всех заказчиков. Те из них, которые имеют поле  rating=200 и более, должны, кроме того,
# иметь слова - "Высокий Рейтинг", а остальные должны иметь слова "Низкий Рейтинг".
# SELECT cnum, city rating, 'Высокий рейтинг' AS [Рейтинг]
# FROM Customers
# WHERE rating >= 200
#
# UNION
#
# SELECT cnum, city rating, 'Низкий рейтинг'
# FROM Customers
# WHERE rating < 200

# 8.	Напишите запрос, который выведет пары имен заказчиков и клиентов.
# SELECT s.sname, c.cname
# FROM Salespeople s INNER JOIN Customers c
# ON s.snum=c.snum

# 9.	Напишите запрос, который выведет  список всех клиентов и их заказы, отсортировав имена клиентов по алфавиту.
#  SELECT c.cname, o.onum
# FROM Orders o INNER JOIN Customers c
# ON o.cnum=c.cnum
# ORDER BY c.cname

# SELECT c.cname, o.onum
# FROM Orders o LEFT JOIN Customers c
# ON o.cnum=c.cnum
# ORDER BY c.cname

# 