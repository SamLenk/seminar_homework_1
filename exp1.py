number = input("Введите число: ")

# Находим сумму цифр числа
digit_sum = sum(int(digit) for digit in str(number) if digit.isdigit())

# Выводим результат на экран
print("Сумма цифр числа:", digit_sum)