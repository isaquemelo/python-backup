count = 0
one = []
two = []

while count < 20:
    count += 1
    number = int(input())
    one.append(number)
count = 0
while count < 20:
    count += 1
    number = int(input())
    two.append(number)
inter = []
for i in one:
    for f in two:
        if i == f:
            if not i in inter:
                inter.append(i)

inter = sorted(inter)

if not inter:
    print("VAZIO")
    exit()
for g in inter:
    print(g)