my_dict = {}

first_key = input('Введите ключ 1:')
first_mean = input('Введите значение 1 к ключу 1:')
my_dict[first_key] = first_mean

secound_key = input('Введите ключ 2:')
secound_mean = input('Введите значение 2 к ключу 2:')
my_dict[secound_key] = secound_mean

third_key = input('Введите ключ 3:')
third_mean = input('Введите значение 3 к ключу 3:')
my_dict[third_key] = third_mean


my_dict['brand'] = 'bmw'
my_dict['color'] = 'green'
print(len(my_dict))
print(my_dict['brand'])
print(my_dict.get('color'))
del my_dict['size']
new_dict = my_dict.copy()
new_dict['where'] = 'UK'
print(new_dict.items())
print(list(new_dict.popitem()))
print(new_dict.keys())
print(new_dict)
print(new_dict.clear())

print(my_dict)
print(new_dict)
