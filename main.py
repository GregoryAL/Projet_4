"""Entry point."""
import sys

from controleur.run import Controleur
from modele.joueurs import Joueur
from modele.ronde import Ronde
from vue.vue import Vue


if __name__ == "__main__":
    """ début du programme """
    # Creation de l'objet Vue du tournoi
    vue_du_tournoi = Vue()
    # Creation de l'objet Controleur
    controleur_du_tournoi = Controleur()
    # Affichage du menu
    while Controleur.affichage_du_menu(controleur_du_tournoi) != 5:
        instance_de_tournoi = Controleur.affichage_du_menu(controleur_du_tournoi)
    # Sortie du programme à la demande de l'utilisateur (choix sortie dans la boucle)
    sys.exit("Vous quittez la gestion du tournoi")


"""gestion_du_tournoi = Controleur()
    instance_du_tournoi = Controleur.creation_du_tournoi(gestion_du_tournoi, information_du_tournoi)
    # ajout de la liste des joueurs dans l'objet de tournoi instancié
    instance_du_tournoi.participants = Controleur.ajout_des_joueurs(gestion_du_tournoi)
    # Boucle le déroulement d'une ronde X fois, X étant le nombre de ronde déterminé à la création du tournoi
    print(instance_du_tournoi.nombre_de_tour_du_tournoi)
    for numero_de_ronde in range(instance_du_tournoi.nombre_de_tour_du_tournoi):
        ronde_actuelle = Controleur.deroulement_d_une_ronde(gestion_du_tournoi, numero_de_ronde,
                                                                instance_du_tournoi.participants)
        instance_du_tournoi.rondes.append(ronde_actuelle)
        print(Ronde.__str__(ronde_actuelle))
        # print(joueurs.Joueur.__str__(instance_du_tournoi.participants[0]))
    print("le vainqueur est " + Joueur.__str__(instance_du_tournoi.participants[0]))
    # print(ronde.Ronde.__str__(instance_du_tournoi))"""
