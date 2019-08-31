class Cake:
    def __init__(self, name, kind, taste, addictions, fillings):
        self.name = name 
        self.kind = kind
        self.taste = taste
        self.addictions = addictions
        self.fillings = fillings

confprod1 = Cake('Chocolate cake', 'cake', 'chocolate', 'caramel glaze', 'strawberries jam')
confprod2 = Cake('Butter cakes', 'cookies', 'creamy', ('sugar icing', 'nuts'), 'raspberry')
confprod3 = Cake('Gingerbread', 'honey-cake', 'spicy', 'sugar sprinkles', '')

bakery_offer = [confprod1, confprod2, confprod3]

print('Today in our offer:')
for conf in bakery_offer:
    print('{} - ({}) main taste: {} with additives of {},filled with {}'.format(conf.name, conf.kind, conf.taste, conf.addictions, conf.fillings))