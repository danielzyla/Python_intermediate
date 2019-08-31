projects = ['Brexit', 'Nord Stream', 'US Mexico Border']
leaders = ['Theresa May', 'Wladimir Putin', 'Donald Trump and Bill Clinton']


for proj, lead in zip(projects, leaders):
    print('The leader of {} is {}.'.format(proj, lead))

dates = ['2016-06-23', '2016-08-29', '1994-01-01']

print ('*'*30)

for proj, date, lead in zip(projects, dates, leaders):
    print('The leader of {} started {} is {}.'.format(proj, date, lead)) 

print ('*'*30)

for i, (proj, date, lead) in enumerate(zip(projects, dates, leaders)):
    print('{} - The leader of {} started {} is {}.'.format(i, proj, date, lead)) 
