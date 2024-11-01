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
