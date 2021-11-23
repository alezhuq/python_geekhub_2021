# 6. Маємо рядок -->
#   "f98neroi4nr0c3n30irn03ien3c0rfekdno400wenwkowe00koijn35pijnp46ij7k5j78p3kj546p465jnpoj35po6j345" ->
#   просто потицяв по клавi
#    Створіть ф-цiю, яка буде отримувати рядки на зразок цього, яка оброблює наступні випадки:
#    -  якщо довжина рядка в діапазонi 30-50 -> прiнтує довжину, кiлькiсть букв та цифр
#    -  якщо довжина менше 30 -> прiнтує суму всiх чисел та окремо рядок без цифр (лише з буквами)
#    -  якщо довжина бульше 50 - > ваша фантазiя


def func_for_long_strings(long_string):
    str_length = len(long_string)

    if 30 <= str_length <= 50:
        letters = sum(i.isalpha() for i in long_string)
        numbers = sum(i.isdigit() for i in long_string)

        print ("there are {} letters and {} digits ".format(letters, numbers))
        print("the length of the string = {}".format(str_length))

    elif str_length < 30:
        numbers = sum(int(i) for i in long_string if i.isdigit())
        without_numbers = [i for i in long_string if i.isalpha()]
        without_numbers = "".join(without_numbers)

        print("the sum of all digits = {}".format(numbers))
        print("string without numbers : ", without_numbers)

    else:
        smash = int(str_length/2)
        print("you've smashed that keyboard approximately {} times(+-5) ".format(smash))


input_long_string = str(input("smash that keyboard! : "))

func_for_long_strings(input_long_string)
