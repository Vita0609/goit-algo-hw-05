def caching_fibonacci():
    # Створюємо порожній словник для кешу
    cache = {}

    def fibonacci(n):
        # Обробка базових випадків
        if n <= 0:
            return 0
        elif n == 1:
            return 1

        # Перевірка, чи є результат у кеші
        if n in cache:
            return cache[n]

        # Обчислення значення та збереження у кеші
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci

fib = caching_fibonacci()

print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610
