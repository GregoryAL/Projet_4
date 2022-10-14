from vue.vue import Vue
from vue.message_d_erreur import MessageDErreur



class SaisieDeDonnees:

    def __init__(self, vue, message_d_erreur):
        """ initialiste un objet Saisie de données """
        self.vue = vue
        self.message_d_erreur = message_d_erreur



    def selection_joueur_a_modifier(self):
        nom_joueur_a_modifier = input("Veuillez entrer le nom du joueur à modifier : \n")
        prenom_joueur_a_modifier = input("Veuillez entrer le prénom du joueur à modifier : \n")
        joueur_a_modifier = {"nom": nom_joueur_a_modifier, "prenom": prenom_joueur_a_modifier}
        return joueur_a_modifier

    def selection_base_a_modifier(self):
        base_a_modifier = input("Voulez vous modifier un joueur de la liste des joueurs ? (1)\n"
                                "Ou  un joueur de la liste des participants du tournoi? (2) \n"
                                ": ")
        return base_a_modifier

    def selection_du_parametre_a_modifier(self):
        parametre_a_modifier = input("Quel paramètre du joueur souhaitez vous modifier?\n"
                                     "[1] Nom\n"
                                     "[2] Prénom\n"
                                     "[3] Date de naissance\n"
                                     "[4] Sexe \n"
                                     "[5] Points elo \n"
                                     "[6] Points tournoi \n"
                                     "Veuillez entrer le chiffre correspondant : \n")
        return int(parametre_a_modifier)

    def entree_nouvelle_valeur_parametre(self, parametre):
        if parametre == "nom":
            return input("Quel est le nouveau Nom?\n:")
        elif parametre == "prenom":
            return input("Quel est le nouveau Prenom?\n:")
        elif parametre == "date_de_naissance":
            return input("Quelle est la nouvelle date de naissance?\n:")
        elif parametre == "sexe":
            return input("Quel est le nouveau sexe?\n:")
        elif parametre == "classement_elo":
            return int(input("Quel est le nouveau nombre de points elo?\n:"))
        elif parametre == "points_tournoi":
            return int(input("Quel est le nouveau nombre de points tournoi?\n:"))



    def modification_classement_elo(self, joueur):
        print("Le classement elo de " + str(joueur.prenom) + " " + str(joueur.nom) + " est " +
              str(joueur.classement_elo) + ".\n")
        nouveau_classement = input("A combien voulez-vous changer le classement elo? \n : ")
        return nouveau_classement

    def modification_point_tournoi(self, joueur):
        print("Le joueur " + str(joueur.prenom) + " " + str(joueur.nom) + " a " +
              str(joueur.points_tournoi) + " points dans le tournoi.")
        nouveaux_points_tournois = input("A combien voulez-vous changer les points du tournoi? \n : ")
        return nouveaux_points_tournois

    def choisir_un_joueur(self):
        return int(input("Veuillez renseignez le numéro du joueur choisi : \n"))


    def menu(self):
        """ Affichage du menu général"""

        # Vide l'écran
        Vue.clean_screen(self.vue)
        # Affiche le menu
        try:
            print("                     Menu pour la gestion d'un tournoi d'échec\n"
                  "_________________________________________________________________________________________________\n"
                  " [1] Selection des joueurs participants au tournoi puis création et lancement du tournoi\n"
                  " [2] Lancement de la ronde suivante\n"
                  " [3] Ajout d'un joueur dans la liste des joueurs\n"
                  " [4] Modification d'un joueur ou d'un participant\n"
                  " [5] Rapport\n"
                  " [6] Sortie du Programme\n"
                  "_________________________________________________________________________________________________")
            choix_utilisateur = int(input("Entrez le chiffre correspondant à l'action voulue :\n"))
            return choix_utilisateur
        except TypeError:
            print("Choix non reconnu...\n")
            return 0

    def recuperation_choix_type_tournoi(self):
        try:
            Vue.clean_screen(self.vue)
            print("_________________________________________________________________________________________________\n"
                  " Merci de sélectionner le type de tournoi : \n"
                  " [1] Methode Suisse\n"
                  " [2] ??? \n")
            choix_type_tournoi = int(input("Entrez le chiffre correspondant :\n"))
            if choix_type_tournoi == 1:
                return "MethodeSuisse"
            else:
                print("Choix non reconnu...\n")
        except ValueError:
            print("Merci d'entrer un chiffre.")

    def menu_rapport(self):
        """ Affichage du menu général"""

        # Vide l'écran
        Vue.clean_screen(self.vue)
        # Affiche le menu
        try:
            print("                     Menu pour la gestion d'un tournoi d'échec\n"
                  "                                     Rapport\n"
                  "_________________________________________________________________________________________________\n"
                  " [1] Liste des joueurs\n"
                  " [2] Liste des participants\n"
                  " [3] Liste des tournois\n"
                  " [4] Liste des tours d'un tournoi\n"
                  " [5] Liste des matchs d'un tournoi\n"
                  " [6] Sortie du menu\n"
                  "_________________________________________________________________________________________________")
            choix_utilisateur = int(input("Entrez le chiffre correspondant à l'action voulue :\n"))
            return choix_utilisateur
        except TypeError:
            print("Choix non reconnu...\n")
            return 0

    def recuperation_nombre_de_participants_du_tournoi(self):
        """ Recupère le nombre de joueurs participants au tournoi """
        return input("Merci de saisir le nombre de participants au tournoi. \n")


    def recuperation_participant_du_tournoi(self, numero_de_joueur):
        """ Recupère le nom et le prenom du joueur à ajouter à la liste des participants """
        joueur_a_ajouter = {}
        if numero_de_joueur == 0:
            joueur_a_ajouter["nom"] = input("Merci de saisir le nom du premier joueur à ajouter. \n")
            joueur_a_ajouter["prenom"] = input("Merci de saisir le prenom du  premier joueur à ajouter. \n")
        else:
            joueur_a_ajouter["nom"] = input("Merci de saisir le nom du " + str(numero_de_joueur+1) + "ème joueur à "
                                                                                                     "ajouter. \n")
            joueur_a_ajouter["prenom"] = input("Merci de saisir le prenom du " + str(numero_de_joueur+1) +
                                     "ème joueur à ajouter. \n")
        return joueur_a_ajouter

    def recuperation_des_resultats_d_un_match(self, match):
        """ Récupère les résultats d'un joueur d'un match d'une ronde"""
        resultat_match = input("Entrez le résultat du match entre 1:" + match.joueur1[0].nom + " et 2:" +
                               match.joueur2[0].nom + " (1/N/2) : \n")
        return resultat_match

    def recuperation_des_informations_du_tournoi(self, nombre_de_participant):
        """ Creation du tournoi """
        # Vide l'écran
        Vue.clean_screen(self.vue)
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
        """ Affiche l'annonce de départ de ronde après appuie sur Entrer """
        input("Appuyer sur 'Entrer' quand la ronde commence")

    def fin_de_la_ronde(self):
        """ Affiche l'annonce de fin de ronde après appuie sur Entrer """
        input("Appuyer sur 'Entrer' lorsque tous les matchs sont terminés")

    def selection_duplicate(self, liste_duplicate):
        """ Demande de selectionner le joueur dans un choix d homonyme. Recupere le choix """
        confirmation_choix_homonyme = ""
        while confirmation_choix_homonyme != "Oui":
            choix_homonyme = ""
            try:
                choix_homonyme = int(input("Merci d'entrer le numéro du joueur à ajouter à la liste de participants \n"))
            except TypeError:
                MessageDErreur.message_d_erreur_d_input_chiffre(self.message_d_erreur)
            confirmation_choix_homonyme = input("Est ce que le choix : \n " +
                                                "[" + str(choix_homonyme) + "] : " +
                                                str(liste_duplicate[choix_homonyme].prenom) + " " +
                                                str(liste_duplicate[choix_homonyme].nom) + " | Date de naissance : " +
                                                str(liste_duplicate[choix_homonyme].date_de_naissance) + " | Sexe : " +
                                                str(liste_duplicate[choix_homonyme].sexe) + " | Classement elo : " +
                                                str(liste_duplicate[choix_homonyme].classement_elo) + "\nEst correct (Oui/Non)? \n:")
        else:
            return liste_duplicate[choix_homonyme]


    def joueur_inexistant(self):
        """ Annonce que le joueur est inexistant, demande si le joueur doit être créé """
        reponse_creation_joueur = input("Joueur inexistant : Voulez vous créer le joueur? (Oui/Non)")
        return reponse_creation_joueur

    def ajout_des_informations_d_un_joueur(self, info_joueur_inexistant):
        """ Recupère les informations d'un joueur à ajouter """
        joueur_a_ajouter = {}
        if info_joueur_inexistant != "":
            recuperation_info_joueur_inexistant = input(" Voulez vous ajouter le joueur " +
                                                        info_joueur_inexistant["prenom"] + " " +
                                                        info_joueur_inexistant["nom"] + " à la liste des "
                                                                                        "joueurs?(Oui/Non)")
            if recuperation_info_joueur_inexistant == "Oui":
                joueur_a_ajouter["nom"] = info_joueur_inexistant["nom"]
                joueur_a_ajouter["prenom"] = info_joueur_inexistant["prenom"]
            else:
                nom_a_ajouter = input("Entrez le nom du joueur à ajouter:\n")
                joueur_a_ajouter["nom"] = nom_a_ajouter
                prenom_a_ajouter = input("Entrez le prenom du joueur à ajouter:\n")
                joueur_a_ajouter["prenom"] = prenom_a_ajouter
        else:
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


