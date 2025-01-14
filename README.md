1 - Les règles du jeu
Deux joueurs s’affrontent sur un plateau carré comportant n
lignes et n
colonnes, où n est un entier pair.
Par défaut n=8

Chaque joueur dispose de deux types de pièces :

Une reine qui se déplace orthogonalement ou en diagonale vers une case vide non nécessairement adjacente, mais à la condition que toutes les cases alignées entre sa position de départ et sa position d'arrivée soient vides (à l'instar d'une reine aux échecs mais sans la possibilité de prendre une éventuelle pièce adverse se situant sur la case d'arrivée).
Une tour qui se déplace orthogonalement vers une case vide non nécessairement adjacente, mais à la condition que toutes les cases alignées entre sa position de départ et sa position d'arrivée soient vides (à l'instar d'une tour aux échecs mais sans la possibilité de prendre une éventuelle pièce adverse se situant sur la case d'arrivée).
Chaque joueur possède initialement une reine et n2//4−1
 tours disposées initialement comme suit (le premier joueur a ici les pièces de couleur bleue et mauve et le second de couleur rouge et orange) :

Exemple de déplacement suite à la configuration initiale précédente, le premier joueur bouge l'une de ses tours après l'avoir sélectionnée :

Après qu'un joueur ait déplacé l'une de ses tours selon les règles ci-dessus, des captures sont possibles. Si la position finale de la tour en question n'est ni sur la même ligne ni sur la même colonne que la reine du même joueur, ces deux pièces forment alors deux sommets d'une même diagonale d'un rectangle virtuel. Si une ou deux tours du joueur adverse sont alors situées sur un ou deux des autres sommets de ce rectangle elles sont capturées.

Cette règle de capture ne s'applique qu'après le déplacement d'une tour et non d'une reine, et seules les tours adverses peuvent être capturées et non la reine adverse.

Exemple d'une prise avec le second joueur qui sélectionne sa tour située sur la quatrième ligne et sixième colonne, qui la déplace vers la septième ligne et sixième colonne ce qui capture la tour du premier joueur qui était située sur la septième ligne et huitième colonne :

Un peu plus tard dans la partie, exemple de déplacement en diagonal de la reine du second joueur :

Dès qu'un joueur n'a plus que deux pièces ou moins (au cumul de sa reine et de ses tours) il a perdu la partie.

Exemple avec une victoire du second joueur :


2 - Implémentation de ce jeu en Python
L'usage de la librairie graphique Tkinter est obligatoire, tout autre choix ne sera pas pris en compte.

Une approche orientée objet est obligatoire et le principe d'encapsulation devra être scrupuleusement respecté. Dans le cas contraire le projet sera directement recalé.

Vous implémenterez au minimum deux classes :

Une classe "joueur" avec (au moins) pour attributs les coordonnées de sa reine sur un plateau ainsi que son nombre de pièces restantes.
Une classe "jeu" avec plusieurs attributs à déterminer dont l'un d'eux sera une liste à deux dimensions modélisant le plateau de jeu.
Le design de l'application est libre (on pourra par exemple choisir les couleurs, les formes des pièces, etc.) mais votre programme devra au moins comporter les fonctionnalités suivantes :

Choix de la dimension du plateau via un menu, le nombre de lignes et de colonnes devant être pair et compris entre 6 et 12.
Affichage du plateau (quadrillage et pièces) et du joueur dont c'est le tour.
À chaque tour de jeu, sélection à la souris par le joueur dont c'est le tour de la pièce qu'il souhaite déplacer (conformément aux règles du jeu, i.e. il ne pourra pas sélectionner une pièce de l'adversaire ou l'une de ses pièces ne pouvant se déplacer). On visualisera cette sélection en entourant par exemple la pièce en question par un cercle (voir captures d'écran de la première partie du sujet).
À chaque tour de jeu, sélection à la souris par le joueur dont c'est le tour de la position finale de la pièce qu'il a précédemment sélectionnée (conformément aux règles du jeu).
Déplacements des pions et captures éventuelles.
Gestion des tours de jeu et de l'alternance des joueurs.
Condition de victoire.
Gestion de la fin de partie (affichage du résultat, proposition d'une nouvelle partie, etc.).
On prendra soin de découpler au maximum les méthodes algorithmiques, i.e. celles qui interagissent avec la structure de données modélisant le plateau, des méthodes graphiques qui elles s'occupent de l'affichage et de la gestion des événements.


3 - Bonus
Les bonus suivants sont facultatifs et ne rentrent donc pas dans le barème de base. Ils apporteront des points supplémentaires et la satisfaction personnelle du devoir accompli.

Prévisualisation des coups jouables.
Sauvegarde d'une partie dans un fichier texte, et reprise de celle-ci ultérieurement.
Animations visuelles et/ou sonores lors du déplacement des pions et des captures.
Mode de jeu individuel contre l'ordinateur, celui-ci jouant de façon aléatoire (ou intelligemment).
