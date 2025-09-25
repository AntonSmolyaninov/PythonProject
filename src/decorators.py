def log(filename=None):
    """Декоратор для логирования вызова функции в файл или консоль."""

    def decorator(func):
        """Внутренняя функция-декоратор, которая принимает функцию для оборачивания."""

        def wrapper(*args, **kwargs):
            """Обёртка, реализующая логирование результата или ошибки вызова функции."""
            try:
                result = func(*args, **kwargs)
                s = f"{func.__name__} ok"
                if filename:
                    with open(filename, "a") as f:
                        f.write(s + "\n")
                else:
                    print(s)
                return result
            except Exception as e:
                err_type = type(e).__name__
                s = f"{func.__name__} error: {err_type}. " f"Inputs: {args}, {kwargs}"
                if filename:
                    with open(filename, "a") as f:
                        f.write(s + "\n")
                else:
                    print(s)
                raise

        return wrapper

    return decorator
