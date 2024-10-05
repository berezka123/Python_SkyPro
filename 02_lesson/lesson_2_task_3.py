def square(a):
    return a * a


a = input("Введите значение стороны квадрата:")
a = float(a)
a = int(a) + 1
print("Площадь квадрата со стороной", a, "равна", square(a))
