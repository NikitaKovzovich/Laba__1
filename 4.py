my_dict = {'a': 50, 'b': 5, 'c': 56, 'd': 4, 'e': 58, 'f': 20}

min_value = min(my_dict.values())

min_keys = [key for key, value in my_dict.items() if value == min_value]

top_three = min_keys[:3]

print(top_three)
