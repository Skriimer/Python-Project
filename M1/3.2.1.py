# Ввод данных
x = float(input("Введите координату X: "))
y = float(input("Введите координату Y: "))

# Определение положения точки
if x == 0 and y == 0:
    result = "Начало координат"
elif x == 0 and y != 0:
    result = "На оси Y"
elif y == 0 and x != 0:
    result = "На оси X"
elif x > 0 and y > 0:
    result = "I четверть"
elif x < 0 and y > 0:
    result = "II четверть"
elif x < 0 and y < 0:
    result = "III четверть"
elif x > 0 and y < 0:
    result = "IV четверть"

# Вывод результата
print(f"Точка ({x}, {y}) находится: {result}")