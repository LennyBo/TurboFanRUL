# TurboFanRUL

## Description

Ce TP à pour but d'implémenter un classificateur en se basant sur deux manières différentes :
- Neural network, en binôme
- Autre, en solo

Ce rapport est lié au Neural Network.

## Data

Les données représentent des Turbofans, plus précisément leur cycle de vie.

On a pour but de déterminer l'état de vie d'un Turbofan en fonction de ses données.

## Classification

Nous avons décidé 3 classes de moteur:
- [0] Bon (x > 150)
- [1] Ok (50 <= x <= 150>)
- [2] Mal (x < 50)

## Preprocessing

Ce chapitre explique ce qu'il y a dans le fichier Preprocessing.py.

Les titre correspondent aux fonctions de ce script.

### loadTurboFanData

lecture du fichier

### separateData

Une fois le fichier csv lu, nous séparons les données en 3 catégories :
- Test (~70%)
- Entraînement (~20%)
- Validation (~10%)

### splitDataWithCycles

Nous allons séparer les catégories de test, d'entraînement et de validation en cycles (à chaque catégorie correspond son tableau de cycles).

L'idée est d'avoir des trios, de la sorte:

Mettons un tableau de données

```python
d = [rul1, rul2, rul3, rul4, rul5, ...]`
```

Le but est de le séparer de la sorte :

```python
[[rul1, rul2, rul3], [rul2, rul3, rul4], [rul3, rul4, rul5], ...]`
```

L'idée est d'ensuite pouvoir, depuis rul1 et rul2, deviner rul3. Pareil depuis rul2 et rul3, deviner rul4, ...

Il est important de ne pas mélanger 2 moteurs, si par exemple un moteur possède 10 données, en procédant de manière "stupide" on se retrouve avec

```python
# M1 = moteur 1
# M2 = moteur 2
[[M1rule1, M1rule2, M1rule3], ..., [M1rul10, M2rul1, M2rul2], [M2rule3, M2rule4, M2rule5], ...]
```

ce qui risque de donner des valeurs incorrects ("le moteur est casi mort? Il va donc super bien aller juste après !")

On a donc vérifier que le moteur était toujours le même avant de créer le cycle correspondant.

Nous allons aussi séparer les catégories en 2 axes :
- x, les informations du moteur
- y, l'état de vie du moteur (RUL)

### classify

Une fois les cycles faits, nous classifions les "y", comme précisé dans [classification](#classification)


## Neural Network


