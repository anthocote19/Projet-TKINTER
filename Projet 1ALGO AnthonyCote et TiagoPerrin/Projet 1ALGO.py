import time
import tkinter as tk
from tkinter import simpledialog, messagebox 
class Joueur:
    def __init__(self, couleur_reine, couleur_tours):
        self.couleur_reine = couleur_reine
        self.couleur_tours = couleur_tours
        self.reine_position = None
        self.tours_positions = []

    def pieces(self):
        return len(self.tours_positions) + 1


class Jeu:
    def __init__(self, dimension):
        self.dimension = dimension
        self.plateau = [[None for _ in range(dimension)] for _ in range(dimension)]
        self.joueur1 = Joueur("pink", "blue")
        self.joueur2 = Joueur("orange", "red")
        self.joueur_actuel = self.joueur1
        self.piece_selectionnee = None
        self.case_selectionnee = None

        self.root = tk.Tk()
        self.root.title("Jeu de Tours")
        self.canvas = tk.Canvas(self.root, width=900, height=600)
        self.canvas.pack()

        self.canvas.bind("<Button-1>", self.selectionner_case)

        self.initialiser_plateau()
        self.dessiner_plateau()

    def initialiser_plateau(self):
        n = self.dimension
        mid = n // 2

        self.joueur1.reine_position = (n - 1, 0)
        self.plateau[n - 1][0] = ("R", "pink")
        for i in range(mid, n):
            for j in range(mid):
                if (i, j) != (n - 1, 0):
                    self.plateau[i][j] = ("T", "blue")
                    self.joueur1.tours_positions.append((i, j))

        self.joueur2.reine_position = (0, n - 1)
        self.plateau[0][n - 1] = ("R", "orange")
        for i in range(mid):
            for j in range(mid, n):
                if (i, j) != (0, n - 1):
                    self.plateau[i][j] = ("T", "red")
                    self.joueur2.tours_positions.append((i, j))


    def dessiner_plateau(self):
        self.canvas.delete("all")
        taille_case = 600 // self.dimension
        for i in range(self.dimension):
            for j in range(self.dimension):
                coor_1, coor_3 = j * taille_case, i * taille_case
                coor_2, coor_4 = coor_1 + taille_case, coor_3 + taille_case
                couleur = "white"
                if (i, j) == self.case_selectionnee:
                    couleur = "lightblue"

                self.canvas.create_rectangle(coor_1, coor_3, coor_2, coor_4, fill=couleur, outline="black")

                piece = self.plateau[i][j]
                if piece:
                    type_piece, couleur = piece
                    self.canvas.create_oval(coor_1 + 5, coor_3 + 5, coor_2 - 5, coor_4 - 5, fill=couleur)
        self.afficher_joueur_actuel()

    def afficher_joueur_actuel(self):
        self.canvas.delete("joueur_actuel")
        if self.joueur_actuel == self.joueur1:
            texte = "Tour du : Joueur 1"
        else:
            texte = "Tour du : Joueur 2"
        
        couleur = "black" 

        self.canvas.create_text(640, 300, text=texte, font=("Arial", 24), fill=couleur, anchor="w", tag="joueur_actuel")

    def joueur_apres(self):
        if self.joueur_actuel == self.joueur1:
            self.joueur_actuel = self.joueur2
        else:
            self.joueur_actuel = self.joueur1
        self.afficher_joueur_actuel()



    def previsualiser_coups_possibles(self):
        if not self.piece_selectionnee:
            return

        type_piece, (ligne_orig, colonne_orig) = self.piece_selectionnee
        taille_case = 600 // self.dimension

        for i in range(self.dimension):
            for j in range(self.dimension):
                if self.deplacement_valide(ligne_orig, colonne_orig, i, j, type_piece):
                    coor_1, coor_3 = j * taille_case, i * taille_case
                    coor_2, coor_4 = coor_1 + taille_case, coor_3 + taille_case
                    self.canvas.create_rectangle(coor_1, coor_3, coor_2, coor_4, fill="yellow", outline="black")

    def selectionner_case(self, event):
        taille_case = 600 // self.dimension
        colonne, ligne = event.x // taille_case, event.y // taille_case

        if (ligne, colonne) == self.case_selectionnee:
            self.case_selectionnee = self.piece_selectionnee = None
            self.dessiner_plateau()
            return

       
        if self.piece_selectionnee:
            self.deplacer_piece(ligne, colonne)
            return

        
        piece = self.plateau[ligne][colonne]
        if piece:
            type_piece, couleur = piece
            if self.joueur_actuel == self.joueur1:
                 couleurs_joueur = ["pink", "blue"]
            else:
                couleurs_joueur = ["orange", "red"]
            if couleur in couleurs_joueur:
                self.piece_selectionnee = (type_piece, (ligne, colonne))
                self.case_selectionnee = (ligne, colonne)
                self.dessiner_plateau()
                self.previsualiser_coups_possibles()


    def deplacement_valide(self, ligne_orig, colonne_orig, ligne, colonne, type_piece):
        if ligne < 0 or ligne >= self.dimension or colonne < 0 or colonne >= self.dimension:
            return False
        if self.plateau[ligne][colonne] is not None:
            return False
        if type_piece == "T":
            if ligne_orig == ligne:
                
                if colonne > colonne_orig:
                    for c in range(colonne_orig + 1, colonne):
                        if self.plateau[ligne][c] is not None:
                            return False
                else:
                    for c in range(colonne_orig - 1, colonne, -1):
                        if self.plateau[ligne][c] is not None:
                            return False

            elif colonne_orig == colonne:
                if ligne > ligne_orig:
                    for l in range(ligne_orig + 1, ligne):
                        if self.plateau[l][colonne] is not None:
                            return False
                else:
                    for l in range(ligne_orig - 1, ligne, -1):
                        if self.plateau[l][colonne] is not None:
                            return False

            else:
                return False  

        elif type_piece == "R":
            if ligne_orig == ligne or colonne_orig == colonne:
                return self.deplacement_valide(ligne_orig, colonne_orig, ligne, colonne, "T")
            if ligne > ligne_orig and colonne > colonne_orig:
                l, c = ligne_orig + 1, colonne_orig + 1
                while l < ligne and c < colonne:
                    if self.plateau[l][c] is not None:
                        return False
                    l += 1
                    c += 1

            elif ligne > ligne_orig and colonne < colonne_orig:
                l, c = ligne_orig + 1, colonne_orig - 1
                while l < ligne and c > colonne:
                    if self.plateau[l][c] is not None:
                        return False
                    l += 1
                    c -= 1

            elif ligne < ligne_orig and colonne > colonne_orig:
                l, c = ligne_orig - 1, colonne_orig + 1
                while l > ligne and c < colonne:
                    if self.plateau[l][c] is not None:
                        return False
                    l -= 1
                    c += 1

            elif ligne < ligne_orig and colonne < colonne_orig:
                l, c = ligne_orig - 1, colonne_orig - 1
                while l > ligne and c > colonne:
                    if self.plateau[l][c] is not None:
                        return False
                    l -= 1
                    c -= 1
            else:
                return False 

        return True


    def deplacer_piece(self, ligne, colonne):
        if self.piece_selectionnee:
            type_piece, (ligne_orig, colonne_orig) = self.piece_selectionnee

            if self.deplacement_valide(ligne_orig, colonne_orig, ligne, colonne, type_piece):
                self.plateau[ligne][colonne] = self.plateau[ligne_orig][colonne_orig]
                self.plateau[ligne_orig][colonne_orig] = None
                if type_piece == "T":
                    self.joueur_actuel.tours_positions.remove((ligne_orig, colonne_orig))
                    self.joueur_actuel.tours_positions.append((ligne, colonne))


                elif type_piece == "R":
                    self.joueur_actuel.reine_position = (ligne, colonne)

                self.capture_tours(ligne_orig, colonne_orig, ligne, colonne)
                self.piece_selectionnee = None
                self.case_selectionnee = None
                self.joueur_apres()
                self.dessiner_plateau()
                self.verifier_victoire()



    def capture_tours(self, ligne_orig, colonne_orig, ligne, colonne):
        if self.joueur_actuel == self.joueur1:
            adversaire = self.joueur2
        else:
            adversaire = self.joueur1
        if ligne != self.joueur_actuel.reine_position[0] and colonne != self.joueur_actuel.reine_position[1]:
           
            cases_a_verifier = [(ligne, self.joueur_actuel.reine_position[1]), (self.joueur_actuel.reine_position[0], colonne)]
            for case in cases_a_verifier:
                l, c = case
                
                if self.plateau[l][c] == ("T", adversaire.couleur_tours):
                    self.plateau[l][c] = None  
                    adversaire.tours_positions.remove((l, c))   
                    self.animation_visuelle(l, c)  


    def animation_visuelle(self, ligne, colonne):
        taille_case = 600 // self.dimension
        coor_1, coor_3 = colonne * taille_case, ligne * taille_case
        coor_2, coor_4 = coor_1 + taille_case, coor_3 + taille_case

        
        couleurs = ["#333333", "#666666", "#999999", "#CCCCCC", "#FFFFFF"]

        for couleur in couleurs:
            self.canvas.create_oval(coor_1 + 5, coor_3 + 5, coor_2 - 5, coor_4 - 5, fill=couleur, outline="")
            self.root.update()
            time.sleep(0.1)  

   
        self.dessiner_plateau()

    def joueur_apres(self):
        if self.joueur_actuel == self.joueur1:
            self.joueur_actuel = self.joueur2
        else:
            self.joueur_actuel = self.joueur1

    def lancer(self):
        self.root.mainloop()

    def verifier_victoire(self):
        perdant = None
        if self.joueur1.pieces() <= 2:
            perdant = "2"
        elif self.joueur2.pieces() <= 2:
            perdant = "1"
        if perdant:
            self.message = "Le joueur " + perdant + " a perdu !"
            self.canvas.unbind("<Button-1>")
            self.afficher_victoire(perdant)
            self.root.after(2000, self.afficher_fenetre_relance)

    def afficher_victoire(self, gagnant):
        texte = "Le joueur " + str(gagnant) + " a gagné !"
        self.canvas.create_text(300, 320, text=texte, font=("Arial", 24), fill="green")
    

    def afficher_fenetre_relance(self):
        reponse = messagebox.askyesno("Fin de Partie", "Voulez-vous relancer une partie ?")
        if reponse:
            self.reinitialiser_jeu()
        else:
            self.root.quit()

    def reinitialiser_jeu(self):
        self.joueur1 = Joueur("pink", "blue")
        self.joueur2 = Joueur("orange", "red")
        self.joueur_actuel = self.joueur1
        self.plateau = [[None for _ in range(self.dimension)] for _ in range(self.dimension)]
        self.initialiser_plateau()
        self.dessiner_plateau()
        self.canvas.bind("<Button-1>", self.selectionner_case)  

def demander_taille_plateau():
    taille = simpledialog.askstring("Configuration", "Entrez la taille du plateau (pair, entre 6 et 12) :")
    
    if taille is None:  
        messagebox.showerror("Erreur", "Vous devez entrer une taille pour continuer.")
        return demander_taille_plateau() 
    
    if not taille.isdigit(): 
        messagebox.showerror("Erreur", "Veuillez entrer un nombre.")
        return demander_taille_plateau()

    taille = int(taille)  

    if taille < 6 or taille > 12 or taille % 2 != 0: 
        messagebox.showerror("Erreur", "Veuillez entrer une taille paire entre 6 et 12.")
        return demander_taille_plateau()

    return taille

if __name__ == "__main__":
    taille_plateau = demander_taille_plateau()
    jeu = Jeu(taille_plateau)
    jeu.lancer() 