import csv

f = open('Scripting_exercise.csv')

csv_f = csv.reader(f)

Jill = []
Candice = []
Alycia = []

for row in csv_f:
    if row[0] == 'Jill':
        Jill.append(row[2:4]) 
    elif row[0] == 'Candice':
        Candice.append(row[2:4])
    elif row[0] == 'Alycia':
        Alycia.append(row[2:4])

print(Jill)
# print(Candice)
# print(Alycia)


import csv

f = open('Scripting_exercise.csv')

csv_f = csv.reader(f)

extraction1 = []

for row in csv_f:
    extraction1.append(row[0:2]) 
print(extraction1)

f.close()
