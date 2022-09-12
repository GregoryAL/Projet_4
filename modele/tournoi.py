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
