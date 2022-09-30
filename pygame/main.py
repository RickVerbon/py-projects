import sys, pygame
import requests
import random


def get_pkmn():
    rnd = random.randint(0, 900)
    res = requests.get('https://pokeapi.co/api/v2/pokemon/' + str(rnd))
    pkmn = res.json()
    pkmn = {
        'name': pkmn['name'],
        'spriteurl': pkmn['sprites']['front_default']
    }
    img_data = requests.get(pkmn['spriteurl']).content    
    with open('pkmn.png', 'wb') as handler:
        handler.write(img_data)
    return pkmn

white = 255,255,255
black = 0,0,0


pygame.init() #initialize pygame
pkmn = get_pkmn()

font = pygame.font.Font(None, 32)
text = font.render("A wild " + pkmn['name'] +" appeared", True, black)
textrect = text.get_rect()

size = width, height = 320, 240


screen = pygame.display.set_mode(size) #setting the size of the screen
pkmn_sprite = pygame.image.load('./pkmn.png')
#pkmnrect = pkmn_sprite.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    
    screen.fill(white)
    
    screen.blit(text, textrect)
    screen.blit(pkmn_sprite, (90,40))
    pygame.display.flip()





