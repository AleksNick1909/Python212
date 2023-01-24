# ДЕКОРАТОРЫ

# def hello():
#     return "Hello, I am func 'hello'"
#
#
# def super_func(func):
#     print("Hello, I am func 'super_func'")
#     print(func())
#
#
# super_func(hello)

#  ******

# def hello():
#     return "Hello, I am func 'hello'"
#
#
# test = hello
# print(test())

# *****

# def my_decorator(func):
#     def func_wrapper():
#         print('Code defore')
#         func()
#         print('Code after')
#
#     return func_wrapper
#
#
# def func_test():
#     print("Hello, I am func 'hello'")
#
#
# test = my_decorator(func_test)
# test()


# ****

# def my_decorator(func):  # декорирующая функция
#     def func_wrapper():
#         print('Code defore')
#         func()
#         print('Code after\n')
#
#     return func_wrapper
#
#
# @my_decorator  # декоратор
# def func_test():  # функция которую декорируем
#     print("Hello, I am func 'hello'")
#
#
# @my_decorator
# def bye():
#     print("Hello, I am func 'bye'")
#
#
# func_test()
# bye()

# ****

# def bold(fn):
#     def wrap():
#         return "<b>" + fn() + "</b>"
#
#     return wrap
#
#
# def italic(fn):
#     def wrap():
#         return "<i>" + fn() + "</i>"
#
#     return wrap
#
#
# @bold
# @italic
# def hello():
#     return "text"
#
#
# print(hello())

# ***** Создать декоратор, который будет выводить количество вызовов декорирующей функции
# и ее содержимое

# def cnt(fn):
#     count = 0
#
#     def wrap():
#         nonlocal count
#         count = count + 1
#         fn()
#         print("Вызов функции:", count)
#
#     return wrap
#
#
# @cnt
# def hello():
#     print("Hello")
#
#
# hello()
# hello()
# hello()

# *****

# def args_decorator(fn):
#     def wrap(arg1, arg2):
#         print("Данные:", arg1, arg2)
#         fn(arg1, arg2)
#
#     return wrap
#
#
# @args_decorator
# def print_full_name(first, last):
#     print("Меня зовут", first, last)
#
#
# print_full_name("Ирина", "Ветрова")


# *****

# def args_decorator(fn):
#     def wrap(*args, **kwargs):
#         print("args:", args)
#         print("args:", kwargs)
#         fn(*args, **kwargs)
#
#     return wrap
#
#
# @args_decorator
# def print_full_name(a, b, c, study="Python"):
#     print(a, b, c, "изучают", study, "\n")
#
#
# print_full_name("Ирина", "Елизавета", "Светлана", study="JavaScript")
# print_full_name("Влад", "Алекс", "Екатерина")


# ******

# def decor(args1, args2):
#     def args_dec(fn):
#         def wrap(x, y):
#             print(args1, x, args2, y, "=", end=' ')
#             fn(x, y)
#
#         return wrap
#     return args_dec
#
#
# @decor("Сумма:", "+")
# def summa(a, b):
#     print(a + b)
#
#
# @decor("Разность", "-")
# def sub(a, b):
#     print(a - b)
#
#
# summa(5, 2)
# sub(5, 2)

# **** создать декоратор который будет принимать в виде аргумента число,
# которое будет умножаться на число принимаемой функцией

def multiply(n1):
    def mult(fn):
        def wrap(n2):
            return n1 * fn(n2)

        return wrap
    return mult


@multiply(3)
def return_num(num):
    return num


print(return_num(5))

# ***** не правильно работает

# def typed(*args, **kwargs):
#     def wrapper(fn):
#         def wrap(*f_args, **f_kwargs):
#             for i in range(len(args)):
#                 if type(f_args[i]) != args[i]:
#                     raise TypeError("Некорректный тип данных")
#             for k in kwargs:
#                 if type(f_kwargs[k]) != kwargs[k]:
#                     raise TypeError("Некорректный тип данных именнованого параметра")
#             return fn(*f_args, **f_kwargs)
#
#         return wrap
#     return wrapper
#
#
# @typed(int, int, int)
# def typed_fn(x, y, z):
#     return x * y * z
#
#
# @typed(str, str, str)
# def typed_fn2(x, y, z):
#     return x + y + z
#
#
# @typed(int, int, z=int)
# def typed_fn3(x, y, z="Hello!"):
#     return (x + y) * z
#
#
# print(typed_fn(3, 4, 5))
# # print(typed_fn(3, 4, "Dog"))
# print(typed_fn2("Hello", "World", "!"))
# # print(typed_fn2(3, 4, 5))
# print(typed_fn3("Hello", "World", z='5'))


# *******************

# def args_decorator(tx=None, decorator_text=''):
#     def my_decorator(func):
#         def wrap(*args):
#             print(decorator_text, end="")
#             func(*args)
#
#         return wrap
#
#     if tx is None:
#         return my_decorator
#     else:
#         return my_decorator(tx)
#
#
# @args_decorator
# def hello_world(text):
#     print(text)
#
#
# @args_decorator(decorator_text="Hello, ")
# def hello_world2(text):
#     print(text)
#
#
# hello_world('Hi!')
# hello_world2('world!')


# *****************