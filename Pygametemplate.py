import pygame 

#initialisation de pygame
pygame.init()

#création de la fenêtre
LARGEUR, HAUTEUR = 800, 600
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR), pygame.RESIZABLE)

#titre de la fenêtre
pygame.display.set_caption("Jeu de plateforme")

#Paramètres du jeu 
FPS = 60
running = True
clock = pygame.time.Clock()

"""
#couleur de fond
couleur = (255, 255, 255)

#remplissage fond 
fenetre.fill(couleur)

#création fond 
fond = pygame.image.load('img/fond.png')

#changement de taille fond 
fond = pygame.transform.scale(fond, (LARGEUR, HAUTEUR))

#remplir fond avec image
fenetre.blit(fond, (0,0))

#afficher texte sur le fond 
myFont = pygame.font.SysFont("Arial", 60)
myText = myFont.render("Jeu de plateforme", True, (0, 0, 0))

#afficher texte
fenetre.blit(myText, (LARGEUR/2-150, HAUTEUR/2-30))

#création personnage
personnage = pygame.Rect(LARGEUR/2-15, HAUTEUR-50, 30, 50)

#dessiner le personnage 
pygame.draw.rect(fenetre, (255, 0, 0), personnage)

#touches 
touches = pygame.key.get_pressed()

#exemple d'utilisation de touches 
if touches[pygame.K_q]:
    personnage.x -= 5

"""

#Boucle principale
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()

