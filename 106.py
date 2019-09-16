class NoDuplicates:

    def __init__(self, list):
        self.list=list

    def __call__(self, new_items):
        for item in new_items:
            if item not in self.list:
                self.list.append(item)

    def __str__(self):
        list=''
        for i in self.list:
            list+=str(i)+', '
        return list


my_no_dup_list = NoDuplicates([])
print(my_no_dup_list.list)

my_no_dup_list(['keyboard','mouse'])
print(my_no_dup_list.list)

my_no_dup_list(['keyboard','mouse', 'pendrive'])
print(my_no_dup_list.list)

my_no_dup_list(['charger', 'pendrive'])
print(my_no_dup_list.list)

print(my_no_dup_list)
