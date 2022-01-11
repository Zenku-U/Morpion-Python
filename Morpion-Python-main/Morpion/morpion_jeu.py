# importation des modules pygame et sys
import pygame, sys

# initialisation de pygame
pygame.init()

# fontion principale pour la fenêtre et le taux de rafraîchissement
def main():
    screen = pygame.display.set_mode((1152, 648)) # Def de la fenetre
    pygame.display.set_caption("Tic Tac Toe")
    clock = pygame.time.Clock()
    

    # boucle du jeu
    affi = affichage(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            
            

        # horloge de rafraîchissement
        affi.update()


        pygame.display.update()
        clock.tick(60)

# affiche l'image de la grille + ses paramètres
class affichage:
    def __init__(self, screen):
        self.ecran = screen
        self.couleur = (137,117,119)
        self.grille = pygame.image.load("Morpion/assets/grille.png").convert_alpha()
        
        self.play = action(screen)

        self.mouse_pos = position()

        self.vainqueur = None
        
    # fonction qui update la couleur de l'écran et qui affiche l'écran de victoire ou d'égalité
    def update(self):
        self.ecran.fill(self.couleur)
        self.ecran.blit(self.grille, (261,36))
        

        if self.vainqueur != None and self.vainqueur != "draw":
            self.ecran_du_vainqueur(self.vainqueur)
        
        elif self.vainqueur == "draw":
            self.ecran_de_égalité()

        else:
            self.vainqueur = self.play.update(self.mouse_pos.update())

# fonction du vainqueur
    def ecran_du_vainqueur(self, joueur):

        font = pygame.font.SysFont('arial rounded', 64)

        txt = "Le joueur " + joueur + " a gagné !"

        text = font.render(txt, True, (255,255,255), (0,0,0))

        self.ecran.blit(text, (self.ecran.get_width()/2 - text.get_width()/2, self.ecran.get_height()/2 - text.get_height()/2))

# fonction de l'égalité
    def ecran_de_égalité(self):

        font = pygame.font.SysFont('arial rounded', 64)

        txt = "Égalité !"

        text = font.render(txt, True, (255,255,255), (0,0,0))

        self.ecran.blit(text, (self.ecran.get_width()/2 - text.get_width()/2, self.ecran.get_height()/2 - text.get_height()/2))

        

# images des icons du triangle et du carré
class icon:
    def __init__(self, screen, image, pos):
        self.ecran = screen
        self.image = pygame.image.load(f"Morpion/assets/{image}.png").convert_alpha()
        self.pos = pos
        self.name = image

    def update(self):
        self.ecran.blit(self.image, self.pos)

#detection de la position de la souris
class position:
    def __init__(self):
        self.pos = None
        self.cadrant = 1
        
    def update(self):
        self.pos = pygame.mouse.get_pos()

        if self.pos[0] > 261 and self.pos[0] < 476 and self.pos[1] > 36 and self.pos[1] < 225:
             self.cadrant = 1
             return self.cadrant
            
        if self.pos[0] > 481 and self.pos[0] < 668 and self.pos[1] > 36 and self.pos[1] < 225:
            self.cadrant = 2
            return self.cadrant
        
        if self.pos[0] > 673 and self.pos[0] < 890 and self.pos[1] > 36 and self.pos[1] < 225:
            self.cadrant = 3
            return self.cadrant

        if self.pos[0] > 261 and self.pos[0] < 476 and self.pos[1] > 231 and self.pos[1] < 416:
            self.cadrant = 4
            return self.cadrant

        if self.pos[0] > 481 and self.pos[0] < 668 and self.pos[1] > 231 and self.pos[1] < 416:
            self.cadrant = 5
            return self.cadrant

        if self.pos[0] > 673 and self.pos[0] < 890 and self.pos[1] > 231 and self.pos[1] < 416:
            self.cadrant = 6
            return self.cadrant

        if self.pos[0] > 261 and self.pos[0] < 476 and self.pos[1] > 421 and self.pos[1] < 611:
            self.cadrant = 7
            return self.cadrant

        if self.pos[0] > 481 and self.pos[0] < 668 and self.pos[1] > 421 and self.pos[1] < 611:
            self.cadrant = 8
            return self.cadrant

        if self.pos[0] > 673 and self.pos[0] < 890 and self.pos[1] > 421 and self.pos[1] < 611:
            self.cadrant = 9
            return self.cadrant

# action du joueur gauche et du joueur droit
class action:
    def __init__(self, screen):

        self.ecran = screen

        self.turn = "left"
        #coordonnées des cadrants
        self.cadr_pos = {1:(261, 36), 2:(481,36), 3:(673,36),
                         4:(261,231), 5:(481,231), 6:(673,231),
                         7:(261,421), 8:(481,421), 9:(673,421)}
        # liste des positions qui ne sont plus jouables
        self.positions_prise = []
        # liste des icons
        self.icon_list = []
        # dictionnaire qui se remplit au fur et à mesure du jeu et qui vérifie une victoire ou une égalité
        self.pos_ecran = {1:None, 2:None, 3:None,
                          4:None, 5:None, 6:None,
                          7:None, 8:None, 9:None}

        

    def update(self, cadrant):
        # Clic gauche de la souris
        if pygame.mouse.get_pressed()[0]:
            if self.turn == "left":
                if not cadrant in self.positions_prise:
                    self.icon_list.append(icon(self.ecran, "triangle186x186", self.cadr_pos[cadrant]))
                    self.pos_ecran[cadrant] = "left"
                    self.positions_prise.append(cadrant)
                    self.turn = "right"
                    temp = self.test_victoire("left")
                    if temp == 0:
                        return "draw"
                    elif temp == 1:
                        return "left"
                    else:
                        pass
        # Clic droit de la souris         
        if pygame.mouse.get_pressed()[2]:
            if self.turn == "right":
                if not cadrant in self.positions_prise:
                    self.icon_list.append(icon(self.ecran, "square186x186", self.cadr_pos[cadrant]))
                    self.pos_ecran[cadrant] = "right"
                    self.positions_prise.append(cadrant)
                    self.turn = "left"
                    temp = self.test_victoire("right") 
                    if temp == 0:
                        return "draw"
                    elif temp == 1:
                        return "right"
                    else:
                        pass

        #petit print pour vérifier le fonctionnement du code dans la console
        print(self.pos_ecran)
        # mettre à jour les images pour les afficher
        for i in self.icon_list:
            i.update()
        return None

        #énorme fonction simplifiée qui vérifie toutes les possibilités de fin de jeu
    def test_victoire(self, joueur):
        if self.pos_ecran[1] == joueur and self.pos_ecran[2] == joueur and self.pos_ecran[3] == joueur:
            return 1 # victoire
        elif self.pos_ecran[1] == joueur and self.pos_ecran[4] == joueur and self.pos_ecran[7] == joueur:
            return 1
        elif self.pos_ecran[1] == joueur and self.pos_ecran[5] == joueur and self.pos_ecran[9] == joueur:
            return 1
        elif self.pos_ecran[2] == joueur and self.pos_ecran[5] == joueur and self.pos_ecran[8] == joueur:
            return 1
        elif self.pos_ecran[3] == joueur and self.pos_ecran[5] == joueur and self.pos_ecran[7] == joueur:
            return 1
        elif self.pos_ecran[3] == joueur and self.pos_ecran[6] == joueur and self.pos_ecran[9] == joueur:
            return 1
        elif self.pos_ecran[4] == joueur and self.pos_ecran[5] == joueur and self.pos_ecran[6] == joueur:
            return 1
        elif self.pos_ecran[7] == joueur and self.pos_ecran[8] == joueur and self.pos_ecran[9] == joueur:
            return 1
        elif len(self.icon_list) == 9:
            return 0 # égalité
        else: return None

main()