my_string = "My string"


def test_1_string(fixture_greeting_function, fixture_greeting_module, fixture_greeting_session):
    """"Тест проверяет, что длинна строки равна 9"""
    assert len(my_string) == 9


def test_2_string(fixture_greeting_function, fixture_greeting_module, fixture_greeting_session):
    """"Тест проверяет, что длинна строки*3 равна 27"""
    assert len(my_string)*3 == 27
