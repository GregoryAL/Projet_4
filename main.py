"""Entry point."""
from controleur.run import Controleur
from modele.joueurs import Joueur
from modele.ronde import Ronde
from vue.vue import Vue


if __name__ == "__main__":
    """ début du programme """
    vue_du_tournoi = Vue()
    controleur_du_tournoi = Controleur()
    information_du_tournoi = Vue.recuperation_des_informations_du_tournoi(vue_du_tournoi)
    print(information_du_tournoi)
    information_des_joueur = Vue.recuperation_des_informations_des_joueurs(vue_du_tournoi)
    print(information_des_joueur)

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
