""" Point d'entrée du contrôleur"""
from vue.vue import Vue
from controleur.gestion_de_tournoi import GestionDeTournoi
from controleur.gestion_de_joueur import GestionDeJoueur
from controleur.gestion_de_rapport import GestionDeRapport
from vue.message_d_erreur import MessageDErreur
from vue.saisie_de_donnees import SaisieDeDonnees
from tinydb import TinyDB


class Controleur:
    """ Contrôleur general """

    def __init__(self):
        """ Initialise le contrôleur. """
        # Crée les objets initialisateur des classes qui seront utilisées
        self.vue_message_d_erreur = MessageDErreur()
        self.vue_instance = Vue(self.vue_message_d_erreur)
        self.vue_saisie_de_donnees = SaisieDeDonnees(self.vue_instance, self.vue_message_d_erreur)
        self.gestion_joueur = GestionDeJoueur(self.vue_instance, self.vue_message_d_erreur, self.vue_saisie_de_donnees)
        self.gestion_rapport = GestionDeRapport(self.vue_instance, self.gestion_joueur, self.vue_message_d_erreur,
                                                self.vue_saisie_de_donnees)
        self.gestion_tournoi = GestionDeTournoi(self.vue_instance, self.gestion_joueur, self.gestion_rapport,
                                                self.vue_message_d_erreur, self.vue_saisie_de_donnees)

    def execute(self):
        """ Lance le programme """
        # Initialise la base de donnée
        db = TinyDB('db.json')
        # Initialise la table joueur
        players_table = db.table('players')
        # Initialise la table tournoi
        tournaments_table = db.table('tournaments')
        # Lance la gestion du tournoi
        GestionDeTournoi.gestion_du_tournoi(self.gestion_tournoi, players_table, tournaments_table)
