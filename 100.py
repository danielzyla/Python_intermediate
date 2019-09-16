class Cake:
    
    known_kinds = ['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel','other']
    bakery_offer = []
    
    def __init__(self, name, kind, taste, additives, filling, gluten_free,text):
    
        self.name = name
        if kind in self.known_kinds:
            self.kind = kind
        else:
            self.kind = 'other'
        self.__taste = taste
        self.__additives = additives.copy()
        self.filling = filling
        self.bakery_offer.append(self)
        self.__gluten_free = gluten_free
        if kind == 'cake' or text == '':
            self.__text = text
        else:
            self.__text = ''
            print('>>>>>Text can be set only for cake ({})'.format(name))
    
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
        print("Gluten free: {}".format(self.__gluten_free))
        if len(self.__text) > 0:
            print("Text:      {}".format(self.__text))
        print('-'*20)
    
    @property
    def taste(self):
        return self.__taste

    @taste.setter
    def taste(self, taste):
        self.__taste = taste
    
    @property
    def additives(self):
        return self.__additives
    
    @additives.setter
    def additives(self, additives):
        self.__additives.extend(additives)
    
    #def __get_text(self):
        #return __text

    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, new_text):
        if self.kind == 'cake':
            self.__text = new_text
        else:
            print('>>>>>Text can be set only for cake ({})'.format(self.name))
    
    @text.deleter
    def text(self):
        self.__text = ''
    


    #@Text = property(__get_text, __set_text, None, 'Text on the cake')
    
cake01 = Cake('Vanilla Cake','cake', 'vanilla', ['chocolade', 'nuts'], 'cream', False, 'Happy Birthday Margaret!')
cake02 = Cake('Chocolade Muffin','muffin', 'chocolade', ['chocolade'], '', False, '')
cake03 = Cake('Super Sweet Maringue','meringue', 'very sweet', [], '', True, '')
cake04 = Cake('Cocoa waffle','waffle','cocoa',[],'cocoa', False, 'Good luck!')
    
print("Today in our offer:")
# for c in Cake.bakery_offer:
#     c.show_info()
    
cake01.text = 'Happy birthday!'
cake02.text = '18'
cake03.additives = ['soft sugar']
cake02.additives = ['vanila cream']
cake03.taste = 'cherry'

for c in Cake.bakery_offer:
    c.show_info()




#del cake01.text
#cake02.show_info()
#print(cake01.text)
#cake02.taste = 'strawberry'
