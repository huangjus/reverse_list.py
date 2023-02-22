# Author: Justin Huang
# GitHub username: huangjus
# Date: 2/21/23
# Description: This function takes a list as input and reverses the order of the elements in that list.

def reverse_list(values):

    """
    Reverses the order of the elements in the input list.

    values: A list of elements.
    """

    left = 0
    right = len(values) - 1

    while left < right:
        values[left], values[right] = values[right], values[left]
        left += 1
        right -= 1
