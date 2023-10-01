# Словарь с информацией о товарах
toy_store = {
    "Мяч": ["Красный мяч для игры в футбол", 10.0, 50],
    "Кукла": ["Кукла с аксессуарами", 15.0, 30],
    "Пазл": ["Пазл с изображением динозавров", 20.0, 25],
    "Машинка": ["Игрушечная машинка", 12.0, 40],
    "Конструктор": ["Конструктор с разноцветными деталями", 25.0, 20],
}


def show_description():
    print("Описание игрушек:")
    for toy, info in toy_store.items():
        print(f"{toy} - {info[0]}")


def show_price():
    print("Цены на игрушки:")
    for toy, info in toy_store.items():
        print(f"{toy} - {info[1]} руб.")


def show_quantity():
    print("Количество игрушек в магазине:")
    for toy, info in toy_store.items():
        print(f"{toy} - {info[2]} шт.")


def show_all_info():
    print("Информация о товарах:")
    for toy, info in toy_store.items():
        print(f"{toy}:")
        print(f"Описание: {info[0]}")
        print(f"Цена: {info[1]} руб.")
        print(f"Количество: {info[2]} шт.")
        print()


def buy_toys():
    total_cost = 0
    while True:
        print("Список доступных игрушек:")
        index = 1
        for toy in toy_store.keys():
            print(f"{index}. {toy}")
            index += 1

        choice = input("Введите номер игрушки, которую хотите купить (или введите '0' для выхода): ")

        if choice == '0':
            break

        if not choice.isdigit():
            print("Неверный формат ввода. Попробуйте снова.")
            continue

        choice = int(choice)

        if choice < 1 or choice > len(toy_store):
            print("Неверный номер игрушки. Попробуйте снова.")
            continue

        toy_names = list(toy_store.keys())
        selected_toy = toy_names[choice - 1]

        quantity_to_buy = input(f"Введите количество для покупки {selected_toy} (или '0' для отмены): ")

        if quantity_to_buy == '0':
            continue

        if not quantity_to_buy.isdigit():
            print("Неверный формат ввода. Покупка отменена.")
            continue

        quantity_to_buy = int(quantity_to_buy)

        if quantity_to_buy <= 0 or quantity_to_buy > toy_store[selected_toy][2]:
            print("Недопустимое количество. Попробуйте снова.")
            continue

        cost = toy_store[selected_toy][1] * quantity_to_buy
        total_cost += cost
        toy_store[selected_toy][2] -= quantity_to_buy

        print(f"Вы купили {quantity_to_buy} шт. {selected_toy} за {cost} руб. Ваша общая сумма: {total_cost} руб.")

    print(f"Общая сумма покупки: {total_cost} руб.")
    print("Остаток товаров в магазине:")
    show_quantity()


def main():
    while True:
        print("\nМеню:")
        print("1. Просмотр описания")
        print("2. Просмотр цены")
        print("3. Просмотр количества")
        print("4. Вся информация")
        print("5. Покупка")
        print("6. До свидания")

        choice = input("Выберите пункт меню: ")

        if choice == '1':
            show_description()
        elif choice == '2':
            show_price()
        elif choice == '3':
            show_quantity()
        elif choice == '4':
            show_all_info()
        elif choice == '5':
            buy_toys()
        elif choice == '6':
            print("До свидания!")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


if name == "main":
    main()