class Person():

    def __init__(self, firstname, lastname):
        self.first = firstname
        self.last = lastname
        #self.fullname = self.first + ' '+ self.last

    @property    
    def fullname(self):
        return self.first + ' '+ self.last


    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

person = Person('selva', 'prabhakaran')
print(person.first)  #> selva
print(person.last)  #> prabhakaran
print(person.fullname)  #> selva prabhakaran
print(person.email())  #> selva.prabhakaran@email.com

person.last = 'prasanna'
print(person.last)  #> prasanna
print(person.fullname)  #> selva prabhakaran
print(person.email())  #> selva.prasanna@email.com
