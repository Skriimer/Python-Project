# Первая часть: вывод первых N чисел Фибоначчи
print(f"Сколько чисел Фибоначчи вывести?",end=" ")
n = int(input())

if n <= 0:
    print("Пожалуйста, введите положительное число")
else:
    fib_sequence = []
    a, b = 0, 1
    
    for i in range(n):
        fib_sequence.append(str(a))
        a, b = b, a + b
    
    print(" ".join(fib_sequence),end="")
print(" ")
print()
# Вторая часть: проверка числа на принадлежность к числам Фибоначчи
print("Проверка числа:")
check_num = int(input("Введите число для проверки: "))

# Генерируем числа Фибоначчи до тех пор, пока не превысим проверяемое число
a, b = 0, 1
is_fibonacci = False

while a <= check_num:
    if a == check_num:
        is_fibonacci = True
        break
    a, b = b, a + b

if is_fibonacci:
    print(f"{check_num} - число Фибоначчи")
else:
    print(f"{check_num} - НЕ число Фибоначчи")