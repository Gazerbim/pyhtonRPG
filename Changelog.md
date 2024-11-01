# Changelog

## Ajouts

- Ajouts d'un widget "Bar" qui permet d'afficher la barre de vie d'une entité (joueur, ennemis). Implémentation à la boucle principale du programme requise
- Ajouts d'un système de sauvegarde, permet de sauvegarder les données du joueur et de les relire. Implémentation à la boucle principale du programme requise

## Mise à jour et déplacement

- Déplacement et mise à jour de la classe [`BigTitle`](Widgets.py) et création d'une fonction `centerFont` permettant le centrage vertical d'un titre
- Mise à jour de la police 1 de la classe [`BigTitle`](Widgets.py) et ajout d'un espace
- Déplacement et mise à jour de la classe [`ChooseWidget`](Widgets.py) pour cause d'un bug important.
- Déplacement des fonctions [`MakeStripes`](utilities.py) et [`CenterText`](utilities.py)
- Mise à jour de la fonction [`main`](main.py) en ajoutant un nouveau titre de début

## Suppression

- Suppression du fichier `forms.py` car vide

## Classe [`ChooseWidget`](Widgets.py)

### Instanciation

Instanciation classique. Pas d'argument

    Syntaxe :

    widget = ChooseWidget() #Instancie 

### `add_choice` 
Permet d'ajouter un choix. Prend un argument textuel
    
    Syntaxe :

    widget.add_choice("Choix 1") #Ajoute "Choix 1" à la liste de choix

### `rmv_choice`
Permet d'effacer un choix. Prend un index (int) ou un argument textuel

    Syntaxe :

    widget.rmv_choice(0) #Supprime le choix à l'index 0

    widget.rmv_choice("Choix 2") #Supprime le choix nommé "Choix 2"

### `rmv_all_choices`
Permet de vider la liste des choix. Pas d'argument

    Syntaxe : 
    
    widget.rmv_all_choices()

### `setflag`
Permet de modifier la valeur d'un flag afin de modifier le comportement du code. Prend un argument textuel et un boolean

    Syntax : 
    
    widget.setflag("AdaptiveFlag", True) #Regle le flag "AdaptiveIndex sur "True" et change le comportement du code

#### Flags :
- AdaptiveIndex
- AllowSeveralSameOption

### Run
Déclenche la boucle du widget et permet de choisir parmi les options. Pas d'argument

    Syntax :
    
    widget.run()

Retourne le choix et peut être écrit comme ceci :
    
    Syntax :

    choice = widget.run()

Ou directement relié à un block match/case :

    Syntax :

    match widget.run():
        case 1: code1()
        case 2: code2()
        case 3: code3()
        case _: defaultcode()


## Suggestions

- Commencer le script de [`spells.py`](spells.py)
- Création d'un système de sauvegarde

N'hésitez pas à mettre vos suggestions