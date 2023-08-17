"""
Створіть контекстний менеджер DividerContext, який буде прінтити символ,
який ми до нього передамо як розділитель для основного блоку коду до та після його виконання.
Реалізувати контекстний менеджер потрібно 2 способами, за допомогою декоратора contextmanager та за допомогою класу.
(приклад можно знайти у презентації)
"""
from contextlib import contextmanager


@contextmanager
def divider_context():

    print(35*"*")
    yield
    print(35*"*")


my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

with divider_context() as dc:
    sorted_list = sorted(my_list)
    print(sorted_list)
