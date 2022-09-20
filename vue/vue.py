""" Vue de base """


class Vue:
    """ Vue du tournoi d'échec """

    def __init__(self):
        self.tournoi = {}
        self.liste_des_joueurs = {}
        self.choix_utilisateur = ""

    def menu(self):
        """ Affichage du menu général"""
        print("Menu pour la gestion d'un tournoi d'échec\n")
        print(" [1] Création d'un tournoi\n")
        print(" [2] Option 2\n")
        print(" [3] option 3\n")
        self.choix_utilisateur = input("Entrez le chiffre correspondant à l'action voulue :\n")
        return self.choix_utilisateur


    def recuperation_des_informations_du_tournoi(self):
        """ Creation du tournoi """
        # Demande le nombre de participant au tournoi
        nombre_de_participant = int(input("Entrez le nombre de participants du tournoi à créer : \n"))
        self.tournoi["nombre_de_participant"] = nombre_de_participant
        # Demande le nom du tournoi
        nom_du_tournoi = input("Entre le nom du tournoi à créer : \n")
        self.tournoi["nom_du_tournoi"] = nom_du_tournoi
        # Demande la location du tournoi
        lieu_du_tournoi = input("Entrez la localisation du tournoi à créer : \n")
        self.tournoi["lieu_du_tournoi"] = lieu_du_tournoi
        # Demande les dates du tournoi
        date_de_debut = input("Entrez la date de début du tournoi à créer au format JJ/MM/AAAA : \n")
        date_de_fin = input("Entrez la date de fin du tournoi à créer au format JJ/MM/AAAA : \n")
        if date_de_debut == date_de_fin:
            date_de_tournoi = [date_de_debut]
        else:
            date_de_tournoi = [date_de_debut, date_de_fin]
        self.tournoi["date_de_tournoi"] = date_de_tournoi
        # Demande le nombre de tour du tournoi
        nombre_de_tour = input("Entrez le nombre de tour du tournoi à créer (Si aucun nombre entré, 4 par défaut): \n")
        if nombre_de_tour != "":
            self.tournoi["nombre_de_tour"] = int(nombre_de_tour)
        # Demande le type du controle de temps du tournoi
        type_de_controle_du_temps = input("Entrez le type de controle de temps du tournoi : \n")
        self.tournoi["type_de_controle_du_temps"] = type_de_controle_du_temps
        # Demande s'il y a des commentaire à ajouter pour le tournoi
        commentaires = input("Entrez des commentaires si nécessaire : \n")
        if commentaires != "":
            self.tournoi["commentaires"] = commentaires
        return self.tournoi

    def recuperation_des_informations_des_joueurs(self):
        for numero_participant in range(self.tournoi["nombre_de_participant"]):
            joueur = {}
            prenom = input("Entrez le prenom du joueur" + str(numero_participant+1) + ":\n")
            joueur["prenom"] = prenom
            nom = input("Entrez le nom du joueur " + str(numero_participant+1) + ":\n")
            joueur["nom"] = nom
            date_de_naissance = input("Entre la date de naissance du joueur " + str(numero_participant+1) + ":\n")
            joueur["date_de_naissance"] = date_de_naissance
            sexe = input("Entre le sexe du joueur " + str(numero_participant+1) + "\n")
            joueur["sexe"] = sexe
            classement_elo = input("Entrez le classement elo du joueur " + str(numero_participant+1) + ":\n")
            joueur["classement_elo"] = classement_elo
            joueur["points_tournoi"] = 0
            self.liste_des_joueurs["joueur"+str(numero_participant+1)] = joueur
        return self.liste_des_joueurs
