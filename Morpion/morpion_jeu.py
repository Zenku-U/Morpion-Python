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
        self.couleur = (139,137,137)
        self.grille = pygame.image.load("assets/grille.png").convert_alpha()

        self.mouse_pos = position()
        
    
    def update(self):
        self.ecran.fill(self.couleur)
        self.ecran.blit(self.grille, (261,36))
        self.mouse_pos.update()

#icons du triangle et du carré
class icon:
    def __init__(self, screen, image):
        self.ecran = screen
        self.image = pygame.image.load(f"assets/{image}.png").convert_alpha()

#detection de la position de la souris
class position:
    def __init__(self):
        self.pos = None

    def update(self):
        self.pos = pygame.mouse.get_pos()

        if self.pos[0] > 261 and self.pos[0] < 476 and self.pos[1] > 36 and self.pos[1] < 225:
            

        if self.pos[0] > 481 and self.pos[0] < 668 and self.pos[1] > 36 and self.pos[1] < 225:
            
        
        if self.pos[0] > 673 and self.pos[0] < 890 and self.pos[1] > 36 and self.pos[1] < 225:
            

        if self.pos[0] > 261 and self.pos[0] < 476 and self.pos[1] > 231 and self.pos[1] < 416:
            

        if self.pos[0] > 481 and self.pos[0] < 668 and self.pos[1] > 231 and self.pos[1] < 416:
            

        if self.pos[0] > 673 and self.pos[0] < 890 and self.pos[1] > 231 and self.pos[1] < 416:
            

        if self.pos[0] > 261 and self.pos[0] < 476 and self.pos[1] > 421 and self.pos[1] < 611:
            

        if self.pos[0] > 481 and self.pos[0] < 668 and self.pos[1] > 421 and self.pos[1] < 611:
            

        if self.pos[0] > 673 and self.pos[0] < 890 and self.pos[1] > 421 and self.pos[1] < 611:
            




        
        




               




main()