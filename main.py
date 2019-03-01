#: -*- coding = utf-8 -*-

__autor__ = "Patrick Soares"

#import libs
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.config import Config
from kivy.clock import Clock
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout


import random

Config.read('config.ini')

class ScreenGame(Widget):

# Classe pricipal do jogo abordando todos os Widgets dentro de si

	Bird=ObjectProperty(None)
	Barrel=ObjectProperty(None)
	Barrel2=ObjectProperty(None)
	Barrel3=ObjectProperty(None)
	
	start=None
	
	def __init__(self,**kwargs):
		super(ScreenGame,self).__init__(**kwargs)
		self.Barrel=self.ids.barrel
		self.Barrel2= self.ids.barrel_2
		self.Barrel3 = self.ids.barrel_3
		self.Bird=self.ids.bird
		self.start=True
	
	def update(self,bt):
		if self.start:
			self.condition()
		self.collides()
		self.ids.bg.update()
		self.ids.bg2.update()
		self.ids.bg3.update()
		
	def condition(self):
		self.Barrel.update()
		self.Bird.move()
		self.Barrel2.update()
		self.Barrel3.update()
	
		
	def collides(self):
		
		bSup = self.Barrel.ids.bar_sup.collide_bird(self.Bird)
		bInf = self.Barrel.ids.bar_inf.collide_bird(self.Bird)
		
		b2Sup=self.Barrel2.ids.bar_sup.collide_bird(self.Bird)
		b2Inf=self.Barrel2.ids.bar_inf.collide_bird(self.Bird)
		
		b3Sup=self.Barrel3.ids.bar_sup.collide_bird(self.Bird)
		b3Inf=self.Barrel3.ids.bar_inf.collide_bird(self.Bird)
		
		if bSup == 'stop' or b2Sup=='stop' or b3Sup == 'stop':
			self.start=False
		
		if bInf == 'stop' or b2Inf=='stop' or b3Inf == 'stop':
			self.start=False
			
class Bird(Widget):
	
	move_y= -11
	up=4
	count_up=0
	
	def move(self):
		self.y += self.move_y
		if self.move_y > 0:
			self.count_up += self.move_y
		if self.count_up >= 140:
			self.move_y = -11
			self.count_up =0
			self.up-=1
	def bird_up(self):
		if self.up <= 4:
			self.count_up=0
			self.move_y =11
			
	


class Barrel(Widget):
	pos_bar=0.0
	pos_sup_y=0.0
	height_bar=0.0
	height_sup=0.0
	pos_mid_y=0.0
	height_mid=0.0
	pos_inf_y=0.0
	height_inf=0.0
	
	def __init__(self,**kwargs):
		super(Barrel,self).__init__(**kwargs)
		self.pos_bar=random.randint(5,8)/10.0
		self.height_bar = 1.0 - self.pos_bar
		

	def update(self):
		self.x-=8
		self.random_pos_height()
		self.show_random_pos()
		
	def random_pos_height(self):
		self.pos_bar = random.randint(5,8)/10.0
		self.pos_sup_y = self.parent.height * self.pos_bar
		self.height_bar = 1.0 - self.pos_bar
		self.height_sup = self.parent.height * self.height_bar 
		
		self.pos_mid_y = self.pos_sup_y -.45
		self.height_mid = self.parent.height * .45
		
		self.pos_inf_y = self.parent.y
		self.height_inf = self.parent.height * (self.pos_bar - .45)
	
	def show_random_pos(self):
		
		if self.x + self.width < self.parent.x:
	
			self.x = self.parent.x+self.parent.width
			self.random_bars()
	
	def random_bars(self):
		#pos e altura aleatoria do cano superior
		self.ids.bar_sup.y = self.pos_sup_y
		self.ids.bar_sup.height = self.height_sup
		
	#pos e altura aleatoria do cano do meio
		self.ids.bar_mid.y = self.pos_mid_y 
		self.ids.bar_mid.height = self.height_mid
	
	#pos e altura aleatoria do cano inferior
		self.ids.bar_inf.y = self.pos_inf_y
		self.ids.bar_inf.height = self.height_inf			


class Barrel_Sup(Widget):
	
	def collide_bird(self,bird):
		if self.collide_widget(bird):
			return 'stop'


class Barrel_Mid(Widget):
	
	def collide_bird(self,bird):
		if self.collide_widget(bird):
			return 'collide'


class Barrel_Inf(Widget):
	
	def collide_bird(self,bird):
		if self.collide_widget(bird):
			return 'stop'

class BackGround(BoxLayout):
	
	def update(self):
		self.x-=1
		
		if self.x + self.width < self.parent.x:
			self.x = self.parent.center_x +(self.parent.center_x )+(self.parent.center_x * .9)


class GameApp(App):
	
	def build(self):
		game=ScreenGame()
		Clock.schedule_interval(game.update,.03)
		return game


if __name__ == '__main__':
	GameApp().run()
