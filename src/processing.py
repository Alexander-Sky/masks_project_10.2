from src.processing import filter_by_state, sort_by_date

# Тестовые данные
test_data = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]

# Тесты для filter_by_state
def test_filter_executed():
    result = filter_by_state(test_data)
    assert len(result) == 2
    assert all(item['state'] == 'EXECUTED' for item in result)

def test_filter_canceled():
    result = filter_by_state(test_data, 'CANCELED')
    assert len(result) == 2
    assert all(item['state'] == 'CANCELED' for item in result)

# Тесты для sort_by_date
def test_sort_desc():
    result = sort_by_date(test_data)
    expected_order = [
        '2019-07-03T18:35:29.512364',
        '2018-10-14T08:21:33.419441',
        '2018-09-12T21:27:25.241689',
        '2018-06-30T02:08:58.425572'
    ]
    assert [item['date'] for item in result] == expected_order

def test_sort_asc():
    result = sort_by_date(test_data, False)
    expected_order = [
        '2018-06-30T02:08:58.425572',
        '2018-09-12T21:27:25.241689',
        '2018-10-14T08:21:33.419441',
        '2019-07-03T18:35:29.512364'
    ]
    assert [item['date'] for item in result] == expected_order