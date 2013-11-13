import sys,argparse,pyperclip,random,os
import db

PWLENTH = 12
PWKEYS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*;,.'


def createpw():
	pw = ''
	for item in range(PWLENTH):	
		rn = random.randint(0, 99)
		index = rn % PWKEYS.__len__()
		pw += PWKEYS[index]
	return pw

def printUsage():
	print '''
Usage:	createpw -d domain [-n name]
create a password and store it with the domain and the name.
	'''

def main():
	parser = argparse.ArgumentParser(
	description = 'the argparse'
	)

	parser.add_argument('-d', action='store', dest='domain')
	parser.add_argument('-n', action='store', dest='name')
	args = parser.parse_args()

	domain = args.domain
	name = args.name
	if(domain == None):
		printUsage()
		return
	db.getDB()
	if db.isExist(domain, name):
		print 'The domain '+ domain + ' is exist, please use setpw or getpw.'
		return

	nextpw = True
	while(nextpw):
		pw = createpw()
		print pw
		isOK =raw_input('Is it OK?(yes/no):(yes)')
		if isOK == '' or isOK == 'yes':
			nextpw = False
			db.insertpw(domain, name, pw)
			if name==None:
				print domain + ' : ' + pw + ' is inserted.'
			else:
				print domain + "|" + name + ' : ' + pw + " is inseted."
			pyperclip.setcb(pw)
			print 'the password is copyed to clipboard.' 


if __name__ == '__main__':
	main()

