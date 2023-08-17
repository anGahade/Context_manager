"""
Створіть контекстний менеджер DividerContext, який буде прінтити символ,
який ми до нього передамо як розділитель для основного блоку коду до та після його виконання.
Реалізувати контекстний менеджер потрібно 2 способами, за допомогою декоратора contextmanager та за допомогою класу.
(приклад можно знайти у презентації)
"""


class DividerContext:

    def __enter__(self):
        print(35*"*")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(35*"*")


my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]


with DividerContext() as dc:
    sorted_list = sorted(my_list)
    print(sorted_list)
