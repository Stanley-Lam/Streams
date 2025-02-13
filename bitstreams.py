# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from queue import *

def find_density(stream, width):
    """
    Compute the average number of 1's in a window.
    TODO: Implement this function. It must have O(n) complexity.

    :param stream: A non-empty generator of 0's and 1's
    :param width: A maximum size of a window
    :return: The average number of 1's in a window of that width
    :raise ZeroDivisionError: If the width exceeds the length of the stream
    """
    one_counter = 0
    total_one = 0
    window_counter = 0
    new_queue = Queue()


    for i in stream:
        enqueue(new_queue, i)
        if i == 1:
            one_counter += 1
        if size(new_queue) < width:
            continue
        total_one += one_counter
        removed_element = dequeue(new_queue)
        if removed_element == 1:
            one_counter -= 1
        window_counter += 1

    if window_counter == 0:
        raise (ZeroDivisionError)

    avg_one = total_one / window_counter
    return avg_one


def find_pattern(stream, width, pattern):
    """
    Find all windows that are equal to a pattern.
    TODO: Implement this function. It must have O(n) complexity.

    :param stream: A non-empty generator of 0's and 1's
    :param width: A maximum size of a window
    :param pattern: An array of 0's and 1's, of that width, for which to search
    :return: A new Queue of indices at which the stream contains the pattern
    """

    sum_counter = 0
    new_queue = Queue()
    pattern_queue = Queue()
    index_counter = - 1
    key = 0

    for j in pattern:
        key = key * 2
        key += j

    for i in stream:
        enqueue(new_queue, i)
        index_counter += 1
        sum_counter = sum_counter * 2
        if i == 1:
            sum_counter += 1
        if size(new_queue) < width:
            continue
        if sum_counter == key:
            enqueue(pattern_queue, index_counter - width + 1)
        removed_element = dequeue(new_queue)
        if removed_element == 1:
            sum_counter -= 2 ** (width - 1)

    return pattern_queue

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
