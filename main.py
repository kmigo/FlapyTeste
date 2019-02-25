# -*- coding: utf-8 -*-

__author__ = 'Patrick Soares'

#imports libs
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.config import Config
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import NumericProperty,ObjectProperty
from kivymd.toast import toast
from kivymd.label import MDLabel
import random


class ScreenGame(FloatLayout):
	birdObj=ObjectProperty(None)
	condition=True
	#score=ObjectProperty(None)
	def __init__(self,**kwargs):
		super(ScreenGame,self).__init__(**kwargs)
		self.height=1200
		self.width=800
		self.move_barrel=15
		self.Score=''
		self.bird_decay=12
		self.cont=0
		self.cd= True
		
		Clock.schedule_interval(self.condition_update,.05)
	
	def condition_update(self,*args):
		if self.cd:
			self.update()
		else:
			pass
			
		if self.barrel_inf == 'stop':
			self.condition=False
			toast('colidiu')
		
		condition_sup=self.ids.barrel.ids.bar_sup.bounce_bird(
		self.birdObj)
		
		condition_inf=self.ids.barrel.ids.bar_inf.bounce_bird(
		self.birdObj)
		
		if condition_sup == 'stop':
			self.condition = False
		
		if condition_inf == 'stop':
			self.condition = False
			
	def update(self):
		if self.condition:
			self.ids.texto.text = str(self.ids.barrel.ids.bar_med.get_score())
			self.ids.barrel.x-=self.move_barrel
			self.ids.bird.y-=self.bird_decay
			self.ids.barrel.ids.bar_med.bounce_bird(self.birdObj)
			self.cont -=14
			if self.cont <= -100 and self.ids.bird.up > 0 or self.bird_decay >= 13.5 and self.cont <= -90 and self.ids.bird.up > 0: 
				self.cont=0
				self.ids.bird.up-=1
			
			if self.bird_decay >= 13.5:
				self.bird_decay = 13.5
	
	
	def bird_up(self):
		if self.ids.bird.up <= 4 and self.condition:
			self.ids.bird.y+=100
			self.ids.bird.up += 1
			self.move_barrel+=.1
			self.bird_decay += .1
			
 	def barrel_inf(self):
 		condition=self.ids.barrel.ids.bar_inf.bounce_bird(
 		self.birdObj)
 		return condition
 	
 	def barrel_sup(self):
 		condition=self.ids.barrel.ids.bar_sup.bounce_bird(
 		self.birdObj)
 		return condition
 		
	
			
		

class Barrel(BoxLayout):
	birdObj=ObjectProperty(None)
	def __init__(self,**kwargs):
		super(Barrel,self).__init__(**kwargs)
		self.pos=(1150,0)
	#	self.birdObj.y=1100	
		self.movimento=10
		self.limite=None
		Clock.schedule_interval(self.barrel_l,.05)
	
	def barrel_l(self,dt):
		valor_sup=random.randint(1,7) / 10.0
		valor_med=random.randint(300,420)
		valor_inf=random.randint(1,7) / 10.0
		if self.x+self.width < self.parent.x:
			self.x = 1150
			self.ids.bar_sup.size_hint_y=valor_sup 
			#self.ids.bar_med.height=valor_med
			self.ids.bar_inf.size_hint_y=valor_inf
		



class BarrelSup(Widget):
	def __init__(self,**kwargs):
		super(BarrelSup,self).__init__(**kwargs)
		
	def bounce_bird(self,bird):
		if self.collide_widget(bird):
			
			return 'stop'

class BarrelMed(Widget):
	bird=ObjectProperty(None)
	def __init__(self,**kwargs):
		super(BarrelMed,self).__init__(**kwargs)
		self.score=0
		self.passando=None
		
		#self.bounce_bird(self.bird)
	def bounce_bird(self,bird):
		teste=0
		if self.collide_widget(bird):
			
			teste+=1
			self.passando=True
			
		
		if self.passando == True and not self.collide_widget(
		bird):
			
			self.score+=1
			self.passando = False
			
			
	
	def get_score(self):
		res = self.score
		return res
	
class BarrelInf(Widget):
	
	def bounce_bird(self,bird):
		if self.collide_widget(bird):
			return 'stop'
	

class Bird(Widget):
	
	def __init__(self,**kwargs):
		super(Bird,self).__init__(**kwargs)
		self.up=0
		self.decay=10
		
	
	def ap(self):
		self.y=400


		
class GameApp(App):
	pass
	
	def build(self):
		game=ScreenGame()
		
		return game

GameApp().run()
