from functools import wraps
from real_world_example.exceptions import AccessDeniedError

# Глобальные словари для маршрутов и правил доступа
router = {}
access_rules = {}


# Декоратор для маршрутизации URL к функции обработчику
def app_route(url):
    def decorator(func):
        if url in router:
            raise ValueError(f"URL '{url}' уже используется.")
        router[url] = func  # Регистрируем маршрут
        return func

    return decorator


# Декоратор для контроля доступа на основе правила
def allow(rule):
    def decorator(func):
        access_rules[func] = rule  # Связываем функцию с правилом доступа

        @wraps(func)
        def wrapper(request, *args, **kwargs):
            # Проверка доступа в зависимости от правила
            if rule == "any":
                return func(request, *args, **kwargs)

            if rule == "registered":
                if request.user.registered:
                    return func(request, *args, **kwargs)
                raise AccessDeniedError("Требуется регистрация для доступа.")

            if rule == "myself":
                target_username = kwargs.get("username")
                if request.user.username == target_username:
                    return func(request, *args, **kwargs)
                raise AccessDeniedError("Доступ разрешён только к своему профилю.")

            raise AccessDeniedError("Неизвестное правило доступа.")

        return wrapper

    return decorator
