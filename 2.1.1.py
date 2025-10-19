# Запрашиваем число у пользователя
print(f"Введите число:",end=" ")
user_input = input()
# Проверяем, что ввели только цифры и может быть минус в начале
is_number = True

# Если строка пустая - это не число
if user_input == "":
    is_number = False
else:
    # Проверяем каждый символ в строке
    for i in range(len(user_input)):
        char = user_input[i]
        
        # Первый символ может быть минусом
        if i == 0 and char == '-':
            continue
        
        # Все символы должны быть цифрами
        if char not in "0123456789":
            is_number = False
            break

# Если это число, анализируем его
if is_number:
    number = int(user_input)
    
    print(f"\nЭто целое число: {number}")
    print("")
    print(f"Анализ числа {number}:")
    print(f"Тип: int")
    
    # Находим абсолютное значение (без знака)
    if number < 0:
        absolute_value = -number
    else:
        absolute_value = number
    print(f"Абсолютное значение: {absolute_value}")
    
    # Определяем знак
    if number > 0:
        print("Знак: положительное")
    elif number < 0:
        print("Знак: отрицательное")
    else:
        print("Знак: это ноль")
    
    # Проверяем четность
    if number % 2 == 0:
        print("Четное: да")
    else:
        print("Четное: нет")
    
    # Проверяем делимость на 3
    if number % 3 == 0:
        print("Делится на 3: да")
    else:
        print("Делится на 3: нет")
    
    # Проверяем делимость на 5
    if number % 5 == 0:
        print("Делится на 5: да")
    else:
        print("Делится на 5: нет")

else:
    print("Ошибка: это не целое число!")