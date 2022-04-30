# Projet: Arbre B en utilisant le langage Python. 

## Auteurs: AGBA Pascal Sébastien ,  Aissatou Ibrahima Diallo 


## Présentation du projet.
Cet projet a été dévellopé par les auteurs ci-dessus dans le cadre de L'UE projet  au S6 de la L3 2022. Il question d'analyser, de modéliser et d'implémenter une sttructure de données  (clé,valeur) de stockages de données d'entiers  avec le langage python. Les fonctions ultimes sont la recherche, l'insertion, la suppression. Et l'analyse  de compléxité de chacun  de ces fonctionnalités est démandée sans   en oublier la documentation.
* Chaabane Djeraba (Responsable de l'UE)
* Monsieur Pierre Tirilly (Chargé de TP)
* Auteurs: AGBA Pascal Sébastien ,  Aissatou Ibrahima Diallo (Etudiants)

## Objectifs du projets.
Ce projet a plusieurs objectifs. Au nombres de ces objectifs, nous pouvons citer:
* L'évaluation de nos capacités à réinvestir nos connaissances d'analyses avec une téchnologie nouvelle;
* Nos aptitudes à collaborer sur un projet sur lequel nous n'avons que peux d'informations mais suffissament pour pouvoir le modéliser;
* La concrétisation de notre analyse en python en nous basant sur l'approche orienté objet;
* La rédaction des  de la documentation de nos algorithmes ainsi que leur l'auto test de ces derniers.
* L'analyse de complexité.




### Architecture du projets :
* Btree 
* Btree hérite de Node.
* import de bisect native de python.
#### Diagramme UML de Node



### Diagramme UML de <Btree>
![UML](/src/UML.jpeg)

### Lien entre les classes <Btree_Node>

![UML](/src/Heritage.jpeg)
## Documentation du travail projet
  * ## Historisque

***Inventé en 1970 par Rudolf Bayer et Edward M.McCreight, l'Arbre permet d'associér un couple (key,valeur). Le pricncipe de son fonctionnement étatnt récursif on peut s'imaginer associer à une clés une liste de valeur. Il est appéle Arbre B  ( B= balanced)  en anglais, elle vise à  avoir un nombre de descendence limité pour une Longueur  fournit.  Cette spécifité vise à limiter l'explosion des la liste des fils  dans une branche tandis que cette avoisinante sont vides.***



* ## Principe de l'algorithme d'insertion
  ***Recherche de chemin permetttant d'atteindre la branche de fils dans lequelle  il faut insérer la clée. Pour cela on recherche d'abord le parent dans lequel on pourrait insérer puis on  descends dans les feuilles au besoin. L'insertion se fait donc de manièere récursive.__path__to(key) permet donc de rechercher le schemin pour l'atteindre.***


  * ## Principe de l'algorithme de suppresion
    ***Detection du parents auquel la valeur est liée. Descente dans le fils concerné. Suppression de la valeur et reorganisation de  des fils gauches et droites au besoin.***





  * ## Principe de l'algorithme de  recherches

   ***Semblable à une interrogation de base de donnée, la recherche d'une clé dans l'arbre consiste  à la vérification de la  valeur  dans la liste des clés. En effet on cherche à savoir si trouver la valeur donné en paramètre dans  les fils d'un parents données.***

# Autres sources.

https://www.geeksforgeeks.org/ (code adapté)
https://www.youtube.com/ (vidéo recomma,dé par le professeur)


# Exemples de mise en marche de l'algorithme 





# Estimation de la complexité 



# Comment exécuter le programme? 







## Parties réalisées
* Insertion dans Btree
* Suppression dans  Btree

* Recherche dans Btree


## Parties non réalisées
B tree +. Cette partie na pas pu être abordées car nous n'avions pas fini de faire les traces des parties déjà terminé et il serait imprudent d'aller vers cette partie sans savoir si l'insertion, la suppression et la recherche se passent bien et sans bugs.  


### Raison 
Malgré l'accompagnement régulier de notre chargé de TP, le sujet est resté un peu flou dans les trois premières semaines. Nous savons ce qui est demandée mais avons décider de la modélisation mais l'implémentation est sujette à des bugs et à la nécessité de repenser et reprendre le code. On a donc été en retard dans la mise en oeuvre de son implémentation.




