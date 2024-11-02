# TODO Напишите функцию для поиска индекса товара

def poisk(list_, product):
    flag = 0
    for i in range(len(list_)):
        if list_[i] == product:
            flag = 1
            ind = i
            break
    if flag == 0:
        return None
    else:
        return ind

items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = poisk(items_list, find_item)  # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")


