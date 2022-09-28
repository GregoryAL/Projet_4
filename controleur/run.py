""" Point d'entrée du contrôleur"""
import sys
from modele.tournoi import Tournoi
from modele.joueurs import Joueur
import datetime
import random
from vue.vue import Vue
from controleur.type_de_tournoi import TypeDeTournoi


class Controleur:
    """ contrôleur general """

    def __init__(self, vue):
        """ initialise le controleur. """
        self.vue_instance = vue


    def execute(self):
        while self.affichage_du_menu() != 5:
            instance_de_tournoi = self.affichage_du_menu()
        # Sortie du programme à la demande de l'utilisateur (choix sortie dans la boucle)
        sys.exit("Vous quittez la gestion du tournoi")


    def affichage_du_menu(self):
        """ Affiche le menu du tournoi, récupère le choix utilisateur et lance la methode correspondante """
        choix_utilisateur = int(Vue.menu(self.vue_instance))
        nombre_de_participants = 0
        liste_participants = []
        liste_joueurs = self.ajout_des_joueurs()
        if choix_utilisateur == 1:
            nombre_de_participants = int(Vue.recuperation_nombre_de_participants_du_tournoi(self.vue_instance))
            for i in range(nombre_de_participants):
                # Recupere le nom et prénom du joueur à ajouter au tournoi :
                participant = Vue.recuperation_participant_du_tournoi(self.vue_instance, i)
                # Verifie que le joueur est dans la liste de joueur
                for joueur_de_la_liste in liste_joueurs.values():
                    nombre_d_entree_dans_le_dictionnaire_de_liste_des_joueurs = len(liste_joueurs)
                    cle_dernier_nom_entre = "player" + str(nombre_d_entree_dans_le_dictionnaire_de_liste_des_joueurs)
                    dernier_nom_entre = liste_joueurs[cle_dernier_nom_entre]
                    if ((str(participant["Nom"])) in joueur_de_la_liste.nom) and ((str(participant["Prenom"])) in joueur_de_la_liste.prenom):
                        print("ok")
                        liste_participants.append(joueur_de_la_liste)
                        print(liste_participants)
                        break
                    else:
                        if str(joueur_de_la_liste.nom) == str(dernier_nom_entre.nom):
                            reponse_creation_joueur = Vue.joueur_inexistant(self.vue_instance)
                            if reponse_creation_joueur == "Oui":
                                input("Fin de l'ajout des participants. Merci de créer le joueur puis recommencer "
                                      "l'ajout des participants")

                                return ""






        elif choix_utilisateur == 2:
            info_instance_tournoi_a_creer = Vue.recuperation_des_informations_du_tournoi(self.vue_instance, nombre_de_participants)
            instance_de_tournoi = self.creation_du_tournoi(info_instance_tournoi_a_creer)
            numero_de_ronde_active = 0
            while numero_de_ronde_active < instance_de_tournoi.nombre_de_tour_du_tournoi:
                numero_de_ronde_active += 1
                print("le numéro de ronde active est " + str(numero_de_ronde_active) + " sur un total de " +
                      str(instance_de_tournoi.nombre_de_tour_du_tournoi) + "rondes")
                ronde_actuelle = self.appairage_match_d_une_ronde(numero_de_ronde_active, instance_de_tournoi,
                                                                  "MethodeSuisse")

                self.depart_d_une_ronde(ronde_actuelle)
                self.fin_d_une_ronde(ronde_actuelle)
                print(ronde_actuelle.liste_matchs[1].joueur1.nom + " a " +
                      str(ronde_actuelle.liste_matchs[1].joueur1.points_tournoi) + ". \n")
                instance_de_tournoi.rondes.append(ronde_actuelle)
                print(instance_de_tournoi.participants[1].nom + " a " +
                      str(instance_de_tournoi.participants[1].points_tournoi) + ". \n")
        elif choix_utilisateur == 3:
            indice_nouveau_joueur = len(liste_joueurs) + 2
            cle_nouveau_joueur = "player" + str(indice_nouveau_joueur)
            joueur_a_ajouter = self.ajout_d_un_joueur()
            liste_joueurs[cle_nouveau_joueur] = joueur_a_ajouter
        elif choix_utilisateur == 4:
            print(int(self.instance_de_tournoi.nombre_de_tour_du_tournoi))
            print(self.instance_de_tournoi)
        elif choix_utilisateur == 5:
            return choix_utilisateur

    def selection_des_participants(self, nombre_de_participant):
        """ Selection des participants dans le pool de joueur connu et lance l'ajout si besoin d un nouveau joueur"""




    def ajout_des_joueurs(self):
        """ Ajout des joueurs """
        # Pool de 28 joueurs statiques
        liste_joueurs = {}
        liste_joueurs["player01"] = Joueur("Nom01", "prénom01", "11/11/11", "M", 1650)
        liste_joueurs["player02"] = Joueur("Nom02", "prénom02", "10/10/10", "F", 1435)
        liste_joueurs["player03"] = Joueur("Nom03", "prénom03", "9/9/9", "U", 1983)
        liste_joueurs["player04"] = Joueur("Nom04", "prénom04", "08/08/08", "M", 1945)
        liste_joueurs["player05"] = Joueur("Nom05", "prénom05", "04/05/06", "F", 1345)
        liste_joueurs["player06"] = Joueur("Nom06", "prénom06", "11/5/11", "M", 1580)
        liste_joueurs["player07"] = Joueur("Nom07", "prénom07", "10/9/10", "F", 1415)
        liste_joueurs["player08"] = Joueur("Nom08", "prénom08", "9/4/9", "U", 1953)
        liste_joueurs["player09"] = Joueur("Nom09", "prénom09", "11/11/11", "M", 1454)
        liste_joueurs["player10"] = Joueur("Nom10", "prénom10", "10/10/10", "F", 1536)
        liste_joueurs["player11"] = Joueur("Nom11", "prénom11", "11/11/11", "M", 1450)
        liste_joueurs["player12"] = Joueur("Nom12", "prénom12", "10/10/10", "F", 1535)
        liste_joueurs["player13"] = Joueur("Nom13", "prénom13", "9/9/9", "U", 1783)
        liste_joueurs["player14"] = Joueur("Nom14", "prénom14", "08/08/08", "M", 1245)
        liste_joueurs["player15"] = Joueur("Nom15", "prénom15", "04/05/06", "F", 1545)
        liste_joueurs["player16"] = Joueur("Nom16", "prénom16", "11/5/11", "M", 1380)
        liste_joueurs["player17"] = Joueur("Nom17", "prénom17", "10/9/10", "F", 1615)
        liste_joueurs["player18"] = Joueur("Nom18", "prénom18", "9/4/9", "U", 1153)
        liste_joueurs["player19"] = Joueur("Nom19", "prénom19", "11/11/11", "M", 1258)
        liste_joueurs["player20"] = Joueur("Nom20", "prénom20", "10/10/10", "F", 1338)
        liste_joueurs["player21"] = Joueur("Nom21", "prénom21", "11/11/11", "M", 1250)
        liste_joueurs["player22"] = Joueur("Nom22", "prénom22", "10/10/10", "F", 1335)
        liste_joueurs["player23"] = Joueur("Nom23", "prénom23", "9/9/9", "U", 1483)
        liste_joueurs["player24"] = Joueur("Nom24", "prénom24", "08/08/08", "M", 1545)
        liste_joueurs["player25"] = Joueur("Nom25", "prénom25", "04/05/06", "F", 1645)
        liste_joueurs["player26"] = Joueur("Nom26", "prénom26", "11/5/11", "M", 1780)
        liste_joueurs["player27"] = Joueur("Nom27", "prénom27", "10/9/10", "F", 1815)
        liste_joueurs["player28"] = Joueur("Nom28", "prénom28", "9/4/9", "U", 1053)
        return liste_joueurs

    def creation_du_tournoi(self, info_tournoi):
        """ Creation d'un tournoi en utilisant les paramètres utilisateurs"""
        # Creation d'un objet tournoi avec les informations récupérées par la Vue
        self.instance_de_tournoi = Tournoi(info_tournoi["nom_du_tournoi"],
                                           info_tournoi["lieu_du_tournoi"],
                                           info_tournoi["date_de_tournoi"],
                                           info_tournoi["type_de_controle_du_temps"],
                                           info_tournoi["nombre_de_participant"],
                                           info_tournoi["nombre_de_tour"],
                                           info_tournoi["commentaires"])
        # Récuperation de la liste des joueurs avec la Vue
        # for i in range(self.instance_de_tournoi.nombre_de_participants):
            # joueur_random_key = random.choice(list(self.liste_joueurs.keys()))
            # joueur_random = self.liste_joueurs[joueur_random_key]
            # self.instance_de_tournoi.participants.append(joueur_random)
            # self.liste_joueurs.pop(joueur_random_key)
        return self.instance_de_tournoi

    def appairage_match_d_une_ronde(self, numero_de_ronde, instance_de_tournoi, methode_de_comptage):
        """ Mécanisme de fonctionnement d'une ronde"""
        # Creation de l'objet instancié tournoi nécessaire
        objet_type_de_tournoi = TypeDeTournoi()
        ronde_actuelle = TypeDeTournoi.choix_type_tournoi(objet_type_de_tournoi, "MethodeSuisse", numero_de_ronde,
                                                          instance_de_tournoi)
        # pour chaque match de la liste des matchs de la ronde
        for match_de_ronde in ronde_actuelle.liste_matchs:
            self.affichage_des_matchs(match_de_ronde)
        # ronde_actuelle.liste_matchs[match_de_ronde] = self.deroulement_d_un_match(
            # ronde_actuelle.liste_matchs[match_de_ronde])
        # ronde_actuelle.resultat_matchs = ([ronde_actuelle.liste_matchs[match_de_ronde].joueur1,
                                           # ronde_actuelle.liste_matchs[match_de_ronde].resultat_joueur1],
                                          # [ronde_actuelle.liste_matchs[match_de_ronde].joueur2,
                                           # ronde_actuelle.liste_matchs[match_de_ronde].resultat_joueur2])
        return ronde_actuelle

    def affichage_des_matchs(self, instance_de_match):
        """ Affiche le match en argument """
        Vue.affichage_des_matchs(self.vue_instance, instance_de_match)

    def depart_d_une_ronde(self, ronde_a_lancer):
        Vue.depart_de_la_ronde(self.vue_instance)
        ronde_a_lancer.date_heure_debut_du_match = datetime.datetime.now()
        return ronde_a_lancer

    def fin_d_une_ronde(self, ronde_a_clore):
        Vue.fin_de_la_ronde(self.vue_instance)
        for match_de_ronde in ronde_a_clore.liste_matchs:
            resultat_du_match = Vue.recuperation_des_resultats_d_un_match(self.vue_instance, match_de_ronde)
            while resultat_du_match in ["1", "2", "N"]:
                if resultat_du_match == "1":
                    verification_resultat_saisie = Vue.verification_resultat_match_avec_vainqueur(self.vue_instance,
                                                                                                  match_de_ronde.joueur1,
                                                                                                  match_de_ronde.joueur2)
                    while verification_resultat_saisie != "OK":
                        verification_resultat_saisie = \
                            Vue.verification_resultat_match_avec_vainqueur(self.vue_instance, match_de_ronde.joueur1,
                                                                           match_de_ronde.joueur2)
                    else:
                        match_de_ronde.resultat_joueur1 = 1
                        match_de_ronde.joueur1.points_tournoi += 1
                        match_de_ronde.resultat_joueur2 = 0
                        ronde_a_clore.date_heure_fin_du_match = datetime.datetime.now()
                elif resultat_du_match == "2":
                    verification_resultat_saisie = Vue.verification_resultat_match_avec_vainqueur(self.vue_instance,
                                                                                                  match_de_ronde.joueur2,
                                                                                                  match_de_ronde.joueur1)
                    while verification_resultat_saisie != "OK":
                        verification_resultat_saisie = \
                            Vue.verification_resultat_match_avec_vainqueur(self.vue_instance, match_de_ronde.joueur2,
                                                                           match_de_ronde.joueur1)
                    else:
                        match_de_ronde.resultat_joueur2 = 1
                        match_de_ronde.joueur2.points_tournoi += 1
                        match_de_ronde.resultat_joueur1 = 0
                        ronde_a_clore.date_heure_fin_du_match = datetime.datetime.now()
                elif resultat_du_match == "N":
                    verification_resultat_saisie = Vue.verification_resultat_match_nul(self.vue_instance,
                                                                                       match_de_ronde.joueur1,
                                                                                       match_de_ronde.joueur2)
                    while verification_resultat_saisie != "OK":
                        verification_resultat_saisie = Vue.verification_resultat_match_nul(self.vue_instance,
                                                                                           match_de_ronde.joueur1,
                                                                                           match_de_ronde.joueur2)
                    else:
                        match_de_ronde.resultat_joueur2 = 0.5
                        match_de_ronde.joueur1.points_tournoi += 0.5
                        match_de_ronde.resultat_joueur1 = 0.5
                        match_de_ronde.joueur2.points_tournoi += 0.5
                        ronde_a_clore.date_heure_fin_du_match = datetime.datetime.now()
            else:
                Vue.message_d_erreur(self.vue_instance)
        return ronde_a_clore

    def classement_des_joueurs(self, liste_participant, facteur_tri):
        """ Classe les joueurs en fonction de leur classement elo pour la première ronde, ou par leur classement
        tournoi pour les rondes suivantes."""
        if facteur_tri == "classement_elo":
            liste_participant.sort(key=lambda x: x.classement_elo, reverse=True)
        elif facteur_tri == "points_tournoi:":
            liste_participant.sort(key=lambda x: x.points_tournoi, reverse=True)
        return liste_participant

    def ajout_d_un_joueur(self):
        """ Ajout d'un joueur à la liste de joueur """
        infos_joueur_a_ajouter = Vue.ajout_des_informations_d_un_joueur(self.vue_instance)
        joueur_a_ajouter = Joueur(infos_joueur_a_ajouter["nom"], infos_joueur_a_ajouter["prenom"],
                                  infos_joueur_a_ajouter["date_de_naissance"], infos_joueur_a_ajouter["sexe"],
                                  infos_joueur_a_ajouter["classement_elo"])
        return joueur_a_ajouter


