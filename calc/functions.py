from typing import Union
from .utils import is_numeric

def add(num1: Union[int, float], num2: Union[int, float]):
    if not is_numeric(num1) or not is_numeric(num2):
        raise TypeError("Invalid type")
        
    return num1 + num2

def sub(num1, num2):
    return num1 - num2
    
def mul(num1, num2):
    return num1 * num2
