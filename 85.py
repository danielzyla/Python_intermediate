class Cake:
    def __init__(self, name, kind, taste, addictions, fillings):
        self.name = name 
        self.kind = kind
        self.taste = taste
        self.addictions = addictions
        self.fillings = fillings
    
    def show_info(self):
        print(self.name.upper())
        print('Kind:\t\t', self.kind)
        print('Taste:\t\t', self.taste)
        print('Additives:')
        for a in self.addictions:
            print('\t\t',a) 
        print('Filling:\t', self.fillings)
        print('-'*20)
    def set_filling(self, filling):
        self.fillings = filling
    def add_additives(self, adds):
        self.addictions.extend(adds)



confprod1 = Cake('Chocolate cake', 'cake', 'chocolate', ['caramel glaze'], 'strawberries jam')
confprod2 = Cake('Butter cakes', 'cookies', 'creamy', ['sugar icing', 'nuts'], 'raspberry')
confprod3 = Cake('Gingerbread', 'honey-cake', 'spicy', ['sugar sprinkles'], '')

bakery_offer = [confprod1, confprod2, confprod3]

confprod3.set_filling('apple jam')
confprod1.add_additives((['whipped cream', 'blueberries']))

for c in bakery_offer:
    c.show_info()