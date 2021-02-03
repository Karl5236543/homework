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


@divided_by_one_hundred
def sum(a, b):
    return a + b


if __name__ == '__main__':
    #---------------------------------------------------#
    # 1
    #---------------------------------------------------#
    print("1:")
    sum(50, 50)
    sum(50, 0)