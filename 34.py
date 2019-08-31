ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
         'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']


gen = ((pp, pk) for pp in ports for pk in ports)

i=0
for x in gen:    
    print(x)
    i+=1
print(i)

gen = ((pp, pk) for pp in ports for pk in ports if pp != pk)

i=0
for x in gen:    
    print(x)
    i+=1
print(i)

gen = ((pp, pk) for pp in ports for pk in ports if pp > pk)

i=0
for x in gen:    
    print(x)
    i+=1
print(i)
