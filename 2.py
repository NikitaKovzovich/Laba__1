input_string = input("Введите строку текста: ")
character_count = {}

for char in input_string:
    if char in character_count:
        character_count[char] += 1
    else:
        # Если символа нет в словаре, добавляем его и устанавливаем счетчик в 1
        character_count[char] = 1

# Находим символ с наибольшим счетчиком
most_common_character = max(character_count, key=character_count.get) # Значение по ключу

print(f"Символ, который появляется наиболее часто: {most_common_character}")

reversed_string = input_string[::-1]
print(f"Строка в обратном порядке: {reversed_string}")