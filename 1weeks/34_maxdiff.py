#차이가 큰걸 만날때까지 -> 
#정렬이 필요할까? 

def absolute(n):
    if n < 0:
        value = -n
    else:
        value = n
    return value

def calculate(array):
    sum = 0
    for i in range(len(array) - 1):
        sum += absolute(array[i] - array[i + 1])
    return sum

def diff_sum(num):
    temp_list = []
    use = [False]*num
    def dfs(count):
        if count == num:
            result_list.append(calculate(temp_list))
            return
        for i in range(num):
            if use[i] == False:
                use[i] = True
                temp_list.append(num_list[i])
                dfs(count+1)
                temp_list.pop()
                use[i] = False
    dfs(0)

n = int(input())
num_list = list(map(int, input().split()))
result_list = []
diff_sum(n)
print(max(result_list))

