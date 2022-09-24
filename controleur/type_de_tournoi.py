class TypeDeTournoi:
    """ Classe gérant les types de tournoi"""

    def __init__(self, type_de_tournoi, numero_de_ronde, instance_tournoi):
        self.type_de_tournoi = type_de_tournoi
        self.numero_de_ronde = numero_de_ronde
        self.instance_tournoi = instance_tournoi

    def creation_des_matchs_methode_suisse(self):
        # Tri des joueurs
        if self.numero_de_ronde == 1:
            self.instance_tournoi.participants.sort(key=lambda x: x.classement_elo, reverse=True)
            print("le classement est : ")
            for joueur in self.instance_tournoi.participants:
                print(joueurs.Joueur.__str__(joueur))
        elif self.numero_de_ronde > 1:
            self.instance_tournoi.participants.sort(key=lambda x: x.points_tournoi, reverse=True)
            print("le classement est : ")
            for joueur in self.instance_tournoi.participants:
                print(joueurs.Joueur.__str__(joueur))
        # Creation des paires
        moitie_des_participants = self.instance_tournoi.nombre_de_participants/2
        if moitie_des_participants is int:
            paire = []
            ronde_actuelle = ronde.Ronde("round" + str(self.numero_de_ronde), datetime.datetime.now())
            for i in range(moitie_des_participants):
                paire.append([i,(moitie_des_participants+i)])
                match_pairing = match.Match(self.instance_tournoi.nombre_de_participants[i], self.instance_tournoi.nombre_de_participants[(moitie_des_participants+i)])
                ronde_actuelle.liste_matchs.append(match_pairing)
            # print(ronde_actuelle.__str__())
            return ronde_actuelle
        else:
            print("Le nombre de joueur n'est pas paire.")
