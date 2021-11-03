# tuple - кортежи, те же списки, нельзя изменять или добавлять

# t = (1,2,3)
# t2 = tuple((1,2,3))
# print(type(t), t)
# print(type(t2), t2)
# print(t[1])

# Unchangeable
# t[1] = 1

# Iterate
# t = (1,2,3)
# for i in t:
#     print(i)

# Get len
# t = (1,2,3)
# print(len(t), t)

# Can be a key
# d = {'1': 'string', (1,2,3): 'tuple'}
# print(d[(1,2,3)])


t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)


def test_1_tuple(fixture_greeting_function, fixture_greeting_module, fixture_greeting_session):
    """"Тест проверяет сумму двух первых элементов кортежа"""
    k = t[0] + t[1];
    assert (k == 3)


def test_2_tuple(fixture_greeting_function, fixture_greeting_module, fixture_greeting_session):
    """"Тест проверяет длинну кортежа"""
    assert (len(t) == 10)
