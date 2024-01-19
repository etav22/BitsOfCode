import logging

from bitsofcode.decorators import multiply, log, log_with_level


def test_multiply():
    @multiply(multiple=5)
    def add_x_y(x, y):
        return x + y

    assert add_x_y(1, 2) == 15


def test_log(caplog):
    caplog.set_level(logging.INFO)

    @log
    def add_x_y(x, y):
        return x + y

    add_x_y(1, 2)
    assert "Running add_x_y with args: (1, 2) and kwargs: {}" in caplog.text
    assert "Finished running add_x_y" in caplog.text


def test_log_with_level(caplog):
    lvl = logging.DEBUG
    caplog.set_level(lvl)

    @log_with_level(level=lvl)
    def add_x_y(x, y):
        return x + y

    add_x_y(1, 2)
    assert "Running add_x_y with args: (1, 2) and kwargs: {}" in caplog.text
    assert "Finished running add_x_y" in caplog.text
