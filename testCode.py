def pageCount(n, p):
    # Write your code here

    res_ftl, res_ltf = int(), int()

    pcounter, pl, pr = 0, 0, 1
    c = False

    while not c and pl < n:
        if pl == p or pr == p:
            res_ftl = pcounter
            c = True
        else:
            pcounter += 1
            pl += 2
            pr += 2

    pcounter1 = 0

    if n % 2 == 0:
        pl1, pr1 = n, n + 1
    else:
        pl1, pr1 = n - 1, n

    c1 = False
    while not c1 and pl > 0:

        if pl1 == p or pr1 == p:
            res_ltf = pcounter1
            c1 = True
        else:
            pl1 -= 2
            pr1 -= 2
        pcounter1 += 1

    # print(res_ftl, res_ltf)
    if res_ftl > res_ltf:
        return res_ltf
    else:
        return res_ftl


if __name__ == '__main__':
    n = 6
    p = 5

    # n = 5
    # p = 4

    result = pageCount(n, p)

    print(result)
