# 7. Створити пустий клас, який називається Thing. Потім створіть об'єкт example цього класу.
# Виведіть типи зазначених об'єктів.


class Thing(object):
    pass


def main():
    example = Thing()
    print(f"{type(Thing) = }\n{type(example) = }")


if __name__ == "__main__":
    main()
