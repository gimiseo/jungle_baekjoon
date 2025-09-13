n,m = map(int, input().split())
trees = list(map(int, input().split()))


def binary_wood_search(arr, start, end):
    global result
    if start > end:
        return
    mid = (start + end) // 2

    total = 0
    for x in arr:
        if mid < x:
            total += x - mid
    if total < m:
        binary_wood_search(arr, start, mid - 1)
    else:
        result = mid
        binary_wood_search(arr, mid + 1, end)

start = 0
end = max(trees)

result = 0

binary_wood_search(trees, start, end)
print(result)