#Import section

from kivy.app import App 
from kivy.uix.widget import Widget 
from kivy.uix.label import Label 
from kivy.uix.floatlayout import FloatLayout 
from kivy.uix.anchorlayout import AnchorLayout 
from kivy.uix.textinput import TextInput 
from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.button import Button 


#Define Consult Summary Widget
class ConsultWidget(Widget):
	consultpage = BoxLayout(orientation='vertical')
	top_bar = BoxLayout(orientation='horizontal')
	go_shift_summary = Button(text='Back to shift summary')
	story = Label(text="story goes here", font_size=18)
	exam = Label(text="exam goes here", font_size=18)
	labs = Label(text="labs go here", font_size=18)
	imaging = Label(text="imaging goes here", font_size=18)
	plan = Label(text="plan goes here", font_size=18)
	consultpage.add_widget(top_bar)
	top_bar.add_widget(go_shift_summary)
	consultpage.add_widget(story)
	consultpage.add_widget(exam)
	consultpage.add_widget(labs)
	consultpage.add_widget(imaging)
	consultpage.add_widget(plan)

#Define Shift Summary Widget

#define main app
class ScutApp(App):
	def build(self):
		return ConsultWidget.consultpage

if __name__ == '__main__':
	ScutApp().run()