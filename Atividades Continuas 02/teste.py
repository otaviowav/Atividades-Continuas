class Conta:
	def __init__(self, titular, agencia, numero, saldo_inicial):
            self.__titular = titular
            self.__agencia = agencia
            self.__numero = numero
            self.__saldo_inicial = saldo_inicial


if __name__ == '__main__':
    conta1 = Conta('João Medeiros', 234, 1)
		
	
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
		"""
		Implemente a property numero
		"""
		pass
	
	@property
	def saldo(self):
		"""
		Implemente a property saldo
		"""
		pass
	
	@property
	def ativa(self):
		"""
		Implemente a property ativa
		"""
		pass
	
	@ativa.setter
	def ativa(self, situacao):
		"""
		Implemente o setter ativa
		"""
		pass
	
	def depositar(self, valor):
		"""
		Implemente o método depositar()
		"""
		pass

	def sacar(self, valor):
		"""
		Implemente o método sacar()
		"""
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