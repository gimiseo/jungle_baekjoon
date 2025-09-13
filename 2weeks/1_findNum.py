num = int(input())
origin = list(map(int, input().split()))
num = int(input())
find = list(map(int, input().split()))

def binary_search(arr, target, start, end):
    if start > end:
        return 0
    mid = (start + end) // 2
    if arr[mid] == target:
        return 1
    elif target < arr[mid]:
        return binary_search(arr, target, start, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, end)

origin.sort()
for f in find:
    result = binary_search(origin, f, 0, len(origin) - 1)
    print(result)
