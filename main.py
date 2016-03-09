#Import section

from kivy.app import App 
from kivy.uix.widget import Widget 
from kivy.uix.label import Label 
from kivy.uix.floatlayout import FloatLayout 
from kivy.uix.anchorlayout import AnchorLayout 
from kivy.uix.textinput import TextInput 
from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.button import Button 
from kivy.uix.dropdown import DropDown 
from kivy.base import runTouchApp
from kivy.uix.textinput import TextInput
import abstraction

#Create the database
CreateDatabase

#Define Consult Summary Widget
class ConsultWidget(Widget):
	#Define the layouts
	consultpage = BoxLayout(orientation='vertical')
	top_bar = BoxLayout(orientation='horizontal')

	#Define the dropdown list
	consult_dropdown = DropDown()
	states = ['Pending','In Progress','Complete']
	def callback(instance):
		x = btn.text
	for state in states:
		btn = Button(text='%r' % state, size_hint_y=None, height=44,)
		btn.bind(on_release=callback)
		consult_dropdown.add_widget(btn)
		mainbutton = Button(text='Consult Status')
		mainbutton.bind(on_release=consult_dropdown.open)
		consult_dropdown.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))

	#Define the buttons
	##Define the back to shift summary button
	go_shift_summary = Button(text='Back to Shift Summary')
	
	#Define the lables
	identification = Label(text="ID")
	story = Label(text="story goes here", font_size=18)
	exam = Label(text="exam goes here", font_size=18)
	labs = Label(text="labs go here", font_size=18)
	imaging = Label(text="imaging goes here", font_size=18)
	plan = Label(text="plan goes here", font_size=18)

	#Define the widget tree for the consult page
	consultpage.add_widget(top_bar)
	top_bar.add_widget(go_shift_summary)
	top_bar.add_widget(mainbutton)

	consultpage.add_widget(identification)
	consultpage.add_widget(story)
	consultpage.add_widget(exam)
	consultpage.add_widget(labs)
	consultpage.add_widget(imaging)
	consultpage.add_widget(plan)

#Define Consult Summary Widget
class ConsultInputWidget(Widget):
	#Define the layouts
	consultpage = BoxLayout(orientation='vertical')
	top_bar = BoxLayout(orientation='horizontal')

	#Define the buttons
	##Define the back to shift summary button
	go_shift_summary = Button(text='Back to Shift Summary')
	##Define the write consult button
	write_consult = Button(text='Start the Consult')

	#Define the Text Inputs
	identification = TextInput(text="ID")
	identification.bind(text=tempfunction)
	story = TextInput(text="story goes here", font_size=18)
	story.bind(text=tempfunction)
	exam = TextInput(text="exam goes here", font_size=18)
	exam.bind(text=tempfunction)
	labs = TextInput(text="labs go here", font_size=18)
	labs.bind(text=tempfunction)
	imaging = TextInput(text="imaging goes here", font_size=18)
	imaging.bind(text=tempfunction)
	plan = TextInput(text="plan goes here", font_size=18)
	plan.bind(text=tempfunction)

	#Define the widget tree for the input page
	consultpage.add_widget(top_bar)
	top_bar.add_widget(go_shift_summary)
	top_bar.add_widget(write_consult)

	consultpage.add_widget(identification)
	consultpage.add_widget(story)
	consultpage.add_widget(exam)
	consultpage.add_widget(labs)
	consultpage.add_widget(imaging)
	consultpage.add_widget(plan)

#define main app class
class ScutApp(App):
	def build(self):
		#show the consult page
		return ConsultInputWidget.consultpage

if __name__ == '__main__':
	ScutApp().run()