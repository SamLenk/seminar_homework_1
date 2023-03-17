ticket_number = input("Введите номер билета: ")

# Проверяем, что введенное значение содержит 6 цифр
if len(ticket_number) != 6 or not ticket_number.isdigit():
    print("Неверный формат номера билета")
else:
    # Получаем суммы первых и последних трех цифр
    sum_first_digits = sum(int(digit) for digit in ticket_number[:3])
    sum_last_digits = sum(int(digit) for digit in ticket_number[3:])

    # Проверяем, является ли билет счастливым
    if sum_first_digits == sum_last_digits:
        print("Этот билет счастливый!")
    else:
        print("Этот билет несчастливый :(")