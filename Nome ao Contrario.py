qnt = int(input())
array = input().split()
array1 = input().split()
del array[qnt:]
del array1[qnt:]

def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    for i in range(len(lst3)):
        lst3[i] = int(lst3[i])

    return sorted(lst3)

result = intersection(array, array1)
# Driver Code
for i in range(len(result)):
    print(result[i])


