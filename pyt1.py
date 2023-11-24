#!/usr/bin/env python3

#fonction qui prend en argument une chaine de caractere et qui verifie si le mot est un palindrome en retournant un boolen
def is_palindrom(a):
	for i in range(len(a)//2):
		if a[i] != a[-i-1]:
			return False
	return True

car = {
        "à" : "a",
        "ä" : "a",
        "â" : "a",
        "ç" : "c",
        "é" : "e",
        "è" : "e",
        "ë" : "e",
        "ï" : "i",
        "ô" : "o",
        "ù" : "u",
        "ü" : "u",
        "û" : "u",
        " " : "",
        "-" : "",
        "," : "",
        "'" : "",
        "?" : "",
        "!" : "",
        "." : ""
    }
# Remplacer des caractères par d'autres
def moulinette(a):
    a = a.lower()
    for cle,valeur in car.items():
        a = a.replace(cle,valeur)
    return a

#Entrer de la chaine de caractere a traiter
a = moulinette(input("entrer un mot: "))

#Condition en utilisant la fonction de reconaissance 
if is_palindrom(a) == True:
	print("Ce mot est un palindrome.")
else:
     print("Ce mot n'est pas un palindrome.")

