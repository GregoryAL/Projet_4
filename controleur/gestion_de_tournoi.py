from modele.tournoi import Tournoi
from modele.joueur import Joueur
from modele.ronde import Ronde
from modele.match import Match
from datetime import datetime
from controleur.type_de_tournoi import TypeDeTournoi
from tinydb import Query
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

    def gestion_du_tournoi(self, liste_joueurs, players_table, tournaments_table):
        """ Gestion du tournoi en fonction du choix de l'utilisateur"""
        try:
            choix_utilisateur = 0
            numero_de_ronde_active = 0
            choix_type_tournoi = ""
            while choix_utilisateur != 6:
                choix_utilisateur = int(SaisieDeDonnees.menu(self.vue_saisie_de_donnees))
                if choix_utilisateur == 1:
                    numero_de_ronde_active = 0
                    # Recupere le type de tournoi qui sera lancé (Ex: Suisse)
                    choix_type_tournoi = SaisieDeDonnees.recuperation_choix_type_tournoi(self.vue_saisie_de_donnees)
                    # Recuperation des infos participants / tournoi, lancement du tournoi, déroulement du tournoi
                    instance_de_tournoi = self.initialisation_tournoi(players_table, tournaments_table)
                elif choix_utilisateur == 2:
                    # Lancement de la ronde suivante
                    try:
                        numero_de_ronde_active += 1
                        ronde = self.initialisation_ronde(numero_de_ronde_active, instance_de_tournoi, players_table,
                                                          choix_type_tournoi, tournaments_table)
                        instance_de_tournoi.rondes.append(ronde)
                    except UnboundLocalError:
                        MessageDErreur.message_d_erreur_tournoi_n_existe_pas(self.vue_message_d_erreur)
                elif choix_utilisateur == 3:
                    # Ajout d'un joueur
                    joueur_a_ajouter = GestionDeJoueur.creation_d_un_joueur(self.objet_gestion_joueur, "")
                    GestionDeJoueur.ajout_joueur_db(self.objet_gestion_joueur, joueur_a_ajouter, players_table)
                elif choix_utilisateur == 4:
                    # Modification d'un joueur / participant
                    base_a_modifier = int(SaisieDeDonnees.selection_base_a_modifier(self.vue_saisie_de_donnees))
                    if base_a_modifier == 1:
                        joueur_a_modifier = SaisieDeDonnees.selection_joueur_a_modifier(self.vue_saisie_de_donnees)
                        joueur_a_modifier_complet = GestionDeJoueur.recherche_correspondance_db(self.objet_gestion_joueur,
                                                                                    players_table, joueur_a_modifier)
                        print(joueur_a_modifier_complet)
                        parametre_a_modifier = GestionDeJoueur.\
                            recuperation_du_parametre_a_modifier_db(self.objet_gestion_joueur)
                        nouvelle_valeur_parametre = SaisieDeDonnees.\
                            entree_nouvelle_valeur_parametre(self.vue_saisie_de_donnees, parametre_a_modifier)
                        GestionDeJoueur.modification_d_un_joueur_db(self.objet_gestion_joueur, players_table, joueur_a_modifier_complet,
                                                                    parametre_a_modifier, nouvelle_valeur_parametre)
                    elif base_a_modifier == 2:
                        try:
                            print(instance_de_tournoi.nom_du_tournoi)
                            joueur_a_modifier = SaisieDeDonnees.selection_joueur_a_modifier(self.vue_saisie_de_donnees)
                            doc_id_joueur = GestionDeJoueur.recherche_correspondance_db(self.objet_gestion_joueur,
                                                                                        players_table,joueur_a_modifier,
                                                                                        tournaments_table)
                        except UnboundLocalError:
                            # Renvoi un message d'erreur si aucun tournoi n'existe
                            MessageDErreur.message_d_erreur_tournoi_n_existe_pas(self.vue_message_d_erreur)
                elif choix_utilisateur == 5:
                    # Affichage rapports tournoi, des tours d'un tournoi, des matchs d'un tournoi
                    try:
                        self.menu_rapport(players_table, tournaments_table, numero_de_ronde_active, instance_de_tournoi)
                    except UnboundLocalError :
                        self.menu_rapport_light(players_table, tournaments_table, numero_de_ronde_active)
                elif choix_utilisateur == 6:
                    # Cas du choix de sortie du programme
                    Vue.message_de_sortie_1(self.vue_instance)
                elif choix_utilisateur == 7:
                    testboucle = "No"
                    #while testboucle != "Yes":
                    valeurtest = input("quelle est la date à tester")
                    try:
                        datetest = datetime.strptime(valeurtest, "%d/%m/%Y")
                        testboucle = "Yes"
                        input("gagne")
                    except ValueError:
                        input("rate")
                        testboucle = "No"
                    input("sortie de 7")
                else:
                    # Prise en charge du cas ou l'utilisateur entre un chiffre au dela des choix
                    MessageDErreur.message_d_erreur_d_input(self.vue_message_d_erreur)
            else:
                Vue.message_de_sortie_2(self.vue_instance)
                # Sortie du programme à la demande de l'utilisateur (choix sortie dans la boucle)
        except ValueError:
            MessageDErreur.message_d_erreur_d_input_chiffre(self.vue_message_d_erreur)
            self.gestion_du_tournoi(liste_joueurs, players_table, tournaments_table)
        except TypeError:
            MessageDErreur.message_d_erreur_d_input(self.vue_message_d_erreur)
            self.gestion_du_tournoi(liste_joueurs, players_table, tournaments_table)

    def menu_rapport_light(self, players_table, tournaments_table, numero_de_ronde_active):
        """ menu du choix de quel rapport afficher, version light, s'affiche lorsque aucun tournoi n'est en cours"""
        # Initialise la variable récupérant le choix utilisateur
        choix_rapport = 0
        # Gere la sortie du menu
        while choix_rapport != 5:
            # Recupere le choix utilisateur
            choix_rapport = int(SaisieDeDonnees.menu_rapport_light(self.vue_saisie_de_donnees))
            if choix_rapport == 1:
                # Affiche la liste des joueurs
                choix_type_tri = GestionDeRapport.choix_classement_ou_alphabetique(self.objet_gestion_rapport)
                GestionDeRapport.affichage_du_classement_db(self.objet_gestion_rapport, "",
                                                            players_table, choix_type_tri)
            elif choix_rapport == 2:
                # Affiche la liste des tournois
                Vue.affichage_liste_de_tournoi(self.vue_instance, tournaments_table)
                input()
            elif choix_rapport == 3:
                # Affiche la liste des tours d'un tournoi
                Vue.affichage_liste_de_tournoi(self.vue_instance, tournaments_table)
                GestionDeRapport.affichage_rapport_tours(self.objet_gestion_rapport, tournaments_table)
            elif choix_rapport == 4:
                # Affiche la liste des matchs d'un tournoi
                Vue.affichage_liste_de_tournoi(self.vue_instance, tournaments_table)
                GestionDeRapport.affichage_rapport_matchs(self.objet_gestion_rapport, tournaments_table, players_table)
            elif choix_rapport == 5:
                # sort du sous menu rapport
                print("en construction...")
            else:
                # gere le cas ou le choix entré n'est pas dans la liste des choix disponibles.
                MessageDErreur.message_d_erreur_d_input(self.vue_message_d_erreur)

    def menu_rapport(self, players_table, tournaments_table, numero_de_ronde_active, instance_de_tournoi):
        """ menu du choix de quel rapport afficher, complet, s'affiche lorsqu'un tournoi est en cours"""
        # Initialise la variable récupérant le choix utilisateur
        choix_rapport = 0
        # Gere la sortie du menu
        while choix_rapport != 6:
            # Recupere le choix utilisateur
            choix_rapport = int(SaisieDeDonnees.menu_rapport(self.vue_saisie_de_donnees))
            if choix_rapport == 1:
                # Affiche la liste des joueurs
                choix_type_tri = GestionDeRapport.choix_classement_ou_alphabetique(self.objet_gestion_rapport)
                GestionDeRapport.affichage_du_classement_db(self.objet_gestion_rapport, "",
                                                            players_table, choix_type_tri)
            elif choix_rapport == 2:
                # Affiche la liste des participants
                try:
                    test_instance_tournoi = instance_de_tournoi.nom_du_tournoi
                except AttributeError:
                    MessageDErreur.message_d_erreur_tournoi_n_existe_pas(self.vue_message_d_erreur)
                else:
                    choix_type_de_tri = GestionDeRapport.choix_classement_ou_alphabetique(self.objet_gestion_rapport)
                    instance_de_tournoi.participants = GestionDeJoueur. \
                        fonction_decorateurs_pour_tri_participants(self.objet_gestion_joueur,
                                                                   instance_de_tournoi.participants,
                                                                   choix_type_de_tri)
                    Vue.affichage_classement_participants(self.vue_instance, numero_de_ronde_active,
                                                          instance_de_tournoi.participants)
                    input()
            elif choix_rapport == 3:
                # Affiche la liste des tournois
                Vue.affichage_liste_de_tournoi(self.vue_instance, tournaments_table)
                input()
            elif choix_rapport == 4:
                # Affiche la liste des tours d'un tournoi
                Vue.affichage_liste_de_tournoi(self.vue_instance, tournaments_table)
                GestionDeRapport.affichage_rapport_tours(self.objet_gestion_rapport, tournaments_table)
            elif choix_rapport == 5:
                # Affiche la liste des matchs d'un tournoi
                Vue.affichage_liste_de_tournoi(self.vue_instance, tournaments_table)
                GestionDeRapport.affichage_rapport_matchs(self.objet_gestion_rapport, tournaments_table, players_table)
            elif choix_rapport == 6:
                # sort du sous menu rapport
                Vue.message_de_sortie_3(self.vue_instance)
            else:
                # gere le cas ou le choix entré n'est pas dans la liste des choix disponibles.
                MessageDErreur.message_d_erreur_d_input(self.vue_message_d_erreur)

    def recuperation_du_nombre_de_participants(self):
        """Récupere le nombre de participants au tournoi"""

        nombre_de_participants = SaisieDeDonnees.\
            recuperation_nombre_de_participants_du_tournoi(self.vue_saisie_de_donnees)
        return nombre_de_participants


    def selection_des_participants_db(self, players_table, nombre_de_participants):
        """ Selection des participants dans le pool de joueurs connus de la base table_players"""
        liste_participants = []
        for i in range(nombre_de_participants):
            # Recupere le nom et prénom du joueur à ajouter au tournoi :
            participant_nom_prenom = SaisieDeDonnees.recuperation_participant_du_tournoi(self.vue_saisie_de_donnees, i)
            participant = GestionDeJoueur.recherche_correspondance_db(self.objet_gestion_joueur, players_table,
                                                                      participant_nom_prenom)
            if participant == "":
                MessageDErreur.message_de_demande_recommencer_ajout_joueur(self.vue_message_d_erreur)
                MessageDErreur.appuyer_sur_entrer_pour_continuer(self.vue_message_d_erreur)
                return ""
            else:
                liste_participants.append([Joueur(participant["nom"], participant["prenom"],
                                          participant["date_de_naissance"], participant["sexe"],
                                          participant["classement_elo"]), 0])
        return liste_participants

    def verification_participant_est_dans_liste_joueurs(self, participant, joueur_de_la_liste):
        """ Verifie si un couple Nom / Prenom se trouve dans la liste des objets joueurs """
        if (participant["Nom"] == joueur_de_la_liste.nom) and (participant["Prenom"] == joueur_de_la_liste.prenom):
            return "Presence"
        else:
            return "Absence"

    def verification_duplicate_joueurs(self, liste_duplicate):
        """ Affiche la liste des homonymes et recupere la selection de l'utilisateur """
        Vue.affichage_duplicate(self.vue_instance, liste_duplicate)
        return SaisieDeDonnees.selection_duplicate(self.vue_saisie_de_donnees, liste_duplicate)

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
        objet_type_de_tournoi = TypeDeTournoi(self.objet_gestion_joueur)
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
        objet_date_heure_debut_ronde = datetime.now()
        ronde_a_lancer.date_heure_debut_de_ronde = str(objet_date_heure_debut_ronde.strftime("%d/%m/%Y %H:%M:%S"))
        return ronde_a_lancer

    def fin_d_une_ronde(self, ronde_a_clore, instance_tournoi):
        """ Clos une ronde et saisie les resultats"""
        SaisieDeDonnees.fin_de_la_ronde(self.vue_saisie_de_donnees)
        objet_date_heure_fin_ronde = datetime.now()
        ronde_a_clore.date_heure_fin_de_ronde = str(objet_date_heure_fin_ronde.strftime("%d/%m/%Y %H:%M:%S"))
        for match_de_ronde in ronde_a_clore.liste_matchs:
            resultat_du_match = SaisieDeDonnees.recuperation_des_resultats_d_un_match(self.vue_saisie_de_donnees,
                                                                                      match_de_ronde)
            while resultat_du_match not in ["1", "2", "N"]:
                MessageDErreur.message_d_erreur(self.vue_message_d_erreur)
                resultat_du_match = SaisieDeDonnees.recuperation_des_resultats_d_un_match(self.vue_saisie_de_donnees,
                                                                                          match_de_ronde)
            else:
                if resultat_du_match == "1":
                    match_de_ronde.resultat_joueur1 = 1
                    match_de_ronde.joueur1[1] += 1
                    match_de_ronde.joueur2[1] += 0
                    match_de_ronde.resultat_joueur2 = 0
                elif resultat_du_match == "2":
                    match_de_ronde.resultat_joueur2 = 1
                    match_de_ronde.joueur2[1] += 1
                    match_de_ronde.joueur1[1] += 0
                    match_de_ronde.resultat_joueur1 = 0
                elif resultat_du_match == "N":
                    match_de_ronde.resultat_joueur2 = 0.5
                    match_de_ronde.joueur1[1] += 0.5
                    match_de_ronde.resultat_joueur1 = 0.5
                    match_de_ronde.joueur2[1] += 0.5
        return ronde_a_clore

    def initialisation_tournoi(self, players_table, tournaments_table):
        # Recuperation des infos participants / tournoi, lancement du tournoi, déroulement du tournoi
        nombre_de_participants = SaisieDeDonnees.verification_champs_est_nombre(self.vue_saisie_de_donnees,
                                                                                "Veuillez entrez le nombre "
                                                                                "de participants : \n")
        liste_participants_tournoi = self.selection_des_participants_db(players_table, nombre_de_participants)
        if len(liste_participants_tournoi) == nombre_de_participants:
            info_instance_tournoi_a_creer = SaisieDeDonnees.\
                recuperation_des_informations_du_tournoi(self.vue_saisie_de_donnees)
            info_instance_tournoi_a_creer["nombre_de_participant"] = nombre_de_participants
            instance_de_tournoi = self.creation_du_tournoi(info_instance_tournoi_a_creer)
            tournaments_table.insert(Tournoi.serialisation_tournoi(instance_de_tournoi))
            instance_de_tournoi.participants = liste_participants_tournoi
            participants_db = []
            for participants in liste_participants_tournoi:
                participants_db.append(Joueur.serialisation_joueur(participants[0]))
            tournoi = Query()
            tournaments_table.update({"participants": participants_db}, tournoi.
                                      nom == instance_de_tournoi.nom_du_tournoi)
            return instance_de_tournoi
        else:
            MessageDErreur.message_d_erreur(self.vue_message_d_erreur)
            return ""

    def initialisation_ronde(self, numero_de_ronde_active, instance_de_tournoi, players_table, choix_type_tournoi,
                             tournaments_table):
        # Lancement de la ronde suivante
        if int(numero_de_ronde_active) <= int(instance_de_tournoi.nombre_de_tour_du_tournoi):
            ronde_actuelle = self.appairage_match_d_une_ronde(numero_de_ronde_active, instance_de_tournoi,
                                                              choix_type_tournoi)
            ronde_actuelle = self.depart_d_une_ronde(ronde_actuelle)
            ronde_actuelle = self.fin_d_une_ronde(ronde_actuelle, instance_de_tournoi)
            if int(numero_de_ronde_active == int(instance_de_tournoi.nombre_de_tour_du_tournoi)):
                self.recuperation_ronde_db(ronde_actuelle, instance_de_tournoi, tournaments_table, players_table,
                                           numero_de_ronde_active)

            return ronde_actuelle
        else:
            MessageDErreur.message_d_erreur_tournoi_termine(self.vue_message_d_erreur)
            input()

    def serialisation_ronde_objet(self, rondes, players_table):
        """ serialise tous les objets contenus dans une ronde"""
        liste_match_serialized = []
        for match in rondes.liste_matchs:
            recherche = Query()
            match_serialized = Match.serialisation_match(match)
            resultat_rech_joueur1_dans_table = players_table.search((recherche.nom == match.joueur1[0].nom) &
                                                               (recherche.prenom == match.joueur1[0].prenom) &
                                                               (recherche.date_de_naissance ==
                                                                match.joueur1[0].date_de_naissance) &
                                                               (recherche.sexe == match.joueur1[0].sexe) &
                                                               (recherche.classement_elo == match.joueur1[0].
                                                                classement_elo))

            match_serialized["joueur1"] = resultat_rech_joueur1_dans_table[0].doc_id
            match_serialized["joueur2"] = (players_table.search((recherche.nom == match.joueur2[0].nom) &
                                                               (recherche.prenom == match.joueur2[0].prenom) &
                                                               (recherche.date_de_naissance ==
                                                                match.joueur2[0].date_de_naissance) &
                                                               (recherche.sexe == match.joueur2[0].sexe) &
                                                               (recherche.classement_elo == match.joueur2[0].
                                                                classement_elo)))[0].doc_id
            match_serialized["tuple_match"] = ([match_serialized["joueur1"], match_serialized["resultat_joueur1"]],
                                               [match_serialized["joueur2"], match_serialized["resultat_joueur2"]])
            liste_match_serialized.append(match_serialized)
        ronde_serial = Ronde.serialisation_ronde(rondes)
        ronde_serial["liste_match"] = liste_match_serialized
        return ronde_serial


    def recuperation_ronde_db(self, rondes, instance_de_tournoi, tournaments_table, players_table, ronde_active):
        """ serialise la ronde, la stock dans la base tournaments, puis reserialise """
        liste_ronde_serial = []
        if ronde_active > 1:
            for ronde in instance_de_tournoi.rondes:
                liste_ronde_serial.append(self.serialisation_ronde_objet(ronde, players_table))
        serial_ronde = self.serialisation_ronde_objet(rondes, players_table)
        liste_ronde_serial.append(serial_ronde)
        tournoi = Query()
        tournaments_table.update({"rondes": liste_ronde_serial}, (tournoi.nom == instance_de_tournoi.nom_du_tournoi))
        # ronde = self.deserialisation_ronde(ronde)
