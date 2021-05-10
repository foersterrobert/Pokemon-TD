import pygame
import sys
from tower import *
from enemy import *
from settings import *
from node import *
from icons import *
from label import Label
from bullet import Bullet
import random

class TD:
    def __init__(self):
        pygame.init()
        self.total_rows = TOTAL_ROWS
        self.WIDTH = WIDTH
        self.gap = GAP
        self.screen = pygame.display.set_mode((self.WIDTH+200, self.WIDTH+45))
        pygame.display.set_caption("TD Pokémon")
        self.movement = 0
        self.clock = pygame.time.Clock()
        
        self.money = 20000
        self.hp = 10
        self.wave = 1

        self.sLabel = Label(self.screen, 30, 810)

        self.pathway = [Path(self.screen, 1, 1, self.gap, self.total_rows), Path(self.screen, 2, 1, self.gap, self.total_rows), Path(self.screen, 3, 1, self.gap, self.total_rows),
                        Path(self.screen, 4, 1, self.gap, self.total_rows), Path(self.screen, 4, 2, self.gap, self.total_rows), Path(self.screen, 4, 3, self.gap, self.total_rows),
                        Path(self.screen, 3, 3, self.gap, self.total_rows), Path(self.screen, 2, 3, self.gap, self.total_rows), Path(self.screen, 1, 3, self.gap, self.total_rows),
                        Path(self.screen, 1, 4, self.gap, self.total_rows), Path(self.screen, 1, 5, self.gap, self.total_rows), Path(self.screen, 2, 5, self.gap, self.total_rows),
                        Path(self.screen, 2, 6, self.gap, self.total_rows), Path(self.screen, 3, 6, self.gap, self.total_rows), Path(self.screen, 4, 6, self.gap, self.total_rows),]
        
        self.pathway[0].image = pygame.image.load("./images/Start.jpg")
        self.pathway[0].image = pygame.transform.scale(self.pathway[0].image, (GAP, GAP))
        
        self.pathway[-1].image = pygame.image.load("./images/End.jpg")
        self.pathway[-1].image = pygame.transform.scale(self.pathway[-1].image, (GAP, GAP))

        self.grid = [[Node(self.screen, 0, 0, self.gap, self.total_rows), Node(self.screen, 1, 0, self.gap, self.total_rows), Node(self.screen, 2, 0, self.gap, self.total_rows), 
            Node(self.screen, 3, 0, self.gap, self.total_rows), Node(self.screen, 4, 0, self.gap, self.total_rows), Node(self.screen, 5, 0, self.gap, self.total_rows), 
            Node(self.screen, 6, 0, self.gap, self.total_rows), Node(self.screen, 7, 0, self.gap, self.total_rows)], 
            
            [Node(self.screen, 0, 1, self.gap, self.total_rows), self.pathway[0], 
            self.pathway[1], self.pathway[2], self.pathway[3],
            Node(self.screen, 5, 1, self.gap, self.total_rows), Node(self.screen, 6, 1, self.gap, self.total_rows), Node(self.screen, 7, 1, self.gap, self.total_rows),],
            
            [Node(self.screen, 0, 2, self.gap, self.total_rows), Node(self.screen, 1, 2, self.gap, self.total_rows), 
            Node(self.screen, 2, 2, self.gap, self.total_rows), Node(self.screen, 3, 2, self.gap, self.total_rows), self.pathway[4],
            Node(self.screen, 5, 2, self.gap, self.total_rows), Node(self.screen, 6, 2, self.gap, self.total_rows), Node(self.screen, 7, 2, self.gap, self.total_rows)], 
            
            [Node(self.screen, 0, 3, self.gap, self.total_rows), self.pathway[8], 
            self.pathway[5], self.pathway[6], self.pathway[7],
            Node(self.screen, 5, 3, self.gap, self.total_rows), Node(self.screen, 6, 3, self.gap, self.total_rows), Node(self.screen, 7, 3, self.gap, self.total_rows)],

            [Node(self.screen, 0, 4, self.gap, self.total_rows), self.pathway[9], 
            Node(self.screen, 2, 4, self.gap, self.total_rows), Node(self.screen, 3, 4, self.gap, self.total_rows), Node(self.screen, 4, 4, self.gap, self.total_rows),
            Node(self.screen, 5, 4, self.gap, self.total_rows), Node(self.screen, 6, 4, self.gap, self.total_rows), Node(self.screen, 7, 4, self.gap, self.total_rows)],

            [Node(self.screen, 0, 5, self.gap, self.total_rows), self.pathway[10], 
            self.pathway[11], Node(self.screen, 3, 5, self.gap, self.total_rows), Node(self.screen, 4, 5, self.gap, self.total_rows),
            Node(self.screen, 5, 5, self.gap, self.total_rows), Node(self.screen, 6, 5, self.gap, self.total_rows), Node(self.screen, 7, 5, self.gap, self.total_rows)], 
            
            [Node(self.screen, 0, 6, self.gap, self.total_rows), Node(self.screen, 1, 6, self.gap, self.total_rows), 
            self.pathway[12], self.pathway[13], self.pathway[14],
            Node(self.screen, 5, 6, self.gap, self.total_rows), Node(self.screen, 6, 6, self.gap, self.total_rows), Node(self.screen, 7, 6, self.gap, self.total_rows)],

            [Node(self.screen, 0, 7, self.gap, self.total_rows), Node(self.screen, 1, 7, self.gap, self.total_rows), 
            Node(self.screen, 2, 7, self.gap, self.total_rows), Node(self.screen, 3, 7, self.gap, self.total_rows), Node(self.screen, 4, 7, self.gap, self.total_rows),
            Node(self.screen, 5, 7, self.gap, self.total_rows), Node(self.screen, 6, 7, self.gap, self.total_rows), Node(self.screen, 7, 7, self.gap, self.total_rows)],
            ]
    
        self.towers = []
        self.enemies = []
        self.icons = []

        self.towerChoose = 'Taubsi'
        self.towerPrices = {'Taubsi': 80, 'Glumanda': 140, 'Dratini': 190}

        self.taubsiIMG = TaubsiIMG(self.screen, self.towerPrices['Taubsi'], 820, 20)
        self.glumandaIMG = GlumandaIMG(self.screen, self.towerPrices['Glumanda'], 820, 205)
        self.dratiniIMG = DratiniIMG(self.screen, self.towerPrices['Dratini'], 820, 390)

        self.icons.append(self.taubsiIMG)
        self.icons.append(self.glumandaIMG)
        self.icons.append(self.dratiniIMG)

        self.move_enemy_event = pygame.USEREVENT + 1
        self.spawn_enemy_event = pygame.USEREVENT + 2
        self.tower_fire_event = pygame.USEREVENT + 3
        self.move_bullets_event = pygame.USEREVENT + 4

        self.multiplier = 1
        self.spawns = 0

        pygame.time.set_timer(self.move_bullets_event, 100)
        pygame.time.set_timer(self.move_enemy_event, round(100/self.multiplier))
        pygame.time.set_timer(self.spawn_enemy_event, round(2800/self.multiplier))
        pygame.time.set_timer(self.tower_fire_event, 200)

        self.wave1 = [Mauzi(self.screen, self.pathway[0].x+GAP//2, self.pathway[0].y+GAP//2), Mauzi(self.screen, self.pathway[0].x+GAP//2, self.pathway[0].y+GAP//2),
        Mauzi(self.screen, self.pathway[0].x+GAP//2, self.pathway[0].y+GAP//2), Mauzi(self.screen, self.pathway[0].x+GAP//2, self.pathway[0].y+GAP//2),
        Mauzi(self.screen, self.pathway[0].x+GAP//2, self.pathway[0].y+GAP//2), Mauzi(self.screen, self.pathway[0].x+GAP//2, self.pathway[0].y+GAP//2),
        Mauzi(self.screen, self.pathway[0].x+GAP//2, self.pathway[0].y+GAP//2), Smogmog(self.screen, self.pathway[0].x+GAP//2, self.pathway[0].y+GAP//2)]

        # self.wave2 = [Mauzi(self.screen, self.pathway[0].x+GAP//2, self.pathway[0].y+GAP//2), Mauzi(self.screen, self.pathway[0].x+GAP//2, self.pathway[0].y+GAP//2),
        # Mauzi(self.screen, self.pathway[0].x+GAP//2, self.pathway[0].y+GAP//2), Smogmog(self.screen, self.pathway[0].x+GAP//2, self.pathway[0].y+GAP//2),
        # Smogmog(self.screen, self.pathway[0].x+GAP//2, self.pathway[0].y+GAP//2), Mauzi(self.screen, self.pathway[0].x+GAP//2, self.pathway[0].y+GAP//2),
        # Mauzi(self.screen, self.pathway[0].x+GAP//2, self.pathway[0].y+GAP//2), Smogmog(self.screen, self.pathway[0].x+GAP//2, self.pathway[0].y+GAP//2)]

        # self.wave3 = [Woingenau(self.screen, self.pathway[0].x+GAP//2, self.pathway[0].y+GAP//2), Woingenau(self.screen, self.pathway[0].x+GAP//2, self.pathway[0].y+GAP//2)]
        # self.wave4 = []
        # self.wave5 = []

        while True:
            # if self.hp > 0:
            #     self.clock.tick(40)
            self.check_events()
            self.update_screen()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == self.tower_fire_event:
                self.tower_fire()

            if event.type == self.move_bullets_event:
                self.move_bullets()

            if event.type == self.move_enemy_event:
                self.move_enemy()

            if event.type == self.spawn_enemy_event:
                self.spawn_enemy()

            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if pos[0] < 800:
                    row, col = self.get_clicked_pos(pos)
                    tile = self.grid[col][row]
                    if event.button == 1:
                        if tile.__str__() == 'Node':
                            if tile.rImage == "./images/BG1.jpg":
                                if not tile.tower and self.money >= self.towerPrices[self.towerChoose]:
                                    if self.towerChoose == 'Taubsi':
                                        Ntower = Taubsi(self.screen, row, col)

                                    elif self.towerChoose == 'Glumanda':
                                        Ntower = Glumanda(self.screen, row, col)

                                    elif self.towerChoose == 'Dratini':
                                        Ntower = Dratini(self.screen, row, col)

                                    self.towers.append(Ntower)
                                    tile.tower = Ntower
                                    self.money -= Ntower.price

                                elif tile.tower and self.money >= tile.tower.upgradeCost[tile.tower.level - 2] and tile.tower.level < tile.tower.maxLevel:
                                    self.money -= tile.tower.upgradeCost[tile.tower.level - 2]
                                    tile.tower.upgrade()

                    else:
                        if tile.__str__() == 'Node' and tile.tower:
                            otower = tile.tower
                            self.money += round(otower.price * .8)
                            self.towers.remove(otower)
                            tile.tower = None

                if pos[0] > 820 and pos[0] < 820 + 150:
                    if pos[1] > self.taubsiIMG.rect.y and pos[1] < self.taubsiIMG.rect.y + self.taubsiIMG.rect.height:
                        self.towerChoose = self.taubsiIMG.name

                    elif pos[1] > self.glumandaIMG.rect.y and pos[1] < self.glumandaIMG.rect.y + self.glumandaIMG.rect.height:
                        self.towerChoose = self.glumandaIMG.name

                    elif pos[1] > self.dratiniIMG.rect.y and pos[1] < self.dratiniIMG.rect.y + self.dratiniIMG.rect.height:
                        self.towerChoose = self.dratiniIMG.name


    def get_clicked_pos(self, pos):
        y, x = pos
        row = y // GAP
        col = x // GAP
        return row, col

    def update_screen(self):
        self.screen.fill((181,168, 220))
        for row in self.grid:
            for tile in row:
                tile.draw()
        
        # for i in range(TOTAL_ROWS):
        #     pygame.draw.line(self.screen, GREY, (0, i * self.gap), (self.WIDTH, i * self.gap))
        
        # for j in range(TOTAL_ROWS):
        #     pygame.draw.line(self.screen, GREY, (j * self.gap, 0), (j * self.gap, self.WIDTH))
        
        for tower in self.towers:
            for bullet in tower.bullets:
                bullet.draw()

            tower.draw(self.money)

        for enemy in self.enemies:
            enemy.draw()

        for icon in self.icons:
            icon.draw(self.towerChoose)
        
        self.sLabel.draw(f'HP: {self.hp}   Wave: {self.wave}   Money: {self.money}$')
        pygame.display.update()

    def move_enemy(self):
        rEnemy = None
        for enemy in self.enemies:
            if enemy.i == len(self.pathway) - 1:
                rEnemy = enemy

            else:
                nPath = self.pathway[enemy.i+1]
                if enemy.rect.centerx < nPath.x + GAP//2:
                    enemy.rect.centerx += enemy.speed

                if enemy.rect.centerx > nPath.x + GAP//2:
                    enemy.rect.centerx -= enemy.speed

                if enemy.rect.centery < nPath.y + GAP//2:
                    enemy.rect.centery += enemy.speed

                elif enemy.rect.centery > nPath.y + GAP//2:
                    enemy.rect.centery -= enemy.speed

                if abs(enemy.rect.centerx - nPath.x - GAP//2) <= 40 and abs(enemy.rect.centery - nPath.y - GAP//2) <= 40:
                    enemy.i += 1

        if rEnemy:
            self.enemies.remove(rEnemy)
            self.hp -= 1

            if self.hp < 1:
                sys.exit()

    def spawn_enemy(self):
        if self.spawns == 10:
            self.multiplier += .3
            self.spawns = 0
            self.money += 20
            self.wave += 1

        self.spawns += 1

        if self.wave == 1:
            if len(self.wave1) > 0:
                spawn = self.wave1[0]
                spawn.max_hp *= self.multiplier
                spawn.hp *= self.multiplier
                self.enemies.append(spawn)
                self.wave1.remove(spawn)

        elif self.wave > 1:
            rEnemy = random.randint(1, 3)
            if rEnemy == 1:
                spawn = Mauzi(self.screen, self.pathway[0].x+GAP//2, self.pathway[0].y+GAP//2)
                spawn.max_hp *= self.multiplier
                spawn.hp *= self.multiplier
                self.enemies.append(spawn)

            if rEnemy == 2:
                spawn = Smogmog(self.screen, self.pathway[0].x+GAP//2, self.pathway[0].y+GAP//2)
                spawn.max_hp *= self.multiplier
                spawn.hp *= self.multiplier
                self.enemies.append(spawn)

            if rEnemy == 3:
                spawn = Woingenau(self.screen, self.pathway[0].x+GAP//2, self.pathway[0].y+GAP//2)
                spawn.max_hp *= self.multiplier
                spawn.hp *= self.multiplier
                self.enemies.append(spawn)



    def tower_fire(self):
        for tower in self.towers:
            for enemy in self.enemies:
                if abs(tower.rect.centerx - enemy.rect.centerx) < tower.range and abs(tower.rect.centery - enemy.rect.centery) < tower.range:
                    if len(tower.bullets) < tower.ammo:
                        tower.bullets.append(Bullet(self.screen, tower.rect.centerx, tower.rect.centery, int(enemy.rect.centerx), int(enemy.rect.centery), tower.bsize, tower.bulletIMG))
                    break

    def move_bullets(self):
        for tower in self.towers:
            for bullet in tower.bullets:
                dx = bullet.x - bullet.ex
                dy = bullet.y - bullet.ey
                d = abs(dx) + abs(dy)
                if d > tower.speed - 1:
                    dyp = abs(dy) / d

                    if dx > 0:
                        bullet.x -= round(tower.speed * (1 - dyp))

                    elif dx < 0:
                        bullet.x += round(tower.speed * (1 - dyp))

                    if dy > 0:
                        bullet.y -= round(tower.speed * (dyp))

                    if dy < 0:
                        bullet.y += round(tower.speed * (dyp))

                else:
                    tower.bullets.remove(bullet)

                hitBullet = None

                for enemy in self.enemies:
                    if abs(bullet.x - enemy.rect.centerx) < enemy.rect.height / 2 and abs(bullet.y - enemy.rect.centery) < enemy.rect.height / 2:
                        hitBullet = bullet

                        enemy.hp -= tower.damage
                        if enemy.hp <= 0:
                            self.enemies.remove(enemy)
                            self.money += enemy.bounty

                            if self.wave == 1:
                                if len(self.enemies) == 0 and len(self.wave1) == 0:
                                    self.wave += 1

    
                try:
                    if hitBullet:
                        tower.bullets.remove(hitBullet)

                except:
                    pass