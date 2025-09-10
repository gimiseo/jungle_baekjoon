num = int(input())
grid = [list(map(int, input().split())) for _ in range(num)]

def travel(num):
    aleady_go = [False] * num
    temp_list = []
    def dfs(count, ex_city):
        if count == num - 1:
            if grid[ex_city][first_city] == 0:
                return
            temp_list.append(grid[ex_city][first_city])
            result_list.append(sum(temp_list))
            temp_list.pop()
            return
        for i in range(num):
            if aleady_go[i] == False and grid[ex_city][i] != 0:
                aleady_go[i] = True
                temp_list.append(grid[ex_city][i])
                dfs(count+1, i)
                aleady_go[i] = False
                temp_list.pop()
    for i in range(num):
        first_city = i
        aleady_go[i] = True
        dfs(0, i)
        aleady_go[i] = False
if num == 2:
    print(grid[0][1] + grid[1][0])
    exit()

result_list = []
travel(num)
print(min(result_list))