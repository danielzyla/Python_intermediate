class Cake:
    
    """Cake - class operatin on cakes available in bakery """

    bakery_offer = []
    
    def __init__(self, name, kind, taste, additives, filling):
        """
            init = agruments accepted
            name - name of the cake
            taste - taste of the cake
            additives - list of additives to the cake, empty is allowed
            filling - filling in the cake
            bakery_offer.append(self) - adds each cake object to bakery_offer list
        """
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
    
    @property
    def full_name(self):
        """Property fullname made of cake name and its kind"""
        return "--== {} - {} ==--".format(self.name.upper(), self.kind)


#help(Cake)
help(Cake.full_name)