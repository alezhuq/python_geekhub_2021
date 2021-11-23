# 6. Маємо рядок --> "f98neroi4nr0c3n30irn03ien3c0rfekdno400wenwkowe00koijn35pijnp46ij7k5j78p3kj546p465jnpoj35po6j345" -> просто потицяв по клавi
#    Створіть ф-цiю, яка буде отримувати рядки на зразок цього, яка оброблює наступні випадки:
# -  якщо довжина рядка в діапазонi 30-50 -> прiнтує довжину, кiлькiсть букв та цифр
# -  якщо довжина менше 30 -> прiнтує суму всiх чисел та окремо рядок без цифр (лише з буквами)
# -  якщо довжина бульше 50 - > ваша фантазiя


def my_func(my_string):

    st_length = len(my_string)
    if 30 <= st_length <= 50:
        letters = sum(i.isalpha() for i in my_string)
        numbers = sum(i.isdigit()for i in my_string)
        print("len = {}, count of letters = {} count of numbers = {}".format(st_length, letters, numbers))
    elif  st_length <= 30:
        sum_of_numbers = sum(int(i) for i in my_string if i.isdigit())
        only_letters = "".join([i for i in my_string if i.isalpha()])
        print("{} - sum of numbers, {} - only letters".format(sum_of_numbers, only_letters))
    else:
        vowels = ["a", "e", "i", "o", "u"]
        str_vowels = sum(i.isdigit() for i in my_string if i in vowels)
        str_consonants = sum(i.isdigit() for i in my_string if i not in vowels)
        print("{} vowels, {} consonants".format(str_vowels, str_consonants))


my_str = str(input("smash that keyboard!"))

my_func(my_str)
