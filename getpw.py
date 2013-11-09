import sys,argparse,pyperclip,sqlite3
import db

DOMAIN = 0
PASSWORD = 1

def printUsage():
	print '''
Usage:	getpw [-n] -d domain
	getpw -a
Get the password.

-a		print all password.
-d domain	print the password of domain.
-n		no print.
	'''


def main():
	parser = argparse.ArgumentParser(
	description = 'the argparse'
	)

	parser.add_argument('-a', action='store_true', default=False, dest='get_all')
	parser.add_argument('-d', action='store', dest='domain')
	parser.add_argument('-n', action='store_true', default=False, dest='noprint')

	args = parser.parse_args()

	db.getDB()
	if args.get_all:
		pw_table = db.getpw()
		if pw_table == None:
			print "The database is empty."
			return
		for pw in pw_table:
			print pw[DOMAIN] + " :  " + pw[PASSWORD]
	elif args.domain != None:
		pw = db.getpw(args.domain)
		pyperclip.setcb(pw[PASSWORD])
		if args.noprint == False:
			print pw[DOMAIN] + " :  " + pw[PASSWORD]
	else: printUsage()

	
if __name__ == '__main__':
	main()
