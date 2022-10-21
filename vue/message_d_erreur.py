

class MessageDErreur:
    """ Vue du tournoi d'échec gérant les messages d'erreur """

    def __init__(self):
        """ Initialise un objet message d'erreur """

    def message_d_erreur_tournoi_n_existe_pas(self):
        """ Affiche un message d'erreur indiquant que l'option n'est pas disponible """
        print("Option indisponible, aucun tournoi en cours")
        self.appuyer_sur_entrer_pour_continuer()

    def message_d_erreur_tournoi_termine(self):
        """ Affiche un message d'erreur indiquant que le tournoi est terminé """
        print("Option indisponible, le tournoi est terminé")
        self.appuyer_sur_entrer_pour_continuer()

    def message_d_erreur_option_tri_alpha(self):
        """ Affiche un message d'erreur indiquant que le choix n'est pas valide et que le tri va se faire
        alphabétiquement par défaut """
        print("Option non reconnu, le tri est fait Alphabétiquement par défaut... \n")

    def appuyer_sur_entrer_pour_continuer(self):
        """ Affiche la demande d'appuyer sur Entrer pour continuer """
        input("Appuyer sur Entrer pour continuer... \n")

    def message_d_erreur(self):
        """ Affiche un message d'erreur générique """
        print("il y a eut une erreur. \n")

    def message_d_erreur_d_input_chiffre(self):
        """ Affiche un message d'erreur, car l'utilisateur n'a pas entré un chiffre """
        input(" L'entrée n'était pas un nombre. Merci d'entrer un nombre")

    def message_d_erreur_d_input(self):
        """ Affiche un message d'erreur, car l'utilisateur a entré un chiffre en dehors des options proposées """
        print("Merci de taper un chiffre entre 1 et 6 à l'affichage du menu")

    def message_d_erreur_d_input_hors_choix(self):
        """Affiche un message quand le chiffre entre ne correspond pas à un choix possible """
        print("Choix non reconnu. Merci de rentrer un chiffre correspondant aux options données.")

    def message_de_demande_recommencer_ajout_joueur(self):
        """ Demande à l'utilisateur de recommencer la création du tournoi """
        print("Merci de recommencer la création du tournoi\n")

    def message_aucune_information_entree(self):
        """ Informe l'utilisateur que rien n'a été saisie, Demande à l'utilisateur d'entrer la donnée demandée """
        print("Aucune information n'a été saisie. Merci de saisir l'information demandée.")

    def message_aucun_choix_entre(self):
        """ Informe l'utilisateur que rien n'a été saisie, Demande à l'utilisateur d'entrer la donnée demandée """
        print("Aucun choix n'a été saisi. Merci de saisir votre choix.")

    def message_type_tournoi_non_pris_en_charge(self):
        print("Type de tournoi non pris en charge...")
