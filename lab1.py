
def max_list_iter(int_list):  # must use iteration not recursion
    """finds the max of a list of numbers and returns the value (not the index)
    If int_list is empty, returns None. If list is None, raises ValueError"""
    if int_list is None:
        raise ValueError
    else:
        if len(int_list) == 0:
            return None
        max_val = 0
        for i in int_list:
            if i > max_val:
                max_val = i
        return max_val


def reverse_rec(int_list):   # must use recursion
    """recursively reverses a list of numbers and returns the reversed list
    If list is None, raises ValueError"""
    if int_list is None:
        raise ValueError
    else:
        length = len(int_list)
        if length <= 1:
            return int_list
        # last item + reversal of list up to last item
        return int_list[length - 1:] + reverse_rec(int_list[:length - 1])


def bin_search(target, low, high, int_list):  # must use recursion
    """searches for target in int_list[low..high] and returns index if found
    If target is not found returns None. If list is None, raises ValueError """
    if int_list is None:
        raise ValueError
    else:
        if high >= low:
            mid = low + (high - low) // 2
            if int_list[mid] == target:
                return mid
            elif int_list[mid] < target:
                return bin_search(target, mid + 1, high, int_list)
            else:
                return bin_search(target, low, mid - 1, int_list)
        else:
            return None
