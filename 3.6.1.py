# Ввод данных
n = int(input("До какого числа (N): "))
m = int(input("До какой степени (M): "))
print()
# Заголовок таблицы
print("Число\t", end="")
for power in range(1, m + 1):
    print(f"^{power}\t", end="")
print()

# Разделительная линия
line_length = 8 + m * 8  # 8 символов для "Число" + по 8 на каждую степень
print("-" * line_length)

# Заполнение таблицы
for number in range(1, n + 1):
    print(f"{number}\t", end="")
    for power in range(1, m + 1):
        result = number ** power
        print(f"{result}\t", end="")
    print()