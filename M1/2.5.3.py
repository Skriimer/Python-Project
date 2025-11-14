import math

# Хранилище данных студентов
students = []

print("=== Мини-база данных студентов ===\n")

while True:
    print("1. Добавить студента")
    print("2. Показать статистику")
    print("3. Выход")
    
    choice = input("\nВыбор: ").strip()
    print()
    if choice == '1':
        print("\n--- Добавление студента ---")
        
        # Ввод имени
        while True:
            name = input("Имя: ").strip()
            if not name:
                print("Ошибка: имя не может быть пустым!")
                continue
            break
        
        # Ввод возраста
        while True:
            try:
                age = input("Возраст: ").strip()
                age = int(age)
                if age < 16 or age > 100:
                    print("Ошибка: возраст должен быть от 16 до 100!")
                    continue
                break
            except ValueError:
                print("Ошибка: введите число!")
        
        # Ввод среднего балла
        while True:
            try:
                gpa = input("Средний балл (0-5): ").strip()
                gpa = float(gpa)
                if gpa < 0 or gpa > 5:
                    print("Ошибка: балл должен быть от 0 до 5!")
                    continue
                break
            except ValueError:
                print("Ошибка: введите число!")
        
        # Ввод информации о стипендии
        while True:
            scholarship = input("Получает стипендию? (да/нет): ").strip().lower()
            if scholarship in ['да', 'д', 'yes', 'y']:
                has_scholarship = True
                break
            elif scholarship in ['нет', 'н', 'no', 'n']:
                has_scholarship = False
                break
            else:
                print("Ошибка: введите 'да' или 'нет'!")
        
        # Добавление студента в базу
        student = {
            'name': name,
            'age': age,
            'gpa': gpa,
            'has_scholarship': has_scholarship
        }
        students.append(student)
        
        print("✓ Студент добавлен!\n")
    
    elif choice == '2':
        if not students:
            print("\nБаза данных пуста!\n")
            continue
        
        print("\n" + "="*50)
        print("СТАТИСТИКА БАЗЫ ДАННЫХ")
        print("="*50)
        
        total_students = len(students)
        print(f"Всего студентов: {total_students}\n")
        
        # Статистика по возрасту
        ages = [student['age'] for student in students]
        min_age = min(ages)
        max_age = max(ages)
        avg_age = sum(ages) / len(ages)
        
        print("Возраст:")
        print(f"  - Минимальный: {min_age}")
        print(f"  - Максимальный: {max_age}")
        print(f"  - Средний: {avg_age:.1f}\n")
        
        # Статистика по успеваемости
        gpas = [student['gpa'] for student in students]
        min_gpa = min(gpas)
        max_gpa = max(gpas)
        avg_gpa = sum(gpas) / len(gpas)
        
        print("Успеваемость:")
        print(f"  - Минимальный балл: {min_gpa:.2f}")
        print(f"  - Максимальный балл: {max_gpa:.2f}")
        print(f"  - Средний балл: {avg_gpa:.2f}\n")
        
        # Статистика по стипендии
        scholarship_count = sum(1 for student in students if student['has_scholarship'])
        no_scholarship_count = total_students - scholarship_count
        scholarship_percent = (scholarship_count / total_students) * 100
        no_scholarship_percent = (no_scholarship_count / total_students) * 100
        
        print("Стипендия:")
        print(f"  - Получают: {scholarship_count} ({scholarship_percent:.1f}%)")
        print(f"  - Не получают: {no_scholarship_count} ({no_scholarship_percent:.1f}%)\n")
        
        # Лучшие студенты
        best_students = [student for student in students if student['gpa'] >= 4.5]
        if best_students:
            print("Лучшие студенты (GPA >= 4.5):")
            for student in best_students:
                print(f"  - {student['name']}: {student['gpa']:.2f}")
        else:
            print("Лучшие студенты (GPA >= 4.5):")
            print("  - Нет студентов с GPA >= 4.5")
        print()
        
        # Распределение по возрасту
        age_groups = {
            '16-18': 0,
            '19-21': 0,
            '22-24': 0,
            '25+': 0
        }
        
        for age in ages:
            if 16 <= age <= 18:
                age_groups['16-18'] += 1
            elif 19 <= age <= 21:
                age_groups['19-21'] += 1
            elif 22 <= age <= 24:
                age_groups['22-24'] += 1
            else:
                age_groups['25+'] += 1
        
        print("Распределение по возрасту:")
        for group, count in age_groups.items():
            if count > 0:
                percent = (count / total_students) * 100
                print(f"  - {group} лет: {count} ({percent:.1f}%)")
        
        print()
    
    elif choice == '3':
        print("До свидания!")
        break
    
    else:
        print("\nНеверный выбор!\n")