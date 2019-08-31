banknotes_coins = [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5, 10, 20, 50, 100, 200, 500]

dict_denominations = {}

for i in banknotes_coins:
    dict_denominations[i]=0

print(dict_denominations)

print('-'*50)

dict_denominations[100] += 1
dict_denominations[20] += 1
dict_denominations[5] += 1
dict_denominations[0.5] += 1
 
dict_denominations[50] += 1
dict_denominations[20] += 2
dict_denominations[5] += 1
dict_denominations[2] += 2
 
dict_denominations[100] += 1
dict_denominations[50] += 1
dict_denominations[2] += 1

print(dict_denominations)

print('-'*50)

for key in sorted(dict_denominations):
    print('Denominate: %6.2f - amount %5d'%(key, dict_denominations[key]))

print('-'*50)

for key in sorted(dict_denominations):
    print('Denominate: {:6.2f} - amount {:5d}'.format(key, dict_denominations[key]))
