#일단, n 자리수에서 k 자리수를 빼는게 중요함
# 그리고 순서가 유지가됨
# 빼는데, 이게 최선의 선택인지는 모르는거지
# 스택문제라고 했으니 스택적 사고로 들어가야함
# 자리수에서 최선일걸 생각할수있어야함
# 뒷자리와 앞자리를 생각했을때 최선인게 뭐냐?
# 우선순위가 있을까?
# 자리수 스택을 만든다.
# 그러고 리스트 순회를 돈다.
# 1먼저 올리고 9가 더 크다? 그럼 9를 올린다.
# 하지만 중요한건 올리는데에 자리수 스택에는 자리가 한정되잇다는 것
# 그 한정된 자리를 카운트하는게 1순위
# len(stack)과 len(num_str) 상시체크, 
# 그러면 들어온 숫자를 채우는 리스트를 만들어보자

n, k = map(int, input().split())
num = input()

stack = []
for i in range(n):
    cur_num = int(num[i])
    while stack and stack[-1] < cur_num and  (n - k) - len(stack) < n - i:
        stack.pop()
    stack.append(cur_num)
if len(stack) > n - k:
    stack = stack[:n-k]
print("".join(map(str,stack))) 

#여기서문제, 자리수 관리를 해야함
#자리수 관리를 해야하니까 해당 남은 자리수 = (n - k) - len(stack) 남은 숫자수 n - (i+1)