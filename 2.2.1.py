print("Калькулятор с пошаговым вычислением\nВведите три числа:")
print("a = ",end="")
a=int(input())
print("b = ",end="")
b=int(input())
print("c = ",end="")
c=int(input())
print(f"\nВычисляем: {a:.1f} + {b:.1f} * {c:.1f} - {a:.1f} ** 2 / {b:.1f}")
r1=a**2
print(f"Шаг 1: {a:.1f} ** 2 = {r1:.1f}")
r2=b*c
print(f"Шаг 2: {b:.1f} * {c:.1f} = {r2:.1f}")
r3=r1/b
print(f"Шаг 3: {r1:.1f} / {b:.1f} = {r3}")
r4=a+r2
print(f"Шаг 4: {a:.1f} + {r2:.1f} = {r4:.1f}")
r5=r4-r3
print(f"Шаг 5: {r4:.1f} - {r3} = {r5}")
print(f"\nИтоговый результат: {r5:.3f}")