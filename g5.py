import random
import pgzrun

WIDTH = 500
HEIGHT = 500
MAX_BULLETS = 3
level = 1
lives = 3
score = 0
bg = Actor('bg1')
p = Actor('player',(100,280))

enemies = []
bullets = []
bombs = []
def draw():
    screen.clear() 
    bg.draw()
    p.draw()
    for enemy in enemies:
        enemy.draw()
    for bullet in bullets:
        bullet.draw()
    for bomb in bombs:
        bomb.draw()
    draw_text()        

def update(delta):
    move_player()
    move_bullets()
    move_enemies()
    create_bombs()
    move_bombs()
    check_for_end_of_level()

def create_enemies():
    for x in range(0,50,60):
        for y in range(0,200,60):
            enemy = Actor ('enemy',(x,y))
            enemies.append(enemy)
def move_player():

    if keyboard.right:
        p.x = p.x + 5
    if keyboard.left:
        p.x = p.x - 5
    if p.x > WIDTH:
        p.x = WIDTH
    if p.x < 0:
        p.x = 0

def  move_enemies():
    global score
    for enemy in enemies:
        enemy.x = enemy.x + enemy.x
        if enemy.x > WIDTH or enemy.x < 0:
            enemy.x = - enemy.x
            animate(enemy, duration = 0.1, y = enemy.y + 60)
        for bullet in bullets:
            if bullet.colliderect(enemy):
                enemies.remove(enemy)  
                bullets.remove(bullet)
                score = score + 1
        if enemy.colliderect(p):
               exits()

def draw_text():
    screen.draw.text("Level" + str(level), (0,0), color = 'red')
    screen.draw.text("Score" + str(score), (100,0), color = 'red')
    screen.draw.text("Lives" + str(lives), (200,0), color = 'red')


def on_key_down(key):
    if key == keys.SPACE and len(bullets) < MAX_BULLETS:
        bullet = Actor('bullets', pos = (p.x, p.y))
        bullets.append(bullet)    
   
def move_bullets():
    for bullet in bullets:
        bullet.y = bullet.y - 6
        if bullet.y < 0:
            bullets.remove(bullets) 

def create_bombs():
    if random.randint(0,100 - level * 6) == 0:
        enemy = random.choice(enemies)
        bomb = Actor('bomb',enemy.pos)
        bombs.append(bomb)            

def move_bombs():
    global lives
    for bomb in bombs:
        bomb.y = bomb.y + 10
        if bomb.colliderect(p):
            bombs.remove(bomb)
            lives = lives - 1
            if lives == 0:
                exit()   

def check_for_end_of_level():
    global level
    if len(enemies) == 0:
        level = level + 1
        create_enemies() 


pgzrun.go()