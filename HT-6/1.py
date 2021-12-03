# 1. Програма-світлофор.
#    Створити програму-емулятор світлофора для авто і пішоходів.
#    Після запуска програми на екран виводиться в лівій половині
#    - колір автомобільного, а в правій - пішохідного світлофора.
#    Кожну секунду виводиться поточні кольори. Через декілька ітерацій - відбувається зміна кольорів
#    - логіка така сама як і в звичайних світлофорах.
from time import sleep



def traffic_lights():
    list_of_lights = ["red", "yellow", "green"]
    while True:
        for i in range(12):

            if i < 4:
                print(list_of_lights[0], list_of_lights[2], sep="\t")

            elif i < 6:
                print(list_of_lights[1], list_of_lights[2], sep="\t")

            elif i < 10:
                print(list_of_lights[2], list_of_lights[0], sep="\t")

            else:
                print(list_of_lights[1], list_of_lights[0], sep="\t")

            sleep(1)


traffic_lights()
