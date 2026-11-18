# Créer CompteBancaire avec les méthodes deposer, retirer, get_solde, avec encapsulation du solde.
# Créer Client avec nom et une instance de CompteBancaire.
# Implémenter afficher() dans Client pour afficher son nom et le solde de son compte.

class CompteBancaire:
    # Initialiser le compte avec un solde
    def __init__(self, solde_initial=0.0):
        self.__solde = solde_initial

    # Déposer de l'argent
    def deposer(self, montant):
        if montant > 0:
            self.__solde += montant

    # Retirer de l'argent
    def retirer(self, montant):
        if 0 < montant <= self.__solde:
            self.__solde -= montant

    # Retourner le solde du compte
    def get_solde(self):
        return self.__solde


class Client:

    # Initialiser le client
    def __init__(self, nom):
        self.nom = nom

        # Créer un compte bancaire pour le client
        self.compte = CompteBancaire()

    # Afficher le nom et le solde du client
    def afficher(self):
        print(f"Client : {self.nom}, Solde : {self.compte.get_solde()}€")


# Créer un client
cli = Client("Yassir")

# Effectuer des opérations sur son compte
cli.compte.deposer(300)
cli.compte.retirer(50)

# Afficher les informations
cli.afficher()

# Résultat attendu :  Client : Yassir, Solde : 250.0€