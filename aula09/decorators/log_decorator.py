from functools import wraps
from loguru import logger

def log_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(f"Chamando a função '{func.__name__}' com args {args} e kwargs {kwargs}")
        try:
            result = func(*args, **kwargs)
            logger.info(f"Função '{func.__name__}' retornou o resultado: {result}")
            return result

        except Exception as e:
            logger.exception(f"Exceção capturada na função '{func.__name__}': {e}")
            raise

    return wrapper
    