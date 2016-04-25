#! /usr/bin/python
from time import sleep	#for waiting times between functions
import json				#for backend

def load_config(__file):		#Loads the data and
    __local_config = False
    try:
        with open(__file) as f:
            __local_config = json.load(f)
    except Exception as e:		#Catches exceptions too!
        print (e)
    return __local_config

def save_config(__obj, __file):		#Writes __obj to __file
    try:
        with open(__file, 'w') as f:
            json.dump(__obj, f, indent=2)
    except Exception as e:			#With more exception handling, just in case
        print (e)
        return False
    return True

def stop():							#The function we (will) call to end the program. This is extremely limited for now, and needs to be rewritten
    global config
    if save_config(config, 'config.json') == False:
        print ("error saving config! any changes will not be saved!")
    quit()

class Library():					#The main class
    def __init__(self):				#The variables get initialised here
        self.libraryname = ''
        self.booknum = 0
        self.books = []
        self.issuers = {}
        self.booksissued = []
        print 'Library initialised...'
        sleep(1)
        print 'Please add required data now...'
        self.readdata()				#Let's add some values to the variables

    def readdata(self):				#As it's name says, reads the data into our variables
        self.libraryname = raw_input("Enter name of the Library...")
        self.booknum = int(raw_input("Enter total number of books associated with the Library..."))
        filename1 = raw_input("Enter filename to load book names from (default := books.json )...")
        if filename1 == '' :
            filename1 = 'books.json'
        self.books = load_config(filename1)
        if self.books == False:
            print "No books present in config! This is an error..."
            sleep(0.5)
            quit()
        filename2 = raw_input("Enter filename for issuers dictionary of format \"name\":[book1,book2,...] default filename is issuers.json...)"
        if filename2 == '' :
            filename2 = 'issuers.json'
        self.issuers = load_config(filename2)
        if self.issuers == False:
            print "No issuers present in config! This is an error..."
            sleep(0.5)
            quit()
        for i in self.issuers.values:
            self.booksissued.append(i)
        print "Issued books list generated successfully..."




e = Library()
