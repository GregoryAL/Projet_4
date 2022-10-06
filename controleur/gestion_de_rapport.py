from vue.vue import Vue
from controleur.gestion_de_joueur import GestionDeJoueur
from vue.message_d_erreur import MessageDErreur
from vue.saisie_de_donnees import SaisieDeDonnees


class GestionDeRapport:
    """ Classe gérant les rapports """

    def __init__(self, vue_instance, gestion_joueur, vue_message_d_erreur, vue_saisie_de_donnees):
        """ crée l'objet type de joueur """
        self.vue_instance = vue_instance
        self.gestion_joueur = gestion_joueur
        self.vue_message_d_erreur = vue_message_d_erreur
        self.vue_saisie_de_donnees = vue_saisie_de_donnees

    def choix_du_type_de_classement_tournoi(self, instance_de_tournoi):
        choix_de_tri = int(SaisieDeDonnees.choix_classement_ou_alphabetique(self.vue_saisie_de_donnees))
        if choix_de_tri == 1:
            return GestionDeJoueur.classement_des_joueurs(self.gestion_joueur, instance_de_tournoi.participants, "nom")
        elif choix_de_tri == 2:
            return GestionDeJoueur.classement_des_joueurs(self.gestion_joueur, instance_de_tournoi.participants,
                                                          "points_tournoi")
        else:
            MessageDErreur.message_d_erreur(self.vue_message_d_erreur)

    def choix_du_type_de_classement_elo(self, liste_joueurs):
        choix_de_tri = int(SaisieDeDonnees.choix_classement_ou_alphabetique(self.vue_saisie_de_donnees))
        if choix_de_tri == 1:
            return GestionDeJoueur.classement_des_joueurs(self.gestion_joueur, liste_joueurs, "nom")
        elif choix_de_tri == 2:
            return GestionDeJoueur.classement_des_joueurs(self.gestion_joueur, liste_joueurs, "classement_elo")
        else:
            MessageDErreur.message_d_erreur(self.vue_message_d_erreur)

    def affichage_du_classement_tournoi(self, instance_de_tournoi, numero_de_ronde_active):
        """ Affiche le classement du tournoi """
        instance_de_tournoi.participants = self.choix_du_type_de_classement_tournoi(instance_de_tournoi)
        nombre_de_participants = len(instance_de_tournoi.participants)
        Vue.affichage_classement(self.vue_instance, instance_de_tournoi.participants, nombre_de_participants,
                                 numero_de_ronde_active)

    def affichage_du_classement_elo(self, liste_joueur_a_trier, numero_de_ronde_active):
        """ Affiche le classement en fonction des points elo """
        liste_joueur_a_trier = GestionDeJoueur.classement_des_joueurs(self.gestion_joueur, liste_joueur_a_trier,
                                                                      "classement_elo")
        nombre_de_joueurs = len(liste_joueur_a_trier)
        Vue.affichage_classement(self.vue_instance, liste_joueur_a_trier, nombre_de_joueurs, numero_de_ronde_active)

    def affichage_du_classement_elo_dict(self, liste_joueur_a_trier):
        """ Affiche le classement en fonction des points elo d'un dictionnaire de joueur"""
        liste_joueur_liste = []
        for objet in liste_joueur_a_trier.values():
            liste_joueur_liste.append(objet)
        liste_triee = self.choix_du_type_de_classement_elo(liste_joueur_liste)
        nombre_de_joueurs = len(liste_joueur_a_trier)
        Vue.affichage_classement(self.vue_instance, liste_triee, nombre_de_joueurs, "")

