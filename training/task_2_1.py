# employee_list = ["Jonh Snow", "Piter Pen", "Drakula", "IvanIV", "Moana", "Juilet"]
# print(employee_list[1] + ", " + employee_list[-2])

# def dev_by_three(num):
#    if num % 3 == 0:
#        return 'Да'
#    else:
#        return 'Нет'


#n = 10
#number = dev_by_three(n)
#print("Делится ли на три", n, "? -", number)

import math

def min_boxes(item):
    boxes = item / 5
    return math.ceil(boxes)


items = input("Сколько у вас предметов? ")
items = int(items)
print("Для", items, "предметов необходимо", min_boxes(items), "коробок.")