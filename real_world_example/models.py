# Класс пользователя
class User:
    def __init__(self, username, registered=False):
        self.username = username
        self.registered = registered


# Класс запроса, содержит информацию о пользователе
class Request:
    def __init__(self, user):
        self.user = user
