Ce script python reprend l'algorithme des chaines de markov pour faire de la complétion de mots.

Le dictionnaire dict.txt est une conversation de chat en anglais, l'autre fichier texte contient quelques messages en francais.

Pour utiliser ce programme:
python3 markov_chain_phrase_completion.py

Si vous ne l'avez pas il faut la librairie numpy.
pip3 install numpy


1)
Si vous utilisez un dictionnaire déjà existant, commencez à écrire un mot.
Lorsque vous souhaitez avoir une proposition sur le mot qui suivra, appuyez sur ENTREE.
Votre message s'affiche en vert, et les proposition de mots suivant s'affichent en jaune.

Vous pouvez quitter le programme à tout moment en tapant la commande quit_pg
Vous pouvez également choisir de supprimer le message contenant tous les mots que vous venez de taper: clear_message.

Sachez que lorsque vous tapez des mots, ceux-ci s'ajoutent au dictionnaire déjà existant pour enrichir les propositions de mots.
Jusquà 10 propositions peuvent être affichées, si vous en voulez plus ou moins il faut modifier la variable n_words de la fonction show_words()

2)
Sachez que vous pouvez utiliser un fichier dict.txt vide et au fur et à mesure que vous taperez des messages, il se remplira, et vous proposera des mots quand vous appuyerez sur ENTREE
