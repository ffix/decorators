# стекинг декораторов (применение нескольких декораторов подряд)
def wrap_with_tag(tag_name: str):
    def decorator(func):
        def wrapper(message: str):
            # print(f'Start decorator with tag {tag_name}')
            res = func('Hello')
            # print(f'Finish decorator with tag {tag_name}')
            return f'<{tag_name}>{res}</{tag_name}>'
        return wrapper

    return decorator


@wrap_with_tag('p')
@wrap_with_tag('strong')
def greet(username):
    return f'Hi, {username}'


# greet = wrap_with_tag('strong')(greet)
# greet = wrap_with_tag('p')(greet)

if __name__ == '__main__':
    print(greet('Fedor'))
