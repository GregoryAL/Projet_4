"""Entry point."""
from controleur.run import Controleur
from vue.vue import Vue


if __name__ == "__main__":
    """ début du programme """
    # Creation de l'objet Controleur
    controleur_du_tournoi = Controleur()
    # Lancement du programme
    controleur_du_tournoi.execute()
