""" Vue de base """
from os import system
from os import name


class Vue:
    """ Vue du tournoi d'échec """

    def __init__(self):
        self.liste_des_joueurs = {}


    def clean_screen(self):
        if name == "nt":
            _ = system("cls")
        else:
            _ = system("clear")

    def message_d_erreur(self):
        print("il y a eut une erreur. \n")

    def menu(self):
        """ Affichage du menu général"""
        # Vide l'écran
        self.clean_screen()
        # Affiche le menu
        print("Menu pour la gestion d'un tournoi d'échec\n")
        print(" [1] Selection des joueurs participants au tournoi puis création et lancement du tournoi \n")
        print(" [2] ????\n")
        print(" [3] Ajout d'un joueur dans la liste des joueurs\n")
        print(" [4] test print\n")
        print(" [5] Sortir de la gestion du tournoi\n")
        choix_utilisateur = input("Entrez le chiffre correspondant à l'action voulue :\n")
        return choix_utilisateur

    def recuperation_nombre_de_participants_du_tournoi(self):
        """ Recupère le nombre de joueurs participants au tournoi """
        nombre_de_participant = input("Merci de saisir le nombre de participants au tournoi. \n")
        return nombre_de_participant

    def recuperation_participant_du_tournoi(self, numero_de_joueur):
        """ Recupère le nom et le prenom du joueur à ajouter à la liste des participants """
        joueur_a_ajouter = {}
        if numero_de_joueur == 0:
            nom_du_joueur = input("Merci de saisir le nom du premier joueur à ajouter. \n")
            prenom_du_joueur = input("Merci de saisir le prenom du  premier joueur à ajouter. \n")
            joueur_a_ajouter["Nom"] = nom_du_joueur
            joueur_a_ajouter["Prenom"] = prenom_du_joueur
        else :
            nom_du_joueur = input("Merci de saisir le nom du " + str(numero_de_joueur+1) + "ème joueur à ajouter. \n")
            prenom_du_joueur = input("Merci de saisir le prenom du " + str(numero_de_joueur+1) + "ème joueur à ajouter. \n")
            joueur_a_ajouter["Nom"] = nom_du_joueur
            joueur_a_ajouter["Prenom"] = prenom_du_joueur
        return joueur_a_ajouter


    def recuperation_des_resultats_d_un_match(self, match):
        """ Récupère les résultats d'un joueur d'un match d'une ronde"""
        resultat_match = input("Entrez le résultat du match entre 1:" + match.joueur1.nom + " et 2:" + match.joueur2.nom +
                                     " (1/N/2) : \n")
        return resultat_match

    def verification_resultat_match_avec_vainqueur(self, joueur1, joueur2):
        """ Verifie que la réponse entrée par l'utilisateur est la bonne"""
        resultat_verification = input(joueur1.nom + " a gagné contre " + joueur2.nom + ". \n Si c'est exacte, tapez "
                                                                                       "'OK' puis entrer: \n")
        return resultat_verification

    def verification_resultat_match_nul(self, joueur1, joueur2):
        resultat_verification = input(joueur1.nom + " a fait match nul contre " + joueur2.nom + ". \n Si c'est exacte, "
                                                                                                "tapez 'OK' puis entrer"
                                                                                                ": \n")
        return resultat_verification

    def recuperation_des_informations_du_tournoi(self, nombre_de_participant):
        """ Creation du tournoi """
        # Vide l'écran
        self.clean_screen()
        informations_de_tournoi = {}
        # Recupere le nombre de participants au tournoi défini dans la sélection des joueurs
        informations_de_tournoi["nombre_de_participant"] = int(nombre_de_participant)
        # Demande le nom du tournoi
        nom_du_tournoi = input("Entre le nom du tournoi à créer : \n")
        informations_de_tournoi["nom_du_tournoi"] = nom_du_tournoi
        # Demande la location du tournoi
        lieu_du_tournoi = input("Entrez la localisation du tournoi à créer : \n")
        informations_de_tournoi["lieu_du_tournoi"] = lieu_du_tournoi
        # Demande les dates du tournoi
        date_de_debut = input("Entrez la date de début du tournoi à créer au format JJ/MM/AAAA : \n")
        date_de_fin = input("Entrez la date de fin du tournoi à créer au format JJ/MM/AAAA : \n")
        if date_de_debut == date_de_fin:
            date_de_tournoi = [date_de_debut]
        else:
            date_de_tournoi = [date_de_debut, date_de_fin]
        informations_de_tournoi["date_de_tournoi"] = date_de_tournoi
        # Demande le nombre de tours du tournoi
        nombre_de_tour = input("Entrez le nombre de tour du tournoi à créer (Si aucun nombre entré, 4 par défaut): \n")
        if nombre_de_tour != "":
            informations_de_tournoi["nombre_de_tour"] = int(nombre_de_tour)
        else:
            informations_de_tournoi["nombre_de_tour"] = 4
        # Demande le type du contrôle de temps du tournoi
        type_de_controle_du_temps = input("Entrez le type de controle de temps du tournoi ( bullet, blitz ou coup "
                                          "rapide): \n")
        informations_de_tournoi["type_de_controle_du_temps"] = type_de_controle_du_temps
        # Demande s'il y a des commentaires à ajouter pour le tournoi
        commentaires = input("Entrez des commentaires si nécessaire : \n")
        if commentaires != "":
            informations_de_tournoi["commentaires"] = commentaires
        else:
            informations_de_tournoi["commentaires"] = ""
        return informations_de_tournoi

    def depart_de_la_ronde(self):
        input("Appuyer sur 'Entrer' quand la ronde commence")

    def fin_de_la_ronde(self):
        input("Appuyer sur 'Entrer' lorsque tous les matchs sont terminés")

    def joueur_inexistant(self):
        reponse_creation_joueur = input("Joueur inexistant : Voulez vous créer le joueur? (Oui/Non)")
        return reponse_creation_joueur

    def ajout_des_informations_d_un_joueur(self, info_joueur_inexistant):
        joueur_a_ajouter = {}
        if info_joueur_inexistant != "":
            recuperation_info_joueur_inexistant = input(" Voulez vous ajouter le joueur " +
                                                        info_joueur_inexistant["Prenom"] + " " +
                                                        info_joueur_inexistant["Nom"] + " à la liste des "
                                                                                        "joueurs?(Oui/Non)")
            if recuperation_info_joueur_inexistant == "Oui":
                joueur_a_ajouter["nom"] = info_joueur_inexistant["Nom"]
                joueur_a_ajouter["prenom"] = info_joueur_inexistant["Prenom"]
            else:
                nom_a_ajouter = input("Entrez le nom du joueur à ajouter:\n")
                joueur_a_ajouter["nom"] = nom_a_ajouter
                prenom_a_ajouter = input("Entrez le prenom du joueur à ajouter:\n")
                joueur_a_ajouter["prenom"] = prenom_a_ajouter
        else :
            nom_a_ajouter = input("Entrez le nom du joueur à ajouter:\n")
            joueur_a_ajouter["nom"] = nom_a_ajouter
            prenom_a_ajouter = input("Entrez le prenom du joueur à ajouter:\n")
            joueur_a_ajouter["prenom"] = prenom_a_ajouter
        date_de_naissance_a_ajouter = input("Entre la date de naissance du joueur à ajouter:\n")
        joueur_a_ajouter["date_de_naissance"] = date_de_naissance_a_ajouter
        sexe_a_ajouter = input("Entre le sexe du joueur à ajouter:\n")
        joueur_a_ajouter["sexe"] = sexe_a_ajouter
        classement_elo_a_ajouter = int(input("Entrez le classement elo du joueur à ajouter:\n"))
        joueur_a_ajouter["classement_elo"] = classement_elo_a_ajouter
        return joueur_a_ajouter

    def affichage_des_matchs(self, instance_de_match):
        print(instance_de_match.joueur1.nom + " affronte " + instance_de_match.joueur2.nom)

