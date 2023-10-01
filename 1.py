def is_prime(num):
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5                # Начинаем проверку с i = 5.
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False # Если число делится на i или (i + 2) без остатка, оно не является простым.
        i += 6           # Увеличиваем i на 6 для оптимизации проверки простых чисел.
                         # Bсе простые числа больше 3 имеют форму 6k ± 1, где k - натуральное число.
    return True          # Если ни одно из условий не выполнилось, число является простым.

count = 0
num = 2
while count < 51:
    if is_prime(num):
        print(num)
        count += 1
    num += 1