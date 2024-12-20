# First-class objects

from typing import Callable


def hail_someone(name: str) -> str:
    return f'Hail to you, {name}'


def say_hi(name: str) -> str:
    return f'Hi, {name}'


def greetings(greet_func: Callable) -> str:
    return greet_func('Sergey')


if __name__ == '__main__':
    print(greetings(hail_someone))

    # print(greetings(say_hi))

    # for func in (hail_someone, say_hi):
    #     print(greetings(func))