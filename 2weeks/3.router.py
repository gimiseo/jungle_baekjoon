n,m = map(int, input().split())
house_list = []
for _ in range(n):
    house_list.append(int(input()))

def router_install(arr, low, high):

    max_d_of_min = 0
    while low <= high:
        mid = (low + high) // 2


        last = arr[0]
        count = 1
        
        for x in arr[1:]:
            if x - last >= mid:
                count += 1
                last = x
            if count == m:
                break
        if count == m:
            max_d_of_min = mid
            low = mid + 1
        else:
            high = mid - 1
    return max_d_of_min
     


house_list.sort()

low = 1
high = house_list[-1] - house_list[0]

result = 0
result = router_install(house_list, low, high)

print(result)