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


@int_only
@divided_by_one_hundred
def sum(a, b):
    return a + b


if __name__ == '__main__':
    #---------------------------------------------------#
    # 1
    #---------------------------------------------------#
    print("---------1----------")
    sum(50, 50)
    sum(50, 0)

    #---------------------------------------------------#
    # 2
    #---------------------------------------------------#
    print("---------2----------")
    print(f'res = {sum(50, 50)}')
    try:
        sum("50", "0")
    except ValueError:
        print("поймано исключение ValueError")