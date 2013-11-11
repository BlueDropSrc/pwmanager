import sys,argparse,pyperclip,sqlite3
import db

DOMAIN = 0
NAME = 1
PASSWORD = 2

def printUsage():
	print '''
Usage:	getpw -d domain [-n name]
	getpw -a
Get the password.

-a		print all password.
-d domain 	print the password in the domain.
-n name 	print the password of the name.
	'''


def main():
	parser = argparse.ArgumentParser(
	description = 'the argparse'
	)

	parser.add_argument('-a', action='store_true', default=False, dest='get_all')
	parser.add_argument('-d', action='store', dest='domain')
	parser.add_argument('-n', action='store', dest='name')

	args = parser.parse_args()

	db.getDB()
	if args.get_all:
		pw_table = db.getpw()
		if pw_table == None:
			print "The database is empty."
			return
		for pw in pw_table:
			if pw[NAME] == None:
				print pw[DOMAIN] + " :  " + pw[PASSWORD]
			else:
				print pw[DOMAIN] + "|" + pw[NAME] + " :  " + pw[PASSWORD]
	elif args.name !=None and args.domain!= None:
		pw = db.getpw(args.domain, args.name)
		if pw == None:
			print "Not Found!Please try getpw -a"
			return
		pyperclip.setcb(pw[PASSWORD])
		print pw[DOMAIN] + "|" + pw[NAME] + " :  " + pw[PASSWORD]
	elif args.domain != None:
		pw_table = db.getpw(args.domain)
		if pw_table == []:
			print "Not Found!Please try getpw -a"
			return
		for pw in pw_table:
			if pw[NAME] == None:
				print pw[DOMAIN] + " :  " + pw[PASSWORD]
			else:
				print pw[DOMAIN] + "|" + pw[NAME] + " :  " + pw[PASSWORD]
			pyperclip.setcb(pw[PASSWORD])
	else: printUsage()

	
if __name__ == '__main__':
	main()
