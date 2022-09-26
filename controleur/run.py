""" Point d'entrée du contrôleur"""
import sys

from modele.tournoi import Tournoi
from modele import match
from modele import ronde
from modele import joueurs
import datetime
import random
from vue.vue import Vue
from controleur.type_de_tournoi import TypeDeTournoi


class Controleur:
    """ contrôleur general """

    def __init__(self, vue):
        """ initialise le controleur. """
        self.liste_joueurs = {}
        self.liste_joueurs = self.ajout_des_joueurs()
        self.vue_instance = vue


    def execute(self):
        while self.affichage_du_menu() != 5:
            instance_de_tournoi = self.affichage_du_menu()
        # Sortie du programme à la demande de l'utilisateur (choix sortie dans la boucle)
        sys.exit("Vous quittez la gestion du tournoi")


    def affichage_du_menu(self):
        """ Affiche le menu du tournoi, récupère le choix utilisateur et lance la methode correspondante """
        choix_utilisateur = int(Vue.menu(self.vue_instance))
        if choix_utilisateur == 1:
            info_instance_tournoi_a_creer = Vue.recuperation_des_informations_du_tournoi(self.vue_instance)
            instance_de_tournoi = self.creation_du_tournoi(info_instance_tournoi_a_creer)
            numero_de_ronde_active = 0
            while numero_de_ronde_active <= instance_de_tournoi.nombre_de_tour_du_tournoi:
                numero_de_ronde_active += 1
                print("le numéro de ronde active est " + str(numero_de_ronde_active) + " sur un total de " +
                      str(instance_de_tournoi.nombre_de_tour_du_tournoi) + "rondes")
                ronde_actuelle = self.appairage_match_d_une_ronde(numero_de_ronde_active, instance_de_tournoi,
                                                                  "MethodeSuisse")
                instance_de_tournoi.rondes.append(ronde_actuelle)
                print(self.instance_de_tournoi.rondes)


        elif choix_utilisateur == 3:
            self.numero_de_ronde_active = len(self.instance_de_tournoi.rondes)
            print(self.numero_de_ronde_active)
            print(self.instance_de_tournoi.rondes)
            print(self.instance_de_tournoi.rondes[self.numero_de_ronde_active-1].liste_matchs)
            self.instance_de_tournoi.rondes[self.numero_de_ronde_active-1].resultat_matchs = \
                self.recuperation_des_scores()
            return self.instance_de_tournoi
        elif choix_utilisateur == 4:
            print(int(self.instance_de_tournoi.nombre_de_tour_du_tournoi))
            print(self.instance_de_tournoi)
        elif choix_utilisateur == 5:
            return choix_utilisateur

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
        for i in range(self.instance_de_tournoi.nombre_de_participants):
            joueur_random_key = random.choice(list(self.liste_joueurs.keys()))
            joueur_random = self.liste_joueurs[joueur_random_key]
            self.instance_de_tournoi.participants.append(joueur_random)
            self.liste_joueurs.pop(joueur_random_key)
        return self.instance_de_tournoi

    def appairage_match_d_une_ronde(self, numero_de_ronde, instance_de_tournoi, methode_de_comptage):
        """ Mécanisme de fonctionnement d'une ronde"""
        # Creation de l'objet instancié tournoi nécessaire
        objet_type_de_tournoi = TypeDeTournoi()
        ronde_actuelle = TypeDeTournoi.choix_type_tournoi(objet_type_de_tournoi, "MethodeSuisse", numero_de_ronde,
                                                          instance_de_tournoi)
        print(ronde_actuelle)
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
        Vue.affichage_des_matchs(self.vue_instance, instance_de_match)

    def recuperation_des_scores(self, numero_de_ronde):
        """ Recuperation des scores de la vue pour chaque match d'une ronde """


        for match_a_recupere in list(self.instance_de_tournoi.rondes[numero_de_ronde].liste_matchs.key()):
            print(match_a_recupere["joueur1"] + "est le joueur1")
            print(match_a_recupere["resultat_joueur1"] + " est le resultat du match du joueur1")
            match_a_recupere["resultat_joueur1"] = Vue.recuperation_des_resultats_d_un_match(match_a_recupere["joueur1"])
            match_a_recupere["resultat_joueur2"] = Vue.recuperation_des_resultats_d_un_match(match_a_recupere["joueur2"])
            match_a_recupere.tuple_match = ([match_a_recupere["joueur1"], match_a_recupere["resultat_joueur1"]],
                                             [match_a_recupere["joueur2"], match_a_recupere["resultat_joueur2"]])
            self.instance_de_tournoi.rondes[self.numero_de_ronde_active-1].resultat_matchs = match_a_recupere.tuple_match
        return self.instance_de_tournoi







    def ajout_des_joueurs(self):
        """ Ajout des joueurs """
        # Pool de 24 joueurs statiques
        self.liste_joueurs["player01"] = joueurs.Joueur("Nom1", "prénom1", "11/11/11", "M", 1650)
        self.liste_joueurs["player02"] = joueurs.Joueur("Nom2", "prénom2", "10/10/10", "F", 1435)
        self.liste_joueurs["player03"] = joueurs.Joueur("Nom3", "prénom3", "9/9/9", "U", 1983)
        self.liste_joueurs["player04"] = joueurs.Joueur("Nom4", "prénom4", "08/08/08", "M", 1945)
        self.liste_joueurs["player05"] = joueurs.Joueur("Nom5", "prénom5", "04/05/06", "F", 1345)
        self.liste_joueurs["player06"] = joueurs.Joueur("Nom6", "prénom6", "11/5/11", "M", 1580)
        self.liste_joueurs["player07"] = joueurs.Joueur("Nom7", "prénom7", "10/9/10", "F", 1415)
        self.liste_joueurs["player08"] = joueurs.Joueur("Nom8", "prénom8", "9/4/9", "U", 1953)
        self.liste_joueurs["player11"] = joueurs.Joueur("Nom11", "prénom11", "11/11/11", "M", 1450)
        self.liste_joueurs["player12"] = joueurs.Joueur("Nom12", "prénom12", "10/10/10", "F", 1535)
        self.liste_joueurs["player13"] = joueurs.Joueur("Nom13", "prénom13", "9/9/9", "U", 1783)
        self.liste_joueurs["player14"] = joueurs.Joueur("Nom14", "prénom14", "08/08/08", "M", 1245)
        self.liste_joueurs["player15"] = joueurs.Joueur("Nom15", "prénom15", "04/05/06", "F", 1545)
        self.liste_joueurs["player16"] = joueurs.Joueur("Nom16", "prénom16", "11/5/11", "M", 1380)
        self.liste_joueurs["player17"] = joueurs.Joueur("Nom17", "prénom17", "10/9/10", "F", 1615)
        self.liste_joueurs["player18"] = joueurs.Joueur("Nom18", "prénom18", "9/4/9", "U", 1153)
        self.liste_joueurs["player21"] = joueurs.Joueur("Nom21", "prénom21", "11/11/11", "M", 1250)
        self.liste_joueurs["player22"] = joueurs.Joueur("Nom22", "prénom22", "10/10/10", "F", 1335)
        self.liste_joueurs["player23"] = joueurs.Joueur("Nom23", "prénom23", "9/9/9", "U", 1483)
        self.liste_joueurs["player24"] = joueurs.Joueur("Nom24", "prénom24", "08/08/08", "M", 1545)
        self.liste_joueurs["player25"] = joueurs.Joueur("Nom25", "prénom25", "04/05/06", "F", 1645)
        self.liste_joueurs["player26"] = joueurs.Joueur("Nom26", "prénom26", "11/5/11", "M", 1780)
        self.liste_joueurs["player27"] = joueurs.Joueur("Nom27", "prénom27", "10/9/10", "F", 1815)
        self.liste_joueurs["player28"] = joueurs.Joueur("Nom28", "prénom28", "9/4/9", "U", 1053)
        return self.liste_joueurs

    def classement_des_joueurs(self, liste_participant, facteur_tri):
        if facteur_tri == "classement_elo":
            liste_participant.sort(key=lambda x: x.classement_elo, reverse=True)
        elif facteur_tri == "points_tournoi:":
            liste_participant.sort(key=lambda x: x.points_tournoi, reverse=True)
        return liste_participant





    def deroulement_d_un_match(self, instance_de_match):
        # affiche le match en cours
        print("le type de joueur1 est " + str(type(instance_de_match.joueur1)))
        # determine un vainqueur
        liste_choix_vainqueur = [str(instance_de_match.joueur1.nom), str(instance_de_match.joueur2.nom), "nul"]
        vainqueur = random.choice(liste_choix_vainqueur)
        # modifie les points de tournoi de chaque joueur en fonction du resultat du match
        if vainqueur == str(instance_de_match.joueur1.nom):
            print(instance_de_match.joueur1.nom + " a gagné contre " + instance_de_match.joueur2.nom)
            instance_de_match.resultat_joueur1 = 1
            instance_de_match.resultat_joueur2 = 0
        elif vainqueur == str(instance_de_match.joueur2.nom):
            print(instance_de_match.joueur2.nom + " a gagné contre " + instance_de_match.joueur1.nom)
            instance_de_match.resultat_joueur1 = 0
            instance_de_match.resultat_joueur2 = 1
        elif vainqueur == "nul":
            print("C'est un match nul")
            instance_de_match.resultat_joueur1 = 0.5
            instance_de_match.resultat_joueur2 = 0.5
        instance_de_match.joueur1.points_tournoi += instance_de_match.resultat_joueur1
        instance_de_match.joueur2.points_tournoi += instance_de_match.resultat_joueur2
        return instance_de_match
        # for participant in liste_de_joueur:
            # print(joueurs.Joueur.__str__(participant))




