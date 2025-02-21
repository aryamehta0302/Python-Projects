import pygame
import random
import json

# Load configuration from a JSON file
with open('config.json') as config_file:
    config = json.load(config_file)

# Initialize pygame
pygame.init()

# Game Constants
WIDTH = config['WIDTH']
HEIGHT = config['HEIGHT']
WHITE = tuple(config['WHITE'])
BLACK = tuple(config['BLACK'])
GROUND_Y = HEIGHT - config['GROUND_OFFSET']
FPS = config['FPS']

# Load assets
dino_img = pygame.image.load(config['DINO_IMAGE'])
dino_img = pygame.transform.scale(dino_img, (50, 50))
dino_crouch_img = pygame.image.load(config['DINO_CROUCH_IMAGE'])
dino_crouch_img = pygame.transform.scale(dino_crouch_img, (50, 30))
cactus_img = pygame.image.load(config['CACTUS_IMAGE'])
cactus_img = pygame.transform.scale(cactus_img, (30, 50))
bird_img = pygame.image.load(config['BIRD_IMAGE'])
bird_img = pygame.transform.scale(bird_img, (40, 40))
powerup_img = pygame.image.load(config['POWERUP_IMAGE'])
powerup_img = pygame.transform.scale(powerup_img, (30, 30))

# Set up screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(config['GAME_TITLE'])
clock = pygame.time.Clock()

# Font for replay button and score
font = pygame.font.Font(None, 36)

# Sound effects
pygame.mixer.init()
jump_sound = pygame.mixer.Sound(config['JUMP_SOUND'])
collision_sound = pygame.mixer.Sound(config['COLLISION_SOUND'])

# Background
background = pygame.image.load("background.png")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# Draw replay button
def draw_replay_button():
    text = font.render("Replay", True, BLACK)
    rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    pygame.draw.rect(screen, WHITE, rect.inflate(20, 10))
    screen.blit(text, rect)
    return rect

# Dinosaur class
class Dinosaur:
    def __init__(self):
        self.x = 50
        self.y = GROUND_Y - 50
        self.vel_y = 0
        self.gravity = 1
        self.is_jumping = False
        self.is_crouching = False
        self.jump_height = -15
        self.image = dino_img
        self.has_shield = False

    def jump(self):
        if not self.is_jumping and not self.is_crouching:
            self.vel_y = self.jump_height
            self.is_jumping = True
            jump_sound.play()

    def crouch(self, state):
        self.is_crouching = state
        if state:
            self.y = GROUND_Y - 30
            self.image = dino_crouch_img
        else:
            self.y = GROUND_Y - 50
            self.image = dino_img

    def update(self):
        if not self.is_crouching:
            self.y += self.vel_y
            self.vel_y += self.gravity
            if self.y >= GROUND_Y - 50:
                self.y = GROUND_Y - 50
                self.is_jumping = False

    def draw(self):
        screen.blit(self.image, (self.x, self.y))
        if self.has_shield:
            screen.blit(powerup_img, (self.x - 10, self.y - 10))

    def get_hitbox(self):
        if self.is_crouching:
            return pygame.Rect(self.x, self.y, 50, 30)
        return pygame.Rect(self.x, self.y, 50, 50)

# Obstacle class
class Obstacle:
    def __init__(self, speed):
        self.x = WIDTH
        self.speed = speed
        self.type = random.choice(['cactus', 'bird'])
        self.y = GROUND_Y - 50 if self.type == 'cactus' else GROUND_Y - 80

    def update(self):
        self.x -= self.speed
        if self.x < -30:
            self.x = WIDTH + random.randint(200, 400)
            self.type = random.choice(['cactus', 'bird'])
            self.y = GROUND_Y - 50 if self.type == 'cactus' else GROUND_Y - 80

    def draw(self):
        if self.type == 'cactus':
            screen.blit(cactus_img, (self.x, self.y))
        else:
            screen.blit(bird_img, (self.x, self.y))

    def get_hitbox(self):
        if self.type == 'cactus':
            return pygame.Rect(self.x, self.y, 30, 50)
        return pygame.Rect(self.x, self.y, 40, 40)

# Power-up class
class PowerUp:
    def __init__(self, speed):
        self.x = WIDTH + random.randint(500, 1000)
        self.y = GROUND_Y - 40
        self.speed = speed
        self.active = True

    def update(self):
        self.x -= self.speed
        if self.x < -30:
            self.respawn()

    def respawn(self):
        self.x = WIDTH + random.randint(500, 1500)
        self.active = True

    def draw(self):
        if self.active:
            screen.blit(powerup_img, (self.x, self.y))

# Game loop
def game_loop():
    dino = Dinosaur()
    score = 0
    speed = 10
    obstacles = [Obstacle(speed)]
    powerup = PowerUp(speed)
    running = True
    game_over = False

    while running:
        screen.fill(WHITE)
        screen.blit(background, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not game_over:
                    dino.jump()
                if event.key == pygame.K_DOWN:
                    dino.crouch(True)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    dino.crouch(False)
            if game_over and event.type == pygame.MOUSEBUTTONDOWN:
                if replay_rect.collidepoint(event.pos):
                    game_loop()
                    return

        if not game_over:
            dino.update()
            for obstacle in obstacles:
                obstacle.update()
                if dino.get_hitbox().colliderect(obstacle.get_hitbox()):
                    if dino.has_shield:
                        dino.has_shield = False
                    else:
                        game_over = True
                        collision_sound.play()
                obstacle.draw()

            powerup.update()
            if powerup.active and dino.get_hitbox().colliderect(pygame.Rect(powerup.x, powerup.y, 30, 30)):
                dino.has_shield = True
                powerup.active = False
                powerup.respawn()
            powerup.draw()
            score += 1
            dino.draw()
            score_text = font.render(f"Score: {score}", True, BLACK)
            screen.blit(score_text, (10, 10))
        else:
            replay_rect = draw_replay_button()
        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()

game_loop()

