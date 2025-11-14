# Ввод данных
number = input("Введите натуральное число: ")

# Проверка, что введено число
if not number.isdigit():
    print("Ошибка: введено не натуральное число!")
else:
    # Вычисление суммы цифр
    digit_sum = 0
    for digit in number:
        digit_sum += int(digit)
    
    # Вывод результата
    print(f"Сумма цифр числа {number} = {digit_sum}")