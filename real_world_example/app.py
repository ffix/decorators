from real_world_example.decorators import router
from real_world_example.exceptions import AccessDeniedError, NotFoundError
from real_world_example.models import User, Request

import real_world_example.routes  # Обязательно мпортируем маршруты, чтобы они зарегистрировались!


# Функция для обработки запроса по URL
def handle_request(url, request):
    try:
        # Проверяем все зарегистрированные маршруты
        for route, handler in router.items():
            if "<username>" in route:
                # Извлекаем базовый путь до параметра
                base_route = route.split("<username>")[0]
                if url.startswith(base_route):
                    # Извлекаем значение параметра из URL
                    username = url[len(base_route) :]
                    response = handler(request, username=username)
                    print(response)
                    return
        # Обработка обычных маршрутов
        handler = router.get(url)
        if handler:
            response = handler(request)
            print(response)
        else:
            raise NotFoundError("Маршрут не найден.")
    except AccessDeniedError as e:
        print(f"Доступ запрещён: {e}")
    except NotFoundError as e:
        print(f"Не найдено: {e}")
    except Exception as e:
        print(f"Ошибка: {e}")


# Пример использования


def main():
    # Создаём пользователей
    guest = User(username="guest")
    user_john = User(username="john", registered=True)

    # Создаём запросы от пользователей
    request_guest = Request(user=guest)
    request_john = Request(user=user_john)

    # Обработка различных запросов
    print("Гость создаёт пользователя:")
    handle_request("/create_user", request_guest)

    print("\nГость пытается просмотреть друзей:")
    handle_request("/list_friends", request_guest)

    print("\nЗарегистрированный пользователь просматривает друзей:")
    handle_request("/list_friends", request_john)

    print("\nПользователь просматривает свой профиль:")
    handle_request("/my_profile/john", request_john)

    print("\nПользователь пытается просмотреть чужой профиль:")
    handle_request("/my_profile/jane", request_john)

    print("\nДоступ к неопределённому маршруту:")
    handle_request("/unknown", request_john)


if __name__ == "__main__":
    main()
