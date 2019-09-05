import pickle
import os
import glob

kindToBeTexted = 'cake'

class Cake:

    known_types = ['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel', 'cookies', 'honey-cake','other']
    bakery_offer=[]

    def __init__(self, name, kind, taste, addictions, fillings, gluten_free, text):
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
        if self.kind == 'cake' or text == '':
            self.__text=text
        else:
            print('The text variable is not avalable for that kind ({}). It is admissible only for "cake" or "".'.format(kind))
            self.__text=''
    def show_info(self):
        print(self.name.upper())
        print('Kind:\t\t', self.kind)
        print('Taste:\t\t', self.taste)
        print('Additives:')
        for a in self.addictions:
            print('\t\t',a) 
        print('Filling:\t', self.fillings)
        print('Gluten-free:\t', self.__gluten_free)
        if self.__text:
            print('Text:\t\t', self.__text)
        print('-'*20)
    def set_filling(self, filling):
        self.fillings = filling
    def add_additives(self, adds):
        self.addictions.extend(adds)
    def __get_text(self):
        return self.__text
    def __set_text(self, new_text):
        if self.kind == kindToBeTexted :
            self.__text = new_text
    Text = property(__get_text, __set_text, None, 'A new text wille be added on the cake')
    def save_to_file(self, path):
        with open(path, 'wb') as f:
            return pickle.dump(self, f)
    @classmethod
    def read_from_file(cls, path):
        with open(path, 'rb') as f:
            new_cake= pickle.load(f)
            print(new_cake)
        cls.bakery_offer.append(new_cake)
        return new_cake

    @staticmethod
    def get_bakery_files1(dir):
        cakes_list=[]
        for d in os.listdir(dir):
            if '.bakery' in d:
                cakes_list.append(os.getcwd()+'/'+d)
        return print(cakes_list)
    @staticmethod
    def get_bakery_files2(dir):
        return print(glob.glob(dir+'/*.bakery'))



confprod1 = Cake('Chocolate cake', 'cake', 'chocolate', ['caramel glaze'], 'strawberries jam', False, 'Happy 10th Birthday, Alice')
confprod2 = Cake('Butter cakes', 'cookies', 'creamy', ['sugar icing', 'nuts'], 'raspberry', False, '')
confprod3 = Cake('Gingerbread', 'honey-cake', 'spicy', ['sugar sprinkles'], '', True, '')

confprod3.set_filling('apple jam')
confprod1.add_additives((['whipped cream', 'blueberries']))
confprod4 = Cake('Cocoa waffle','waffle','cocoa',[],'cocoa', False, 'Happy Anniversary, Sarah and James')

confprod2.__gluten_free = True
confprod2._Cake__gluten_free = True
del confprod2.__gluten_free

confprod1.Text ='The best wishes!!'
confprod2.text ='The best wishes!!'

#for c in Cake.bakery_offer:
    #c.show_info()

##print(dir(confprod1))

filepath1=os.path.join(os.getcwd(), 'confprod1.bakery')
filepath2=os.path.join(os.getcwd(), 'confprod2.bakery')

confprod1.save_to_file(filepath1)
confprod2.save_to_file(filepath2)

fdir = os.getcwd()
print(fdir)
confprod1.get_bakery_files1(fdir)
confprod2.get_bakery_files1(fdir)
Cake.get_bakery_files2(fdir)
Cake.get_bakery_files2(fdir)

confprod5 = Cake.read_from_file(filepath1)
print(confprod1)
print(confprod5)
confprod1.show_info()
confprod5.show_info()
confprod6=confprod2
confprod6.show_info()
print(Cake.bakery_offer)
print(confprod6)
print(confprod2)

""" print(isinstance(confprod1, Cake))
print(type(confprod1) is Cake)
print(confprod1.__class__)

print('Conf attribs', vars(confprod1))
print('Cake attribs', vars(Cake))
print('Conf attribs', dir(confprod1))
print('Cake attribs',dir(Cake)) """