from functools import wraps


def type_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(func.__name__, end='  ')
        print(*args, kwargs, sep=',', end=': ')
        print(type(func(*args, **kwargs)))
    return wrapper


@type_logger
def calc_cube(x):
    return x ** 3


@type_logger
def half_summ(*args):
    result = list(args)
    return sum(result) / 2


@type_logger
def kwargs_func(*args, **kwargs):
    return True


a = calc_cube(5)
b = half_summ(1, 2, 3)
c = kwargs_func(1, 2, 3, key='aaa', val='bbb')
print(calc_cube.__name__)
