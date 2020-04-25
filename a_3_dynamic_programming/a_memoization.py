# Dynamic Programming: an optimization technique using caching.

from functools import lru_cache


def add100(n):
    print('Long time')
    return n+100


print(add100(5))
print(add100(5))

# Memoization 1

cache = {}


def memoizedadd100(n):
    if n in cache:
        return n + 100
    else:
        print('Long time')
        cache[n] = n+100
        return cache[n]


print(memoizedadd100(6))
print(memoizedadd100(6))

# Memoization 2
# https://docs.python.org/3.3/library/functools.html --> Doc for lru_cache


@lru_cache(maxsize=1000)
def memoized2add100(n):
    return n + 100


print(memoized2add100(8))
print(memoized2add100(8))
print(memoized2add100.cache_info())
