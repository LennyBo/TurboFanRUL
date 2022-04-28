# NASA TurbofanRUL classifier SVC

## Extraction des données

Pour l'extraction des données, pareil que pour le NN, on a la possibilité de regroupper nCycles ensemble pour faire la classification du cycle d'aprés. 

Le scaler va fit sur le premier passage dans la fonction et puis seulement transform sur tout les passages suivant.

Ceci permet de fit sur le train, puis de transform sur le test.

## Separation des données

La séparation des données est faite en deux étapes. La premiere est de choisir un pourcentage de train val et test. Ces pourcentages vont decider le nombre de moteur de train et de test et de val. Ces moteur serons séparé des le debut.

La deuxième étape est de regrouper les cycles ensemble. Si le nombre de cycles est 3 par exemple, le résultat sera 2 features des cycles précédents 1 features du cycle actuel et le label de la classe du cycle actuel.

Dans ce dataset, il n'y a pas de nan, donc pas de fillna et pas de drop.
Par contre, le regroupement va s'assurer de ne pas mélanger les moteur et cylces afin d'eviter d'avoir des cycles précédent qui n'on rien a voir avec le cycle actuel.


## Classification

Le dataset de base est un dataset de type regression. Au lieu de faire une regression, nous avons décidé de classifier le nombre de cycles en 3 classes.

High health medium health et low health.

La raison etant qu'au cas ou on voulais implémenter le model dans un cockpit d'un avion, ça serait plus simple a comprendre pour un pilote.

Pour cette raison, les resultats sont en accuracy et non pas en mean absolute error.

## Choix de la baseline

La classification choisisent ne donne pas des classes de même probabilité. La calsse medium est plus probable que les 2 autres classes.
Pour cette raison, la baseline sera de prédire la classe medium a chaque fois.

Ceci nous donne un baseline a battre d'environ 0.48.
Il serait possible de faire des classes de même probablilité et on aurait une baseline de 0.33 dans ce cas.

