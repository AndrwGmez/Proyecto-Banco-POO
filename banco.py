import random 
from os import system 
from datetime import datetime 
from cuenta import Cuenta


class Banco:

	def __init__(self):
		self.__cuentas = []
		self.__numeros_cuenta = []


	def generar_numero_cuenta(self):
		while True: 
			numero = random.randint(1, 9)
			if numero not in self.__numeros_cuenta:
				self.__numeros_cuenta.append(numero)
				break
		return numero	


	def buscar_cuenta(self, numero_cuenta):
		for i in range (len(self.__cuentas)):
			if numero_cuenta == self.__cuentas[i].get_numero_cuenta():
				return i 
		return -1


	def adicionar_cuenta(self, cuenta):
		pos = self.buscar_cuenta(cuenta.get_numero_cuenta())
		if pos == -1:
			self.__cuentas.append(cuenta)
			return True 
		return False 



	def visualizar_cuenta(self, num_cuenta):
		pos = self.buscar_cuenta(num_cuenta)
		if pos != -1:
			self.__cuentas[pos].visualizar()
			return True
		return False



	def retirar_monto_cuenta(self, monto, num_cuenta):
		pos = self.buscar_cuenta(num_cuenta)
		if pos != -1:
			if self.__cuentas[pos].retirar(monto):
				return True
		return False



	def depositar_monto_cuenta(self, monto, num_cuenta):
		pos = self.buscar_cuenta(num_cuenta)
		if pos != -1:
			if self.__cuentas[pos].depositar(monto):
				return True
		return False


	def consultar_saldo_cuenta(self, num_cuenta):
		pos = self.buscar_cuenta(num_cuenta)
		saldo = -1
		if pos != -1:
			saldo = self.__cuentas[pos].consultar()
			return saldo

	
	def mostrar_titular_cuenta(self, id_titular):
		pss = self.buscar_cuenta(id_titular)
		sc = -1
		if pss != -1:
			sc = self.__cuentas[pss].mstrar()
			return sc 



	def pedir_datos_cuenta(self):
		try:
			system("clear")
			print("***********************")
			print("    ADICIONAR SOCIO    ")
			print("***********************")
			print()

			titular = input("Ingrese el nombre del titular : ")
			id_titular = int(input("Ingrese el numero de indentificion del titular : "))
			num_cuenta = self.generar_numero_cuenta()
			saldo = int(input("Digite el saldo inicial de la cuenta : "))
			fecha_actual = datetime.now()
			print()

			while True:
				print("***********************")
				print("    Tipos De Cuenta    ")
				print("***********************")
				print()
				print(" 1 = Ahorros")
				print("***********************")
				print(" 2 = Corriente")
				print()


				try:
					op_tipo_cuenta = int(input("Ingrese La Opcion A Utilizar : "))

					if op_tipo_cuenta == 1:
						tipo_cuenta = "Ahorro"
						cupo = 0 
						break 

					elif op_tipo_cuenta == 2:
						tipo_cuenta = "Corriente"



						try:
							cupo = float(input("Digite el cupo asignado para la cuenta : "))
							break


						except ValueError:
							print("***********************")
							print("Error - El cupo debe ser una cantidad numerica")
							print("***********************")
							input()



					else:
						print("***********************")
						print("Error - La Opcion no correcta, ingrese 1 ó 2")
						print("***********************")
						input()


				except ValueError:
					print("***********************")
					print("Error - Solo valores numericos")
					print("***********************")
					input()


			cuenta = Cuenta(titular, id_titular, num_cuenta, saldo, fecha_actual, tipo_cuenta, cupo)
			self.adicionar_cuenta(cuenta)
			print()
			print("***********************")
			print("La cuenta se creo correctamente")
			print("Su numero de cuenta es : %d "% num_cuenta)
			print("***********************")
			input()


		except ValueError:
			print("***********************")
			print("Error - Ingrese un valor numerico")
			print("***********************")
			input()


	def pedir_datos_visualizar_cuenta(self):

		try:
			system("clear")
			print("***********************")
			print("    VISUALIZAR CUENTA    ")
			print("***********************")
			print()
			num_cuenta = int(input("Ingrese el numero de la cuenta : "))
			if self.buscar_cuenta(num_cuenta) != -1:
				self.visualizar_cuenta(num_cuenta)
				input()
				print()
			
			else:			
				print()
				print("***********************")
				print("    Error - No se encuentra el numero de cuenta    ")
				print("***********************")
				print()
				input()


		except ValueError:
				print("***********************")
				print("Error Solo Valores Numericos enteros")
				print("***********************")
				input()




	def pedir_datos_retiro_cuenta(self):
		try:
			system("clear")
			print("***********************")
			print("    RETIRO CUENTA    ")
			print("***********************")
			num_cuenta = int(input("Digite el numero de cuenta : "))

			if self.buscar_cuenta(num_cuenta) != -1:
				monto = float(input("Ingrese la cantidad de dinero, a retirar de la cuenta : "))


				if self.retirar_monto_cuenta(monto, num_cuenta):
					print("***********************")
					print("    ¡El retiro se realizo correctamente!  ")
					print("***********************")
					print()
					input()

				else:			
					print()
					print("***********************")
					print("   ¡El retiro NO se realizo correctamente! ")
					print("***********************")
					print()
					input()

			else:			
					print()
					print("***********************")
					print("   El numero de cuenta ingresado no existe ")
					print("***********************")
					print()
					input()

		except ValueError:
			print("***********************")
			print("    Error - El valor del monto debe ser numerico")
			print("***********************")
			input()


	def pedir_datos_deposito_cuenta(self):
		try:
			system("clear")
			print("***********************")
			print("    DEPOSITO CUENTA    ")
			print("***********************")
			num_cuenta = int(input("Digite el numero de cuenta : "))

			if self.buscar_cuenta(num_cuenta) != -1:
				monto = float(input("Ingrese la cantidad de dinero a depositar en la cuenta : "))

				if self.depositar_monto_cuenta(monto, num_cuenta):
					print("***********************")
					print(" ¡El deposito se realizo correctamente¡")
					print("***********************")
					input()

	
				else:
					print("***********************")
					print("El deposito No se realizo correctamente")
					print("***********************")
					input()


		except ValueError:
				print("***********************")
				print("El valor debe ser un valor numerico")
				print("***********************")
				input()



	def mostrar_saldo_cuenta(self):
		try:
			system("clear")
			print("***********************")
			print("    SALDO CUENTA    ")
			print("***********************")
			num_cuenta = int(input("Digite el numero de cuenta : "))


			if self.buscar_cuenta(num_cuenta) != -1:
				print("***********************")
				print("El saldo de la cuenta es : $%2f" %(self.consultar_saldo_cuenta(num_cuenta)))
				print("***********************")
				input()

			else:
				print("***********************")
				print("El valor debe ser un valor numerico")
				print("***********************")
				input()


		except ValueError:
				print("***********************")
				print("El valor debe ser un valor numerico")
				print("***********************")
				input()


	def mostrar_id_titular_cuentar(self):
		try:
			system("clear")
			print("***********************")
			print("    MOSTRAR CLIENTE    ")
			print("***********************")
			id_titular = int(input("Digite el numero de cuenta : "))


			if self.buscar_cuenta(id_titular) != -1:
				print("***********************")
				print("El nombre del titular es : %s" %(self.mostrar_titular_cuenta(id_titular)))
				input()



			else:
				print("***********************")
				print("El titular no existe, no se encuentro")	
				print("***********************")                                                                          
				input()


		except ValueError:
				print("***********************")
				print("El valor debe ser un valor numerico")
				print("***********************")
				input()


	def mostrar_menu_principal(self):
		while True:
			system("clear")
			print("***********************")
			print("     BANCO ADSO        ")
			print("***********************")
			print("***********************")
			print("***********************")
			print("     Menu Principal    ")
			print("***********************")
			print("***********************")
			print("***********************")
			print("    1 = Crear Cuenta   ")
			print("***********************")
			print("    2 = Visualizar Cuenta ")
			print("***********************")
			print("    3 = Retiro de cuenta ")
			print("***********************")
			print("    4 = Depositar de cuenta ")
			print("***********************")
			print("    5 = Consultar de cuenta ")
			print("***********************")
			print("    6 = Consultar nombre de titular ")
			print("***********************")
			print("    10 = Salir         ")
			print("***********************")
			print()
			try:
				print()
				print("***********************")
				op = int(input("Ingrese La Opcion A Utilizar : "))
				print("Hasta Luego")

				if op == 1:
					self.pedir_datos_cuenta()


				elif op == 2:
					self.pedir_datos_visualizar_cuenta()



				elif op == 3:
					self.pedir_datos_retiro_cuenta()



				elif op == 4:
					self.pedir_datos_deposito_cuenta()



				elif op == 5:
					self.mostrar_saldo_cuenta()


				elif op == 6:
					self.mostrar_id_titular_cuentar()



				elif op == 10:
					break

				else:
					print("***********************")
					print ("Error")
					print("***********************")



			except ValueError:
				print("***********************")
				print("Error Solo Valores Numericos")
				print("***********************")


if __name__ == '__main__':
	banco = Banco()
	banco.mostrar_menu_principal()




# get return 
# set asignar 

