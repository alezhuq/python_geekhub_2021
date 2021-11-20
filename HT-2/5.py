# 5. Написати скрипт, який залишить в словнику тільки пари із унікальними значеннями (дублікати значень - видалити).
#    Словник для роботи захардкодити свій.

my_hardcoded_dict = {'q': 0, 'w': 1, 'e': 2, "z": 1, "y": 1, 'x': 2, "c": 0}

list_of_values = []
temp_dict = dict()

for key, value in my_hardcoded_dict.items():
    
    if value not in list_of_values:
        list_of_values.append(value)
        temp_dict[key] = value

my_hardcoded_dict = temp_dict

print(my_hardcoded_dict)
