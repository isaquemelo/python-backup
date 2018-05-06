numero1 = int(input())


def get_prime_numbers(max_number):
    # Crear una lista que contiene el estado (tachado/no tachado)
    # de cada número desde 2 hasta max_number.
    numbers = [True, True] + [True] * (max_number - 1)
    # Se comienza por el 2. Esta variable siempre tiene un
    # número primo.
    last_prime_number = 2
    # Esta variable contiene el número actual en la lista,
    # que siempre es un múltiplo de last_prime_number.
    i = last_prime_number

    # Proceder siempre que el cuadrado de last_prime_number (es decir,
    # el último número primo obtenido) sea menor o igual que max_number.
    while last_prime_number ** 2 <= max_number:
        # Tachar todos los múltiplos del último número primo obtenido.
        i += last_prime_number
        while i <= max_number:
            numbers[i] = False
            i += last_prime_number
        # Obtener el número inmediatamente siguiente al último
        # número primo obtenido (last_prime_number) que no esté tachado.
        j = last_prime_number + 1
        while j < max_number:
            if numbers[j]:
                last_prime_number = j
                break
            j += 1
        i = last_prime_number

    # Retornar todas los números de la lista que no están tachados.
    return [i + 2 for i, not_crossed in enumerate(numbers[2:]) if not_crossed]

def isprime(n):
    return n in get_prime_numbers(n)

def gera_primos(qnt):
    qntPrimos = 0
    numero = 1
    while True:
        if qnt == 0:
            break
        if qntPrimos == qnt:
            break
        numero += 1
        if isprime(numero):
            qntPrimos+=1
            print(numero)


gera_primos(numero1)
