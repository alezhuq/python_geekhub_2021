# 2. Створити клас Person, в якому буде присутнім метод __init__
# який буде приймати * аргументів, які зберігатиме в відповідні змінні.
# Методи, які повинні бути в класі Person - show_age, print_name, show_all_information.

# Створіть 2 екземпляри класу Person та в кожному з екземплярів створіть атребут profession.


class Person(object):

    def __init__(self, name=None, age=None, *args):
        self.name = name
        self.age = age
        self.rest_info = args

    def show_age(self):
        print(self.age)

    def print_name(self):
        print(self.name)

    def show_all_information(self):
        for key, value in vars(self).items():
            print(f"{key}, {value}")


def main():
    grisha = Person("Grisha", 34, "married")
    grisha.profession = "fireman"
    grisha.show_all_information()

    arkadiy = Person("arkadiy", 26, "engaged")
    arkadiy.profession = "scientist"
    arkadiy.show_all_information()


if __name__ == "__main__":
    main()
