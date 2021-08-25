class Conta:
    def __init__(self, titular, agencia, numero, saldo_inicial):
        self.__titular = titular
        self.__agencia = agencia
        self.__numero = numero
        self.__saldo_inicial = saldo_inicial

    @property
    def titular(self):
        """
        Implemente a property titular
        """
        pass

    @property
    def agencia(self):
        """
        Implemente a property agencia
        """
        pass

    @property
    def numero(self):
        return self.numero
        pass

    @property
    def saldo(self):
        return self.__saldo_inicial
        pass

    @property
    def ativa(self):
        self.ativa = False

        pass

    @ativa.setter
    def ativa(self, situacao):
        """
        Implemente o setter ativa
        """
        pass

    def depositar(self, valor):
        self.__saldo_inicial += valor
        pass

    def sacar(self, valor):
        self.__saldo_inicial -= valor
        pass

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
