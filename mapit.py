import webbrowser, sys, pyperclip

sys.argv        #stores input arguments as list of strings

if len(sys.argv)>1:
    address =' '.join(sys.argv[1:]) #checking if command line arguments were passed. Also note first element in argv is always file name or location

else:
    address = pyperclip.paste() #applies adrress copied to clipboard


webbrowser.open('https://www.google.co.in/maps/place/' + address) #searches for given address in google maps
