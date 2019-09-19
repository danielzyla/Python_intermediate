import itertools as it

""" def get_factors(x):
    
    ret_list = []
    for i in range(1, x):
        if x % i == 0:
            ret_list.append(i)
    return ret_list

print(get_factors(20))

candidate_list = [i for i in range(1,10001)]

# filtered_list =[]

# for num in candidate_list:
#     if num == sum(get_factors(num)):
#         filtered_list.append(num)

filtered_list = it.filterfalse(lambda x: x!=sum(get_factors(x)), candidate_list)

for num in filtered_list:
    print("Perfect number is {}\t and it has dividers {} ".format(num, get_factors(num)))
 """



def check_if_has_dividers(x):
    
    for i in range(2, x):
        if x % i == 0:
            return True
    else:
        return False

# not optimal:
#prime_numbers = list(it.filterfalse(lambda x: check_if_has_dividers(x), range(1, 10000)))
#print(prime_numbers)

#print(prime_numbers[:10])

prime_numbers = it.islice(it.filterfalse(lambda x: check_if_has_dividers(x), range(10000000)), 10)
print(list(prime_numbers))