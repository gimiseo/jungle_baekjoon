#달팽이는 하루 낮에는 A만큼 올라가고... 밤에는 B만큼 내려간다..
#10억번은 그냥 오래걸린다.
#days = ceil((goal - up) / (up - down)) + 1 수학적으로 접근해야한다....
#goal - up 마지막 전날까지 필요한 거리 
#up - down 딱 하루 올라가는 거리
#ceil -> 수학적 반올림 함수

import math
up, down, goal = map(int, input().split())
days = math.ceil((goal - up) / (up - down)) + 1
print(days)
