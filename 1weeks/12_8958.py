num = int(input())

str_list = []
for _ in range(num):
    str_list.append(input())
for a in str_list:
    score = 0
    combo = 0
    for i in range(len(a)):
        if a[i] == "O":
            combo += 1
            score += combo
        else:
            combo = 0
    print(score)