def generaPares(limite):
	num=1
	miLista=[]

	while num<limite:

		miLista.append(num*2)
		num=num+1

	return miLista	

print(generaPares(10))

#Generador no necesita lista porque generaelementos iterables

def generaPares(limite):
	num=1

	while num<limite:

		yield num*2 #Devuelve esto
		num=num+1

#Objeto iterable
#Entre llamada y llamada entra en estado de suspension para ahorrar recursos
devuelvePares=generaPares(10)


print(next(devuelvePares))
print("Aqui podria ir mas codigo....")
print(next(devuelvePares))