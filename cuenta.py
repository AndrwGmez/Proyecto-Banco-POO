class Cuenta:

	TIPO_CUENTA = ("Ahorro" , "Corriente")


	def __init__(self, titular, id_titular, num_cuenta, saldo, fecha_actual, tipo_cuenta, cupo):

		self.__titular = titular
		self.__id_titular = id_titular
		self.__num_cuenta = num_cuenta
		self.__saldo = saldo
		self.__fecha_actual = fecha_actual
		self.__tipo_cuenta = self.validar_tipo_cuenta(tipo_cuenta)
		self.__cupo = cupo

	def validar_tipo_cuenta(self, tipo_cuenta):
		if tipo_cuenta in Cuenta.TIPO_CUENTA:
			return tipo_cuenta
		return Cuenta.TIPO_CUENTA[0]


	def set_titular(self, titular):
		self.__titular = titular

	def get_titular(self):
		return self.__titular




	def set_id_titular (self, id_titular):
		self.__id_titular = id_titular

	def get_id_titular(self):
		return self.__id_titular



		
	def set_numero_cuenta(self, num_cuenta):
		self.__num_cuenta = num_cuenta

	def get_numero_cuenta(self):
		return self.__num_cuenta




	def set_fecha(self, fecha_actual):
		self.__fecha_actual = fecha_actual

	def get_fecha(self):
		return self.__fecha_actual


	def set_saldo(self, saldo):
		self.__saldo = __saldo

	def get_saldo(self):
		return self.__saldo




	def set_tipo_cuenta(self, tipo_cuenta):
		self.__tipo_cuenta = self.validar_tipo_cuenta(tipo_cuenta)

	def get_tipo_cuenta(self):
		return self.__tipo_cuenta


	def visualizar(self):
		print("Tituar : %s" %(self.__titular))
		print("Id titular : %s" %(self.__id_titular))
		print("Numero cuenta : %s" %(self.__num_cuenta))
		print("Saldo : %s" %(self.__saldo))
		print("Fecha apertura : %s" %(self.__fecha_actual))
		print("Tipo de cuenta : %s" %(self.__tipo_cuenta))
		print("Cupo de la Cuenta : %s" %(self.__cupo))


	def retirar(self,monto):
		if self.__tipo_cuenta == Cuenta.TIPO_CUENTA[0]:
			if  self.__saldo - monto <= 10000:
				self.__saldo -= monto
				return True
			else:
				return False


		elif self.__tipo_cuenta == Cuenta.TIPO_CUENTA[1]:
			if (self.__cupo + self.__saldo) - monto >= 0:
				if self.__saldo - monto <= 0:
					self.__cupo = self.__cupo +  (self.__saldo - monto)
					self.__saldo = 0
					return True
			return False



	def depositar(self, monto):
		if monto > 0:
			self.__saldo += monto
			return True
		return False


	def consultar(self):
		return self.__saldo


	def mstrar(self):
		return self.__titular
