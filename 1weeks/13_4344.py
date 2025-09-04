#round(num,display_youWant)

num = int(input())
for _ in range(num):
    score_list = list(map(int, input().split()))
    studentNum = score_list.pop(0)
    average = sum(score_list) / studentNum
    over_num = 0
    for i in score_list:
        if i > average:
            over_num += 1
    print(f"{over_num/studentNum*100:.3f}%")
