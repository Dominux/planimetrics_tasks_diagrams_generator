from typing import Any


def swap_2_elements_in_list(input_list: list, element: Any, index_to_put: int):
    try:
        a_i = input_list.index(element)
    except ValueError:
        a_i = None
    b = input_list[index_to_put]

    # swapping
    input_list[index_to_put] = element
    if a_i:
        input_list[a_i] = b
    else:
        input_list.append(b)
