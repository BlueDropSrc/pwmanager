import sys,argparse,pyperclip,random,os
import db

PWLENTH = 12
PWKEYS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*;,.'


def createpw():
	pw = ''
	for item in range(PWLENTH):	
		rn = random.randint(0, 99)
		index = rn % PWKEYS.__len__()
		pw += PWKEYS[index]
	return pw

def printUsage():
	print '''
Usage:	createpw -d domain
create a password and store it with the domain.
	'''

def main():
	parser = argparse.ArgumentParser(
	description = 'the argparse'
	)

	parser.add_argument('-d', action='store', dest='domain')
	args = parser.parse_args()

	domain = args.domain
	if(domain == None):
		printUsage()
		return
	db.getDB()
	if db.isExist(domain):
		print 'The domain '+ domain + ' is exist, please use setpw or getpw.'
		return

	nextpw = True
	while(nextpw):
		pw = createpw()
		print pw
		isOK =raw_input('Is it OK?(yes/no):(yes)')
		if isOK == '' or isOK == 'yes':
			nextpw = False
			db.insertpw(domain, pw)
			print domain + ' : ' + pw + ' is inserted.'
			pyperclip.setcb(pw)
			print 'the password is copyed to clipboard.' 


if __name__ == '__main__':
	main()

