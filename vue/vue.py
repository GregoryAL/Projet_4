""" Vue de base """
from os import system
from os import name
import sys
from vue.message_d_erreur import MessageDErreur


class Vue:
    """ Vue du tournoi d'échec """

    def __init__(self, objet_message_erreur):
        """ Initialise un objet vue"""
        self.liste_des_joueurs = []
        self.objet_message_erreur = objet_message_erreur

    def clean_screen(self):
        """ Efface l'écran """
        if name == "nt":
            _ = system("cls")
        else:
            _ = system("clear")

    def affichage_classement(self, numero_de_ronde_active, liste_db_triee):
        """ Affiche le classement des joueurs en fonction des resultats du tournoi """
        if numero_de_ronde_active != "":
            print("Numéro de Ronde : " + str(numero_de_ronde_active) + " : \n")
        for player in liste_db_triee:
            print(player["prenom"] + " " + player["nom"] +
                  " || Date de naissance : " + player["date_de_naissance"] +
                  " || Sexe : " + player["sexe"] +
                  " || Classement elo : " + str(player["classement_elo"]))

    def affichage_creation_tournoi_en_cours(self):
        print("Création du tournoi en cours...")

    def affichage_classement_participants(self, numero_de_ronde_active, liste_db_triee):
        """ Affiche le classement des joueurs en fonction des resultats du tournoi """
        self.clean_screen()
        if numero_de_ronde_active != "":
            print(" \n Numéro de Ronde " + str(numero_de_ronde_active) + " :")
        i=0
        for player in liste_db_triee:
            i += 1
            print("[" + str(i) + "] " +
                  player[0].prenom + " " + player[0].nom +
                  " || Date de naissance : " + player[0].date_de_naissance +
                  " || Sexe : " + player[0].sexe +
                  " || Classement elo : " + str(player[0].classement_elo) +
                  " || Nombre de point dans le tournoi en cours : " + str(player[1]))

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

    def message_de_sortie_3(self):
        """ Affiche un message de sortie et quitte le menu rapport"""
        print("Vous quittez le menu Rapport ")

    def affichage_des_matchs(self, instance_de_match):
        """ Affiche le match """
        print(instance_de_match.joueur1[0].nom + " affronte " + instance_de_match.joueur2[0].nom)


    def affichage_liste_de_tournoi(self, tournaments_table):
        for tournament in tournaments_table:
            try:
                print("ID : " + str(tournament.doc_id) +
                      " Nom du Tournoi [" + str(tournament["nom"]) + "] Lieu : " + str(tournament["lieu"]) +
                      " Date du Tournoi : " + str(tournament["dates_du_tournoi"]) +
                      " Type de controle du temps : " + str(tournament["type_controle_de_temps"]) +
                      " Nombre de participant : " + str(tournament["nombre_de_participants"]) +
                      " Commentaires : " + str(tournament["commentaire"]))

            except:
                input("erreur")

    def affichage_liste_des_tours(self, ronde):
        i = 0
        for ronde_tour in ronde["rondes"]:
            i += 1
            print("[" + str(i) + "]" + " Nom de la ronde : " + ronde_tour["nom_de_la_ronde"] + " |" +
                  " Date et Heure de début de la ronde : " + ronde_tour["date_heure_debut_ronde"] + " |"
                  + "Date et Heure de fin de la ronde : " + ronde_tour["date_heure_fin_ronde"] + " |")

    def affichage_liste_des_matchs(self, ronde, players_table):
        i = 0
        for ronde_tour in ronde["rondes"]:
            print(ronde_tour["nom_de_la_ronde"] + " : ")
            for match in ronde_tour["liste_match"]:
                i += 1
                joueur1_match = players_table.get(doc_id=match["joueur1"])
                joueur1_string_nom_prenom = (joueur1_match["prenom"] + " " + joueur1_match["nom"])
                joueur2_match = players_table.get(doc_id=match["joueur2"])
                joueur2_string_nom_prenom = (joueur2_match["prenom"] + " " + joueur2_match["nom"])
                if (int(match["resultat_joueur1"]) == 1) & (int(match["resultat_joueur2"]) == 0):
                    print(" Match " + str(i) + " : Entre " + joueur1_string_nom_prenom + " et " +
                          joueur2_string_nom_prenom + " | Vainqueur : " + joueur1_string_nom_prenom)
                elif (int(match["resultat_joueur1"]) == 0) & (int(match["resultat_joueur2"]) == 1):
                    print(" Match " + str(i) + " : Entre " + joueur1_string_nom_prenom + " et " +
                          joueur2_string_nom_prenom + " | Vainqueur : " + joueur2_string_nom_prenom)
                elif match["resultat_joueur1"] == match["resultat_joueur2"]:
                    print(" Match " + str(i) + " : Entre " + joueur1_string_nom_prenom + " et " +
                          joueur2_string_nom_prenom + " | Match Nul ")
                else:
                    MessageDErreur.message_d_erreur(self.objet_message_erreur)
        input()