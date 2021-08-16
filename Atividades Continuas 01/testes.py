def eh_primo(n):
    num_divisores = 0 #Conta o numero de divisores de n
    candidato = 1 #número candidato a divisor
    while candidato <= n:
        if n % candidato == 0:
            num_divisores += 1
        candidato += 1
    if num_divisores == 2:
        return True
    else:
        return False

#Programa principal
resultado = eh_primo(20)
print(f'O Resultado da função é: {resultado}')
