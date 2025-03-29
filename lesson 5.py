try:
    numerator = int(input("Введіть чисельник: "))
    denominator = int(input("введіть знаменик: "))
    print(numerator / denominator)
except ZeroDivisionError:
    print("Помилка: Ділення на 6 не можливо")
except ValueError:
    print("Помилка: Введені данні не є числом")

















