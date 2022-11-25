def merge_sort(list):
    """
    Sorts a list in ascending order

    Divide: Find the midpoint of the list and divide
    Conquer: Recursively sort the sublists created
    Combine: Merg the sorted sublists
    """
    if len(list) <= 1:
        return list

    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)


def split(list):
    """
    Divide the unsorted list at midpoint
    Returns two sublists - left and right
    """
    mid = len(list) // 2
    left = list[:mid]
    right = list[mid:]

    return left, right
