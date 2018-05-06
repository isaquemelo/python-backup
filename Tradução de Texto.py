qnty = int(input())
count = 0
words = {}

while count < qnty:
    count += 1
    term = input().replace(" ", "").split("=>")
    original = term[0]
    translated = term[1]
    words[original] = translated

while True:
    final = ""
    sentences = input().split()
    if sentences[0] == '*':
        break

    for i in sentences:
        ultimo = len(sentences)-1
        try:
            if i == sentences[ultimo]:
                final += "{}".format(words[i])
            else:
                final += "{} ".format(words[i])
        except:
            print("ERRO")
            pass

    print(final)