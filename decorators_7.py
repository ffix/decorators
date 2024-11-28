# Параметризация декораторов


def apply_transform(transform):
    def decorator(func):
        def wrapper(username):
            return func(transform(username))
        return wrapper
    return decorator


def custom_upper(text):
    return str.upper(text)


# @apply_transform(str.upper)
# @apply_transform(lambda x: str.upper(x))
@apply_transform(custom_upper)
def greet(username):
    return f'Hi, {username}'

# @apply_transform(custom_upper)
# def hail(username):
#     return f'Hail, {username}'


if __name__ == '__main__':
    print(greet('Fedor'))
    # print(hail('Fedor'))


