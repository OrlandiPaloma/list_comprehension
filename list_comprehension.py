#Utilizando LIST COMPREHENSION
#Y=[VALOR A ADICIONAR   LAÇO   CONDIÇÃO]

x=[1,2,3,4,5]
y=[i**2 for i in x]

print("Usando list comprehension)")
print(x)
print(y)
print("\n")

#exemplo para que a lista Z mostre somente os numeros impares da lista x:

x=[1,2,3,4,5]
z=[i for i in x if i%2==1]

print("Mostrando somente numero impares")
print(x)
print(z)
print("\n")

#exemplo para que a listaW mostre somente os numeros pares da lista 1:

lista1 = [1,2,3,4,5,6,7,8,9,10]
listaw=[i for i in lista1 if i%2==0]
print("mostrando somente numeros pares")
print(lista1)
print(listaw)
