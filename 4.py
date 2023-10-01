my_dict = {'a': 50, 'b': 5, 'c': 56, 'd': 4, 'e': 58, 'f': 20}

# Найдите минимальное значение в словаре
min_value = min(my_dict.values())

# Создайте список ключей, у которых значение равно минимальному значению
min_keys = [key for key, value in my_dict.items() if value == min_value]

# Если у вас больше трех ключей с минимальным значением, возьмите только первые три
top_three = min_keys[:3]

print(top_three)