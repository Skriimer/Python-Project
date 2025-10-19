# Запрос двух строк
print(f"Введите первую строку:",end=" ")
string1 = input()
print(f"Введите вторую строку:",end=" ")
string2 = input()
print()
print()
# Вывод меню операций
print("Выберите операцию:")
print("1. Объединить строки")
print("2. Повторить первую строку")
print("3. Проверить вхождение")
print("4. Сравнить длины")

# Запрос выбора операции
print(f"\nВаш выбор (1-4):",end=" ")
choice = input("")

# Выполнение выбранной операции
if choice == "1":
    # Операция 1: Объединить строки
    # result = string1 + string2
    print(f"Результат: {string1} {string2}")
    
elif choice == "2":
    # Операция 2: Повторить первую строку
    try:
        print(f"\nСколько раз повторить?",end=" ")
        n = int(input())
        result = string1 * n
        print(f"\nРезультат: {result}")
    except ValueError:
        print("\nОшибка: введите целое число!")
        
elif choice == "3":
    # Операция 3: Проверить вхождение
    if string1 in string2:
        print(f"\n'{string1}' входит в '{string2}'")
    else:
        print(f"\n'{string1}' НЕ входит в '{string2}'")
        
elif choice == "4":
    # Операция 4: Сравнить длины
    len1 = len(string1)
    len2 = len(string2)
    print(f"\nДлина первой строки: {len1}")
    print(f"Длина второй строки: {len2}")
    
    if len1 > len2:
        print("Первая строка длиннее")
    elif len1 < len2:
        print("Вторая строка длиннее")
    else:
        print("Строки одинаковой длины")
        
else:
    # Неверный выбор
    print("\nНеверный выбор!")