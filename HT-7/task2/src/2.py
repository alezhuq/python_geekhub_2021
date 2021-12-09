# 2. Написати функцію, яка приймає два параметри: ім'я файлу та кількість символів.
#    На екран повинен вивестись список із трьома блоками - символи з початку, із середини та з кінця файлу.
#    Кількість символів в блоках - та, яка введена в другому параметрі.
#    Придумайте самі, як обробляти помилку, наприклад, коли кількість символів більша, ніж є в файлі
#    (наприклад, файл із двох символів і треба вивести по одному символу,
#    то що виводити на місці середнього блоку символів?)
#    В репозиторій додайте і ті файли, по яким робили тести.
#    Як визначати середину файлу (з якої брать необхідні символи) -
#    кількість символів поділити навпіл, а отримане "вікно" символів відцентрувати щодо середини файла
#    і взяти необхідну кількість. В разі необхідності заокруглення одного чи обох параметрів - дивіться на свій розсуд

from pathlib import Path


def beginning_middle_end_n_symbols(filename: str, number_of_symbols: int):
    with open(Path(__file__).parent.parent / "data" / filename) as data_content:
        a = str(data_content.readline())
    if len(a)<3*number_of_symbols:
        print("not enough symbols in the file")
    else:
        print(a[:number_of_symbols])
        left_n = (len(a)-number_of_symbols)//2
        right_n = (len(a)+number_of_symbols)//2

        print(a[left_n:right_n])
        print(a[-number_of_symbols:])


beginning_middle_end_n_symbols("file1.txt", 3)
