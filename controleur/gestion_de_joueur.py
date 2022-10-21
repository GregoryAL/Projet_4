from modele.joueur import Joueur
from vue.message_d_erreur import MessageDErreur
from vue.saisie_de_donnees import SaisieDeDonnees
from tinydb import Query


class GestionDeJoueur:
    """ Classe gérant les joueurs"""

    def __init__(self, vue_instance, vue_message_d_erreur, vue_saisie_de_donnees):
        """ Crée l'objet type de joueur """
        self.vue_instance = vue_instance
        self.vue_message_d_erreur = vue_message_d_erreur
        self.vue_saisie_de_donnees = vue_saisie_de_donnees

    def selection_d_un_joueur_a_modifier(self):
        """ Récupère les informations du joueur à modifier"""
        choix_du_joueur_a_modifier = SaisieDeDonnees.selection_joueur_a_modifier(self.vue_saisie_de_donnees)
        return choix_du_joueur_a_modifier

    def recherche_correspondance_db(self, players_table, joueur_a_rechercher):
        """ Recherche toutes les correspondances d'un couple Nom/Prénom dans une base"""
        joueur = Query()
        resultat_recherche = players_table.search((joueur.nom == joueur_a_rechercher["nom"]) &
                                                  (joueur.prenom == joueur_a_rechercher["prenom"]))
        i = 0
        if len(resultat_recherche) > 1:
            for resultat in resultat_recherche:
                Vue.affichage_resultat_recherche(self.vue_instance, resultat)
                i += 1
            joueur_choisi = SaisieDeDonnees.choisir_un_joueur(self.vue_saisie_de_donnees)
            return resultat_recherche[joueur_choisi]
        elif len(resultat_recherche) == 1:
            return resultat_recherche[0]
        else:
            joueur_cree = self.creation_joueur_si_inexistant(players_table, joueur_a_rechercher)
            if joueur_cree != "":
                joueur_cree_recherche = Query()
                joueur_cree_liste = players_table.search((joueur_cree_recherche.nom == joueur_cree.nom) &
                                                         (joueur_cree_recherche.prenom == joueur_cree.prenom))
                return joueur_cree_liste[0]
            else:
                return ""

    def creation_joueur_si_inexistant(self, players_table, joueur_a_rechercher):
        """ Demande si l'utilisateur veut créer le joueur inexistant, si oui renvoi le joueur cree apres ajout
        dans db """
        # Informe que le joueur n'existe pas et demande si le joueur doit être créé.
        creation_joueur_oui_non = SaisieDeDonnees.joueur_inexistant(self.vue_saisie_de_donnees)
        if creation_joueur_oui_non == "Oui":
            # Recupere les informations du joueur à ajouter à la liste, recupere automatiquement Nom/Prenom
            # si l'utilisateur le veut
            info_joueur_a_creer = SaisieDeDonnees.ajout_des_informations_d_un_joueur(self.vue_saisie_de_donnees,
                                                                                     joueur_a_rechercher)
            # Crée l'objet joueur
            objet_joueur = self.creation_objet_joueur(info_joueur_a_creer)
            # ajoute la serialisation de cet objet à la base des joueurs
            self.ajout_joueur_db(objet_joueur, players_table)
            return objet_joueur
        elif creation_joueur_oui_non == "Non":
            return ""

    def recuperation_du_parametre_a_modifier_db_joueur(self):
        """ Affiche une liste de choix et demande à l'utilisateur d'entrer le chiffre correspondant à son choix,
        converti ensuite le chiffre récupéré en string du choix correspondant"""
        parametre_a_modifier = SaisieDeDonnees.selection_du_parametre_a_modifier_joueur(self.vue_saisie_de_donnees)
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
        else:
            MessageDErreur.message_d_erreur(self.vue_message_d_erreur)

    def recuperation_du_parametre_a_modifier(self):
        """ Récupération du paramètre à modifier """
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
                                                             joueur_a_modif["classement_elo"])
                                                            )
                             )
        Vue.affichage_changement_effectue(self.vue_message_d_erreur)

    def modification_d_un_participant(self, instance_tournoi, indice_participant, parametre_a_modifier,
                                      nouveau_parametre):
        """ Modifie un paramètre d'un participant """
        if parametre_a_modifier == "nom":
            instance_tournoi.participants[indice_participant-1][0].nom = nouveau_parametre
        elif parametre_a_modifier == "prenom":
            instance_tournoi.participants[indice_participant-1][0].prenom = nouveau_parametre
        elif parametre_a_modifier == "date_de_naissance":
            instance_tournoi.participants[indice_participant-1][0].date_de_naissance = nouveau_parametre
        elif parametre_a_modifier == "sexe":
            instance_tournoi.participants[indice_participant-1][0].sexe = nouveau_parametre
        elif parametre_a_modifier == "classement_elo":
            instance_tournoi.participants[indice_participant-1][0].classement_elo = nouveau_parametre
        elif parametre_a_modifier == "points_tournoi":
            instance_tournoi.participants[indice_participant-1][1] = nouveau_parametre
        return instance_tournoi

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
        liste_joueurs_db = []
        for joueur in liste_joueurs:
            liste_joueurs_db.append(Joueur.serialisation_joueur(joueur))
        players_table.insert_multiple(liste_joueurs_db)
        return liste_joueurs

    def fonction_decorateurs_pour_tri_participants(self, liste_participants, type_tri):
        """ Ajout d'un indice à la liste des participants, la trie, puis supprime l'indice et renvoi la liste triée"""
        liste_de_liste_a_trie = []
        if type_tri == "nom":
            for participant in liste_participants:
                indice = participant[0].nom
                liste_de_liste_a_trie.append([indice, participant[0], participant[1]])
            liste_de_liste_a_trie.sort(key=lambda x: x[0], reverse=False)
            for liste in liste_de_liste_a_trie:
                del liste[0]
        elif type_tri == "classement_elo":
            for participant in liste_participants:
                indice = participant[0].classement_elo
                liste_de_liste_a_trie.append([indice, participant[0], participant[1]])
            liste_de_liste_a_trie.sort(key=lambda x: x[0], reverse=True)
            for liste in liste_de_liste_a_trie:
                del liste[0]
        elif type_tri == "points_tournoi":
            for participant in liste_participants:
                indice = participant[0].classement_elo
                liste_de_liste_a_trie.append([indice, participant[0], participant[1]])
            liste_de_liste_a_trie.sort(key=lambda x: (x[2], x[0]), reverse=True)
            for item in liste_de_liste_a_trie:
                del item[0]
        return liste_de_liste_a_trie

    def classement_des_joueurs(self, liste_participant, facteur_tri):
        """ Classe les joueurs en fonction de leur classement elo, classement
        tournoi ou alphabétique """
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
            table_sorted = sorted(players_table.all(), key=lambda x: (x[facteur_tri], x["classement_elo"]),
                                  reverse=True)
        elif facteur_tri == "nom":
            table_sorted = sorted(players_table.all(), key=lambda x: x[facteur_tri])
        else:
            table_sorted = sorted(players_table.all(), key=lambda x: x[facteur_tri], reverse=True)
        return table_sorted

    def creation_d_un_joueur(self, nom_prenom_info_joueur):
        """ Ajout d'un joueur à la liste de joueur """
        infos_joueur_a_ajouter = SaisieDeDonnees.ajout_des_informations_d_un_joueur(self.vue_saisie_de_donnees,
                                                                                    nom_prenom_info_joueur)
        joueur_a_ajouter = self.creation_objet_joueur(infos_joueur_a_ajouter)
        return joueur_a_ajouter

    def creation_objet_joueur(self, infos_joueur_a_ajouter):
        joueur_a_ajouter = Joueur(infos_joueur_a_ajouter["nom"], infos_joueur_a_ajouter["prenom"],
                                  infos_joueur_a_ajouter["date_de_naissance"], infos_joueur_a_ajouter["sexe"],
                                  infos_joueur_a_ajouter["classement_elo"])
        return joueur_a_ajouter

    def ajout_joueur_db(self, joueur_a_ajouter, players_table):
        """ Ajoute un objet joueur à la db joueur apres l'avoir sérialisé """
        players_table.insert(Joueur.serialisation_joueur(joueur_a_ajouter))
