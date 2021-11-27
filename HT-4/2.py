# 2. Написати функцію < bank > , яка працює за наступною логікою:
# користувач робить вклад у розмірі < a > одиниць строком на < years > років під < percents > відсотків
# (кожен рік сума вкладу збільшується на цей відсоток,
# ці гроші додаються до суми вкладу і в наступному році на них також нараховуються відсотки).
# Параметр < percents > є необов'язковим і має значення по замовчуванню < 10 > (10%).
# Функція повинна принтануть і вернуть суму, яка буде на рахунку.


def bank(a, years, percents=10):
    for i in range(years):
        a += a * percents / 100
    print("sum after {} year(s) = {}".format(years, a))
    return a


[*arguments] = input("input in the next order :amount_of_money, years, percentage (e.g. (100, 1, 33.3))").split(sep=", ")

[*arguments] = map(int, [*arguments])

your_new_value = bank(*arguments)
