import os

from src.decorators import log


@log()
def add(x, y):
    return x + y


@log()
def bad_add(x, y):
    return x + y


@log("test_log.txt")
def sub(x, y):
    return x - y


@log("test_log.txt")
def fail(x, y):
    return x / y  # может вызвать ZeroDivisionError


def test_console_ok(capsys):
    add(3, 4)
    captured = capsys.readouterr()
    assert "add ok" in captured.out


def test_console_error(capsys):
    try:
        bad_add(1, "a")
    except TypeError:
        pass  # Ожидали ошибку
    captured = capsys.readouterr()
    assert "bad_add error: TypeError." in captured.out
    assert "Inputs: (1, 'a'), {}" in captured.out


def test_file_ok():
    # Удаляем файл, если был создан
    if os.path.exists("test_log.txt"):
        os.remove("test_log.txt")

    sub(10, 6)
    with open("test_log.txt") as f:
        lines = f.readlines()
    assert "sub ok\n" in lines


def test_file_error():
    if os.path.exists("test_log.txt"):
        os.remove("test_log.txt")
    try:
        fail(5, 0)
    except ZeroDivisionError:
        pass  # Мы ожидали ошибку

    with open("test_log.txt") as f:
        lines = f.readlines()
    assert any("fail error: ZeroDivisionError." in line for line in lines)
    assert any("Inputs: (5, 0), {}" in line for line in lines)


def teardown_module(module):
    if os.path.exists("test_log.txt"):
        os.remove("test_log.txt")
