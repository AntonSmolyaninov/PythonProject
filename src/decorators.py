import functools
from typing import Callable, Optional, ParamSpec, TypeVar

P = ParamSpec("P")
R = TypeVar("R")


def log(filename: Optional[str] = None) -> Callable[[Callable[P, R]], Callable[P, R]]:
    """Декоратор для логирования вызова функции в файл или консоль."""

    def decorator(func: Callable[P, R]) -> Callable[P, R]:
        """Внутренняя функция-декоратор, которая принимает функцию для оборачивания."""

        @functools.wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
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
