def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """

    # first[0] and last[-1] numbers of first and last rows
    # [1] and [-2] numbers of [1] and [-2] rows
    # [1,2,3,4]
    # [4,5,6,7]
    # [7,8,9,0]
    # [1,2,3,4]

    sum = 0

    for i in range(len(matrix)):
        sum += matrix[i][i]
        sum += matrix[i][-1 - i]
    return sum