from router import app_route
from request import userrequest
from errors import AccessDenied

from collections import defaultdict
storage = defaultdict(list)

def allow(rule):
    def decorator(func):
        storage[rule].append(func)
        def wrapper(*args, **kwargs):
            # func(*args, **kwargs)
            if rule == 'any':
                return func(*args, **kwargs)
            if rule == "registered":
                if userrequest.user.registered:
                    return func(*args, **kwargs)
                raise AccessDenied
            ...
        return wrapper
    return decorator


@app_route('/create_user')
@allow('any')
def create_user():
    ...

@app_route('/list_friend')
#@deny('all')
@allow('registered')
def list_friends():
    ...

@app_route('/list_friend')
@allow('myself')
def show_my_own_profile():
    ...


print(storage)




# class User: ...

#
# class UserStorage:
#     def add_user(self, user: User):
#         app.db.store_user(user)
#
# storage = UserStorage()
#


# http://exmaple.com/list_friends
#
# #@allow('any')
# @app_route('/create_user')
# def create_user():
#     ...
#
# #@allow('registered')
# #@deny('all')
# @app_route('/list_friend')
# def list_friends():
#     ...
#
# #@allow('myself')
# @app_route('/list_friend')
# def show_my_own_profile():
#     ...
#
# print(storage)
#
# # @lru_cache
# # def call_outer_server(url):
# #     requsts.get(...)
# #
# # call_outer_server('http://example.com')
# # call_outer_server('http://example.com')