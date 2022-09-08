"""Entry point."""
from modele import tournoi
from modele import joueurs
from controleur import run


if __name__ == "__main__":
    """ début du programme """
    """ donnée du tournoi statique"""
    tournoi_de_test_statique = tournoi.Tournoi("tournoi de test", "lieu de test", "01/01/22", "blitz", 8)

    # Ajout des 8 joueurs

    player1 = joueurs.Joueur("Nom1", "prénom1", "11/11/11", "M", 1650)
    player2 = joueurs.Joueur("Nom2", "prénom2", "10/10/10", "F", 1435)
    player3 = joueurs.Joueur("Nom3", "prénom3", "9/9/9", "U", 1983)
    player4 = joueurs.Joueur("Nom4", "prénom4", "08/08/08", "M", 1945)
    player5 = joueurs.Joueur("Nom5", "prénom5", "04/05/06", "F", 1345)
    player6 = joueurs.Joueur("Nom6", "prénom6", "11/5/11", "M", 1580)
    player7 = joueurs.Joueur("Nom7", "prénom7", "10/9/10", "F", 1415)
    player8 = joueurs.Joueur("Nom8", "prénom8", "9/4/9", "U", 1953)

    liste_participant = [player1, player2, player3, player4, player5, player6, player7, player8]
    instance_tournoi = run.TournoiSuisse(1, liste_participant)
    ronde1 = run.TournoiSuisse.appairage_des_joueurs(instance_tournoi)
    for match in ronde1.liste_matchs:
        print(match.joueur1.nom+" affronte "+match.joueur2.nom)





