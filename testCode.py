def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here

    apples_counter = [1 if s <= a + apple <= t else 0 for apple in apples]
    print(sum(apples_counter))

    oranges_counter = [1 if t >= (b + orange) >= s else 0 for orange in oranges]
    print(sum(oranges_counter))


if __name__ == '__main__':
    s = 2
    t = 3
    a = 1
    b = 5

    apples = [2]
    oranges = [-2]

    countApplesAndOranges(s, t, a, b, apples, oranges)
