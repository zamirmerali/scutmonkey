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
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
import sqlite3
import abstraction
from functools import partial

#Define Full Consult Widget
class ConsultWidget(Widget):
	#Define the layouts
	consultpage = BoxLayout(orientation='vertical')
	top_bar = BoxLayout(orientation='horizontal')

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
	mrn = TextInput(text="MRN", font_size=12)
	name = TextInput(text="name", font_size=12)
	story = TextInput(text="story goes here", font_size=12)
	exam = TextInput(text="exam goes here", font_size=12)
	labs = TextInput(text="labs go here", font_size=12)
	imaging = TextInput(text="imaging goes here", font_size=12)
	plan = TextInput(text="plan goes here", font_size=12)

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
	def callback(*args):
		db = abstraction.Database()
		sql = """
		INSERT INTO Consults (mrn, name, story, exam, labs, imaging, plan) VALUES ('%s','%s','%s','%s','%s','%s','%s') ;
		""" % (
			ConsultInputWidget.mrn.text,
			ConsultInputWidget.name.text,
			ConsultInputWidget.story.text,
			ConsultInputWidget.exam.text,
			ConsultInputWidget.labs.text,
			ConsultInputWidget.imaging.text,
			ConsultInputWidget.plan.text)

		print "Something happened"
		db.executescript(sql)

	start_consult.bind(on_release = callback)

#Define the Shift Summary Widget
class ShiftSummaryWidget(Widget):
	#define the layouts
	encounter = GridLayout(cols=1, spacing=5, size_hint_y=None)
	root = ScrollView(size_hint=(None, None), size=(800, 600))
	#Define the buttons
	#figure out how many rows there are
	db = abstraction.Database()
	numberofrows = db.totalrows()

	#Define the summary buttons
	encounter.bind(minimum_height=encounter.setter('height'))
	for i in range(numberofrows):
		db = abstraction.Database()
		patientsummary = db.summary(i)
		btn = Button(text=str(patientsummary), size_hint_y=None, height=100)
		encounter.add_widget(btn)
	
	
	#Define the labels

	#Define the widget tree for the Shift Summary Page
	root.add_widget(encounter)

	

#define main app class
class ScutApp(App):
	def build(self):
		#show the consult page
		#return ConsultInputWidget.consultpage

		#show the consult summary page
		#return ConsultWidget.consultpage

		#show the shift summary page
		return ShiftSummaryWidget.root

if __name__ == '__main__':
	ScutApp().run()