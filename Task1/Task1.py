f = input("Рядок:")
ll = len(f)
m1 = []
m2 = []
i = 0

while i < ll:
    f_int = ''
    q = f[i]
    while '0' <= q <= '9':
        f_int += q
        i += 1
        if i < ll:
            q = f[i]
        else:
            break
    i += 1
    if f_int != '':
        m1.append(int(f_int))
print("Вивід чисел:",m1)

for w in '1234567890':
    f=f.replace(w, '')
f.strip(' ')
while f.find('  ') != -1:
    f = f.replace('  ', ' ')
print("Вивід слів:",f)
def cap(f):
     f, result = f.title(), ""
     for word in f.split():
        result += word[:-1] + word[-1].upper() + " "
     return result[:-1]     

print("\nПерша та остання заглавні:\n", cap(f), sep='')

l_numb = max(m1)
print("Макс. число=",l_numb)

for i in range(len(m1)):
    if m1[i] != l_numb:
        m2.append(m1[i]**i)
print("Массив в степені:",m2)
