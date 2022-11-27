# In this challenge, the user enters a string and a substring.
# You have to print the number of times that the substring occurs in the given string.
# String traversal will take place from left to right, not from right to left.

def count_substring(string, sub_string):
    counter = 0
    if sub_string in string:
        i = string.index(sub_string)
        while i <= (len(string) - len(sub_string)):
            counter += 1 if string[i:i + len(sub_string)] == sub_string else 0
            i += 1
    return counter


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)