# Projet : Développez un programme logiciel en Python de gestion de tournois d'échecs


*Auteur : Grégory ALLEN*

## Fonctionnalité : 

Le programme permet de gérer des tournois d'échecs.
Il permet de :
  - Gérer une liste de joueur pouvant participer à un tournoi
    - Ajouter/Modifier des joueurs à cette liste
    - Consulter la liste de ces joueurs
    - Utiliser ces joueurs dans la création d'un tournoi d'échec
  - Créer un tournoi en renseignant :
    - La méthode de comptage de points
    - Le nombre de participants et leurs nom
    - Le nom du tournoi
    - La localisation du tournoi
    - Les dates de début et fin de tournoi
    - Le nombre de tour
    - Le type de contrôle de temps
    - Des commentaires
  - Lancer le prochain tour d'un tournoi en cours
  - Stocker un tournoi en cours
  - Reprendre un tournoi stocké
  - Consulter :
    - La liste des joueurs
    - La liste des participants à un tournoi en cours
    - La liste des tournois
    - La liste des tours d'un tournoi
    - La liste des matchs d'un tour d'un tournoi.

## Limitation :

## Installation et utilisation :
  
### Créer un environnement virtuel Python : 
 
- #### En ligne de commande, se placer dans le répertoire de travail désiré :

  - sous Windows, saisir :

  `cd \chemin\vers_le\repertoire_desire` 

  - sous Linux, saisir :
   
  `cd chemin/vers_le/repertoire_desire`
     
- #### Créer un environnement virtuel dans le repertoire de travail désiré :
 
  - sous Windows, saisir :

  `python -m venv env`  

  - sous Linux, saisir :
   
  `python3 -m venv env`
   
- #### Activer l'environnement virtuel
       
  - sous Windows, saisir : 
       
  `env\Scripts\activate.bat`
       
  - sous Linux, saisir : 
      
  `source env/bin/activate`  

### Préparer l'environnement virtuel pour qu'il puisse lancer notre script

- #### Télécharger les fichiers du dépot Github et placer ces fichiers dans *chemin/vers_le/repertoire_desire/*  

- #### Récupérer les modules / packages nécessaires pour faire fonctionner notre script :
    
    Toujours en étant dans */chemin/vers_le/repertoire_desire* saisir :  
    
    `pip install -r requirements.txt`

### Lancer notre script de récupération d'informations  

- #### En ligne de commande, toujours en étant dans *chemin/vers_le/repertoire_desire*, saisir :

  - sous Windows, saisir :
       
  `python .\main.py`
       
  - sous Linux, saisir : 
      
  `python3 main.py`  
    
## Résultat attendu :  

- Le programme va créer un fichier db.json à son premier lancement.

- Il va ensuite afficher un menu qui donnera accès à toutes les options disponibles.
