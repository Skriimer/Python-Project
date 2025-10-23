import math

print("=== Геометрический калькулятор ===")
print("1. Круг")
print("2. Прямоугольник")
print("3. Треугольник")
print("\nВыберите фигуру (1-3): ",end="")
choice = int(input())

if choice == 1:
    # Круг
#    print(" Введите радиус: ",end="")
#    radius = float(input())
    radius = float(input("Введите радиус: "))
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius   
    print(f"\n\nКруг с радиусом {radius:.1f}:")
    print(f"Площадь: {area:.2f}")
    print(f"Длина окружности: {circumference:.2f}")

elif choice == 2:
    # Прямоугольник
    print("\nВведите длину: ")
    length = float(input())
    print("\nВведите ширину: ")
    width = float(input())
    
    area = length * width
    perimeter = 2 * (length + width)
    diagonal = math.sqrt(length ** 2 + width ** 2)
    
    print(f"\n\nПрямоугольник {length} x {width}:")
    print(f"Площадь: {area:.2f}")
    print(f"Периметр: {perimeter:.2f}")
    print(f"Диагональ: {diagonal:.2f}")

elif choice == 3:
    # Треугольник
    print("\nВведите сторону a: ")
    a = float(input())
    print("Введите сторону b: ")
    b = float(input())
    print("Введите сторону c: ")
    c = float(input())
    
    # Проверка на существование треугольника
    if a + b > c and a + c > b and b + c > a:
        perimeter = a + b + c
        # Формула Герона
        p = perimeter / 2
        area = math.sqrt(p * (p - a) * (p - b) * (p - c))
        
        print(f"\n\nТреугольник со сторонами {a}, {b}, {c}:")
        print(f"Периметр: {perimeter:.2f}")
        print(f"Площадь: {area:.2f}")
    else:
        print(f"\n\nТреугольник с такими сторонами не существует!")

else:
    print("Неверный выбор! Пожалуйста, выберите от 1 до 3.")