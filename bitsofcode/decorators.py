from functools import wraps
import logging


def multiply(multiple: int = 10):
    def multiply_wrapper(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            num = func(*args, **kwargs)
            product = num * multiple
            return product

        return wrapper

    return multiply_wrapper


def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f"Running {func.__name__} with args: {args} and kwargs: {kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"Finished running {func.__name__}")
        return result

    return wrapper


def log_with_level(level: int = logging.INFO):
    def log(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            logging.log(
                level, f"Running {func.__name__} with args: {args} and kwargs: {kwargs}"
            )
            result = func(*args, **kwargs)
            logging.log(level, f"Finished running {func.__name__}")
            return result

        return wrapper

    return log
