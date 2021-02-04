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


def not_str(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        if True in [isinstance(el, str) for el in args] or \
            True in [isinstance(el, str) for el in kwargs.values()]:
            raise ValueError("string type is not supported")
        return func(*args, **kwargs)
    return inner


def cached(func):
    cache = {}
    used_cache_count = 0
    @functools.wraps(func)
    def inner(*args, **kwargs):
        nonlocal used_cache_count
        oll_args = tuple(kwargs.items()) + args
        if oll_args in cache:
            used_cache_count += 1
            print(f'Used cache with counter = {used_cache_count}')
            return cache[oll_args]
        else:
            cache[oll_args] = func(*args, **kwargs)
            print(f'Function executed with counter = {len(cache)}, '\
                f'function result = {cache[oll_args]}')
            return cache[oll_args]
    return inner


@divided_by_one_hundred
def sum1(a, b):
    return a + b


@not_str
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
    sum3(12,10)
    sum3(1,3)
    sum3(12,10)
    sum3(12,10)
    sum3(a=12,b=10)
    sum3(a=12,b=10)
