def month_to_season(month):
    if month == 1 or month == 2 or month == 12:
        return "Зима"
    elif month in range(3, 6):
        return "Весна"
    elif month in range(6, 9):
        return "Лето"
    elif month in range(9, 12):
        return "Осень"
    else:
        return "Месяца с таким номером не существует"


m = input("Введите номер месяца:")
m = int(m)
print(month_to_season(m))
