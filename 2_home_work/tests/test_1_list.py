my_list = [1, 2, 3, 4, 5]


def test_list(fixture_greeting_function, fixture_greeting_module, fixture_greeting_session):
    """"Тест проверяет, что длинна списка равна 5"""
    assert len(my_list) == 5
