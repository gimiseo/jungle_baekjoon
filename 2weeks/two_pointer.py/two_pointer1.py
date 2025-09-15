n_list = [1, 2, 4, 4, 5, 6]

l_pointer = 0
r_pointer = len(n_list) - 1
target = 8

while l_pointer < r_pointer:
    sum = (n_list[l_pointer] + n_list[r_pointer])
    if target == sum:
        print(n_list[l_pointer], n_list[r_pointer])
        l_pointer += 1
    elif sum < target:
        l_pointer += 1
    else:
        r_pointer -= 1
