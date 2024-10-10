from smartphone import Smartphone

catalog = [Smartphone("Nokia", "3110", "+79210123456"),
           Smartphone("iPhone", "16Pro", "+79111234567"),
           Smartphone("Huawei", "30Pro", "+79052345678"),
           Smartphone("Sansung", "A30", "+79003456789"),
           Smartphone("Motorola", "T91", "+79019876543")]

for i in catalog:
    print(f"{i.trademark} - {i.model}.  {i.phonenumber}")
