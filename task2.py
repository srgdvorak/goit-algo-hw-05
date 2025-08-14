import re
from typing import Callable

def generator_numbers(text: str):
    """
    Генерує всі дійсні числа з тексту, які відокремлені лише пробілами з обох боків.
    Числа на початку чи в кінці тексту ігноруються.
    """
    pattern = r"(?<= )\d+\.\d+(?= )|(?<= )\d+(?= )"
    for match in re.finditer(pattern, text):
        yield float(match.group())

def sum_profit(text: str, func: Callable):
    """
    Підсумовує всі числа, знайдені за допомогою генератора func.
    """
    return sum(func(text))