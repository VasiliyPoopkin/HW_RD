#task 1


# import datetime
#
# def print_call_info(func):
#     def wrapper(*args, **kwargs):
#         print(f"Function {func.__name__} called at {datetime.datetime.now()}")
#         return func(*args, **kwargs)
#     return wrapper
#
# @print_call_info
# def sum_number(a, b):
#     return a + b
#
# result = sum_number(2, 2)
# print(result)


#task 2


# class ContextManager:
#     def __enter__(self):
#         print("==========")
#
#     def __exit__(self, exc_type, exc_value, traceback):
#         print("==========")
#         if exc_type is not None:
#             print(f"An error occurred: {exc_type.__name__}: {exc_value}")
#         return True
#
# with ContextManager():
#     def sum_number(a, b):
#         return a + b
#     result = sum_number(2, 2)
#     print(result)


#task 3


# import datetime
#
# def print_call_info(times):
#     def wrapper(func):
#         def inner(*args, **kwargs):
#             for i in range(times):
#                 print(f'Function name: {func.__name__}')
#                 print(f'Time: {datetime.datetime.now()}')
#                 result = func(*args, **kwargs)
#             return result
#         return inner
#     return wrapper
#
#
# @print_call_info(times=3)
#
# def sum_number(a, b):
#     return a + b
#
# result = sum_number(2, 2)
# print(result)
