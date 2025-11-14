# Ввод данных
print(f"Введите имя:",end=" ")
first_name=input()
print(f"Введите фамилию:",end=" ")
last_name=input()
# Приведение к нижнему регистру для email
first_name_lower = first_name.lower()
last_name_lower = last_name.lower()

# Создание email адресов
full_email = f"{first_name_lower}.{last_name_lower}@school.ru"
short_email = f"{first_name_lower[0]}{last_name_lower}@school.ru"

# Вывод результатов
print("\nВаши данные:")
print(f"Имя: {first_name}")
print(f"Фамилия: {last_name}")
print(f"Email (полный): {full_email}")
print(f"Email (короткий): {short_email}")