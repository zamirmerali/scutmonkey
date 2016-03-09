#module for database abstracting
#import section
import sqlite3

#class to create a database
class CreateDatabase:
	db = sqlite3.connect('memory')
	cursor = db.cursor()
	cursor.execute('''
		CREATE TABLE consult(id INTEGER PRIMARY KEY, mrn INTEGER, firstname TEXT, lastname TEXT, story TEXT, exam TEXT, labs TEXT, imaging TEXT, plan TEXT)
		''')
	db.commit()

#class to write to the database
class WriteDatabase:
	cursor = db.cursor()

#function taking consult info as paramaters and writing to the database
	def writedata(mrn,firstname,lastname,story,exam,labs,imaging):
		cursor.execute('''INSERT INTO consult(mrn, firstname, lastname, story, exam, labs, imaging) VALUES(?,?,?,?,?,?,?)''', (mrn,firstname,lastname,story,exam,labs,imaging))
		db.commit()
		
