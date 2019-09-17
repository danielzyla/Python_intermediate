import csv
import os

dir = os.getcwd()
filename = 'drugs.csv'
filepath = os.path.join(dir, filename)

with open(filepath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # for row in csvreader:
    #     print('|'.join(row))
    # print('|'.join(next(csvreader)))
    # print(next(csvreader))
    # print(next(csvreader))
    # print(next(csvreader))
    # print(next(csvreader))
    while True:
        try: 
            print('|'.join(next(csvreader)))
        except StopIteration:
            break
