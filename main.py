"""Point d"entrée. """
from controleur.run import Controleur


if __name__ == "__main__":
    """ début du programme """
    # Creation de l'objet Controleur
    controleur_du_tournoi = Controleur()
    # Lancement du programme
    Controleur.execute(controleur_du_tournoi)
