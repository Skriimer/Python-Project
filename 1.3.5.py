number = int(input("Введите целое число: "))
is_even = number % 2 == 0
digit_count = len(str(abs(number)))

if number > 0:
    sign = "положительное"
elif number < 0:
    sign = "отрицательное"
else:
    sign = "Это ноль"

print("\nИнформация о числе", number, ":")
print(f"Тип: {type(number)}")
print(f"Четное: {is_even}")
print(f"Количество цифр: {digit_count}")
print(f"Число {sign}")