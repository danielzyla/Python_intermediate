def Combinations(products, promotions, customers):
    for prod in products:
        for promo in promotions:
            for cust in customers:
                yield "{} - {} -{}".format(prod, promo, cust)

    
products = ["Product {}".format(i) for i in range(1, 4)]
promotions = ["Promotion {}".format(i) for i in range(1, 2)]
customers = ['Customer {}'.format(i) for i in range(1, 5)]
    
combinations = Combinations(products, promotions, customers)
    
for c in combinations:
    print(c)