from utils import *


def test_select():
    assert select([{"state": "EXECUTED"}, {"state": "EXECUTED"}, {"state": "CANCELED"}]) == \
           [{"state": "EXECUTED"}, {"state": "EXECUTED"}]
    assert select([{"state": "EXECUTED"}, {"state": "EXECUTED"}, {"stat": " "}]) == \
           [{"state": "EXECUTED"}, {"state": "EXECUTED"}]


def test_sort():
    assert sorted_operations([{"date": "2019-08-26T10:50:58.294041"}, {"date": "2019-07-03T18:35:29.512364"},
                              {"date": "2018-06-30T02:08:58.425572"}]) == \
           [{"date": "2019-08-26T10:50:58.294041"}, {"date": "2019-07-03T18:35:29.512364"},
            {"date": "2018-06-30T02:08:58.425572"}]


def test_hide():
    assert hide_numbers("Счет 75106830613657916952") == "Счет **6952"
    assert hide_numbers("Visa Classic 6831982476737658") == "Visa Classic 6831 98** **** 7658"
    assert hide_numbers("Maestro 7810846596785568") == "Maestro 7810 84** **** 5568"


def test_output():
    assert last_operations([{"date": "2019-12-07T06:17:14.634890", "description": "Перевод организации",
                             "from": "Visa Classic 2842878893689012", "to": "Счет 35158586384610753655",
                             "operationAmount": {"amount": "48150.39", "currency": {"name": "USD"}}}]) == \
           ["07.12.2019 Перевод организации \nVisa Classic 2842 87** **** 9012 -> Счет **3655\n48150.39 USD\n"]

    assert last_operations([{"date": "2019-08-26T10:50:58.294041", "description": "Перевод организации",
                             "to": "Счет 64686473678894779589",
                             "operationAmount": {"amount": "31957.58", "currency": {"name": "руб."}}}]) == \
           ["26.08.2019 Перевод организации \n -> Счет **9589\n31957.58 руб.\n"]
