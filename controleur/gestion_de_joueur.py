from modele.joueur import Joueur
from vue.message_d_erreur import MessageDErreur
from vue.saisie_de_donnees import SaisieDeDonnees
from tinydb import Query
from vue.vue import Vue


class GestionDeJoueur:
    """ Classe gérant les joueurs"""

    def __init__(self, vue_instance, vue_message_d_erreur, vue_saisie_de_donnees):
        """ crée l'objet type de joueur """
        self.vue_instance = vue_instance
        self.vue_message_d_erreur = vue_message_d_erreur
        self.vue_saisie_de_donnees = vue_saisie_de_donnees

    def deserialisation_joueur(self, joueur):
        nom = joueur["nom"]
        prenom = joueur["prenom"]
        date_de_naissance = joueur["date_de_naissance"]
        sexe = joueur["sexe"]
        classement_elo = joueur["classement_elo"]
        points_tournoi = joueur["points_tournoi"]
        return Joueur(nom, prenom, date_de_naissance, sexe, classement_elo, points_tournoi)

    def selection_d_un_joueur_a_modifier(self):
        choix_du_joueur_a_modifier = SaisieDeDonnees.selection_joueur_a_modifier(self.vue_saisie_de_donnees)
        return choix_du_joueur_a_modifier

    def selection_d_un_joueur_a_modifier_elo(self):
        choix_du_joueur_a_modifier = int(SaisieDeDonnees.selection_joueur_a_modifier(self.vue_saisie_de_donnees))
        return choix_du_joueur_a_modifier

    def modification_d_un_joueur(self, participants):
        indice_joueur_a_modifier = 0
        try:
            indice_joueur_a_modifier = int(self.selection_d_un_joueur_a_modifier())-1
        except TypeError:
            MessageDErreur.message_d_erreur_d_input_chiffre(self.vue_message_d_erreur)
        # change le classement tournoi
        participants[indice_joueur_a_modifier].points_tournoi = \
            int(SaisieDeDonnees.modification_point_tournoi(self.vue_saisie_de_donnees,
                                                           participants[indice_joueur_a_modifier]))
        return participants

    def recherche_correspondance_db(self, players_table, joueur_a_rechercher):
        """ Recherche toutes les correspondances d'un couple Nom/Prenom dans une base"""
        Joueur = Query()
        resultat_recherche = players_table.search((Joueur.nom == joueur_a_rechercher["nom"]) & (Joueur.prenom == joueur_a_rechercher["prenom"]))
        i=0
        for resultat in resultat_recherche:
            print("[" + str(i) + "] | " + str(resultat))
            i += 1
        if len(resultat_recherche)>1:
            joueur_choisi = int(input("Veuillez renseignez le numéro du joueur à modifier : \n"))
            return resultat_recherche[joueur_choisi]
        else:
            return resultat_recherche[0]

    def recuperation_du_parametre_a_modifier_db(self):
        parametre_a_modifier = SaisieDeDonnees.selection_du_parametre_a_modifier(self.vue_saisie_de_donnees)
        if parametre_a_modifier == 1:
            return "nom"
        elif parametre_a_modifier == 2:
            return "prenom"
        elif parametre_a_modifier == 3:
            return "date_de_naissance"
        elif parametre_a_modifier == 4:
            return "sexe"
        elif parametre_a_modifier == 5:
            return "classement_elo"
        elif parametre_a_modifier == 6:
            return "points_tournoi"
        else:
            MessageDErreur.message_d_erreur(self.vue_message_d_erreur)

    def modification_d_un_joueur_db(self, players_table, joueur_a_modif, parametre, nouvelle_valeur):
        """ Modifie les paramètres d'un joueur de la db"""
        joueurmodif = Query()
        players_table.update({parametre: nouvelle_valeur}, ((joueurmodif.nom == joueur_a_modif["nom"]) &
                                                            (joueurmodif.prenom == joueur_a_modif["prenom"]) &
                                                            (joueurmodif.date_de_naissance ==
                                                             joueur_a_modif["date_de_naissance"]) &
                                                            (joueurmodif.sexe == joueur_a_modif["sexe"]) &
                                                            (joueurmodif.classement_elo ==
                                                             joueur_a_modif["classement_elo"]) &
                                                            (joueurmodif.points_tournoi ==
                                                             joueur_a_modif["points_tournoi"])
                                                            )
                             )
        input("Changement effectué...")


    def modification_d_un_joueur_elo(self, liste_joueurs, players_table):
        indice_joueur_a_modifier = 0
        try:
            indice_joueur_a_modifier = int(self.selection_d_un_joueur_a_modifier_elo())-1
        except TypeError:
            MessageDErreur.message_d_erreur_d_input_chiffre(self.vue_message_d_erreur)
        # change le classement elo
        liste_joueurs[indice_joueur_a_modifier].classement_elo = \
            int(SaisieDeDonnees.modification_classement_elo(self.vue_saisie_de_donnees,
                                                            liste_joueurs[indice_joueur_a_modifier]))
        joueur_cherche_db = Query()
        players_table.search(joueur_cherche_db.nom == liste_joueurs[indice_joueur_a_modifier].nom)
        return liste_joueurs

    def ajout_des_joueurs(self, players_table):
        """ Ajout des joueurs """
        # Pool de 28 joueurs statiques
        players_table.truncate()
        liste_joueurs = [Joueur("Nom01", "prénom01", "11/11/11", "M", 1650),
                         Joueur("Nom02", "prénom02", "10/10/10", "F", 1435),
                         Joueur("Nom03", "prénom03", "9/9/9", "U", 1983),
                         Joueur("Nom04", "prénom04", "08/08/08", "M", 1945),
                         Joueur("Nom05", "prénom05", "04/05/06", "F", 1345),
                         Joueur("Nom06", "prénom06", "11/5/11", "M", 1580),
                         Joueur("Nom07", "prénom07", "10/9/10", "F", 1415),
                         Joueur("Nom17", "prénom17", "10/9/10", "F", 1615),
                         Joueur("Nom18", "prénom18", "9/4/9", "U", 1153),
                         Joueur("Nom19", "prénom19", "11/11/11", "M", 1258),
                         Joueur("Nom20", "prénom20", "10/10/10", "F", 1338),
                         Joueur("Nom21", "prénom21", "11/11/11", "M", 1250),
                         Joueur("Nom22", "prénom22", "10/10/10", "F", 1335),
                         Joueur("Nom08", "prénom08", "9/4/9", "U", 1953),
                         Joueur("Nom01", "prénom01", "10/10/10", "F", 1222),
                         Joueur("Nom09", "prénom09", "11/11/11", "M", 1454),
                         Joueur("Nom10", "prénom10", "10/10/10", "F", 1536),
                         Joueur("Nom11", "prénom11", "11/11/11", "M", 1450),
                         Joueur("Nom12", "prénom12", "10/10/10", "F", 1535),
                         Joueur("Nom13", "prénom13", "9/9/9", "U", 1783),
                         Joueur("Nom14", "prénom14", "08/08/08", "M", 1245),
                         Joueur("Nom15", "prénom15", "04/05/06", "F", 1545),
                         Joueur("Nom01", "prénom01", "09/09/09", "M", 1502),
                         Joueur("Nom16", "prénom16", "11/5/11", "M", 1380),
                         Joueur("Nom23", "prénom23", "9/9/9", "U", 1483),
                         Joueur("Nom24", "prénom24", "08/08/08", "M", 1545),
                         Joueur("Nom25", "prénom25", "04/05/06", "F", 1645),
                         Joueur("Nom26", "prénom26", "11/5/11", "M", 1780),
                         Joueur("Nom27", "prénom27", "10/9/10", "F", 1815),
                         Joueur("Nom28", "prénom28", "9/4/9", "U", 1053)]
        for joueur in liste_joueurs:
            self.ajout_joueur_db(joueur, players_table)
        return liste_joueurs

    def ajout_joueur_db(self, joueur, players_table):
        joueur = Joueur.serialisation_joueur(joueur)
        players_table.insert(joueur)

    def classement_des_joueurs(self, liste_participant, facteur_tri):
        """ Classe les joueurs en fonction de leur classement elo pour la première ronde, ou par leur classement
        tournoi pour les rondes suivantes."""
        if facteur_tri == "classement_elo":
            liste_participant.sort(key=lambda x: x.classement_elo, reverse=True)
        elif facteur_tri == "points_tournoi":
            liste_participant.sort(key=lambda x: (x.points_tournoi, x.classement_elo), reverse=True)
        elif facteur_tri == "nom":
            liste_participant.sort(key=lambda x: x.nom, reverse=False)
        return liste_participant

    def classement_des_joueurs_db(self, players_table, facteur_tri):
        """ Classe les joueurs en fonction de leur classement elo pour la première ronde, ou par leur classement
        tournoi pour les rondes suivantes."""
        if facteur_tri == "points_tournoi":
            table_sorted = sorted(players_table.all(), key=lambda x: (x[facteur_tri], x["classement_elo"]), reverse=True)
        elif facteur_tri == "nom":
            table_sorted = sorted(players_table.all(), key=lambda x: x[facteur_tri])
        else :
            table_sorted = sorted(players_table.all(), key=lambda x: x[facteur_tri], reverse=True)
        return table_sorted

    def creation_d_un_joueur(self, nom_prenom_info_joueur):
        """ Ajout d'un joueur à la liste de joueur """
        infos_joueur_a_ajouter = SaisieDeDonnees.ajout_des_informations_d_un_joueur(self.vue_saisie_de_donnees,
                                                                                    nom_prenom_info_joueur)
        joueur_a_ajouter = Joueur(infos_joueur_a_ajouter["nom"], infos_joueur_a_ajouter["prenom"],
                                  infos_joueur_a_ajouter["date_de_naissance"], infos_joueur_a_ajouter["sexe"],
                                  infos_joueur_a_ajouter["classement_elo"])
        return joueur_a_ajouter

    def ajout_d_un_joueur_a_la_liste(self, joueur_a_ajouter, liste_joueurs, players_table):
        """ Ajoute un joueur à la liste des joueurs existants parmis lesquels il est possible de sélectionner
        les participants"""
        liste_joueurs.append(joueur_a_ajouter)
        self.ajout_joueur_db(joueur_a_ajouter, players_table)
        return liste_joueurs
