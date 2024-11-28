# routes.py

from real_world_example.decorators import app_route, allow

# Обработчики маршрутов


@app_route("/create_user")
@allow("any")
def create_user(request):
    return f"Пользователь '{request.user.username}' создан."


@app_route("/list_friends")
@allow("registered")
def list_friends(request):
    return f"Список друзей пользователя '{request.user.username}'."


@app_route("/my_profile/<username>")
@allow("myself")
def my_profile(request, username):
    return f"Профиль пользователя '{username}'."
