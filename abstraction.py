#module for database abstracting
#import section
import sqlite3
import os

#create a database abstraction class. This handles all database interaction
class Database(object):
	column_labels=['mrn','name','hpi','gcs','cn','motor','sensory','coags','labs','cthead','mribrain','plan','todo']

	#create the database, main function
	def __init__(self, db_file="data/data.db"):
		database_already_exists = os.path.exists(db_file)
		self.db = sqlite3.connect(db_file)
		if not database_already_exists:
			self.setuptable()

	def labels(self,column_lables):
		for i in column_labels:
			print i

	#execute any SQL statement
	def executescript(self,sql):
		print sql
		cursor = self.db.cursor()
		cursor.executescript(sql)
		self.db.commit()
		cursor.close()

	#find the total number of databse rows
	def totalrows(self):
		cursor = self.db.cursor()
		cursor.execute("SELECT * FROM Consults")
		numberofrows = len(cursor.fetchall())
		return numberofrows


	#create the database table
	def setuptable(self):
		sql = """
		CREATE TABLE Consults 
		(
			id INTEGER PRIMARY KEY AUTOINCREMENT,
			mrn TEXT,
			name TEXT,
			story TEXT,
			exam TEXT,
			labs TEXT,
			imaging TEXT,
			plan TEXT
		) ;

		INSERT INTO Consults (mrn, name, story, exam, labs, imaging, plan) 
		VALUES (011231, 'Merali', 'healthy', 'normal', 'normal', 'nil acute', 'normal') ;

		INSERT INTO Consults (mrn, name, story, exam, labs, imaging, plan) 
		VALUES (049202, 'Zamir', 'dead', 'normal', 'hello', 'smelly', 'discuss') ;
		"""
		self.executescript(sql)

	#execute a command
	def execute(self,sql):
		print sql
		cursor = self.db.cursor()
		cursor.execute(sql)
		self.db.commit()
		cursor.close()


	#generate a patient summary
	def summary(self,user_id):
		self.user_id = user_id 
		user_id = user_id+1
		sql = "SELECT id, mrn, name, story, exam, labs, imaging, plan FROM Consults WHERE id = %s" % user_id 
		#sql = "SELECT id, mrn, name, story, exam, labs, imaging, plan FROM Consults WHERE id = 3"
		print sql
		cursor = self.db.cursor()
		cursor.execute(sql)
		records = cursor.fetchone()
		cursor.close()
		mrn = records[1]
		name = records[2]
		story = records[3]
		exam = records[4]
		labs = records[5]
		imaging = records[6]
		plan = records[7]

		#format the record into a patient summary. 
		patientsummary = "MRN: " + mrn + "  Name: " + name + "\nID:" + story + "\nExam:" + exam + " Imaging: " + imaging + "\nPlan: " + plan
		return patientsummary

	#generate a consult overview
	def consultoverview(self,user_id):
		self.user_id = user_id
		user_id = user_id+1
		sql = "SELECT id, mrn, name, story, exam, labs, imaging, plan FROM Consults WHERE id = %s" % user_id 
		print sql
		cursor = self.db.cursor()
		cursor.execute(sql)
		records = cursor.fetchone()
		cursor.close()

		return records

if __name__ == '__main__':
	db = Database()
	newID = db.totalrows()
	print newID
	
	#assign each value to a new variable
	

	

	



	




