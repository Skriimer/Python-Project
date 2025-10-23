# Ввод данных
days_in_month = int(input("Дней в месяце: "))
first_day = int(input("День недели 1 числа (1-пн, 7-вс): "))

print("\n")

# Базовая версия календаря
print("Пн Вт Ср Чт Пт Сб Вс")
print("-" * 21)

# Вычисляем отступ для первого дня
current_position = 1

# Печатаем пробелы до первого дня
for i in range(1, first_day):
    print("   ", end="")
    current_position += 1

# Печатаем дни месяца
for day in range(1, days_in_month + 1):
    # Форматируем вывод дня (выравнивание по правому краю)
    print(f"{day:2}", end=" ")
    
    # Переход на новую строку после воскресенья
    if current_position % 7 == 0:
        print()
    
    current_position += 1

# Добавляем пустую строку в конце, если последняя неделя не завершена
if (current_position - 1) % 7 != 0:
    print()