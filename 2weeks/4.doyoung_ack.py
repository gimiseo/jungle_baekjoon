n= int(input())
solution = list(map(int, input().split()))

solution.sort()

left = 0
right = len(solution) - 1

ans = [solution[left],solution[right]]

abs_min = abs(solution[left] + solution[right])
while left < right:
    cur_sum = solution[left] + solution[right]
    if cur_sum == 0:
        ans[0], ans[1] = solution[left], solution[right]
        break
    if abs_min > abs(cur_sum):
        abs_min = abs(cur_sum)
        ans[0], ans[1] = solution[left], solution[right]
    if cur_sum < 0:
        left += 1
    else:
        right -= 1

print(ans[0], ans[1])