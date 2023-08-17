"""
Реалізувати менеджер контексту Timer, який вимірює час виконання блоку коду.
Контекстний менеджер повинен виводити час, що минув, при виході з контексту.
Використовуйте контекстний менеджер для вимірювання часу виконання певного фрагменту коду.
Реалізувати контекстний менеджер потрібно 2 способами, за допомогою декоратора contextmanager та за допомогою класу.
"""
from time import time, sleep


class Timer:
    def __init__(self):
        self.interval = 0

    def __enter__(self):
        self.start = time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        end = time()
        self.interval = end - self.start
        print(f"Operation time = {self.interval:.2f} seconds")


my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

with Timer() as timer:
    sleep(2)
    sorted_list = sorted(my_list)

