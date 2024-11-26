#sum of 1 to 100 numbers
num = 100
sum = 0

for i in range(num+1):
    sum += i
print(sum)

#odd number from 1 to 100
o=[]
for i in range(num+1):
    if i%2 != 0:
        o.append(i)
print(o)

#even number from 1 to 100
e=[]
for i in range(num+1):
    if i != 0 and i%2 == 0:
        e.append(i)
print(e)


