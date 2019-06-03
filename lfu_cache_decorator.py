import pprint


def my_lfu_decorator(max_size):
    def decorator(func):
        cache = {}

        def wrapper(number):
            if number in cache.keys():
                cache[number]['counter'] += 1
            else:
                if len(cache) == max_size:
                    # delete lfu
                    print('<deleting value {}>'.format(min(cache.keys(), key=lambda x: cache[x]['counter'])))
                    cache.pop(min(cache.keys(), key=lambda x: cache[x]['counter']))

                cache[number] = {
                    'result': func(number),
                    'counter': 1
                }

            return cache[number]['result']

        def cache_info():
            pprint.pprint(cache)

        wrapper.cache_info = cache_info

        return wrapper
    return decorator


@my_lfu_decorator(5)
def power_two(number):
    return number ** 2


print(power_two(1))
power_two.cache_info()
print(power_two(1))
power_two.cache_info()
print(power_two(2))
power_two.cache_info()
print(power_two(2))
power_two.cache_info()
print(power_two(2))
power_two.cache_info()
print(power_two(2))
power_two.cache_info()
print(power_two(3))
power_two.cache_info()
print(power_two(3))
power_two.cache_info()
print(power_two(3))
power_two.cache_info()
print(power_two(4))
power_two.cache_info()
print(power_two(5))
power_two.cache_info()
print(power_two(6)) # '4' or '5' should be deleted from cache
power_two.cache_info()
