from vue.vue import Vue
from controleur.gestion_de_joueur import GestionDeJoueur
from vue.message_d_erreur import MessageDErreur
from vue.saisie_de_donnees import SaisieDeDonnees
from modele.tournoi import Tournoi


class GestionDeRapport:
    """ Classe gérant les rapports """

    def __init__(self, vue_instance, gestion_joueur, vue_message_d_erreur, vue_saisie_de_donnees):
        """ Crée l'objet joueur """
        self.vue_instance = vue_instance
        self.gestion_joueur = gestion_joueur
        self.vue_message_d_erreur = vue_message_d_erreur
        self.vue_saisie_de_donnees = vue_saisie_de_donnees

    def selection_participants(self, instance_tournoi):
        """ Affiche les participants et demande de saisir l'index du participant à modifier """
        self.affichage_classement_participant_indexee_triee(instance_tournoi, "non")
        choix_index = SaisieDeDonnees.verification_champs_est_nombre(self.vue_saisie_de_donnees,
                                                                     "Merci de sélectionner le joueur à modifier \n :")
        return int(choix_index)

    def choix_classement_elo_ou_alpha(self):
        """ Recupère le choix de l'utilisateur entre un tri alphabétique ou par classement """
        choix_classement = SaisieDeDonnees.recuperation_type_tri_liste_joueur(self.vue_saisie_de_donnees)
        if choix_classement == 1:
            return "nom"
        elif choix_classement == 2:
            return "classement_elo"
        else:
            MessageDErreur.message_d_erreur_option_tri_alpha(self.vue_message_d_erreur)
            MessageDErreur.appuyer_sur_entrer_pour_continuer(self.vue_message_d_erreur)
            return "nom"

    def choix_classement_ou_alphabetique(self):
        """ Recupère le choix de l'utilisateur entre un tri alphabétique ou par classement """
        choix_classement = SaisieDeDonnees.recuperation_type_tri_liste_participant(self.vue_saisie_de_donnees)
        if choix_classement == 1:
            return "nom"
        elif choix_classement == 2:
            return "classement_elo"
        elif choix_classement == 3:
            return "points_tournoi"
        else:
            MessageDErreur.message_d_erreur_option_tri_alpha(self.vue_message_d_erreur)
            MessageDErreur.appuyer_sur_entrer_pour_continuer(self.vue_message_d_erreur)
            return "nom"

    def choix_du_type_de_classement_tournoi(self, instance_de_tournoi):
        """ Methode récupérant le type de tri voulu et renvoyant la liste triée"""
        choix_de_tri = int(self.choix_classement_ou_alphabetique())
        if choix_de_tri == 1:
            return GestionDeJoueur.classement_des_joueurs(self.gestion_joueur, instance_de_tournoi.participants, "nom")
        elif choix_de_tri == 2:
            return GestionDeJoueur.classement_des_joueurs(self.gestion_joueur, instance_de_tournoi.participants,
                                                          "points_tournoi")
        elif choix_de_tri == 3:
            return GestionDeJoueur.classement_des_joueurs(self.gestion_joueur, instance_de_tournoi.participants,
                                                          "points_tournoi")
        else:
            MessageDErreur.message_d_erreur(self.vue_message_d_erreur)

    def affichage_rapport_tours(self, tournaments_table):
        """ Récupère l'id du tournoi dont les tours doivent être affichés puis affiche la liste des tours"""
        try:
            id_tournoi = int(SaisieDeDonnees.recuperation_id_tournoi(self.vue_saisie_de_donnees,
                                                                     "liste des tours.\n:"))
        except TypeError:
            MessageDErreur.message_d_erreur_d_input_chiffre(self.vue_message_d_erreur)
        else:
            resultat_tour = tournaments_table.get(doc_id=id_tournoi)
            Vue.affichage_liste_des_tours(self.vue_instance, resultat_tour)
            MessageDErreur.appuyer_sur_entrer_pour_continuer(self.vue_message_d_erreur)

    def affichage_rapport_matchs(self, tournaments_table, players_table):
        """ Récupère l'id du tournoi dont les matchs doivent être affiché puis lance l'affichage"""
        try:
            id_tournoi = int(SaisieDeDonnees.recuperation_id_tournoi(self.vue_saisie_de_donnees,
                                                                     "liste des matchs.\n:"))
        except TypeError:
            MessageDErreur.message_d_erreur_d_input_chiffre(self.vue_message_d_erreur)
        else:
            resultat_tour = tournaments_table.get(doc_id=id_tournoi)
            Vue.affichage_liste_des_matchs(self.vue_instance, resultat_tour, players_table)
            MessageDErreur.appuyer_sur_entrer_pour_continuer(self.vue_message_d_erreur)

    def affichage_du_classement_db(self, numero_de_ronde_active, players_table, type_tri):
        """ Affiche le classement en fonction des points elo """
        liste_joueur_triee = GestionDeJoueur.classement_des_joueurs_db(self.gestion_joueur, players_table, type_tri)
        Vue.affichage_classement(self.vue_instance, numero_de_ronde_active, liste_joueur_triee)
        MessageDErreur.appuyer_sur_entrer_pour_continuer(self.vue_message_d_erreur)

    def affichage_classement_participant_indexee_triee(self, instance_de_tournoi, tri_oui_non):
        """ Affiche la liste des participants, si besoin triée en fonction du paramètre choisi par
        l'utilisateur"""
        if not isinstance(instance_de_tournoi, Tournoi):
            MessageDErreur.message_d_erreur_tournoi_n_existe_pas(self.vue_message_d_erreur)
        else:
            if tri_oui_non == "oui":
                choix_type_de_tri = self.choix_classement_ou_alphabetique()
                instance_de_tournoi.participants = GestionDeJoueur. \
                    fonction_decorateurs_pour_tri_participants(self.gestion_joueur,
                                                               instance_de_tournoi.participants,
                                                               choix_type_de_tri)
            Vue.affichage_classement_participants(self.vue_instance, len(instance_de_tournoi.rondes),
                                                  instance_de_tournoi.participants)
