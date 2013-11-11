import sqlite3,os

global DB,CU
DBPATH = os.getenv('HOME') + '/Dropbox'
DBNAME = '.pwmanager.sqlite'

def getDB():
	global DB,CU
	DB = sqlite3.connect(DBPATH + '/' +  DBNAME)
	CU = DB.cursor()
	try:
		CU.execute('create table account(id integer primary key,domain varchar(20) UNIQUE,name varchar(20), password varchar(20))')
	except: 1 == 1

def isExist(domain, name):
	if name==None:
		CU.execute("select * from account where domain=?", (domain,))
	else:
		CU.execute("select * from account where domain=? and name=?", (domain, name))
	return CU.fetchone() != None

def insertpw(domain, name, pw):
	if name==None:
		CU.execute("insert into account (domain, password) values(?,?)", (domain, pw))
	else:
		CU.execute("insert into account (domain, name, password) values(?,?,?)", (domain, name, pw))

	DB.commit()

def getpw(domain = None, name=None):
	if domain == None :
		CU.execute("select domain, name, password from account")
		pw = CU.fetchall()
	elif name == None:
		CU.execute("select domain, name, password from account where domain=?", (domain,))
		pw = CU.fetchall()
	else:
		CU.execute("select domain, name, password from account where domain=? and name=?", (domain,name))
		pw = CU.fetchone()
	return pw

def setpw(domain, name, password):
	if name==None:
		CU.execute("update account set password=? where domain=?", (password, domain))
	else:
		CU.execute("update account set password=? and name=? where domain=?", (password, name, domain))
		
	DB.commit()
