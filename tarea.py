#Ejercicio 1
def lista_sin_repetidos(lst):
    if len(lst) == len(set(lst)):
        print("no hay elementos repetidos")
    else:
        print("si hay elementos repetidos")

lista = [1, 2, 3, 2, 5]

print(f"Lista {lista}: ", end="")
lista_sin_repetidos(lista)

#Ejercicio 2
def encontrar_palindromos(lst):
    palindromos = [item for item in lst if isinstance(item, str) and item == item[::-1]]
    if palindromos:
        print("Palíndromos encontrados:", ", ".join(palindromos))
    else:
        print("No existe")

lista_palindromos = ["casa", "radar", "perro", "oso"]
encontrar_palindromos(lista_palindromos)

#Ejercicio 3
def encontrar_cadenas_vocales(lst):
    vocales = set("aeiouAEIOU")
    cadenas_con_vocales = [item for item in lst if isinstance(item, str) and sum(1 for char in item if char in vocales) >= 2]

    if cadenas_con_vocales:
        print("Cadena con dos o mas vocales:", ", ".join(cadenas_con_vocales))
    else:
        print("No existe")

lista = ["queso", "hambre", "pollo", "gris", "verde"]
encontrar_cadenas_vocales(lista)

#Ejercicio 4
def es_lista_palindromo(lst):
    if lst == lst[::-1]:
        print("La lista es un palíndromo.")
    else:
        print("La lista no es un palíndromo.")

lista1 = [1, 2, 3, 2, 1]
lista2 = [1, 2, 3, 4, 5]
lista3 = ["a", "b", "c", "b", "a"]
lista4 = ["r", "o", "j", "o", "s"]

print("\nLista 1:")
es_lista_palindromo(lista1)
print("\nLista 2:")
es_lista_palindromo(lista2)
print("\nLista 3:")
es_lista_palindromo(lista3)
print("\nLista 4:")
es_lista_palindromo(lista4)
## Ejercicios adicionales
## Ejercicio 1. Determinar si una lista tiene exactamente un solo elemento repetido
from collections import Counter

def repetido(lista):
    conteo = Counter(lista)
    repetidos = sum(1 for v in conteo.values() if v > 1)
    return repetidos == 1

lista = [1, 2, 3, 4, 2]
print(repetido(lista))

lista = [1, 2, 3, 4, 5]
print(repetido(lista))
#Ejercicio 2  Buscar la cadena más corta en una lista y verificar si es palíndromo
def palindromo(s):
    return s == s[::-1]

def cadena(lista):
    if not lista:
        return "Lista vacía"

    corta = min(lista, key=len)
    return corta if palindromo(corta) else " la palabra mas corta no es palíndromo"

lista = ["hola", "oso", "sol", "radar"]
print(cadena(lista))
#Ejercicio 3  Determinar si en una lista existe una cadena con tres o más consonantes seguidas
import re

def consonantes(lista):
    patron = r"[bcdfghjklmnpqrstvwxyz]{3,}"
    for palabra in lista:
        if re.search(patron, palabra, re.IGNORECASE):
            return palabra
    return "No existe"

lista = ["programacion", "abstracto", "paliza", "cancion"]
print(consonantes(lista))
#Ejercicio 4 Determinar si una lista sigue un patrón de espejo parcial
def espejo(lista):
    n = len(lista)
    mitad = n // 2
    return lista[:mitad] == lista[-mitad:][::-1]

lista1 = [1, 2, 3, 3, 2, 1]
lista2 = [1, 2, 3, 1, 2, 3]
print(espejo(lista1))
print(espejo(lista2))