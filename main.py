#Import section

from kivy.app import App 
from kivy.uix.widget import Widget 

#Define Main App Class
class ScutWidget(Widget):
	pass

class ScutApp(App):
	def build(self):
		return ScutWidget()

if __name__ == '__main__':
	ScutApp().run()