# part1
import csv
file = open('books.csv')
A=0
for line in file:
    A+=1
print(A)
D=0
# part2
with open('books.csv',newline= '') as csvfile:
    reader = csv.DictReader(csvfile,delimiter=";")
    for row in reader:
        if len(row['Book-Title'])>30:
          D+=1
    print(D)
# part3
print('enter the full name of the author: ')
P=0
x=input(str)
with open('books.csv',newline= '') as csvfile:
    reader = csv.DictReader(csvfile,delimiter=";")
    for row in reader:
        if row['Book-Author'] == x:
            if row['Year-Of-Publication']=='2014' or row['Year-Of-Publication']=='2016' or row['Year-Of-Publication'] =='2017':
                print(row['Book-Title'])
                P+=1
    if P==0:
        print('is there a restriction on the issuance of books by this author or is there no such author in the library')
# part4
import random
m=1
u=1
d=0
filepath = r"books.csv"
f = open("gg.txt", "w")
while d<20:
    file = open(filepath, "r", newline="")
    i = random.randint(1, 9410)
    for row in file:
        a = row.split(';')
        if m == i:
            f.write(str(u)+') ')
            f.write(a[2] + '.' + a[1] + '-' + a[3] + '; \n')
            u+=1
        m+=1
    m=1
    d+=1
    file.close()
