def caching_fibonacci():
    """
    Функція створює кеш та повертає рекурсивну функцію fibonacci(n),
    яка обчислює числа Фібоначчі з використанням кешування (замикання).
    """
    cache = {}  # Словник для зберігання вже обчислених значень

    def fibonacci(n):
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n in cache:
            return cache[n]
        # Рекурсивне обчислення з кешуванням
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci