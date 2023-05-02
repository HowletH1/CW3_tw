from utils import *


def test_select():
    assert select([{"state": "EXECUTED"}, {"state": "EXECUTED"}, {"state": "CANCELED"}]) == \
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
