#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    uniq_set1 = set()
    uniq_set2 = set()
    for element in set_1:
        if element not in set_2:
            uniq_set1.add(element)

    for element in set_2:
        if element not in set_1:
            uniq_set2.add(element)

    result_set = uniq_set1.union(uniq_set2)
    return result_set
