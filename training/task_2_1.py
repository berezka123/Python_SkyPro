# 1) Работа со списками.
# employee_list = ["Jonh Snow", "Piter Pen", "Drakula", "IvanIV", "Moana", "Juilet"]
# print(employee_list[1] + ", " + employee_list[-2])


# 2) Деление на три.
# def dev_by_three(num):
#    if num % 3 == 0:
#        return 'Да'
#    else:
#        return 'Нет'
#
#
#n = 10
#number = dev_by_three(n)
#print("Делится ли на три", n, "? -", number)


# 3) Округление.
#import math
#
#
#def min_boxes(item):
#    boxes = item / 5
#    return math.ceil(boxes)
#
#
#items = input("Сколько у вас предметов? ")
#items = int(items)
#print("Для", items, "предметов необходимо", min_boxes(items), "коробок.")

# 4) Два делителя.
#def check_divisibility(num):
#    for i in range(1, num + 1):
#        if (i % 2 == 0) and (i % 4 != 0):
#            print("Делится на 2, но не на 4")
#        elif (i % 2 == 0) and (i % 4 == 0):
#            print("Делится и на 2, и на 4")
#        else:
#            print(i)
#
#
#number = int(input("Введите число:"))
#
#check_divisibility(number)


# 5) Квартал.
#def quarter_of_year(month_number):
#    if month_number in range(1, 4):
#        print("I квартал")
#    elif month_number in range(4, 7):
#        print("II квартал")
#    elif month_number in range(7, 10):
#        print("III квартал")
#    elif month_number in range(10, 13):
#        print("IV квартал")
#
#number_of_month = int(input("Введите номер месяца (от 1 до 12): "))
#
#if number_of_month in range(1, 13):
#    quarter_of_year(number_of_month)
#else:
#    print("Ну сказано же: номер месяца от 1 до 12!")


# 6) Фильтрация списка.
#lst = [17, 34, 9, 21, 13, 48, 24, 7, 81, 29, 16, 12, 42]
#
#for i in lst:
#    if (i > 15) and (i % 3 == 0):
#        print(i)


# 7) Range.
#l = list(range(25, 0, -5))
#print(l)


# 8) Поменять значения местами.
var_1 = 50
var_2 = 5

var_lst = [var_1, var_2]

var_1 = var_lst[-1]
var_2 = var_lst[0]

print(f"var_1 = {var_1}, var_2 = {var_2}")
