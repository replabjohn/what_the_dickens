#!/usr/local/bin/python
# -*- coding: UTF-8 -*-

import string, io, StringIO
import glob, os, random
import time, re
import sys, subprocess
import pycorpora

from types import *

import names, places
import change_colours, make_covers
import source.index, blurbwriter
import markovify_local as markovify
import bibliography
from cleanup import cleanup as cleanup
from use_nltk import modify_text

try:
	import reportlab
except ImportError:
	print "This project requires the reportlab toolkit to produce PDF output." 
	print "Download it from https://www.reportlab.com/opensource/"
	sys.exit(-1)

try:
	import PIL
except ImportError:
	print "This project requires PIL - the Python Image Library." 
	print "Download it from https://pypi.org/project/Pillow/"
	sys.exit(-1)


#do we need all these...?
import PIL.Image as Image

from reportlab.lib.colors import black, white, red, lightgrey, darkgrey
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.utils import ImageReader
from reportlab.graphics import renderPDF
from reportlab.graphics.shapes import Group, Drawing
from reportlab.pdfgen import canvas
from reportlab.pdfbase.pdfmetrics import registerFont, stringWidth
from reportlab.pdfbase.ttfonts import TTFont

__VERSION__ = "0.2.3b"

#VERBOSE = 1
VERBOSE = 0

poss_intro_titles = ["PREFACE", "AUTHOR'S PREFACE", "INTRODUCTION",
					 "AUTHOR'S INTRODUCTION",
					 "AUTHOR'S NOTE"]
poss_titles = list(poss_intro_titles)
for t in poss_titles:
	poss_intro_titles.append(source.index.prettify(t))


def registerFonts(VERBOSE=0, SILENT=0):
	#VERBOSE = 1
	VERBOSE = 0

	if SILENT == 1:
		VERBOSE = 0

	if VERBOSE ==1 :
		if SILENT != 1:
			print "registering Fonts..."

	KNOWN_FONT_PAIRS = [
		#Gentium Basic
		["Gentium Basic",                      "GenBasR.ttf"],
		["Gentium Basic Bold",                 "GenBasB.ttf"],
		["Gentium Basic Bold Italic",          "GenBasBI.ttf"],
		["Gentium Basic Italic",               "GenBasI.ttf"],
		#Gill Sans Nova
		["Gill Sans Nova Bold",                "GillSansBoNova.ttf"],
		["Gill Sans Nova Cond Ultra Bold",     "GillSansCondUltraBoNova.ttf"],
		["Gill Sans Nova Ultra Bold",          "GillSansUltraBoNova.ttf"],
		]
		#most stuff is done using Gentium Basic

	startdir = os.getcwd()

	FONTDIR = "."

	if os.path.isdir(os.path.join(os.getcwd(), "fonts")):
		FONTDIR = os.path.join(os.getcwd(), "fonts")
		if VERBOSE > 0:
			print "Found fontdir: '%s'" % FONTDIR
	os.chdir(FONTDIR)

	for f in KNOWN_FONT_PAIRS:
		fontname, ttffile = f
		if os.path.isfile(ttffile):
			if VERBOSE > 0:
				printstring = " found '%s' ... " % fontname
				print printstring
			try:
				registerFont(TTFont(fontname, ttffile))
				if VERBOSE > 1:
				   print "Registered OK."
				elif VERBOSE > 0:
				   print ".",
				else:
				   pass
			except reportlab.pdfbase.ttfonts.TTFError:
				print "ERROR REGISTERING FONT!"
	if VERBOSE > 0:
		if SILENT != 1:
			print "OK\n"
	os.chdir(startdir)


class DataHolder:
	"""a class just for holding titles etc"""

	def __init__(self):
		self.Document_Title = "A Guide"
		self.title_long = self.Document_Title
		self.title_split = self.Document_Title
		self.Version = __VERSION__
		self.author     = None
		self.edition    = None
		self.publisher  = None
		self.first_publication_year = None
		self.publication_year       = None
		self.characters		= None
		self.main_character	= None
		self.dickens_book	= None
		self.dickens_filename = None
		self.chapter_dividers = None
		self.chapter_names = None
		self.chapter_heads_to_check = []

		self.text = None

		self.topmargin = 100 #px
		self.leftmargin = 75 #px
		self.rightmargin = self.leftmargin
		self.bottommargin = self.topmargin

		self.pagenum = 1 # used for numbering pages

		self.linktexts = [[]] # have an empty string per series

		self.generationtime = time.strftime("%a %d %b %Y, %H:%M:%S")


def check_for_files(VERBOSE=0):

	#DEBUG = 1
	DEBUG = 0

	if VERBOSE > 0:
		print "Checking for modified texts of source files..."

	thisdir = os.getcwd()
	modified_files = glob.glob(os.path.join(thisdir, "source", "modified", "*.txt"))
	if DEBUG == 1:
		print "modified_files path: '%s'" % (os.path.join(thisdir, "source", "modified", "*.txt"))
		print "len(modified_files): %s" % len(modified_files)
	if len(modified_files) == 0:
		if VERBOSE > 0:
			print "\tNONE FOUND.\n\tREGENERATING...\n\n"
		os.chdir(os.path.join(thisdir, "source"))
		source.index.modify_files(VERBOSE=VERBOSE)
		os.chdir(thisdir)
		if VERBOSE > 0:
			print "\tDONE.\n\n"
	else:
		if VERBOSE > 0:
			print "\tModified source files found OK.\n\n"
		else:
			pass

def make_intro(d, author=None, dickens_book=None, year=None):

	if author == None:
		author = names.getName()
	if dickens_book == None:
		if d.dickens_book != None:
			dickens_book = d.dickens_book
		else:
			dickens_book = "a book by Charles Dickens"
	if year == None:
		year = "%s" % (int(time.strftime("%Y")) - 1) #last year
	month = random.choice(("January", "February", "March", "April", "May", "June", "July",
						   "August", "September", "October", "November", "December"))

	place = places.get_random_place()

	heading = random.choice(("PREFACE",
							 "AUTHOR'S PREFACE",
							 "INTRODUCTION",
							 "AUTHOR'S INTRODUCTION",
							 "AUTHOR'S NOTE"))

	bit1 = random.choice(("This",
						  "This book",
						  "The book you are holding",
						  "The book you are holding in your hands"))

	bit2 = random.choice(("my version of",
						  "my retelling of",
						  "my attempt to retell",
						  "my feeble attempt to retell",
						  "my homage to")) 

	bit3 = random.choice(("you like it",
						  "you enjoy it",
						  "you like it",
						  "you enjoy it",
						  "the attempt was worth it",
						  "the experiment was successful",
						  "you think %sthe attempt was worth it" % random.choice(("","", "that ")),
						  "you think %sthe experiment was successful." % random.choice(("","", "that ")),
						  "I do it justice",
						  "I did it justice"))

	# It's the story of.... never mind.
	randnum = random.choice((0,1))
	if randnum == 1:
		if d.main_character != None:
			thisname = random.choice((d.main_character, string.split(d.main_character, " ")[0]))
			
			bit4 = "It's the %s of %s%s... %s you'll find out soon enough." % (random.choice(("tale", "story")),
																		random.choice(("a man", "a person",
																					   "a man called %s" % thisname, "a person called %s" % thisname,
																					   "a man named %s" % thisname, "a person named %s" % thisname,
																					   thisname, thisname
																					   )),
																		random.choice((" who ", "")),
																		random.choice(("but never mind", "never mind"))
																		)
		else:
			bit4 = "It's the %s of %s%s... %s you'll find out soon enough." % (random.choice(("tale", "story")),
																		random.choice(("a man", "a person")),
																		random.choice((" who ", "")),
																		random.choice(("but never mind", "never mind"))
																		)
	else:
		bit4 = ""
									  

	randnum2 = random.choice((0,1))
	if randnum2 == 1:
		bit5 = "I %s to write %s %s because %s is %s%s I %s that there was %s for %s." % (random.choice(("wanted", "decided", "had")),
									 random.choice(("this", "my")),
									 random.choice(("book", "novel", "tale", "story")),
									 random.choice(("the original",
													"Dickens' orginal",
													"the original story",
													"Dickens' orginal story")),
									 random.choice(("so %s" % random.choice(("impressive",
																			 "masterful",
																			 "magnificent",
																			 "brilliant",
																			 "good")),
													"such a %s" % random.choice(("tour de force", "masterpiece",
																				 "masterwork", "delight",
																				 "classic", "treasure",
																				 "magnum opus", "masterwork",
																				 "tour de force"))
													)),
									 random.choice((" and", " but", ", and", ", but")),
									 random.choice(("felt", "thought")),
									 random.choice(("room",
													"still room",
													"space",
													"enough room",
													"enough space",
													"plenty of room",
													"plenty of space")),
									 random.choice(("me to put my own spin on it",
													"me to tweak it to make it my own",
													"me to retell it my own way"))
																						  )
	else:
		bit5 = ""

	if bit5 != "":									  
		randnum3 = random.choice((0,1))
		if randnum3 == 1:
			if bit4 != "":
				#swap bit4 and bit5
				tx = bit4
				bit4 = bit5
				bit5 = tx
				bit5 = "\n%s" % (bit5)
		else:
			if bit4 != "":
				bit5 = "\n%s" % (bit5)

	text = """%s




%s is %s %s.

I hope %s.

%s
%s



%s
%s
%s %s

[INTRO#END]
""" % (heading, bit1, bit2, dickens_book, bit3, bit4, bit5, author, place, month, year)
	return text


def get_gendered_name(name):
	"returns a single firstname of the same gender when given a name."

	allnames = names.male_firstnames+names.female_firstnames
	allnames = list(allnames) + source.index.DICKENS_FEMALE_NAMES + source.index.DICKENS_MALE_NAMES

	#figure out what's actually the name in a multi-word string..
	name = string.capwords(name)
	if len(string.split(name, " ")) == 1:
		firstname = name
	elif len(string.split(name, " ")) == 2:
		pt1, pt2 = string.split(name, " ")
		if string.capwords(pt1) in allnames:
			firstname = pt1
		elif string.capwords(pt2) in allnames:
			firstname = pt2
	else:
		pt1, pt2, pt3 = string.split(name, " ", maxsplit=2)
		if pt1 in allnames:
			firstname = pt1
		elif pt2 in allnames:
			firstname = pt2
		elif pt3 in allnames:
			firstname = pt3

	#check for the gender...
	gender = source.index.check_gender(firstname)

	if gender == "female":
		newname = names.getFemaleFirstName()
	elif gender == "male":
		newname = names.getMaleFirstName()
	else:
		newname = random.choice(names.male_firstnames + names.female_firstnames)
	return newname

def make_a_small_person(name):
	""""makes a replacement for 'Little Emily' or 'Tiny Tim'"

Checks 'name' to get its gender, then makes up an appropriate replacement.

Returns the name as a string.

eg

>>> main.make_a_small_person("tiny tim")
'Minuscule Michael'
>>> main.make_a_small_person("little emily")
'Tiny Therese'

"""

	#improve to make allitertive output optional?

	allnames = names.male_firstnames+names.female_firstnames
	allnames = list(allnames) + source.index.DICKENS_FEMALE_NAMES + source.index.DICKENS_MALE_NAMES

	#figure out what's actually the name in a multi-word string..
	name = string.capwords(name)
	if len(string.split(name, " ")) == 1:
		firstname = name
	elif len(string.split(name, " ")) == 2:
		pt1, pt2 = string.split(name, " ")
		if string.capwords(pt1) in allnames:
			firstname = pt1
		elif string.capwords(pt2) in allnames:
			firstname = pt2
	else:
		pt1, pt2, pt3 = string.split(name, " ", maxsplit=2)
		if pt1 in allnames:
			firstname = pt1
		elif pt2 in allnames:
			firstname = pt2
		elif pt3 in allnames:
			firstname = pt3

	#check for the gender...
	#gender = source.index.check_gender(firstname)

	smallwords = ["Tiny", "Small", "Little", "Diminutive",	#make these more common
				  "Tiny", "Small", "Little", "Diminutive",
				  "Tiny", "Small", "Little", "Diminutive",
				  "Minute", "Mini", "Baby", "Petite",
				  "Minute", "Mini", "Baby", "Petite",
				  "Miniature", "Minuscule", "Microscopic", "Infinitesimal",
				  "Micro", "Diminutive", "Pocket-sized",
				  "Lilliputian", "Minor", "Minimal", "inappreciable",
				  "Token", "Nominal", "Paltry", "Meagre", "Wee",
				  "Teeny", "Teeny-Weeny", "Teensy", "Teensy-weensy", "Weeny",
				  "Itsy-Bitsy", "Itty-Bitty", "Tiddly", "Pint-Sized", "Bite-Sized",
				  "Titchy", "Iittle-bitty"
				  ]

	mysmallword = random.choice(smallwords)

	newname = get_gendered_name(firstname)
	loopcount = 0
	while newname[0] != mysmallword[0]:
		loopcount = loopcount + 1
		if loopcount > 200:
			break # no point being a bloody fool about it
		else:
			newname = get_gendered_name(firstname)

	return "%s %s" % (mysmallword, newname) 	


def getlogo(animal):
	"""Picks an image file to use when given an animal name."""

	animals_dict =  {
		  "antelope"    :   ["B393.png",
							 "B393.png"],
		  "bat"     :       ["BatVolant.png"],
		  "bear"    :       ["B346.png",
							 "B350.png",
							 "bear_couped_2.png",
							 "bear_head_couped.png",
							 "bear_head_erased.png",
							 "bear_rampant.png",
							 "DemiBearRampant.png"],
		  "bull"    :       ["B377.png",
							 "bulls_head_erased.png"],
		  "cat"     :       ["CatPassantGaudant.png",
							 "CatSejantGaurdant.png",
							 "CatSejantGaurdantErect.png"],
		  "crow"    :       ["E473.png",     #(actually a raven, but close enough)
							 "raven.png"],
		  "deer"    :       ["HindHeadCouped.png",
							 "HindHeadErased.png",
							 "HindStatant.png",
							 "HindTrippant.png",
							 "B380.png",
							 "B382.png",
							 "B383.png",
							 "B387.png",
							 "bucks_head_erased.png"],
		  "dog" :                   ["dog-head-2.png",
									 "dog-head.png",
									 "dog-passant-1.png",
									 "dog-passant-2.png",
									 "dog-rampant-2.png",
									 "dog-rampant-3.png",
									 "dog-rampant.png",
									 "dog-sejant-2.png",
									 "dog-sejant-with-ball.png",
									 "dog-sejant.png",
									 "GreyhoundCourant.png",
									 "GreyhoundHeaddErased.png",
									 "greyhound_passant.png",
									 "talbot_head_erased.png"],
		  "ewe"     :           ["Sheep.png",
								 "SheepPassant.png"],
		  "fish"    :           ["X481.png",
								 "X482.png",
								 "SalmonNaiantProper.png"],
		  "fox"     :           ["FoxHeadCouped.png",
									 "FoxHeadCouped2.png",
									 "FoxPassant.png",
									 "FoxRampant.png",
									 "FoxSejant.png",
									 "FoxsFace.png",
									 "FoxsHeadErased.png"],
		  "grizzly bear"    :       ["B346.png",
									 "B350.png",
									 "bear_couped_2.png",
									 "bear_head_couped.png",
									 "bear_head_erased.png",
									 "bear_rampant.png",
									 "DemiBearRampant.png"],
		  "hedgehog"    :       ["hedgehog.png",
								 "hedgehog.png"],
		  "horse"       :       ["B360.png",
								 "horse_head_erased.png"
								 ],
		  "ibex"        :   ["Ibex.png",
							 "Ibex.png"],
		  "lamb"        :   ["Sheep.png",
							"SheepPassant.png"],
		  "leopard"     :   ["leopards_head_erased_and_affronte.png",
							 "leopards_head_erased_and_affronte.png"],
		  "lion"        :   ["L282.png",
							 "L283.png",
							 "L286.png",
							 "L287.png",
							 "L289.png",
							 "L292.png",
							 "L295.png",
							 "L296.png",
							 "L300.png",
							 "L303.png",
							 "L304.png",
							 "L306.png",
							 "L307.png",
							 "L309.png",
							 "L311.png",
							 "L312.png",
							 "L319.png",
							 "L320.png",
							 "lion-couchant-crowned.png",
							 "Lion_couchant.png",
							 "Lion_Passant2.png",
							 "Lion_rampant_2.png",
							 "Lion_rampant_double_queued.png",
							 "Lion_rampant_queue_nowed.png",
							 "Lion_rampant_regardant.png",
							 "Lion_rampant_regardant_queue_nowed.png",
							 "Lion_sejant_erect.png",
							 "Lion_sejant_regardant_erect.png",
							 "Lion_statant.png",
							 "Lion_Statant_Holding_Out_The_Forepaw.png"
							 ],
		  "otter"       :       ["OtterStatant.png",
								 "OtterStatant.png",
								 ],
		  "panther"     :       ["Panther2.png",
								 "panther_rampant.png"
								 ],
		  "polar bear"    :       ["B346.png",
									 "B350.png",
									 "bear_couped_2.png",
									 "bear_head_couped.png",
									 "bear_head_erased.png",
									 "bear_rampant.png",
									 "DemiBearRampant.png"],
		  "porcupine"   :            ["hedgehog.png",
									 "hedgehog.png"],
		  "porpoise"    :   ["X479.png",
							 "X480.png"],
		  "rabbit"      :   ["ConeyRampant.png",
							 "ConeyRampant2.png"],
		  "ram"         :   ["B400.png",
							 "rams_head_cabossed.png",
							 "ram_passant.png",
							 "ram_rampant.png",
							 "ram_statant.png"],
		  "reindeer"    :   ["reindeer_head_erased.png",
							 "reindeer_statant.png"],
		  "sheep"       :   ["Sheep.png",
							 "SheepPassant.png"],
		  "silver fox"  :   ["FoxHeadCouped.png",
							 "FoxHeadCouped2.png",
							 "FoxPassant.png",
							 "FoxRampant.png",
							 "FoxSejant.png",
							 "FoxsFace.png",
							 "FoxsHeadErased.png"],
		  "snake"   :   ["X483.png",
						 "serpent_erect.png",
						 "Serpent_involved.png",
						 "Serpent_Nowed.png",
						 "Serpent_Nowed2.png"],
		  "tiger"   :   ["btiger.png",
						 "btiger2.png",
						 "tiger.png",
						 "tiger_head_erased.png"],
		  "wildcat" :    ["CatPassantGaudant.png",
						  "CatSejantGaurdant.png",
						  "CatSejantGaurdantErect.png"],
		  "wolf"    :   ["wolf-passant-ululant.png",
						 "wolf-salient.png",
						 "WolfPassant.png",
						 "WolfRampant.png",
						 "WolfSaliant.png",
						 "wolfs_head_erased.png",
						 "wolf_courant.png",
						 "wolf_salient.png",
						 "wolf_sejant_head_erect.png",
						 "B337.png",
						 "B339.png",
						 "B340.png"]
		  }
	animal = string.lower(string.strip(animal))
	if animals_dict.has_key(animal):
		return random.choice(animals_dict[animal])
	else:
		return None


def doTitles(c,d, VERBOSE=0, SILENT=0):
	"""Do title page"""

	colour = random.choice(("Red", "Green", "Blue", "Violet", "White", "Black", "Orange", "Yellow"))
	animal = string.capwords(random.choice(pycorpora.animals.common["animals"]))
	if len(string.split(animal)) > 1:
		animal = string.split(animal)[-1]

	pressname = random.choice(("Books", "Press", "Books", "Press", "Productions", "Design", "Designs"))
	company_name = "%s %s %s" % (colour, animal, pressname)

	if VERBOSE > 0:
		if SILENT != 1:
			print "\n\t\tGenerating Title Pages"
	DocTitle = d.Document_Title

	c.setAuthor(d.author)
	c.setTitle(DocTitle)

	#need a named bookmark for Outlines to work...
	c.bookmarkPage("TitlePage", fit="Fit")
	c.addOutlineEntry(key="TitlePage", level=1, title="Title page", closed=1)

	c.showOutline()

	c.setFont("Gentium Basic", 14)

	#c.getPageNumber()

	c.setFont("Gentium Basic Bold", 60)

	ypos = A4[1] - 250 

	TitleFontSize = 60

	#check to make sure the first line isn't too long to fit
	for thisline in d.title_split.split("\n"):
		if stringWidth(thisline, "Gentium Basic Bold", 60, 'latin-1') > (A4[0]-d.leftmargin-d.rightmargin):
			TitleFontSize = 42

	for thisline in d.title_split.split("\n"):
		thisline = source.index.prettify(string.strip(thisline))
		c.setFont("Gentium Basic Bold", TitleFontSize)
		textWidth = stringWidth(thisline, "Gentium Basic Bold", TitleFontSize, 'latin-1')

		xpos = d.leftmargin

		if textWidth < (A4[0] - d.leftmargin - d.rightmargin):
			newline = ""
			ypos = ypos - 80

			xpos = (A4[0]/2.0) - (textWidth/2.0) 

			#shadow
			c.setFillColor(darkgrey)
			c.drawString(xpos-3,ypos-3,string.strip(thisline))

			#main name
			c.setFillColor(black)
			c.setStrokeColor(black)
			c.drawString(xpos,ypos,(thisline))
			ypos = ypos - TitleFontSize

		else:
			newline = ""
			#for word in line.split():
			for word in thisline.split(" "):
				newline2 = "%s %s" % (newline, word)
				newline2width = stringWidth(string.strip(newline2), "Gentium Basic Bold", TitleFontSize, "latin-1")
				if newline2width > (A4[0] - d.leftmargin - d.rightmargin):

					newlinewidth = stringWidth(string.strip(newline), "Gentium Basic Bold", TitleFontSize, "latin-1")
					xpos = (A4[0]/2.0) - (newlinewidth/2.0) 

					#shadow
					c.setFillColor(darkgrey)
					c.drawString(xpos-3,ypos-3,string.strip(newline))

					#main name
					c.setFillColor(black)
					c.setStrokeColor(black)
					c.drawString(xpos,ypos,(string.strip(newline)))

					if TitleFontSize == 60:
						ypos = ypos-80
					else:
						ypos = ypos-60

					newline = word

				else:
					newline= newline2

		#xpos = (A4[0]/2.0) - (textWidth/2.0) 
		newlinewidth = stringWidth(string.strip(newline), "Gentium Basic Bold", TitleFontSize, "latin-1")
		xpos = (A4[0]/2.0) - (newlinewidth/2.0) 

		#shadow
		c.setFillColor(darkgrey)
		c.drawString(xpos-3,ypos-3,string.strip(newline))

		#main name
		c.setFillColor(black)
		c.setStrokeColor(black)
		c.drawString(xpos,ypos,string.strip(newline))
		ypos = ypos - TitleFontSize

	ypos = ypos - 60

	#Add author's name 
	c.setFont("Gentium Basic Bold", 42)
	thisline = string.strip(d.author)
	textWidth = stringWidth(thisline, "Gentium Basic Bold", 42, 'latin-1')
	x = (A4[0]/2.0) - (textWidth/2.0) 
	c.setFillColor(darkgrey)
	c.drawString(x-3,ypos-3,thisline)

	c.setFillColor(black)
	c.setStrokeColor(black)
	c.drawString(x,ypos,thisline)

	#reset colours etc
	c.setFillColor(black)
	c.setStrokeColor(black)
	c.setFont("Gentium Basic", 14)

	mydrawing = Drawing(150, 200)
	lx = A4[0]/2.0      #Logo X
	#lx = lx - 150/2.0

	lx = lx - 250/2.0

	lx = lx + 10        # fiddle
	ly = A4[1]/2.0      #Logo Y

	ly = ly - 250/2.0

	logofile = getlogo(animal)

	if VERBOSE > 0:
		print "\t\t\tFOUND LOGO : ", logofile
	if logofile != None:
		this_dir= os.getcwd()
		mylogo = os.path.join("images", "animals", logofile)

		img = Image.open(mylogo)

		newcolour = None
		if colour == "Red":
			newcolor = (238, 0, 0)
		elif colour == "Green":
			newcolor = (0, 128, 0)
		elif colour == "Blue":
			newcolor = (0, 0, 204)
		elif colour == "Violet":
			newcolor = (139, 0, 75)
		elif colour == "White":
			newcolor = (253, 253, 253)
		elif colour == "Black":
			newcolor = (17, 17, 17)
		elif colour == "Orange":
			newcolor = (198, 112, 0)
		elif colour == "Yellow":
			newcolor = (254, 254, 0)

		if newcolor != None:
			img = change_colours.change_Main_Color(img, newcolor)
			img = change_colours.change_Other_Color(img, (255,255,255))

		mysize = 50
		iw, ih = img.size

		if iw > ih:
			wpercent = (mysize/float(iw))
			hsize = int((float(ih)*float(wpercent)))
			img = img.resize((mysize,hsize), Image.ANTIALIAS)
		else:
			wpercent = (mysize/float(ih))
			hsize = int((float(iw)*float(wpercent)))
			img = img.resize((hsize, mysize), Image.ANTIALIAS)

		lx = A4[0]/2.0       #Logo X
		lx = lx - 25
		ly = 67

		#fiddle to sort out problems with PNG transparency issues
		img_data = StringIO.StringIO()
		img.save(img_data, format='png')
		img_data.seek(0)
		img_out = ImageReader(img_data)

		c.drawImage(img_out, lx, ly, width=img.size[0], height=img.size[1], mask='auto')

	printString = company_name
	capit = random.choice((1,0))
	if capit == 1:
		printString = string.upper(printString)

	pressfont = random.choice(("Gentium Basic Bold",
							   "Gentium Basic Bold Italic",
							   "Gentium Basic Italic"))

	c.setFont(pressfont, 14)

	textWidth = stringWidth(printString, "Gentium Basic", 14, 'latin-1')

	x = (A4[0]/2.0) - (textWidth/2.0) 
	y = 50 
	c.drawString(x,y,printString)

	if VERBOSE > 0:
		if SILENT != 1:
			print "OK\n"

	c.showPage()
	return company_name


def make_front_matter(publisher, ISBN=None, publication_year=None, first_publication_year=None, d=None):
	"""makes up the page with the lagal blurb, ISBN, publishing info etc"""

	#do ISBN etc
	if ISBN== None:
		ISBN = make_covers.make_ISBN(spacer="-")
	if d != None:
		d.ISBN = ISBN

	upper_publisher = string.upper(publisher)
	publisher = string.capwords(publisher)
	d.publisher = publisher

	if publication_year == None:
		publication_year = time.strftime("%Y") #this year
		d.publication_year == publication_year

	if first_publication_year == None:
		first_publication_year = random.choice((publication_year,
												publication_year,
												"%s" % (int(publication_year) - 1),
												"%s" % (int(publication_year) - 2),
												"%s" % (int(publication_year) - 3),
												"%s" % (int(publication_year) - 4),
												"%s" % (int(publication_year) - 5)
												))
		d.first_publication_year = first_publication_year

	#d.first_publication_year = first_publication_year
	if d != None:
		d.first_publication_year = first_publication_year


	legal_blurb = random.choice(("""
Apart from any use permitted under UK copyright law,
this publication may only be reproduced, stored or transmitted,
in any form, or by any means, with prior permission in writing
of the publishers or, in tne case of reprographic production,
in accordance with the terms of licences issued
by the Copyright Licensing Agency.
""",
#Above taken from 'The Casebook of Sherlock Holmes' by Sir Authur COnan Doyle
#(Headline publishing group, ISBN 978 0755 334377)

								 """
This book is copyright under the Berne Convention. All rights
reserved. No part of this publication may be reproduced, stored in
a retrieval system, or transmitted in any form or by any means,
electronic, electrical, chemical, mechanical, optical,
photocopying, recording, or otherwise, without prior permission
in writing of the publisher.
""",
#Above taken from 'Ghost Stations III' by Bruce Barrymore Halfpenny
#(Casdec Ltd, ISBN 0 90759557 X)

								 """
This book is distributed under a Creative Commons Attribution- 
NonCommercial- Share Alike 3.0 license. That means: 

You are free: 
* to Share - to copy, distribute and transmit the work 
* to Remix - to adapt the work 

Under the following conditions: 
* Attribution. You must attribute the work in the manner 
specified by the author or licensor (but not in any way that 
suggests that they endorse you or your use of the work). 
* Noncommercial. You may not use this work for commercial 
purposes. 
* Share Alike. If you alter, transform, or build upon this work, 
you may distribute the resulting work only under the same 
or similar license to this one. 
* For any reuse or distribution, you must make clear to others 
the license terms of this work. 
* Any of the above conditions can be waived if you get my 
permission 

More info here: http://creativecommons.Org/licenses/by-nc-sa/3.0/ 

"""
#Above taken from 'Little Brother' (by Cory Doctorow)
#https://archive.org/stream/ost-english-cory_doctorow_-_little_brother/Cory_Doctorow_-_Little_Brother_djvu.txt

))

	#Original sample text:
##    """First published in Great Britain in XXXX
##
##This paperback edition published
##by XXXX in XXXX
##
##Apart from any use permitted under UK copyright law,
##this publication may only be reproduced, stored or transmitted,
##in any form,or by any means, with prior permission in writing
##of the publishers or, in tne case of reprographic production,
##in accordance with the terms of licences issued
##by the Copyright Licensing Agency.
##
##All characters in this publication are fictitious and any resemblances
##to real persons, living or dead, is purely coincidental.
##
##0 979 07553 3448 4 (ISBN-13)
##
##Typeset in FONT by XXXX
##
##HEADLINE PUBLISHING GROUP
##A division of blahblahblah
##
##URL HERE
##    
##"""

	font = "Gentium"    # may need to change if we decide to change the font we use (or use a randomly selected one)

	animal = string.capwords(random.choice(pycorpora.animals.common["animals"]))
	if len(string.split(animal)) > 1:
		animal = string.split(animal)[-1]

	edition = random.choice(("paperback", "hardback", "electronic", "electronic"))
	d.edition = edition

	big_publishing_company = random.choice(("MegaDodo Publications",
											"%s%s Publications" % (random.choice(("Mega", "Ultra",
																				  "Mega", "Ultra",
																				  "Urban ")),
																   animal)))

	website_URL = "" # may change this in future. Use the github page?

	front_matter = """First published in Great Britain in %s

This %s edition published
by %s in %s



%s



All characters in this publication are fictitious and any resemblances
to real persons, living or dead, is purely coincidental.



%s (ISBN-13)

Typeset in %s by %s

%s
A division of %s

%s
	
""" % (first_publication_year, edition, publisher, publication_year, legal_blurb,
	   ISBN, font, publisher, upper_publisher, big_publishing_company, website_URL)

	return d, front_matter


def make_title(title=None, VERBOSE=0):

	if title != None:
		if string.find(title, " by Charles Dickens") > -1:
			title = string.replace(title, " by Charles Dickens", "")

	new_title = "TITLE"
	is_eponymous = 0
	old_eponymous_character = None
	new_eponymous_character = None

	# eponymous books
	eponymous_books = ["Oliver Twist",
					   "David Copperfield",
					   "Nicholas Nickleby",
					   #    ["821-0.txt",   "Dombey and Son",???
					   "Oliver Twist; or, The Parish Boy's Progress",
					   "The Mystery of Edwin Drood",#???
					   "Martin Chuzzlewit",
					   "Barnaby Rudge: A Tale of the Riots of 'Eighty",
					   "Oliver Twist, Vol. 1 (of 3)",
					   "The Personal History of David Copperfield",
					   "Doctor Marigold",   #???
					   "George Silverman's Explanation",    #???
					   "Oliver Twist, Vol. 2 (of 3)",
					   "Oliver Twist, Vol. 3 (of 3)",
					   "Captain Boldheart & the Latin-Grammar Master",#???
					   "The Trial of William Tinkling",
					   "Tom Tiddler's Ground",
					   ]

	eponymous_books_and_characters = [
		["Oliver Twist",                                    "Oliver Twist"],
		["David Copperfield",                               "David Copperfield"],
		["Nicholas Nickleby",                               "Nicholas Nickleby"],
		#"Dombey and Son",???
		["Oliver Twist; or, The Parish Boy's Progress",     "Oliver Twist"],
		["The Mystery of Edwin Drood",                      "Edwin Drood"],
		["Martin Chuzzlewit",                               "Martin Chuzzlewit"],
		["Barnaby Rudge: A Tale of the Riots of 'Eighty",   "Barnaby Rudge"],
		["Oliver Twist, Vol. 1 (of 3)",                     "Oliver Twist"],
		["The Personal History of David Copperfield",       "David Copperfield"],
		["Doctor Marigold",                                 "Doctor Marigold"],
		["George Silverman's Explanation",                  "George Silverman"],
		["Oliver Twist, Vol. 2 (of 3)",                     "Oliver Twist"],
		["Oliver Twist, Vol. 3 (of 3)",                     "Oliver Twist"],
		["Captain Boldheart & the Latin-Grammar Master",    "Captain Boldheart"],
		["The Trial of William Tinkling",                   "William Tinkling"],
		["Tom Tiddler's Ground",                            "Tom Tiddler"],
		]


	all_books = [
					   "A Tale of Two Cities",
					   "A Christmas Carol in Prose; Being a Ghost Story of Christmas",
					   "Great Expectations",
					   "Oliver Twist",
					   "Hard Times",
					   "David Copperfield",
					   "Bleak House",
					   "A Christmas Carol",
					   "Three Ghost Stories",
					   "The Pickwick Papers",
					   "The Old Curiosity Shop",
					   "Our Mutual Friend",
					   "Little Dorrit",
					   "Nicholas Nickleby",
					   "Dombey and Son",
					   "Oliver Twist; or, The Parish Boy's Progress. Illustrated",
					   "Oliver Twist; or, The Parish Boy's Progress",
					   "American Notes",
					   "The Mystery of Edwin Drood",
					   "Sketches by Boz, Illustrative of Every-Day Life and Every-Day People",
					   "Martin Chuzzlewit",
					   "A Christmas Carol",
					   "A Child's History of England",
					   "Barnaby Rudge: A Tale of the Riots of 'Eighty",
					   "Hunted Down: The Detective Stories of Charles Dickens",
					   "Speeches: Literary and Social",
					   "The Uncommercial Traveller",
					   "The Haunted Man and the Ghost's Bargain",
					   "Oliver Twist, Vol. 1 (of 3)",
					   "The Chimes",
					   "The Cricket on the Hearth: A Fairy Tale of Home",
					   "Mugby Junction",
					   "The Magic Fishbone",
					   "Pictures from Italy",
					   "Reprinted Pieces",
					   "The Personal History of David Copperfield",
					   "Some Christmas Stories",
					   "The Battle of Life",
					   "Doctor Marigold",
					   "George Silverman's Explanation",
					   "A Message from the Sea",
					   "The Posthumous Papers of the Pickwick Club",
					   "Holiday Romance",
					   "The Wreck of the Golden Mary",
					   "Mudfog and Other Sketches",
					   "Oliver Twist, Vol. 2 (of 3)",
					   "Oliver Twist, Vol. 3 (of 3)",
					   "Sunday Under Three Heads",
					   "The Seven Poor Travellers",
					   "Somebody's Luggage",
					   "The Posthumous Papers of the Pickwick Club",
					   "Sketches of Young Couples",
					   "The Lamplighter",
					   "Captain Boldheart & the Latin-Grammar Master",
					   "The Cricket on the Hearth: A Fairy Tale of Home",
					   "Children Stories",
					   "The Holly-Tree",
					   "A Child's Dream of a Star",
					   "The Trial of William Tinkling",
					   "Tom Tiddler's Ground",
					   "Tales from Dickens"
					   ]

	if title in eponymous_books:
		is_eponymous = 1
		for book_list in eponymous_books_and_characters:
			if book_list[0] == title:
				old_eponymous_character = book_list[1]
		#would do something to check for females here, but Dickens never wrote any books
		#titled after females. What a sexist.       
		new_eponymous_character = names.getMaleName()
		if old_eponymous_character != None:
			#make single word styles more popular
			new_title_style = random.choice(("Type 1", "Type 2", "Type 3", "Type 4", "Type 3", "Type 4", "Type 3", "Type 4"))
			if VERBOSE > 0:
				print "\tnew_title_style:", new_title_style
			if new_title_style == "Type 1":
				#keep the original style
				new_title = title.replace(old_eponymous_character, new_eponymous_character)
			elif new_title_style == "Type 2":
				#Full name
				new_title = new_eponymous_character
			elif new_title_style == "Type 3":
				#First name
				new_title = string.split(new_eponymous_character, " ")[0]
			elif new_title_style == "Type 4":
				#Surname 
				new_title = string.split(new_eponymous_character, " ")[1]
	else:
		#not named after the main character...
		#do a Markov based book title...

		book_title_text = ""

		for t in all_books:
			if t == all_books[0]:
				book_title_text = t
			else:
				book_title_text = "%s\n%s" % (book_title_text, t)

		#now add in all the books in our bibliography...
		bibliobooks = bibliography.publications
		for bk in bibliobooks:
				book_title_text = "%s\n%s" % (book_title_text, bk)

		text_model = markovify.NewlineText(book_title_text, state_size = 1)
		#text_model = markovify.NewlineText(book_title_text, state_size = 2)

		#new_title = text_model.make_sentence(max_chars=70,
		new_title = text_model.make_sentence(max_chars=40,
											 min_chars=10,
											 test_output=True,
											 tries=9999,
											 max_overlap_ratio=0.5,
											 max_overlap_total=5)

		if string.find(new_title, "by Charles Dickens") > -1:
			new_title = new_title.replace("by Charles Dickens", "")
		if string.find(new_title, "of Charles Dickens") > -1:
			new_title = new_title.replace("of Charles Dickens", "")

		while new_title in all_books:
			#new_title = text_model.make_sentence(max_chars=180,
			new_title = text_model.make_sentence(max_chars=40,
											 min_chars=10,
											 test_output=True,
											 tries=9999,
											 max_overlap_ratio=0.5,
											 max_overlap_total=5)
			if string.find(new_title, "by Charles Dickens") > -1:
				new_title = new_title.replace("by Charles Dickens", "")
			if string.find(new_title, "of Charles Dickens") > -1:
				new_title = new_title.replace("of Charles Dickens", "")

		new_title = string.strip(new_title)

	return new_title, is_eponymous, old_eponymous_character, new_eponymous_character


def demo_titles(num=10):
	loopcount = 0
	for n in range(0,num):
		loopcount = loopcount + 1
		old_title = source.index.characters_dict[random.choice(source.index.characters_dict.keys())]["title"]
		new_title, is_eponymous, old_eponymous_character, new_eponymous_character = make_title(old_title)
		print
		print "TITLE %s:\n\tnew title:\t'%s'\n\tbased on:\t'%s'" % (loopcount, new_title, old_title)

	print "\nDONE.\n\n"



def make_text(d, VERBOSE):

	if VERBOSE > 0:
		print "\tmaking text...\n"

	DEBUG = 0
	#DEBUG = 1

	if VERBOSE > 0:
		print "STAGE !: CHOOSING BOOK TO MODIFY...."


	book_info = source.index.characters_dict
	book_to_use = random.choice(book_info.keys())
	book_to_use_dict = book_info[book_to_use]

	#HACKs FOR TESTING...
	#book_to_use = "98-0.txt"

	#HARD TIMES - divided with "CHAPTER I" etc...
	#book_to_use = "786-0.txt"

	#Oliver Twist
	#book_to_use = "pg730.txt"

	#David Copperfield - divided with "CHAPTER I" etc...
	#book_to_use = "766-0.txt"

	#Holiday Romance
	#book_to_use = "809-0.txt"

	#"A Christmas Carol by Charles Dickens"
	#book_to_use = "pg19337.txt"

	#"The Wreck of the Golden Mary by Charles Dickens"],
	#book_to_use = "pg1465.txt"

	#The Personal History of David Copperfield
	#book_to_use = "pg43111.txt"

	#book_to_use_dict = book_info[book_to_use]

	print "\tchose '%s'" % book_to_use_dict["title"]

	if DEBUG == 1:
		print "book_to_use:"
		print book_to_use
		print
	book_to_use_title = book_to_use_dict["title"]

	d.dickens_book = book_to_use_title
	d.dickens_filename = book_to_use_dict["filename"]

	BOOK_TILE, is_eponymous, old_eponymous_character, new_eponymous_character = make_title(book_to_use_title)

	d.Document_Title = BOOK_TILE

	d.title_long = d.Document_Title
	d.title_split = d.Document_Title
	if string.find(BOOK_TILE, ": ") > -1:
		d.title_split = "%s:\n%s" % (string.split(d.Document_Title, ": ")[0], string.split(d.Document_Title, ": ")[1])
		
	if DEBUG == 1:
		print "book_info[book_to_use]:"
		print book_info[book_to_use]
		print
		print """book_info[book_to_use]["chapter dividers"]:"""
		print book_info[book_to_use]["chapter dividers"]
		print

	if book_info[book_to_use].has_key("chapter dividers"):
		if VERBOSE > 0:
			print "\tFOUND CHAPTER DIVIDERS OK"
		chapter_dividers = book_info[book_to_use]["chapter dividers"]
	else:
		if VERBOSE > 0:
			print "\tNO CHAPTER DIVIDERS FOUND!"
		chapter_dividers = None

	if book_info[book_to_use].has_key("chapter names"):
		if VERBOSE > 0:
			print "\tFOUND CHAPTER NAMES OK"
		chapter_names = book_info[book_to_use]["chapter names"]
	else:
		if VERBOSE > 0:
			print "\tNO CHAPTER NAMES FOUND!"
		chapter_names = None

	d.chapter_dividers = chapter_dividers
	d.chapter_names = chapter_names

	NEW_AUTHOR = names.getName()
	d.author = NEW_AUTHOR

	if d.publication_year == None:
		publication_year = time.strftime("%Y") #this year
		d.publication_year = publication_year
	if d.first_publication_year == None:
		first_publication_year = random.choice(("%s" % (int(publication_year) - 1),
												"%s" % (int(publication_year) - 2),
												"%s" % (int(publication_year) - 3),
												"%s" % (int(publication_year) - 4),
												"%s" % (int(publication_year) - 5)
												))

		d.first_publication_year = first_publication_year

	if VERBOSE > 0:
		print "\tretelling '%s'..." % book_to_use_title
		print "\tauthor:\t'%s'..." % NEW_AUTHOR

	intro = make_intro(d=d, author=NEW_AUTHOR,
					   dickens_book=d.dickens_book,
					   year=first_publication_year)

	text = "%s" % intro
	prefix, suffix = string.split(book_to_use, ".")
	dickens_fn = "%s_NEW.%s" % (prefix, suffix)

	dickens_text = io.open(os.path.join(os.getcwd(), "source", "modified", dickens_fn),
						   encoding="UTF-8", mode="r").read()
	if VERBOSE > 0:
		print "\n\tread in '%s' OK..." % (os.path.join(os.getcwd(), "source", "modified", dickens_fn))

	if VERBOSE > 1:
		print "\n\tMaking sure text is UTF-8"
	try:
		dickens_text = dickens_text.decode("UTF-8", "ignore")
	except:
		dickens_text = dickens_text.encode("UTF-8", "ignore")
	#io.open(os.path.join(os.getcwd(), "source", "modified", dickens_fn),
	#                      encoding="UTF-8", mode="r").read()
	if VERBOSE > 1:
		print "\n\t...OK"


	if VERBOSE > 1:
		print "\n\tTrimming off original front matter..."

	chapter_heads_to_check=[]

	#words - caps
	numbers_type1 = ["ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE", "TEN",
					 "ELEVEN", "TWELVE", "THIRTEEN", "FOURTEEN", "FIFTEEN", "SIXTEEN", "SEVENTEEN", "EIGHTEEN", "NINETEEN", "TWENTY",
					 "TWENTY-ONE", "TWENTY-TWO", "TWENTY-THREE", "TWENTY-FOUR", "TWENTY-FIVE", "TWENTY-SIX", "TWENTY-SEVEN", "TWENTY-EIGHT", "TWENTY-NINE", "THIRTY",
					 "THIRTY-ONE", "THIRTY-TWO", "THIRTY-THREE", "THIRTY-FOUR", "THIRTY-FIVE", "THIRTY-SIX", "THIRTY-SEVEN", "THIRTY-EIGHT", "THIRTY-NINE", "FORTY",
					 ] 

	#words - mixed case
	numbers_type1B = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
					 "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen", "Twenty",
					 ] 
	#numerals
	numbers_type2 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
					 "11", "12", "13", "14", "15", "16", "17", "18", "19", "20",
					 "21", "22", "23", "24", "25", "26", "27", "28", "29", "30",
					 "31", "32", "33", "34", "35", "36", "37", "38", "39", "40",
					 "41", "42", "43", "44", "45", "46", "47", "48", "49", "50",
					 "51", "52", "53", "54", "55", "56", "57", "58", "59", "60",
					 "61", "62", "63", "64", "65", "66", "67", "68", "69", "70",
					 "71", "72", "73", "74", "75", "76", "77", "78", "79", "80",
					 "81", "82", "83", "84", "85", "86", "87", "88", "89", "90",
					 ] 

	numbers_type2B = ["1.", "2.", "3.", "4.", "5.", "6.", "7.", "8.", "9.", "10.",
					 "11.", "12.", "13.", "14.", "15.", "16.", "17.", "18.", "19.", "20.",
					 "21.", "22.", "23.", "24.", "25.", "26.", "27.", "28.", "29.", "30.",
					 "31.", "32.", "33.", "34.", "35.", "36.", "37.", "38.", "39.", "40.",
					 "41.", "42.", "43.", "44.", "45.", "46.", "47.", "48.", "49.", "50.",
					 "51.", "52.", "53.", "54.", "55.", "56.", "57.", "58.", "59.", "60.",
					 "61.", "62.", "63.", "64.", "65.", "66.", "67.", "68.", "69.", "70.",
					 "71.", "72.", "73.", "74.", "75.", "76.", "77.", "78.", "79.", "80.",
					 "81.", "82.", "83.", "84.", "85.", "86.", "87.", "88.", "89.", "90.",
					 ] 

	#Roman numerals
	numbers_type3 = ["I", "II", "III", "IV", "V", "VI", "VI", "VIII", "IX", "X",
					 "XI", "XII", "XIII", "XIV", "XV", "XVI", "XVI", "XVIII", "XIX", "XX",
					 "XXI", "XXII", "XXIII", "XXIV", "XXV", "XXVI", "XXVI", "XXVIII", "XXIX", "XXX",
					 "XXXI", "XXXII", "XXXIII", "XXXIV", "XXXV", "XXXVI", "XXXVI", "XXXVIII", "XXXIX", "XL",
					 "XLI", "XLII", "XLIII", "XLIV", "XLV", "XLVI", "XLVII", "XLVIII", "XLIX", "L",
					 "LI", "LII", "LIII", "LIV", "LV", "LVI", "LVII", "LVIII", "LIX", "LX",
					 "LXI", "LXII", "LXIII", "LXIV", "LXV", "LXVI", "LXVII", "LXVIII", "LXIX", "LXX",
					 "LXXI", "LXXII", "LXXIII", "LXXIV", "LXXV", "LXXVI", "LXXVII", "LXXVIII", "LXXIX", "LXXX",
					 ] 

	numbers_type4 = ["FIRST", "SECOND", "THIRD", "FOURTH", "FIFTH", "SIXTH", "SEVENTH", "EIGHT", "NINTH", "TENTH",
					 ] 
					 

	if 	d.chapter_dividers != None:
		cd = d.chapter_dividers

		if VERBOSE > 0:
			print "checking for '%s %s'..." % (cd, numbers_type1[0])
		if string.find(dickens_text, "%s %s" % (cd, numbers_type1[0])) > -1:
			item = "%s %s" % (cd, numbers_type1[0])
			if VERBOSE > 0:
				print "FOUND '%s'!" % item
			for dx in numbers_type1:
				chapter_heads_to_check.append("%s %s" % (cd, dx))

		if VERBOSE > 0:
			print "checking for '%s %s'..." % (cd, numbers_type1B[0])
		if string.find(dickens_text, "%s %s" % (cd, numbers_type1B[0])) > -1:
			item = "%s %s" % (cd, numbers_type1B[0])
			for dx in numbers_type1B:
				chapter_heads_to_check.append("%s %s" % (cd, dx))

		if VERBOSE > 0:
			print "checking for '%s %s'..." % (cd, numbers_type2[0])
		if string.find(dickens_text, "%s %s" % (cd, numbers_type2[0])) > -1:
			item = "%s %s" % (cd, numbers_type2[0])
			if VERBOSE > 0:
				print "FOUND '%s'!" % item
			for dx in numbers_type2:
				chapter_heads_to_check.append("%s %s" % (cd, dx))

		if VERBOSE > 0:
			print "checking for '%s %s'..." % (cd, numbers_type2B[0])
		if string.find(dickens_text, "%s %s" % (cd, numbers_type2B[0])) > -1:
			item = "%s %s" % (cd, numbers_type2B[0])
			if VERBOSE > 0:
				print "FOUND '%s'!" % item
			for dx in numbers_type2:
				chapter_heads_to_check.append("%s %s" % (cd, dx))

		if VERBOSE > 0:
			print "checking for '%s %s'..." % (cd, numbers_type3[0])
		if string.find(dickens_text, "%s %s" % (cd, numbers_type3[0])) > -1:
			item = "%s %s" % (cd, numbers_type3[0])
			if VERBOSE > 0:
				print "FOUND '%s'!" % item
			for dx in numbers_type3:
				chapter_heads_to_check.append("%s %s" % (cd, dx))

		if VERBOSE > 0:
			print "checking for '%s %s'..." % (cd, numbers_type4[0])
		if string.find(dickens_text, "%s %s" % (cd, numbers_type4[0])) > -1:
			item = "%s %s" % (cd, numbers_type4[0])
			if VERBOSE > 0:
				print "FOUND '%s'!" % item
			for dx in numbers_type4:
				chapter_heads_to_check.append("%s %s" % (cd, dx))

		if VERBOSE > 0:
			print "checking for '%s%s'..." % (cd, numbers_type1[0])
		if string.find(dickens_text, "%s%s" % (cd, numbers_type1[0])) > -1:
			item = "%s%s" % (cd, numbers_type1[0])
			if VERBOSE > 0:
				print "FOUND '%s'!" % item
			for dx in numbers_type1:
				chapter_heads_to_check.append("%s%s" % (cd, dx))

		if VERBOSE > 0:
			print "checking for '%s%s'..." % (cd, numbers_type1B[0])
		if string.find(dickens_text, "%s%s" % (cd, numbers_type1B[0])) > -1:
			item = "%s%s" % (cd, numbers_type1B[0])
			if VERBOSE > 0:
				print "FOUND '%s'!" % item
			for dx in numbers_type1B:
				chapter_heads_to_check.append("%s%s" % (cd, dx))

		if VERBOSE > 0:
			print "checking for '%s%s'..." % (cd, numbers_type2[0])
		if string.find(dickens_text, "%s%s" % (cd, numbers_type2[0])) > -1:
			item = "%s%s" % (cd, numbers_type2[0])
			if VERBOSE > 0:
				print "FOUND '%s'!" % item
			for dx in numbers_type2:
				chapter_heads_to_check.append("%s%s" % (cd, dx))

		if VERBOSE > 0:
			print "checking for '%s%s'..." % (cd, numbers_type3[0])
		if string.find(dickens_text, "%s%s" % (cd, numbers_type3[0])) > -1:
			item = "%s%s" % (cd, numbers_type3[0])
			if VERBOSE > 0:
				print "FOUND '%s'!" % item
			for dx in numbers_type3:
				chapter_heads_to_check.append("%s%s" % (cd, dx))

		if VERBOSE > 0:
			print "checking for '%s%s'..." % (cd, numbers_type4[0])
		if string.find(dickens_text, "%s%s" % (cd, numbers_type4[0])) > -1:
			item = "%s%s" % (cd, numbers_type4[0])
			if VERBOSE > 0:
				print "FOUND '%s'!" % item
			for dx in numbers_type4:
				chapter_heads_to_check.append("%s %s" % (cd, dx))

		if VERBOSE > 0:
			print "chapter_heads_to_check:"
			print chapter_heads_to_check
		d.chapter_heads_to_check = chapter_heads_to_check

	elif d.chapter_names != None:
		chapter_heads_to_check = d.chapter_names
		d.chapter_heads_to_check = chapter_heads_to_check

		if VERBOSE > 0:
			print "chapter_heads_to_check:"
			print chapter_heads_to_check
		d.chapter_heads_to_check = chapter_heads_to_check

	if 	d.chapter_heads_to_check in [None, []]:
		if 	d.chapter_dividers != None:
			dickens_text = dickens_text[dickens_text.index(chapter_dividers):]
			if VERBOSE > 1:
				print "trimmed to '%s'" % chapter_dividers 
		elif d.chapter_names != None:
			dickens_text = dickens_text[dickens_text.index(chapter_names[0]):]
			if VERBOSE > 1:
				print "trimmed to '%s'" % chapter_names[0]

	if VERBOSE > 1:
		print "\n\t...OK"

	dt_split = dickens_text.split("\n")
	print "\t (length of file: %s lines)" % len(dt_split)

	#do our substitutions here...

	#remove any misc rubbish... Publishers' info, prefaces to old editions, notes from transcribers etc...
	if book_to_use_dict.has_key("garbage to delete"):
		for line in book_to_use_dict["garbage to delete"]:
			#dickens_text = dickens_text.replace(line, "") # remove it completely
			try:
				try:
					dickens_text = dickens_text.replace(line.decode("UTF-8", "ignore"), "") # remove it completely
				except:
					dickens_text = dickens_text.replace(line.encode("UTF-8", "ignore"), "") # remove it completely
			except:
				pass # FIX LATER!

	author_placeholder = "[AUTHOR]"
	author_placeholder_caps = "[AUTHOR_CAPS]"

	#NEW_AUTHOR
	NEW_AUTHOR_CAPS = string.upper(NEW_AUTHOR)
	try:
		dickens_text = dickens_text.replace(author_placeholder.decode("UTF-8", "ignore"),
											NEW_AUTHOR.decode("UTF-8", "ignore"))
	except:
		dickens_text = dickens_text.replace(author_placeholder.encode("UTF-8", "ignore"),
											NEW_AUTHOR.encode("UTF-8", "ignore"))

	try:
		dickens_text = dickens_text.replace(author_placeholder_caps.decode("UTF-8", "ignore"),
											NEW_AUTHOR_CAPS.decode("UTF-8", "ignore"))
	except:
		dickens_text = dickens_text.replace(author_placeholder_caps.encode("UTF-8", "ignore"),
											NEW_AUTHOR_CAPS.encode("UTF-8", "ignore"))

	book_placeholder = "[BOOK_SHORT_TITLE]"
	book_placeholder_caps = "[BOOK_SHORT_TITLE_CAPS]"

	NEW_TITLE = d.title_long
	NEW_TITLE_CAPS = string.upper(d.title_long)


	try:
		dickens_text = dickens_text.replace(book_placeholder.decode("UTF-8", "ignore"),
											NEW_TITLE.decode("UTF-8", "ignore"))
	except:
		dickens_text = dickens_text.replace(book_placeholder.encode("UTF-8", "ignore"),
											NEW_TITLE.encode("UTF-8", "ignore"))

	try:
		dickens_text = dickens_text.replace(book_placeholder_caps.decode("UTF-8", "ignore"),
											NEW_TITLE_CAPS.decode("UTF-8", "ignore"))
	except:
		dickens_text = dickens_text.replace(book_placeholder_caps.encode("UTF-8", "ignore"),
											NEW_TITLE_CAPS.encode("UTF-8", "ignore"))

	if VERBOSE > 0:
		print "\nSTAGE 2: modifying text ...."

	if VERBOSE > 0:
		print "\tRunning 'cleanup' routine...."

	#cleanup is our routine to removes some of the worst excesses of
	#Dickens' over-wordy style.

	#text = cleanup(text, VERBOSE=VERBOSE, use_log=0)

	dickens_text = cleanup(dickens_text, VERBOSE=VERBOSE, use_log=0)

	if VERBOSE > 0:
		print "\tOK.\n"

	if VERBOSE > 0:
		print "\tInserting synonyms...."

	#now try to replace synonyms using NLTK

	dickens_text = modify_text(dickens_text, VERBOSE=VERBOSE, d=d)

	if VERBOSE > 0:
		print "\tOK.\n"

	if VERBOSE > 0:
		print "OK.\n\n"

	if VERBOSE > 0:
		print "\nSTAGE 3: DOING NAME SUBSTITUTIONS...."

	d.characters = []

	CHARACTER_NUMBER = 0
	found_characters = []
	new_characters = []
	replaced_surnames = []
	new_surnames = []

	female_titles = ["Miss", "Mrs.", "Madame", "Lady", "Mademoiselle", "Grandmother"]
	male_titles = ["Mr.", "Doctor", "Dr.", "Uncle", "Monsieur", "Marquis", "Inspector", "Captain", "Prince", "Grandfather"]
	titles = source.index.titles

	for character_name in book_to_use_dict["characters"]:

		#do all the characters first, in case they share surnames...
		CHARACTER_NUMBER = CHARACTER_NUMBER + 1
		placeholder = "[CHARACTER_NAME_%03d]" % CHARACTER_NUMBER

		placeholder_surname = "[CHARACTER_%03d_SURNAME]" % CHARACTER_NUMBER
		placeholder_firstname = "[CHARACTER_%03d_FIRSTNAME]" % CHARACTER_NUMBER
		placeholder_firstname_caps = "[CHARACTER_%03d_FIRSTNAME_CAPS]" % CHARACTER_NUMBER
		placeholder_surname_caps = "[CHARACTER_%03d_SURNAME_CAPS]" % CHARACTER_NUMBER

		if type(character_name) in (StringType, UnicodeType):

			if VERBOSE > 0:
				printstring = "\tSubstituting '%s'..." % character_name
				print printstring,
			if string.find(character_name, " ") > -1:
				firstname, surname = string.split(character_name, " ", maxsplit=1)
			elif len(string.split(character_name, " ")) == 1:
				firstname, surname = string.split(character_name, " ")[0], None
			if firstname in names.male_firstnames:
				gender = "male"
			elif firstname in names.female_firstnames:
				gender = "female"
			elif firstname in male_titles:
				gender = "male"
			elif firstname in female_titles:
				gender = "female"
			else:
				gender = "????"
			if VERBOSE > 0:
				printstring = "with a %s character..." % gender
				print printstring,

			if character_name in source.index.little_people:
				#Tiny Tim, Little Nell etc
				NEW_CHARACTER = make_a_small_person(character_name)

			elif gender == "male":
				if len(string.split(character_name, " ")) == 2:
					NEW_CHARACTER = names.getMaleName()
					NEW_FIRSTNAME, NEW_SURNAME = string.split(NEW_CHARACTER, " ")
				elif len(string.split(character_name, " ")) == 1:
					NEW_CHARACTER = names.getMaleFirstName()
					NEW_FIRSTNAME, NEW_SURNAME = NEW_CHARACTER, None
				else:
					NEW_CHARACTER = names.getMaleName()
					NEW_FIRSTNAME, NEW_SURNAME = string.split(NEW_CHARACTER, " ")
			elif gender == "female":
				if len(string.split(character_name, " ")) == 2:
					NEW_CHARACTER = names.getFemaleName()
					NEW_FIRSTNAME, NEW_SURNAME = string.split(NEW_CHARACTER, " ")
				elif len(string.split(character_name, " ")) == 1:
					NEW_CHARACTER = names.getFemaleFirstName()
					NEW_FIRSTNAME, NEW_SURNAME = NEW_CHARACTER, None
				else:
					NEW_CHARACTER = names.getFemaleName()
					NEW_FIRSTNAME, NEW_SURNAME = string.split(NEW_CHARACTER, " ")

			elif gender == "????":
				#this is Dickens... assume it's a surname
				NEW_CHARACTER = names.getSurname()
				NEW_FIRSTNAME, NEW_SURNAME = None, NEW_CHARACTER

			if character_name in source.index.exceptions:
				NEW_CHARACTER = character_name
				NEW_FIRSTNAME, NEW_SURNAME = string.split(character_name, " ", maxsplit=1)

			if string.find(character_name, "[") > -1:
				print "\tcharacter_name: '%s' " % character_name
				print "\tNEW_CHARACTER: ", NEW_CHARACTER
				print "\tNEW_FIRSTNAME: ", NEW_FIRSTNAME
				print "\tNEW_SURNAME: ", NEW_SURNAME

			found_characters.append(character_name)
			if surname != None:
				if surname in replaced_surnames:
					if NEW_SURNAME != None:
						NEW_CHARACTER = NEW_CHARACTER.replace(NEW_SURNAME,
															  new_surnames[replaced_surnames.index(surname)])
				else:
					replaced_surnames.append(surname)
					new_surnames.append(NEW_SURNAME)

			if firstname in male_titles:
				NEW_CHARACTER = NEW_CHARACTER.replace(NEW_FIRSTNAME,
													  firstname)
				NEW_FIRSTNAME = firstname
			elif firstname in female_titles:
				NEW_CHARACTER = NEW_CHARACTER.replace(NEW_FIRSTNAME,
													  firstname)
				NEW_FIRSTNAME = firstname

			if character_name[-4:] == ", Jr":
				#for eg 'Thomas Gradgrind, Jr'
				sr_character = character_name[:-4]
				if sr_character in found_characters:
					NEW_CHARACTER = "%s, Jr" % new_characters[found_characters.index(sr_character)]

			if character_name[-4:] == ", Sr":
				#for eg 'Barnaby Rudge, Sr'
				jr_character = character_name[:-4]
				if jr_character in found_characters:
					NEW_CHARACTER = "%s, Sr" % new_characters[found_characters.index(jr_character)]

			new_characters.append(NEW_CHARACTER)
			if VERBOSE > 0:
				print "called '%s'." % NEW_CHARACTER
			else:
				print ".",
								
			character_name_caps = string.upper(character_name)
			new_character_name_caps = string.upper(NEW_CHARACTER)

			placeholder_caps = "[CHARACTER_NAME_CAPS_%03d]" % CHARACTER_NUMBER
			if VERBOSE > 1:
				print "\t\treplacing '%s" % placeholder
			if VERBOSE > 1:
				print "\t\t\tstring.find(dickens_text, placeholder)[BEFORE REPLACE]:",string.find(dickens_text, placeholder)
			try:
				dickens_text = dickens_text.replace(placeholder, NEW_CHARACTER)
			except:
				try:
					dickens_text = dickens_text.replace(placeholder, NEW_CHARACTER)
				except:
					print """FAILED ON '%s'!""" % NEW_CHARACTER
			if VERBOSE > 1:
				print "\t\t\tstring.find(dickens_text, placeholder)[AFTER REPLACE]:",string.find(dickens_text, placeholder)

			if VERBOSE > 1:
				print "\t\treplacing '%s" % placeholder_caps
			if VERBOSE > 1:
				print "\t\t\tstring.find(dickens_text, placeholder_caps)[BEFORE REPLACE]:",string.find(dickens_text, placeholder_caps)
			try:
				dickens_text = dickens_text.replace(placeholder_caps, new_character_name_caps)
			except:
				try:
					dickens_text = dickens_text.replace(placeholder_caps, new_character_name_caps)
				except:
					print """FAILED ON '%s'!""" % new_character_name_caps
			if VERBOSE > 1:
				print "\t\t\tstring.find(dickens_text, placeholder_caps)[AFTER REPLACE]:",string.find(dickens_text, placeholder_caps)

			d.characters.append(NEW_CHARACTER)
			if VERBOSE > 1:
				print "\t\tAdded character '%s' to d.characters..." % (NEW_CHARACTER)
			if book_to_use_dict.has_key("main character"):
				if character_name == book_to_use_dict["main character"]:
					d.main_character = NEW_CHARACTER
					if VERBOSE > 0:
						print "\t\tCharacter '%s' is the MAIN CHARACTER!" % (NEW_CHARACTER)

			# placeholder_surname
			if VERBOSE > 1:
				print "\t\treplacing '%s" % placeholder_surname
			if VERBOSE > 1:
				print "\t\t\tstring.find(dickens_text, placeholder)[BEFORE REPLACE]:",string.find(dickens_text, placeholder_surname)

			if NEW_SURNAME in [None, ""]:
				try:
					dickens_text = dickens_text.replace(placeholder_surname, "")
				except:
					try:
						dickens_text = dickens_text.replace(placeholder_surname, "")
					except:
						print """FAILED ON '%s'!""" % NEW_SURNAME
			else:
				try:
					dickens_text = dickens_text.replace(placeholder_surname, NEW_SURNAME)
				except:
					try:
						dickens_text = dickens_text.replace(placeholder_surname, NEW_SURNAME)
					except:
						print """FAILED ON '%s'!""" % NEW_SURNAME
			if VERBOSE > 1:
				print "\t\t\tstring.find(dickens_text, placeholder_surname)[AFTER REPLACE]:",string.find(dickens_text, placeholder_surname)

			# placeholder_firstname
			if VERBOSE > 1:
				print "\t\treplacing '%s" % placeholder_firstname
			if VERBOSE > 1:
				print "\t\t\tstring.find(dickens_text, placeholder_firstname)[BEFORE REPLACE]:",string.find(dickens_text, placeholder_firstname)

			if NEW_FIRSTNAME == None:
				try:
					dickens_text = dickens_text.replace(placeholder_firstname, "")
				except:
					try:
						dickens_text = dickens_text.replace(placeholder_firstname, "")
					except:
						print """FAILED ON '%s'!""" % NEW_FIRSTNAME
			else:
				try:
					dickens_text = dickens_text.replace(placeholder_firstname, NEW_FIRSTNAME)
				except:
					try:
						dickens_text = dickens_text.replace(placeholder_firstname, NEW_FIRSTNAME)
					except:
						print """FAILED ON '%s'!""" % NEW_FIRSTNAME
			if VERBOSE > 1:
				print "\t\t\tstring.find(dickens_text, placeholder)[AFTER REPLACE]:",string.find(dickens_text, placeholder_firstname)

			#placeholder_firstname_caps
			if VERBOSE > 1:
				print "\t\treplacing '%s" % placeholder_firstname_caps
			if VERBOSE > 1:
				print "\t\t\tstring.find(dickens_text, placeholder)[BEFORE REPLACE]:",string.find(dickens_text, placeholder_firstname_caps)

			if NEW_FIRSTNAME != None:
				try:
					dickens_text = dickens_text.replace(placeholder_firstname_caps, string.upper(NEW_FIRSTNAME))
				except:
					try:
						dickens_text = dickens_text.replace(placeholder_firstname_caps, string.upper(NEW_FIRSTNAME))
					except:
						print """FAILED ON '%s'!""" % string.upper(NEW_FIRSTNAME)
			else:
				try:
					dickens_text = dickens_text.replace(placeholder_firstname_caps, string.upper(NEW_SURNAME))
				except:
					try:
						dickens_text = dickens_text.replace(placeholder_firstname_caps, string.upper(NEW_SURNAME))
					except:
						print """FAILED ON '%s'!""" % string.upper(NEW_SURNAME)

			if VERBOSE > 1:
				print "\t\t\tstring.find(dickens_text, placeholder)[AFTER REPLACE]:",string.find(dickens_text, placeholder_firstname_caps)

			# placeholder_surname_caps
			if VERBOSE > 1:
				print "\t\treplacing '%s" % placeholder_surname_caps
			if VERBOSE > 1:
				print "\t\t\tstring.find(dickens_text, placeholder)[BEFORE REPLACE]:",string.find(dickens_text, placeholder_surname_caps)
			if NEW_SURNAME != None:
				try:
					dickens_text = dickens_text.replace(placeholder_surname_caps, string.upper(NEW_SURNAME))
				except:
					try:
						dickens_text = dickens_text.replace(placeholder_surname_caps, string.upper(NEW_SURNAME))
					except:
						print """FAILED ON '%s'!""" % string.upper(NEW_SURNAME)
			else:
				try:
					dickens_text = dickens_text.replace(placeholder_surname_caps, string.upper(NEW_CHARACTER))
				except:
					try:
						dickens_text = dickens_text.replace(placeholder_surname_caps, string.upper(NEW_CHARACTER))
					except:
						print """FAILED ON '%s'!""" % string.upper(NEW_CHARACTER)

			if VERBOSE > 1:
				print "\t\t\tstring.find(dickens_text, placeholder)[AFTER REPLACE]:",string.find(dickens_text, placeholder_surname_caps)

		elif type(character_name) in (TupleType, ListType):
			for cn in character_name:
				character_name_caps = string.upper(cn)
				placeholder_caps = "[CHARACTER_NAME_CAPS_%03d]" % CHARACTER_NUMBER

				if cn in found_characters:
					NEW_CHARACTER = "%s" % new_characters[found_characters.index(cn)]
					if len(string.split(NEW_CHARACTER)) == 2:
						NEW_FIRSTNAME, NEW_SURNAME = string.split(NEW_CHARACTER, " ")
					elif len(string.split(NEW_CHARACTER)) == 1:
						if NEW_CHARACTER in names.female_firstnames:
							NEW_FIRSTNAME, NEW_SURNAME = NEW_CHARACTER, None
						elif NEW_CHARACTER in names.male_firstnames:
							NEW_FIRSTNAME, NEW_SURNAME = NEW_CHARACTER, None
						else:
							NEW_FIRSTNAME, NEW_SURNAME = None, NEW_CHARACTER
				else:
					if VERBOSE > 0:
						printstring = "\tSubstituting '%s'..." % cn
						print printstring,
					if string.find(cn, " ") > -1:
						firstname, surname = string.split(cn, " ", maxsplit=1)
					elif len(string.split(cn, " ")) == 1:
						firstname, surname = string.split(cn, " ")[0], None
					if firstname in names.male_firstnames:
						gender = "male"
					elif firstname in names.female_firstnames:
						gender = "female"
					elif firstname in male_titles:
						gender = "male"
					elif firstname in female_titles:
						gender = "female"
					else:
						gender = "????"
					if VERBOSE > 0:
						printstring = "with a %s character..." % gender
						print printstring,
					if gender == "male":
						if len(string.split(cn, " ")) == 2:
							NEW_CHARACTER = names.getMaleName()
							NEW_FIRSTNAME, NEW_SURNAME = string.split(NEW_CHARACTER, " ")
						elif len(string.split(cn, " ")) == 1:
							NEW_CHARACTER = names.getMaleFirstName()
							NEW_FIRSTNAME, NEW_SURNAME = NEW_CHARACTER, None
						else:
							NEW_CHARACTER = names.getMaleName()
							NEW_FIRSTNAME, NEW_SURNAME = string.split(NEW_CHARACTER, " ", maxsplit=2)
					elif gender == "female":
						if len(string.split(cn, " ")) == 2:
							NEW_CHARACTER = names.getFemaleName()
							NEW_FIRSTNAME, NEW_SURNAME = string.split(NEW_CHARACTER, " ", maxsplit=2)
						elif len(string.split(cn, " ")) == 1:
							NEW_CHARACTER = names.getFemaleFirstName()
							NEW_FIRSTNAME, NEW_SURNAME = NEW_CHARACTER, None
						else:
							NEW_CHARACTER = names.getFemaleName()
							NEW_FIRSTNAME, NEW_SURNAME = string.split(NEW_CHARACTER, " ")

					elif gender == "????":
						#this is Dickens... assume it's a surname
						NEW_CHARACTER = names.getSurname()
						NEW_FIRSTNAME, NEW_SURNAME = None, NEW_CHARACTER

					found_characters.append(cn)
					if surname != None:
						if surname in replaced_surnames:
							if NEW_SURNAME != None:
								NEW_CHARACTER = NEW_CHARACTER.replace(NEW_SURNAME,
																	  new_surnames[replaced_surnames.index(surname)])
						else:
							replaced_surnames.append(surname)
							new_surnames.append(NEW_SURNAME)

					if firstname in male_titles:
						NEW_CHARACTER = NEW_CHARACTER.replace(NEW_FIRSTNAME,
															  firstname)
					elif firstname in female_titles:
						NEW_CHARACTER = NEW_CHARACTER.replace(NEW_FIRSTNAME,
															  firstname)

					if cn[-4:] == ", Jr":
						#for eg 'Thomas Gradgrind, Jr'
						sr_character = cn[:-4]
						if sr_character in found_characters:
							NEW_CHARACTER = "%s, Jr" % new_characters[found_characters.index(sr_character)]

					if cn[-4:] == ", Sr":
						#for eg 'Barnaby Rudge, Sr'
						jr_character = cn[:-4]
						if jr_character in found_characters:
							NEW_CHARACTER = "%s, Sr" % new_characters[found_characters.index(jr_character)]


					new_characters.append(NEW_CHARACTER)
					if VERBOSE > 0:
						print "called '%s'." % NEW_CHARACTER
										
					character_name_caps = string.upper(cn)
					new_character_name_caps = string.upper(NEW_CHARACTER)

				if VERBOSE > 1:
					print "\t\treplacing '%s" % placeholder
					print "\t\treplacing '%s" % placeholder_caps
				if VERBOSE > 1:
					print "\t\t\tstring.find(dickens_text, placeholder)[BEFORE REPLACE]:",string.find(dickens_text, placeholder)
					print "\t\t\tstring.find(dickens_text, placeholder_caps)[BEFORE REPLACE]:",string.find(dickens_text, placeholder_caps)
				try:
					dickens_text = dickens_text.replace(placeholder, NEW_CHARACTER)
					dickens_text = dickens_text.replace(placeholder_caps, new_character_name_caps)
				except:
					dickens_text = dickens_text.replace(placeholder, NEW_CHARACTER)
					dickens_text = dickens_text.replace(placeholder_caps, new_character_name_caps)

				# placeholder_surname
				if VERBOSE > 1:
					print "\t\treplacing '%s" % placeholder_surname
				if VERBOSE > 1:
					print "\t\t\tstring.find(dickens_text, placeholder)[BEFORE REPLACE]:",string.find(dickens_text, placeholder_surname)
				try:
					dickens_text = dickens_text.replace(placeholder_surname, NEW_SURNAME)
				except:
					try:
						dickens_text = dickens_text.replace(placeholder_surname, NEW_SURNAME)
					except:
						print """FAILED ON '%s'!""" % NEW_SURNAME
				if VERBOSE > 1:
					print "\t\t\tstring.find(dickens_text, placeholder_surname)[AFTER REPLACE]:",string.find(dickens_text, placeholder_surname)

				# placeholder_firstname
				if VERBOSE > 1:
					print "\t\treplacing '%s" % placeholder_firstname
				if VERBOSE > 1:
					print "\t\t\tstring.find(dickens_text, placeholder_firstname)[BEFORE REPLACE]:",string.find(dickens_text, placeholder_firstname)
				try:
					dickens_text = dickens_text.replace(placeholder_firstname, NEW_FIRSTNAME)
				except:
					try:
						dickens_text = dickens_text.replace(placeholder_firstname, NEW_FIRSTNAME)
					except:
						print """FAILED ON '%s'!""" % NEW_FIRSTNAME
				if VERBOSE > 1:
					print "\t\t\tstring.find(dickens_text, placeholder)[AFTER REPLACE]:",string.find(dickens_text, placeholder_firstname)

				#placeholder_firstname_caps
				if VERBOSE > 1:
					print "\t\treplacing '%s" % placeholder_firstname_caps
				if VERBOSE > 1:
					print "\t\t\tstring.find(dickens_text, placeholder)[BEFORE REPLACE]:",string.find(dickens_text, placeholder_firstname_caps)

				if NEW_FIRSTNAME != None:
					try:
						dickens_text = dickens_text.replace(placeholder_firstname_caps, string.upper(NEW_FIRSTNAME))
					except:
						try:
							dickens_text = dickens_text.replace(placeholder_firstname_caps, string.upper(NEW_FIRSTNAME))
						except:
							print """FAILED ON '%s'!""" % string.upper(NEW_FIRSTNAME)
				else:
					try:
						dickens_text = dickens_text.replace(placeholder_firstname_caps, string.upper(NEW_CHARACTER))
					except:
						try:
							dickens_text = dickens_text.replace(placeholder_firstname_caps, string.upper(NEW_CHARACTER))
						except:
							print """FAILED ON '%s'!""" % string.upper(NEW_FIRSTNAME)
				if VERBOSE > 1:
					print "\t\t\tstring.find(dickens_text, placeholder)[AFTER REPLACE]:",string.find(dickens_text, placeholder_firstname_caps)


				# placeholder_surname_caps
				if VERBOSE > 1:
					print "\t\treplacing '%s" % placeholder_surname_caps
				if VERBOSE > 1:
					print "\t\t\tstring.find(dickens_text, placeholder)[BEFORE REPLACE]:",string.find(dickens_text, placeholder_surname_caps)
				if NEW_SURNAME != None:
					try:
						dickens_text = dickens_text.replace(placeholder_surname_caps, string.upper(NEW_SURNAME))
					except:
						try:
							dickens_text = dickens_text.replace(placeholder_surname_caps, string.upper(NEW_SURNAME))
						except:
							print """FAILED ON '%s'!""" % string.upper(NEW_SURNAME)
				else:
					try:
						dickens_text = dickens_text.replace(placeholder_surname_caps, string.upper(NEW_CHARACTER))
					except:
						try:
							dickens_text = dickens_text.replace(placeholder_surname_caps, string.upper(NEW_CHARACTER))
						except:
							print """FAILED ON '%s'!""" % string.upper(NEW_CHARACTER)
				if VERBOSE > 1:
					print "\t\t\tstring.find(dickens_text, placeholder)[AFTER REPLACE]:",string.find(dickens_text, placeholder_surname_caps)

				if VERBOSE > 1:
					print "\t\t\tstring.find(dickens_text, placeholder_caps)[AFTER REPLACE]:",string.find(dickens_text, placeholder_caps)

				d.characters.append(NEW_CHARACTER)
				if VERBOSE > 0:
					print "\t\tAdded character '%s' to d.characters..." % (NEW_CHARACTER)
				if book_to_use_dict.has_key("main character"):
					if character_name == book_to_use_dict["main character"]:
						d.main_character = NEW_CHARACTER
						if VERBOSE > 0:
							print "\t\tCharacter '%s' is the MAIN CHARACTER!" % (NEW_CHARACTER)

	CHARACTER_NUMBER = 0
	for character_name in book_to_use_dict["characters"]:
		CHARACTER_NUMBER = CHARACTER_NUMBER + 1
		if type(character_name) in (StringType, UnicodeType):
			if len(string.split(character_name, " ")) == 2:
				#firstname, surname = string.split(character_name, " ")
				firstname, surname = string.split(character_name, " ")

				if character_name in found_characters:
					NEW_CHARACTER = "%s" % new_characters[found_characters.index(character_name)]
					if len(string.split(NEW_CHARACTER)) == 2:
						NEW_FIRSTNAME, NEW_SURNAME = string.split(NEW_CHARACTER, " ")
					elif len(string.split(NEW_CHARACTER)) == 1:
						if NEW_CHARACTER in names.female_firstnames:
							NEW_FIRSTNAME, NEW_SURNAME = NEW_CHARACTER, None
						elif NEW_CHARACTER in names.male_firstnames:
							NEW_FIRSTNAME, NEW_SURNAME = NEW_CHARACTER, None
						else:
							NEW_FIRSTNAME, NEW_SURNAME = None, NEW_CHARACTER

				surname_placeholder = "[CHARACTER_%03d_SURNAME]" % CHARACTER_NUMBER
				firstname_placeholder = "[CHARACTER_%03d_FIRSTNAME]" % CHARACTER_NUMBER
				if firstname not in titles:
					if VERBOSE > 1:
						print "\t\treplacing '%s" % firstname_placeholder
					if VERBOSE > 1:
						print "\t\t\tstring.find(dickens_text, firstname_placeholder)[BEFORE REPLACE]:",string.find(dickens_text, firstname_placeholder)
					try:
						if NEW_FIRSTNAME != None:
							dickens_text = dickens_text.replace(firstname_placeholder, NEW_FIRSTNAME)
					except:
						if NEW_FIRSTNAME != None:
							dickens_text = dickens_text.replace(firstname_placeholder, NEW_FIRSTNAME)
					if VERBOSE > 1:
						print "\t\t\tstring.find(dickens_text, firstname_placeholder)[AFTER REPLACE]:",string.find(dickens_text, firstname_placeholder)

				if VERBOSE > 1:
					print "\t\treplacing '%s" % surname_placeholder
				if VERBOSE > 1:
					print "\t\t\tstring.find(dickens_text, surname_placeholder)[AFTER REPLACE]:",string.find(dickens_text, surname_placeholder)
				try:
					if NEW_SURNAME != None:
						dickens_text = dickens_text.replace(surname_placeholder, NEW_SURNAME)
				except:
					try:
						if NEW_SURNAME != None:
							dickens_text = dickens_text.replace(surname_placeholder, NEW_SURNAME)
					except:
						print "FAILED ON '%s'!" % surname
				if VERBOSE > 1:
					print "\t\t\tstring.find(dickens_text, surname_placeholder)[AFTER REPLACE]:",string.find(dickens_text, surname_placeholder)

		elif type(character_name) in (TupleType, ListType):
			for cn in character_name:
				if len(string.split(cn, " ")) == 2:
					firstname, surname = string.split(cn, " ")
					surname_placeholder = "[CHARACTER_%03d_SURNAME]" % CHARACTER_NUMBER
					firstname_placeholder = "[CHARACTER_%03d_FIRSTNAME]" % CHARACTER_NUMBER

					if cn in found_characters:
						NEW_CHARACTER = "%s" % new_characters[found_characters.index(cn)]
						if len(string.split(NEW_CHARACTER)) == 2:
							NEW_FIRSTNAME, NEW_SURNAME = string.split(NEW_CHARACTER, " ")
						elif len(string.split(NEW_CHARACTER)) == 1:
							if NEW_CHARACTER in names.female_firstnames:
								NEW_FIRSTNAME, NEW_SURNAME = NEW_CHARACTER, None
							elif NEW_CHARACTER in names.male_firstnames:
								NEW_FIRSTNAME, NEW_SURNAME = NEW_CHARACTER, None
							else:
								NEW_FIRSTNAME, NEW_SURNAME = None, NEW_CHARACTER

					if firstname not in titles:
						if VERBOSE > 1:
							print "\t\treplacing '%s" % firstname_placeholder
						if VERBOSE > 1:
							print "\t\t\tstring.find(dickens_text, firstname_placeholder)[BEFORE REPLACE]:",string.find(dickens_text, firstname_placeholder)
						try:
							if NEW_FIRSTNAME != None:
								dickens_text = dickens_text.replace(firstname_placeholder, NEW_FIRSTNAME)
							else:
								if NEW_SURNAME != None:
									dickens_text = dickens_text.replace(firstname_placeholder, NEW_SURNAME)
						except:
							if NEW_FIRSTNAME != None:
								dickens_text = dickens_text.replace(firstname_placeholder, NEW_FIRSTNAME)
							else:
								if NEW_SURNAME != None:
									dickens_text = dickens_text.replace(firstname_placeholder, NEW_SURNAME)
					if VERBOSE > 1:
						print "\t\t\tstring.find(dickens_text, firstname_placeholder)[AFTER REPLACE]:",string.find(dickens_text, firstname_placeholder)

					if VERBOSE > 1:
						print "\t\treplacing '%s" % surname_placeholder
					if VERBOSE > 1:
						print "\t\t\tstring.find(dickens_text, surname_placeholder)[BEFORE REPLACE]:",string.find(dickens_text, surname_placeholder)
					try:
						if NEW_SURNAME != None:
							dickens_text = dickens_text.replace(surname_placeholder, NEW_SURNAME)
						else:
							if NEW_FIRSTNAME != None:
								dickens_text = dickens_text.replace(surname_placeholder, NEW_FIRSTNAME)
					except:
						if NEW_SURNAME != None:
							dickens_text = dickens_text.replace(surname_placeholder, NEW_SURNAME)
						else:
							if NEW_FIRSTNAME != None:
								dickens_text = dickens_text.replace(surname_placeholder, NEW_FIRSTNAME)
					if VERBOSE > 1:
						print "\t\t\tstring.find(dickens_text, surname_placeholder)[AFTER REPLACE]:",string.find(dickens_text, surname_placeholder)

	#a few last little fixes...

	if string.find(dickens_text, "_") > -1:
		dickens_text = string.replace(dickens_text, "_", "")
	if string.find(dickens_text, "\n ") > -1:
		dickens_text = string.replace(dickens_text, "\n ", "\n")
	if string.find(dickens_text, "  ") > -1:
		dickens_text = string.replace(dickens_text, "  ", " ")

	#can't just replace all instances of California in use_nltk, because
	#there are a couple of legit mentions of California in the source texts
	if string.find(dickens_text, "californiant") > -1:
		dickens_text = string.replace(dickens_text, "californiant", "can't")
	if string.find(dickens_text, "calciumn't") > -1:
		dickens_text = string.replace(dickens_text, "calciumn't", "can't")

	try:
		text = "%s\n%s" % (text.decode("UTF-8", "Ignore"), dickens_text.decode("UTF-8", "Ignore"))
	except:
		text = "%s\n%s" % (text.encode("UTF-8", "Ignore"), dickens_text.encode("UTF-8", "Ignore"))

	d.text = text

	print

	if DEBUG == 1:
		storyfile = open(os.path.join(os.getcwd(), "TEMP", "STORY.txt"), "w")
		for line in text.split("\n"):
			storyfile.write("%s\n" % line)
		storyfile.close()
		if VERBOSE > 0:
			print "\nwrote file '%s.\n\n" % os.path.join(os.getcwd(), "TEMP", "STORY.txt")
		

	if VERBOSE > 0:
		print "DONE.\n\n"

	return d, text


def doFurniture(c,d, section="", page=""):
	"""adds furniture to a page (headers and footers)"""

	c.setFont("Gentium Basic", 10)

	fiddle = 50

	sectionfiddle = stringWidth(section, "Gentium Basic", 10, "latin-1")

	c.drawString(d.leftmargin, A4[1] - (d.topmargin-fiddle), "%s" % (d.title_long))
	c.drawString(A4[0] - (d.leftmargin) - sectionfiddle, A4[1] - (d.topmargin-fiddle), section)
	c.drawString(A4[0] - (d.leftmargin), (d.topmargin-fiddle), "%s" % page)

	#c.setFont("Gentium Basic", 14)
	c.setFont("Gentium Basic", 12)



def do_chapter_heading(c, d, chapter_title, VERBOSE = 0):
	c.showPage()
	x = d.leftmargin
	y = A4[1] - d.topmargin
	c.setFont("Gentium Basic Bold", 14)

	c.drawString(x, y, "%s" % (string.strip(chapter_title)))
	y = y -28
	linkname= string.replace(chapter_title, " ", "")
	c.bookmarkPage(linkname)

	c.addOutlineEntry(key=linkname, level=1, title=chapter_title, closed=None)
	c.setFont("Gentium Basic", 12)
	if VERBOSE > 0:
		print "\t\tAdded chapter title '%s'..." % chapter_title.encode("ascii", "ignore")
	
	return c,y

def add_text_to_PDF(c, d, VERBOSE=0):

	if VERBOSE > 0:
		print "\n\tAdding text to PDF..."

	xpos = d.leftmargin
	ypos = A4[1] - d.topmargin

	if d.chapter_dividers == None:
		chapter_dividers = "DUMMY-DUMMY-DUMMY"
	else:
		chapter_dividers = d.chapter_dividers
	if d.chapter_names == None:
		chapter_names = []
	else:
		chapter_names = d.chapter_names

	for x in range(0, len(chapter_names)):
		chapter_names[x] = string.strip(chapter_names[x])
		if VERBOSE > 0:
			print "\tChapter: '%s'" % chapter_names[x]
		new_chapter_name = source.index.prettify(string.strip(chapter_names[x]))
		chapter_names.append(new_chapter_name)
		if VERBOSE > 0:
			print "\t\tAdded chapter: '%s'" % new_chapter_name.encode("ascii", "ignore")

	chapter_dividers = string.strip(chapter_dividers)

	prevline = None
	for line in d.text.split("\n"):
		
		if VERBOSE == 0:
			print ".",

		#strip-out extraneous spaces
		line = string.strip(line)
		while string.find(line, "  ") > -1:
			line = string.replace(line, "  ", " ")

		if line in poss_intro_titles:
			c, y = do_chapter_heading(c, d, line, VERBOSE)
			ypos = y
		elif line in d.chapter_heads_to_check:
			c, y = do_chapter_heading(c, d, line, VERBOSE)
			ypos = y
		elif string.upper(line) in d.chapter_heads_to_check:
			c, y = do_chapter_heading(c, d, string.upper(line), VERBOSE)
			ypos = y
		elif string.strip(line) in chapter_names:
			c, y = do_chapter_heading(c, d, line, VERBOSE)
			ypos = y
		elif string.strip(line)[:len(chapter_dividers)] == chapter_dividers:
			c, y = do_chapter_heading(c, d, line, VERBOSE)
			ypos = y
		elif string.strip(line) == "[INTRO#END]":
			c.showPage()
			c.showPage()
		else:
			c.setFont("Gentium Basic", 12)
			linewidth = stringWidth(line, "Gentium Basic Bold", 12, "latin-1")

			if line in ("", None):
				#if more than 2 blank lines in a row, skip it...
				if prevline in ("", None):
					pass
				else:
					if linewidth < (A4[0] - d.leftmargin - d.rightmargin):
						newline = ""
						xpos = d.leftmargin
						if ypos < d.bottommargin:
							c.showPage()
							d.pagenum = d.pagenum + 1
							doFurniture(c,d, "", d.pagenum)
							ypos = A4[1] - d.topmargin
						if string.strip(line) in chapter_names:
							chap_name = string.strip(line)
							c.setFont("Gentium Basic Bold", 12)
							c.addOutlineEntry(key=chap_name, level=1, title=chap_name, closed=None)
							c.bookmarkPage(chap_name)
							if VERBOSE > 0:
								print "\t\tFOUND CHAPTER '%s'" % chap_name
						elif string.strip(line) in d.chapter_heads_to_check:
							chap_name = string.strip(line)
							c.setFont("Gentium Basic Bold", 12)
							c.addOutlineEntry(key=chap_name, level=1, title=chap_name, closed=None)
							c.bookmarkPage(chap_name)
							if VERBOSE > 0:
								print "\t\tFOUND CHAPTER '%s'" % chap_name
						elif string.upper(string.strip(line)) in d.chapter_heads_to_check:
							chap_name = string.upper(string.strip(line))
							c.setFont("Gentium Basic Bold", 12)
							c.addOutlineEntry(key=chap_name, level=1, title=chap_name, closed=None)
							c.bookmarkPage(chap_name)
							if VERBOSE > 0:
								print "\t\tFOUND CHAPTER '%s'" % chap_name
						elif string.split(line, " ")[0] == string.split(chapter_dividers, " ")[0]:
							c.setFont("Gentium Basic Bold", 12)
							chap_name = string.strip(line)
							c.addOutlineEntry(key=chap_name, level=1, title=chap_name, closed=None)
							c.bookmarkPage(chap_name)
							if VERBOSE > 0:
								print "\t\tFOUND CHAPTER '%s'" % chap_name
						else:
							c.setFont("Gentium Basic", 12)
						try:
							line=line.decode("utf-8")
							line=line.encode("latin-1","ignore")
						except:
							pass
						c.drawString(xpos, ypos, "%s" % (line))
					else:
						newline = ""
						for word in line.split():
							newline2 = "%s %s" % (newline, word)
							newline2dwidth = stringWidth(newline2, "Gentium Basic Bold", 12, "latin-1")
							if newline2dwidth > (A4[0] - d.leftmargin - d.rightmargin):
								c.drawString(xpos, ypos, "%s" % (newline))
								newline = "%s" % word
								ypos = ypos-16
								if ypos < d.bottommargin:
									c.showPage()
									d.pagenum = d.pagenum + 1
									doFurniture(c,d, "", d.pagenum)
									ypos = A4[1] - d.topmargin
									newline = word
							else:
								newline= newline2
						c.setFont("Gentium Basic", 12)
						c.drawString(xpos, ypos, "%s" % (string.strip(newline)))
						if ypos < d.bottommargin:
							c.showPage()
							d.pagenum = d.pagenum + 1
							doFurniture(c,d, series, d.pagenum)
							ypos = A4[1] - d.topmargin
					##ypos = ypos-16
				

			elif linewidth < (A4[0] - d.leftmargin - d.rightmargin):
				newline = ""
				xpos = d.leftmargin

				if ypos < d.bottommargin:
					c.showPage()
					d.pagenum = d.pagenum + 1
					doFurniture(c,d, "", d.pagenum)
					ypos = A4[1] - d.topmargin

				if string.strip(line) in chapter_names:
					chap_name = string.strip(line)
					c.setFont("Gentium Basic Bold", 12)
					c.addOutlineEntry(key=chap_name, level=1, title=chap_name, closed=None)
					c.bookmarkPage(chap_name)
					if VERBOSE > 0:
						print "\t\tFOUND CHAPTER '%s'" % chap_name

				elif string.strip(line) in d.chapter_heads_to_check:
					chap_name = string.strip(line)
					c.setFont("Gentium Basic Bold", 12)
					c.addOutlineEntry(key=chap_name, level=1, title=chap_name, closed=None)
					c.bookmarkPage(chap_name)
					if VERBOSE > 0:
						print "\t\tFOUND CHAPTER '%s'" % chap_name

				elif string.upper(string.strip(line)) in d.chapter_heads_to_check:
					chap_name = string.upper(string.strip(line))
					c.setFont("Gentium Basic Bold", 12)
					c.addOutlineEntry(key=chap_name, level=1, title=chap_name, closed=None)
					c.bookmarkPage(chap_name)
					if VERBOSE > 0:
						print "\t\tFOUND CHAPTER '%s'" % chap_name

				elif string.split(line, " ")[0] == string.split(chapter_dividers, " ")[0]:
				    c.setFont("Gentium Basic Bold", 12)
				    chap_name = string.strip(line)
				    c.addOutlineEntry(key=chap_name, level=1, title=chap_name, closed=None)
				    c.bookmarkPage(chap_name)
				    if VERBOSE > 0:
						print "\t\tFOUND CHAPTER '%s'" % chap_name
				else:
				    c.setFont("Gentium Basic", 12)

				#c.setFont("Gentium Basic Bold", 12)

				try:
					line=line.decode("utf-8")
					line=line.encode("latin-1","ignore")
				except:
					pass
				c.drawString(xpos, ypos, "%s" % (line))

			else:
				newline = ""
				for word in line.split():
					newline2 = "%s %s" % (newline, word)
					newline2dwidth = stringWidth(newline2, "Gentium Basic Bold", 12, "latin-1")
					if newline2dwidth > (A4[0] - d.leftmargin - d.rightmargin):
						c.drawString(xpos, ypos, "%s" % (newline))
						newline = "%s" % word
						ypos = ypos-16
						if ypos < d.bottommargin:
							c.showPage()
							d.pagenum = d.pagenum + 1
							doFurniture(c,d, "", d.pagenum)
							ypos = A4[1] - d.topmargin
							newline = word
					else:
						newline= newline2

				c.setFont("Gentium Basic", 12)

				c.drawString(xpos, ypos, "%s" % (string.strip(newline)))
				if ypos < d.bottommargin:
					c.showPage()
					d.pagenum = d.pagenum + 1
					doFurniture(c,d, series, d.pagenum)
					ypos = A4[1] - d.topmargin

			ypos = ypos-16

		prevline = line		
	return c


def make_PDF(d, VERBOSE=0):
	if VERBOSE > 0:
		print "\tMaking PDF...\n"
	
	OUTPUTDIR = os.getcwd()

	time_date = time.strftime("%Y%m%d_%H%M%S", time.localtime(time.time()))
	#outfileName = "TEST_%s.pdf" % time_date
	outfileName = "OUTPUT_%s.pdf" % time_date
	text_outfileName = "OUTPUT_TEXTONLY_%s.txt" % time_date
	text_outfile = open(text_outfileName, "w")

	d.outfileName = outfileName
	d.text_outfileName = text_outfileName

	#width, height = letter  #keep for later
	width, height = A4  #keep for later

	c = canvas.Canvas(os.path.join(OUTPUTDIR, outfileName), pagesize=A4)

	c.addOutlineEntry(key="DEMO", level=0, title=d.Document_Title, closed=None)
	c.bookmarkPage("DEMO")

	background_colour=make_covers.pick_colour()
	back = background_colour["RGB Colour"]
	foreground_colour=make_covers.pick_colour()
	fore = foreground_colour["RGB Colour"]

	cover_style = make_covers.get_cover_style()

	if VERBOSE > 0:
		print "\t\tcover_style:", cover_style

	foreground_colour = make_covers.pick_colour()
	background_colour = make_covers.pick_colour()

	if VERBOSE > 0:
		print "\t\tcreating front cover..."
		print "\t\tbackground_colour:", background_colour

	if cover_style == "Type 1":
		back = background_colour["RGB Colour"]
		fore = foreground_colour["RGB Colour"]

	elif cover_style == "Type 2":
		#black(-ish)
		back = (10,10,10)
		background_colour = back

		#white(-ish)
		fore = (240,240,240)
		foreground_colour = fore

	elif cover_style == "Type 3":
		#blue
		back = (56, 104, 140, 1)
		background_colour = back
		#white(-ish)
		fore = (240,240,240)
		foreground_colour = fore

	elif cover_style == "Type 4":
		#black(-ish)
		back = (10,10,10)
		background_colour = back
		#white(-ish)
		fore = (240,240,240)
		foreground_colour = fore


	if VERBOSE > 0:
		print "\t\t\tcreating front cover..."

	c = make_covers.make_front_cover(c, VERBOSE=VERBOSE, outfileName=outfileName,
									 width=A4[0], height=A4[1],
									 author=d.author, bookname=d.Document_Title,
									 blurb=None, background_colour=back,
									 foreground_colour=fore,
									 cover_style=cover_style,
									 book_file=d.dickens_filename)

	c.showPage()

	make_covers.make_text_front_cover(c, VERBOSE=VERBOSE, outfileName=text_outfileName,
									 width=A4[0], height=A4[1],
									 author=d.author, bookname=d.Document_Title,
									 blurb=None, background_colour=back,
									 foreground_colour=fore)


	company_name = doTitles(c,d, VERBOSE)
	d.publisher = company_name

	ISBN = make_covers.make_ISBN(spacer="-")
	d.ISBN = ISBN

	if VERBOSE > 0:
		print "\tGenerating ISBN..."
	ISBN = make_covers.make_ISBN(spacer="-")
	ISBN_for_barcode = string.strip(string.replace(string.replace(ISBN, "-", "")," ", ""))
	if VERBOSE > 0:
		print "\tISBN: '%s'" % ISBN
		print "\tISBN_for_barcode: '%s'" % ISBN_for_barcode
	d.ISBN = ISBN
	d.ISBN_for_barcode = ISBN_for_barcode

	d, front_matter = make_front_matter(publisher=d.publisher,
					  ISBN=ISBN,
					  publication_year=d.publication_year,
					  first_publication_year=d.first_publication_year,
					  d=d)

	if d.edition == "paperback":
		price = random.choice(range(4,9))
	elif d.edition == "hardback":
		price = random.choice(range(10,19))
	else:
		price = random.choice(range(4,15))

	price = "£%s.99" % price
	if VERBOSE > 0:
		print "\tprice: '%s'" % price
		print

	c.setFont("Gentium Basic", 10)

	front_matter_height = len(front_matter.split("\n"))*12

	ypos = (front_matter_height + 24) 

	c.bookmarkPage("FrontMatter", fit="Fit")
	c.addOutlineEntry(key="FrontMatter", level=2, title="Front matter", closed=1)

	textfile = open(outfileName, "a")
	textfile.write("\n\n")

	for line in front_matter.split("\n"):
		textWidth = c.stringWidth(line, "Gentium Basic", 10)
		xpos = (A4[0]/2.0) - (textWidth/2.0)

		c.drawString(xpos, ypos, line)

		ypos = ypos - 12
		textfile.write("%s\n" % line)

	# Do we want to admit we are a program,
	# Or pretent we are a 'real' book...?

	ADMIT_WHO_WE_ARE = 1
	#ADMIT_WHO_WE_ARE = 0

	if ADMIT_WHO_WE_ARE == 1:

		c.setFont("Gentium Basic", 8)

		#PRODUCED BY
		thisprogram = string.split(__file__, os.pathsep)[-1]
		if thisprogram[:2] == ".\\":
			thisprogram = string.strip(thisprogram[2:])
		
		printString = "Actually produced by WHAT THE DICKENS (%s, Version: %s)" % (thisprogram, d.Version)

		textWidth = stringWidth(printString, "Gentium Basic", 8, 'latin-1')

		x = (A4[0]/2.0) - (textWidth/2.0) 
		y = 50 
		c.drawString(x,y,printString)

		GITHUB_URL = "https://github.com/replabjohn/what_the_dickens"

		textWidth = stringWidth(GITHUB_URL, "Gentium Basic", 8, 'latin-1')

		x = (A4[0]/2.0) - (textWidth/2.0) 
		y = y - 10 
		c.drawString(x,y,GITHUB_URL)

		#TIME GENERATED
		printString = "Generation date:  %s" % d.generationtime

		textWidth = stringWidth(printString, "Gentium Basic", 8, 'latin-1')

		x = (A4[0]/2.0) - (textWidth/2.0) 
		y = y - 10 
		c.drawString(x,y,printString)

		c.setFont("Gentium Basic", 14)

	c.showPage()
	d.pagenum = d.pagenum + 1

	seperator = "="*20
	seperator = "\n\n%s\n\n" % (seperator)

	text_outfile.write(seperator)

	make_covers.write_page_to_disk(outfileName=text_outfileName,
								   text = front_matter)

	text_outfile.write(seperator)

	add_text_to_PDF(c, d, VERBOSE)

	make_covers.write_page_to_disk(outfileName=text_outfileName,
								   text=d.text,
								   pagewidth=80, VERBOSE=0)

	#couple of blank pages before the back cover...
	#gives us at least one blank page and makes sure that the cover
	#itself isn't superimposed on top of the last page of text.

	c.showPage()
	d.pagenum = d.pagenum + 1
	c.showPage()
	d.pagenum = d.pagenum + 1

	text_outfile.write(seperator)

	newblurb = blurbwriter.make_content_summary(author=d.author, characters=d.characters,
										   main_character = d.main_character,
										   title = d.Document_Title,
										   dickens_title = d.dickens_book)

	if VERBOSE > 0:
		print "\tcreating back cover..."

	c, blurb = make_covers.make_back_cover(c, VERBOSE=VERBOSE, outfileName=outfileName,
									 width=A4[0], height=A4[1],
									 author=d.author, bookname=d.Document_Title,
									 blurb=newblurb, background_colour=back,
									 foreground_colour=fore, ISBN_text=d.ISBN,
									 ISBN_for_barcode=d.ISBN_for_barcode, price=price, 
									 cover_style=cover_style, dickens_book = d.dickens_book)
	c.save()

	make_covers.make_text_back_cover(c, VERBOSE=VERBOSE, outfileName=text_outfileName,
									 width=A4[0], height=A4[1],
									 author=d.author, bookname=d.Document_Title,
									 blurb=blurb, background_colour=back,
									 foreground_colour=fore,
									 price=price, ISBN=d.ISBN)

	print "\nwrote file '%s'\n\n" % os.path.join(OUTPUTDIR, outfileName)

	return outfileName


def run(VERBOSE=0):

	DEBUG = 0
	#DEBUG = 1
	#DEBUG = 2

	check_for_files(VERBOSE)

	registerFonts(VERBOSE)

	d = DataHolder()

	d, text = make_text(d, VERBOSE)

	if d.text != text:
		print "!!!ERROR!!!"
		sys.exit(-1)
	
	if VERBOSE > 0:
		print "\n\tmaking text 'pretty'..."
	newtext = ""

	#add newlines after paragraph ends
	nt_split = text.split("\n\n")
	for l in range(0, len(nt_split)):
		nt_split[l] = "%s\n" % nt_split[l]

	for ln in nt_split:
		ln = source.index.prettify(ln)
		if DEBUG == 1:
			print ".",
		newtext = "%s\n%s" % (newtext, ln)
		if DEBUG > 1:
			print ln.encode("ascii", "ignore")
	d.text = newtext

	if VERBOSE > 0:
		print "\tText 'prettifying' done OK..."

	outfileName = make_PDF(d, VERBOSE)
	return outfileName


if __name__ == "__main__":
	print "\n'What The Dickens'\n(Version: %s)\n\n" % __VERSION__
	#check_for_files(VERBOSE)

	if "test_intro" in sys.argv:
		print "TESTING INTRO..."
		for f in range(0, 10):
			d= DataHolder()
			intro = make_intro(d, author=None, dickens_book=None, year=None)
			print "\n\n%s\n\n" % (20*"=")
			print intro
	elif "demo_titles" in sys.argv:
		print "TESTING TITLES..."
		demo_titles(num=10)

	else:
		outfileName = run(VERBOSE)
		if os.path.isfile(outfileName):
			#try and open the PDF file... method varies with platform
			#only tested this on Windows, but the others should work...
			#see 'https://stackoverflow.com/questions/1679798/how-to-open-a-file-with-the-standard-application'
			if sys.platform.startswith('win'):
				os.startfile(outfileName)
			elif sys.platform.startswith('linux'):
				subprocess.call(["xdg-open", outfileName])
			else:
				subprocess.Popen(outfileName,shell=True)

			#on windows it works with os.system('start <myFile>').
			#On Mac (it's os.system('open <myFile>')

