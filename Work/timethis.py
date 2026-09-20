def timethis(func):
    import time

    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(
            f"Function {func.__name__} took {end - start:.4f} seconds to execute.")
        return result
    return wrapper
