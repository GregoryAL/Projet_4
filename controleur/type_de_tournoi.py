from modele import joueurs
from modele import ronde
import datetime
from modele import match
from modele import tournoi



class TypeDeTournoi:
    """ Classe gérant les types de tournoi"""

    def __init__(self, type_de_tournoi, numero_de_ronde, instance_tournoi):
        self.type_de_tournoi = type_de_tournoi
        self.numero_de_ronde = numero_de_ronde
        self.instance_tournoi = instance_tournoi

    def creation_des_matchs_methode_suisse(self):
        # Tri des joueurs
        print("numero de ronde " + str(self.numero_de_ronde))
        if self.numero_de_ronde == 1:
            self.instance_tournoi.participants.sort(key=lambda x: x.classement_elo, reverse=True)
            print("le classement est : ")
            for joueur in self.instance_tournoi.participants:
                print(joueurs.Joueur.__str__(joueur))
        elif self.numero_de_ronde > 1:
            self.instance_tournoi.participants.sort(key=lambda x: x.points_tournoi, reverse=True)
            print("le classement est : ")
            for joueur in self.instance_tournoi.participants:
                print(joueurs.Joueur.__str__(joueur))
        # Creation des paires
        print("le nombre de participants est " + str(self.instance_tournoi.nombre_de_participants))
        moitie_des_participants = int(self.instance_tournoi.nombre_de_participants/2)
        print("la moitié des participants est " + str(moitie_des_participants))
        ronde_actuelle = ronde.Ronde("round" + str(self.numero_de_ronde), datetime.datetime.now())
        for i in range(moitie_des_participants):
            print("i est " + str(i) + " et le joueur est " + self.instance_tournoi.participants[i].nom)
            id_joueur_2 = moitie_des_participants + i
            print("id joueur2 est " + str(id_joueur_2) + " et le joueur est " +
                  self.instance_tournoi.participants[id_joueur_2].nom)
            match_pairing = match.Match(self.instance_tournoi.participants[i],
                                        self.instance_tournoi.participants[id_joueur_2])
            ronde_actuelle.liste_matchs["Match"+str(i+1)] = match_pairing
            print(ronde_actuelle.liste_matchs)
        return ronde_actuelle
