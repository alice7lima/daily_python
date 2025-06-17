from functools import wraps
import time
from loguru import logger

def timer_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        time_spent = time.time() - start_time

        logger.info(f"Função '{func.__name__}' executada em : {time_spent:.4f} segundos")
        return result

    return wrapper