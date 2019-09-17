import random
#import time

def taste_gen():
    while True:
        sweet = random.randint(1,100)
        sour = random.randint(1,100)
        salty = random.randint(1,100)
        if (sweet + sour + salty) == 100:
            yield [sweet, sour, salty]
            break
    

for mix in range(10):
    print(next(taste_gen()))

    
    
""" def random_with_sum(number_of_values, asserted_sum):
    
    trial = 0
    numbers = list(range(number_of_values))
    while True:
    
        trial +=1
        for i in range(number_of_values):
            numbers[i] = random.randint(1, 101)
    
        if sum(numbers) == asserted_sum:
            yield((trial, numbers))
            trial = 0
    
    
for i in range(10):
    (number_of_trials, numbers) = next(random_with_sum(3, 100))
    print(number_of_trials, numbers) """

#time.sleep(10)