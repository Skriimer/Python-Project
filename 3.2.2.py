# Ввод данных
num1 = float(input("Первое число: "))
num2 = float(input("Второе число: "))
operation = input("Операция (+, -, *, /): ").strip()

# Выполнение операции и вывод результата
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 == 0:
        print("Ошибка: деление на ноль!")
        exit()
    else:
        result = num1 / num2
else:
    print("Неизвестная операция!")
    exit()

# Форматируем вывод
if result == int(result):
    result = int(result)
if num1 == int(num1):
    num1 = int(num1)
if num2 == int(num2):
    num2 = int(num2)

print(f"{num1:.1f} {operation} {num2:.1f} = {result:.1f}")