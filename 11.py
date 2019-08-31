##choice ='''
##
##choose on from the list:
##'load data' -\t\t 1
##'export data' -\t\t 2
##'analyze & predict' -\t 3
##
##'''
##
##optlisted={'1':'load data', '2':'export data', '3':'analyze & predict'}
##
##choicenr=input(choice)
##
##while choicenr:
##    if not choicenr.isdigit():
##        print('it is not number')
##        choicenr=input(choice)
##        continue
##    else:
##        if choicenr in optlisted:
##            print(optlisted[choicenr])
##            break
##        else:
##            print('Incorrect number')
##            choicenr=input(choice)
##            continue


options = ['load data', 'export data', 'analyze & predict']
choice = 'x'

def DisplayOptions(optlist):
    for opt in optlist:
        print('%d - '%(optlist.index(opt)+1)+opt) 
    return input()
    

while choice:
    choice=DisplayOptions(options)
    if choice:    
        try:
            choice_num=int(choice)
            if choice_num >0 and choice_num <=3:
                print(options[choice_num-1])
            else:
                print('incorrect choice')
        except ValueError:
            print('a number must be entered')
            continue
    else:
        input('press enter to end')
     



