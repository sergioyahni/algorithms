# Given the names and grades for each student in a class of N students,
# store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

if __name__ == '__main__':
    # l = []
    # for _ in range(int(input())):
    #     name = input()
    #     score = float(input())
    #     l.append([name, score])
    l = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
    scores = [item[1] for item in l]
    lowest_score = list(set(scores))
    lowest_score.sort()
    lowest_score.pop(0)
    second_lowest = min(lowest_score)

    people = [p[0] for p in l if p[1] == second_lowest]
    print("\n".join(people))











