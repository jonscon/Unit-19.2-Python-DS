def read_file_list(filename):
    """Read file and print out each line separately with a "-" before it.

    For example, if we have a file, `dogs`, containing:
        Fido
        Whiskey
        Dr. Sniffle

    This should work:

        >>> read_file_list("dogs")
        - Fido
        - Whiskey
        - Dr. Sniffle

        >>> read_file_list("cats")
        - Auden
        - Ezra
        - Fluffy
        - Meowsley

    It will raise an error if the file cannot be found.
    """

    # hint: when you read lines of files, there will be a "newline"
    # (end-of-line character) at the end of each line, and you want to
    # strip that off before you print it. Do some research on that!

    # Open file and read all lines into lines list
    with open(filename) as file1:
        lines = file1.readlines()
    
    # Iterate through lines and print out each line, getting rid of all trailing whitespaces (tabs, spaces, newlines)
    for line in lines:
        chars = list(line)
        chars.insert(0, '- ')
        print(''.join(chars).strip())