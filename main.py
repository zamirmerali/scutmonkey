#Import section
import kivy
kivy.require('1.8.0')

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
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen, ScreenManager 


#Define Consult View
class ConsultView(Screen):
	consultpage = BoxLayout(orientation='vertical')
	top_bar = BoxLayout(orientation='horizontal',size_hint_y=None, height=80)
	consult_body = BoxLayout(orientation='vertical')
	go_shift_summary = Button(text='Back to Shift Summary', font_size=14, size_hint_y=None, height=80)
	delete_consult = Button(text='Delete Consult', font_size=14,size_hint_y=None, height=80)

	def __init__ (self,**kwargs):
		super (ConsultView, self).__init__(**kwargs)

		#call the class instances of the widgets
		consultpage = ConsultView.consultpage
		top_bar = ConsultView.top_bar
		consult_body = ConsultView.consult_body
		go_shift_summary = ConsultView.go_shift_summary
		delete_consult = ConsultView.delete_consult

		#create instance of generate consult function
		generateconsult = GenerateConsult()
		generateconsult.fullconsult(1)

		#bind method to the top bar buttons
		go_shift_summary.bind(on_release = self.changersummary)
		#delete_consult.bind(on_release = deleteconsult)

		#define widget tree for everything except the 13
		consultpage.add_widget(top_bar)
		consultpage.add_widget(consult_body)
		top_bar.add_widget(go_shift_summary)
		top_bar.add_widget(delete_consult)

		self.add_widget(consultpage)
	
	#function for the consult summary button
	def changersummary(self,*args):
		self.manager.current = 'shiftsummary'

#Generate Full Consult
class GenerateConsult(Widget):
	#function for generating the full consult
	def fullconsult(self,user_id,*args):
		print user_id

		#call the class instances of the widgets
		consultpage = ConsultView.consultpage
		top_bar = ConsultView.top_bar
		consult_body = ConsultView.consult_body
		go_shift_summary = ConsultView.go_shift_summary
		delete_consult = ConsultView.delete_consult

		#clear existing widget tree if it exists
		if consult_body.children>0:
			consult_body.clear_widgets()
			print 'tree cleared'

		#access the consult for the given user_id
		db = abstraction.Database()
		consultoverview = db.consultoverview(user_id)
		print consultoverview[1]

		#Define the lables and set text to correct value
		mrn = Label(text=consultoverview[1],font_size=14,halign='left',text_size=(775,40))
		name = Label(text=consultoverview[2],font_size=14,halign='left',text_size=(775,40))
		story = Label(text=consultoverview[3], font_size=14,halign='left',text_size=(775,40))
		gcs = Label(text=consultoverview[4],font_size=14,halign='left',text_size=(775,40))
		cranialnerves = Label(text='',font_size=14,halign='left',text_size=(775,40))
		motorexam = Label(text='', font_size=14,halign='left',text_size=(775,40))
		sensoryexam = Label(text='', font_size = 14,halign='left',text_size=(775,40))
		coags = Label(text=consultoverview[5], font_size=14,halign='left',text_size=(775,40))
		labs = Label(text='', font_size=14,halign='left',text_size=(775,40))
		cthead = Label(text=consultoverview[6], font_size=14,halign='left',text_size=(775,40))
		mribrain = Label(text='', font_size=14,halign='left',text_size=(775,40))
		plan = Label(text=consultoverview[7], font_size=14,halign='left',text_size=(775,40))
		todo = Label(text='', font_size=14,halign='left',text_size=(775,40))

		#Add the 13 to the consult body widget
		consult_body.add_widget(mrn)
		consult_body.add_widget(name)
		consult_body.add_widget(story)
		consult_body.add_widget(gcs)
		consult_body.add_widget(cranialnerves)
		consult_body.add_widget(motorexam)
		consult_body.add_widget(sensoryexam)
		consult_body.add_widget(coags)
		consult_body.add_widget(labs)
		consult_body.add_widget(cthead)
		consult_body.add_widget(mribrain)
		consult_body.add_widget(plan)
		consult_body.add_widget(todo)

#Define Consult Input Screen 
class ConsultInput(Screen):

	def __init__(self,**kwargs):
		super (ConsultInput,self).__init__(**kwargs)

		#Define the layouts
		consultpage = BoxLayout(orientation='vertical')
		top_bar = BoxLayout(orientation='horizontal')
		id_bar = BoxLayout(orientation='horizontal')

		#Define the Text Inputs
		mrn = TextInput(text="Mrn", font_size=12)
		name = TextInput(text="name", font_size=12)
		story = TextInput(text="story goes here", font_size=12)
		exam = TextInput(text="exam goes here", font_size=12)
		labs = TextInput(text="labs go here", font_size=12)
		imaging = TextInput(text="imaging goes here", font_size=12)
		plan = TextInput(text="plan goes here", font_size=12)


		#Define the widget tree for the input page
		#Create the top bar
		go_shift_summary = Button(text='Back to Shift Summary')
		start_consult = Button(text='Start the Consult')
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
		self.add_widget(consultpage)

		#Define the buttons
		##Bind Function to the back to shift summary button
		#generatesummary = GenerateSummary()
		go_shift_summary.bind(on_release = self.changer)

		##Bind function to the write consult button
		start_consult.bind(on_release=partial(self.callback,mrn,name,story,exam,labs,imaging,plan))
		

	#set the action of the start consult button
	def callback(self,mrn,name,story,exam,labs,imaging,plan,*args):

		db = abstraction.Database()
		sql = """
		INSERT INTO Consults (mrn, name, story, exam, labs, imaging, plan) VALUES ('%s','%s','%s','%s','%s','%s','%s') ;
		""" % (
			mrn.text,
			name.text,
			story.text,
			exam.text,
			labs.text,
			imaging.text,
			plan.text)

		print "Something happened"
		#print mrn.text
		db.executescript(sql)

	def changer(self,*args):
		self.manager.current = 'shiftsummary'

		generatesummary = GenerateSummary()
		generatesummary.generatelist()

#Generate a Summary Consult
class GenerateSummary(Widget):
	#function for generating the summary list
	def generatelist(self):

		encounter = ShiftSummary.encounter
		new_consult = ShiftSummary.new_consult

		if encounter.children>0:
			encounter.clear_widgets()

		db = abstraction.Database()
		numberofrows = db.totalrows()

		encounter.add_widget(new_consult)
		for i in range(numberofrows):
			patientsummary = db.summary(i)
			btn = Button(text=str(patientsummary), text_size = (775,90), halign='left', valign ='top', size_hint_y=None, height=100, background_color=(1,1,1,1))
			encounter.add_widget(btn)
			btn.bind(on_release=partial(self.buttonid,i))

	def buttonid(self,user_id,*args):
		generateconsult = GenerateConsult()
		generateconsult.fullconsult(user_id)
		App.get_running_app().root.current = 'consultview'

#Define the Shift Summary Screen
class ShiftSummary(Screen):

	encounter = GridLayout(cols=1, spacing=5, size_hint_y=None)
	root = ScrollView(size_hint=(None, None), size=(800, 600))
	new_consult = Button(text='New Consult', size_hint_y=None, height=80, background_color=(1,0,0,1))

	def __init__(self,**kwargs):
		super (ShiftSummary,self).__init__(**kwargs)

		encounter = ShiftSummary.encounter
		new_consult = ShiftSummary.new_consult
		root = ShiftSummary.root

		generatesummary = GenerateSummary()
		generatesummary.generatelist()
		encounter.bind(minimum_height=encounter.setter('height'))
		new_consult.bind(on_release=self.changerinput)
		
		#Define the widget tree for the Shift Summary Page
		root.add_widget(encounter)
		self.add_widget(root)


	#function for the new consult button
	def changerinput(self,*args):
		self.manager.current = 'consultinput'

	def changerview(self,*args):
		self.manager.current = 'consultview'

#define main app class
class ScutApp(App):
	def build(self):
		my_screenmanager = ScreenManager()
		shiftsummary = ShiftSummary(name='shiftsummary')
		consultinput = ConsultInput(name='consultinput')
		consultview = ConsultView(name='consultview')
		my_screenmanager.add_widget(shiftsummary)
		my_screenmanager.add_widget(consultinput)
		my_screenmanager.add_widget(consultview)
		
		
		
		return my_screenmanager

		#show the consult page
		#return ConsultInputWidget.consultpage
		#show the consult summary page
		#return ConsultWidget.consultpage
		#show the shift summary page
		#return ShiftSummaryWidget.root 

if __name__ == '__main__':
	ScutApp().run()