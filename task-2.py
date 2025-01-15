import re
from typing import Callable, Generator

def generator_numbers(text: str) -> Generator[float, None, None]:
    # Використовуємо регулярний вираз для знаходження дійсних чисел
    pattern = r'(?<= )\d+\.\d+(?= )'
    matches = re.findall(pattern, text)
    
    # Повертаємо знайдені числа як генератор
    for match in matches:
        yield float(match)

def sum_profit(text: str, func: Callable) -> float:
    # Використовуємо генератор для підсумовування чисел
    total = sum(func(text))
    return total

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income:.2f}")
