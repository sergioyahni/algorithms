# You are given a string S .
# Your task is to find out if the string S
# contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.

if __name__ == '__main__':
    s = input()
    attributes = {'alphanumeric': 0, 'alphabetical': 0, 'digits': 0, 'lowercase': 0, 'uppercase': 0}
    for c in s:
        if c.isalpha() or c.isnumeric():
            attributes['alphanumeric'] += 1
        if c.isalpha():
            attributes['alphabetical'] += 1
        if c.isnumeric():
            attributes['digits'] += 1
        if c.islower():
            attributes['lowercase'] += 1
        if c.isupper():
            attributes['uppercase'] += 1
    for k in attributes:
        if attributes[k] > 0:
            print(True)
        else:
            print(False)

    print(any(s.isalpha() for s in s))
    """
    alphanumeric
    alphabetical 
    digits
    lowercase
    uppercase 
    """