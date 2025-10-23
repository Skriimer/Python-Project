print("=== Логический калькулятор ===")
print("Введите значения переменных (True/False или 1/0):\n")

# Ввод значений
print("A = ",end="")
A = bool(input())
print("B = ",end="")
B = bool(input())
print("C = ",end="")
C = bool(input())
B=False
print(f"\nИсходные значения: A={A}, B={B}, C={C}")

print("\n=== Базовые операции ===")
print(f"A and B = {A and B}")
print(f"A or B = {A or B}")
print(f"not A = {not A}")
print(f"A and not B = {A and not B}")
print(f"not A or B = {not A or B}")

print("\n=== Сложные выражения ===")
print(f"(A and B) or C = {(A and B) or C}")
print(f"A and (B or C) = {A and (B or C)}")
print(f"not (A and B) = {not (A and B)}")
print(f"(not A) or (not B) = {(not A) or (not B)} (закон де Моргана)")
print(f"(A or B) and (B or C) and (A or C) = {(A or B) and (B or C) and (A or C)}")
print()
#print("Импликация и эквивалентность:")
# Импликация A → B эквивалентна not A or B
print(f"A → B (импликация) = {not A or B}")
# Эквивалентность A ↔ B эквивалентна (A and B) or (not A and not B)
print(f"A ↔️ B (эквивалентность) = {(A and B) or (not A and not B)}")