import time
import functools
import pprint


def my_lru_cache(func=None, *, maxsize=128):
    if not func:
        return lambda func : my_lru_cache(func, maxsize=maxsize)

    cache = {}
    @functools.wraps(func)
    def inner(*args, **kwargs):
        inner.call_count += 1
        key = args, tuple(sorted(kwargs.items()))
        if key in cache:
            inner.hits += 1
            cache[key]['time'] = time.time()
            return cache[key]['result']
        else:
            cache[key] = {
                'result': func(*args, **kwargs),
                'time': time.time()
            }
            if inner.currsize >= inner.maxsize:
                the_oldest = min(cache, key=lambda key : cache[key]['time'])
                del cache[the_oldest]
            else:
                inner.currsize += 1
            inner.misses += 1
            return cache[key]['result']

    def cache_info():
        return {
            'hits': inner.hits,
            'misses': inner.misses,
            'maxsize': inner.maxsize,
            'curresize': inner.currsize,
        }
    
    def cache_clear():
        inner.hits, inner.misses, inner.currsize = 0, 0, 0

    inner.cache_info = cache_info
    inner.cache_clear = cache_clear
    inner.maxsize = maxsize
    inner.currsize, inner.misses, inner.hits, inner.call_count = 0, 0, 0, 0
    return inner


@my_lru_cache(maxsize=64)
def fibonachi_number(n):
    if n < 2:
        return n
    return fibonachi_number(n - 2) + fibonachi_number(n - 1)


if __name__ == '__main__':
    fibonachi_number(100)
    fibonachi_number(100)
    print(fibonachi_number.cache_info())

    fibonachi_number.cache_clear()
    fibonachi_number(100)
    print(fibonachi_number.cache_info())