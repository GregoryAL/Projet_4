"""Entry point."""
from controleur import run


if __name__ == "__main__":
    """ début du programme """
    gestion_du_tournoi = run.Controleur()
    instance_du_tournoi = run.Controleur.creation_du_tournoi(
        gestion_du_tournoi)
    # ajout de la liste des joueurs dans l'objet de tournoi instancié
    instance_du_tournoi.participants = run.Controleur.ajout_des_joueurs(
        gestion_du_tournoi)
    # Boucle le déroulement d'une ronde X fois, X étant le nombre de ronde
    # déterminé à la création du tournoi
    print(instance_du_tournoi.nombre_de_tour_du_tournoi)
    for numero_de_ronde in range(
            instance_du_tournoi.nombre_de_tour_du_tournoi):
        ronde_actuelle = run.Controleur.deroulement_d_une_ronde(
            gestion_du_tournoi, numero_de_ronde,
            instance_du_tournoi.participants)
        instance_du_tournoi.rondes.append(ronde_actuelle)
        print(instance_du_tournoi.rondes.__repr__())
    print("le vainqueur est " + instance_du_tournoi.participants[0].prenom
          + " " + instance_du_tournoi.participants[0].nom)
    print(instance_du_tournoi.rondes.__repr__())
