def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """

    # Create a counter
    counter = {}
    for num in nums:
        counter[num] = counter.get(num, 0) + 1
    
    # Get the largest number of occurences
    max_freq = max(counter.values())

    # Find the number with that largest number of occurences
    for (num, freq) in counter.items():
        if freq == max_freq:
            return num