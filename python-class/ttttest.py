
example_list_1 = [0, 0, 1, 0]
def are_all_items_same(items):
    for x in range(0, len(example_list_1)):
        if example_list_1[x] != items[0]:
            return(False)
    return(True)
print(are_all_items_same(example_list_1))