my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# генератор списка
even_numbers = [x for x in my_tuple if x % 2 == 0]

# Вычисляем сумму четных элементов
sum_of_even_numbers = sum(even_numbers)

print("Сумма четных элементов:", sum_of_even_numbers)