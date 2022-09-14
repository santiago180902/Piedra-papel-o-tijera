# juguemos piedra papel o tijera


import random


#INPUT
user = random.randrange(1, 3)
Pc = ""
print("1.Piedra")
print("2.Papel")
print("3.Tijera")
opcion = int(input("Usted que elije: "))

#procesing
if opcion == 1:
    escogeUser = "Piedra"
elif opcion == 2:
    escogeUser = "Papel"
elif opcion == 3:
    escogeUser = "Tijera"
print("Tu elijes: ", escogeUser)

if user == 0:
    escogePc = "Piedra"
elif user == 1:
    escogePc = "Papel"
elif user == 2:
    escogePc = "Tijera"

print("La PC elijio: ", escogePc)
print("...")

#OUTPUT
if escogePc == "Piedra" and escogeUser == "papel":
    print("Ganaste, papel envulve piedra.")

elif escogePc == "Papel" and escogeUser == "tijera":
    print("Ganaste, Tijera corta papel.")

elif escogePc == "Tijera" and escogeUser == "piedra":
    print("Ganaste, Piedra pisa tijera.")

if escogePc == "Papel" and escogeUser == "piedra":
    print("Perdiste, papel envulve piedra.")

elif escogePc == "Tijera" and escogeUser == "papel":
    print("Perdiste, Tijera corta papel.")

elif escogePc == "Piedra" and escogeUser =="tijera":
    print("Perdiste, Piedra aplasta tijera.")

elif escogePc == escogeUser:
    print("Empate")


#Fin