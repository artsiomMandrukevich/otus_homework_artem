# dict - словарь

# CRUD (create, remove, update, delete)

# d = {}
# d['key'] = 'value'
# d['key'] = 'new_value'
# del d['key']
# del d
#
# # Iterate
# d = {'1': 'one', '2': 'two', '3': 'three', '4': 'four', '0': 'zero'}
#
# for i in d:
#     print(i)
#
# print("-----------------")
#
# for k in d.keys():
#     print(k)
#
# print("-----------------")
#
# for v in d.values():
#     print(v)
#
# print("-----------------")
#
# for i in d.items():
#     print(i)
#
# print("-----------------")
#
# for k,v in d.items():
#     print(k, v)
#
# print("-----------------")
#
# # Unordered
# # Справедливо для работы с большими словарями
# # https://www.quora.com/Are-Python-dictionaries-unordered


d = {}
d = {'status': 'OK', 'value': 2}


def test_1_dict(fixture_greeting_function, fixture_greeting_module, fixture_greeting_session):
    """"Тест проверяет, что значение для ключа status равно OK"""
    assert (d['status'] == 'OK')


def test_2_dict(fixture_greeting_function, fixture_greeting_module, fixture_greeting_session):
    """"Тест проверяет, что значение для ключа value*2 равно 4"""
    assert (d['value'] * 2 == 4)


def test_3_dict(fixture_greeting_function, fixture_greeting_module, fixture_greeting_session):
    """"Тест добавляет пару ключ-значение в словарь, проверяет что длинна словаря увеличилась"""
    d['second'] = 'second_value'
    assert (len(d) == 3)
