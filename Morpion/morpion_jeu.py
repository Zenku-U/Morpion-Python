import pygame, sys
#importation des modules pygame et sys



#initialisation de pygame
pygame.init()

#fontion principale pour la fenêtre et le taux de rafraîchissement
def main():
    screen = pygame.display.set_mode((1152, 648)) # Def de la fenetre
    pygame.display.set_caption("Tic Tac Toe")
    clock = pygame.time.Clock()
    

    #Class principal ici
    affi = affichage(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            
            

        # Event ici
        affi.update()


        pygame.display.update()
        clock.tick(60)

#affiche l'image de la grille + ses paramètres
class affichage:
    def __init__(self, screen):
        self.ecran = screen
        self.couleur = (139,26,26)
        self.grille = pygame.image.load("assets/grille.png").convert_alpha()
        
        self.play = action(screen)

        self.mouse_pos = position()
        
    
    def update(self):
        self.ecran.fill(self.couleur)
        self.ecran.blit(self.grille, (261,36))
        
        self.play.update(self.mouse_pos.update())

#icons du triangle et du carré
class icon:
    def __init__(self, screen, image, pos):
        self.ecran = screen
        self.image = pygame.image.load(f"assets/{image}.png").convert_alpha()
        self.pos = pos

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


class action:
    def __init__(self, screen):

        self.ecran = screen

        self.turn = "left"

        self.cadr_pos = {1:(261, 36), 2:(481,36), 3:(673,36),
                         4:(261,231), 5:(481,231), 6:(673,231),
                         7:(261,421), 8:(481,421), 9:(673,421)}

        self.positions_prise = []
        
        self.icon_list = []

    def update(self, cadrant):
        # Clic gauche
        if pygame.mouse.get_pressed()[0]:
            if self.turn == "left":
                if not cadrant in self.positions_prise:
                    self.icon_list.append(icon(self.ecran, "triangle", self.cadr_pos[cadrant]))
                    self.positions_prise.append(cadrant)
                    self.turn = "right"

        if pygame.mouse.get_pressed()[2]:
            if self.turn == "right":
                if not cadrant in self.positions_prise:
                    self.icon_list.append(icon(self.ecran, "square", self.cadr_pos[cadrant]))
                    self.positions_prise.append(cadrant)
                    self.turn = "left"


        print(self.turn)
                

                





        for i in self.icon_list:
            i.update()
                    
                    






        
        




               



# Clic gauche Triangle
# Clic droit Carre
main()