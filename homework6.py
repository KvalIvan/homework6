my_dict = {'Ivan': 23, 'Vlad': 30, 'Max': 17, 'Kirill': 16}
print(my_dict)
print(my_dict['Vlad'])  # Тут можно сделать либо через get а можно и без просто когда мы знаем
# Что в словаре есть данный ключ то можно не указывать get
print(my_dict.get('Eva'))
my_dict.update({'Anton': 23, 'Sasha': 24})
a = my_dict.pop('Ivan')
print(a)
print(my_dict)

print('')  # Решил добавить ещё один принт чтобы отедить первую задачу от второй

my_set = {1, 2, 4, 4, 2, 'slovo', 'slovo', 'Games', True}
print(my_set)
(my_set.add(5))
(my_set.add('Valorant'))
(my_set.discard(4))  # Решил сделать через discard чтобы не было ошибки если элемета в о множестве нету
print(my_set)