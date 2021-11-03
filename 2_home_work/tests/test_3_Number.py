x = 2;
y = 2;
z = 4;


def summary(x, y):
    """"Функция возвращает сумму двух чисел"""
    return x + y


def test_1_number(fixture_greeting_function, fixture_greeting_module, fixture_greeting_session):
    """"Тест проверяет, что функция summary работает правильно"""
    assert summary(x, y) == z
