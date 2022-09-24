class Tournoi:
    """ Contient les informations du tournoi """
    def __init__(self,  nom_du_tournoi, lieu_du_tournoi,
                 date_du_tournoi, type_de_controle_du_temps,
                 nombre_de_participants, nombre_de_tour_du_tournoi=4,
                 commentaire=""):
        self.nom_du_tournoi = nom_du_tournoi
        self.lieu_du_tournoi = lieu_du_tournoi
        self.date_du_tournoi = date_du_tournoi
        self.nombre_de_tour_du_tournoi = nombre_de_tour_du_tournoi
        self.type_de_controle_du_temps = type_de_controle_du_temps
        self.nombre_de_participants = nombre_de_participants
        self.commentaire = commentaire
        self.participants = []
        self.rondes = []

    def __str__(self):
        return("Le tournoi {name} se déroulant à {lieu} le {date1}, a {nombre_tours} en {controle_temps}. Il y a "
               "{nombre_participants} participants, qui sont entre autre {participant1} et {participant2}".format(
                date1=self.date_du_tournoi[0], nombre_tours=self.nombre_de_tour_du_tournoi, name=self.nom_du_tournoi,
                controle_temps=self.type_de_controle_du_temps, nombre_participants=self.nombre_de_participants,
                participant1=self.participants[0], participant2=self.participants[1],
                lieu=self.lieu_du_tournoi, sep=" "))
