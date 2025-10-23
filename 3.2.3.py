# Ввод данных
a = float(input("Сторона a: "))
b = float(input("Сторона b: "))
c = float(input("Сторона c: "))

# Проверка существования треугольника
triangle_exists = True
violation = ""

if a + b <= c:
    triangle_exists = False
    violation = f"a + b = {a + b} ≤ c = {c}"
elif a + c <= b:
    triangle_exists = False
    violation = f"a + c = {a + c} ≤ b = {b}"
elif b + c <= a:
    triangle_exists = False
    violation = f"b + c = {b + c} ≤ a = {a}"

# Если треугольник не существует
if not triangle_exists:
    print("Треугольник не существует")
    print(violation)
else:
    # Вычисление периметра
    perimeter = a + b + c
    
    # Определение типа треугольника
    triangle_type = ""
    
    # Проверка на равносторонний
    if a == b == c:
        triangle_type = "равносторонний"
    # Проверка на равнобедренный
    elif a == b or a == c or b == c:
        triangle_type = "равнобедренный"
    else:
        triangle_type = "разносторонний"
    
    # Проверка на прямоугольный (с учетом погрешности вычислений)
    sides = sorted([a, b, c])
    is_right = abs(sides[2]**2 - (sides[0]**2 + sides[1]**2)) < 1e-10
    
    # Добавление информации о прямоугольности
    if is_right:
        triangle_type += " прямоугольный"
    
    # Вывод результатов
    print("Треугольник существует")
    print(f"Тип треугольника: {triangle_type}")
    print(f"Периметр: {perimeter}")