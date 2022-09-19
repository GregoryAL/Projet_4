""" Vue de base """


class Vue:
    """ Vue du tournoi d'échec """
    def __init__(self):
        self.tournoi = ""

    def creation_du_tournoi(self):
        """ Creation du tournoi """
        self.tournoi = self.demande_du_nom_du_tournoi(), \
            self.demande_du_lieu_du_tournoi(), \
            self.demande_des_dates_du_tournoi(), \
            self.demande_de_type_de_controle_du_temps(), \
            self.demande_du_nombre_de_participant_au_tournoi(), \
            self.demande_du_nombre_de_tour(), \
            self.demande_de_commentaire_pour_le_tournoi()
        return self.tournoi

    def demande_du_nombre_de_participant_au_tournoi(self):
        """ Demande le nombre de participant au tournoi """
        nombre_de_participant = int(input("Entrez le nombre de participants du tournoi à créer : \n"))
        return nombre_de_participant

    def demande_du_nom_du_tournoi(self):
        """ Demande le nom du tournoi """
        nom_du_tournoi = input("Entre le nom du tournoi à créer : \n")
        return nom_du_tournoi

    def demande_du_lieu_du_tournoi(self):
        """ Demande la location du tournoi """
        lieu_du_tournoi = input("Entrez la localisation du tournoi à créer : \n")
        return lieu_du_tournoi

    def demande_des_dates_du_tournoi(self):
        """ Demande les dates du tournoi """
        date_de_debut = input("Entrez la date de début du tournoi à créer au format JJ/MM/AAAA : \n")
        date_de_fin = input("Entrez la date de fin du tournoi à créer au format JJ/MM/AAAA : \n")
        if date_de_debut == date_de_fin:
            date_de_tournoi = [date_de_debut]
        else:
            date_de_tournoi = [date_de_debut, date_de_fin]
        return date_de_tournoi

    def demande_du_nombre_de_tour(self):
        """ Demande le nombre de tour du tournoi """
        nombre_de_tour = int(input("Entrez le nombre de tour du tournoi à créer (Si aucun nombre entré, 4 par défaut): \n"))
        if nombre_de_tour == "":
            return 4
        else:
            return nombre_de_tour

    def demande_de_type_de_controle_du_temps(self):
        """ Demande le type du controle de temps du tournoi """
        type_controle_du_temps = input("Entrez le type de controle de temps du tournoi : \n")
        return type_controle_du_temps

    def demande_de_commentaire_pour_le_tournoi(self):
        """ Demande s'il y a des commentaire à ajouter pour le tournoi"""
        commentaires = input("Entrez des commentaires si nécessaire : \n")
        if commentaires == "":
            return ""
        else:
            return commentaires


"""print("Veuillez renseigner les informations du tournoi : ")
    instance_de_tournoi = tournoi.Tournoi(input("nombre de participants : "),
                                          input("nom : "),
                                          input("lieu : "),
                                          input("date : "),
                                          input("nombre de tour : "),
                                          input("controle du temps : "))

    print(instance_de_tournoi.nombre_de_participants)
    for i in range(int(instance_de_tournoi.nombre_de_participants)):
        joueur_name = input("Entrez le nom du joueur " + str(i+1) + " : ")
        print(joueur_name)
        joueur_firstname = input("Entrez le prenom du joueur " + str(i+1) + "  : ")
        print(joueur_firstname)
        joueur_birthdate = input("Entrez la date de naissance du joueur " + str(i+1) + "  : ")
        print(joueur_birthdate)
        joueur_sex = input("Entrez le sexe du joueur " + str(i+1) + "  : ")
        print(joueur_sex)
        joueur_elo_rating = input("Entrez le classement elo du joueur " + str(i+1) + "  : ")
        print(joueur_elo_rating)"""
