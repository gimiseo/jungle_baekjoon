import heapq

#최소 힙으로만 기능함
#리스트를 힙으로 만드는법
data = [5, 3, 8, 1]
heapq.heapify(data)  
print(data)


heapq.heappush(data, 2)
print(data)

min_val = heapq.heappop(data)
print(min_val)  # 1
print(data)     # [2, 3, 8, 5]

print(data[0])


#최대 힙 만드는법
max_heap = []
heapq.heappush(max_heap, -5)
heapq.heappush(max_heap, -1)
heapq.heappush(max_heap, -9)

print(-heapq.heappop(max_heap))