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

    def choix_classement_ou_alphabetique(self):
        """ Recupere le choix de l'utilisateur entre un tri alphabetique ou par classement """
        choix_classement = int(input("Voulez vous un tri : \n [1] Alphabetique \n [2] Par Classement elo\n "
                                     "[3] par classement tournoi\n:"))
        if choix_classement == 1:
            return "nom"
        elif choix_classement == 2:
            return "classement_elo"
        elif choix_classement == 3:
            return "points_tournoi"
        else:
            MessageDErreur.message_d_erreur_option_tri_alpha(self.vue_message_d_erreur)
            return "nom"

    def choix_du_type_de_classement_tournoi(self, instance_de_tournoi):
        choix_de_tri = int(self.choix_classement_ou_alphabetique())
        if choix_de_tri == 1:
            return GestionDeJoueur.classement_des_joueurs(self.gestion_joueur, instance_de_tournoi.participants, "nom")
        elif choix_de_tri == 2:
            return GestionDeJoueur.classement_des_joueurs(self.gestion_joueur, instance_de_tournoi.participants,
                                                          "points_tournoi")
        elif choix_de_tri == 3:
            return GestionDeJoueur.classement_des_joueurs(self.gestion_joueur, instance_de_tournoi.participants,
                                                          "points_tournoi")
        else:
            MessageDErreur.message_d_erreur(self.vue_message_d_erreur)

    def choix_du_type_de_classement_db(self, liste_joueurs):
        choix_de_tri = int(self.choix_classement_ou_alphabetique())
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
        Vue.affichage_classement(self.vue_instance, numero_de_ronde_active, players_table)

    def affichage_du_classement_db(self, numero_de_ronde_active, players_table, type_tri):
        """ Affiche le classement en fonction des points elo """
        liste_joueur_triee = GestionDeJoueur.classement_des_joueurs_db(self.gestion_joueur, players_table, type_tri)
        Vue.affichage_classement(self.vue_instance, numero_de_ronde_active, liste_joueur_triee)
        MessageDErreur.appuyer_sur_entrer_pour_continuer(self.vue_message_d_erreur)

    def affichage_du_classement_elo_dict(self, liste_joueur_a_trier):
        """ Affiche le classement en fonction des points elo d'un dictionnaire de joueur"""
        liste_joueur_liste = []
        for objet in liste_joueur_a_trier.values():
            liste_joueur_liste.append(objet)
        liste_triee = self.choix_du_type_de_classement_elo(liste_joueur_liste)
        nombre_de_joueurs = len(liste_joueur_a_trier)
        Vue.affichage_classement(self.vue_instance, "", players_table)

