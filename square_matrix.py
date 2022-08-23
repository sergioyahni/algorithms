def staircase(n):
    # Write your code here
    for m in range(n):
        print('n:', n, ' m:', m + 1)
        print(' ' * (n-(m + 1)), "#" * (m+1))
if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
