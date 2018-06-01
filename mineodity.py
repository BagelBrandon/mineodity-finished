# Imports
import pygame
import random

# Initialize game engine
pygame.init()




# Window
WIDTH = 960
HEIGHT = 720
SIZE = (WIDTH, HEIGHT)
TITLE = "Mineodity"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)


# Timer
clock = pygame.time.Clock()
refresh_rate = 60

# Stages
START = 0
PLAYING = 1
END = 2
WIN = 3
LOSE = 4

# Colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (100, 255, 100)

# Images
ship_img = pygame.image.load('assets/img/player.png')
laser_img = pygame.image.load('assets/img/bullet.png')
enemy_img = pygame.image.load('assets/img/creeper.png')
creeperh = pygame.image.load('assets/img/creeperh.png')
bomb_img = pygame.image.load('assets/img/bomb.png')
startscreen = pygame.image.load('assets/img/start.jpg')
winscreen = pygame.image.load('assets/img/finish.jpg')
ghast = pygame.image.load('assets/img/ghast.png')
ghasth = pygame.image.load('assets/img/ghasth.png')
shieldfull = pygame.image.load('assets/img/shieldfull.png')
hit1 = pygame.image.load('assets/img/hit1.png')
hit2 = pygame.image.load('assets/img/hit2.png')
hit3 = pygame.image.load('assets/img/hit3.png')
hit4 = pygame.image.load('assets/img/hit4.png')
dead = pygame.image.load('assets/img/dead.png')
lose = pygame.image.load('assets/img/lose.jpg')
ship2 = pygame.image.load('assets/img/ship2.png')
ship3 = pygame.image.load('assets/img/ship3.png')
ship4 = pygame.image.load('assets/img/ship4.png')
ship5 = pygame.image.load('assets/img/ship5.png')
background = pygame.image.load('assets/img/background.jpg')
ship_images = [ship_img, ship3, ship2, ship4, ship5]

# Fonts
FONT_SM = pygame.font.Font("assets/fonts/font.ttf", 24)
FONT_MD = pygame.font.Font("assets/fonts/font.ttf", 32)
FONT_LG = pygame.font.Font("assets/fonts/font.ttf", 64)

# Sounds
shot = pygame.mixer.Sound('assets/sounds/shot.ogg')
bowhit = pygame.mixer.Sound('assets/sounds/ehitbow.ogg')
death = pygame.mixer.Sound('assets/sounds/death.ogg')
edamage = pygame.mixer.Sound('assets/sounds/enemyhit.ogg')
damage = pygame.mixer.Sound('assets/sounds/hit.ogg')
pygame.mixer.music.load("assets/sounds/mineodity.ogg")
gdamage = pygame.mixer.Sound('assets/sounds/ghast.ogg')

def setup():
    global stage, mobs, ship, lasers, vel1, player, bombs, fleet, soundef
    vel1= [0,0]
    ship = Ship(384, 536, ship_images, damage)
    mob7 = Mob(64, 64, enemy_img, edamage)
    mob1 = Mob(128, 64, enemy_img, edamage)
    mob2 = Mob(192, 64, enemy_img, edamage)
    mob3 = Mob(256, 64, enemy_img, edamage)
    mob4 = Mob(320, 64, enemy_img, edamage)
    mob5 = Mob(384, 64, enemy_img, edamage)
    mob6 = Mob(448, 64, enemy_img, edamage)
    mob8 = Mob(96, 128, ghast, gdamage)
    mob9 = Mob(160, 128, ghast, gdamage)
    mob10 = Mob(224, 128, ghast, gdamage)
    mob11 = Mob(288, 128, ghast, gdamage)
    mob12 = Mob(352, 128, ghast, gdamage)
    mob13 = Mob(416, 128, ghast, gdamage)
    mob14 = Mob(480, 128, ghast, gdamage)
    mob15 = Mob(64, 192, enemy_img, edamage)
    mob16 = Mob(128, 192, enemy_img, edamage)
    mob17 = Mob(192, 192, enemy_img, edamage)
    mob18 = Mob(256, 192, enemy_img, edamage)
    mob19 = Mob(320, 192, enemy_img, edamage)
    mob20 = Mob(384, 192, enemy_img, edamage)
    mob21 = Mob(448, 192, enemy_img, edamage)
    mob21 = Mob(448, 192, enemy_img, edamage)
    mob22 = Mob(96, 128, ghast, gdamage)
    mob23 = Mob(160, 128, ghasth, gdamage)
    mob24 = Mob(224, 128, ghasth, gdamage)
    mob25 = Mob(288, 128, ghasth, gdamage)
    mob26 = Mob(352, 128, ghasth, gdamage)
    mob27 = Mob(416, 128, ghasth, gdamage)
    mob28 = Mob(480, 128, ghasth, gdamage)

    mobs = pygame.sprite.Group()
    
    mobs.add(mob1, mob2, mob3, mob4, mob5, mob6, mob7, mob8, mob9, mob10, mob11,
         mob12, mob13,mob14, mob15, mob16, mob17, mob18, mob19, mob20, mob21, mob22,
         mob23, mob24, mob25, mob26, mob27, mob28)
    
    soundef()
    sheild = 5

    player = pygame.sprite.Group()
    player.add(ship)
    player.score = 0

    lasers = pygame.sprite.Group()

    bombs = pygame.sprite.Group()

    fleet = Fleet(mobs)
    stage = START
# set stage
stage = START

    

# Game classes
class Ship(pygame.sprite.Sprite):
    def __init__(self, x, y, ship_images, soumd):
        super().__init__()

        self.image = ship_images[0]
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = x
        self.rect.y = y
        self.ship_images = ship_images
        self.speed = 3
        self.shield = 5

    def move_left(self):
        self.rect.x -= self.speed
        
    def move_right(self):
        self.rect.x += self.speed

    def shoot(self):
        las = Laser(laser_img)
        
        las.rect.centerx = self.rect.centerx
        las.rect.centery = self.rect.top
        
        lasers.add(las)
        shot.play()

    def update(self, bombs):
        hit_list = pygame.sprite.spritecollide(self, bombs, True, pygame.sprite.collide_mask)

        for hit in hit_list:
            self.shield -= 1
            damage.play()
                
        if self.shield == 0:
            death.play()
            self.kill()

        if self.rect.x >= WIDTH - 32:
            self.rect.x =  WIDTH- 32
        elif self.rect.x <= 0:
            self.rect.x = 0

        if self.shield == 5:
            self.image = ship_images[0]
        elif self.shield == 4:
            self.image = ship_images[1]
        elif self.shield == 3:
            self.image = ship_images[2]
        elif self.shield == 2:
            self.image = ship_images[3]
        elif self.shield == 1:
            self.image = ship_images[4]

        hit_list = pygame.sprite.spritecollide(self, mobs, False)
        if len(hit_list) > 0:
            self.shield = 0
            player.shield = 0
            death.play()
class Laser(pygame.sprite.Sprite):
    
    def __init__(self, image):
        super().__init__()

        self.image = image
        self.rect = image.get_rect()
        
        self.speed = 6

    def update(self):
        self.rect.y -= self.speed
    
    
class Mob(pygame.sprite.Sprite):
    def __init__(self, x, y, image, sound):
        super().__init__()

        self.image = image
        self.rect = image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = x
        self.rect.y = y
        self.shield = 2
        self.sound = sound
        

    def drop_bomb(self):
        bomb = Bomb(bomb_img)
        bomb.rect.centerx = self.rect.centerx
        bomb.rect.centery = self.rect.bottom
        bombs.add(bomb)
        
    def update(self, lasers, player):
        hit_list = pygame.sprite.spritecollide(self, lasers, True,  pygame.sprite.collide_mask)

        for hit in hit_list:
            self.shield -= 1
            player.score += 1
            self.sound.play()

        if self.shield == 0:
            self.sound.play()
            self.kill()


class Bomb(pygame.sprite.Sprite):
    
    def __init__(self, image):
        super().__init__()

        self.image = image
        self.rect = image.get_rect()
        
        self.speed = 3

    def update(self):
        self.rect.y += self.speed
    
    
class Fleet:

    def __init__(self, mobs):
        self.mobs = mobs
        self.bomb_rate = 10
        self.speed = 10
        self.moving_right = True
        

    def move(self):
        reverse = False

        if self.moving_right:
            for m in mobs:
                m.rect.x += self.speed
                if m.rect.right >= WIDTH:
                    reverse = True

        else:
            for m in mobs:
                m.rect.x -= self.speed
                if m.rect.left <= True:
                    reverse = True

        if reverse == True:
            self.moving_right = not self.moving_right

            for m in mobs:
                m.rect.y += 16

    def choose_bomber(self):
        rand = random.randrange(0, self.bomb_rate)
        all_mobs = mobs.sprites()
        
        if len(all_mobs) > 0 and rand == 0:
            return random.choice(all_mobs)
        else:
            return None
    
    def update(self):
        self.move()

        bomber = self.choose_bomber()
        if bomber != None:
            bomber.drop_bomb()


    def is_clear(self):
        return len(self.mobs) == 0
    

# Make sprite groups


# Game helper functions
def soundef():
    if stage == START:
        pygame.mixer.music.load("assets/sounds/begin.ogg")
    elif stage == PLAYING:
        pygame.mixer.music.load("assets/sounds/mineodity.ogg")
    elif stage == LOSE:
        pygame.mixer.music.load("assets/sounds/end.ogg")
    elif stage == WIN:
        pygame.mixer.music.load("assets/sounds/congrats.ogg")

    pygame.mixer.music.play(-1)
        
def show_title_screen():
    if stage == START:
        screen.blit(startscreen, (0, 0))

def show_win_screen():
    screen.blit(winscreen, (0,0))

def show_lose_screen():
    screen.blit(lose, (0,0))

def show_stats(player):
    score_text = FONT_MD.render(str(player.score), 1, WHITE)
    screen.blit(score_text, [32, 32])

def show_shield(player):
    if ship.shield == 5:
        screen.blit(shieldfull, [64, 672])
    if ship.shield == 4:
        screen.blit(hit1, [64, 672])
    if ship.shield == 3:
        screen.blit(hit2, [64, 672])
    if ship.shield == 2:
        screen.blit(hit3, [64, 672])
    if ship.shield == 1:
        screen.blit(hit4, [64, 672])
    if ship.shield == 0:
        screen.blit(dead, [64, 672])

setup()
soundef()


# Game loop

done = False

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
        elif event.type == pygame.KEYDOWN:
            
            if stage == START:
                if event.key == pygame.K_SPACE:
                    stage = PLAYING
                    soundef()
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    
            elif stage == PLAYING:
                if event.key == pygame.K_SPACE:
                    ship.shoot()
                    
            if stage == WIN:
                if event.key == pygame.K_r:
                    setup()
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    
            if stage == LOSE:
                if event.key == pygame.K_r:
                    setup()
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    
    if stage == PLAYING:
        pressed = pygame.key.get_pressed()
        if ship.shield == 0:
            stage = LOSE
            soundef()


        if pressed[pygame.K_LEFT]:
            ship.move_left()
        elif pressed[pygame.K_RIGHT]:
            ship.move_right()

        if fleet.is_clear():
            stage = WIN
            soundef()

        

    # Game logic (Check for collisions, update points, etc.)
    if stage == PLAYING:
        player.update(bombs)
        lasers.update()   
        mobs.update(lasers, player)
        bombs.update()
        fleet.update()


     
    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.blit(background, (0,0))
    if stage == PLAYING:
        lasers.draw(screen)
        player.draw(screen)
        bombs.draw(screen)
        mobs.draw(screen)
        show_shield(player)
        show_stats(player)

    if stage == START:
        show_title_screen()
    if stage == WIN:
        show_win_screen()
    if stage == LOSE:
        show_lose_screen()



    
    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)



# Close window and quit
pygame.quit()

