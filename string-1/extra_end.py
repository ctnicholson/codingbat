def extra_end(str):
    """
    This function returns a new string, given a string, that is made of 3 copies of te last 2 characters of the original string.
    String length is at least two 
    """
    return str[-2:] * 3

print(extra_end('Hello'))
print(extra_end('ab'))
print(extra_end('Hi'))