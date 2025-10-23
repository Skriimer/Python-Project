print("=== Система проверки допуска ===")
print()
# Ввод данных
age = int(input("Введите возраст: "))
income = float(input("Введите месячный доход: "))
has_passport = input("Есть паспорт? (да/нет): ").lower().strip()
has_criminal_record = input("Есть судимость? (да/нет): ").lower().strip()
credit_history = input("Кредитная история (хорошая/плохая/нет): ").lower().strip()

print("\n=== Результаты проверки ===")

# Проверка водительских прав
driver_license_conditions = []
can_get_driver_license = True

if age < 18:
    driver_license_conditions.append("Недостаточный возраст")
    can_get_driver_license = False
if has_passport != 'да':
    driver_license_conditions.append("Нет паспорта")
    can_get_driver_license = False
if has_criminal_record == 'да':
    driver_license_conditions.append("Есть судимость")
    can_get_driver_license = False

if can_get_driver_license:
    print("Водительские права: ✓ Можно получить")
else:
    print("Водительские права: ✗ Нельзя получить")
    for condition in driver_license_conditions:
        print(f"  - {condition}")

# Проверка кредита
credit_conditions = []
can_get_credit = True

if age < 21 or age > 65:
    credit_conditions.append("Неподходящий возраст")
    can_get_credit = False
if income < 30000:
    credit_conditions.append("Недостаточный доход")
    can_get_credit = False
if has_passport != 'да':
    credit_conditions.append("Нет паспорта")
    can_get_credit = False
if credit_history == 'плохая':
    credit_conditions.append("Плохая кредитная история")
    can_get_credit = False

if can_get_credit:
    print("\nКредит: ✓ Можно получить")
else:
    print("\nКредит: ✗ Нельзя получить")
    for condition in credit_conditions:
        print(f"  - {condition}")

# Проверка ипотеки
mortgage_conditions = []
can_get_mortgage = True

if age < 21 or age > 65:
    mortgage_conditions.append("Неподходящий возраст")
    can_get_mortgage = False
if income < 60000:
    mortgage_conditions.append("Недостаточный доход")
    can_get_mortgage = False
if has_passport != 'да':
    mortgage_conditions.append("Нет паспорта")
    can_get_mortgage = False
if credit_history != 'хорошая':
    mortgage_conditions.append("Не хорошая кредитная история")
    can_get_mortgage = False

if can_get_mortgage:
    print("\nИпотека: ✓ Можно получить")
else:
    print("\nИпотека: ✗ Нельзя получить")
#    for condition in mortgage_conditions:
#        print(f"  - {condition}")

# Проверка социальных льгот
social_benefits = []
has_social_benefits = False

if age >= 65:
    social_benefits.append("Пенсионер")
    has_social_benefits = True
if 18 <= age <= 25:
    social_benefits.append("Студенческий возраст")
    has_social_benefits = True
if income < 20000:
    social_benefits.append("Низкий доход")
    has_social_benefits = True

if has_social_benefits:
    print("\nСоциальные льготы: ✓ Положены")
    for benefit in social_benefits:
        print(f"  - {benefit}")
else:
    print("\nСоциальные льготы: ✗ Не положены")