def values(dires):
    dires = [1,2,3,4]
    g = (dires[i:] + dires[:i] for i in range(len(values)))
    dires.append(g)
    print(dires)

    return dires

print(type(values))

def print_check(honey_positions):
    sum = 0  # переменная для накопления общей суммы
    print("ООО Медовый Гексагон\n")
    # в цикле будем выводить название, количество и цену

    for honey in honey_positions:
        name = honey[0]
        amount = honey[1]
        price = honey[2]
        print(f"{name} ({amount} шт.) - {price} руб.")
        sum += amount * price  # здесь же будем считать ещё и общую сумму

    print(f"\nИтого: {sum} руб.")
    print("Спасибо за покупку!")

print(print_check(honey_positions = [
        ("Мёд липовый", 3, 1250),
        ("Мёд цветочный", 7, 1000),
        ("Мёд гречишный", 6, 1300),
        ("Донниковый мёд", 1, 1750),
        ("Малиновый мёд", 10, 2000),
    ]))