"""Entry point."""
from controleur import run
from modele import joueurs
from modele import ronde
from vue import output


if __name__ == "__main__":
    """ début du programme """
    information_du_tournoi = output.Vue()
    information_du_tournoi = output.Vue.creation_du_tournoi(information_du_tournoi)
    print(information_du_tournoi)
    gestion_du_tournoi = run.Controleur()
    instance_du_tournoi = run.Controleur.creation_du_tournoi(gestion_du_tournoi, information_du_tournoi)
    # ajout de la liste des joueurs dans l'objet de tournoi instancié
    instance_du_tournoi.participants = run.Controleur.ajout_des_joueurs(gestion_du_tournoi)
    # Boucle le déroulement d'une ronde X fois, X étant le nombre de ronde déterminé à la création du tournoi
    print(instance_du_tournoi.nombre_de_tour_du_tournoi)
    for numero_de_ronde in range(instance_du_tournoi.nombre_de_tour_du_tournoi):
        ronde_actuelle = run.Controleur.deroulement_d_une_ronde(gestion_du_tournoi, numero_de_ronde,
                                                                instance_du_tournoi.participants)
        instance_du_tournoi.rondes.append(ronde_actuelle)
        print(ronde.Ronde.__str__(ronde_actuelle))
        print(joueurs.Joueur.__str__(instance_du_tournoi.participants[0]))
    print("le vainqueur est ")
    joueurs.Joueur.__str__(instance_du_tournoi.participants[1])
    # print(ronde.Ronde.__str__(instance_du_tournoi))"""
