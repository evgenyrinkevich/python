from functools import wraps


def val_checker(checker):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if checker(*args, **kwargs):
                func(*args, **kwargs)
            else:
                raise ValueError

            return func(*args, **kwargs)

        return wrapper

    return decorator


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


print(calc_cube(9))
