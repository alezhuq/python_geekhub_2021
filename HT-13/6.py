# 6. Створіть клас в якому буде атребут який буде рахувати кількість створених екземплярів класів.

class ClassWithCounter(object):
    __count = 0

    def __new__(cls, *args, **kwargs):
        cls.count_plus()
        return object.__new__(cls, *args, **kwargs)

    def __del__(self):
        ClassWithCounter.count_minus()

    @staticmethod
    def count_plus():
        ClassWithCounter.__count += 1

    @staticmethod
    def count_minus():
        if ClassWithCounter.__count > 0:
            ClassWithCounter.__count -= 1
        else:
            print("impossible action!")
            exit(1)

    @staticmethod
    def get_count():
        return ClassWithCounter.__count


def main():
    first_instance = ClassWithCounter()
    # print(first_instance.__count) # err
    print(ClassWithCounter.get_count())
    second_instance = ClassWithCounter()
    print(ClassWithCounter.get_count())
    del second_instance
    # print(second_instance) # err
    print(ClassWithCounter.get_count())


if __name__ == "__main__":
    main()
