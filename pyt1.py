#!/usr/bin/env python3

def is_palindrom(a):
	for i in range(len(a)//2):
		if a[i] != a[-i-1]:
			return False
	return True

a = input("entrer un mot: ")

if is_palindrom(a) == True:
	print("Ce mot est un palindrome.")
else:
     print("Ce mot n'est pas un palindrome.")
