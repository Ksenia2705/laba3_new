# TODO Напишите функцию find_common_participants

def find_common_participants(str1, str2, razdelitl=","):
    new_str1 = str1.split(razdelitl)
    new_str2 = str2.split(razdelitl)

    set1 = set(new_str1)
    set2 = set(new_str2)

    intersection_set = set1.intersection(set2)

    new_list = list(intersection_set)

    return new_list


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

result = find_common_participants(participants_first_group, participants_second_group, '|')
print(result)
# TODO Проверьте работу функции с разделителем отличным от запятой
