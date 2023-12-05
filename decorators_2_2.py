from typing import Callable

# run_count = 0

def produce_child(name: str) -> Callable:
    print("I am the father")

    # global run_count
    # run_count += 1

    def the_son():
        print("The son was born")

    def the_daughter():
        print("The daughter was born")

    return the_son if name == 'Bob' else the_daughter


if __name__ == '__main__':
    child_func = produce_child(name='Alice')
    child_func()

    # print(run_count)
    # produce_func = produce_child
    # print(run_count)
    # child_func = produce_func("Bob")
    # child_func()
    # print(run_count)