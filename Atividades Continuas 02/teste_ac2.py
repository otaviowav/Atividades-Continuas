import atividade_conta

contas = []
idx_conta_atual = 0
conta_atual = ''
while True:
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
        status_conta = 'desativada'
        if contas[idx_conta_atual].ativa:
            status_conta = 'ativa'
        print(f'Conta atual: {contas[idx_conta_atual].titular} ({status_conta})'.center(35))
    else:
        print('Nenhuma conta selecionada'.center(35))
    print('-'*35)

    act = input("Digite um número: ")
    print()
    if act == '0':
        break

    # Abrir nova conta
    if act == '1':
        print('     ', '-'*50)
        print('     Abertura de conta'.center(55))
        print('     ', '-'*50)
        titular = input('       Nome do titular:'.ljust(25))
        agencia = input('       Agência:'.ljust(25))
        numero = input('       Número:'.ljust(25))
        while True:
            try:
                saldo_inicial = float(input('       Saldo Inicial:'.ljust(25)))
            except ValueError:
                print('     Valor inválido! Digite novamente.'.center(55))
                continue
            if isinstance(saldo_inicial, float):
                break
        print('     ', '-'*50)
        ask = '0'
        while True:
            ask = input('       Para confirmar digite 1, cancelar 0: ')
            if ask == '1' or ask == '0':
                break
        if ask == '1':
            conta = atividade_conta.Conta(titular, agencia, numero, saldo_inicial)
            contas.append(conta)
            conta_atual = conta
            idx_conta_atual = len(contas)-1
            print()
            print('     Conta criada(desativada)'.center(55))
            print('     ', '-'*50, '\n')
        elif ask == '0':
            print()
            print('     Operação cancelada'.center(55))
            print('     ', '-'*50, '\n')

    # Saldo da conta atual
    elif act == '2':
        if not isinstance(conta_atual, atividade_conta.Conta):
            print('Selecione ou abra uma conta!')
        else:
            print('     ', '-'*40)
            print('     Saldo em conta'.center(45))
            print('     ', '-'*40)
            print(f'       Titular: {contas[idx_conta_atual].titular}')
            print(f'       Agência: {contas[idx_conta_atual].agencia} | Número: {contas[idx_conta_atual].numero}')
            print(f'\n       SALDO:\t{contas[idx_conta_atual].saldo:.2f}')
            print('     ', '-'*40)

    # Depositar na conta atual
    elif act == '3':
        if not isinstance(conta_atual, atividade_conta.Conta):
            print('Selecione ou abra uma conta!')
        else:
            print('     ', '-'*50)
            print('     Depositar'.center(55))
            print('     ', '-'*50)
            valor = '0'
            if contas[idx_conta_atual].ativa:
                while True:
                    valor = input('       Valor a depositar(0 para cancelar): ')
                    if valor == '0':
                        break
                    try:
                        valor = float(valor)
                    except ValueError:
                        print('       Entrada inválida!')
                        continue
                    if valor > 0:
                        contas[idx_conta_atual].depositar(valor)
                        print(f'       Deposito de {valor} realizado com sucesso!')
            else:
                print('       CONTA DESATIVADA!')
                print('       A conta deve estar ativada para depositar!')
            print('     ', '-'*50)

    # Sacar da conta atual
    elif act == '4':
        if not isinstance(conta_atual, atividade_conta.Conta):
            print('Selecione ou abra uma conta!')
        else:
            print('     ', '-'*60)
            print('     Sacar'.center(65))
            print('     ', '-'*60)
            if contas[idx_conta_atual].ativa:
                while True:
                    valor = input('       Valor para saque(0 para cancelar): ')
                    if valor == '0':
                        break
                    try:
                        valor = float(valor)
                    except ValueError:
                        print('       Entrada inválida!')
                        continue
                    if valor > 0:
                        if contas[idx_conta_atual].saldo >= valor:
                            contas[idx_conta_atual].sacar(valor)
                            print(f'       Saque de {valor} realizado com sucesso!')
                            print(f'       Saldo restante: {contas[idx_conta_atual].saldo:.2f}')
                        else:
                            print('       Saldo insuficiente!')
            else:
                print('       CONTA DESATIVADA!')
                print('       A conta deve estar ativada para sacar!')
            print('     ', '-'*60)

    # Transferir para outra conta
    elif act == '5':
        if not isinstance(conta_atual, atividade_conta.Conta):
            print('Selecione ou abra uma conta!')
        else:
            print('     ', '-'*60)
            print('     Transferência - Contas disponíveis'.center(65))
            print('     ', '-'*60)
            print('        Id.        |'.center(20), 'Informações'.center(25))
            print('     ', '-'*60)
            disponiveis = False
            idx_contas = []
            n = 1
            for i in range(len(contas)):
                if i != idx_conta_atual:
                    print('        ', f'{n}'.ljust(3), f'\t\tTitular: {contas[i].titular}')
                    print('        ', f'   \t\tAgência: {contas[i].agencia}   |   Número: {contas[i].numero}')
                    status = 'DESATIVADA'
                    if contas[i].ativa:
                        status = 'ATIVA'
                    print('        ', f'   \t\tSTATUS: {status}')
                    disponiveis = True
                    idx_contas.append(n-1)
                n += 1
            if disponiveis:
                print('     ', '-'*60)
            ask = '0'
            if disponiveis:
                transf = False
                err = False
                while True:
                    ask = input('       Fazer transferência? 1 para sim, 0 para não: ')
                    if ask == '0':
                        break
                    if ask == '1':
                        while True:
                            to_conta = input('       Id da conta destino(0 para cancelar): ')
                            if to_conta == '0':
                                break
                            if to_conta.isdigit():
                                if int(to_conta)-1 in idx_contas:
                                    if contas[int(to_conta)-1].ativa and contas[idx_conta_atual].ativa:
                                        while True:
                                            valor_transf = input('       Valor da transferência(0 para cancelar): ')
                                            if valor_transf == '0':
                                                break
                                            try:
                                                valor_transf = float(valor_transf)
                                            except ValueError:
                                                print('       Valor inválido!')
                                                continue
                                            if contas[idx_conta_atual].saldo >= valor_transf:
                                                contas[idx_conta_atual].transferir(contas[int(to_conta)-1], valor_transf)
                                                print(f'       A quantia de {valor_transf:.2f} foi transferida com sucesso!')
                                                transf = True
                                                break
                                            else:
                                                print('       Saldo insuficiente!')
                                    else:
                                        print('       A conta atual ou a conta de destino encontra-se desativada!')
                                        print('       Ambas as contas devem estar ativas para transferir!')
                                        err = True
                                        break
                                else:
                                    print('       Conta inexistente!')
                            else:
                                print('       Conta inválida!')
                            if transf or err:
                                break
                    if transf:
                        break
                print('     ', '-'*60)
            else:
                print('       Não existe contas para transferir!'.center(65))
                print('     ', '-'*60)

    # Extrato da conta atual
    elif act == '6':
        if not isinstance(conta_atual, atividade_conta.Conta):
            print('Selecione ou abra uma conta!')
        else:
            contas[idx_conta_atual].tirar_extrato()

    # Exibir contas / Trocar de conta
    elif act == '7':
        print('     ', '-'*60)
        print('     Contas abertas'.center(65))
        print('     ', '-'*60)
        print('        Id.        |'.center(20), 'Informações'.center(25))
        print('     ', '-'*60)
        n = 1
        for i in contas:
            print('        ', f'{n}'.ljust(3), f'\t\tTitular: {i.titular}')
            print('        ', f'   \t\tAgência: {i.agencia}   |   Número: {i.numero}')
            status = 'DESATIVADA'.ljust(10)
            if i.ativa:
                status = 'ATIVA'.ljust(10)
            print('        ', f'   \t\tSTATUS: {status}   |   SALDO: {i.saldo:.2f}')
            print()
            n += 1
        print('     ', '-'*60)
        if contas:
            ask = '0'
            while True:
                conta_trocada = False
                ask = input('       Trocar de conta? 1 para sim, 0 para não: ')
                if ask == '0':
                    break
                if ask == '1':
                    while True:
                        to_conta = input('       Id da conta(0 para cancelar): ')
                        if to_conta == '0':
                            break
                        if to_conta.isdigit():
                            if int(to_conta)-1 <= len(contas):
                                conta_atual = contas[int(to_conta)-1]
                                idx_conta_atual = int(to_conta)-1
                                print(f'       Conta Id. {to_conta} selecionada!')
                                conta_trocada = True
                                break
                            else:
                                print('       Conta inexistente!')
                        else:
                            print('       Conta inexistente!')
                if conta_trocada:
                    break
        else:
            print('       Não existe contas abertas!'.center(65))
        print('     ', '-'*60)

    # Ativar/Desativar uma conta
    elif act == '8':
        if not isinstance(conta_atual, atividade_conta.Conta):
            print('Selecione ou abra uma conta!')
        else:
            print('     ', '-'*60)
            print('     Ativar/Desativar'.center(65))
            print('     ', '-'*60)
            if not contas[idx_conta_atual].ativa:
                while True:
                    print('       A conta atual encontra-se DESATIVADA!')
                    opt = input('       Deseja ATIVA-LA? 1 para sim, 0 para não: ')
                    if opt == '0':
                        break
                    if opt == '1':
                        contas[idx_conta_atual].ativa = True
                        print('       CONTA ATIVADA!')
                        break
            else:
                while True:
                    print('       A conta atual encontra-se ATIVA!')
                    opt = input('       Deseja DESATIVA-LA? 1 para sim, 0 para não: ')
                    if opt == '0':
                        break
                    if opt == '1':
                        contas[idx_conta_atual].ativa = False
                        print('       CONTA DESATIVADA!')
                        break

    # Relatorio de todas as contas
    elif act == '9':
        print('#'*70)
        print('Relatório de contas'.center(70))
        print('#'*70)
        print('Id.'.center(20), '|', 'Informações'.center(49))
        print('#'*70)
        n = 1
        for i in contas:
            print(f'   {n}'.ljust(3), f'\t\t\tTitular: {i.titular}')
            print(f'   \t\t\tAgência: {i.agencia}   |   Número: {i.numero}')
            status = 'DESATIVADA'
            if i.ativa:
                status = 'ATIVADA'
            print(f'   \t\t\tSTATUS: {status}')
            print(f'\n\t\t\tSALDO: {i.saldo:.2f}')
            print('\n\t\t\tOperações:')
            i.tirar_extrato()
            print()
            print('#'*70)
            n += 1
