import functools
from random import choice


def create_cache1lvl(lock_obj):
    def cache1lvl(maxsize=100):
        def decorating_function(user_function):
            cache = {}
            lock = lock_obj()

            @functools.wraps(user_function)
            def wrapper(key, *args, **kwargs):
                try:
                    result = cache[key]
                except KeyError:
                    with lock:
                        if len(cache) == maxsize:
                            for i in range(maxsize // 10 or 1):
                                del cache[choice(cache.keys())]
                        cache[key] = user_function(key, *args, **kwargs)
                        result = cache[key]
                return result

            def clear():
                cache.clear()

            def delete(key):
                try:
                    del cache[key]
                    return True
                except KeyError:
                    return False

            wrapper.clear = clear
            wrapper.cache = cache
            wrapper.delete = delete
            return wrapper

        return decorating_function

    return cache1lvl


def create_cache2lvl(lock_obj):
    def cache2lvl(maxsize=100):
        def decorating_function(user_function):
            cache = {}
            lock = lock_obj()

            @functools.wraps(user_function)
            def wrapper(*args, **kwargs):
                try:
                    result = cache[args[0]][args[1]]
                except KeyError:
                    with lock:
                        if wrapper.cache_size == maxsize:
                            to_delete = maxsize // 10 or 1
                            for i in range(to_delete):
                                key1 = choice(cache.keys())
                                key2 = choice(cache[key1].keys())
                                del cache[key1][key2]
                                if not cache[key1]:
                                    del cache[key1]
                            wrapper.cache_size -= to_delete
                        result = user_function(*args, **kwargs)
                        try:
                            cache[args[0]][args[1]] = result
                        except KeyError:
                            cache[args[0]] = {args[1]: result}
                        wrapper.cache_size += 1
                return result

            def clear():
                cache.clear()
                wrapper.cache_size = 0

            def delete(key, *args):
                if args:
                    try:
                        del cache[key][args[0]]
                        if not cache[key]:
                            del cache[key]
                        wrapper.cache_size -= 1
                        return True
                    except KeyError:
                        return False
                else:
                    try:
                        wrapper.cache_size -= len(cache[key])
                        del cache[key]
                        return True
                    except KeyError:
                        return False

            wrapper.clear = clear
            wrapper.cache = cache
            wrapper.delete = delete
            wrapper.cache_size = 0
            return wrapper

        return decorating_function

    return cache2lvl
