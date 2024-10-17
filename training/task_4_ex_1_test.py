from task_4_ex_1 import StringProcessor

def test_pos_normal():
    string = StringProcessor()
    result = string.process("hello, world")
    assert result == "Hello, world."


def test_pos_normal_from_capital():
    string = StringProcessor()
    result = string.process("Hello, world")
    assert result == "Hello, world."


def test_pos_normal_with_dot():
    string = StringProcessor()
    result = string.process("hello, world.")
    assert result == "Hello, world."


def test_neg_from_tabulation():
    string = StringProcessor()
    result = string.process("\thello, world")
    assert result == "Hello, world."


def test_neg_with_CR():
    string = StringProcessor()
    result = string.process("hello, world\r")
    assert result == "Hello, world."