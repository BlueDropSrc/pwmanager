import sys,argparse,pyperclip
import db

def printUsage():
	print '''
Usage:	setpw -d domain -p password
set the password of the domain.
	'''

def main():
	parser = argparse.ArgumentParser(
	description = 'the argparse'
	)

	parser.add_argument('-d', action='store', dest='domain')
	parser.add_argument('-p', action='store', dest='password')
	args = parser.parse_args()

	if args.domain == None or args.password == None:
		printUsage()
		return
	
	db.getDB()
	if db.isExist(args.domain):
		db.setpw(args.domain, args.password)
		print "Success! you can check it by running getpw."
	else:
		print "the domain " + domain + " is not exist, please try createpw."



if __name__ == '__main__':
	main()
