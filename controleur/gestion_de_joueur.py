from modele.joueur import Joueur
from vue.vue import Vue
from vue.message_d_erreur import MessageDErreur
from vue.saisie_de_donnees import SaisieDeDonnees


class GestionDeJoueur:
    """ Classe gérant les joueurs"""

    def __init__(self, vue_instance, vue_message_d_erreur, vue_saisie_de_donnees):
        """ crée l'objet type de joueur """
        self.vue_instance = vue_instance
        self.vue_message_d_erreur = vue_message_d_erreur
        self.vue_saisie_de_donnees = vue_saisie_de_donnees

    def selection_d_un_joueur_a_modifier(self):
        choix_du_joueur_a_modifier = SaisieDeDonnees.selection_joueur_a_modifier(self.vue_saisie_de_donnees)
        return choix_du_joueur_a_modifier

    def selection_d_un_joueur_a_modifier_dict(self):
        choix_du_joueur_a_modifier = int(SaisieDeDonnees.selection_joueur_a_modifier(self.vue_saisie_de_donnees))
        return choix_du_joueur_a_modifier

    def modification_d_un_joueur(self, participants):
        try:
            indice_joueur_a_modifier = int(self.selection_d_un_joueur_a_modifier())-1
        except TypeError:
            MessageDErreur.message_d_erreur_d_input_chiffre(self.vue_message_d_erreur)
        # change le classement tournoi
        participants[indice_joueur_a_modifier].points_tournoi = \
            int(SaisieDeDonnees.modification_point_tournoi(self.vue_saisie_de_donnees, participants[indice_joueur_a_modifier]))
        return participants

    def modification_d_un_joueur_dict(self, liste_joueurs):
        """ Modifie les points elo d'un joueur de la liste"""
        indice_joueur_a_modifier = int(self.selection_d_un_joueur_a_modifier_dict())
        if indice_joueur_a_modifier <= 9:
            cle_joueur_a_modifier = "player0" + str(indice_joueur_a_modifier)
        else:
            cle_joueur_a_modifier = "player" + str(indice_joueur_a_modifier)
        # change le classement elo
        liste_joueurs[cle_joueur_a_modifier].classement_elo = \
            int(SaisieDeDonnees.modification_classement_elo(self.vue_saisie_de_donnees, liste_joueurs[cle_joueur_a_modifier]))
        return liste_joueurs

    def ajout_des_joueurs(self):
        """ Ajout des joueurs """
        # Pool de 28 joueurs statiques
        liste_joueurs = {"player01": Joueur("Nom01", "prénom01", "11/11/11", "M", 1650),
                         "player02": Joueur("Nom02", "prénom02", "10/10/10", "F", 1435),
                         "player03": Joueur("Nom03", "prénom03", "9/9/9", "U", 1983),
                         "player04": Joueur("Nom04", "prénom04", "08/08/08", "M", 1945),
                         "player05": Joueur("Nom05", "prénom05", "04/05/06", "F", 1345),
                         "player06": Joueur("Nom06", "prénom06", "11/5/11", "M", 1580),
                         "player07": Joueur("Nom07", "prénom07", "10/9/10", "F", 1415),
                         "player17": Joueur("Nom17", "prénom17", "10/9/10", "F", 1615),
                         "player18": Joueur("Nom18", "prénom18", "9/4/9", "U", 1153),
                         "player19": Joueur("Nom19", "prénom19", "11/11/11", "M", 1258),
                         "player20": Joueur("Nom20", "prénom20", "10/10/10", "F", 1338),
                         "player21": Joueur("Nom21", "prénom21", "11/11/11", "M", 1250),
                         "player22": Joueur("Nom22", "prénom22", "10/10/10", "F", 1335),
                         "player08": Joueur("Nom08", "prénom08", "9/4/9", "U", 1953),
                         "player09": Joueur("Nom09", "prénom09", "11/11/11", "M", 1454),
                         "player10": Joueur("Nom10", "prénom10", "10/10/10", "F", 1536),
                         "player11": Joueur("Nom11", "prénom11", "11/11/11", "M", 1450),
                         "player12": Joueur("Nom12", "prénom12", "10/10/10", "F", 1535),
                         "player13": Joueur("Nom13", "prénom13", "9/9/9", "U", 1783),
                         "player14": Joueur("Nom14", "prénom14", "08/08/08", "M", 1245),
                         "player15": Joueur("Nom15", "prénom15", "04/05/06", "F", 1545),
                         "player16": Joueur("Nom16", "prénom16", "11/5/11", "M", 1380),
                         "player23": Joueur("Nom23", "prénom23", "9/9/9", "U", 1483),
                         "player24": Joueur("Nom24", "prénom24", "08/08/08", "M", 1545),
                         "player25": Joueur("Nom25", "prénom25", "04/05/06", "F", 1645),
                         "player26": Joueur("Nom26", "prénom26", "11/5/11", "M", 1780),
                         "player27": Joueur("Nom27", "prénom27", "10/9/10", "F", 1815),
                         "player28": Joueur("Nom28", "prénom28", "9/4/9", "U", 1053)}
        return liste_joueurs

    def classement_des_joueurs(self, liste_participant, facteur_tri):
        """ Classe les joueurs en fonction de leur classement elo pour la première ronde, ou par leur classement
        tournoi pour les rondes suivantes."""
        if facteur_tri == "classement_elo":
            liste_participant.sort(key=lambda x: x.classement_elo, reverse=True)
        elif facteur_tri == "points_tournoi":
            liste_participant.sort(key=lambda x: (x.points_tournoi, x.classement_elo), reverse=True)
        elif facteur_tri == "nom":
            liste_participant.sort(key=lambda x: x.nom, reverse=False)
        return liste_participant

    def creation_d_un_joueur(self, nom_prenom_info_joueur):
        """ Ajout d'un joueur à la liste de joueur """
        infos_joueur_a_ajouter = SaisieDeDonnees.ajout_des_informations_d_un_joueur(self.vue_saisie_de_donnees, nom_prenom_info_joueur)
        joueur_a_ajouter = Joueur(infos_joueur_a_ajouter["nom"], infos_joueur_a_ajouter["prenom"],
                                  infos_joueur_a_ajouter["date_de_naissance"], infos_joueur_a_ajouter["sexe"],
                                  infos_joueur_a_ajouter["classement_elo"])
        return joueur_a_ajouter

    def ajout_d_un_joueur_a_la_liste(self, joueur_a_ajouter, liste_joueurs):
        """ Ajoute un joueur à la liste des joueurs existants parmis lesquels il est possible de sélectionner
        les participants"""
        indice_nouveau_joueur = len(liste_joueurs) + 1
        cle_nouveau_joueur = "player" + str(indice_nouveau_joueur)
        liste_joueurs[cle_nouveau_joueur] = joueur_a_ajouter
        return liste_joueurs
