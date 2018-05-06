'''

ESTRUTURA DE DADOS:

4 * (-)  + 1 * (-) + 4* (-)

4 * (-)  + 1 * (|) + 4* (-)
3 * (-)  + 3 * (|) + 3* (-)
2 * (-)  + 5 * (|) + 2* (-)
1 * (-)  + 7 * (|) + 1* (-) ----> MEIO
2 * (-)  + 5 * (|) + 2* (-)
3 * (-)  + 3 * (|) + 3* (-)
4 * (-)  + 1 * (|) + 4* (-)


4 * (-)  + 1 * (-) + 4* (-)


'''

n = int(input())
totalLen = (n *2) + 1

background = "."
diamond = "*"




count = 1
for i in range(n,0,-1):
    print(i*background, diamond*count, sep="")
    count += 2
count -= 2

for i in range(1,n+1):

    print(i*background, diamond*count, sep="")

    count -= 2

