# -*- coding: utf-8 -*-

import re
from itertools import chain

def magica(lista):
    a = b = c = d = e = f = g = h = i = j = k = l = m = n = o = p = q = r = s = t = u = v = x = y = z = 0
    ç = á = é = í = à = ô = ã = â = ê = 0
    final = []
    for ii in range(len(lista)):
        if lista[ii] == "ç":
            ç += 1
        elif lista[ii] == "á":
            á += 1
        elif lista[ii] == "é":
            é += 1
        elif lista[ii] == "í":
            í += 1
        elif lista[ii] == "à":
            à += 1
        elif lista[ii] == "ô":
            ô += 1
        elif lista[ii] == "ã":
            ã += 1
        elif lista[ii] == "â":
            â += 1
        elif lista[ii] == "ê":
            ê += 1
        elif lista[ii] == "a":
            a += 1
        elif lista[ii] == "b":
            b += 1
        elif lista[ii] == "c":
            c += 1
        elif lista[ii] == "d":
            d += 1
        elif lista[ii] == "e":
            e += 1
        elif lista[ii] == "f":
            f += 1
        elif lista[ii] == "g":
            g += 1
        elif lista[ii] == "h":
            h += 1
        elif lista[ii] == "i":
            i += 1
        elif lista[ii] == "j":
            j += 1
        elif lista[ii] == "k":
            k += 1
        elif lista[ii] == "l":
            l += 1
        elif lista[ii] == "m":
            m += 1
        elif lista[ii] == "n":
            n += 1
        elif lista[ii] == "o":
            o += 1
        elif lista[ii] == "p":
            p += 1
        elif lista[ii] == "q":
            q += 1
        elif lista[ii] == "r":
            r += 1
        elif lista[ii] == "s":
            s += 1
        elif lista[ii] == "t":
            t += 1
        elif lista[ii] == "u":
            u += 1
        elif lista[ii] == "v":
            v += 1
        elif lista[ii] == "x":
            x += 1
        elif lista[ii] == "y":
            y += 1
        elif lista[ii] == "z":
            z += 1
        else:
            pass
    contados = [[a, ["a"]], [b, ["b"]], [c, ["c"]], [d, ["d"]], [e, ["e"]], [f, ["f"]], [g, ["g"]], [h, ["h"]],
                [i, ["i"]], [j, ["j"]], [k, ["j"]], [l, ["l"]], [m, ["m"]], [n, ["n"]], [o, ["o"]], [p, ["p"]],
                [q, ["q"]], [r, ["r"]], [s, ["s"]], [t, ["t"]], [u, ["u"]], [v, ["v"]], [x, ["x"]], [y, ["y"]],
                [z, ["z"]], [ç, ["ç"]], [á, ["á"]], [é, ["é"]], [í, ["í"]], [à, ["à"]], [ô, ["ô"]], [ã, ["ã"]],
                [â, ["â"]], [ê, ["ê"]]]
    bau2 = sorted(sorted(contados, key=lambda x: x[1]), key=lambda x: x[0], reverse=True)
    for i in range(0,len(bau2)):
        if bau2[i][0] != 0:
            letra = bau2[i][1][0]
            numero = bau2[i][0]
            final.append([letra.upper(), numero])
        else:
            pass
    return final
geral = []
count = 0
while True:
    qnt = int(input())
    if qnt == 0:
        exit()
        break
    else:
        count +=1
        for countaa in range(qnt):
            entrada = input().lower()
            lista = list(entrada)
            geral.append(lista)
        print("TESTE {}".format(count))
        listao = (list(chain.from_iterable(geral)))
        final = magica(listao)
        for i in range(len(final)):
            print(final[i][0],final[i][1])
        del geral[:]
        del listao[:]