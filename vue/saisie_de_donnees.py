from vue.vue import Vue
from vue.message_d_erreur import MessageDErreur
from datetime import datetime


class SaisieDeDonnees:
    """ Vue du tournoi d'échec gérant les saisies """

    def __init__(self, vue, message_d_erreur):
        """ Initialise un objet Saisie de données """
        self.vue = vue
        self.message_d_erreur = message_d_erreur

    def selection_joueur_a_modifier(self):
        """ Récupère les informations du joueur à modifier """
        nom_joueur_a_modifier = self.verification_champs_non_vide("entrer le nom du joueur à modifier")
        prenom_joueur_a_modifier = self.verification_champs_non_vide(
            "Veuillez entrer le prénom du joueur à modifier : \n")
        joueur_a_modifier = {"nom": nom_joueur_a_modifier, "prenom": prenom_joueur_a_modifier}
        return joueur_a_modifier

    def selection_base_a_modifier(self):
        """ Permet la sélection de la liste à modifier (joueur ou participant) """
        base_a_modifier = self.verification_champs_est_nombre("Sélectionnez l'option désirée : \n"
                                                              "[1] Modifier un joueur de la liste des joueurs \n"
                                                              "[2] Modifier un joueur de la liste des participants du "
                                                              "tournoi \n"
                                                              ": ")
        return base_a_modifier

    def selection_du_parametre_a_modifier(self):
        """ Sélection du paramètre du participant à modifier """
        parametre_a_modifier = self.verification_champs_est_nombre("Quel paramètre du joueur souhaitez vous modifier"
                                                                   "?\n"
                                                                   "[1] Nom\n"
                                                                   "[2] Prénom\n"
                                                                   "[3] Date de naissance\n"
                                                                   "[4] Sexe \n"
                                                                   "[5] Points elo \n"
                                                                   "[6] Points tournoi \n"
                                                                   "Veuillez entrer le chiffre correspondant : \n")
        return int(parametre_a_modifier)

    def selection_du_parametre_a_modifier_joueur(self):
        """ Sélection du paramètre du joueur à modifier """
        parametre_a_modifier = self.verification_champs_est_nombre("Quel paramètre du joueur souhaitez vous modifier"
                                                                   "?\n"
                                                                   "[1] Nom\n"
                                                                   "[2] Prénom\n"
                                                                   "[3] Date de naissance\n"
                                                                   "[4] Sexe \n"
                                                                   "[5] Points elo \n"
                                                                   "Veuillez entrer le chiffre correspondant : \n")
        return int(parametre_a_modifier)

    def entree_nouvelle_valeur_parametre(self, parametre):
        """ Récupère la nouvelle valeur du paramètre Joueur sélectionné """
        if parametre == "nom":
            return self.verification_champs_non_vide("le nouveau Nom")
        elif parametre == "prenom":
            return self.verification_champs_non_vide("le nouveau Prénom")
        elif parametre == "date_de_naissance":
            return self.verification_si_valeur_est_date("la nouvelle date de naissance")
        elif parametre == "sexe":
            return self.verification_champs_non_vide("le nouveau sexe")
        elif parametre == "classement_elo":
            return self.verification_champs_est_nombre("Entrez le nouveau nombre de points elo :\n")
        elif parametre == "points_tournoi":
            return self.verification_champs_est_nombre("Entrez le nouveau nombre de points tournoi :\n")

    def choisir_un_joueur(self):
        """ Récupère l'id du joueur choisi """
        return int(self.verification_champs_est_nombre("Veuillez renseignez le numéro du joueur choisi : \n"))

    def menu(self):
        """ Affichage du menu général"""

        # Vide l'écran
        Vue.clean_screen(self.vue)
        # Affiche le menu
        try:
            entete = "Menu pour la gestion d'un tournoi d'échec"
            separateur = ""
            creation_tournoi = "[1] Selection des joueurs participants au tournoi puis création et lancement du tournoi"
            lancement_ronde = "[2] Lancement de la ronde suivante                                                     "
            ajout_joueur = "[3] Ajout d'un joueur dans la liste des joueurs                                        "
            modification_joueur = "[4] Modification d'un joueur ou d'un participant                                " \
                                  "       "
            rapport = "[5] Rapport                                                                            "
            sortie_programme = "[6] Sortie du Programme                                                                "
            print(entete.center(119) + "\n" +
                  separateur.center(119, "_") + "\n" +
                  creation_tournoi.center(119) + "\n" +
                  lancement_ronde.center(119) + "\n" +
                  ajout_joueur.center(119) + "\n" +
                  modification_joueur.center(119) + "\n" +
                  rapport.center(119) + "\n" +
                  sortie_programme.center(119) + "\n" +
                  separateur.center(119, "_"))
            choix_utilisateur = int(self.verification_champs_est_nombre("Entrez le chiffre correspondant à l'action "
                                                                        "voulue :\n"))
            return choix_utilisateur
        except TypeError:
            print("Choix non reconnu...\n")
            return 0

    def recuperation_choix_type_tournoi(self):
        """ Récupération du choix de type de tournoi """
        test_de_choix_valide = False
        while test_de_choix_valide is False:
            Vue.clean_screen(self.vue)
            choix_type_tournoi = self.verification_champs_est_nombre("________________________________________________"
                                                                     "_____________________________________________"
                                                                     "____\n"
                                                                     " Merci de sélectionner le type de tournoi : \n"
                                                                     " [1] Methode Suisse\n"
                                                                     " [2] ??? \n Veuillez entrer le chiffre "
                                                                     "correspondant :\n")
            if choix_type_tournoi == 1:
                return "MethodeSuisse"
            else:
                MessageDErreur.message_d_erreur_d_input_hors_choix(self.message_d_erreur)
                input()
                test_de_choix_valide = False

    def menu_rapport_light(self):
        """ Affichage du menu général """

        # Vide l'écran
        Vue.clean_screen(self.vue)
        # Affiche le menu
        try:
            entete1 = "Menu pour la gestion d'un tournoi d'échec"
            entete2 = "Rapport"
            entete3 = "!  Menu Réduit car aucune instance de tournoi en cours  !"
            separateur = "_"
            liste_joueur = " [1] Liste des joueurs            "
            liste_tournoi = " [2] Liste des tournois           "
            liste_tour = " [3] Liste des tours d'un tournoi "
            liste_match = " [4] Liste des matchs d'un tournoi"
            sortie_menu = " [5] Sortie du menu               "
            print(entete1.center(119) + "\n" + entete2.center(119) + "\n" + entete3.center(119) + "\n" +
                  separateur.center(119, "_") + "\n" +
                  liste_joueur.center(119) + "\n" +
                  liste_tournoi.center(119) + "\n" +
                  liste_tour.center(119) + "\n" +
                  liste_match.center(119) + "\n" +
                  sortie_menu.center(119) + "\n" +
                  separateur.center(119, "_"))
            choix_utilisateur = int(self.verification_champs_est_nombre("Entrez le chiffre correspondant à l'action "
                                                                        "voulue :\n"))
            return choix_utilisateur
        except TypeError:
            print("Choix non reconnu...\n")
            return 0

    def menu_rapport(self):
        """ Affichage du menu général """
        # Vide l'écran
        Vue.clean_screen(self.vue)
        # Affiche le menu
        try:
            entete1 = "Menu pour la gestion d'un tournoi d'échec"
            entete2 = "Rapport"
            separateur = "_"
            liste_joueur = " [1] Liste des joueurs            "
            liste_participant = " [2] Liste des participants       "
            liste_tournoi = " [3] Liste des tournois           "
            liste_tour = " [4] Liste des tours d'un tournoi "
            liste_match = " [5] Liste des matchs d'un tournoi"
            sortie_menu = " [6] Sortie du menu               "
            print(entete1.center(119) + "\n" + entete2.center(119) + "\n" +
                  separateur.center(119, "_") + "\n" +
                  liste_joueur.center(119) + "\n" +
                  liste_participant.center(119) + "\n" +
                  liste_tournoi.center(119) + "\n" +
                  liste_tour.center(119) + "\n" +
                  liste_match.center(119) + "\n" +
                  sortie_menu.center(119) + "\n" +
                  separateur.center(119, "_"))
            choix_utilisateur = int(self.verification_champs_est_nombre("Entrez le chiffre correspondant à l'action "
                                                                        "voulue :\n"))
            return choix_utilisateur
        except TypeError:
            print("Choix non reconnu...\n")
            return 0

    def recuperation_nombre_de_participants_du_tournoi(self):
        """ Récupère le nombre de joueurs participants au tournoi """
        return self.verification_champs_est_nombre("Merci de saisir le nombre de participants au tournoi. \n")

    def recuperation_id_tournoi(self, attribut):
        """ Récupère l'ID du tournoi choisi """
        return self.verification_champs_est_nombre("___________________________________________________________________"
                                                   "_______________________ \n"
                                                   "Merci de saisir l'ID du tournoi dont vous voulez la " +
                                                   str(attribut))

    def recuperation_participant_du_tournoi(self, numero_de_joueur):
        """ Récupère le nom et le prénom du joueur à ajouter à la liste des participants """
        joueur_a_ajouter = {}
        if numero_de_joueur == 0:
            joueur_a_ajouter["nom"] = self.verification_champs_non_vide("le nom du premier joueur à ajouter")
            joueur_a_ajouter["prenom"] = self.verification_champs_non_vide("le prenom du  premier joueur à ajouter")
        else:
            joueur_a_ajouter["nom"] = self.verification_champs_non_vide("le nom du " + str(numero_de_joueur+1) +
                                                                        "ème joueur à ajouter")
            joueur_a_ajouter["prenom"] = self.verification_champs_non_vide("le prenom du " + str(numero_de_joueur+1) +
                                                                           "ème joueur à ajouter")
        return joueur_a_ajouter

    def recuperation_des_resultats_d_un_match(self, match):
        """ Récupère les résultats d'un joueur d'un match d'une ronde """
        resultat_match = self.verification_champs_non_vide("le résultat du match entre 1:" + match.joueur1[0].nom +
                                                           " et 2:" + match.joueur2[0].nom + " (1/N/2)")
        return resultat_match

    def recuperation_type_tri_liste_joueur(self):
        return int(self.verification_champs_est_nombre("Merci de choisir le type de tri : \n "
                                                       "[1] Alphabétique \n "
                                                       "[2] Classement elo\n"
                                                       " :"))

    def recuperation_type_tri_liste_participant(self):
        return int(self.verification_champs_est_nombre("Merci de choisir le type de tri : \n "
                                                       "[1] Alphabétique \n "
                                                       "[2] Classement elo \n "
                                                       "[3] Points tournois \n"
                                                       " :"))

    def verification_champs_non_vide(self, type_valeur_recherchee):
        """ Vérifie que l'utilisateur a bien saisi une valeur """
        valeur_recherchee = input("Entrez " + type_valeur_recherchee + " : \n")
        while valeur_recherchee == "":
            print("Vous n'avez pas entré de valeur, merci d'entrer " + str(type_valeur_recherchee))
            valeur_recherchee = input("Entrez " + type_valeur_recherchee + " : \n")
        return valeur_recherchee

    def test_si_variable_un_nombre(self, variable):
        """ Test si une variable est un nombre et renvoie true / false """
        try:
            variable = int(variable)
            return True
        except (TypeError, ValueError):
            return False

    def verification_champs_est_nombre(self, type_valeur_recherchee):
        """ Prompt un message demandant la valeur du descriptif en argument puis teste la valeur et boucle
        jusqu'à ce que la valeur entree soit un chiffre """
        test_si_valeur_est_nombre = False
        valeur_recherchee = ""
        while test_si_valeur_est_nombre is False:
            valeur_recherchee = input(type_valeur_recherchee)
            test_si_valeur_est_nombre = self.test_si_variable_un_nombre(valeur_recherchee)
            if test_si_valeur_est_nombre is False:
                MessageDErreur.message_d_erreur_d_input_chiffre(self.message_d_erreur)
                Vue.clean_screen(self.vue)
        else:
            return int(valeur_recherchee)

    def recuperation_des_informations_du_tournoi(self):
        """ Création du tournoi """
        # Vide l'écran
        Vue.clean_screen(self.vue)
        informations_de_tournoi = {}
        # Demande le nom du tournoi
        nom_du_tournoi = self.verification_champs_non_vide("le nom du tournoi à créer")
        informations_de_tournoi["nom_du_tournoi"] = nom_du_tournoi
        # Demande la location du tournoi
        lieu_du_tournoi = self.verification_champs_non_vide("la localisation du tournoi à créer")
        informations_de_tournoi["lieu_du_tournoi"] = lieu_du_tournoi
        # Demande les dates du tournoi
        date_de_debut = self.verification_si_valeur_est_date("la date de début du tournoi à créer")
        date_de_fin = self.verification_si_valeur_est_date("la date de fin du tournoi à créer")
        if date_de_debut == date_de_fin:
            date_de_tournoi = [date_de_debut]
        else:
            date_de_tournoi = [date_de_debut, date_de_fin]
        informations_de_tournoi["date_de_tournoi"] = date_de_tournoi
        # Demande le nombre de tours du tournoi
        nombre_de_tour = self.verification_champs_est_nombre(
            "Entrez le nombre de tour du tournoi à créer (Si aucun nombre entré, 4 par défaut): \n")
        if nombre_de_tour != "":
            informations_de_tournoi["nombre_de_tour"] = int(nombre_de_tour)
        else:
            informations_de_tournoi["nombre_de_tour"] = 4
        # Demande le type du contrôle de temps du tournoi
        type_de_controle_du_temps = self.recuperation_type_de_tournoi()
        informations_de_tournoi["type_de_controle_du_temps"] = type_de_controle_du_temps
        # Demande s'il y a des commentaires à ajouter pour le tournoi
        commentaires = input("Entrez des commentaires si nécessaire : \n")
        informations_de_tournoi["commentaires"] = commentaires
        return informations_de_tournoi

    def recuperation_type_de_tournoi(self):
        """ Récupère le type de contrôle du temps du tournoi """
        valeur_test = False
        while valeur_test is False:
            type_de_tournoi = self.verification_champs_est_nombre("Entrez le type de controle de temps du tournoi \n"
                                                                  "[1] Bullet \n"
                                                                  "[2] Blitz \n"
                                                                  "[3] Coup rapide \n:")
            if int(type_de_tournoi) == 1:
                return "Bullet"
            elif int(type_de_tournoi) == 2:
                return "Blitz"
            elif int(type_de_tournoi) == 3:
                return "Coup rapide"
            else:
                MessageDErreur.message_d_erreur_d_input_hors_choix(self.message_d_erreur)
                valeur_test = False

    def depart_de_la_ronde(self):
        """ Affiche l'annonce de départ de ronde après appuie sur Entrer """
        input("Appuyer sur 'Entrer' quand la ronde commence")

    def fin_de_la_ronde(self):
        """ Affiche l'annonce de fin de ronde après appuie sur Entrer """
        input("Appuyer sur 'Entrer' lorsque tous les matchs sont terminés")

    def selection_duplicate(self, liste_duplicate):
        """ Demande de sélectionner le joueur dans un choix d'homonyme. Récupère le choix """
        confirmation_choix_homonyme = ""
        while confirmation_choix_homonyme != "Oui":
            choix_homonyme = ""
            try:
                choix_homonyme = int(input("Merci d'entrer le numéro du joueur à ajouter à la liste de "
                                           "participants \n"))
            except TypeError:
                MessageDErreur.message_d_erreur_d_input_chiffre(self.message_d_erreur)
            confirmation_choix_homonyme = input("Est ce que le choix : \n " +
                                                "[" + str(choix_homonyme) + "] : " +
                                                str(liste_duplicate[choix_homonyme].prenom) + " " +
                                                str(liste_duplicate[choix_homonyme].nom) + " | Date de naissance : " +
                                                str(liste_duplicate[choix_homonyme].date_de_naissance) + " | Sexe : " +
                                                str(liste_duplicate[choix_homonyme].sexe) + " | Classement elo : " +
                                                str(liste_duplicate[choix_homonyme].classement_elo) + "\nEst correct "
                                                                                                      "(Oui/Non)? \n:")
        else:
            return liste_duplicate[choix_homonyme]

    def joueur_inexistant(self):
        """ Annonce que le joueur est inexistant, demande si le joueur doit être créé """
        reponse_creation_joueur = input("Joueur inexistant : Voulez vous créer le joueur? (Oui/Non)")
        return reponse_creation_joueur

    def verification_si_valeur_est_date(self, prompt_recherche):
        """ Vérifie si la valeur saisie est une date """
        date_au_format_ok = False
        while date_au_format_ok is False:
            date_saisie = input("Entrez " + prompt_recherche + " au format JJ/MM/AAAA : \n")
            try:
                datetest = datetime.strptime(date_saisie, "%d/%m/%Y")
                date_au_format_ok = True
                return date_saisie
            except ValueError:
                input("la date n'est pas au bon format. Veuillez réessayer. ")
                date_au_format_ok = False

    def ajout_des_informations_d_un_joueur(self, info_joueur_inexistant):
        """ Récupère les informations d'un joueur à ajouter """
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
