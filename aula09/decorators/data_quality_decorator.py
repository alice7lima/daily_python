from functools import wraps
import pandas as pd

def data_quality_decorator(expected_columns=None, expected_types=None):
    return lambda func: check_data_quality(func, expected_columns, expected_types)

def check_data_quality(func, expected_columns, expected_types):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        if not isinstance(result, pd.DataFrame):
            raise TypeError(f"A função '{func.__name__}' não retornou um DataFrame pandas.")
        
        if expected_columns:
            for column in expected_columns:
                if column not in result.columns:
                    raise KeyError(f"Coluna '{column}' não encontrada no dataframe.")
                
        if expected_types:
            for column, type in expected_types.items():
                if column in result.columns and result[column].dtype != type:
                    raise TypeError(f"A coluna '{column}' no dataframe não é do tipo esperado ({type.__name__})")
                
        return result
    
    return wrapper