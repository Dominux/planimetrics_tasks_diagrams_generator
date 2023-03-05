from typing import Any


def swap_2_elements_in_list(input_list: list, element: Any, index_to_put: int):
    a_i = input_list.index(element)
    b = input_list[index_to_put]

    # swapping
    input_list[index_to_put] = element
    input_list[a_i] = b
