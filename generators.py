def numbers(num):
    lst = []
    for i in range(num):
        lst.append(i)
    return lst

def numbers1(num):
    return list(range(num))

def numbers2(num):
    return [i for i in range(num)]

def numbers3(num):
    lst = []
    i = 0
    while i < num:
        lst.append(i)
        i+=1
    return lst


# def numbers_g(num):
#     for i in range(num):
#         yield i

if __name__ == "__main__":
    print(list(numbers(10)))
    print(list(numbers1(10)))
    print(list(numbers2(10)))
    print(list(numbers3(10)))

    # print(numbers_g(10))
    # for i in numbers_g(10):
    #     print(i+100)


