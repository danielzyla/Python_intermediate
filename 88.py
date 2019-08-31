class Cake:

    known_types = ['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel', 'cookies', 'honey-cake','other']
    bakery_offer=[]

    def __init__(self, name, kind, taste, addictions, fillings):
        self.name = name 
        if kind in Cake.known_types:
            self.kind = kind
        else:
            self.kind = 'other'
        self.taste = taste
        self.addictions = addictions
        self.fillings = fillings
        Cake.bakery_offer.append(self)
    
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

confprod3.set_filling('apple jam')
confprod1.add_additives((['whipped cream', 'blueberries']))
confprod4 = Cake('Cocoa waffle','waffle','cocoa',[],'cocoa')

for c in Cake.bakery_offer:
    c.show_info()

print(isinstance(confprod1, Cake))
print(type(confprod1) is Cake)
print(confprod1.__class__)

print('Conf attribs', vars(confprod1))
print('Cake attribs', vars(Cake))
print('Conf attribs', dir(confprod1))
print('Cake attribs',dir(Cake))