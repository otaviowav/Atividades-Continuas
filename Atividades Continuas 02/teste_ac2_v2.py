import atividade_conta

contas = []
idx_conta_atual = 0
conta_atual = ''


def open_menu():
    print()
    print('-'*35)
    print('menu'.center(35))
    print('-'*35)
    print('| 1. Abrir conta'.ljust(34), end='|\n')
    print('| 2. Saldo'.ljust(34), end='|\n')
    print('| 3. Depositar'.ljust(34), end='|\n')
    print('| 4. Sacar'.ljust(34), end='|\n')
    print('| 5. Transferir'.ljust(34), end='|\n')
    print('| 6. Extrato'.ljust(34), end='|\n')
    print('| 7. Contas/Trocar'.ljust(34), end='|\n')
    print('| 8. Ativar/Desativar conta'.ljust(34), end='|\n')
    print('| 9. Relatório de contas'.ljust(34), end='|\n')
    print('| 0. Sair'.ljust(34), end='|\n')
    print('-'*35)
    if isinstance(conta_atual, atividade_conta.Conta):
        status = 'desativada'
        if contas[idx_conta_atual].ativa:
            status = 'ativa'
        print(f'Conta atual: {contas[idx_conta_atual].titular} ({status})'.center(35))
    else:
        print('Nenhuma conta selecionada'.center(35))
    print('-'*35)


def abrir_conta():
    global contas
    global conta_atual
    global idx_conta_atual
    make_title('Abertura de conta', 50)
    print('\t', end='')
    titular = input(' Nome do titular: '.ljust(20))
    print('\t', end='')
    agencia = input(' Agência: '.ljust(20))
    print('\t', end='')
    numero = input(' Número: '.ljust(20))
    while True:
        print('\t', end='')
        saldo_inicial = input(' Saldo Inicial: '.ljust(20))
        try:
            saldo_inicial = float(saldo_inicial)
        except ValueError:
            print('\t', ' Valor inválido!'.center(50), sep='')
            print('\t')
            continue
        if isinstance(saldo_inicial, float) and saldo_inicial > 0:
            break
        else:
            print('\t', ' O saldo inicial deve ser positivo!'.center(50), sep='')
            print('\t')
            continue
    print('\t', '-'*50, sep='')
    confirm = '0'
    while True:
        print('\t', end='')
        confirm = input(' Para confirmar digite 1, cancelar 0: ')
        if confirm == '1' or confirm == '0':
            break
    if confirm == '1':
        conta = atividade_conta.Conta(titular, agencia, numero, saldo_inicial)
        contas.append(conta)
        conta_atual = conta
        idx_conta_atual = len(contas)-1
        print('\t', 'Conta criada (desativada)'.center(50), sep='')
        print('\t')
    elif confirm == '0':
        print('\t', 'Operação cancelada'.center(50), sep='')
        print('\t')
    print('\t', '-'*50, sep='')
    print()


def saldo():
    if not isinstance(conta_atual, atividade_conta.Conta):
        print('Selecione ou abra uma conta!')
    else:
        make_title('Saldo em conta', 50)
        print('\t', ' Titular: '.ljust(11), f'{contas[idx_conta_atual].titular}', sep='')
        print('\t', ' Agência: '.ljust(11), f'{contas[idx_conta_atual].agencia}', '   |   ', 'Número: '.ljust(9), f'{contas[idx_conta_atual].numero}', sep='')
        print('\t')
        print('\t', ' SALDO: '.ljust(11), f'{contas[idx_conta_atual].saldo:.2f}', sep='')
        print('\t', '-'*50, sep='')
    print()


def depositar():
    if not isinstance(conta_atual, atividade_conta.Conta):
        print('Selecione ou abra uma conta!')
    else:
        make_title('Depósito na conta', 50)
        valor = '0'
        if contas[idx_conta_atual].ativa:
            while True:
                print('\t', end='')
                valor = input(' Valor a depositar (0 para cancelar): ')
                if valor == '0':
                    break
                try:
                    valor = float(valor)
                except ValueError:
                    print('\t', 'Entrada inválida!'.center(50), sep='')
                    print('\t')
                    continue
                if valor > 0:
                    contas[idx_conta_atual].depositar(valor)
                    print('\t', f'Deposito de {valor} realizado com sucesso!'.center(50), sep='')
                    print('\t')
                else:
                    print('\t', 'Valor inválido!'.center(50), sep='')
                    print('\t')
        else:
            print('\t', 'CONTA DESATIVADA!'.center(50), sep='')
            print('\t', 'A conta deve estar ativa para depositar!'.center(50), sep='')
        print('\t', '-'*50, sep='')
    print()


def sacar():
    if not isinstance(conta_atual, atividade_conta.Conta):
        print('Selecione ou abra uma conta!')
    else:
        make_title('Sacar', 50)
        if contas[idx_conta_atual].ativa:
            while True:
                print('\t', end='')
                valor = input(' Valor para saque (0 para cancelar): ')
                if valor == '0':
                    break
                try:
                    valor = float(valor)
                except ValueError:
                    print('\t', 'Entrada inválida!'.center(50), sep='')
                    print('\t')
                    continue
                if valor > 0:
                    if contas[idx_conta_atual].saldo >= valor:
                        contas[idx_conta_atual].sacar(valor)
                        print('\t', f'Saque de {valor} realizado com sucesso!'.center(50), sep='')
                        print('\t', f'Saldo final: {contas[idx_conta_atual].saldo:.2f}'.center(50), sep='')
                        print('\t')
                    else:
                        print('\t', 'Saldo insuficiente!'.center(50), sep='')
                        print('\t')
                else:
                    print('\t', 'Valor inválido!'.center(50), sep='')
                    print('\t')
        else:
            print('\t', 'CONTA DESATIVADA!'.center(50), sep='')
            print('\t', 'A conta deve estar ativa para sacar!'.center(50), sep='')
        print('\t', '-'*50, sep='')
    print()


def transferir():
    if not isinstance(conta_atual, atividade_conta.Conta):
        print('Selecione ou abra uma conta!')
    else:
        make_title('Transferência - Contas disponíveis', 65)
        print('\t', f'     Conta atual: {idx_conta_atual+1}', sep='')
        print('\t', f'     Titular: {contas[idx_conta_atual].titular}   |   SALDO: {contas[idx_conta_atual].saldo:.2f}', sep='')
        print('\t', '-'*65, sep='')
        print('\t', 'Id.'.center(14), '|', 'Informações'.center(50), sep='')
        print('\t', '-'*65, sep='')
        idx_contas = []
        n = 1
        for i in range(len(contas)):
            if i != idx_conta_atual:
                print('\t', ' '*5, f'{n}'.ljust(19), f'Titular: {contas[i].titular}'.ljust(49), sep='')
                print('\t', ' '*24, f'Agência: {contas[i].agencia}   |   Número: {contas[i].numero}'.ljust(49), sep='')
                status = 'DESATIVADA'
                if contas[i].ativa:
                    status = 'ATIVA'
                print('\t', ' '*24, f'STATUS: {status}'.ljust(49), sep='')
                idx_contas.append(n-1)
            n += 1
        ask = '0'
        if len(idx_contas) > 0:
            print('\t', '-'*65, sep='')
            transf = False
            err = False
            while True:
                print('\t', end='')
                ask = input(' Fazer transferência? 1 para sim, 0 para não: ')
                if ask == '0':
                    break
                if ask == '1':
                    while True:
                        print('\t', end='')
                        to_conta = input(' Id da conta destino (0 para cancelar): ')
                        if to_conta == '0':
                            break
                        try:
                            to_conta = int(to_conta)
                        except ValueError:
                            print('\t', 'Conta inválida!'.center(65), sep='')
                            print('\t')
                            continue
                        if to_conta-1 in idx_contas:
                            if contas[to_conta-1].ativa and contas[idx_conta_atual].ativa:
                                while True:
                                    print('\t', end='')
                                    valor = input(' Valor da transferência (0 para cancelar): ')
                                    if valor == '0':
                                        break
                                    try:
                                        valor = float(valor)
                                    except ValueError:
                                        print('\t', 'Valor inválido!'.center(65), sep='')
                                        print('\t')
                                        continue
                                    if contas[idx_conta_atual].saldo >= valor:
                                        contas[idx_conta_atual].transferir(contas[to_conta-1], valor)
                                        print('\t', f'A quantia de {valor:.2f} foi transferida com sucesso!'.center(65), sep='')
                                        transf = True
                                        break
                                    else:
                                        print('\t', 'Saldo insuficiente!'.center(65), sep='')
                                        print('\t')
                            else:
                                print('\t', 'A conta atual ou de destino encontra-se desativada!'.center(65), sep='')
                                print('\t', 'Ambas as contas devem estar ativas!'.center(65), sep='')
                                print('\t')
                                err = True
                                break
                        else:
                            print('\t', 'Conta indisponível!'.center(65), sep='')
                            print('\t')

                        if transf or err:
                            break
                if transf:
                    break
        else:
            print('\t', 'Não há contas para transferir!'.center(65), sep='')
            print('\t')
        print('\t', '-'*65, sep='')
    print()


def extrato():
    if not isinstance(conta_atual, atividade_conta.Conta):
        print('Selecione ou abra uma conta!')
    else:
        contas[idx_conta_atual].tirar_extrato()
    print()


def chaveia_conta():
    global contas
    global conta_atual
    global idx_conta_atual
    make_title('Trocar de conta', 65)
    print('\t', 'Id.'.center(14), '|', 'Informações'.center(50), sep='')
    print('\t', '-'*65, sep='')
    n = 1
    for i in contas:
        print('\t', ' '*5, f'{n}'.ljust(19), f'Titular: {i.titular}'.ljust(49), sep='')
        print('\t', ' '*24, f'Agência: {i.agencia}   |   Número: {i.numero}'.ljust(49), sep='')
        status = 'DESATIVADA'
        if i.ativa:
            status = 'ATIVA'
        print('\t', ' '*24, f'STATUS: {status}'.ljust(49), sep='')
        print('\t', ' '*24, f'SALDO: {i.saldo:.2f}'.ljust(49), sep='')
        print()
        n += 1
    print('\t', '-'*65, sep='')
    if contas:
        ask = '0'
        while True:
            conta_trocada = False
            print('\t', end='')
            ask = input(' Trocar de conta? 1 para sim, 0 para não: ')
            if ask == '0':
                break
            if ask == '1':
                while True:
                    print('\t', end='')
                    to_conta = input(' Id da conta (0 para cancelar): ')
                    if to_conta == '0':
                        break
                    try:
                        to_conta = int(to_conta)
                    except ValueError:
                        print('\t', 'Conta inválida!'.center(65), sep='')
                        print('\t')
                        continue
                    if to_conta-1 <= len(contas):
                        conta_atual = contas[to_conta-1]
                        idx_conta_atual = to_conta-1
                        print('\t', f'Conta Id. {to_conta} selecionada!'.center(65), sep='')
                        conta_trocada = True
                        break
                    else:
                        print('\t', 'Conta inexistente!'.center(65), sep='')
                        print('\t')
            if conta_trocada:
                break
    else:
        print('\t', 'Não existe contas abertas!'.center(65), sep='')
    print('\t', '-'*65, sep='')
    print()


def ativar():
    if not isinstance(conta_atual, atividade_conta.Conta):
        print('Selecione ou abra uma conta!')
    else:
        make_title('Ativar/Desativar', 50)
        status = 'DESATIVADA'
        if contas[idx_conta_atual].ativa:
            status = 'ATIVA'
        while True:
            print('\t', f'A conta atual encontra-se {status}!'.center(50), sep='')
            print('\t')
            if status == 'DESATIVADA':
                print('\t', end='')
                confirm = input(' Deseja ATIVA-LA? 1 para sim, 0 para não: ')
                if confirm == '0':
                    break
                if confirm == '1':
                    contas[idx_conta_atual].ativa = True
                    print('\t', 'CONTA ATIVADA!'.center(50), sep='')
                    break
            else:
                print('\t', end='')
                confirm = input(' Deseja DESATIVA-LA? 1 para sim, 0 para não: ')
                if confirm == '0':
                    break
                if confirm == '1':
                    contas[idx_conta_atual].ativa = False
                    print('\t', 'CONTA DESATIVADA!'.center(50), sep='')
                    break
        print('\t', '-'*50, sep='')
    print()


def relatorio():
    make_title_relatorio('Relatório de contas', 65)
    print('Id.'.center(14), '|', 'Informações'.center(50), sep='')
    print('#'*65, sep='')
    n = 1
    for i in contas:
        print(' '*5, f'{n}'.ljust(19), f'Titular: {i.titular}'.ljust(49), sep='')
        print(' '*24, f'Agência: {i.agencia}   |   Número: {i.numero}'.ljust(49), sep='')
        status = 'DESATIVADA'
        if i.ativa:
            status = 'ATIVA'
        print(' '*24, f'STATUS: {status}'.ljust(49), sep='')
        print(' '*24, f'SALDO: {i.saldo:.2f}'.ljust(49), sep='')
        print()
        print(' '*5, '-OPERAÇÕES-'.ljust(49), sep='')
        i.tirar_extrato()
        print()
        print('#'*65)
        n += 1


def make_title(titulo, tamanho):
    print('\t', '-'*tamanho, sep='')
    print('\t', f'{titulo}'.center(tamanho), sep='')
    print('\t', '-'*tamanho, sep='')


def make_title_relatorio(titulo, tamanho):
    print('#'*tamanho, sep='')
    print(f'{titulo}'.center(tamanho), sep='')
    print('#'*tamanho, sep='')


while True:
    open_menu()
    act = input("Digite um número: ")
    print()
    if act == '0':
        break

    if act == '1':  # Abrir nova conta
        abrir_conta()
    elif act == '2':  # Saldo da conta atual
        saldo()
    elif act == '3':  # Depositar na conta atual
        depositar()
    elif act == '4':  # Sacar da conta atual
        sacar()
    elif act == '5':  # Transferir para outra conta
        transferir()
    elif act == '6':  # Extrato da conta atual
        extrato()
    elif act == '7':  # Exibir contas / Trocar de conta
        chaveia_conta()
    elif act == '8':  # Ativar/Desativar uma conta
        ativar()
    elif act == '9':  # Relatorio de todas as contas
        relatorio()
