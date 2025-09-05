# int	ft_recursive_factorial(int nb)
# {
# 	if (nb < 0)
# 		return (0);
# 	if (nb == 0 || nb == 1)
# 		return (1);
# 	return (nb * ft_recursive_factorial(nb - 1));
# } 42샤라웃...

def factorial(num):
    #재귀 종료 조건
    if (num == 0 or num == 1):
        return 1
    return num * factorial(num - 1)

print(factorial(int(input())))