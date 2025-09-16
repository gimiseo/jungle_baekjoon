# n = int(input())
# numbers = list(map(int, input().split()))

# #일단 
# max_count = 1
# for i in range(len(numbers) - 1):
#     tail = []
#     increase = numbers[i]
#     for j in range(i + 1, len(numbers)):
#         if numbers[j] > increase:
#             increase = numbers[j]
#             count += 1
#     if max_count < count:
#         max_count = count
# print(max_count)