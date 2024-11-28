# Синтаксис декоратора

from functools import wraps
from typing import Callable

def oops_decorator(func: Callable) -> Callable:
    @wraps(func)
    def wrapper():
        print('I say oops')
        func()
        print('I say oops again')
    return wrapper


@oops_decorator
def say_hello_world() -> str:
    print('Hello world')


@oops_decorator
def say_hello_friend() -> str:
    print('Hello friend')


if __name__ == '__main__':
    say_hello_world()
