from linked_list import SinglyLinkedList
from typing import List


def merge_sort(list: List[int]) -> List[int]:
    """
    Sorts a list in ascending order

    Divide: Find the midpoint of the list and divide
    Conquer: Recursively sort the sublists created
    Combine: Merg the sorted sublists

    Takes O(kn log n) time
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

    Takes overall O(k log n) time
    """
    mid = len(list) // 2
    left = list[:mid]
    right = list[mid:]

    return left, right


def merge(left, right):
    """
    Merges two lists, sorting them in the process
    Returns a new merged list

    Runs in overall O(n) time
    """
    l: List[int] = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1

    while i < len(left):
        l.append(left[i])
        i += 1

    while j < len(right):
        l.append(right[j])
        j += 1

    return l


def verify_sorted(list: List[int]) -> bool:
    n = len(list)

    if n == 0 or n == 1:
        return True

    return list[0] < list[1] and verify_sorted(list[1:])


alist = [54, 243, 57, 12, 68, 768, 3]
l = merge_sort(alist)

print(verify_sorted(alist))
print(verify_sorted(l))
