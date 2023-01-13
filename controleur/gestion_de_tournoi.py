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
        """ Crée l'objet type de tournoi """
        # Récupère les objets initialisateur des classes qui seront utilisées
        self.vue_instance = vue_instance
        self.objet_gestion_joueur = objet_gestion_joueur
        self.objet_gestion_rapport = objet_gestion_rapport
        self.vue_message_d_erreur = vue_message_d_erreur
        self.vue_saisie_de_donnees = vue_saisie_de_donnees

    def gestion_du_tournoi(self, players_table, tournaments_table):
        """ Gestion du tournoi en fonction du choix de l'utilisateur"""
        # Initialise les variables qui seront utilisées dans la boucle de gestion de tournoi
        sortie_tournoi = "Non"
        instance_de_tournoi = "Aucun"
        numero_de_ronde_active = 0
        choix_utilisateur = 0
        choix_type_tournoi = ""
        # Lance la boucle gérant le menu principal du tournoi
        while sortie_tournoi == "Non":
            try:
                # Tant que l'utilisateur ne signale pas vouloir sortir du programme en saisissant 6 quand le menu
                # s'affiche, reste dans la boucle du menu principal du tournoi.
                while choix_utilisateur != 8:
                    # Appel la vue proposant les choix disponibles dans le menu principal et récupère le choix
                    # utilisateur.
                    choix_utilisateur = int(SaisieDeDonnees.menu(self.vue_saisie_de_donnees))
                    # Création du tournoi
                    if choix_utilisateur == 1:
                        numero_de_ronde_active = 0
                        # Récupère le type de tournoi qui sera lancé (Ex : Suisse)
                        choix_type_tournoi = SaisieDeDonnees.\
                            recuperation_choix_type_tournoi(self.vue_saisie_de_donnees)
                        # Recuperation des infos participants / tournoi, lancement du tournoi, déroulement du tournoi
                        instance_de_tournoi = self.initialisation_tournoi(players_table, tournaments_table)
                    # Chargement d'un tournoi
                    if choix_utilisateur == 2:
                        id_tournoi_a_reprendre = SaisieDeDonnees.\
                            recuperation_tournoi_a_terminer(self.vue_saisie_de_donnees, tournaments_table)
                        input("\n Le tournoi à reprendre est le : " + str(id_tournoi_a_reprendre))
                        instance_de_tournoi = self.instanciation_tournoi_db(id_tournoi_a_reprendre, tournaments_table)
                        numero_de_ronde_active = len(instance_de_tournoi.rondes)
                    # Lancement de la ronde suivante
                    elif choix_utilisateur == 3:
                        # Test si un tournoi est en cours et renvoi un message d'erreur le cas contraire
                        if not isinstance(instance_de_tournoi, Tournoi):
                            MessageDErreur.message_d_erreur_tournoi_n_existe_pas(self.vue_message_d_erreur)
                        else:
                            # Incrémente le numéro de la ronde de 1
                            numero_de_ronde_active += 1
                            # Lance le déroulement de la ronde
                            ronde = self.initialisation_ronde(numero_de_ronde_active, instance_de_tournoi,
                                                              players_table, choix_type_tournoi, tournaments_table)
                            # Ajout les informations de la ronde à l'instance de tournoi en cours
                            instance_de_tournoi.rondes.append(ronde)
                    # Enregistre le tournoi en cours
                    elif choix_utilisateur == 4:
                        # Test si un tournoi est en cours et renvoi un message d'erreur le cas contraire
                        if not isinstance(instance_de_tournoi, Tournoi):
                            MessageDErreur.message_d_erreur_tournoi_n_existe_pas(self.vue_message_d_erreur)
                        else:
                            # Inscrit les informations de toutes les rondes en DB
                            if numero_de_ronde_active >= 1:
                                self.recuperation_ronde_db(ronde, instance_de_tournoi, tournaments_table, players_table,
                                                           numero_de_ronde_active)
                            Vue.enregistrement_de_tournoi_ok(self.vue_instance)
                            MessageDErreur.appuyer_sur_entrer_pour_continuer(self.vue_message_d_erreur)
                            numero_de_ronde_active = 0
                            instance_de_tournoi = []
                            ronde = []
                    # Ajoute un joueur dans la base des joueurs
                    elif choix_utilisateur == 5:
                        # Ajout d'un joueur
                        joueur_a_ajouter = GestionDeJoueur.creation_d_un_joueur(self.objet_gestion_joueur, "")
                        GestionDeJoueur.ajout_joueur_db(self.objet_gestion_joueur, joueur_a_ajouter, players_table)
                    # Modifie un paramètre d'un joueur ou d'un participant
                    elif choix_utilisateur == 6:
                        # Demande à l'utilisateur de sélectionner si c'est un joueur de la base joueur ou un
                        # participant du tournoi à modifier
                        base_a_modifier = int(SaisieDeDonnees.selection_base_a_modifier(self.vue_saisie_de_donnees))
                        # Cas où c'est un joueur à modifier
                        if base_a_modifier == 1:
                            self.modification_du_joueur_dans_db_player(players_table)
                        # Cas où c'est un participant à modifier
                        elif base_a_modifier == 2:
                            instance_de_tournoi = self.modification_du_participant_dans_instance_tournoi(
                                instance_de_tournoi)
                    # Affichage rapports joueurs, participants, tournoi, tours d'un tournoi, matchs d'un tournoi
                    elif choix_utilisateur == 7:
                        # Vérifie si un tournoi est en cours et affiche un menu des rapports disponibles réduit
                        # (sans la liste des participants) si ce n'est pas le cas
                        if not isinstance(instance_de_tournoi, Tournoi):
                            self.menu_rapport_light(players_table, tournaments_table)
                        else:
                            self.menu_rapport(players_table, tournaments_table, instance_de_tournoi)
                    # Sortie du programme
                    elif choix_utilisateur == 8:
                        # Affiche un message de sortie
                        Vue.message_de_sortie_1(self.vue_instance)
                    else:
                        # Prise en charge du cas ou l'utilisateur entre un chiffre au dela des choix
                        MessageDErreur.message_d_erreur_d_input(self.vue_message_d_erreur)
                else:
                    Vue.message_de_sortie_2(self.vue_instance)
                    # Sortie du programme à la demande de l'utilisateur (choix sortie dans la boucle)
                    sortie_tournoi = "Oui"
            # Gère les cas où l'utilisateur saisi une donnée qui ne correspond pas aux choix proposés
            except ValueError:
                MessageDErreur.message_d_erreur_d_input_chiffre(self.vue_message_d_erreur)
                sortie_tournoi = "Non"
            except TypeError:
                MessageDErreur.message_d_erreur_d_input(self.vue_message_d_erreur)
                sortie_tournoi = "Non"

    def modification_du_joueur_dans_db_player(self, players_table):
        """ Choisi un joueur à modifier, puis change le paramètre désiré dans players_base"""
        # Demande au joueur de rentrer le nom et prénom du joueur à modifier dans la base
        joueur_a_modifier = SaisieDeDonnees.selection_joueur_a_modifier(self.vue_saisie_de_donnees)
        # Récupère les joueurs correspondants à ces nom/prénom dans la base et demande à l'utilisateur de choisir le
        # joueur désiré en cas d'homonyme
        joueur_a_modifier_complet = GestionDeJoueur.recherche_correspondance_db(self.objet_gestion_joueur,
                                                                                players_table, joueur_a_modifier)
        # Récupère le type du paramètre que l'utilisateur souhaite modifier
        parametre_a_modifier = GestionDeJoueur. \
            recuperation_du_parametre_a_modifier_db_joueur(self.objet_gestion_joueur)
        # Récupère la nouvelle valeur du paramètre à modifier
        nouvelle_valeur_parametre = SaisieDeDonnees. \
            entree_nouvelle_valeur_parametre(self.vue_saisie_de_donnees, parametre_a_modifier)
        # Fais la modification du paramètre dans la base
        GestionDeJoueur.modification_d_un_joueur_db(self.objet_gestion_joueur, players_table,
                                                    joueur_a_modifier_complet, parametre_a_modifier,
                                                    nouvelle_valeur_parametre)

    def modification_du_participant_dans_instance_tournoi(self, instance_de_tournoi):
        """ Choisi un participant à modifier, puis change le paramètre désire dans la liste des participants de l'objet
        instance_de_tournoi.participants"""
        # Vérifie qu'un tournoi est en cours
        if not isinstance(instance_de_tournoi, Tournoi):
            MessageDErreur.message_d_erreur_tournoi_n_existe_pas(self.vue_message_d_erreur)
        else:
            # Affiche le nom du tournoi
            Vue.affichage_du_nom_du_tournoi(self.vue_instance, instance_de_tournoi)
            # Récupère le choix de quel participant modifier
            indice_participant = GestionDeRapport.selection_participants(self.objet_gestion_rapport,
                                                                         instance_de_tournoi)
            # Récupère le paramètre à modifier
            parametre_a_modifier = GestionDeJoueur. \
                recuperation_du_parametre_a_modifier(self.objet_gestion_joueur)
            # Récupère la nouvelle valeur du paramètre
            nouvelle_valeur_parametre = SaisieDeDonnees. \
                entree_nouvelle_valeur_parametre(self.vue_saisie_de_donnees, parametre_a_modifier)
            # Modifie le paramètre du joueur dans l'instance de tournoi
            instance_de_tournoi = GestionDeJoueur.modification_d_un_participant(
                self.objet_gestion_joueur,
                instance_de_tournoi, indice_participant,
                parametre_a_modifier,
                nouvelle_valeur_parametre)
            # Retourne l'instance de tournoi modifiée
            return instance_de_tournoi

    def menu_rapport_light(self, players_table, tournaments_table):
        """ Menu du choix de quel rapport afficher, version light, s'affiche lorsque aucun tournoi n'est en cours"""
        # Initialise la variable récupérant le choix utilisateur
        choix_rapport = 0
        # Gere la sortie du menu
        while choix_rapport != 5:
            # Récupère le choix utilisateur
            choix_rapport = int(SaisieDeDonnees.menu_rapport_light(self.vue_saisie_de_donnees))
            if choix_rapport == 1:
                # Affiche la liste des joueurs
                choix_type_tri = GestionDeRapport.choix_classement_elo_ou_alpha(self.objet_gestion_rapport)
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
                Vue.message_de_sortie_3(self.vue_instance)
            else:
                # gere le cas ou le choix entré n'est pas dans la liste des choix disponibles.
                MessageDErreur.message_d_erreur_d_input(self.vue_message_d_erreur)

    def menu_rapport(self, players_table, tournaments_table, instance_de_tournoi):
        """ Menu du choix de quel rapport afficher, complet, s'affiche lorsqu'un tournoi est en cours"""
        # Initialise la variable récupérant le choix utilisateur
        choix_rapport = 0
        # Gere la sortie du menu
        while choix_rapport != 6:
            # Récupère le choix utilisateur
            choix_rapport = int(SaisieDeDonnees.menu_rapport(self.vue_saisie_de_donnees))
            if choix_rapport == 1:
                # Affiche la liste des joueurs
                choix_type_tri = GestionDeRapport.choix_classement_elo_ou_alpha(self.objet_gestion_rapport)
                GestionDeRapport.affichage_du_classement_db(self.objet_gestion_rapport, "",
                                                            players_table, choix_type_tri)
            elif choix_rapport == 2:
                # Affiche la liste des participants
                GestionDeRapport.affichage_classement_participant_indexee_triee(self.objet_gestion_rapport,
                                                                                instance_de_tournoi, "oui")
                MessageDErreur.appuyer_sur_entrer_pour_continuer(self.vue_message_d_erreur)
            elif choix_rapport == 3:
                # Affiche la liste des tournois
                Vue.affichage_liste_de_tournoi(self.vue_instance, tournaments_table)
                MessageDErreur.appuyer_sur_entrer_pour_continuer(self.vue_message_d_erreur)
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
        """ Récupère le nombre de participants au tournoi """
        # Récupère le nombre de participants
        nombre_de_participants = SaisieDeDonnees.\
            recuperation_nombre_de_participants_du_tournoi(self.vue_saisie_de_donnees)
        # Retourne le nombre de participants
        return nombre_de_participants

    def selection_des_participants_db(self, players_table, nombre_de_participants):
        """ Selection des participants dans le pool de joueurs connus de la base table_players"""
        # Initialise la liste de participant
        liste_participants = []
        # Crée une boucle qui s'itérera autant de fois qu'il y a de participants
        for i in range(nombre_de_participants):
            # Récupère le nom et prénom du joueur à ajouter au tournoi :
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
        """ Vérifie si un couple Nom / Prénom se trouve dans la liste des objets joueurs """
        if (participant["Nom"] == joueur_de_la_liste.nom) and (participant["Prenom"] == joueur_de_la_liste.prenom):
            return "Presence"
        else:
            return "Absence"

    def verification_duplicate_joueurs(self, liste_duplicate):
        """ Affiche la liste des homonymes et récupère la selection de l'utilisateur """
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

    def instanciation_tournoi_db(self, id_tournoi, tournaments_table):
        """ Recupère un tournoi en utilisant les paramètres mis en paramètres """
        # Recupère les informations du tournoi à récupérer dans une variable
        info_tournoi_recuperees = tournaments_table.get(doc_id=int(id_tournoi))
        # Création du dictionnaire mettant en forme les informations du tournoi pour pouvoir les instancier
        info_tournoi_a_charger = {}
        info_tournoi_a_charger["nom_du_tournoi"] = info_tournoi_recuperees["nom"]
        info_tournoi_a_charger["lieu_du_tournoi"] = info_tournoi_recuperees["lieu"]
        info_tournoi_a_charger["date_de_tournoi"] = info_tournoi_recuperees["dates_du_tournoi"]
        info_tournoi_a_charger["type_de_controle_du_temps"] = info_tournoi_recuperees["type_controle_de_temps"]
        info_tournoi_a_charger["nombre_de_participant"] = info_tournoi_recuperees["nombre_de_participants"]
        info_tournoi_a_charger["nombre_de_tour"] = info_tournoi_recuperees["nombre_de_tour"]
        info_tournoi_a_charger["commentaires"] = info_tournoi_recuperees["commentaire"]
        instance_de_tournoi = self.creation_du_tournoi(info_tournoi_a_charger)
        instance_de_tournoi.completion = info_tournoi_recuperees["completion"]
        instance_de_tournoi.rondes = info_tournoi_recuperees["rondes"]
        instance_de_tournoi.participants = []
        self.ajout_joueur_instance_tournoi(info_tournoi_recuperees, instance_de_tournoi)

        print(len(instance_de_tournoi.participants))
        print(instance_de_tournoi.participants)
        print(len(instance_de_tournoi.rondes))
        print(instance_de_tournoi.completion)
        print(str(info_tournoi_recuperees))
        print(str(info_tournoi_a_charger))
        print(str(instance_de_tournoi.rondes))
        print(str(instance_de_tournoi.participants))
        input()
        return instance_de_tournoi

    def ajout_joueur_instance_tournoi(self, info_tournoi_recuperees, instance_de_tournoi):
        i=0
        while i < len(info_tournoi_recuperees["participants"]):
            print(info_tournoi_recuperees["participants"][i]["nom"])
            instance_de_tournoi.participants.append([Joueur(info_tournoi_recuperees["participants"][i]["nom"],
                                                     info_tournoi_recuperees["participants"][i]["prenom"],
                                                     info_tournoi_recuperees["participants"][i]["date_de_naissance"],
                                                     info_tournoi_recuperees["participants"][i]["sexe"],
                                                     info_tournoi_recuperees["participants"][i]["classement_elo"]), 0])
            i += 1

    def appairage_match_d_une_ronde(self, numero_de_ronde, instance_de_tournoi, type_de_tournoi):
        """ Mécanisme de fonctionnement d'une ronde"""
        # Creation de l'objet instancié tournoi nécessaire
        objet_type_de_tournoi = TypeDeTournoi(self.objet_gestion_joueur, self.vue_message_d_erreur)
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
        """ Lance une ronde """
        # Prompt l'utilisateur à démarrer la ronde en appuyant sur entrée
        SaisieDeDonnees.depart_de_la_ronde(self.vue_saisie_de_donnees)
        # Récupère la date et l'heure lorsque l'utilisateur appuie sur entrée
        objet_date_heure_debut_ronde = datetime.now()
        # Stock l'heure de depart de la ronde dans l'entité ronde
        ronde_a_lancer.date_heure_debut_de_ronde = str(objet_date_heure_debut_ronde.strftime("%d/%m/%Y %H:%M:%S"))
        # Retourne l'entité ronde
        return ronde_a_lancer

    def fin_d_une_ronde(self, ronde_a_clore):
        """ Clos une ronde et saisie les resultats"""
        # Prompt l'utilisateur à signaler la fin de la ronde en appuyant sur entrée
        SaisieDeDonnees.fin_de_la_ronde(self.vue_saisie_de_donnees)
        # Récupère la date et l'heure lorsque l'utilisateur appuie sur entrée
        objet_date_heure_fin_ronde = datetime.now()
        # Stock l'heure de fin de la ronde dans l'entité ronde
        ronde_a_clore.date_heure_fin_de_ronde = str(objet_date_heure_fin_ronde.strftime("%d/%m/%Y %H:%M:%S"))
        # Boucle sur tous les matchs de la ronde contenus dans la liste des matchs de l'entité ronde
        for match_de_ronde in ronde_a_clore.liste_matchs:
            # Récupère le résultat du match
            resultat_du_match = SaisieDeDonnees.recuperation_des_resultats_d_un_match(self.vue_saisie_de_donnees,
                                                                                      match_de_ronde)
            # Gère le cas ou le résultat entré par l'utilisateur n'est pas dans la liste des choix
            while resultat_du_match not in ["1", "2", "N"]:
                MessageDErreur.message_d_erreur(self.vue_message_d_erreur)
                resultat_du_match = SaisieDeDonnees.recuperation_des_resultats_d_un_match(self.vue_saisie_de_donnees,
                                                                                          match_de_ronde)
            # Gère le cas où le résultat entré par l'utilisateur est dans la liste des choix
            else:
                # Stocke les résultats dans l'entité match en fonction du résultat
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
                    match_de_ronde.resultat_joueur1 = 0.5
                    match_de_ronde.joueur1[1] += 0.5
                    match_de_ronde.resultat_joueur2 = 0.5
                    match_de_ronde.joueur2[1] += 0.5
        return ronde_a_clore

    def initialisation_tournoi(self, players_table, tournaments_table):
        """ Récupère les informations nécessaires et crée le tournoi. """
        # Recuperation des infos participants / tournoi, lancement du tournoi, déroulement du tournoi
        nombre_de_participants = SaisieDeDonnees.verification_champs_est_nombre(self.vue_saisie_de_donnees,
                                                                                "Veuillez entrez le nombre "
                                                                                "de participants : \n")
        # Récupère la liste des participants
        liste_participants_tournoi = self.selection_des_participants_db(players_table, nombre_de_participants)
        # Gère le cas où un problème serait arrivé dans la sélection de la liste des participants
        if len(liste_participants_tournoi) == nombre_de_participants:
            # Récupère les infos du tournoi à créer
            info_instance_tournoi_a_creer = SaisieDeDonnees.\
                recuperation_des_informations_du_tournoi(self.vue_saisie_de_donnees)
            # Ajoute le nombre de participant dans le dictionnaire contenant des infos du tournoi à créer
            info_instance_tournoi_a_creer["nombre_de_participant"] = nombre_de_participants
            # Crée l'instance de tournoi avec les informations récupérées
            instance_de_tournoi = self.creation_du_tournoi(info_instance_tournoi_a_creer)
            # Affiche un message indiquant que le tournoi est en cours de création, le stockage du tournoi pouvant
            # prendre quelques secondes
            Vue.affichage_creation_tournoi_en_cours(self.vue_instance)
            # Stocke le tournoi en DB
            tournaments_table.insert(Tournoi.serialisation_tournoi(instance_de_tournoi))
            # Stocke la liste des participants dans l'instance de tournoi
            instance_de_tournoi.participants = liste_participants_tournoi
            # Stocke la liste des participants en DB
            participants_db = []
            for participants in liste_participants_tournoi:
                participants_db.append(Joueur.serialisation_joueur(participants[0]))
            tournoi = Query()
            tournaments_table.update({"participants": participants_db}, tournoi.nom ==
                                     instance_de_tournoi.nom_du_tournoi)
            # Renvoi l'instance du tournoi
            return instance_de_tournoi
        else:
            # Affiche un message d'erreur en cas de problème avec la récupération des participants
            MessageDErreur.message_d_erreur(self.vue_message_d_erreur)
            return ""

    def initialisation_ronde(self, numero_de_ronde_active, instance_de_tournoi, players_table, choix_type_tournoi,
                             tournaments_table):
        """ Determine les appairages de match, lance une ronde et récupère les résultats des matchs, puis affiche les
        résultats du tournoi si c'est la dernière ronde."""
        # Lancement de la ronde suivante
        # Vérifie si la dernière ronde a été jouée et renvoi un message indiquant que le tournoi est terminé si c'est
        # le cas
        if instance_de_tournoi.completion == "Non":
            # Défini les appairages de match et les stocks dans la variable ronde
            ronde_actuelle = self.appairage_match_d_une_ronde(numero_de_ronde_active, instance_de_tournoi,
                                                              choix_type_tournoi)
            # Prompt le départ de la ronde et stock l'heure de début
            ronde_actuelle = self.depart_d_une_ronde(ronde_actuelle)
            # Prompt la fin de la ronde et stock l'heure de fin
            ronde_actuelle = self.fin_d_une_ronde(ronde_actuelle)
            # Gère le cas ou la ronde est la dernière du tournoi
            if int(numero_de_ronde_active == int(instance_de_tournoi.nombre_de_tour_du_tournoi)):
                # Passe la complétion du tournoi à oui indiquant qu'il est terminé
                instance_de_tournoi.completion = "Oui"
                tournoi = Query()
                tournaments_table.update({"completion": instance_de_tournoi.completion}, tournoi.nom ==
                                         instance_de_tournoi.nom_du_tournoi)
                # Inscrit les informations de toutes les rondes en DB
                self.recuperation_ronde_db(ronde_actuelle, instance_de_tournoi, tournaments_table, players_table,
                                           numero_de_ronde_active)
                # Tri la liste des participants en fonction du nombre de points tournoi
                instance_de_tournoi.participants = GestionDeJoueur. \
                    fonction_decorateurs_pour_tri_participants(self.objet_gestion_joueur,
                                                               instance_de_tournoi.participants,
                                                               "points_tournoi")
                # Affiche le classsement final du tournoi
                Vue.affichage_classement_final_tournoi(self.vue_instance, instance_de_tournoi)
            # Renvoi l'entité ronde_actuelle
            return ronde_actuelle
        else:
            MessageDErreur.message_d_erreur_tournoi_termine(self.vue_message_d_erreur)

    def serialisation_ronde_objet(self, rondes, players_table):
        """ Sérialise tous les objets contenus dans une ronde. """
        liste_match_serialized = []
        # Boucle dans les matchs de la liste de matchs
        for match in rondes.liste_matchs:
            # Recherche le joueur en DB correspondant aux nom et prénom entrés
            recherche = Query()
            match_serialized = Match.serialisation_match(match)
            resultat_rech_joueur1_dans_table = players_table.search((recherche.nom == match.joueur1[0].nom) &
                                                                    (recherche.prenom == match.joueur1[0].prenom) &
                                                                    (recherche.date_de_naissance ==
                                                                    match.joueur1[0].date_de_naissance) &
                                                                    (recherche.sexe == match.joueur1[0].sexe) &
                                                                    (recherche.classement_elo == match.joueur1[0].
                                                                    classement_elo))
            # Stocke dans la variable match sérialisé les informations du joueur récupérées en db
            match_serialized["joueur1"] = resultat_rech_joueur1_dans_table[0].doc_id
            match_serialized["joueur2"] = (players_table.search((recherche.nom == match.joueur2[0].nom) &
                                                                (recherche.prenom == match.joueur2[0].prenom) &
                                                                (recherche.date_de_naissance ==
                                                                match.joueur2[0].date_de_naissance) &
                                                                (recherche.sexe == match.joueur2[0].sexe) &
                                                                (recherche.classement_elo == match.joueur2[0].
                                                                classement_elo)))[0].doc_id
            # Stocke dans la variable match sérialisé le tuple du match
            match_serialized["tuple_match"] = ([match_serialized["joueur1"], match_serialized["resultat_joueur1"]],
                                               [match_serialized["joueur2"], match_serialized["resultat_joueur2"]])
            liste_match_serialized.append(match_serialized)
        # Sérialise la ronde
        ronde_serial = Ronde.serialisation_ronde(rondes)
        # Stocke la liste des matchs dans la ronde sérialisée
        ronde_serial["liste_match"] = liste_match_serialized
        # Retourne la ronde sérialisée
        return ronde_serial

    def recuperation_ronde_db(self, rondes, instance_de_tournoi, tournaments_table, players_table, ronde_active):
        """ Sérialise la ronde, la stocke dans la base tournaments, puis re-sérialise """
        liste_ronde_serial = []
        # Vérifie si une ronde est en cours
        if ronde_active > 1:
            # Stocke les rondes du tournoi dans la variable de liste de rondes sérialisées
            for ronde in instance_de_tournoi.rondes:
                liste_ronde_serial.append(self.serialisation_ronde_objet(ronde, players_table))
        # Serialise la ronde en cours
        serial_ronde = self.serialisation_ronde_objet(rondes, players_table)
        # Ajout la ronde serialisée à la liste des autres rondes
        liste_ronde_serial.append(serial_ronde)
        # Met à jour le tournoi avec la liste des rondes sérialisées en DB
        tournoi = Query()
        tournaments_table.update({"rondes": liste_ronde_serial}, (tournoi.nom == instance_de_tournoi.nom_du_tournoi))
