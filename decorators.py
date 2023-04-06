import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        print(f'Tiempo de ejecucion {end_time - start_time} segundos')

    return wrapper


def cache(func):
    result_cache = {}
    def wrapper(*args, **kwargs):
        key = str(args) + str(kwargs)

        if key in result_cache:
            print(f'devuelvo del cache {result_cache[key]}')
            return result_cache[key]
        
        result = func(*args, **kwargs)
        result_cache[key] = result
        return result
    return wrapper


def logger(func):
    def wrapper(*args, **kwargs):
        key = str(args) + str(kwargs)
        print('Entrada', args, kwargs)
        result = func(*args, **kwargs)
        print('salida', result)
        return result
    return wrapper



@cache
@timer
@logger
def hola_mundo():
    print('hola mundo')


hola_mundo()