#골드바흐의 추측
#소수로 빼봤는데 그수가 소수면 되는거 아님?
#아 근데 제일 가까운걸로 하란다...

def is_prime(nb):
    i = 3
    if nb <= 1:
        return False
    if nb == 2:
        return True
    if nb%2 == 0:
        return False
    while i*i <= nb:
        if nb%i == 0:
            return False
        i += 2
    return True

case_num = int(input())

for _ in range(case_num):
    i = 3
    case = int(input())
    i = case // 2
    while True:
        if is_prime(i) and is_prime(case - i):
                print(f"{i} {case-i}")
                break
        i -= 1


#사고흐름... 1. 그냥 3부터 빼기 