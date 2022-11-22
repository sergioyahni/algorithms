# Given the participants' score sheet for your University Sports Day,
# you are required to find the runner-up score. You are given n scores.
# Store them in a list and find the score of the runner-up.

if __name__ == '__main__':
    arr = [57, 57, 57, -57, 57]
    x = list(set(arr))
    x.sort()
    x.pop(-1)
    print(max(x))