import re
from typing import Callable

def generator_numbers(text: str):
    """
    Генерує всі дійсні числа з тексту (ті, що чітко відокремлені пробілами).
    """
    # Регулярний вираз для знаходження дійсних чисел
    pattern = r"(?<=\s)\d+\.\d+(?=\s)|(?<=\s)\d+(?=\s)"
    for match in re.finditer(pattern, f" {text} "):  # Додаємо пробіли з обох боків для коректності
        yield float(match.group())

def sum_profit(text: str, func: Callable):
    """
    Підсумовує всі числа, знайдені за допомогою переданого генератора func.
    """
    return sum(func(text))