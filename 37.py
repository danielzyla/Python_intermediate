import math

argument_list=[]

##a=0
##while a <10:
##    argument_list.append(round(a,1))
##    a+=0.1
##
##print(argument_list)
##
##
##formula=input('Enter your function pattern: ')
##
##for x in argument_list:
##    print('If x = {} then results is {}'.format(x, eval(formula)))

for i in range (100):
    argument_list.append(i/10)
    i += 1
    
formula = input("Please enter a formula, use 'x' as the argument: ")
 
for x in argument_list:
    print("{0:3.1f} {1:6.2f}".format(x, eval(formula)))
