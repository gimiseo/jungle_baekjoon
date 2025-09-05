# int	ft_is_prime(int nb)
# {
# 	int	i;

# 	i = 3;
# 	if (nb <= 1)
# 		return (0);
# 	if (nb == 2)
# 		return (1);
# 	if (nb % 2 == 0)
# 		return (0);
# 	while (i * i <= nb)
# 	{
# 		if (nb % i == 0)
# 			return (0);
# 		i += 2;
# 	}
# 	return (1);
# }
#바야흐로... 1년전 풀어던 코드 샤라웃...

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

num = int(input())
num_list = list(map(int, input().split()))

count = 0
for a in num_list:
    if is_prime(a):
        count +=1
print(count)