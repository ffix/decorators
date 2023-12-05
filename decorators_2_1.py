# name = 'Alice'

def the_father():
    # father_name = "Max"

    print("I am the father")

    def the_son():
        print("I am the son")
        # name_of_the_son = "Bob"
        # print(f"I am the son {name_of_the_son}, my father is {father_name}")



    def the_daughter():
        print("I am the daughter")

        # print(f"I am the daughter name {name}, my father is {father_name}")


    the_son()
    the_daughter()


if __name__ == '__main__':
    the_father()
    # the_son()