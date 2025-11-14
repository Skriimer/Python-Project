# Ввод данных
print(f"Название товара:",end=" ")
product_name=input()
print(f"\nЦена за единицу:",end=" ")
price=float(input())
print(f"\nКоличество:",end=" ")
quantity=int(input())
print("\n")
# Расчет общей стоимости
total = price * quantity

# Вывод чека с форматированием чисел
print("=" * 40)
print("         КАССОВЫЙ ЧЕК")
print("=" * 40)
print(f"Товар: {product_name}")
print(f"Цена:  {price:.2f} руб.")
print(f"Кол-во: {quantity} шт.")
print("-" * 40)
print(f"ИТОГО: {total:.2f} руб.")
print("=" * 40)
print("    Спасибо за покупку!")