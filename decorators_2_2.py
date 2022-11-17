from typing import Callable


def produce_child(name: str) -> Callable:
    print("I am the father")

    def the_son():
        print("The son was born")

    def the_daughter():
        print("The daughter was born")

    return the_son if name == 'Bob' else the_daughter


if __name__ == '__main__':
    child_func = produce_child(name='Alice')
    child_func()
