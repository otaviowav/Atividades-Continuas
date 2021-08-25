class Conta:
    def __init__(self, titular, agencia, numero, saldo_inicial):
        self.__titular = titular
        self.__agencia = agencia
        self.__numero = numero
        self.__saldo_inicial = 0
        self.__ativa = True
        self.__operacoes = [('saldo inicial', saldo_inicial)]



    @property
    def titular(self):
        return self.__titular

    @property
    def agencia(self):
        return self.__agencia

    @property
    def numero(self):
        return self.__numero

    @property
    def saldo(self):
        return self.__saldo_inicial

    @property
    def ativa(self):
        self.__ativa = False

    @ativa.setter
    def ativa(self, situacao):
        self.__ativa = situacao
        if situacao == 1:
            return True 
            print('Conta ativa')
        if situacao == 2:
            return False
            print('Conta desativada')
        """
        Implemente o setter ativa
        """
        pass

    def depositar(self, valor):
        if valor < 0:
            return 'O valor deve ser positivo'
        self.__saldo_inicial += valor

    def sacar(self, valor):
        if valor < 0:
            return 'O valor deve ser positivo'
        if valor > self.__saldo_inicial:
            return 'Saldo insuficiente'
        self.__saldo_inicial -= valor

    def transferir(self, conta_destino, valor):
        """
        Implemente o método transferencia()
        """
        pass

    def tirar_extrato(self):
        """
        Implemente o método tirar_extrato()
        """
        pass


c1 = Conta('Otavio', 344, 1, 0)
#c1.depositar(300)
c1.sacar(1000)
print(c1.titular, c1.agencia, c1.numero, c1.saldo)
