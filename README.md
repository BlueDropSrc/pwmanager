pwmanager
======

Intro
-----

pwmanager - Some script that can help you create and manage your web password.

platform:Unix like system.
Author: BlueDrop
Email: BlueDropSrc@gmail.com
Version: 0.1.0


Install?(1,2,3 is optionnal)
----------------------------
1.Open the file db.py, set the config DBPATH(default:$HOME) and DBNAME(default:.pwmanager.sqlite)<br />
2.Open the file create.py, set the config PWLENGTH(default:12) and PWKEYS(default:abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&;*,.)<br />
3.Open the file install.sh, set the config INSTALL_DIR<br />
4.Run the script install.sh

Usage?
------
There are three commands:createpw, getpw, setpw
1.createpw 
create a password and store it with the domain.
After that, it copy the password created to clipboard.
Usage:	createpw -d domain
2.getpw
Get the password of the domain you gave, or all in the database.
Usage:	getpw [-n] -d domain
	getpw -a

-a		print all password.
-d domain	print the password of domain.
-n		no print.
3.setpw
set the password of the domain you gave.
Usage:	setpw -d domain -p password
