from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n):
    return 0 if n == 0 else 1 if n == 1 else fibonacci(n - 1) + fibonacci(n - 2)
fibonacci(100)