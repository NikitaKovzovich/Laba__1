my_list = [13, 56, 'Python', 34, 19, 'love']

for i in range(len(my_list)):
    if isinstance(my_list[i], int): # является ли элемент целым числом
        if my_list[i] % 2 == 0:  # чётное ли число
            digits = [int(digit) for digit in str(my_list[i])]
            rez = 1
            for digit in digits:
                rez *= digit
            my_list[i] = rez
        else:
            # Если число нечётное, заменяем его на 1
            my_list[i] = 1

print(my_list)