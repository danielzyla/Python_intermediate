class Cake:

    known_types = ['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel', 'cookies', 'honey-cake','other']
    bakery_offer=[]

    def __init__(self, name, kind, taste, addictions, fillings, gluten_free):
        self.name = name 
        if kind in Cake.known_types:
            self.kind = kind
        else:
            self.kind = 'other'
        self.taste = taste
        self.addictions = addictions
        self.fillings = fillings
        Cake.bakery_offer.append(self)
        self.__gluten_free=gluten_free
    
    def show_info(self):
        print(self.name.upper())
        print('Kind:\t\t', self.kind)
        print('Taste:\t\t', self.taste)
        print('Additives:')
        for a in self.addictions:
            print('\t\t',a) 
        print('Filling:\t', self.fillings)
        print('Gluten-free:\t', self.__gluten_free)
        print('-'*20)
    def set_filling(self, filling):
        self.fillings = filling
    def add_additives(self, adds):
        self.addictions.extend(adds)


confprod1 = Cake('Chocolate cake', 'cake', 'chocolate', ['caramel glaze'], 'strawberries jam', False)
confprod2 = Cake('Butter cakes', 'cookies', 'creamy', ['sugar icing', 'nuts'], 'raspberry', False)
confprod3 = Cake('Gingerbread', 'honey-cake', 'spicy', ['sugar sprinkles'], '', True)

confprod3.set_filling('apple jam')
confprod1.add_additives((['whipped cream', 'blueberries']))
confprod4 = Cake('Cocoa waffle','waffle','cocoa',[],'cocoa', False)

confprod2.__gluten_free = True
confprod2._Cake__gluten_free = True
del confprod2.__gluten_free

for c in Cake.bakery_offer:
    c.show_info()

print(vars(confprod2))
print(dir(confprod2))

""" print(isinstance(confprod1, Cake))
print(type(confprod1) is Cake)
print(confprod1.__class__)

print('Conf attribs', vars(confprod1))
print('Cake attribs', vars(Cake))
print('Conf attribs', dir(confprod1))
print('Cake attribs',dir(Cake)) """