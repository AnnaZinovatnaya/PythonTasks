def swap(target_list, item_index1,  item_index2):
    target_list[item_index1], target_list[item_index2] = target_list[item_index2], target_list[item_index1]


a = [1, 2, 3, 4, 5, 6]

swap(a, 0, 1)

print(a)
