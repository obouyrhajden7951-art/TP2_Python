# Créer une classe CompteBancaire avec deux attributs : _titulaire (protégé), __solde (privé).
# Ajouter des méthodes deposer(montant) et retirer(montant) avec vérification de validité.
# Utiliser @property pour exposer solde en lecture seule.
# Empêcher toute modification directe du solde depuis l’extérieur.
class CompteBancaire:

    # Initialiser le compte bancaire
    def __init__(self, titulaire, solde_initial=0):
        self._titulaire = titulaire
        self.__solde = solde_initial

    # Ajouter de l'argent au compte
    def deposer(self, montant):
        if montant > 0:
            self.__solde += montant
        else:
            print("Montant invalide.")

    # Retirer de l'argent du compte
    def retirer(self, montant):
        if 0 < montant <= self.__solde:
            self.__solde -= montant
        else:
            print("Fonds insuffisants ou montant invalide.")

    # Accéder au solde sans pouvoir le modifier directement
    @property
    def solde(self):
        return self.__solde

    # Afficher les informations du compte
    def __str__(self):
        return f"Titulaire : {self._titulaire}, Solde : {self.solde} €"


# Tester la classe
if __name__ == "__main__":

    # Créer un compte bancaire
    compte = CompteBancaire("Ali", 1000)

    # Effectuer les opérations
    compte.deposer(200)
    compte.retirer(150)

    # Afficher les informations
    print(compte)
    print("Solde accessible (lecture) :", compte.solde)

    # Tentative de modification directe du solde
    compte.solde = 500

    # Résultat attendu

# Titulaire : Ali, Solde : 1050 €
# Solde accessible (lecture) : 1050
# Traceback (most recent call last): ...
# AttributeError: can't set attribute 'solde'