# Исключение для доступа, когда у пользователя нет необходимых прав
class AccessDeniedError(Exception):
    pass


# Исключение для случая, когда маршрут не найден
class NotFoundError(Exception):
    pass
