from modele.ronde import Ronde
from modele.match import Match
from controleur.gestion_de_joueur import GestionDeJoueur
from vue.message_d_erreur import MessageDErreur


class TypeDeTournoi:
    """ Classe gérant les types de tournoi"""

    def __init__(self, objet_gestion_joueur, objet_message_d_erreur):
        """ Crée l'objet type de tournoi """
        self.objet_gestion_joueur = objet_gestion_joueur
        self.objet_message_d_erreur = objet_message_d_erreur

    def choix_type_tournoi(self, type_de_tournoi, numero_de_ronde, instance_tournoi):
        if type_de_tournoi == "MethodeSuisse":
            return self.creation_des_matchs_methode_suisse(numero_de_ronde, instance_tournoi)
        else:
            MessageDErreur.message_type_tournoi_non_pris_en_charge(self.objet_message_d_erreur)

    def creation_des_matchs_methode_suisse(self, numero_de_ronde, instance_tournoi):
        # Tri des joueurs
        if int(numero_de_ronde) == 1:
            instance_tournoi.participants = \
                GestionDeJoueur.fonction_decorateurs_pour_tri_participants(self.objet_gestion_joueur,
                                                                           instance_tournoi.participants,
                                                                           "classement_elo")
        elif int(numero_de_ronde) >= 2:
            instance_tournoi.participants = \
                GestionDeJoueur.fonction_decorateurs_pour_tri_participants(self.objet_gestion_joueur,
                                                                           instance_tournoi.participants,
                                                                           "points_tournoi")
        # Creation des paires
        moitie_des_participants = int(instance_tournoi.nombre_de_participants/2)
        ronde_actuelle = Ronde(nom=("round" + str(numero_de_ronde)))
        for i in range(moitie_des_participants):
            id_joueur_2 = moitie_des_participants + i
            match_pairing = Match(instance_tournoi.participants[i], instance_tournoi.participants[id_joueur_2])
            ronde_actuelle.liste_matchs.append(match_pairing)
        return ronde_actuelle
