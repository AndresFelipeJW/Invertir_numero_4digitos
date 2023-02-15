#Programa para invertir numeros de 4 digitos

print("--------------------------------")
print("---- NUMERO PARA INVERITR  -----")
print("--------------------------------")

#input
n = int(input("digite el NUMERO DE 4 DIGITOS PARA INVERTIR: "))


#processing

ni = ((n%10)*1000) + ((n//10)*1)


# output
print("-----------------------------")
print("--------- RESUTADOS ---------")
print("-----------------------------")

print(" REULTADO INVERSO:" + str(ni))

