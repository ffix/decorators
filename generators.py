def numbers(num):
    lst = []
    for i in range(num):
        lst.append(i)
    return lst

def numbers1(num):
    return list(range(num))

def numnbers2(num):
    return [i for i in range(num)]

def numbers3(num):
    lst = 0
    i = 0
    while i < num:
        lst.append(i)
    return lst

print(list(numbers(10)))

# for i in numbers(10):
#     print(i+100)


# def numbers(num):
#     for i in range(num):
#         yield i