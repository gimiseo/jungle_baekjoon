#사각형 변으로 가는 최단거리
x,y,w,h = map(int, input().split())

#그냥 w-x 하고 h-y  x , y 중 누가더작은지 확인하고 그거 프린트하면 될듯


list = [h-y, x, y]

min = w-x
for i in list:
    if min > i:
        min = i
print(min)