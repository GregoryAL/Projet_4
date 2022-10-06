""" Point d'entrée du contrôleur"""
from modele.joueur import Joueur
from vue.vue import Vue
from controleur.gestion_de_tournoi import GestionDeTournoi
from controleur.gestion_de_joueur import GestionDeJoueur
from controleur.gestion_de_rapport import GestionDeRapport
from vue.message_d_erreur import MessageDErreur
from vue.saisie_de_donnees import SaisieDeDonnees


class Controleur:
    """ contrôleur general """

    def __init__(self):
        """ initialise le controleur. """
        self.vue_instance = Vue()
        self.vue_message_d_erreur = MessageDErreur()
        self.vue_saisie_de_donnees = SaisieDeDonnees(self.vue_instance)
        self.gestion_joueur = GestionDeJoueur(self.vue_instance, self.vue_message_d_erreur, self.vue_saisie_de_donnees)
        self.gestion_rapport = GestionDeRapport(self.vue_instance, self.gestion_joueur, self.vue_message_d_erreur,
                                                self.vue_saisie_de_donnees)
        self.gestion_tournoi = GestionDeTournoi(self.vue_instance, self.gestion_joueur, self.gestion_rapport,
                                                self.vue_message_d_erreur, self.vue_saisie_de_donnees)

    def execute(self):
        """ lance le programme """
        liste_joueurs = GestionDeJoueur.ajout_des_joueurs(self.gestion_joueur)
        GestionDeTournoi.gestion_du_tournoi(self.gestion_tournoi, liste_joueurs)

