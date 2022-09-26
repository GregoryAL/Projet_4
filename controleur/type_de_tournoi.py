from modele import ronde
import datetime
from modele.match import Match



class TypeDeTournoi:
    """ Classe gérant les types de tournoi"""

    def __init__(self):
        """ crée l'objet type de tournoi """


    def choix_type_tournoi(self, type_de_tournoi, numero_de_ronde, instance_tournoi):
        if type_de_tournoi == "MethodeSuisse":
            return self.creation_des_matchs_methode_suisse(numero_de_ronde, instance_tournoi)
        else:
            print("Type de tournoi non pris en charge.")

    def creation_des_matchs_methode_suisse(self, numero_de_ronde, instance_tournoi):
        # Tri des joueurs
        print("numero de ronde " + str(numero_de_ronde))
        if numero_de_ronde == 1:
            instance_tournoi.participants.sort(key=lambda x: x.classement_elo, reverse=True)
        elif numero_de_ronde > 1:
            instance_tournoi.participants.sort(key=lambda x: x.points_tournoi, reverse=True)
        # Creation des paires
        moitie_des_participants = int(instance_tournoi.nombre_de_participants/2)
        ronde_actuelle = ronde.Ronde("round" + str(numero_de_ronde), datetime.datetime.now())
        for i in range(moitie_des_participants):
            id_joueur_2 = moitie_des_participants + i
            match_pairing = Match(instance_tournoi.participants[i],instance_tournoi.participants[id_joueur_2])
            ronde_actuelle.liste_matchs.append(match_pairing)
            print(ronde_actuelle.liste_matchs)
        return ronde_actuelle
