import sys,argparse,pyperclip
import db

def printUsage():
	print '''
Usage:	setpw -d domain [-n name]-p password
set the password of the name in the domain.
	'''

def main():
	parser = argparse.ArgumentParser(
	description = 'the argparse'
	)

	parser.add_argument('-d', action='store', dest='domain')
	parser.add_argument('-p', action='store', dest='password')
	parser.add_argument('-n', action='store', dest='name')
	args = parser.parse_args()

	if args.domain == None or args.password == None:
		printUsage()
		return
	
	db.getDB()
	if db.isExist(args.domain, args.name):
		db.setpw(args.domain, args.name, args.password)
		print "Success! you can check it by running getpw."
	else:
		if args.name==None:
			print "the domain " + args.domain + " is not exist, please try createpw."
		else:
			print "the domain " + args.domain + " and the name " + args.name + " is not exist, please try createpw."



if __name__ == '__main__':
	main()
