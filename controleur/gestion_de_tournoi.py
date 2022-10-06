from modele.tournoi import Tournoi
from modele.joueur import Joueur
import datetime
from controleur.type_de_tournoi import TypeDeTournoi
from tinydb import TinyDB, Query
from vue.vue import Vue
from vue.message_d_erreur import MessageDErreur
from vue.saisie_de_donnees import SaisieDeDonnees
from controleur.gestion_de_joueur import GestionDeJoueur
from controleur.gestion_de_rapport import GestionDeRapport

class GestionDeTournoi:
    """ Classe gérant le tournoi"""

    def __init__(self, vue_instance, objet_gestion_joueur, objet_gestion_rapport, vue_message_d_erreur,
                 vue_saisie_de_donnees):
        """ crée l'objet type de tournoi """
        self.vue_instance = vue_instance
        self.objet_gestion_joueur = objet_gestion_joueur
        self.objet_gestion_rapport = objet_gestion_rapport
        self.vue_message_d_erreur = vue_message_d_erreur
        self.vue_saisie_de_donnees = vue_saisie_de_donnees

    def gestion_du_tournoi(self, liste_joueurs):
        """ Gestion du tournoi en fonction du choix de l'utilisateur"""

        choix_utilisateur = 0
        numero_de_ronde_active = 0
        db = TinyDB('db.json')
        players_table = db.table('players')
        """players_table.truncate()  # clear the table first
        players_table.insert_multiple(serialized_players)
        tournament_table = db.table('tournament')
        tournament_table.truncate()
        tournament_table.insert(serialized_tournament)"""
        while choix_utilisateur != 6:
            choix_utilisateur = int(SaisieDeDonnees.menu(self.vue_saisie_de_donnees))
            if choix_utilisateur == 1:
                # Recuperation des infos participants / tournoi, lancement du tournoi, déroulement du tournoi
                nombre_de_participants = self.recuperation_du_nombre_de_participants()
                if nombre_de_participants == "":
                    MessageDErreur.appuyer_sur_entrer_pour_continuer(self.vue_message_d_erreur)
                else:
                    liste_participants_tournoi = self.selection_des_participants(liste_joueurs, nombre_de_participants)
                    if liste_participants_tournoi == "":
                        print("retour")
                    else:
                        info_instance_tournoi_a_creer = SaisieDeDonnees. \
                            recuperation_des_informations_du_tournoi(self.vue_saisie_de_donnees, nombre_de_participants)
                        print(liste_participants_tournoi)
                        instance_de_tournoi = self.creation_du_tournoi(info_instance_tournoi_a_creer)
                        instance_de_tournoi.participants = liste_participants_tournoi
                        numero_de_ronde_active = 0
            elif choix_utilisateur == 2:
                # Lancement de la ronde suivante
                try:
                    if numero_de_ronde_active < instance_de_tournoi.nombre_de_tour_du_tournoi:
                        numero_de_ronde_active += 1
                        print("le numéro de ronde active est " + str(numero_de_ronde_active) + " sur un total de " +
                              str(instance_de_tournoi.nombre_de_tour_du_tournoi) + "rondes")
                        ronde_actuelle = self.appairage_match_d_une_ronde(numero_de_ronde_active, instance_de_tournoi,
                                                                          "MethodeSuisse")

                        self.depart_d_une_ronde(ronde_actuelle)
                        self.fin_d_une_ronde(ronde_actuelle)
                        instance_de_tournoi.rondes.append(ronde_actuelle)
                    else:
                        MessageDErreur.message_d_erreur_tournoi_termine(self.vue_message_d_erreur)
                except UnboundLocalError:
                    MessageDErreur.message_d_erreur_tournoi_n_existe_pas(self.vue_message_d_erreur)
            elif choix_utilisateur == 3:
                # Ajout d'un joueur
                indice_nouveau_joueur = len(liste_joueurs) + 1
                cle_nouveau_joueur = "player" + str(indice_nouveau_joueur)
                joueur_a_ajouter = GestionDeJoueur.creation_d_un_joueur(self.objet_gestion_joueur, "")
                db.insert(Joueur.serialisation_joueur(joueur_a_ajouter))
                liste_joueurs[cle_nouveau_joueur] = joueur_a_ajouter
            elif choix_utilisateur == 4:
                # Affichage modification du classement elo d'un joueur de la liste
                GestionDeRapport.affichage_du_classement_elo_dict(self.objet_gestion_rapport, liste_joueurs)
                choix_action_sur_liste = SaisieDeDonnees.selection_de_l_action_a_effectuer(self.vue_saisie_de_donnees)
                if str(choix_action_sur_liste) == "Oui":
                    liste_joueurs = GestionDeJoueur.modification_d_un_joueur_dict(self.objet_gestion_joueur,
                                                                                  liste_joueurs)
            elif choix_utilisateur == 5:
                # Affichage modification du classement tournoi d'un participant du tournoi
                try:
                    # Recupere et affiche le classement du tournoi
                    GestionDeRapport.affichage_du_classement_tournoi(self.objet_gestion_rapport, instance_de_tournoi,
                                                                     numero_de_ronde_active)
                except UnboundLocalError:
                    # Renvoi un message d'erreur si aucun tournoi n'existe
                    MessageDErreur.message_d_erreur_tournoi_n_existe_pas(self.vue_message_d_erreur)
                choix_action_sur_liste = SaisieDeDonnees.selection_de_l_action_a_effectuer(self.vue_saisie_de_donnees)
                if str(choix_action_sur_liste) == "Oui":
                    instance_de_tournoi.participants = \
                        GestionDeJoueur.modification_d_un_joueur(self.objet_gestion_joueur,
                                                                 instance_de_tournoi.participants)
            elif choix_utilisateur == 6:
                # Affichage rapports tournoi, des tours d'un tournoi, des matchs d'un tournoi
                print("rapports")

            elif choix_utilisateur == 7:
                # Cas du choix de sortie du programme
                Vue.message_de_sortie_1(self.vue_instance)
            else:
                # Prise en charge du cas ou l'utilisateur entre un chiffre au dela de 6
                MessageDErreur.message_d_erreur_d_input(self.vue_message_d_erreur)
        else:
            Vue.message_de_sortie_2(self.vue_instance)
            # Sortie du programme à la demande de l'utilisateur (choix sortie dans la boucle)

    def recuperation_du_nombre_de_participants(self):
        """Récupere le nombre de participants au tournoi"""
        try:
            nombre_de_participants = int(SaisieDeDonnees.
                                         recuperation_nombre_de_participants_du_tournoi(self.vue_saisie_de_donnees))
            return nombre_de_participants
        except TypeError:
            MessageDErreur.message_d_erreur_d_input_chiffre(self.vue_message_d_erreur)
            return ""

    def selection_des_participants(self, liste_joueurs, nombre_de_participants):
        """ Selection des participants dans le pool de joueurs connus """
        liste_participants = []
        for i in range(nombre_de_participants):
            # Recupere le nom et prénom du joueur à ajouter au tournoi :
            participant = SaisieDeDonnees.recuperation_participant_du_tournoi(self.vue_saisie_de_donnees, i)
            # Recupere le nombre d'entree dans le dictionnaire de liste de joueurs
            nombre_d_entree_dans_le_dictionnaire_de_liste_des_joueurs = len(liste_joueurs)
            # Recrée la clée de la dernière entrée du dictionnaire de joueur
            cle_dernier_nom_entre = "player" + str(nombre_d_entree_dans_le_dictionnaire_de_liste_des_joueurs)
            # Recupère le dernier nom entré dans la liste de joueur
            dernier_nom_entre = liste_joueurs[cle_dernier_nom_entre]
            # Verifie que le joueur est dans la liste de joueur en parcourant toutes les entrées du dictionnaire
            nombre_de_joueur_dans_la_liste = len(liste_joueurs)
            for j in range(nombre_de_joueur_dans_la_liste):
                if j < 9:
                    joueur_de_la_liste = liste_joueurs["player0"+str(j+1)]
                else:
                    joueur_de_la_liste = liste_joueurs["player"+str(j+1)]
                # Vérifie si le prenom et nom entrée par l'utilisateur fait partie de la liste de joueurs
                test_presence = self.verification_participant_est_dans_liste_joueurs(participant, joueur_de_la_liste)
                # Si le test est concluant, ajoute le joueur de la liste de joueurs à la liste de participants
                if test_presence == "Presence":
                    joueur_de_la_liste.points_tournoi = 0
                    print("joueur ajouté : " + str(joueur_de_la_liste))
                    liste_participants.append(joueur_de_la_liste)
                    print(liste_participants)
                    break
                else:
                    # Sinon, vérifie si la valeur testée est la dernière valeur du dictionnaire
                    if str(joueur_de_la_liste.nom) == str(dernier_nom_entre.nom):
                        # Si oui, Cela indique que le joueur n'existe pas, demande à l'utilisateur s'il veut le créer
                        reponse_creation_joueur = SaisieDeDonnees.joueur_inexistant(self.vue_saisie_de_donnees)
                        if reponse_creation_joueur == "Oui":
                            # Si oui, Crée un joueur en récupérant les informations Noms/Prenom entrées préalablement
                            joueur_a_ajouter = GestionDeJoueur.creation_d_un_joueur(self.objet_gestion_joueur,
                                                                                    participant)
                            # Ajout ce joueur à la liste des participants
                            liste_participants.append(joueur_a_ajouter)
                            # Ajout de ce joueur à la liste des joueurs
                            liste_joueurs = GestionDeJoueur.ajout_d_un_joueur_a_la_liste(self.objet_gestion_joueur,
                                                                                         joueur_a_ajouter,
                                                                                         liste_joueurs)
                            nombre_de_joueur_dans_la_liste += 1
                        else:
                            MessageDErreur.message_de_demande_recommencer_ajout_joueur(self.vue_message_d_erreur)
                            return ""
        return liste_participants

    def verification_participant_est_dans_liste_joueurs(self, participant, joueur_de_la_liste):
        """ Verifie si un couple Nom / Prenom se trouve dans la liste des objets joueurs """
        if ((str(participant["Nom"])) in joueur_de_la_liste.nom) and ((str(participant["Prenom"])) in
                                                                      joueur_de_la_liste.prenom):
            return "Presence"
        else:
            return "Absence"


    def creation_du_tournoi(self, info_tournoi):
        """ Creation d'un tournoi en utilisant les paramètres utilisateurs"""
        # Creation d'un objet tournoi avec les informations récupérées par la Vue
        instance_de_tournoi = Tournoi(info_tournoi["nom_du_tournoi"],
                                      info_tournoi["lieu_du_tournoi"],
                                      info_tournoi["date_de_tournoi"],
                                      info_tournoi["type_de_controle_du_temps"],
                                      info_tournoi["nombre_de_participant"],
                                      info_tournoi["nombre_de_tour"],
                                      info_tournoi["commentaires"])
        return instance_de_tournoi

    def appairage_match_d_une_ronde(self, numero_de_ronde, instance_de_tournoi, type_de_tournoi):
        """ Mécanisme de fonctionnement d'une ronde"""
        # Creation de l'objet instancié tournoi nécessaire
        objet_type_de_tournoi = TypeDeTournoi()
        ronde_actuelle = TypeDeTournoi.choix_type_tournoi(objet_type_de_tournoi, type_de_tournoi, numero_de_ronde,
                                                          instance_de_tournoi)
        # pour chaque match de la liste des matchs de la ronde
        for match_de_ronde in ronde_actuelle.liste_matchs:
            self.affichage_des_matchs(match_de_ronde)
        return ronde_actuelle


    def affichage_des_matchs(self, instance_de_match):
        """ Affiche le match en argument """
        Vue.affichage_des_matchs(self.vue_instance, instance_de_match)


    def depart_d_une_ronde(self, ronde_a_lancer):
        """ lance une ronde """
        SaisieDeDonnees.depart_de_la_ronde(self.vue_saisie_de_donnees)
        ronde_a_lancer.date_heure_debut_du_match = datetime.datetime.now()
        return ronde_a_lancer

    def fin_d_une_ronde(self, ronde_a_clore):
        """ Clos une ronde et saisie les resultats"""
        SaisieDeDonnees.fin_de_la_ronde(self.vue_saisie_de_donnees)
        for match_de_ronde in ronde_a_clore.liste_matchs:
            resultat_du_match = SaisieDeDonnees.recuperation_des_resultats_d_un_match(self.vue_saisie_de_donnees,
                                                                                      match_de_ronde)
            while resultat_du_match not in ["1", "2", "N"]:
                MessageDErreur.message_d_erreur(self.vue_message_d_erreur)
            else:
                if resultat_du_match == "1":
                    verification_resultat_saisie = \
                        SaisieDeDonnees.verification_resultat_match_avec_vainqueur(self.vue_saisie_de_donnees,
                                                                                   match_de_ronde.joueur1,
                                                                                   match_de_ronde.joueur2)
                    while str(verification_resultat_saisie) != "OK":
                        verification_resultat_saisie = \
                            SaisieDeDonnees.verification_resultat_match_avec_vainqueur(self.vue_saisie_de_donnees,
                                                                                       match_de_ronde.joueur1,
                                                                                       match_de_ronde.joueur2)
                    else:
                        match_de_ronde.resultat_joueur1 = 1
                        match_de_ronde.joueur1.points_tournoi += 1
                        match_de_ronde.resultat_joueur2 = 0
                        ronde_a_clore.date_heure_fin_du_match = datetime.datetime.now()
                elif resultat_du_match == "2":
                    verification_resultat_saisie = \
                        SaisieDeDonnees.verification_resultat_match_avec_vainqueur(self.vue_saisie_de_donnees,
                                                                                   match_de_ronde.joueur2,
                                                                                   match_de_ronde.joueur1)
                    while verification_resultat_saisie != "OK":
                        verification_resultat_saisie = \
                            SaisieDeDonnees.verification_resultat_match_avec_vainqueur(self.vue_saisie_de_donnees,
                                                                                       match_de_ronde.joueur2,
                                                                                       match_de_ronde.joueur1)
                    else:
                        match_de_ronde.resultat_joueur2 = 1
                        match_de_ronde.joueur2.points_tournoi += 1
                        match_de_ronde.resultat_joueur1 = 0
                        ronde_a_clore.date_heure_fin_du_match = datetime.datetime.now()
                elif resultat_du_match == "N":
                    verification_resultat_saisie = SaisieDeDonnees.\
                        verification_resultat_match_nul(self.vue_saisie_de_donnees, match_de_ronde.joueur1,
                                                        match_de_ronde.joueur2)
                    while verification_resultat_saisie != "OK":
                        verification_resultat_saisie = SaisieDeDonnees.\
                            verification_resultat_match_nul(self.vue_saisie_de_donnees, match_de_ronde.joueur1,
                                                            match_de_ronde.joueur2)
                    else:
                        match_de_ronde.resultat_joueur2 = 0.5
                        match_de_ronde.joueur1.points_tournoi += 0.5
                        match_de_ronde.resultat_joueur1 = 0.5
                        match_de_ronde.joueur2.points_tournoi += 0.5
                        ronde_a_clore.date_heure_fin_du_match = datetime.datetime.now()

        return ronde_a_clore

