class Cake:
    
    bakery_offer = []
    
    def __init__(self, name, kind, taste, additives, filling):
    
        self.name = name
        self.kind = kind
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling
        self.bakery_offer.append(self)
    
    def show_info(self):
        print("{}".format(self.name.upper()))
        print("Kind:        {}".format(self.kind))
        print("Taste:       {}".format(self.taste))
        if len(self.additives) > 0:
            print("Additives:")
            for a in self.additives:
                print("\t\t{}".format(a))
        if len(self.filling) > 0:
            print("Filling:     {}".format(self.filling))
        print('-'*20)

    def __str__(self):
        additives=''
        for additive in self.additives:
            additives+=additive+' '
        return '{} {} with {}'.format(self.kind, self.name, self.additives)
        #return self.kind+' '+self.name+' '+additives

    def __iadd__(self, additive):
        print(self.additives)
        if type(additive) is str:
            self.additives.append(additive)
            print(self.additives)
            return self
            #return Cake(self.name, self.kind, self.taste, self.additives, self.filling)
        elif type(additive) is list:
            self.additives.extend(additive)
            return self
            #return Cake(self.name, self.kind, self.taste, self.additives, self.filling)
        else:
            raise Exception('Inproper type given')

        
cake01 = Cake('Vanilla Cake','cake', 'vanilla', ['chocolade', 'nuts'], 'cream')

print(cake01)

cake01.show_info()

cake01+='sugar'

print(cake01)

cake01+=['jelly', 'apple cream']

print(cake01)
