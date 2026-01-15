from typing import List


def get_group_count(array: List[int]) -> int:
    if not len(array):
        return 0

    max_depth: int = 0

    def get_depth(i: int, acc: int = 0) -> int:
        while True:
            if array[i] == -1:
                return acc
            
            i = array[i]
            acc += 1

    for index, _ in enumerate(array):
        max_depth = max(get_depth(index), max_depth)
    
    return max_depth + 1