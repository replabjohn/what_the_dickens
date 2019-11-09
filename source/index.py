#!/usr/local/bin/python
# -*- coding: UTF-8 -*-

#All text files downloaded from Project Gutenburg
#http://www.gutenberg.org/ebooks/search/?query=Dickens

#Versions are all 'Plain Text UTF-8'


import glob, os, string, io, sys
from types import *


#local version of Maxwell Forbes' Gutenberg utility
#various bits of https://github.com/mbforbes/Gutenberg lumped into one file

#go up a directory and load their version of stripheaders,
#so we don't need to keep two copies of it...

thisdir = os.getcwd()
os.chdir("..")
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
import stripheaders
import names
os.chdir(thisdir)


VERBOSE = 1
VERBOSE = 0


#having these characters in a list we can check agains allows us to
#create a suitably diminutive replacement

little_people = [["Little Em'ly", "Emily"],
				 "Little Em'ly",
				 "Tiny Tim",
				 ["Little Nell", "Nell", "Nell Trent", "Nelly Trent"],
				 "Little Nell"
				 ]


#Dickens has *so* *many* uncommon names not contained in my standard names library!

DICKENS_FEMALE_NAMES = [
	"Betsey", "Biddy", "Clemency", "Clementina", 
	"Lucie", "Maggy", "Sissy", "Sophy", "Sophronia", "Susannab", #!!! Susannab? Looks like a typo,but isn't.
	"Pleasant", "Volumnia", "Nell", "Nelly", "Nettie", "Em'ly",
	"Caddy"
	]

DICKENS_MALE_NAMES = [
	"Abel", "Augustus", "Baytham", "Bentley", "Charley", "Ebenezer",
	"Ham", "Jem", "Job", "Josiah", "Kit", "Sampson", "Nemo",
	"Nicodemus", "Noddy", "Neddy", "Watt", "Wilkins", "Uriah",
	"Leicester", "Serjeant", "Rogue", "Jean-Baptiste", "Dolge", #!!! "Serjeant" is a name, not a rank in this context.
	"Chick", "Tite", "Reuben",
	"Jean-baptiste" # allows for error by using 'string.capwords'
	]


def check_gender(name):
	"""checks name to see if its recognised as male or female.

	returns either "male", "female" or "????".

	(Doesn't allow for ambiguous names like "Chris" which could be
	either male or femals - it just assumes they are male.
	"""

	gender = "????"
	firstname = None

	allnames = names.male_firstnames+names.female_firstnames
	allnames = list(allnames) + DICKENS_FEMALE_NAMES + DICKENS_MALE_NAMES

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
	elif name in little_people:
		if type(name) in (StringType, UnicodeType):
			firstname = string.split(name, " ")[1]
		elif type(name) in (ListType, TupleType):
			for nn in name:
				if len(string.split(nn, " ")) > 1:
					firstname = string.split(nn, " ")[1]
				elif len(string.split(nn, " ")) == 1:
					firstname = string.split(nn, " ")[0]
		
	else:
		pt1, pt2, pt3 = string.split(name, " ", maxsplit=2)
		if pt1 in allnames:
			firstname = pt1
		elif pt2 in allnames:
			firstname = pt2
		elif pt3 in allnames:
			firstname = pt3
	

	#check for the gender...
	if firstname in names.male_firstnames:
		gender = "male"
	elif firstname in names.female_firstnames:
		gender = "female"
	elif firstname in DICKENS_MALE_NAMES:
		gender = "male"
	elif firstname in DICKENS_FEMALE_NAMES:
		gender = "female"

	return gender


index = [
	["98-0.txt",    "A Tale of Two Cities by Charles Dickens"],
	["46-0.txt",    "A Christmas Carol in Prose; Being a Ghost Story of Christmas by Charles Dickens"],
	["1400-0.txt",  "Great Expectations by Charles Dickens"],
	["pg730.txt",   "Oliver Twist by Charles Dickens"],
	["786-0.txt",   "Hard Times by Charles Dickens"],
	["766-0.txt",   "David Copperfield by Charles Dickens"],
	["pg1023.txt",  "Bleak House by Charles Dickens"],
	["pg19337.txt", "A Christmas Carol by Charles Dickens"],
	["1289-0.txt",  "Three Ghost Stories by Charles Dickens"],
	["580-0.txt",   "The Pickwick Papers by Charles Dickens"],
	["700-0.txt",   "The Old Curiosity Shop by Charles Dickens"],
	["883-0.txt",   "Our Mutual Friend by Charles Dickens"],
	["963-0.txt",   "Little Dorrit by Charles Dickens"],
	["967-0.txt",   "Nicholas Nickleby by Charles Dickens"],
	["821-0.txt",   "Dombey and Son by Charles Dickens"],
	#["46675-0.txt", "Oliver Twist; or, The Parish Boy's Progress. Illustrated by Charles Dickens"],
	["46675-0.txt", "Oliver Twist; or, The Parish Boy's Progress by Charles Dickens"],
	["675-0.txt",   "American Notes by Charles Dickens"],
	["564-0.txt",   "The Mystery of Edwin Drood by Charles Dickens"],
	#["882-0.txt",  "Sketches by Boz, Illustrative of Every-Day Life and Every-Day People by Dickens"],
	["882-0.txt",   "Sketches by Boz, Illustrative of Every-Day Life and Every-Day People by Charles Dickens"],
	["968-0.txt",   "Martin Chuzzlewit by Charles Dickens"],
	["pg30368.txt", "A Christmas Carol by Charles Dickens"],
	["pg699.txt",   "A Child's History of England by Charles Dickens"],
	["917-0.txt",   "Barnaby Rudge: A Tale of the Riots of 'Eighty by Charles Dickens"],
	["807-0.txt",   "Hunted Down: The Detective Stories of Charles Dickens by Charles Dickens"],
	["824-0.txt",   "Speeches: Literary and Social by Charles Dickens"],
	["914-0.txt",   "The Uncommercial Traveller by Charles Dickens"],
	["644-0.txt",   "The Haunted Man and the Ghost's Bargain by Charles Dickens"],
	["47529-0.txt", "Oliver Twist, Vol. 1 (of 3) by Charles Dickens"],
	["653-0.txt",   "The Chimes by Charles Dickens"],
	["678-0.txt",   "The Cricket on the Hearth: A Fairy Tale of Home by Charles Dickens"],
	["27924-0.txt", "Mugby Junction by Charles Dickens"],
	["pg23344.txt", "The Magic Fishbone by Charles Dickens"],
	["650-0.txt",   "Pictures from Italy by Charles Dickens"],
	["872-0.txt",   "Reprinted Pieces by Charles Dickens"],
	["pg43111.txt", "The Personal History of David Copperfield by Charles Dickens"],
	["1467-0.txt",  "Some Christmas Stories by Charles Dickens"],
	["676-0.txt",   "The Battle of Life by Charles Dickens"],
	["pg1415.txt",  "Doctor Marigold by Charles Dickens"],
	["810-0.txt",   "George Silverman's Explanation by Charles Dickens"],
	["pg1407.txt",  "A Message from the Sea by Charles Dickens"],
	["pg47534.txt", "The Posthumous Papers of the Pickwick Club, v. 1 (of 2) by Charles Dickens"],
	["809-0.txt",   "Holiday Romance by Charles Dickens"],
	["pg1465.txt",  "The Wreck of the Golden Mary by Charles Dickens"],
	["912-0.txt",   "Mudfog and Other Sketches by Charles Dickens"],
	["47530-0.txt", "Oliver Twist, Vol. 2 (of 3) by Charles Dickens"],
	["47531-0.txt", "Oliver Twist, Vol. 3 (of 3) by Charles Dickens"],
	["922-0.txt",   "Sunday Under Three Heads by Charles Dickens"],
	["pg1392.txt",  "The Seven Poor Travellers by Charles Dickens"],
	["pg1414.txt",  "Somebody's Luggage by Charles Dickens"],
	["pg47535.txt", "The Posthumous Papers of the Pickwick Club, v. 2 (of 2) by Charles Dickens"],
	["916-0.txt",   "Sketches of Young Couples by Charles Dickens"],
	["927-0.txt",   "The Lamplighter by Charles Dickens"],
	["pg23765.txt", "Captain Boldheart & the Latin-Grammar Master by Charles Dickens"],
	["pg37581.txt", "The Cricket on the Hearth: A Fairy Tale of Home by Charles Dickens"],
	["pg37121.txt", "Charles Dickens' Children Stories by Charles Dickens"],
	["pg1394.txt",  "The Holly-Tree by Charles Dickens"],
	["42232-0.txt", "A Child's Dream of a Star by Charles Dickens"],
	["pg23452.txt", "The Trial of William Tinkling by Charles Dickens"],
	["pg1413.txt",  "Tom Tiddler's Ground by Charles Dickens"],
#   ["", ""],
#   ["", ""],
	["pg30127.txt", "Tales from Dickens by Charles Dickens"]
	]


def stupify(text):
	"""Converts UTF-8 characters to ascii characters.
	Converts 'smart quotes' to 'dumb quotes' etc."""
	try:
		text = text.decode('utf-8', 'ignore')
	except:
		text = text.encode('utf-8', 'ignore')

##    text = string.replace(text, "--".encode("utf-8", "ignore"), " - ".encode("utf-8", "ignore"))
##    text = string.replace(text, u" \u2013 ".encode("utf-8", "ignore"), u" - ".encode("utf-8", "ignore")) #'EN DASH' (U+2013)
##    text = string.replace(text, u"\u2026 ".encode("utf-8", "ignore"), u"... ".encode("utf-8", "ignore")) #(U+2026) Horizontal Ellipsis  “…”
##    text = string.replace(text, u"\u2019".encode("utf-8", "ignore"), u"'".encode("utf-8", "ignore")) #'RIGHT SINGLE QUOTATION MARK' (U+2019)
##    text = string.replace(text, u"\u2018".encode("utf-8", "ignore"), u"'".encode("utf-8", "ignore")) #'LEFT SINGLE QUOTATION MARK' (U+2018)
##    text = string.replace(text, u"\u201c".encode("utf-8", "ignore"), u'"'.encode("utf-8", "ignore")) #U+201C  “   Left double quotation mark
##    text = string.replace(text, u"\u201d".encode("utf-8", "ignore"), u'"'.encode("utf-8", "ignore")) #U+201D  ”   Right double quotation mark


	text = string.replace(text, "--".encode("utf-8", "ignore"), " - ".encode("ascii", "ignore"))
	try:
		text = string.replace(text, u" \u2013 ".encode("utf-8", "ignore"), u" - ".encode("ascii", "ignore")) #'EN DASH' (U+2013)
	except:
		foundline = " \\u2013 "
		print "FAILED ON '%s'" % foundline

	try:
		text = string.replace(text, u"\u2026 ".encode("utf-8", "ignore"), u"... ".encode("ascii", "ignore")) #(U+2026) Horizontal Ellipsis  “…”
	except:
		foundline = " \\u2026 "
		print "FAILED ON '%s'" % foundline

	try:
		text = string.replace(text, u"\u2019".encode("utf-8", "ignore"), u"'".encode("ascii", "ignore")) #'RIGHT SINGLE QUOTATION MARK' (U+2019)
	except:
		foundline = " \\u2019 "
		print "FAILED ON '%s'" % foundline

	try:
		text = string.replace(text, u"\u2018".encode("utf-8", "ignore"), u"'".encode("ascii", "ignore")) #'LEFT SINGLE QUOTATION MARK' (U+2018)
	except:
		foundline = " \\u2018 "
		print "FAILED ON '%s'" % foundline

	try:
		text = string.replace(text, u"\u201c".encode("utf-8", "ignore"), u'"'.encode("ascii", "ignore")) #U+201C    “   Left double quotation mark
	except:
		foundline = " \\u201c "
		print "FAILED ON '%s'" % foundline

	try:
		text = string.replace(text, u"\u201d".encode("utf-8", "ignore"), u'"'.encode("ascii", "ignore")) #U+201D    ”   Right double quotation mark
	except:
		foundline = " \\u201d "
		print "FAILED ON '%s'" % foundline

	return text


def prettify(text):
	"""Converts ascii characters to UTF-8 characters to make typographically 'prettier'"""

	newtext = ""

	try:
		text = string.replace(text, " - ", u" \u2013 ") #'EN DASH' (U+2013)
		text = string.replace(text, "... ", u"\u2026 ") #(U+2026) Horizontal Ellipsis  “…”
		#assume they're all right single quotes...
		text = string.replace(text, "'", u"\u2019") #'RIGHT SINGLE QUOTATION MARK' (U+2019)
		newtext = ""
		inquotes = 0
		for chr in text:
			if chr == '"':
				if inquotes == 0:
					chr = u"\u201c" #U+201C “   Left double quotation mark
					inquotes = 1
				elif inquotes == 1:
					chr = u"\u201d" #U+201D ”   Right double quotation mark
					inquotes = 0
			newtext = "%s%s" % (newtext,chr)
	except:
		print "*** ERROR WITH text '%s' ***" % text
	if newtext == "":
		return text
	else:
		return newtext


characters_dict = {
	"98-0.txt":         {"filename":    "98-0.txt",
						 "title":       "A Tale of Two Cities by Charles Dickens",
						 "characters":
										#from Sparknotes - Literature - A Tale of Two Cities - CHARACTER LIST
										#https://www.sparknotes.com/lit/twocities/characters/
										["Charles Darnay",
										"Sydney Carton",
										"Doctor Manette",
										"Lucie Manette",
										"Monsieur Defarge",
										"Madame Defarge",
										"Jarvis Lorry",
										"Jerry Cruncher",
										"Miss Pross",
										"Marquis Evrémonde",
										"Mr. Stryver",
										"John Barsad",
										"Roger Cly",
										"Gabelle"],
						 "chapter dividers":    None,
						 "chapter names":   ["I. The Period",
											 "II. The Mail",
											 "III. The Night Shadows",
											 "IV. The Preparation",
											 "V. The Wine-shop",
											 "VI. The Shoemaker",
											 "I. Five Years Later",
											 "II. A Sight",
											 "III. A Disappointment",
											 "IV. Congratulatory",
											 "V. The Jackal",
											 "VI. Hundreds of People",
											 "VII. Monseigneur in Town",
											 "VIII. Monseigneur in the Country",
											 "IX. The Gorgon's Head",
											 "X. Two Promises",
											 "XI. A Companion Picture",
											 "XII. The Fellow of Delicacy",
											 "XIII. The Fellow of no Delicacy",
											 "XIV. The Honest Tradesman",
											 "XV. Knitting",
											 "XVI. Still Knitting",
											 "XVII. One Night",
											 "XVIII. Nine Days",
											 "XIX. An Opinion",
											 "XX. A Plea",
											 "XXI. Echoing Footsteps",
											 "XXII. The Sea Still Rises",
											 "XXIII. Fire Rises",
											 "XXIV. Drawn to the Loadstone Rock",
											 "I. In Secret",
											 "II. The Grindstone",
											 "III. The Shadow",
											 "IV. Calm in Storm",
											 "V. The Wood-sawyer",
											 "VI. Triumph",
											 "VII. A Knock at the Door",
											 "VIII. A Hand at Cards",
											 "IX. The Game Made",
											 "X. The Substance of the Shadow",
											 "XI. Dusk",
											 "XII. Darkness",
											 "XIII. Fifty-two",
											 "XIV. The Knitting Done",
											 "XV. The Footsteps Die Out For Ever",
											 ],
						 "garbage to delete":   [],
						 "main character":    None,
						 },

	"46-0.txt":         {"filename":    "46-0.txt",
						 #"title":       "A Christmas Carol in Prose; Being a Ghost Story of Christmas by Charles Dickens",
						 "title":       "A Christmas Carol by Charles Dickens",
						 "characters":
										#from Sparknotes - Literature - A Christmas Carol - CHARACTERS
										#https://www.sparknotes.com/lit/christmascarol/characters/
										["Ebenezer Scrooge",
										"Bob Cratchit",
										"Tiny Tim",
										"Jacob Marley",
										"The Ghost Of Christmas Past",
										"The Ghost Of Christmas Present",
										"The Ghost Of Christmas Yet To Come",
										"Fred",
										"Fezziwig",
										"Belle",
										"Peter Cratchit",
										"Martha Cratchit",
										"Fan",
										"The Portly Gentlemen",
										"Mrs. Cratchit"],
						 "chapter dividers":    "Stave ",
						 "chapter names":       None,
						 "garbage to delete":   ["""IN PROSE
BEING
A Ghost Story of Christmas

""",
												 """PREFACE

I HAVE endeavoured in this Ghostly little book,
to raise the Ghost of an Idea, which shall not put my
readers out of humour with themselves, with each other,
with the season, or with me.  May it haunt their houses
pleasantly, and no one wish to lay it.

Their faithful Friend and Servant,
								   C. D.
December, 1843.
"""],
						 "main character":    "Ebenezer Scrooge",
						 },

	"1400-0.txt":       {"filename":    "1400-0.txt",
						 "title":       "Great Expectations by Charles Dickens",
						 "characters":
										#from Sparknotes - Literature - Great Expectations - CHARACTER LIST
										#https://www.sparknotes.com/lit/greatex/characters/
										[["Pip", "Philip Pirrip"],
										"Estella",
										"Miss Havisham",
#                                        "Abel Magwitch (“The Convict”)",
										["Abel Magwitch","The Convict"],
										"Joe Gargery",
										"Jaggers",
										"Herbert Pocket",
										"Wemmick",
										"Biddy",
										"Dolge Orlick",
										"Mrs. Joe",
										"Uncle Pumblechook",
										"Compeyson",
										"Bentley Drummle",
										"Molly",
										"Mr. Wopsle",
										"Startop",
										"Miss Skiffins",
										#additional
										["Georgiana",   "Georgiana Pirrip"],
										["Alexander",   "Alexander Pirrip"],
										["Bartholomew", "Bartholomew Pirrip"],
										["Abraham",     "Abraham Pirrip"]
										 ],
						 "chapter dividers":    None,
						 "chapter names":       None,
						 "garbage to delete":   ["[1867 Edition]\n",
												 "[Project Gutenberg Editor's Note: There is also another version of",
												 "this work etext98/grexp10.txt scanned from a different edition]",
												 "[Project Gutenberg Editor's Note: [CHARACTER_004_FIRSTNAME]re is also another version of",
												 "this work etext98/grexp10.txt scanned from a different edition]",
												 ],
						 "main character":    "Philip Pirrip",
						 },


	"pg730.txt":        {"filename":    "pg730.txt",
						 "title":       "Oliver Twist by Charles Dickens",
						 "characters":
										#Charles Dickens Info - Characters In Oliver Twist
										#https://www.charlesdickensinfo.com/novels/oliver-twist/whos-who/
										[["Artful Dodger", "Jack Dawkins"],
										#2Bull's-Eye", Bill Sikes’s dog,
										"Charley Bates",
										"Mr. Brownlow",
										"Mr. Bumble",
										"Oliver Twist",
										"Noah Claypole",
										"Toby Crackit",
										"Edward Leeford",
										"Monks",
										"Fagin",
										"Agnes Fleming",
										"Mr. Gamfield",
										"Mr. Giles",
										"Mr. Grimwig",
										"Mr. Losberne",
										"Mrs. Mann",
										"Mrs. Maylie",
										"Harry Maylie",
										"Miss Rose Maylie",
										"Rose Maylie",
										"Edward Leeford",
										"Nancy",
										"Bill Sikes",
										"Mr. Sowerberry",
										 #minor characters
										 "Mr. Limbkins"],
						 "chapter dividers":    "CHAPTER ",
						 "chapter names":       None,
						 "garbage to delete":   ["""OR

THE PARISH BOY'S PROGRESS

"""],
						 "main character":    "Oliver Twist",
						 },

	"786-0.txt":        {"filename":    "786-0.txt",
						 "title":       "Hard Times by Charles Dickens",
						 "characters":
										#Sparknotes - Literature  Hard Times  CHARACTER LIST
										#https://www.sparknotes.com/lit/hardtimes/characters/
										["Thomas Gradgrind",
										"Louisa Gradgrind",
										"Thomas Gradgrind, Jr",
										["Josiah Bounderby", "Mr. Bounderby"],
										["Cecelia Jupe", "Sissy Jupe"],
										"Mrs. Sparsit",
										"Stephen Blackpool",
										"Rachael",
										"James Harthouse",
										"Mr. Sleary",
										"Bitzer",
										["Mr. McChoakumchild", "Mr. M'Choakumchild"],
										"Mrs. Pegler",
										"Mrs. Gradgrind",
										"Slackbridge",
										"Jane Gradgrind"],
						 "chapter dividers":    "CHAPTER ",
						 "chapter names":       None,
						 "garbage to delete":   ["Transcribed from the 1905 Chapman and Hall edition by David Price, email",
												 "ccx074@pglaf.org",
												 "_With illustrations by Marcus Stone_, _Maurice_",
												 "_Greiffenhagen_, _and F. Walker_",
												 "FOOTNOTES",
												 "{0}  _Reprinted Pieces_ was released as a separate eText by Project",
												 "Gutenberg, and is not included in this eText.",

												 "LONDON: CHAPMAN & HALL, LD.",
												 "NEW YORK: CHARLES SCRIBNER'S SONS",
												 "1905",
												 "AND\n                           REPRINTED PIECES {0}",
												 "[Picture: Stephen and Rachael in the sick room]",
												 "[Picture: Mr. Harthouse dines at the Bounderby's]",
												 "[Picture: Mr. Harthouse dines at the Bounderby’s]",
												 "[Picture: Mr. Harthouse and Tom Gradgrind in the garden]",
												 "[Picture: Stephen Blackpool recovered from the Old Hell Shaft]"
												 ],
						 "main character":    None,
						 },


	"766-0.txt":        {"filename":    "766-0.txt",
						 "title":       "David Copperfield by Charles Dickens",
						 "characters":
										#Charles Dickens Info - Characters in David Copperfield
										#https://www.charlesdickensinfo.com/novels/david-copperfield/whos-who/
									   [
									   ["Richard Babley", "Mr. Dick"],
									   "Barkis",
									   "Clara Copperfield",
									   "David Copperfield",
									   "Mr. Creakle",
									   #["Little Em’ly", "Emily"],
									   ["Little Em'ly", "Emily"],
									   "Mrs. Grummidge",
									   "Uriah Heep",
									   "Littimer",
									   "Wilkins Micawber",
									   "Edward Murdstone",
									   "Jane Murdstone",
									   "Clara Peggotty",
									   "Daniel Peggotty",
									   "Ham Peggotty",
									   "Dora Spenlow",
									   "James Steerforth",
									   "Dr. Strong",
									   "Tommy Traddles",
									   "Betsey Trotwood",
									   "Agnes Wickfield",
									   "Mr. Wickfield"],
						 "chapter dividers":    "CHAPTER ",
						 "chapter names":       None,
						 "garbage to delete":   ["""               AFFECTIONATELY INSCRIBED TO
			   THE HON.  Mr. AND Mrs. RICHARD WATSON,
			   OF ROCKINGHAM, NORTHAMPTONSHIRE.
""",
												 """PREFACE TO 1850 EDITION


I do not find it easy to get sufficiently far away from this Book, in
the first sensations of having finished it, to refer to it with the
composure which this formal heading would seem to require. My interest
in it, is so recent and strong; and my mind is so divided between
pleasure and regret - pleasure in the achievement of a long design,
regret in the separation from many companions - that I am in danger of
wearying the reader whom I love, with personal confidences, and private
emotions.

Besides which, all that I could say of the Story, to any purpose, I have
endeavoured to say in it.

It would concern the reader little, perhaps, to know, how sorrowfully
the pen is laid down at the close of a two-years' imaginative task; or
how an Author feels as if he were dismissing some portion of himself
into the shadowy world, when a crowd of the creatures of his brain
are going from him for ever. Yet, I have nothing else to tell; unless,
indeed, I were to confess (which might be of less moment still) that no
one can ever believe this Narrative, in the reading, more than I have
believed it in the writing.

Instead of looking back, therefore, I will look forward. I cannot close
this Volume more agreeably to myself, than with a hopeful glance towards
the time when I shall again put forth my two green leaves once a month,
and with a faithful remembrance of the genial sun and showers that have
fallen on these leaves of [BOOK_SHORT_TITLE], and made me happy.

	 London, October, 1850.
""",
												 """PREFACE TO THE CHARLES DICKENS EDITION


I REMARKED in the original Preface to this Book, that I did not find it
easy to get sufficiently far away from it, in the first sensations of
having finished it, to refer to it with the composure which this formal
heading would seem to require. My interest in it was so recent and
strong, and my mind was so divided between pleasure and regret - pleasure
in the achievement of a long design, regret in the separation from many
companions - that I was in danger of wearying the reader with personal
confidences and private emotions.

Besides which, all that I could have said of the Story to any purpose, I
had endeavoured to say in it.

It would concern the reader little, perhaps, to know how sorrowfully the
pen is laid down at the close of a two-years' imaginative task; or how
an Author feels as if he were dismissing some portion of himself into
the shadowy world, when a crowd of the creatures of his brain are going
from him for ever. Yet, I had nothing else to tell; unless, indeed, I
were to confess (which might be of less moment still), that no one can
ever believe this Narrative, in the reading, more than I believed it in
the writing.

So true are these avowals at the present day, that I can now only take
the reader into one confidence more. Of all my books, I like this the
best. It will be easily believed that I am a fond parent to every child
of my fancy, and that no one can ever love that family as dearly as I
love them. But, like many fond parents, I have in my heart of hearts a
favourite child. And his name is

[BOOK_SHORT_TITLE_CAPS].

	 1869
"""],
						 "main character":    "David Copperfield",
						 },

	"pg1023.txt":       {"filename":    "pg1023.txt",
						 "title":       "Bleak House by Charles Dickens",
						 "characters":
										#from Sparknotes - Literature - Bleak House - CHARACTER LIST
										#https://www.sparknotes.com/lit/bleakhouse/characters/
										["Esther Summerson",
										["Mr. John Jarndyce", "John Jarndyce", "Mr. Jarndyce"],
										"Ada Clare",
										"Richard Carstone",
										"Lady Dedlock",
										["Sir Leicester Dedlock", "Leicester Dedlock"],
										"Mr. Tulkinghorn",
										["Mrs. Baytham Badger", "Mrs. Badger", "Baytham Badger"],
										"Mr. Badger",
										["Mr. Matthew Bagnet", "Mr. Bagnet", "Matthew Bagnet"],
										"Mrs. Bagnet",
										"Malta Bagnet",
										"Quebec Bagnet",
										"Woolwich Bagnet",
										"Miss Barbary",
										"Inspector Bucket",
										["Mr. Lawrence Boythorn", "Mr. Boythorn", "Lawrence Boythorn"],
										"Mr. Chadband",
										["Mrs. Rachael Chadband", "Mrs. Chadband", "Rachael Chadband"],
										"Volumnia Dedlock",
										"Miss Flite",
										"Mr. Gridley",
										["Mr. William Guppy", "Mr. Guppy", "William Guppy"],
										"Guster",
										#"Captain Hawdon (Nemo)",
										["Captain Hawdon", "Captain Nemo Hawdon", "Nemo Hawdon"],
										"Mademoiselle Hortense",
										"Mrs. Jellyby",
										"Mr. Jellyby",
										#"Caroline (Caddy) Jellyby",
										["Caroline Jellyby", "Caddy Jellyby"],
										"Peepy Jellyby",
										"Jenny",
										["Jo", "Toughey"],
										#"Mr. Tony Jobling (Mr. Weevle)",
										"Mr. Tony Jobling",
										"Mr. Weevle",
										"Mr. Krook",
										"Liz",
										#"Charlotte (Charley) Neckett",
										["Charlotte Neckett", "Charley Neckett"],
										"Mrs. Pardiggle",
										"Rosa",
										["Mr. George Rouncewell", "Mr. Rouncewell", "George Rouncewell"],
										"Mrs. Rouncewell",
										["Mr. Watt Rouncewell","Mr. Rouncewell", "Watt Rouncewell"],
										"Harold Skimpole",
										#"Bartholomew (Chick) Smallweed",
										["Bartholomew Smallweed", "Chick Smallweed"],
										"Judy Smallweed",
										"Grandfather Smallweed",
										"Grandmother Smallweed",
										"Mr. Snagsby",
										"Mrs. Snagsby",
										"Phil Squod",
										"Mr. Turveydrop",
										"Prince Turveydrop",
										"Mr. Vholes",
										"Allan Woodcourt",
										"Mrs. Woodcourt"],
						 "chapter dividers":    "CHAPTER ",
						 "chapter names":       None,
						 "garbage to delete":   ["Transcriber's note. This referred to a specific page in",
												 "the printed book. In this Project Gutenberg edition the",
												 "pertinent information is in Chapter XXX, paragraph 90.",
												 "** Another case, very clearly described by a dentist,",
												 "occurred at the town of Columbus, in the United States",
												 "of America, quite recently. The subject was a German who",
												 "kept a liquor-shop and was an inveterate drunkard."],
						 "main character":    None,
						 },



	"pg19337.txt":      {"filename":    "pg19337.txt",
						 "title":       "A Christmas Carol by Charles Dickens",
						 "characters":
										#from Sparknotes - Literature - A Christmas Carol - CHARACTERS
										#https://www.sparknotes.com/lit/christmascarol/characters/
										["Ebenezer Scrooge",
										"Bob Cratchit",
										"Tiny Tim",
										"Jacob Marley",
										"The Ghost Of Christmas Past",
										"The Ghost Of Christmas Present",
										"The Ghost Of Christmas Yet To Come",
										"Fred",
										"Fezziwig",
										"Belle",
										"Peter Cratchit",
										"Martha Cratchit",
										"Fan",
										"The Portly Gentlemen",
										"Mrs. Cratchit"],
						 "chapter dividers":    "STAVE ",
						 "chapter names":       None,
						 "garbage to delete":   ["""ILLUSTRATED BY
GEORGE AL[CHARACTER_NAME_CAPS_008] WILLIAMS""",
												 """ILLUSTRATED BY
GEORGE ALTREY WILLIAMS""",
												 """New York\nTHE PLATT & PECK CO.""",
												 """_Copyright, 1905, by_ THE BAKER & TAYLOR COMPANY""",
												 """[Illustration: "He had been [CHARACTER_003_SURNAME]'s blood horse all the way from church."]""",
												 """INTRODUCTION


The combined qualities of the realist and the idealist which Dickens
possessed to a remarkable degree, together with his naturally jovial
attitude toward life in general, seem to have given him a remarkably
happy feeling toward Christmas, though the privations and hardships of
his boyhood could have allowed him but little real experience with this
day of days.

Dickens gave his first formal expression to his Christmas thoughts in
his series of small books, the first of which was the famous "Christmas
Carol," the one perfect chrysolite. The success of the book was
immediate. Thackeray wrote of it: "Who can listen to objections
regarding such a book as this? It seems to me a national benefit, and to
every man or woman who reads it, a personal kindness."

This volume was put forth in a very attractive manner, with
illustrations by John Leech, who was the first artist to make these
characters live, and his drawings were varied and spirited.

There followed upon this four others: "The Chimes," "The Cricket on the
Hearth," "The Battle of Life," and "The Haunted Man," with illustrations
on their first appearance by Doyle, Maclise, and others. The five are
known to-day as the "Christmas Books." Of them all the "Carol" is the
best known and loved, and "The Cricket on the Hearth," although third in
the series, is perhaps next in point of popularity, and is especially
familiar to Americans through Joseph Jefferson's characterisation of
Caleb Plummer.

Dickens seems to have put his whole self into these glowing little
stories. Whoever sees but a clever ghost story in the "Christmas Carol"
misses its chief charm and lesson, for there is a different meaning in
the movements of [CHARACTER_001_SURNAME] and his attendant spirits. A new life is
brought to [CHARACTER_001_SURNAME] when he, "running to his window, opened it and put
out his head. No fog, no mist; clear, bright, jovial, stirring cold;
cold, piping for the blood to dance to; Golden sun-light; Heavenly sky;
sweet fresh air; merry bells. Oh, glorious! Glorious!" All this
brightness has its attendant shadow, and deep from the childish heart
comes that true note of pathos, the ever memorable toast of [CHARACTER_NAME_003],
"God bless Us, Every One!" "The Cricket on the Hearth" strikes a
different note. Charmingly, poetically, the sweet chirping of the little
cricket is associated with human feelings and actions, and at the crisis
of the story decides the fate and fortune of the carrier and his wife.

Dickens's greatest gift was characterization, and no English writer,
save Shakespeare, has drawn so many and so varied characters. It would
be as absurd to interpret all of these as caricatures as to deny Dickens
his great and varied powers of creation. Dickens exaggerated many of his
comic and satirical characters, as was his right, for caricature and
satire are very closely related, while exaggeration is the very essence
of comedy. But there remains a host of characters marked by humour and
pathos. Yet the pictorial presentation of Dickens's characters has ever
tended toward the grotesque. The interpretations in this volume aim to
eliminate the grosser phases of the caricature in favour of the more
human. If the interpretations seem novel, if [CHARACTER_001_SURNAME] be not as he has
been pictured, it is because a more human [CHARACTER_001_SURNAME] was desired - a [CHARACTER_001_SURNAME]
not wholly bad, a [CHARACTER_001_SURNAME] of a better heart, a [CHARACTER_001_SURNAME] to whom the
resurrection described in this story was possible. It has been the
illustrator's whole aim to make these people live in some form more
fully consistent with their types.

								   GEORGE AL[CHARACTER_NAME_CAPS_008] WILLIAMS.
_Chatham, N.J._
"""],
						 "main character":    "Ebenezer Scrooge",
						 },

	"580-0.txt":      {"filename":    "580-0.txt",
						 "title":       "The Pickwick Papers by Charles Dickens",
						 "characters":
										#CliffsNotes - Literature  - Notes - The Pickwick Papers - Character List
										#https://www.cliffsnotes.com/literature/p/the-pickwick-papers/character-list
										[
										["Samuel Pickwick", "Mr. Pickwick"],
										"Tracy Tupman",
										"Augustus Snodgrass",
										"Nathaniel Winkle",
										"Mr. Blotton",
										"Alfred Jingle",
										"Dr. Slammer",
										"Lieutenant Tappleton",
										"Dr. Payne",
										["Jem Hutley", "Dismal Jemmy"],
										"Colonel Bulder",
										"Mrs. Bulder",
										["Sir Thomas Clubber", "Thomas Clubber"],
										"Mr. Wardle",
										"Emily Wardle",
										"Isabella Wardle",
										"Rachael Wardle",
										"Mrs. Wardle",
										"Joe the Fat Boy",
										"Mr. Trundle",
										"An old clergyman",
										"Mr. Miller",
										"Sam Weller",
										"Mr. Perker",
										["Mrs. Martha Bardell", "Martha Bardell", "Mrs. Bardell"],
										["Master Tommy Bardell", "Tommy Bardell", "Master Bardell"],
										"Mr. Pott",
										"Mrs. Pott",
										"Mr. Slurk",
										["The Hon. Samuel Slumkey", "Samuel Slumkey"],
										["The Hon. Horatio Fizkin", "Horatio Fizkin"],
										"The one-eyed bagman",
										["Mrs. Leo Hunter", "Mrs. Hunter"],
										["Mr. Leo Hunter", "Leo Hunter", "Mr. Hunter"],
										"Count Smorltork",
										"Job Trotter",
										"Miss Tomkins",
										"Captain Boldwig",
										"Peter Lowten",
										#"Dodson and Fogg",
										"Dodson",
										"Fogg",
										"Mr. Jackson",
										"Jack Bamber",
										"Peter Magnus",
										"Miss Witherfield",
										"George Nupkins",
										"Mrs. Nupkins",
										["Miss Henrietta Nupkins", "Henrietta Nupkins","Miss Nupkins"],
										"Daniel Grummer",
										"Mr. Dubbley",
										"Mr. Jinks",
										"Mr. Muzzle",
										"Tony Weller",
										"Susan Weller",
										"The Reverend Stiggins",
										"Anthony Humm",
										["Mrs. Betsy Cluppins", "Betsy Cluppins", "Mrs. Cluppins"],
										["Mrs. Susannab Sanders", "Susannab Sanders", "Mrs. Sanders"],
										"Arabella Allen",
										"Ben Allen",
										"Bob Sawyer",
										"Jack Hopkins",
										["Mrs. Mary Ann Raddle", "Mary Ann Raddle", "Mrs. Raddle"],
										"Mr. Raddle",
										"Serjeant Snubbin",
										"Mr. Mallard",
										"Mr. Phunky",
										"Serjeant Buzfuz",
										"Mr. Justice Stareleigh",
										"Colonel Dowler",
										"Mrs. Dowler",
										"Mrs. Craddock",
										"Angelo Cyrus Bantam",
										"John Smauker",
										"Mrs. Wugsby",
										"Lady Snuphanuph",
										"Mary",
										"A scientific gentleman",
										["Mr. Tom Roker", "Tom Roker", "Mr. Roker"],
										"Neddy",
										"The Chancery prisoner",
										"Mr. Smangle",
										#"Mr. Mivins (The Zephyr",
										"Mr. Mivins",
										"The Zephyr",
										["Mr. Solomon Pell", "Solomon Pell", "Mr. Pell"],
										#"Arabella Allen's aunt",
										"Mr. Martin",
										"Mr. Winkle, Sr.",
										"Wilkins Flasher",
										"Philip Strother",
										"Wade Grove",
                                        #additional minor characters
                                        "Joseph Smiggers"],
						 "chapter dividers":    "CHAPTER ",
						 "chapter names":       None,
						 "garbage to delete":   ["Produced by Jo Churcher, and David Widger"],
						 "main character":    "Samuel Pickwick",
						 },

	"700-0.txt":        {"filename":    "700-0.txt",
						 "title":       "The Old Curiosity Shop by Charles Dickens",
						 "characters":
										#from Charles Dickens Info - Characters in The Old Curiosity Shop
										#https://www.charlesdickensinfo.com/novels/old-curiosity-shop/whos-who/
										["Sally Brass",
										 "Sampson Brass",
										 "Grandfather",
										 "Mrs. Jarley",
										 "The Marchioness",
										 "Kit Nubbles",
										 ["Daniel Quilp", "Quilp"],
										 "The Single Gentleman",
										"Dick Swiveller",
										"Fred Trent",
										["Little Nell", "Nell", "Nell Trent", "Nelly Trent"],
										 ],
						 "chapter dividers":    "CHAPTER ",
						 "chapter names":       None,
						 "garbage to delete":   [],
						 "main character":    None,
						 },

	"883-0.txt":        {"filename":    "883-0.txt",
						 "title":       "Our Mutual Friend by Charles Dickens",
						 "characters":
										#from GradeSaver - Study Guides - Our Mutual Friend - Character List
										#https://www.gradesaver.com/our-mutual-friend/study-guide/character-list
										["Lizzie Hexam",
										"Eugene Wrayburn",
										"John Harmon", "John Rokesmith", "Julius Handford",
										"Silas Wegg",
										["Noddy Boffin", "Nicodemus Boffin"],
										"Mrs. Boffin",
										"Bella Wilfer",
										"Charley Hexam",
										"Mortimer Lightwood",
										"Jenny Wren",
										"Mr. Riah",
										"Bradley Headstone",
										"Mr. Venus",
										["Mr. Alfred Lammle", "Alfred Lammle", "Mr. Lammle"],
										["Mrs. Sophronia Lammle", "Sophronia Lammle", "Mrs. Lammle"],
										"Georgiana Podsnap",
										"Fledgeby",
										"Rogue Riderhood",
										"Mr. Wilfer",
										"Mr. Inspector",
										#"Mr. and Mrs. Podsnap",
										"Mr. Podsnap",
										"Mrs. Podsnap",
										"Mrs. Wilfer",
										"Lavinia Wilfer",
										"George Sampson",
										"Twemlow",
										"Betty Higden",
										"Johnny",
										"Sloppy",
										"Gaffer Hexam",
										"Pleasant Riderhood",
										#"Mr. and Mrs. Veneering",
										"Mr. Veneering",
										"Mrs. Veneering",
										"Miss Peecher",
										"George Radfoot"],
						 "chapter dividers":    "Chapter ",
						 "chapter names":       None,
						 "garbage to delete":   [],
						 "main character":    None,
						 },


#   ["963-0.txt",   "Little Dorrit by Charles Dickens"],
	"963-0.txt":        {"filename":    "963-0.txt",
						 "title":       "Little Dorrit by Charles Dickens",
						 "characters":
										#from GradeSaver - Study Guides - Little Dorrit - Character List
										#https://www.gradesaver.com/little-dorrit/study-guide/character-list
										[
										['Amy "Little" Dorrit', "Little Dorrit", "Amy Dorrit"],
										["Mr. William Dorrit", "William Dorrit", "Mr. Dorrit"], 
										"Arthur Clennam",
										"Fanny Dorrit",
										"Daniel Doyce",
										"Mr. Merdle",
										"Mrs. Merdle",
										["Mr. Nandy", "Old Nandy"],
										"Edmund Sparkler",
										"Mr. Chivery",
										"Mrs. Chivery",
										"Flora Casby Finching",
										"Flintwinch",
										#"Monsieur Rigaud/Blandois/Lagnier",
										["Monsieur Rigaud", "Blandois", "Lagnier"],
										"Mrs. Clennam",
										"Affery",
										"Pet Meagles",
										["Jean-Baptiste Cavalletto", "Mr. Baptist"],
										"Tattycoram",
										"Mrs. General",
										"Mrs. Gowan",
										"Henry Gowan",
										"Miss Wade",
										"Mr. Casby",
										"Pancks",
										#"Mr. and Mrs. Plornish",
										"Mr. Plornish",
										"Mrs. Plornish",
										"John Chivery",
										"Tite Barnacle",
										"Maggy",
										"Mr. Rugg",
										"Miss Rugg",
										"Clarence Barnacle"],
						 "chapter dividers":    "CHAPTER ",
						 "chapter names":       None,
						 "garbage to delete":   ["Preface to the 1857 Edition",
												 """
PREFACE TO THE 1857 EDITION


I have been occupied with this story, during many working hours of two
years. I must have been very ill employed, if I could not leave its
merits and demerits as a whole, to express themselves on its being read
as a whole. But, as it is not unreasonable to suppose that I may have
held its threads with a more continuous attention than anyone else can
have given them during its desultory publication, it is not unreasonable
to ask that the weaving may be looked at in its completed state, and
with the pattern finished.

If I might offer any apology for so exaggerated a fiction as the
Barnacles and the Circumlocution Office, I would seek it in the
common experience of an Englishman, without presuming to mention the
unimportant fact of my having done that violence to good manners, in the
days of a Russian war, and of a Court of Inquiry at Chelsea. If I might
make so bold as to defend that extravagant conception, Mr Merdle, I
would hint that it originated after the Railroad-share epoch, in the
times of a certain Irish bank, and of one or two other equally
laudable enterprises. If I were to plead anything in mitigation of the
preposterous fancy that a bad design will sometimes claim to be a good
and an expressly religious design, it would be the curious coincidence
that it has been brought to its climax in these pages, in the days of
the public examination of late Directors of a Royal British Bank. But,
I submit myself to suffer judgment to go by default on all these counts,
if need be, and to accept the assurance (on good authority) that nothing
like them was ever known in this land.

Some of my readers may have an interest in being informed whether or no
any portions of the Marshalsea Prison are yet standing. I did not know,
myself, until the sixth of this present month, when I went to look. I
found the outer front courtyard, often mentioned here, metamorphosed
into a butter shop; and I then almost gave up every brick of the jail
for lost. Wandering, however, down a certain adjacent ‘Angel Court,
leading to Bermondsey’, I came to ‘Marshalsea Place:’ the houses in
which I recognised, not only as the great block of the former prison,
but as preserving the rooms that arose in my mind’s-eye when I became
Little Dorrit’s biographer. The smallest boy I ever conversed with,
carrying the largest baby I ever saw, offered a supernaturally
intelligent explanation of the locality in its old uses, and was very
nearly correct. How this young Newton (for such I judge him to be) came
by his information, I don’t know; he was a quarter of a century too
young to know anything about it of himself. I pointed to the window of
the room where Little Dorrit was born, and where her father lived so
long, and asked him what was the name of the lodger who tenanted that
apartment at present? He said, ‘Tom Pythick.’ I asked him who was Tom
Pythick? and he said, ‘Joe Pythick’s uncle.’

A little further on, I found the older and smaller wall, which used
to enclose the pent-up inner prison where nobody was put, except for
ceremony. But, whosoever goes into Marshalsea Place, turning out of
Angel Court, leading to Bermondsey, will find his feet on the very
paving-stones of the extinct Marshalsea jail; will see its narrow yard
to the right and to the left, very little altered if at all, except that
the walls were lowered when the place got free; will look upon rooms
in which the debtors lived; and will stand among the crowding ghosts of
many miserable years.

In the Preface to Bleak House I remarked that I had never had so many
readers. In the Preface to its next successor, Little Dorrit, I have
still to repeat the same words. Deeply sensible of the affection and
confidence that have grown up between us, I add to this Preface, as I
added to that, May we meet again!

London May 1857
"""],
						 "main character":    "Amy Dorrit",
						 },


#   ["967-0.txt",   "Nicholas Nickleby by Charles Dickens"],
	"967-0.txt":        {"filename":    "967-0.txt",
						 "title":       "Nicholas Nickleby by Charles Dickens",
						 "characters":
										#from Sparknotes - Literature - A Christmas Carol - CHARACTERS
										#https://www.sparknotes.com/lit/christmascarol/characters/
										["",
										"",
										""],
						 "chapter dividers":    "CHAPTER ",
						 "chapter names":       None,
						 "garbage to delete":   ["containing a Faithful Account of the Fortunes, Misfortunes,",
												 "Uprisings, Downfallings and Complete Career of the Nickelby Family",
												 """AUTHOR’S PREFACE


This story was begun, within a few months after the publication of
the completed “Pickwick Papers.” There were, then, a good many cheap
Yorkshire schools in existence. There are very few now.

Of the monstrous neglect of education in England, and the disregard
of it by the State as a means of forming good or bad citizens, and
miserable or happy men, private schools long afforded a notable example.
Although any man who had proved his unfitness for any other occupation
in life, was free, without examination or qualification, to open a
school anywhere; although preparation for the functions he undertook,
was required in the surgeon who assisted to bring a boy into the world,
or might one day assist, perhaps, to send him out of it; in the chemist,
the attorney, the butcher, the baker, the candlestick maker; the whole
round of crafts and trades, the schoolmaster excepted; and although
schoolmasters, as a race, were the blockheads and impostors who might
naturally be expected to spring from such a state of things, and to
flourish in it; these Yorkshire schoolmasters were the lowest and most
rotten round in the whole ladder. Traders in the avarice, indifference,
or imbecility of parents, and the helplessness of children; ignorant,
sordid, brutal men, to whom few considerate persons would have entrusted
the board and lodging of a horse or a dog; they formed the worthy
cornerstone of a structure, which, for absurdity and a magnificent
high-minded LAISSEZ-ALLER neglect, has rarely been exceeded in the
world.

We hear sometimes of an action for damages against the unqualified
medical practitioner, who has deformed a broken limb in pretending to
heal it. But, what of the hundreds of thousands of minds that have been
deformed for ever by the incapable pettifoggers who have pretended to
form them!

I make mention of the race, as of the Yorkshire schoolmasters, in the
past tense. Though it has not yet finally disappeared, it is dwindling
daily. A long day’s work remains to be done about us in the way of
education, Heaven knows; but great improvements and facilities towards
the attainment of a good one, have been furnished, of late years.

I cannot call to mind, now, how I came to hear about Yorkshire schools
when I was a not very robust child, sitting in bye-places near Rochester
Castle, with a head full of PARTRIDGE, STRAP, TOM PIPES, and SANCHO
PANZA; but I know that my first impressions of them were picked up
at that time, and that they were somehow or other connected with a
suppurated abscess that some boy had come home with, in consequence of
his Yorkshire guide, philosopher, and friend, having ripped it open with
an inky pen-knife. The impression made upon me, however made, never left
me. I was always curious about Yorkshire schools--fell, long afterwards
and at sundry times, into the way of hearing more about them--at last,
having an audience, resolved to write about them.

With that intent I went down into Yorkshire before I began this book, in
very severe winter time which is pretty faithfully described herein.
As I wanted to see a schoolmaster or two, and was forewarned that those
gentlemen might, in their modesty, be shy of receiving a visit from the
author of the “Pickwick Papers,” I consulted with a professional friend
who had a Yorkshire connexion, and with whom I concerted a pious fraud.
He gave me some letters of introduction, in the name, I think, of my
travelling companion; they bore reference to a supposititious little boy
who had been left with a widowed mother who didn’t know what to do
with him; the poor lady had thought, as a means of thawing the tardy
compassion of her relations in his behalf, of sending him to a Yorkshire
school; I was the poor lady’s friend, travelling that way; and if
the recipient of the letter could inform me of a school in his
neighbourhood, the writer would be very much obliged.

I went to several places in that part of the country where I understood
the schools to be most plentifully sprinkled, and had no occasion to
deliver a letter until I came to a certain town which shall be nameless.
The person to whom it was addressed, was not at home; but he came down
at night, through the snow, to the inn where I was staying. It was after
dinner; and he needed little persuasion to sit down by the fire in a
warm corner, and take his share of the wine that was on the table.

I am afraid he is dead now. I recollect he was a jovial, ruddy,
broad-faced man; that we got acquainted directly; and that we talked
on all kinds of subjects, except the school, which he showed a great
anxiety to avoid. “Was there any large school near?” I asked him, in
reference to the letter. “Oh yes,” he said; “there was a pratty big
‘un.” “Was it a good one?” I asked. “Ey!” he said, “it was as good as
anoother; that was a’ a matther of opinion”; and fell to looking at the
fire, staring round the room, and whistling a little. On my reverting to
some other topic that we had been discussing, he recovered immediately;
but, though I tried him again and again, I never approached the question
of the school, even if he were in the middle of a laugh, without
observing that his countenance fell, and that he became uncomfortable.
At last, when we had passed a couple of hours or so, very agreeably, he
suddenly took up his hat, and leaning over the table and looking me
full in the face, said, in a low voice: “Weel, Misther, we’ve been vara
pleasant toogather, and ar’ll spak’ my moind tiv’ee. Dinnot let the
weedur send her lattle boy to yan o’ our school-measthers, while there’s
a harse to hoold in a’ Lunnun, or a gootther to lie asleep in. Ar
wouldn’t mak’ ill words amang my neeburs, and ar speak tiv’ee quiet
loike. But I’m dom’d if ar can gang to bed and not tellee, for weedur’s
sak’, to keep the lattle boy from a’ sike scoondrels while there’s a
harse to hoold in a’ Lunnun, or a gootther to lie asleep in!” Repeating
these words with great heartiness, and with a solemnity on his jolly
face that made it look twice as large as before, he shook hands and went
away. I never saw him afterwards, but I sometimes imagine that I descry
a faint reflection of him in John Browdie.

In reference to these gentry, I may here quote a few words from the
original preface to this book.

“It has afforded the Author great amusement and satisfaction, during the
progress of this work, to learn, from country friends and from a variety
of ludicrous statements concerning himself in provincial newspapers,
that more than one Yorkshire schoolmaster lays claim to being the
original of Mr. Squeers. One worthy, he has reason to believe, has
actually consulted authorities learned in the law, as to his having good
grounds on which to rest an action for libel; another, has meditated a
journey to London, for the express purpose of committing an assault and
battery on his traducer; a third, perfectly remembers being waited on,
last January twelve-month, by two gentlemen, one of whom held him
in conversation while the other took his likeness; and, although Mr.
Squeers has but one eye, and he has two, and the published sketch does
not resemble him (whoever he may be) in any other respect, still he
and all his friends and neighbours know at once for whom it is meant,
because--the character is SO like him.

“While the Author cannot but feel the full force of the compliment thus
conveyed to him, he ventures to suggest that these contentions may arise
from the fact, that Mr. Squeers is the representative of a class, and
not of an individual. Where imposture, ignorance, and brutal cupidity,
are the stock in trade of a small body of men, and one is described
by these characteristics, all his fellows will recognise something
belonging to themselves, and each will have a misgiving that the
portrait is his own.

“The Author’s object in calling public attention to the system would be
very imperfectly fulfilled, if he did not state now, in his own person,
emphatically and earnestly, that Mr. Squeers and his school are faint
and feeble pictures of an existing reality, purposely subdued and kept
down lest they should be deemed impossible. That there are, upon record,
trials at law in which damages have been sought as a poor recompense
for lasting agonies and disfigurements inflicted upon children by the
treatment of the master in these places, involving such offensive and
foul details of neglect, cruelty, and disease, as no writer of fiction
would have the boldness to imagine. And that, since he has been engaged
upon these Adventures, he has received, from private quarters far beyond
the reach of suspicion or distrust, accounts of atrocities, in the
perpetration of which upon neglected or repudiated children, these
schools have been the main instruments, very far exceeding any that
appear in these pages.”

This comprises all I need say on the subject; except that if I had seen
occasion, I had resolved to reprint a few of these details of legal
proceedings, from certain old newspapers.

One other quotation from the same Preface may serve to introduce a fact
that my readers may think curious.

“To turn to a more pleasant subject, it may be right to say, that
there ARE two characters in this book which are drawn from life. It is
remarkable that what we call the world, which is so very credulous in
what professes to be true, is most incredulous in what professes to be
imaginary; and that, while, every day in real life, it will allow in one
man no blemishes, and in another no virtues, it will seldom admit a
very strongly-marked character, either good or bad, in a fictitious
narrative, to be within the limits of probability. But those who take an
interest in this tale, will be glad to learn that the BROTHERS CHEERYBLE
live; that their liberal charity, their singleness of heart, their
noble nature, and their unbounded benevolence, are no creations of the
Author’s brain; but are prompting every day (and oftenest by stealth)
some munificent and generous deed in that town of which they are the
pride and honour.”

If I were to attempt to sum up the thousands of letters, from all sorts
of people in all sorts of latitudes and climates, which this unlucky
paragraph brought down upon me, I should get into an arithmetical
difficulty from which I could not easily extricate myself. Suffice it
to say, that I believe the applications for loans, gifts, and offices
of profit that I have been requested to forward to the originals of the
BROTHERS CHEERYBLE (with whom I never interchanged any communication
in my life) would have exhausted the combined patronage of all the Lord
Chancellors since the accession of the House of Brunswick, and would
have broken the Rest of the Bank of England.

The Brothers are now dead.

There is only one other point, on which I would desire to offer a
remark. If Nicholas be not always found to be blameless or agreeable, he
is not always intended to appear so. He is a young man of an impetuous
temper and of little or no experience; and I saw no reason why such a
hero should be lifted out of nature."""],
						 "main character":    "Nicholas Nickleby",
						 },


  "821-0.txt":          {"filename":    "821-0.txt",
						 "title":       "Dombey and Son by Charles Dickens",
						 "characters":
										#from Sparknotes - Charles Dickens Info - Characters in Dombey and Son
										#https://www.charlesdickensinfo.com/novels/dombey-and-son/whos-who/
										["Louisa Chick",
										 ["Captain Edward (Ned) Cuttle", "Captain Edward Cuttle", "Captain Ned Cuttle",
										  "Edward Cuttle", "Ned Cuttle", "Captain Cuttle"],
										 "Florence Dombey",
										 ["Paul Dombey", "Mr. Dombey", "Dom-bey"],
										 ["Paul Jr. Dombey", "Paul Dombey, Jr."],
										 "Walter Gay",
										 ["Solomon Gills", "Uncle Sol"],
										 "Edith Granger",
										 ["Miss Susan Nipper", "Susan Nipper", "Miss Nipper"]
										 ],
						 "chapter dividers":    "CHAPTER ",
						 "chapter names":       None,
						 "garbage to delete":   ["Transcribed from the 1867/68 Chapman and Hall_ Works of Charles Dickens_,",
												 "_Volume_ 4, _Christmas Books_ by David Price, email ccx074@pglaf.org",
												 "[Picture: Public domain book cover]"],
						 "main character":    None,
						 },


  "676-0.txt":          {"filename":    "676-0.txt",
						 "title":       "The Battle of Life by Charles Dickens",
						 "characters":
										#from Wikipedia, the free encyclopedia
										#https://en.wikipedia.org/wiki/The_Battle_of_Life
										["Grace Jeddler",
										 "Marion Jeddler",
										 "Clemency Newcome",
										 "Ben Britain",
										 "Dr. Jeddler",
										 "Alfred Heathfield",
										 "Michael Warden",
										 "Snitchey",
										 "Craggs",
										 ["aunt Martha", "Martha"]
										 ],
						 "chapter dividers":    "Part the ",
						 "chapter names":       None,
						 "garbage to delete":   [],
						 "main character":    None,
						 },


#   ["653-0.txt",   "The Chimes by Charles Dickens"],
  "653-0.txt":          {"filename":    "653-0.txt",
						 "title":       "The Chimes by Charles Dickens",
						 "characters":
										#from Wikipedia, the free encyclopedia
										#https://en.wikipedia.org/wiki/The_Chimes
										[
											["Toby 'Trotty' Veck", "Toby Veck", "Trotty Veck"],
											["Margaret 'Meg' Veck", "Margaret Veck", "Meg Veck"],
											["Mrs. Anne Chickenstalker", "Anne Chickenstalker", "Mrs. Chickenstalker"],
											"Alderman Cute",
											"Mr. Filer",
											["Sir Joseph Bowley", "Sir Joseph", "Joseph Bowley"],
											"Will Fern",
											"Lilian Fern"],
						 "chapter dividers":    "CHAPTER ",
						 "chapter names":       None,
						 "garbage to delete":   [],
						 "main character":    None,
						 },


  "pg43111.txt":      {"filename":    "pg43111.txt",
						 "title":       "The Personal History of David Copperfield by Charles Dickens",
						 "characters":
										#Charles Dickens Info - Characters in David Copperfield
										#https://www.charlesdickensinfo.com/novels/david-copperfield/whos-who/
										[
											["Richard Babley", "Mr. Dick"],
											"Barkis",
											"Clara Copperfield",
											"David Copperfield",
											"Mr. Creakle",
											#["Little Em’ly", "Emily"],
											["Little Em'ly", "Emily"],
											"Mrs. Grummidge",
											"Uriah Heep",
											"Littimer",
											"Wilkins Micawber",
											"Edward Murdstone",
											"Jane Murdstone",
											"Clara Peggotty",
											"Daniel Peggotty",
											"Ham Peggotty",
											"Dora Spenlow",
											"James Steerforth",
											"Dr. Strong",
											"Tommy Traddles",
											"Betsey Trotwood",
											"Agnes Wickfield",
											"Mr. Wickfield"],
						 "chapter dividers":    "CHAPTER ",
						 "chapter names":       None,
						 "garbage to delete":   ["""Transcriber's note:""",
												 "The errors detailed in the errata at the start of the print"
												 "edition have been corrected.",
												 "Text enclosed by underscores is in italics (_italics_).",
												 "oe-ligatures have been expanded.",
												 "--> represents a hand pointing right.",
												 "[Illustration: Frontispiece]",
												 "[Illustration: David Copperfield. By Charles Dickens.]",
												 "With Illustrations by H. K. Browne.",
												 """London:
Bradbury & Evans, 11, Bouverie Street.
1850.""",
												 """London
Bradbury and Evans, Printers, Whitefriars.""",
												 """AFFECTIONATELY INSCRIBED

								   TO

				 THE HON. MR. AND MRS. RICHARD WATSON,

								   OF

					 ROCKINGHAM, NORTHAMPTONSHIRE.""",
												 "AFFECTIONATELY INSCRIBED",
												 "THE HON. MR. AND MRS. RICHARD WATSON",
												 "ROCKINGHAM, NORTHAMPTONSHIRE."],
						 "main character":    "David Copperfield",
						 },


  "pg1415.txt":         {"filename":    "pg1415.txt",
						 "title":       "Doctor Marigold by Charles Dickens",
						 "characters":
										["Doctor Marigold",
										 "Sophy Marigold",
										 "Willum Redgrave"],
						 "chapter dividers":    None,
						 "chapter names":       None,
						 "garbage to delete":   ["""Transcribed from the 1894 Chapman and Hall "Christmas Stories" edition by""",
												 "David Price, email ccx074@coventry.ac.uk"],
						 "main character":    "Doctor Marigold",
						 },



#   ["810-0.txt",   "George Silverman's Explanation by Charles Dickens"],
  "810-0.txt":          {"filename":    "810-0.txt",
						 "title":       "George Silverman's Explanation by Charles Dickens",
						 "characters":
										#from Sparknotes - Literature - A Christmas Carol - CHARACTERS
										#https://www.sparknotes.com/lit/christmascarol/characters/
										["George Silverman",
										 "Brother Hawkyard",
										 "Brother Gimblet",
										 "Brother Parksop"],
						 "chapter dividers":    None,
						 "chapter names":       ["FIRST CHAPTER",
												 "SECOND CHAPTER",
												 "THIRD CHAPTER",
												 "FOURTH CHAPTER",
												 "FIFTH CHAPTER",
												 "SIXTH CHAPTER",
												 "SEVENTH CHAPTER",
												 "EIGHTH CHAPTER",
												 "NINTH CHAPTER"],
						 "garbage to delete":   ["Transcribed from the 1905 Chapman and Hall “Hard Times and Reprinted",
"Pieces” edition by David Price, email ccx074@pglaf.org"],
						 "main character":    "George Silverman",
						 },


  "809-0.txt":          {"filename":    "809-0.txt",
                         "title":       "Holiday Romance by Charles Dickens",
                         "characters":
                                        ["William Tinkling",
                                        ["Nettie Ashford", "Miss Nettie Ashford"],
                                        ["Lieut.-Col. Robin Redforth", "Robin Redforth"],
                                        "Alice Rainbird",
                                        "Miss Grimmer"],
                         "chapter dividers":    "PART ",
                         "chapter names":       None,
                         "garbage to delete":   ["Transcribed from the 1905 Chapman and Hall “Hard Times and Reprinted",
"Pieces” edition by David Price, email ccx074@pglaf.org",
                                                 """FOOTNOTES


{251}  Aged eight.

{258}  Aged seven.

{266}  Aged nine.

{274}  Aged half-past six."""],
                         "main character":    "William Tinkling",
						 },


#   ["pg1465.txt",  "The Wreck of the Golden Mary by Charles Dickens"],
##  "pg1465.txt":      {"filename":    "pg1465.txt",
##                         "title":       "The Wreck of the Golden Mary by Charles Dickens",
##                         "characters":
##                                        #from Sparknotes - Literature - A Christmas Carol - CHARACTERS
##                                        #https://www.sparknotes.com/lit/christmascarol/characters/
##                                        ["",
##                                        "",
##                                        ""],
##                         "chapter dividers":    None,
##                         "chapter names":       None,
##                         "garbage to delete":   [],
##                       "main character":    None,
##

#["917-0.txt",   "Barnaby Rudge: A Tale of the Riots of 'Eighty by Charles Dickens"],
#Barnaby Rudge: A Tale of the Riots of 'Eighty by Charles Dickens

  "917-0.txt":           {"filename":    "917-0.txt",
#                         "title":       "Barnaby Rudge: A Tale of the Riots of 'Eighty by Charles Dickens",
                         "title":       "Barnaby Rudge by Charles Dickens",
                         "characters":
                                        #from GradeSaver - Study Guides - Barnaby Rudge - Character List
                                        #https://www.gradesaver.com/barnaby-rudge/study-guide/character-list
                                        ["Barnaby Rudge",
										 "Mary Rudge",
										 ["Old John Willet", "John Willet"],
										 "Joe Willets",
										 "Gabriel Varden",
										 "Geoffrey Haredale",
										 "Reuben Haredale",
										 "Emma Haredale",
										 "John Chester",
										 "Edward Chester",
										 ["Barnaby Rudge Senior", "Barnaby Rudge, Sr"],
                                         "Mr. Waterton"],
                         "chapter dividers":    None,
                         "chapter names":       None,
                         "garbage to delete":   ["Produced by Donald Lainson",
                                                 """Contibutor’s Note:

I’ve left in archaic forms such as ‘to-morrow’ or ‘to-day’ as they
occured in my copy. Also please be aware if spell-checking, that within
dialog many ‘mispelled’ words exist, i.e. ‘wery’ for ‘very’, as intended
by the author.

D.L."""],
                       "main character":    "Barnaby Rudge",
						 },




  "pg23765.txt":      {"filename":    "pg23765.txt",
                         "title":       "Captain Boldheart & the Latin-Grammar Master by Charles Dickens",
                         "characters":
                                        ["Captain Boldheart"],
                         "chapter dividers":    None,
                         "chapter names":       None,
                         "garbage to delete":   ["Produced by Geetu Melwani and the Online Distributed",
                                                 "Proofreading Team at http://www.pgdp.net (This file was",
                                                 "produced from images generously made available by The",
                                                 "Internet Archive/American Libraries.)",
                                                 "ILLUSTRATED BY",
                                                 "BEATRICE PEARSE",
                                                 '[Illustration: "Invited them to Breakfast"]',
                                                 '[Illustration: "Invited them to Breakfast"]',
                                                 '[Illustration: "His crew lay grouped around him"]',
                                                 '[Illustration: THE RESCUE OF WILLIAM BOOZEY.]',
                                                 '[Illustration: "Arm-in-arm with the Chief"]',
                                                 '[Illustration: "TWO SAVAGES FLOURED HIM BEFORE PUTTING HIM TO THE',
                                                 '[Illustration: "THE LATIN-GRAMMAR-MASTER HAD A SPARE NIGHTCAP LENT HIM',
                                                 '[Illustration: "ERE THE SUN WENT DOWN FULL MANY A HORNPIPE HAD BEEN',
                                                 '''[Illustration: "Married the Chief's daughter"]''',
                                                 '[Illustration: "DOST KNOW THE NAME OF YON SHIP, MAYOR?"]',
                                                 '[Illustration: STANDING SENTRY OVER HIM]',
                                                 '[Illustration: "His lovely Bride came forth"]',
                                                 '''[Illustration: "CAPTAIN BOLDHEART'S LADY BEGGED FOR HIM AND HE WAS
SPARED."]''',
                                                 """       *       *       *       *       *


           THE ORANGE TREE SERIES
            OF CHILDREN'S BOOKS

FULLY ILLUSTRATED IN COLOUR, 1s. net. Foolscap 4to, boards

       *       *       *       *       *

1. THE STORY OF RICHARD DOUBLEDICK. By Charles Dickens. With
illustrations by W. B. Wollen, R.I., R.O.I.

2. THE MAGIC FISHBONE. By Charles Dickens. With illustrations by S.
Beatrice Pearse.

3. THE TRIAL OF WILLIAM TINKLING. By Charles Dickens. With illustrations
by S. Beatrice Pearse.

4. CAPTAIN BOLDHEART AND THE LATIN-GRAMMAR MASTER. By Charles Dickens.
With illustrations by S. Beatrice Pearse.


           THE WONDER BOOK

By Nathaniel Hawthorne. With Coloured Illustrations by Patten Wilson.

5. THE GORGON'S HEAD
6. THE GOLDEN TOUCH

_The above are ready. The following are in active preparation._

 7. THE PARADISE OF CHILDREN
 8. THE THREE GOLDEN APPLES
 9. THE MIRACULOUS PITCHER
10. THE CHIMAERA


           TANGLEWOOD TALES

By Nathaniel Hawthorne. With Coloured Illustrations by Patten Wilson.

11. THE MINOTAUR
12. THE PYGMIES
13. THE DRAGON'S TEETH
14. CIRCE'S PALACE
15. THE POMEGRANATE SEEDS
16. THE GOLDEN FLEECE

LONDON: CONSTABLE & COMPANY, LIMITED

       *       *       *       *       *"""],
                       "main character":    None,
						 },


  "564-0.txt":          {"filename":    "564-0.txt",
						 "title":       "The Mystery of Edwin Drood by Charles Dickens",
						 "characters":
										#from eNotes.com - Homework Help - Study Guides - The Mystery of Edwin Drood by Charles Dickens
										#https://www.enotes.com/topics/mystery-edwin-drood/characters
										["Edwin Drood",
										"Jack Jasper",
										"Rosa Bud",
										"Neville Landless",
										"Helena Landless",
										["the Reverend Septimus Crisparkle", "Mr. Crisparkle", "Septimus Crisparkle"],
										"Mr. Grewgious",
										"Datchery",
										"Durdles",
                                         #Additional characters
                                         "Mr. Honeythunder",
                                         ],
						 "chapter dividers":    "CHAPTER ",
						 "chapter names":       None,
						 "garbage to delete":   ["[Picture: Rochester castle]",
												 "[Picture: In the Court]",
												 "[Picture: Under the trees]",
												 "[Picture: At the piano]",
												 "[Picture: On dangerous ground]",
												 "[Picture: Mr. Crisparkle is overpaid]",
												 "[Picture: Durdles cautions Mr. Sapsea against boasting]",
												 '[Picture: "Good-bye, Rosebud darling"]',
												 "[Picture: Mr. Grewgious has his suspicions]",
												 "[Picture: Jasper's sacrifices]",
												 "[Picture: Mr. Grewgious experiences a new sensation]",
												 "[Picture: Up the river]",
												 "[Picture: Sleeping it off]",
												 """ [Picture: Facsimile of a page of the manuscript of “The Mystery of Edwin
								 Drood"]"""],
						 "main character":       "Edwin Drood",
						 },

}


titles = ["Lady", "Grandmother", "Aunt", "Mrs.", "Miss", "Mr.", "Doctor", "Dr.", "Uncle",
		  "Inspector", "Captain", "Prince", "Grandfather", "Alderman", "Brother",
		  "Count", "Colonel", "The Hon.", "The Reverend", "Lieutenant", "Sir", "Master",
		  "Monsieur", "Madame", "Mademoiselle", "Marquis", "Lieut.-Col."]


def modify_files(VERBOSE=1):
	converted_count = 0
	thisdir = os.getcwd()
	keys = characters_dict.keys()
	keys.sort()
	for f in keys:
		if VERBOSE == 1:
			print "working on file '%s'..." % f
		else:
			print ".",
		if os.path.isfile(os.path.join(thisdir, "raw", f)):
			if VERBOSE == 1:
				print "\t('%s')" % string.split(characters_dict[f]["title"], " by ")[0] 
			else:
				print ".",
			converted_count = converted_count + 1
			prefix, suffix = string.split(f, ".")
			newfn = "%s_NEW.%s" % (prefix, suffix)
			outfile = io.open(os.path.join(thisdir, "modified", newfn), encoding="UTF-8", mode="w")
			infile = io.open(os.path.join(thisdir, "raw", f), encoding="UTF-8", mode="r").read()
			infile = stripheaders.strip_headers(infile)
			infile = stupify(infile)

			full_title = characters_dict[f]["title"]
			full_title_placeholder = "[BOOK_FULL_TITLE]"
			try:
				infile = infile.replace(full_title.decode("UTF-8", "ignore"), full_title_placeholder.decode("UTF-8", "ignore"))
			except:
				infile = infile.replace(full_title.encode("UTF-8", "ignore"), full_title_placeholder.encode("UTF-8", "ignore"))

			short_title = string.split(characters_dict[f]["title"], " by ")[0] 
			short_title_placeholder = "[BOOK_SHORT_TITLE]"
			try:
				infile = infile.replace(short_title.decode("UTF-8", "ignore"), short_title_placeholder.decode("UTF-8", "ignore"))
			except:
				infile = infile.replace(short_title.encode("UTF-8", "ignore"), short_title_placeholder.encode("UTF-8", "ignore"))

			short_title_caps = string.upper(short_title) 
			short_title_caps_placeholder = "[BOOK_SHORT_TITLE_CAPS]"
			try:
				infile = infile.replace(short_title_caps.decode("UTF-8", "ignore"), short_title_caps_placeholder.decode("UTF-8", "ignore"))
			except:
				infile = infile.replace(short_title_caps.encode("UTF-8", "ignore"), short_title_caps_placeholder.encode("UTF-8", "ignore"))

			author1 = "Charles Dickens"
			author2 = string.upper(author1)

			author_placeholder = "[AUTHOR]"
			author_placeholder_caps = "[AUTHOR_CAPS]"
			try:
				infile = infile.replace(author1.decode("UTF-8", "ignore"), author_placeholder.decode("UTF-8", "ignore"))
			except:
				infile = infile.replace(author1.encode("UTF-8", "ignore"), author_placeholder.encode("UTF-8", "ignore"))
			try:
				infile = infile.replace(author1.decode("UTF-8", "ignore"), author_placeholder.decode("UTF-8", "ignore"))
			except:
				infile = infile.replace(author2.encode("UTF-8", "ignore"), author_placeholder_caps.encode("UTF-8", "ignore"))


			#make use of this later...
			exceptions = ["Artful Dodger", "The Convict"]

			CHARACTER_NUMBER = 0
			for character_name in characters_dict[f]["characters"]:
				#do all the characters first, in case they share surnames...
				CHARACTER_NUMBER = CHARACTER_NUMBER + 1
				placeholder = "[CHARACTER_NAME_%03d]" % CHARACTER_NUMBER
				#infile = infile.replace(character_name.encode("UTF-8", "ignore"), placeholder.encode("UTF-8", "ignore"))
				if type(character_name) in (StringType, UnicodeType):
					character_name_caps = string.upper(character_name)
					placeholder_caps = "[CHARACTER_NAME_CAPS_%03d]" % CHARACTER_NUMBER
					try:
						infile = infile.replace(character_name.decode("UTF-8", "ignore"), placeholder.decode("UTF-8", "ignore"))
					except:
						try:
							infile = infile.replace(character_name.encode("UTF-8", "ignore"), placeholder.encode("UTF-8", "ignore"))
						except:
							print """FAILED ON '%s'!""" % character_name
					try:
						infile = infile.replace(character_name_caps.decode("UTF-8", "ignore"), placeholder_caps.decode("UTF-8", "ignore"))
					except:
						try:
							infile = infile.replace(character_name_caps.encode("UTF-8", "ignore"), placeholder_caps.encode("UTF-8", "ignore"))
						except:
							print """FAILED ON '%s'!""" % character_name_caps
				elif type(character_name) in (TupleType, ListType):
					for cn in character_name:
						character_name_caps = string.upper(cn)
						placeholder_caps = "[CHARACTER_NAME_CAPS_%03d]" % CHARACTER_NUMBER
						try:
							infile = infile.replace(cn.decode("UTF-8", "ignore"), placeholder.decode("UTF-8", "ignore"))
							infile = infile.replace(character_name_caps.decode("UTF-8", "ignore"), placeholder_caps.decode("UTF-8", "ignore"))
						except:
							infile = infile.replace(cn.encode("UTF-8", "ignore"), placeholder.encode("UTF-8", "ignore"))
							infile = infile.replace(character_name_caps.encode("UTF-8", "ignore"), placeholder_caps.encode("UTF-8", "ignore"))

			CHARACTER_NUMBER = 0
			for character_name in characters_dict[f]["characters"]:
				CHARACTER_NUMBER = CHARACTER_NUMBER + 1
				if type(character_name) in (StringType, UnicodeType):
					if len(string.split(character_name, " ")) == 2:
						firstname, surname = string.split(character_name, " ")
						surname_placeholder = "[CHARACTER_%03d_SURNAME]" % CHARACTER_NUMBER
						firstname_placeholder = "[CHARACTER_%03d_FIRSTNAME]" % CHARACTER_NUMBER
						firstname_caps = string.upper(firstname)
						firstname_placeholder_caps = "[CHARACTER_%03d_FIRSTNAME_CAPS]" % CHARACTER_NUMBER
						surname_caps = string.upper(surname)
						surname_placeholder_caps = "[CHARACTER_%03d_SURNAME_CAPS]" % CHARACTER_NUMBER
						if firstname not in titles:
							try:
								infile = infile.replace(firstname.decode("UTF-8", "ignore"), firstname_placeholder.decode("UTF-8", "ignore"))
							except:
								infile = infile.replace(firstname.encode("UTF-8", "ignore"), firstname_placeholder.encode("UTF-8", "ignore"))
							try:
								infile = infile.replace(firstname_caps.decode("UTF-8", "ignore"), firstname_placeholder_caps.decode("UTF-8", "ignore"))
							except:
								infile = infile.replace(firstname_caps.encode("UTF-8", "ignore"), firstname_placeholder_caps.encode("UTF-8", "ignore"))
						try:
							infile = infile.replace(surname.decode("UTF-8", "ignore"), surname_placeholder.decode("UTF-8", "ignore"))
						except:
							try:
								infile = infile.replace(surname.encode("UTF-8", "ignore"), surname_placeholder.encode("UTF-8", "ignore"))
							except:
								print "FAILED ON '%s'!" % surname

						try:
							infile = infile.replace(surname_caps.decode("UTF-8", "ignore"), surname_placeholder_caps.decode("UTF-8", "ignore"))
						except:
							try:
								infile = infile.replace(surname_caps.encode("UTF-8", "ignore"), surname_placeholder_caps.encode("UTF-8", "ignore"))
							except:
								print "FAILED ON '%s'!" % surname

				elif type(character_name) in (TupleType, ListType):
					for cn in character_name:
						if len(string.split(cn, " ")) == 2:
							firstname, surname = string.split(cn, " ")
							surname_placeholder = "[CHARACTER_%03d_SURNAME]" % CHARACTER_NUMBER
							firstname_placeholder = "[CHARACTER_%03d_FIRSTNAME]" % CHARACTER_NUMBER
							firstname_caps = string.upper(firstname)
							firstname_placeholder_caps = "[CHARACTER_%03d_FIRSTNAME_CAPS]" % CHARACTER_NUMBER
							surname_caps = string.upper(surname)
							surname_placeholder_caps = "[CHARACTER_%03d_SURNAME_CAPS]" % CHARACTER_NUMBER
							if firstname not in titles:
								try:
									infile = infile.replace(firstname.decode("UTF-8", "ignore"), firstname_placeholder.decode("UTF-8", "ignore"))
								except:
									infile = infile.replace(firstname.encode("UTF-8", "ignore"), firstname_placeholder.encode("UTF-8", "ignore"))

								try:
									infile = infile.replace(firstname_caps.decode("UTF-8", "ignore"), firstname_placeholder_caps.decode("UTF-8", "ignore"))
								except:
									infile = infile.replace(firstname_caps.encode("UTF-8", "ignore"), firstname_placeholder_caps.encode("UTF-8", "ignore"))

							try:
								infile = infile.replace(surname.decode("UTF-8", "ignore"), surname_placeholder.decode("UTF-8", "ignore"))
							except:
								infile = infile.replace(surname.encode("UTF-8", "ignore"), surname_placeholder.encode("UTF-8", "ignore"))

							try:
								infile = infile.replace(surname_caps.decode("UTF-8", "ignore"), surname_placeholder_caps.decode("UTF-8", "ignore"))
							except:
								try:
									infile = infile.replace(surname_caps.encode("UTF-8", "ignore"), surname_placeholder_caps.encode("UTF-8", "ignore"))
								except:
									print "FAILED ON '%s'!" % surname
			outfile.write(infile.decode("UTF-8", "ignore"))
			outfile.close()
			if VERBOSE == 1:
				print "\twrote output file '%s'\n" % os.path.join(thisdir, "modified", newfn)
			else:
				print ".",
		else:
			print "\tNO DATA FILE FOUND FOR '%s'!\n" % f
					   
	os.chdir(thisdir)
	if VERBOSE == 1:
		print "DONE."
		print "nConverted %s files.\n" % converted_count
	else:
		print "DONE."

def test_names():
	"test to see if names are recognised as male or female..."

	all_names = []
	unrecognised_names = []

	for key in characters_dict.keys():
		characters = characters_dict[key]["characters"]
		for c in characters:
			if type(c) in (StringType, UnicodeType):
				all_names.append(c)
			elif type(c) in (ListType, TupleType):
				for d in c:
					all_names.append(d)
	all_name = all_names.sort()
	names_tested = 0
	recognised_names = 0
	unrecognised_names_count = 0

	for n in all_names:
		names_tested = names_tested + 1
		if string.find(n, " ") > -1:
			firstname, surname = string.split(n, " ", maxsplit=1)
		else:
			firstname = n
			

		if check_gender(firstname) == "female":
			print "name:\t'%s'\tFEMALE" % firstname
			recognised_names = recognised_names + 1
		elif check_gender(firstname) == "male":
			print "name:\t'%s'\tMALE" % firstname
			recognised_names = recognised_names + 1
		elif firstname == "Mr.":
			print "name:\t'%s'\tMALE" % n
			recognised_names = recognised_names + 1
		elif firstname in ("Mrs.", "Miss", "Madame"):
			print "name:\t'%s'\tFEMALE" % n
			recognised_names = recognised_names + 1
		elif firstname in titles:
			recognised_names = recognised_names + 1
		else:
			unrecognised_names.append(n)
			unrecognised_names_count = unrecognised_names_count + 1

	unrecognised_names.sort()            

	print "\n\n%s names tested.\n%s names recognised\n%s names UNRECOGNISED" % (names_tested,
																			   recognised_names,
																			   unrecognised_names_count)


	print "\n\nUNRECONISED NAMES:"

	outfile = open("UNREGONISED_NAMES_LOG.txt", "w")
	for n in unrecognised_names:
		print "\t%s" % n
		outfile.write("\t%s\n" % n)
	outfile.close()


def count_files():
	if os.path.isdir("raw"):
		thisdir = os.getcwd()
		os.chdir(os.path.join(thisdir, "raw"))
		allfiles = glob.glob("*.txt")
		os.chdir(thisdir)
		return len(allfiles)
	else:
		return 0

if __name__ == "__main__":
	if VERBOSE == 1:
		print "\n'What The Dickens'\n"
		print "%s Dickens books known about" % (len(index))
		print "%s data files found\n\n" % count_files()
		print
	modify_files(VERBOSE=VERBOSE)
	#test_names()
	