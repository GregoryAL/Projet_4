""" Point d'entrée du contrôleur"""
from modele.joueur import Joueur
from vue.vue import Vue
from controleur.gestion_de_tournoi import GestionDeTournoi
from controleur.gestion_de_joueur import GestionDeJoueur
from controleur.gestion_de_rapport import GestionDeRapport


class Controleur:
    """ contrôleur general """

    def __init__(self, vue):
        """ initialise le controleur. """
        self.vue_instance = vue

    def execute(self):
        """ lance le programme """
        gestion_joueur = GestionDeJoueur(self.vue_instance)
        gestion_rapport = GestionDeRapport(self.vue_instance, gestion_joueur)
        gestion_tournoi = GestionDeTournoi(self.vue_instance, gestion_joueur, gestion_rapport)
        liste_joueurs = GestionDeJoueur.ajout_des_joueurs(gestion_joueur)
        GestionDeTournoi.gestion_du_tournoi(gestion_tournoi, liste_joueurs)

