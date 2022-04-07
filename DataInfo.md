# Time Series Datasets

## Introduction
Ces trois datasets proviennent d'un projet effectué par l'équipe de RaD de la HE-Arc. Ils sont tous les trois des séries temporelles.

L'objectif principal avec ces données est de prédire une valeure dans le future. C'est une tâche de régression, plus d'information sur les metrics à utiliser ici: https://scikit-learn.org/stable/modules/model_evaluation.html#regression-metrics 

Ce document décrit ces trois datasets et explique le ou les objectifs pour chacuns.

Tous ces fichiers sont des `.csv` lisiblent facilement avec Pandas.  
Tip: `pandas.read_csv(filepath, index_col=0, parse_dates=True)` pour les datasets avec une date comme index principal.

## Digester
Un digester est une usine qui produit du papier ou carton à partir du bois.

### Description des données
Nom du fichier: `digester_data.csv`

Il y a environ un mois de données dans ce fichier (5968 lignes). 
Les données sont enregistrées toutes les 10 minutes.

Il y a 37 colonnes dans ce dataset. Ce sont toutes des mesures provenant de capteurs dans l'usine.  
La plus improtante est `Blow Kappa` qui mesure la qualité de la production.  
**L'objectif est de prédire ce `Blow Kappa` en utilisant les autres capteurs.**  


## NASA Turbofan
Ce dataset provient d'une expérience de la NASA. Un Turbofan est un type de moteur d'avion.
Le but de cette expérience est de mesurer la dégradation d'un moteur durant son utilisation.
Les données sont disponible en ligne sur Kaggle: https://www.kaggle.com/datasets/behrad3d/nasa-cmaps. Il y a aussi plus de documentation sur le dataset.

### Description des données
Nom du fichier: `NASA_Turbofan_RUL_data.csv`

Ce dataset est différent des deux autres car il n'y a pas de date fournie. A la place il y a un nombre de cycles de vie sous forme d'un nombre entier.

Le dataset est composé des expériences sur 100 moteurs différents. Les Moteurs sont toujours testés jusqu'à usure complète.

Il y a 20631 lignes dans le dataset.

* `unit number`: Numéro du moteur (1 à 100)
* `time (cycles)`: Temps en cycles de vie (1 à n)
* `op. setting <1-3>`: Paramètres de l'expérience (peuvent être ignorés car stable pour cette série d'expériences)
* `sensor <01-21>`: 21 différents capteurs sur le moteur. Les données sont anonymisées.
* `RUL`: "Remaining Useful Life", Nombre de cycles de vie restant avant arrêt forcé.

**L'objectif sur ce dataset est de prédire le RUL avec les données de capteurs sur le moteur.**


## Closed Cooled Water System
Ces données proviennent d'un sous-système d'une centrale de combustion des déchets.
Ce système a pour but de réfroidir l'eau utilisée dans les turbines.
Il est composé d'une pompe qui envoie l'eau vers des ventilateurs pour la refroidir.

### Description des données
Nom du fichier: `closed_cooled_water_system_data.csv`

La première colonne est la date de la mesure.  
Les données sont enregistrées toutes les 30 minutes.  
Il y a exactement **une année** de données disponible (17568 lignes).  

* `Ambient Temperature [°C]`: Temperature de l'air extérieur.
* `Temperature Before Fans [°C]`: Temperature de l'air avant les ventilateurs.
* `Temperature After Fans [°C]`: Temperature de l'air après les ventilateurs.
* `Fan Speed [%]`: Vitesse des ventilateurs, régulé automatiquement.
* `Bypass valve Position [%]`: Ouverture de la valve de bypass, permet de laisser passer de l'eau chaude.
* `Pressure Before Pumps [bar]`: Pression avant les pompes.
* `Pressure Between Pumps [bar]`: Pression à l'interieur du système.
* `Pump Motor Power [kW]`: Puissance du moteur de la pompe.

Il y a deux objectifs pour ce dataset:

* **Prédire la température après les ventilateurs.**
* **Prédire la puissance du moteur de la pompe.**

Ces deux prédictions sont à faire 30 minutes ou 1 heure dans le future.
