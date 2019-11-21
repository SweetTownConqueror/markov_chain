C'est un matin en regardant mon téléphone et en m'apprêtant à écrire un message que j'ai pris conscience que mon téléphone me proposait des mots pour me faciliter la rédaction de mon message.
Je pensais alors que derrière il y avait de complexes algorithmes d'apprentissage automatique ou de réseau de neurones, mais après quelques recherches j'ai trouvé que la plupart de ces algorithmes de prédictions de mots étaient en fait des chaines de markov.

Pour me familiariser avec ce concept de chaines de markov, et après quelques recherches je suis tombé sur ce site qui propose un implémentation rapide et simple de cet algorithme:
https://towardsdatascience.com/simulating-text-with-markov-chains-in-python-1a27e6d13fc6

J'ai donc implémenté le code dans mon script markov_chain.py, et vais vous en faire une description detaillée.
J'ai également pour projet de faire un petit script dérivé de celui-ci pour faire de la prédiction de mots en partant d'un dictionnaire vide qui s'auto-remplira en fonction des entrées de l'utilisateur et lui proposera des mots grâce à l'algorithme de chaine de markov.


Description générale:
markov_chain.py:
Ce script génère une phrase dont les mots sont choisis en fonction d'un texte auquel on applique une chaine de markov.

Description détaillée
markov_chain.py:
1)
Le script va récupérer tous les mots du texte et construire un dictionnaire à partir de ces mots.
Le dictionnaire est en fait un tableau classique, construit de la manière suivante:
tableau(mot1=>mot2, mot2=>mot3, mot3=>mot4, mot4=>mot5...) (Pour information, le mot à gauche de la flèche est appelé en programmation une "key", et le mot à droite de la flèche une "value", et on peut retrouver une value grâce à une key , exemple: tableau(mot1) retournera mot2 )
Le but est de construire un tableau qui n'a aucune key identiques.
Ainsi, si mot2 et mot3 sont identique, le tableau deviendra:
tableau(mot1=>mot2, mot2=>(mot3 ,mot4), mot4=>mot5...)
tableau(mot1=>mot2, mot2=>(mot2 ,mot4), mot4=>mot5...)

2)
Ce dictionnaire est la base pour pouvoir proposer des mots pour créer une phrase.
Pour commencer la chaine (qui est en fait un tableau contenant les mots de la phrase à générer), il faut un premier mot.
Ce mot est choisit au hasard parmi tous les mots du texte. 
Admettons que le hasard tombe sur "mot1" du texte, 
alors la chaine = (mot1)
On regarde à quelle valeur correspond ce mot1, ici il correspond à mot2 (tableau ci dessus)
alors la chaine = (mot1, mot2)
On regarde à quelle valeur correspond ce mot2, ici il correspond à (mot3, mot4) (tableau ci dessus) on tombe sur 2 valeurs, on choisit donc une de ces 2 valeurs au hasard si le hasard tombe sur mot4
alors la chaine = (mot1, mot2, mot4)
...
Et ainsi de suite jusquà ce que la chaine atteigne le nombre de mots qu'on lui aura spécifié.

3)
on a plus qu'à afficher chaque mot de notre chaine et on a une phrase générée qui est dans le même "goût" que le texte passé au script


J'ai fait le test avec mon téléphone sur un mot qu'il ne connaissait pas : "hhh"
Au début il n'avait aucun mots à me proposer.
Ensuite j'envoie le message suivant: "hhh un"
Lorsque je retape un message en écrivant "hhh", le mot suivant qui m'est proposé est "un" : il s'agit ici du dictionnaire du téléphone auquel il a rajouté la key "hhh" et value "un".
Je peux ajouter de nouvelles values à la clé hhh en utilisant hhh comme mot dans mes phrases.
Le téléphone n'affiche pas plus de 10 propositions. S'il y a une onzième value le téléphone a ses propres critères pour choisir de l'ajouter en supprimant une value déjà existante, ou de ne pas l'ajouter du tout.

