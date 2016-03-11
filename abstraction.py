#module for database abstracting
#import section
import sqlite3
import os

#create a database abstraction class. This handles all database interaction
class Database(object):
	#create the database, main function
	def __init__(self, db_file="data/data.db"):
		database_already_exists = os.path.exists(db_file)
		self.db = sqlite3.connect(db_file)
		if not database_already_exists:
			self.setuptable()

	#execute any SQL statement
	def executescript(self,sql):
		print sql
		cursor = self.db.cursor()
		cursor.executescript(sql)
		self.db.commit()
		cursor.close()

	#create the database table
	def setuptable(self):
		sql = """
		CREATE TABLE Consults 
		(
			id INTEGER PRIMARY KEY AUTOINCREMENT,
			mrn INTEGER,
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

	#execute any sql statement, used for inserting records
	def insert(self,sql):
		print sql
		newID = 0
		cursor = self.db.cursor()
		cursor.execute(sql)
		newID = cursor.lastrowid
		self.db.commit()
		cursor.close()
		return newID

	#select a record from the table
	def select(self,sql):
		cursor = self.db.cursor()
		cursor.execute(sql)
		records = cursor.fetchall()
		cursor.close()

#if __name__ == '__main__':
#	db = Database()
#	sql = 'SELECT * FROM Consults WHERE mrn="011231"'
#	records = db.select(sql)
#	print('1):', records)
	




