mdp = input("Entrer le mdp : ")


falseMdp = "Mot de passe faible, ne répond pas aux exigences de la politique de mot de passe."
trueMdp = "Mot de passe fort, répond aux exigences de la politique de mot de passe."
list = ["!", "@", "#", "$", "%", "&"]

def CheckPassword (arg):
	if len(arg) >= 20 :
		for a in list:
			if a in arg:
				print(trueMdp)
				return
		print(falseMdp)
	else:
		print(falseMdp)

CheckPassword(mdp)



