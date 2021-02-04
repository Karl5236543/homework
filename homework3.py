import functools


def divided_by_one_hundred(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        res = func(*args, **kwargs)
        if res % 100 == 0:
            print("We are OK!")
        else:
            print(f"Bad news guys, we got {res % 100}")
        return res
    return inner


def int_only(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        if False in [isinstance(el, int) for el in args] or \
            False in [isinstance(el, int) for el in kwargs.values()]:
            raise ValueError("string type is not supported")
        return func(*args, **kwargs)
    return inner


def cached(func):
    cache = {}
    @functools.wraps(func)
    def inner(*args, **kwargs):
        print(cache)
        oll_args = tuple(kwargs.items()) + args
        if oll_args in cache:
            return cache[oll_args]
        else:
            cache[oll_args] = func(*args, **kwargs)
            return cache[oll_args]
    return inner


@divided_by_one_hundred
def sum1(a, b):
    return a + b


@int_only
def sum2(a, b):
    return a + b


@cached
def sum3(a, b):
    return a + b


if __name__ == '__main__':
    #---------------------------------------------------#
    # 1
    #---------------------------------------------------#
    print("---------1----------")
    sum1(50, 50)
    sum1(50, 0)

    #---------------------------------------------------#
    # 2
    #---------------------------------------------------#
    print("---------2----------")
    print(f'res = {sum2(50, 50)}')
    try:
        sum2("50", "0")
    except ValueError:
        print("поймано исключение ValueError")

    #---------------------------------------------------#
    # 2
    #---------------------------------------------------#
    print("---------3----------")
    sum3(b = 10,a = 12)
    sum3(10,12)
