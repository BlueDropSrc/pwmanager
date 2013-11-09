import sqlite3,os

global DB,CU
DBPATH = os.getenv('HOME')
DBNAME = '.pwmanager.sqlite'

def getDB():
	global DB,CU
	DB = sqlite3.connect(DBPATH + '/' +  DBNAME)
	CU = DB.cursor()
	try:
		CU.execute('create table account(id integer primary key,domain varchar(20) UNIQUE,password varchar(20))')
	except: 1 == 1

def isExist(domain):
	CU.execute("select * from account where domain=?", (domain,))
	return CU.fetchone() != None

def insertpw(domain, pw):
	CU.execute("insert into account (domain, password) values(?,?)", (domain, pw))
	DB.commit()

def getpw(domain = None):
	if domain == None :
		CU.execute("select domain, password from account")
		pw = CU.fetchall()
	else:
		CU.execute("select domain, password from account where domain=?", (domain,))
		pw = CU.fetchone()
	return pw

def setpw(domain,password):
	CU.execute("update account set password=? where domain=?", (password, domain))
	DB.commit()
