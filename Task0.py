
from random import randint

isor = []
for i in range(30):
   isor.append(randint(-100, 100))

maxnumber = max(isor)
print(isor)
print("Макс. число =", maxnumber)
print("Порядковий номер макс. числа =", int(isor.index(maxnumber))+1)
print("Парні(-), що знаходяться поруч:")

for i in range(29):
  if isor[i] < 0 and isor[i+1] < 0:
    print(isor[i], isor[i+1])
  
  