# Sprite classes

# Imports
import pygame as pg
from settings import *

vec = pg.math.Vector2

# Classes

class Player(pg.sprite.Sprite):

	def __init__(self, game, w, h):
		pg.sprite.Sprite.__init__(self)
		self.game = game
		self.image = pg.Surface((w, h))
		self.image.fill(BLUE)
		self.rect = self.image.get_rect()
		self.rect.center = (WIDTH / 2, HEIGHT / 2)
		self.pos = vec(WIDTH / 2, HEIGHT / 2)
		self.vel = vec(0, 0)
		self.acc = vec(0, 0)

	def jump(self):
		self.rect.y += 1
		hits = pg.sprite.spritecollide(self, self.game.platforms, False)
		self.rect.y -= 1
		if hits:
			self.vel.y = -PLAYER_JUMP

	def update(self):
		self.acc = vec(0, GRAVITY)

		keys = pg.key.get_pressed()

		if keys[pg.K_d]:
			self.acc.x = PLAYER_ACC
		if keys[pg.K_a]:
			self.acc.x = -PLAYER_ACC

		self.acc.x += self.vel.x * PLAYER_FRICTION
		self.vel += self.acc
		self.pos += self.vel + 0.5 * self.acc

		if self.pos.x < 0:
			self.pos.x = 0

		if self.pos.x > WIDTH:
			self.pos.x = WIDTH

		self.rect.midbottom = self.pos

class Platform(pg.sprite.Sprite):

	def __init__(self, x, y, w, h):
		pg.sprite.Sprite.__init__(self)
		self.image = pg.Surface((w, h))
		self.image.fill(BLACK)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

class Square(pg.sprite.Sprite):

	def __init__(self, game, w, h):
		pg.sprite.Sprite.__init__(self)
		self.game = game
		self.image = pg.Surface((w, h))
		self.image.fill(RED)
		self.rect = self.image.get_rect()
		self.rect.center = (0, HEIGHT -40)
		self.pos = vec(0, (HEIGHT -40))
		self.vel = vec(SQUARE_SPEED, 0)

	def update(self):

		if self.pos.x < 0:
			self.game.score += 1
			self.vel.x = -self.vel.x + 0.1
			print(self.vel.x)

		if self.pos.x > WIDTH:
			self.game.score += 1
			self.vel.x = -self.vel.x - 0.1
			print(self.vel.x)

		self.pos.x += self.vel.x

		self.rect.midbottom = self.pos