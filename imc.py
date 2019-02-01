#IMC - Primer programa en Python

#Muestra y captura los siguientes datos, kg - m

medida=float(input("Cual es tu medida en metros?: "))
peso=float(input("Cual es tu peso en kilogramos?: "))

#Calcula el IMC
imc=peso/(medida**2)
print("Tu IMC es", round(imc,1))
