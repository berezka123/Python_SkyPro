import pytest
import json


empty_dict = {}

company_list_json = """
[
    {
    "id": 111,
    "isActive": true,
    "createDateTime": "2024-04-05T17:30:00.713Z",
    "lastChangedDateTime": "2024-04-05T17:30:00.713Z",
    "name": "Барбершоп 'Цирюльникъ'",
    "description": "Крутые стрижки для крутых шишек"
    },
    {
    "id": 112,
    "isActive": true,
    "createDateTime": "2024-04-05T17:30:00.713Z",
    "lastChangedDateTime": "2024-04-05T17:30:00.713Z",
    "name": "Кондитерская Профи-троли",
    "description": "Сладко и точка"
    },
    {
    "id": 113,
    "isActive": true,
    "createDateTime": "2024-04-05T17:30:00.713Z",
    "lastChangedDateTime": "2024-04-05T17:30:00.713Z",
    "name": "Муж на час",
    "description": "Помощь в делах"
    }
]
"""

def test_read_error():
    with pytest.raises(KeyError):
        value = empty_dict["key"]
        assert value == None

def test_get_read_error():
    value = empty_dict.get("key", "По Вашему запросу ничего не найдено :(")
    assert value == "По Вашему запросу ничего не найдено :("

def test_json_parsing():
    company_list = json.loads(company_list_json)
    assert len(company_list) == 3
    company_one = company_list[0]
    assert company_one["name"] == "Барбершоп 'Цирюльникъ'"