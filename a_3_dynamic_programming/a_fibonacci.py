# (1) Recursive approach:
from functools import lru_cache


def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(7))
# Time complexity O(2^n)
# Space complexity O(n)


# (2) Dynamic programming approach = recursion + memoization

# Using lru_cache: https://docs.python.org/3/library/functools.html


@lru_cache(maxsize=1000)
# Decorator to wrap a function with a memoizing callable that saves up to the maxsize most recent calls.
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)


print(fib(10))
print(fib.cache_info())

# Without external libraries
cache = {}


def fibo(n):
    if n in cache:
        return cache[n]
    elif n < 2:
        cache[n] = n
        return cache[n]
    else:
        cache[n] = fib(n-1) + fib(n-2)

        return cache[n]


x = fibo(8)
print(cache)
print(x)

# Time complexity: O(n)
# Space complexity: storing cache makes it worse than the recursive only approach
