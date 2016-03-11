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
import sqlite3
import abstraction

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

#Define Consult Input Widget
class ConsultInputWidget(Widget):
	#Define the layouts
	consultpage = BoxLayout(orientation='vertical')
	top_bar = BoxLayout(orientation='horizontal')
	id_bar = BoxLayout(orientation='horizontal')

	#Define the buttons
	##Define the back to shift summary button
	go_shift_summary = Button(text='Back to Shift Summary')
	##Define the write consult button
	start_consult = Button(text='Start the Consult')

	#Define the Text Inputs
	mrn = TextInput(text="MRN")
	name = TextInput(text="name")
	story = TextInput(text="story goes here", font_size=18)
	exam = TextInput(text="exam goes here", font_size=18)
	labs = TextInput(text="labs go here", font_size=18)
	imaging = TextInput(text="imaging goes here", font_size=18)
	plan = TextInput(text="plan goes here", font_size=18)

	#Define the widget tree for the input page
	#Create the top bar
	consultpage.add_widget(top_bar)
	top_bar.add_widget(go_shift_summary)
	top_bar.add_widget(start_consult)
	#Create the ID bar
	consultpage.add_widget(id_bar)
	id_bar.add_widget(mrn)
	id_bar.add_widget(name)
	#Create the consult information
	consultpage.add_widget(story)
	consultpage.add_widget(exam)
	consultpage.add_widget(labs)
	consultpage.add_widget(imaging)
	consultpage.add_widget(plan)

	#set the action of the start consult button
	db = abstraction.Database()
	sq1 = "INSERT INTO Consults (mrn, name, story, exam, labs, imaging, plan) VALUES (?,?,?,?,?,?,?)", (mrn, name,story, exam, labs, imaging, plan)
	print sq1
	start_consult.bind(on_press=db.executescript(sq1))

#define main app class
class ScutApp(App):
	def build(self):
		#show the consult page
		return ConsultInputWidget.consultpage

if __name__ == '__main__':
	ScutApp().run()