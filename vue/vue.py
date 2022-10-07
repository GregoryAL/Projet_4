""" Vue de base """
from os import system
from os import name
import sys


class Vue:
    """ Vue du tournoi d'échec """

    def __init__(self):
        """ Initialise un objet vue"""
        self.liste_des_joueurs = []

    def clean_screen(self):
        """ Efface l'écran """
        if name == "nt":
            _ = system("cls")
        else:
            _ = system("clear")

    def affichage_classement(self, liste_triee, nombre_de_participants, numero_de_ronde_active):
        """ Affiche le classement des joueurs en fonction des resultats du tournoi """
        if numero_de_ronde_active != "":
            print("Numéro de Ronde : " + str(numero_de_ronde_active) + " : \n")
        for i in range(nombre_de_participants):
            print(" | " + str((i+1)) + " | : " + str(liste_triee[i]) + " \n")

    def affichage_choix_liste_participants(self, liste_participants):
        nombre_de_participants = len(liste_participants)
        for i in range(nombre_de_participants):
            print(" | " + str((i+1)) + " | : " + str(liste_participants[i]))

    def affichage_duplicate(self, liste_duplicate):
        print("Il y a plus d'un joueur avec ces noms et prénoms. \n")
        for i in range(len(liste_duplicate)):
            print(" [" + str(i) + "] : " + str(liste_duplicate[i].prenom) + " " + str(liste_duplicate[i].nom) +
                  " | Date de naissance : " + str(liste_duplicate[i].date_de_naissance) +
                  " | Sexe : " + str(liste_duplicate[i].sexe) +
                  " | Classement elo : " + str(liste_duplicate[i].classement_elo) + "\n")

    def message_de_sortie_1(self):
        """ Affiche un message de sortie """
        print("Merci d'avoir utilisé le logiciel de gestion de tournoi d'échec.\n")

    def message_de_sortie_2(self):
        """ Affiche un message de sortie et quitte le programme"""
        sys.exit("Vous quittez la gestion du tournoi")

    def affichage_des_matchs(self, instance_de_match):
        """ Affiche le match """
        print(instance_de_match.joueur1.nom + " affronte " + instance_de_match.joueur2.nom)
