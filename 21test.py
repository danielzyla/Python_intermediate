##for i in range(11,1, -1):
##    print(i)
##
##list = list(range(11,1,-1))
##print(type(list), list)



colors=["red", "orange", "green", "violet", "blue", "yellow"]

##def col(collist, n):
##    choice=collist[:]
##    if n in range(1,len(collist)+1):
##        mycolors=choice[:n]
##    return mycolors
##
##print(col(colors,5))



##for i in range(len(colors)+1):
##    for j in range(1,len(colors)+1):
##        if j>i:
##            print(colors[i:j])


def get_list_of_colors(colors, n):
    return colors[:n]
 
colors = ["red", "orange", "green", "violet", "blue", "yellow"]
 
for i in range(1,len(colors)+1):
    print(get_list_of_colors(colors, i))


korpo='''Korporacja (z łac. corpo – ciało, ratus – szczur; pol. ciało szczura) – organizacja, która pod przykrywką prowadzenia biznesu włada dzisiejszym światem. Wydawać się może utopijnym miejscem realizacji pasji zawodowych. W rzeczywistości jednak nie jest wcale tak kolorowo. Korporacja służy do wyzyskiwania człowieka w imię postępu. Rządzi w niej prawo dżungli. '''

print(korpo[korpo.index('(')+1:korpo.index(')')])

