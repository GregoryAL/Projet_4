from modele.ronde import Ronde
from modele.match import Match
from controleur.gestion_de_joueur import GestionDeJoueur


class TypeDeTournoi:
    """ Classe gérant les types de tournoi"""

    def __init__(self, objet_gestion_joueur):
        """ crée l'objet type de tournoi """
        self.objet_gestion_joueur = objet_gestion_joueur

    def choix_type_tournoi(self, type_de_tournoi, numero_de_ronde, instance_tournoi):
        if type_de_tournoi == "MethodeSuisse":
            return self.creation_des_matchs_methode_suisse(numero_de_ronde, instance_tournoi)
        else:
            print("Type de tournoi non pris en charge.")

    def creation_des_matchs_methode_suisse(self, numero_de_ronde, instance_tournoi):
        # Tri des joueurs
        if int(numero_de_ronde) == 1:
            instance_tournoi.participants = GestionDeJoueur.fonction_decorateurs_pour_tri_participants\
                (self.objet_gestion_joueur, instance_tournoi.participants, "classement_elo")
        elif int(numero_de_ronde) >= 2:
            instance_tournoi.participants = GestionDeJoueur.fonction_decorateurs_pour_tri_participants\
                (self.objet_gestion_joueur, instance_tournoi.participants, "points_tournoi")
        # Creation des paires
        moitie_des_participants = int(instance_tournoi.nombre_de_participants/2)
        ronde_actuelle = Ronde(nom=("round" + str(numero_de_ronde)))
        for i in range(moitie_des_participants):
            id_joueur_2 = moitie_des_participants + i
            match_pairing = Match(instance_tournoi.participants[i], instance_tournoi.participants[id_joueur_2])
            ronde_actuelle.liste_matchs.append(match_pairing)
            print("match entre " + instance_tournoi.participants[i][0].nom + " et " +
                  instance_tournoi.participants[id_joueur_2][0].nom)
        return ronde_actuelle
