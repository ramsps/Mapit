# Mapit
A python program to launch any location in google maps from Run dialogue box 

Mapit programme (as learnt from automate the boring stuff, Udemy)

>Quick method of searching for any place in google maps from the windows run box

Steps:
1. Copy mapit.py and mapit.bat files to the same location
2. Add the location of the files to path environment variable, which can be done as(in Windows 10) :
	control panel>>System and Security>>System>>Advanced System Settings>>Environment Variables>>Path(under System Variables)>>New    
3. Open run box(Windows key + R key) 
	type and hit enter : mapit <place name> For example: mapit andheri mumbai
				OR
	if you have copid text of any location to clipboard, just type mapit and hit enter

#Internet connection and Google chrome required
#Once the path environment variable is added, as long as the files are not moved from their location, this will work

#This was a rogram to understand requests module. Also utilised pyperclip.
