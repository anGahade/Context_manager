"""
Реалізувати менеджер контексту Timer, який вимірює час виконання блоку коду.
Контекстний менеджер повинен виводити час, що минув, при виході з контексту.
Використовуйте контекстний менеджер для вимірювання часу виконання певного фрагменту коду.
Реалізувати контекстний менеджер потрібно 2 способами, за допомогою декоратора contextmanager та за допомогою класу.
"""
from contextlib import contextmanager
import time


@contextmanager
def timer():
    start = time.time()
    print("Your operation has started!")
    yield
    end = time.time()
    print(f"Operation time = {end - start:.2f} seconds")


my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

with timer() as t:
    time.sleep(1)
    sorted_list = sorted(my_list)

