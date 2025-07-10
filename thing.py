import pygame as pg
import time

pg.init()
pg.mixer.init()
pg.mixer.music.load("assets/mus/annoyingloop.ogg")
pg.font.init()
sans = pg.font.SysFont("Comic Sans MS", 30)

windowwidth = 800
windowheight = int(windowwidth * 0.8)

window = pg.display.set_mode((windowwidth, windowheight))
pg.display.set_caption("PROJECT_UNNAMED")

clock = pg.time.Clock()
fps = 60

MoveLeft = False
MoveRight = False
MoveUp = False
MoveDown = False

bg = (100, 100, 100)

def drawbg():
    window.fill(bg)

class Entity(pg.sprite.Sprite):
    def __init__(self, species, x, y, scale, spd):
        pg.sprite.Sprite.__init__(self)
        self.species = species
        self.spd = spd
        self.facing = 1
        self.flip = False
        self.current_anim = ""
        self.anim = []
        self.frame = 0
        self.upd_time = pg.time.get_ticks()
        spr = pg.image.load(f"assets/spr/{species}/idle/0.png")
        self.scale = scale
        self.spr = pg.transform.scale(spr, (int(spr.get_width() * self.scale), int(spr.get_height() * self.scale)))
        self.hitbox = self.spr.get_rect()
        self.hitbox.center = (x, y)

    def move(self, MoveLeft, MoveRight, MoveUp, MoveDown):
        dx = 0
        dy = 0

        if MoveLeft:
            dx = -self.spd
            self.flip = True
            self.facing = -1
        if MoveRight:
            dx = self.spd
            self.flip = False
            self.facing = 1
        if MoveUp:
            dy = -self.spd
        if MoveDown:
            dy = self.spd

        self.hitbox.x += dx
        self.hitbox.y += dy

    def animate(self):
        anim_time = 100
        if pg.time.get_ticks() - self.upd_time > anim_time:
            self.upd_time = pg.time.get_ticks()
            self.frame += 1
            if self.frame >= len(self.anim):
                self.frame = 0
        self.spr = self.anim[self.frame]

    def reset_anim(self, type, length):
        if self.current_anim == type:
            return
        self.anim = []
        self.frame = 0
        for i in range(length):
            spr = pg.image.load(f"assets/spr/{self.species}/{type}/{i}.png")
            spr = pg.transform.scale(spr, (int(spr.get_width() * self.scale), int(spr.get_height() * self.scale)))
            self.anim.append(spr)
        print(f"Switched to animation: {type}")

    def create(self):
        window.blit(pg.transform.flip(self.spr, self.flip, False), self.hitbox)


class Bullet(pg.sprite.Sprite):
    def __init__(self, x, y, scale, spd):
        pg.sprite.Sprite.__init__(self)
        self.spd = spd
        spr = pg.image.load("assets/spr/bullet.png")
        self.spr = pg.transform.scale(spr, (int(spr.get_width() * scale), int(spr.get_height() * scale)))
        self.hitbox = self.spr.get_rect()
        self.hitbox.center = (x, y)

    def move(self, MoveLeft, MoveRight, MoveUp, MoveDown):
        dx = 0
        dy = 0

        if MoveLeft:
            dx = -self.spd
            self.flip = True
            self.facing = -1
        if MoveRight:
            dx = self.spd
            self.flip = False
            self.facing = 1
        if MoveUp:
            dy = -self.spd
        if MoveDown:
            dy = self.spd

        self.hitbox.x += dx
        self.hitbox.y += dy

    def create(self):
        window.blit(self.spr, self.hitbox)


protag = Entity("protag", 200, 200, 2, 5)
redguy = Entity("redguy", 400, 400, 1, 10)
bullet = Bullet(0, 0, 2, 7)

redguy_counter = 0
red_up = False
red_down = False
red_left = False
red_right = True

bullet_max = 30
bullet_counter = bullet_max
BulletUp = False
BulletDown = False
BulletLeft = False
BulletRight = False

HitRed = False
counted = False
started = False
HitBullet = False

score = 0

protag.reset_anim("idle", 2)
redguy.reset_anim("idle", 2)

Run = True
pg.mixer.music.play(-1)
playing = True
bullet_counter = 200
while Run:
    drawbg()

    clock.tick(60)

    if not HitBullet:
        protag.create()
        protag.move(MoveLeft, MoveRight, MoveUp, MoveDown)

    if counted:
        window.blit(score_text, (0, 0))

    if not HitRed:
        redguy.animate()
        redguy.create()
        redguy.move(red_left, red_right, red_up, red_down)

    if counted and not HitBullet:
        bullet.create()
        if bullet_counter == bullet_max:
            BulletUp = False
            BulletDown = False
            BulletLeft = False
            BulletRight = False
            if bullet.hitbox.left > protag.hitbox.left:
                BulletLeft = True
            if bullet.hitbox.left < protag.hitbox.left:
                BulletRight = True
            if bullet.hitbox.top > protag.hitbox.top:
                BulletUp = True
            if bullet.hitbox.top < protag.hitbox.top:
                BulletDown = True
    bullet.move(BulletLeft, BulletRight, BulletUp, BulletDown)
    bullet_counter += 1


    for event in pg.event.get():
        if event.type == pg.QUIT:
            Run = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_a:
                MoveLeft = True
                protag.reset_anim("walk_side", 2)
            if event.key == pg.K_d:
                MoveRight = True
                protag.reset_anim("walk_side", 2)
            if event.key == pg.K_w:
                MoveUp = True
                protag.reset_anim("walk_up", 4)
            if event.key == pg.K_s:
                MoveDown = True
                protag.reset_anim("walk_down", 4)

        if event.type == pg.KEYUP:
            if event.key == pg.K_a:
                MoveLeft = False
            if event.key == pg.K_d:
                MoveRight = False
            if event.key == pg.K_w:
                MoveUp = False
            if event.key == pg.K_s:
                MoveDown = False

            if not (MoveLeft or MoveRight or MoveUp or MoveDown):
                protag.reset_anim("idle", 2)

    protag.animate()

    if protag.hitbox.colliderect(redguy.hitbox):
        if not HitRed:
            pg.mixer.music.load("assets/snd/red.mp3")
            pg.mixer.music.play()
            HitRed = True
            playing = True
            gaster_timer = 0
            counted = False

    if protag.hitbox.colliderect(bullet.hitbox):
        HitBullet = True
        pg.mixer.music.load("assets/snd/dead.mp3")
        pg.mixer.music.play()

    if HitRed and not playing:
        pg.mixer.music.load("assets/mus/boss.ogg")
        pg.mixer.music.play(-1)
        playing = True

    pg.display.update()
    redguy_counter += 1
    if redguy_counter == 5:
        redguy_counter = 0
        if red_left:
            red_left = False
            red_right = True
        elif red_right:
            red_right = False
            red_left = True

    if HitRed and not counted:
        gaster_timer += 1
        if gaster_timer == 100:
            counted = True
            playing = False

    if bullet_counter > bullet_max:
        bullet_counter = 0

    if MoveUp or MoveDown or MoveLeft or MoveRight:
        bullet_max = 30
    else:
        if bullet_max > 1:
            bullet_max -= 1

    if counted and not started:
        start_time = pg.time.get_ticks()
        started = True

    if counted and not HitBullet:
        score += 1
        score_text = sans.render(f"Score: {score}", False, (0, 0, 0))


pg.quit()