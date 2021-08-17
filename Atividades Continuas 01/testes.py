def eh_primo(n):
    num_divisores = 0 #Conta o numero de divisores de n
    for i in range(1, n+1):
        if n % i == 0:
            num_divisores += 1
    if num_divisores == 2:
        return True
    else:
        return False

def lista_primos(n):
    primos_encontrados = [] # Começa com uma lista vazia
    for i in range(2, n): # Varia i de 2 até n-1
        if eh_primo(i):
            primos_encontrados.append(i)
    return primos_encontrados

def conta_primos(s):
    i = 0
    while i <= len(s):
        if eh_primo(s[i]):
            pass
            i += 1

lista = [11, 2, 3, 4, 11, 2, 5, 2]
conta_primos(lista)
#Programa principal
#print("O Resultado da função é:", lista_primos(10))


