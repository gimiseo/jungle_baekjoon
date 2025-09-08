def perms(a):
    n = len(a)
    used = [False]*n
    path = []
    out = []  # 여기 모았다가 한 번에 반환

    def dfs():
        if len(path) == n:
            out.append(tuple(path))
            return
        for i in range(n):
            if used[i]:
                continue
            used[i] = True
            path.append(a[i])
            dfs()
            path.pop()
            used[i] = False

    dfs()
    return out

# 사용
for p in perms([1, 2, 3]):
      print(p)

