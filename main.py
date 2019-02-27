#: -*- coding = utf-8 -*-

__autor__ = "Patrick Soares"

#import libs
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.config import Config
from kivy.clock import Clock


Config.read('config.ini')

class ScreenGame(Widget):
	def __init__(self,**kwargs):
		super(ScreenGame,self).__init__(**kwargs)
		
		Clock.schedule_interval(self.update,.1)
	
	def update(self,bt):
		self.ids.barrel.x-=5


class Bird(Widget):
	pass


class Barrel(Widget):
	pass


class Barrel_Sup(Widget):
	pass


class Barrel_Mid(Widget):
	pass


class Barrel_Inf(Widget):
	pass


class GameApp(App):
	
	def build(self):
		game=ScreenGame()
		return game


if __name__ == '__main__':
	GameApp().run()