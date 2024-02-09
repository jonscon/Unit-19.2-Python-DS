def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(") 
        False
    """

    # Check for edge cases: if beg is ')' or if odd amount of parentheses
    if len(parens) % 2 == 1 or parens[0] == ')':
        return False

    # Check if beg and end parentheses are not equal to each other; iterate inward
    for i in range(len(parens) // 2):
        if parens[i] == parens[-1 - i]:
            return False
    return True