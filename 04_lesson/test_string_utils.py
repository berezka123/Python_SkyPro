import pytest
from string_utils import StringUtils


# Тесты функции capitilize:
@pytest.mark.parametrize("input_text, expected_output", [
        ("python", "Python"),
        ("33 cows", "33 cows"),
        ("hello, world", "Hello, world"),
    ],
)
def test_positive_capitalize(input_text, expected_output):
    string = StringUtils()
    assert string.capitilize(input_text) == expected_output


@pytest.mark.parametrize("input_text, expected_output", [
        ("", ""),
        ("\tpython", "\tPython"),  # \t - символ табуляции.
        ("- hello", "- Hello"),
        (" hello", " Hello")
    ],
)
def test_negative_capitalize(input_text, expected_output):
    string = StringUtils()
    assert string.capitilize(input_text) == expected_output


# Тесты функции trim:
@pytest.mark.parametrize("input_text, expected_output", [
        (" python", "python"),
        (" 33 cows", "33 cows"),
        ("   Hello, world", "Hello, world"),
    ],
)
def test_positive_trim(input_text, expected_output):
    string = StringUtils()
    assert string.trim(input_text) == expected_output


@pytest.mark.parametrize("input_text, expected_output", [
        ("", ""),
        ("\tpython", "python"),
        ("\nHello", "Hello"),
    ],
)
def test_negative_trim(input_text, expected_output):
    string = StringUtils()
    assert string.trim(input_text) == expected_output


# Тесты для функции to_list:
@pytest.mark.parametrize("input_text, expected_output", [
        ("snow,rain,hail", ["snow", "rain", "hail"]),
        ("01:ab:23:cd:45", ["01:ab:23:cd:45"])
    ]
)
def test_positive_to_list_without_delimeter(input_text, expected_output):
    string = StringUtils()
    assert string.to_list(input_text) == expected_output


@pytest.mark.parametrize("input_text, delimeter, expected_output", [
        ("snow; rain; hail", ";", ["snow", " rain", " hail"]),
        ("01:ab:23:cd:45", ":", ["01", "ab", "23", "cd", "45"]),
        ("+7 987-65-43", " ", ["+7", "987-65-43"])
    ]
)
def test_positive_to_list_with_delimeter(input_text, delimeter,
                                         expected_output):
    string = StringUtils()
    assert string.to_list(input_text, delimeter) == expected_output


@pytest.mark.parametrize("input_text, expected_output", [
        (" , , ", [" ", " ", " "]),
        ("", [""])
    ]
)
def test_negative_to_list_without_delimeter(input_text, expected_output):
    string = StringUtils()
    assert string.to_list(input_text) == expected_output


@pytest.mark.parametrize("input_text, delimeter, expected_output", [
        ("snow; rain; hail", "", ["snow; rain; hail"]),
        ("01--ab--23--cd--45", "--", ["01", "ab", "23", "cd", "45"]),
        ("", "", [""])
    ]
)
def test_negative_to_list_with_delimeter(input_text, delimeter,
                                         expected_output):
    string = StringUtils()
    assert string.to_list(input_text, delimeter) == expected_output


# Тесты для функции contains:
@pytest.mark.parametrize("input_text, symbol, expected_output", [
        ("example@example.com", "@", True),
        ("python", "p", True),
        (" SkyPro", " ", True)
    ]
)
def test_positive_contains(input_text, symbol, expected_output):
    string = StringUtils()
    assert string.contains(input_text, symbol) == expected_output


@pytest.mark.parametrize("input_text, symbol, expected_output", [
        ("Hometask :(", ":(", True),
        ("python", "P", False),
        ("SkyPro", "SkyPro", True)
    ]
)
def test_negative_contains(input_text, symbol, expected_output):
    string = StringUtils()
    assert string.contains(input_text, symbol) == expected_output


# Тесты для функции delete_symbol:
@pytest.mark.parametrize("input_text, symbol, expected_output", [
        ("example@example.com", "@", "exampleexample.com"),
        ("python", "p", "ython"),
        ("Sky Pro", " P", "Skyro")
    ]
)
def test_positive_delete_symbol(input_text, symbol, expected_output):
    string = StringUtils()
    assert string.delete_symbol(input_text, symbol) == expected_output


@pytest.mark.parametrize("input_text, symbol, expected_output", [
        ("Hello, \nWorld!", "\n", "Hello, World!"),
        ("python", "", "python"),
        ("python", "Y", "python"),
        ("Sky Pro", " r ", "Sky Pro")
    ]
)
def test_negative_delete_symbol(input_text, symbol, expected_output):
    string = StringUtils()
    assert string.delete_symbol(input_text, symbol) == expected_output


# Тесты для функции starts_with:
@pytest.mark.parametrize("input_text, symbol, expected_output", [
        ("+7 987-65-43", "+", True),
        ("python", "p", True),
        (":( Home Task", ":(", True)
    ]
)
def test_positive_starts_with(input_text, symbol, expected_output):
    string = StringUtils()
    assert string.starts_with(input_text, symbol) == expected_output


@pytest.mark.parametrize("input_text, symbol, expected_output", [
        ("SkyPro", "  ", False),
        ("SkyPro", "", False),
        ("python", "P", False)
    ]
)
def test_negative_starts_with(input_text, symbol, expected_output):
    string = StringUtils()
    assert string.starts_with(input_text, symbol) == expected_output


# Тесты для функции end_with:
@pytest.mark.parametrize("input_text, symbol, expected_output", [
        ("+7 987-65-43", "+", False),
        ("python", "n", True),
        ("python\n", "\n", True),
        (":( Home Task!", "!", True)
    ]
)
def test_positive_end_with(input_text, symbol, expected_output):
    string = StringUtils()
    assert string.end_with(input_text, symbol) == expected_output


@pytest.mark.parametrize("input_text, symbol, expected_output", [
        ("SkyPro", "O", False),
        ("SkyPro", "\n", False),
        ("python", "P", False)
    ]
)
def test_negative_end_with(input_text, symbol, expected_output):
    string = StringUtils()
    assert string.end_with(input_text, symbol) == expected_output


# Тесты для функции is_empty:
@pytest.mark.parametrize("input_text, expected_output", [
        (":(", False),
        (" python", False),
        ("   ", True),
        ("\t", True)
    ]
)
def test_positive_is_empty(input_text, expected_output):
    string = StringUtils()
    assert string.is_empty(input_text) == expected_output


@pytest.mark.parametrize("input_text, expected_output", [
        ("\n\r", True),
        (None, True)
    ]
)
def test_negative_is_empty(input_text, expected_output):
    string = StringUtils()
    assert string.is_empty(input_text) == expected_output


# Тесты для функции list_to_string:
@pytest.mark.parametrize("input_text, expected_output", [
        (["snow", "rain", "hail"], "snow, rain, hail"),
        (["01:ab:23:cd:45"], "01:ab:23:cd:45"),
        ([1, 1, 2, 3, 5, 8], "1, 1, 2, 3, 5, 8")
    ]
)
def test_positive_list_to_string_without_delimeter(input_text,
                                                   expected_output):
    string = StringUtils()
    assert string.list_to_string(input_text) == expected_output


@pytest.mark.parametrize("input_text, delimeter, expected_output", [
        (["snow", "rain", "hail"], ";", "snow;rain;hail"),
        (["01", "ab", "23", "cd", "45"], ":", "01:ab:23:cd:45"),
        (["Sky", "Pro"], ":)", "Sky:)Pro")
    ]
)
def test_positive_list_to_string_with_delimeter(input_text, delimeter,
                                                expected_output):
    string = StringUtils()
    assert string.list_to_string(input_text, delimeter) == expected_output


@pytest.mark.parametrize("input_text, expected_output", [
        ([" ", " ", " "], " ,  ,  "),
        (["", ""], ", ")
    ]
)
def test_negative_list_to_string_without_delimeter(input_text,
                                                   expected_output):
    string = StringUtils()
    assert string.list_to_string(input_text) == expected_output


@pytest.mark.parametrize("input_text, delimeter, expected_output", [
        (["Hello,", "World!"], "\n", "Hello,\nWorld!")
    ]
)
def test_negative_list_to_string_with_delimeter(input_text, delimeter,
                                                expected_output):
    string = StringUtils()
    assert string.list_to_string(input_text, delimeter) == expected_output
