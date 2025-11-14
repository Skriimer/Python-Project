width = int(input("Ширина прямоугольника: "))
height = int(input("Высота прямоугольника: "))
print("\n")

# 1. Прямоугольник
print("Прямоугольник:")
for i in range(height):
    print('*' * width)

print()

# 2. Прямоугольник с рамкой
print("Прямоугольник с рамкой:")
for i in range(height):
    if i == 0 or i == height - 1:
        print('*' * width)
    else:
        print('*' + ' ' * (width - 2) + '*')

print()

triangle_size = int(input("Размер треугольника: "))

print("\n")

# 3. Прямоугольный треугольник
print("Прямоугольный треугольник:")
for i in range(1, triangle_size + 1):
    print('*' * i)

print()

# 4. Равнобедренный треугольник
print("Равнобедренный треугольник:")
for i in range(triangle_size):
    spaces = ' ' * (triangle_size - i - 1)
    stars = '*' * (2 * i + 1)
    print(spaces + stars)

print()

# 5. Ромб
print("Ромб:")
# Верхняя часть
for i in range(triangle_size):
    spaces = ' ' * (triangle_size - i - 1)
    stars = '*' * (2 * i + 1)
    print(spaces + stars)
# Нижняя часть
for i in range(triangle_size - 2, -1, -1):
    spaces = ' ' * (triangle_size - i - 1)
    stars = '*' * (2 * i + 1)
    print(spaces + stars)

print()

# 6. Шахматная доска
print("Шахматная доска:")
size = 8  # стандартный размер шахматной доски
for i in range(size):
    for j in range(size):
        if (i + j) % 2 == 0:
            print('□', end=' ')
        else:
            print('■', end=' ')
    print()