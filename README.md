1 - Rules of the game
Two players face each other on a square board with n
rows and n
columns, where n is an even integer.
By default n=8

Each player has two types of pieces:

A queen that moves orthogonally or diagonally to an empty square that is not necessarily adjacent, but on the condition that all the squares aligned between its starting position and its arrival position are empty (like a queen in chess but without the possibility of taking a possible opposing piece located on the arrival square).
A rook that moves orthogonally to an empty square that is not necessarily adjacent, but on the condition that all the squares aligned between its starting position and its arrival position are empty (like a rook in chess but without the possibility of taking a possible opposing piece located on the arrival square).
Each player initially has a queen and n2//4−1
rooks initially arranged as follows (the first player here has the blue and purple pieces and the second player has the red and orange pieces):

Example of movement following the previous initial configuration, the first player moves one of his rooks after selecting it:

After a player has moved one of his rooks according to the rules above, captures are possible. If the final position of the rook in question is neither on the same line nor on the same column as the queen of the same player, these two pieces then form two vertices of the same diagonal of a virtual rectangle. If one or two rooks of the opposing player are then located on one or two of the other vertices of this rectangle, they are captured.

This capture rule only applies after the movement of a rook and not of a queen, and only the opposing rooks can be captured and not the opposing queen.

Example of a capture with the second player who selects his tower located on the fourth row and sixth column, who moves it to the seventh row and sixth column which captures the tower of the first player which was located on the seventh row and eighth column:

A little later in the game, example of diagonal movement of the queen of the second player:

As soon as a player has only two pieces or less (cumulative of his queen and his towers) he has lost the game.

Example with a victory of the second player:

2 - Implementation of this game in Python
The use of the Tkinter graphics library is mandatory, any other choice will not be taken into account.

An object-oriented approach is mandatory and the encapsulation principle must be scrupulously respected. Otherwise the project will be directly rejected.

You will implement at least two classes:

A "player" class with (at least) as attributes the coordinates of his queen on a board as well as its number of remaining pieces.
A "game" class with several attributes to be determined, one of which will be a two-dimensional list modeling the game board.
The design of the application is free (for example, we can choose the colors, the shapes of the pieces, etc.) but your program must at least include the following features:

Choice of the size of the board via a menu, the number of rows and columns must be even and between 6 and 12.
Display of the board (grid and pieces) and the player whose turn it is.
At each turn of the game, selection with the mouse by the player whose turn it is of the piece he wishes to move (in accordance with the rules of the game, i.e. he will not be able to select an opponent's piece or one of his pieces that cannot move). We will visualize this selection by surrounding for example the piece in question with a circle (see screenshots of the first part of the subject).
At each turn of the game, the player whose turn it is selects with the mouse the final position of the piece he has previously selected (in accordance with the rules of the game).
Movement of pawns and possible captures.
Management of game turns and alternation of players.
Victory condition.
Management of the end of the game (display of the result, proposal of a new game, etc.).
Care will be taken to decouple as much as possible the algorithmic methods, i.e. those that interact with the data structure modeling the board, from the graphical methods that take care of the display and management of events.

3 - Bonuses
The following bonuses are optional and therefore do not enter into the basic scale. They will bring additional points and the personal satisfaction of duty accomplished.

Preview of playable moves.
Saving a game in a text file, and resuming it later.
Visual and/or sound animations when moving pawns and captures.
Individual game mode against the computer, which plays randomly (or intelligently).
