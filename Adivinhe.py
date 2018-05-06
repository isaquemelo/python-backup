def gato(bit, password, attempt):
    position = 0
    exists = 0
    matchs = []

    for i in range(bit):
        if password[i] == attempt[i]:
            position += 1
            matchs.append(attempt[i])

    for i in range(bit):
        for f in range(bit):

            if password[i] == attempt[f]:

                if attempt[f] in matchs:
                    pass
                else:
                    exists += 1

    return "({},{})".format(position,exists)


qty = int(input())
count = 0
while count < qty:
    count += 1
    bit = int(input())
    password = list(input())
    position = 0
    exists = 0
    matchs = []

    while True:
        attempt = list(input())
        if attempt[0] == '0' and attempt[-1] == '0':
            break
        if (attempt == password):
            print("({},{})".format(bit,0))
            break
        print(gato(bit, password, attempt))



        attempt = ""


