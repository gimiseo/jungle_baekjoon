#gpt선생님의 말씀... 하이브리도는 그렇게 하는게...아니야..!
import sys
n = int(sys.stdin.readline())
array = []
for _ in range(n):
    array.append(int(sys.stdin.readline()))

# def insert(array, start, end):
#   for i in range(start + 1, end + 1):
#     for j in range(i, 0, -1):
#       if array[j] < array[j - 1]:
#         array[j], array[j - 1] = array[j - 1], array[j]
#       else:
#         break

def quick_sort(array, start, end):
    if (end - start + 1) <= 16:
       for i in range(start + 1, end + 1):
        for j in range(i, 0, -1):
          if array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
          else:
            break
       return
    if start > end:
        return
    pivot = start
    left = start + 1
    right = end

    while left <= right: #역전된때까지 넘어설때까지 계속 돌린다..
        while left <= end and array[left] <= array[pivot]:
            left += 1
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left],array[right] = array[right],array[left]
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)

quick_sort(array, 0, len(array) - 1)

for a in array:
    print(a)
  