#!/usr/local/bin/python
# -*- coding: UTF-8 -*-

import os, string, random, glob, time
import blurbwriter, names
from source.index import prettify

import reportlab
import PIL

import PIL.Image as Image
from PIL import ImageOps

from reportlab.lib.colors import black, white, red, lightgrey, darkgrey
from reportlab.lib.colors import *
from reportlab.lib.units import inch, cm, mm
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.utils import ImageReader
from reportlab.graphics import renderPDF
from reportlab.graphics.shapes import Group, Drawing, Rect
from reportlab.pdfgen import canvas
from reportlab.pdfbase.pdfmetrics import registerFont, stringWidth
from reportlab.pdfbase.ttfonts import TTFont

from reportlab.graphics.barcode import eanbc


VERBOSE = 0
#VERBOSE = 1

heraldic_cols = {
	"Murrey":       {"Name":               "Murrey",
					 "Colour":             "dark reddish purple",
					 "Screen Colour":      "#8b004b",
					 "RGB Colour":         (139, 0, 75)
					 },
	"Sanguine":     {"Name":                "Sanguine",
					 "Colour":              "blood red",
					 "Screen Colour":       "#b22222",
					 "RGB Colour":          (178, 34, 34)
					 },
	"Tenné":        {"Name":                "Tenné",
					 "Colour":              "orange",
					 "Screen Colour":       "#c67000",
					 "RGB Colour":          (198, 112, 0)
					 },
	"Argent":       {"Name":                "Argent",
					 "Colour":              "white",
					 "Screen Colour":       "#fdfdfd",
					 "RGB Colour":          (253, 253, 253)
					 },
	"Or":           {"Name":                "Or",
					 "Colour":              "yellow",
					 "Screen Colour":       "#fefe00",
					 "RGB Colour":          (254, 254, 0)
					 },
	"Gules":        {"Name":                "Gules",
					 "Colour":              "red",
					 "Screen Colour":       "#ee0000",
					 "RGB Colour":          (238, 0, 0)
					 },
	"Sable":        {"Name":                "Sable",
					 "Colour":              "black",
					 "Screen Colour":       "#111111",
					 "RGB Colour":          (17, 17, 17)
					 },
	"Azure":        {"Name":                "Azure",
					 "Colour":              "blue",
					 "Screen Colour":       "#0000cc",
					 "RGB Colour":          (0, 0, 204)
					 },
	"Vert":         {"Name":                "Vert",
					 "Colour":              "green",
					 "Screen Colour":       "#008000",
					 "RGB Colour":          (0, 128, 0)
					 },
	"Purpure":      {"Name":                "Purpure",
					 "Colour":              "purple",
					 "Screen Colour":       "#600060",
					 "RGB Colour":          (96, 0, 96)
					 }
	}

POSS_COVER_STYLES = ["Type 1", "Type 2", "Type 3", "Type 4"]


def get_checksum(s):
	"""code snippet from https://codegolf.stackexchange.com/questions/342/calculate-isbn-13-check-digit
	returns a whole 13-digit ISBN, not just the checksum"""
	#s = ISBN
	#lambda s:s+`-sum(map(int,s+s[1::2]*2))%10`
	return s+`-sum(map(int,s+s[1::2]*2))%10`


def make_ISBN_barcode(c, ISBN):
	"""Creates a barcode for the supplied ISBN and plonks it in a drawing. 
(No error checking on the suppplied ISBN - do it elsewhere)."""

	if c == None:
		c = canvas.Canvas("barcodes_test.pdf", pagesize=A4)

	if ISBN == None:
		#could randomly generate an ISBN, but "1234567890" makes it
		#more obvious that one wasn't passed in.
		barcode_value = "1234567890"
	else:
		barcode_value =  ISBN

	# draw the eanbc13 code
	barcode_eanbc13 = eanbc.Ean13BarcodeWidget(barcode_value)
	bounds = barcode_eanbc13.getBounds()
	width = bounds[2] - bounds[0]
	height = bounds[3] - bounds[1]
	d = Drawing(50, 10)
	d.add(barcode_eanbc13)
	renderPDF.draw(d, c, (A4[0]/2.0)-52, 2.5*cm)

	return c


def make_ISBN(spacer="-", year_generated=None):
	"""create a valid looking ISBN number. The checksum is valid, and
	both the prefix element and (single-digit) registration group
	element are what they would be for a UK-based publisher. The
	Registrant element, SHOULD however, be one that's unissued, making
	the ISBN invalid."""

	#it is customary to separate the parts with hyphens or spaces.
	#is spacer should be either "-" or " "
	spacer = random.choice((" ", "-"))

	current_year = int(time.localtime()[0])

	if year_generated == None:
		year_generated = current_year

	#An ISBN is an International Standard Book Number. ISBNs were 10 digits
	#in length up to the end of December 2006, but since 1 January 2007
	#they now always consist of 13 digits.

	#10-digit ISBNS (ie pre-2007 ones) are not currently implemented...
	#forfuture expansion
	if year_generated < 2007:
		ISBN_len = 10
	else:
		ISBN_len = 13

	#GS1 Prefix
	#978 – 979
	#Allocated to International ISBN Agency for books, portion of 979
	#sub-allocated to International ISMN Agency for music

	#Prefix element – currently this can only be either 978 or 979. It is
	#always 3 digits in length
	prefix_element              = "978" #978 is most common

	#The single-digit group
	#identifiers within the 978-prefix element are: 0 or 1 for
	#English-speaking countries
	registration_group_element  = "1"

	#Registrant element - this identifies the particular publisher or
	#imprint. This may be up to 7 digits in length

	#According to Wikipedia, 
	#List of 6-digit publisher codes
	#https://en.wikipedia.org/wiki/List_of_group-1_ISBN_publisher_codes

	#THESE NUMBER RANGES *APPEAR* TO BE UNKNOWN AND/OR UNUSED.
	#(NB THE LIST IS INCOMPLETE - SO THIS MAY NOT BE THE CASE!)
	#949931~972999
	#987800~989667
	#989669~998999      <- this one wouold give us a range of 9,330 numbers

	#Publisher code – Penguin Books is 140

	#r = random.choice(range(989669, 998999))
	r = random.choice(range(9669, 9999))
	registrant_element          = "%04d" % r

	#Here are some of the London, UK based publishers who use a 6-digit publisher code...
	#870870 John Brown Publishing Ltd.
	#903222 Nightingale
	#903258 Carroll & Brown Publishers
	#905847 Old Street Publishing
	#905881 Granta Publications
	#906694 Quercus
	#911214 Jonathan Cape, imprint of Vintage Publishing

	#Publication element – this identifies the particular edition and
	#format of a specific title. This may be up to 6 digits in length
	s = random.choice(range(1,9999))
	publication_element         = "%04d" % s

	#Check digit – this is always the final single digit that
	#mathematically validates the rest of the number. It is calculated
	#using a Modulus 10 system with alternate weights of 1 and 3.
	check_digit = get_checksum("%s%s%s%s" % (prefix_element, registration_group_element, registrant_element, publication_element))

	#may use this elsewhere, but we want to split ours with dashes(or spaces)
	checksun_digit = check_digit[-1]

	ISBN = string.join((prefix_element, registration_group_element,
						registrant_element, publication_element, checksun_digit),
						sep=spacer)

	return ISBN


def make_back_cover(c, VERBOSE, outfileName, width, height, author, bookname,
					blurb, background_colour=None, foreground_colour=None,
					ISBN_text=None, ISBN_for_barcode=None, price=None,
					cover_style="Type 1", dickens_book = None):

	"""creates the back cover for our book."""

	#prints LOADS of annoying debugging messages. Best  to tun off unless something's screwed up!
	DEBUG = 0
	#DEBUG = 1

	bookname = string.strip(bookname)
	bookname = prettify(bookname)
	#having these capitalised looks odd...
	bookname = bookname.replace(" To ", " to ")
	bookname = bookname.replace(" Of ", " of ")
	bookname = bookname.replace(" The ", " the ")

	if cover_style != "Type 4":
		#since Type 4 calls Type 2, this would give us two bookmarks for the back cover...
		c.bookmarkPage("BackCover")
		c.addOutlineEntry(key="BackCover", level=1, title="Back Cover", closed=None)

	if cover_style == "Type 1":

		#"Type 1" =     our initial cover style
		#               coloured tint over a full page picture, white text (with dropshadow)

		c.setFillColorRGB(background_colour[0], background_colour[1],background_colour[2], 0.5)
		c.rect(0,0,A4[0],A4[1], fill=1)

		c.setFillColorRGB(0.95, 0.95, 0.95, 0.75)
		c.rect(cm, cm, A4[0]-(2*cm), A4[1]-(2*cm), fill=1)

		xpos = 2*cm
		ypos = A4[1] - 2.5*cm

		blurb = prettify(blurb)

		c.setFillColorRGB(0.1, 0.1, 0.1)

		newline2 = prettify(bookname)
		#newline2 = "%s %s" % (newline, word)

		c.setFont("Gentium Basic Bold", 24)

		newline2dwidth = stringWidth(newline2, "Gentium Basic Bold", 24, "latin-1")

		if newline2dwidth < (A4[0] - 4*cm):
			xpos = (A4[0]/2.0) - (stringWidth(newline2, "Gentium Basic Bold", 24, "latin-1")/2.0)
			c.drawString(xpos, ypos, "%s" % (string.strip(newline2)))
		else:
			newline = ""
			for word in newline2.split():
				newline2 = "%s %s" % (newline, word)
				newline2dwidth = stringWidth(newline2, "Gentium Basic Bold", 24, "latin-1")
				if newline2dwidth > (A4[0] - 4*cm):
				#if newline2dwidth > (A4[0] - 2*cm):
					xpos = (A4[0]/2.0) - (stringWidth(newline, "Gentium Basic Bold", 24, "latin-1")/2.0)
					c.drawString(xpos, ypos, "%s" % (string.strip(newline)))
					newline = "%s" % word
					ypos = ypos-20
				else:
					newline= newline2
			xpos = (A4[0]/2.0) - (stringWidth(string.strip(newline), "Gentium Basic Bold", 24, "latin-1")/2.0)
			c.drawString(xpos, ypos, "%s" % (string.strip(newline)))

		c.setFont("Gentium Basic", 16)

		ypos = ypos - 1.25*cm
		xpos = 2*cm

		for line in blurb.split("\n"):

			linewidth = stringWidth(line, "Gentium Basic", 16, "latin-1")
			c.setFont("Gentium Basic", 16)

			if linewidth < (A4[0] - 4*cm):
			#if linewidth < (A4[0] - 2*cm):
				xpos = 2*cm
				ypos = ypos - 18

				if ypos < 2*cm:
					c.showPage()
					ypos = (A4[1] - 2 * cm)

				try:
					line=line.decode("utf-8")
					line=line.encode("latin-1","ignore")
				except:
					pass
				c.drawString(xpos, ypos, "%s" % (string.strip(line)))
			else:
				newline = ""
				for word in line.split():
					newline2 = "%s %s" % (newline, word)
					newline2dwidth = stringWidth(newline2, "Gentium Basic", 16, "latin-1")
					if newline2dwidth > (A4[0] - 4*cm):
					#if newline2dwidth > (A4[0] - 2*cm):
						c.drawString(xpos, ypos, "%s" % (string.strip(newline)))
						newline = "%s" % word
						ypos = ypos-20
					else:
						newline= newline2
				c.drawString(xpos, ypos, "%s" % (string.strip(newline)))
				if ypos < 2*cm:
					c.showPage()
					#d.pagenum = d.pagenum + 1
					ypos = A4[1] - 2*cm

		ypos = ypos-20

		ypos = ypos-0.05*cm


		thisblurbnum = 0
		#do critics' quotes...

		#try and avoid repeats...
		used_blurbs = []

		while ypos > 192:
			if DEBUG == 1:
				print
				print "--==******==--"
				print "...YPOS STILL MORE THAN 182..."
				print "--==******==--"
				print
			thisblurb = blurbwriter.do_blurb(quotechar='"', author=author, characters=None,
											 main_character=None, bookname=bookname,
											 num_blurbs=1, thisblurb=thisblurbnum)

			while thisblurb in used_blurbs:
				thisblurb = blurbwriter.do_blurb(quotechar='"', author=author, characters=None,
												 main_character=None, bookname=bookname,
												 num_blurbs=1, thisblurb=thisblurbnum)

			used_blurbs.append(thisblurb)

			thisblurbnum = thisblurbnum + 1

			thisblurb = prettify(thisblurb)
			if DEBUG == 1:
				print "========================="
				print "created new blurb..."
				print "thisblurb:"
				try:
					print "'%s'" % thisblurb.decode("ascii", "ignore")
				except:
					print "'%s'" % thisblurb.encode("ascii", "ignore")
				print "'ypos: %s'" % ypos
				print "========================="
			
			c.setFont("Gentium Basic", 14)
			thisblurbwidth = stringWidth(thisblurb, "Gentium Basic", 14, "latin-1")

			if string.find(thisblurb, "\n") > -1:
				if DEBUG == 1:
					print "FOUND A NEWLINE...."
					print "thisblurb:"
					try:
						print "'%s'" % thisblurb.decode("ascii", "ignore")
					except:
						print "'%s'" % thisblurb.encode("ascii", "ignore")
					print
				for line in thisblurb.split("\n"):
					line = string.strip(line)
					if line in ["", "\n", None]:
						pass
					else:
						thislinewidth = stringWidth(line, "Gentium Basic", 14, "latin-1")
						if thislinewidth < (A4[0] - 4*cm):
							#it's a short line...
							if string.find(line, "(") > -1:
								if DEBUG == 1:
									print "!!! FOUND OPENING BRACKET..."
								if string.find(line, ")") > -1:
									if DEBUG == 1:
										print "!!!!! FOUND CLOSING BRACKET! ..."
									#opening AND closing brackets probably mean that it's a newspaper attribution line...
									if DEBUG == 1:
										print "FOUND AN ATTRIBUTION LINE... SETTING FONT TO BOLD ITALIC..."
									c.setFont("Gentium Basic Bold Italic", 14)
									if string.find(line, "interesting") > -1:
										if DEBUG == 1:
											print '... oh, it was "interesting"... SETTING FONT TO back to BASIC...'
										c.setFont("Gentium Basic", 14)
								else:
									if DEBUG == 1:
										print "ATTRIBUTION LINE NOT FOUND... SETTING FONT TO BASIC..."
									c.setFont("Gentium Basic", 14)
							else:
								if DEBUG == 1:
									print "ATTRIBUTION LINE NOT FOUND... SETTING FONT TO BASIC..."
								c.setFont("Gentium Basic", 14)
							c.drawString(xpos, ypos, "%s" % (string.strip(line)))
						else:
							#it's a long line...
							newlineslist = []
							#with multi-line quotes, if we just add them line-by-line, the first line may be in a good
							#position, but the second or third goes under the ISBN box. Add them to a list,
							#and if it's still OK once we've checked all the lines, add the whole quote at the end...
							newline = ""
							fontset = None

							for word in line.split():
								newline2 = "%s %s" % (newline, word)
								newline2dwidth = stringWidth(newline2, "Gentium Basic", 14, "latin-1")
								if newline2dwidth > (A4[0] - 4*cm):
								#if newline2dwidth > (A4[0] - 2*cm):
									#xpos = (A4[0]/2.0) - (stringWidth(newline2, "Gentium Basic Bold", 24, "latin-1")/2.0)
									if string.find(newline2, "(") > -1:
										if string.find(newline2, ")") > -1:
											#opening AND closing brackets probably mean that it's a newspaper attribution line...
											#c.setFont("Gentium Basic Italic", 14)
											fontset = "Gentium Basic Italic"
										else:
											#c.setFont("Gentium Basic", 14)
											fontset = "Gentium Basic"
									else:
										#c.setFont("Gentium Basic", 14)
										fontset = "Gentium Basic"
									#c.drawString(xpos, ypos, "%s" % (string.strip(newline)))
									newlineslist.append([fontset, xpos, ypos, string.strip(newline)])
									newline = "%s" % word
									ypos = ypos-20
								else:
									newline= newline2

							if string.find(newline2, "(") > -1:
								if string.find(newline2, ")") > -1:
									#opening AND closing brackets probably mean that it's a newspaper attribution line...
									#c.setFont("Gentium Basic Italic", 14)
									fontset = "Gentium Basic Italic"
								else:
									#c.setFont("Gentium Basic", 14)
									fontset = "Gentium Basic"
							else:
								#c.setFont("Gentium Basic", 14)
								fontset = "Gentium Basic"

							newlineslist.append([fontset, xpos, ypos, string.strip(newline)])

							#c.setFont("Gentium Basic", 14)
							fontset = "Gentium Basic"

							#is ypos still high enough to clear the ISBN box?
							if ypos > 192:
								#I guess it is. OK, add the whole quote...
								for listybit in newlineslist:
									fontset, xpos, ypos, newline = listybit
									c.setFont(fontset, 14)
									c.drawString(xpos, ypos, newline)

						ypos = ypos-18
					
			else:

				if DEBUG == 1:
					print "NEWLINE *NOT* FOUND..."
					print "thisblurb:"
					try:
						print "'%s'" % thisblurb.decode('ascii','ignore')
					except:
						print "'%s'" % thisblurb.encode('ascii','ignore')
					print

				if thisblurbwidth < (A4[0] - 4*cm):
					#xpos = (A4[0]/2.0) - (stringWidth(newline2, "Gentium Basic Bold", 24, "latin-1")/2.0)
					c.drawString(xpos, ypos, "%s" % (string.strip(thisblurb)))
				else:
					newline = ""
					for word in thisblurb.split():
						newline2 = "%s %s" % (newline, word)
						newline2dwidth = stringWidth(newline2, "Gentium Basic", 14, "latin-1")
						if newline2 in ["", "\n", None]:
							pass
						else:
							if newline2dwidth > (A4[0] - 4*cm):
							#if newline2dwidth > (A4[0] - 2*cm):
								#xpos = (A4[0]/2.0) - (stringWidth(newline2, "Gentium Basic Bold", 24, "latin-1")/2.0)
								###c.drawString(xpos, ypos, "%s" % (string.strip(newline)))
								newline = "%s" % word
								ypos = ypos-20
							else:
								newline= newline2
					#xpos = (A4[0]/2.0) - (stringWidth(newline2, "Gentium Basic Bold", 24, "latin-1")/2.0)
					c.drawString(xpos, ypos, "%s" % (string.strip(newline)))

			try:
				blurb = u"%s\n\n%s" % (blurb.decode("UTF-8", 'ignore') , thisblurb.decode("UTF-8", 'ignore'))
			except:
				try:
					blurb = u"%s\n\n%s" % (blurb.encode("UTF-8", 'ignore'), thisblurb.encode("UTF-8", 'ignore'))
					#blurb = u"%s\n\n%s" % (blurb.decode("ascii", 'ignore') , thisblurb.decode("ascii", 'ignore'))
				except:
					blurb = u"%s\n\n%s" % (blurb.encode("ascii", 'ignore'), thisblurb.encode("ascii", 'ignore'))

			if DEBUG == 1:
				print "***************"
				print "blurb (in loop)"
				try:
					print "'%s'" % blurb.decode("ascii", 'ignore')
				except:
					print "'%s'" % blurb.encode("ascii", 'ignore')
				print "***************"
				print

			ypos = ypos-20
			if DEBUG == 1:
				print
				print "--==******==--"
				print "...ENDING LOOP.... YPOS NOW %s ... " % ypos 
				print "--==******==--"
				print

		ypos = ypos-20
			
		#backing box for barcode....
		c.setFillColorRGB(243, 243, 243, 0.75)
		c.rect((A4[0]/2.0)-60, 2.35*cm, 4.3*cm, 3.425*cm, fill=1,stroke=0)
		c.setFillColor(black)

		#add the actual barcode 
		c = make_ISBN_barcode(c, string.strip(ISBN_for_barcode))

		#'Price' and 'ISBN' line
		ypos = 1.5 *cm
		xpos = 2 * cm

		#price_text = price
		price_text = u"%s\n" % price.decode('UTF-8')

		if string.find(price, "rice") == -1:
			price_text = "Price %s" % price_text

		ISBN_text = ISBN_text
		if string.find(ISBN_text, "ISBN") == -1:
			ISBN_text = "ISBN  %s" % ISBN_text

		c.setFont("Gentium Basic Bold", 24)
		c.drawString(xpos, ypos, "%s" % (string.strip(price_text)))

		c.setFont("Gentium Basic Bold", 24)
		ISBN_width = stringWidth(ISBN_text, "Gentium Basic Bold", 24, "latin-1")
		xpos = A4[0]- (2.0 * cm) - ISBN_width
		c.drawString(xpos, ypos, "%s" % (string.strip(ISBN_text)))

		c.setFont("Helvetica", 10)
		ISBN_width_2 = stringWidth(ISBN_text, "Helvetica", 10, "latin-1")
		ypos = 5.25 * cm
		xpos = (A4[0]/2.0) - (ISBN_width_2/2.0)
		c.drawString(xpos, ypos, "%s" % (string.strip(ISBN_text)))


	elif cover_style == "Type 2":

		#"Type 2" =     modelled on Penguin Classics editions
		#               - black base, author in orange (CAPS), book name in white italics, colour illustration, 
		#               white bar with 'PENGUIN CLASSIC' text (black, CAPS).
		#               see sample '5ccf136d3895d2067207a8a2.jpg' (Jane Eyre)
		#				(pic here: https://sg.carousell.com/p/jane-eyre-by-charlotte-bronte-penguin-classics-literature-book-20316303/ )

		c.setFillColorRGB(0.05, 0.05, 0.05, 1)

		c.rect(0,0,A4[0],A4[1], fill=1)

		xpos = 2*cm
		ypos = A4[1] - 2.5*cm

		blurb = prettify(blurb)

		c.setFillColorRGB(background_colour[0], background_colour[1], background_colour[2], 1)

		newline2 = prettify(bookname)
		#newline2 = "%s %s" % (newline, word)

		c.setFont("Gentium Basic Bold", 24)

		newline2dwidth = stringWidth(newline2, "Gentium Basic Bold", 24, "latin-1")

		if newline2dwidth < (A4[0] - 4*cm):
			xpos = (A4[0]/2.0) - (stringWidth(newline2, "Gentium Basic Bold", 24, "latin-1")/2.0)
			c.drawString(xpos, ypos, "%s" % (string.strip(newline2)))
		else:
			newline = ""
			for word in newline2.split():
				newline2 = "%s %s" % (newline, word)
				newline2dwidth = stringWidth(newline2, "Gentium Basic Bold", 24, "latin-1")
				if newline2dwidth > (A4[0] - 4*cm):
				#if newline2dwidth > (A4[0] - 2*cm):
					xpos = (A4[0]/2.0) - (stringWidth(newline, "Gentium Basic Bold", 24, "latin-1")/2.0)
					c.drawString(xpos, ypos, "%s" % (string.strip(newline)))
					newline = "%s" % word
					ypos = ypos-20
				else:
					newline= newline2
			xpos = (A4[0]/2.0) - (stringWidth(string.strip(newline), "Gentium Basic Bold", 24, "latin-1")/2.0)
			c.drawString(xpos, ypos, "%s" % (string.strip(newline)))

		c.setFont("Gentium Basic", 16)

		ypos = ypos - 1.25*cm
		xpos = 2*cm

		for line in blurb.split("\n"):

			linewidth = stringWidth(line, "Gentium Basic", 16, "latin-1")
			c.setFont("Gentium Basic", 16)

			if linewidth < (A4[0] - 4*cm):
			#if linewidth < (A4[0] - 2*cm):
				xpos = 2*cm
				ypos = ypos - 18

				if ypos < 2*cm:
					#c.showPage()
					ypos = (A4[1] - 2 * cm)

				try:
					line=line.decode("utf-8")
					line=line.encode("latin-1","ignore")
				except:
					pass
				c.drawString(xpos, ypos, "%s" % (string.strip(line)))
			else:
				newline = ""
				for word in line.split():
					newline2 = "%s %s" % (newline, word)
					newline2dwidth = stringWidth(newline2, "Gentium Basic", 16, "latin-1")

					if newline2dwidth > (A4[0] - 4*cm):
					#if newline2dwidth > (A4[0] - 2*cm):
						c.drawString(xpos, ypos, "%s" % (string.strip(newline)))
						newline = "%s" % word
						ypos = ypos-20
					else:
						newline= newline2
				c.drawString(xpos, ypos, "%s" % (string.strip(newline)))
				if ypos < 2*cm:
					#c.showPage()

					ypos = A4[1] - 2*cm

		ypos = ypos-20

		ypos = ypos-0.05*cm

		#do critics' quotes...

		thisblurbnum = 0
	
		#try and avoid repeats...
		used_blurbs = []

		while ypos > 192:
			if DEBUG == 1:
				print
				print "--==******==--"
				print "...YPOS STILL MORE THAN 182..."
				print "--==******==--"
				print

			thisblurb = blurbwriter.do_blurb(quotechar='"', author=author,
											 characters=None, main_character=None,
											 bookname=bookname, num_blurbs=1,
											 thisblurb=thisblurbnum)

			while thisblurb in used_blurbs:
				thisblurb = blurbwriter.do_blurb(quotechar='"', author=author,
												 characters=None, main_character=None,
												 bookname=bookname, num_blurbs=1,
												 thisblurb=thisblurbnum)
			used_blurbs.append(thisblurb)

			thisblurbnum = thisblurbnum + 1

			thisblurb = prettify(thisblurb)
			if DEBUG == 1:
				print "========================="
				print "created new blurb..."
				print "thisblurb:"
				try:
					print "'%s'" % thisblurb.decode("ascii", "ignore")
				except:
					print "'%s'" % thisblurb.encode("ascii", "ignore")
				print "'ypos: %s'" % ypos
				print "========================="
			
			c.setFont("Gentium Basic", 14)
			thisblurbwidth = stringWidth(thisblurb, "Gentium Basic", 14, "latin-1")

			if string.find(thisblurb, "\n") > -1:
				if DEBUG == 1:
					print "FOUND A NEWLINE...."
					print "thisblurb:"
					try:
						print "'%s'" % thisblurb.decode("ascii", "ignore")
					except:
						print "'%s'" % thisblurb.encode("ascii", "ignore")
					print
				for line in thisblurb.split("\n"):
					line = string.strip(line)
					if line in ["", "\n", None]:
						pass
					else:
						thislinewidth = stringWidth(line, "Gentium Basic", 14, "latin-1")
						if thislinewidth < (A4[0] - 4*cm):
							#it's a short line...
							#if string.find(newline2, "(") > -1:
							if string.find(line, "(") > -1:
								if DEBUG == 1:
									print "!!! FOUND OPENING BRACKET..."
								#if string.find(newline2, ")") > -1:
								if string.find(line, ")") > -1:
									if DEBUG == 1:
										print "!!!!! FOUND CLOSING BRACKET! ..."
									#opening AND closing brackets probably mean that it's a newspaper attribution line...
									if DEBUG == 1:
										print "FOUND AN ATTRIBUTION LINE... SETTING FONT TO BOLD ITALIC..."
									c.setFont("Gentium Basic Bold Italic", 14)
									if string.find(line, "interesting") > -1:
										if DEBUG == 1:
											print '... oh, it was "interesting"... SETTING FONT TO back to BASIC...'
										c.setFont("Gentium Basic", 14)
								else:
									if DEBUG == 1:
										print "ATTRIBUTION LINE NOT FOUND... SETTING FONT TO BASIC..."
									c.setFont("Gentium Basic", 14)
							else:
								if DEBUG == 1:
									print "ATTRIBUTION LINE NOT FOUND... SETTING FONT TO BASIC..."
								c.setFont("Gentium Basic", 14)
							c.drawString(xpos, ypos, "%s" % (string.strip(line)))
						else:
							#it's a long line...
							newlineslist = []
							#with multi-line quotes, if we just add them line-by-line, the first line may be in a good
							#position, but the second or third goes under the ISBN box. Add them to a list,
							#and if it's still OK once we've checked all the lines, add the whole quote at the end...
							newline = ""
							fontset = None

							for word in line.split():
								newline2 = "%s %s" % (newline, word)
								newline2dwidth = stringWidth(newline2, "Gentium Basic", 14, "latin-1")
								if newline2dwidth > (A4[0] - 4*cm):
								#if newline2dwidth > (A4[0] - 2*cm):
									#xpos = (A4[0]/2.0) - (stringWidth(newline2, "Gentium Basic Bold", 24, "latin-1")/2.0)
									if string.find(newline2, "(") > -1:
										if string.find(newline2, ")") > -1:
											#opening AND closing brackets probably mean that it's a newspaper attribution line...
											#c.setFont("Gentium Basic Italic", 14)
											fontset = "Gentium Basic Italic"
										else:
											#c.setFont("Gentium Basic", 14)
											fontset = "Gentium Basic"
									else:
										#c.setFont("Gentium Basic", 14)
										fontset = "Gentium Basic"
									#c.drawString(xpos, ypos, "%s" % (string.strip(newline)))
									newlineslist.append([fontset, xpos, ypos, string.strip(newline)])
									newline = "%s" % word
									ypos = ypos-20
								else:
									newline= newline2
							#xpos = (A4[0]/2.0) - (stringWidth(newline2, "Gentium Basic Bold", 24, "latin-1")/2.0)

							if string.find(newline2, "(") > -1:
								if string.find(newline2, ")") > -1:
									#opening AND closing brackets probably mean that it's a newspaper attribution line...
									#c.setFont("Gentium Basic Italic", 14)
									fontset = "Gentium Basic Italic"
								else:
									#c.setFont("Gentium Basic", 14)
									fontset = "Gentium Basic"
							else:
								#c.setFont("Gentium Basic", 14)
								fontset = "Gentium Basic"

							newlineslist.append([fontset, xpos, ypos, string.strip(newline)])

							#c.setFont("Gentium Basic", 14)
							fontset = "Gentium Basic"

							#is ypos still high enough to clear the ISBN box?
							if ypos > 192:
								#I guess it is. OK, add the whole quote...
								for listybit in newlineslist:
									fontset, xpos, ypos, newline = listybit
									c.setFont(fontset, 14)
									c.drawString(xpos, ypos, newline)

						ypos = ypos-18
					
			else:

				if DEBUG == 1:
					print "NEWLINE *NOT* FOUND..."
					print "thisblurb:"
					try:
						print "'%s'" % thisblurb.decode('ascii', 'ignore')
					except:
						print "'%s'" % thisblurb.encode('ascii', 'ignore')
					print

				if thisblurbwidth < (A4[0] - 4*cm):
					#xpos = (A4[0]/2.0) - (stringWidth(newline2, "Gentium Basic Bold", 24, "latin-1")/2.0)
					c.drawString(xpos, ypos, "%s" % (string.strip(thisblurb)))
				else:
					newline = ""
					for word in thisblurb.split():
						newline2 = "%s %s" % (newline, word)
						newline2dwidth = stringWidth(newline2, "Gentium Basic", 14, "latin-1")
						if newline2 in ["", "\n", None]:
							pass
						else:
							if newline2dwidth > (A4[0] - 4*cm):
							#if newline2dwidth > (A4[0] - 2*cm):
								#xpos = (A4[0]/2.0) - (stringWidth(newline2, "Gentium Basic Bold", 24, "latin-1")/2.0)
								###c.drawString(xpos, ypos, "%s" % (string.strip(newline)))
								newline = "%s" % word
								ypos = ypos-20
							else:
								newline= newline2
					#xpos = (A4[0]/2.0) - (stringWidth(newline2, "Gentium Basic Bold", 24, "latin-1")/2.0)
					c.drawString(xpos, ypos, "%s" % (string.strip(newline)))

			try:
				blurb = u"%s\n\n%s" % (blurb, thisblurb.decode("UTF-8", 'ignore'))
			except:
				try:
					blurb = u"%s\n\n%s" % (blurb, thisblurb.encode("UTF-8", 'ignore'))
				except:
					try:
						blurb = u"%s\n\n%s" % (blurb, thisblurb.decode("ascii", 'ignore'))
					except:
						blurb = u"%s\n\n%s" % (blurb, thisblurb.encode("ascii", 'ignore'))

			if DEBUG == 1:
				print "***************"
				print "blurb (in loop)"
				try:
					print "'%s'" % blurb.decode("ascii", 'ignore')
				except:
					print "'%s'" % blurb.encode("ascii", 'ignore')
				print "***************"
				print

			ypos = ypos-20
			if DEBUG == 1:
				print
				print "--==******==--"
				print "...ENDING LOOP.... YPOS NOW %s ... " % ypos 
				print "--==******==--"
				print

		ypos = ypos-20
			
		#backing box for barcode....
		c.setFillColorRGB(243, 243, 243, 0.85)
		c.rect((A4[0]/2.0)-60, 2.35*cm, 4.3*cm, 3.425*cm, fill=1,stroke=0)
		c.setFillColorRGB(background_colour[0], background_colour[1], background_colour[2], 1)

		#add the actual barcode 
		c = make_ISBN_barcode(c, string.strip(ISBN_for_barcode))

		#'Price' and 'ISBN' line
		ypos = 1.5 *cm
		xpos = 2 * cm

		#price_text = price
		price_text = u"%s\n" % price.decode('UTF-8')

		if string.find(price, "rice") == -1:
			price_text = "Price %s" % price_text

		ISBN_text = ISBN_text
		if string.find(ISBN_text, "ISBN") == -1:
			ISBN_text = "ISBN  %s" % ISBN_text

		c.setFont("Gentium Basic Bold", 24)
		c.drawString(xpos, ypos, "%s" % (string.strip(price_text)))

		c.setFont("Gentium Basic Bold", 24)
		ISBN_width = stringWidth(ISBN_text, "Gentium Basic Bold", 24, "latin-1")
		xpos = A4[0]- (2.0 * cm) - ISBN_width
		c.drawString(xpos, ypos, "%s" % (string.strip(ISBN_text)))

		c.setFillColor(black)

		c.setFont("Helvetica", 10)
		ISBN_width_2 = stringWidth(ISBN_text, "Helvetica", 10, "latin-1")
		ypos = 5.25 * cm
		xpos = (A4[0]/2.0) - (ISBN_width_2/2.0)
		c.drawString(xpos, ypos, "%s" % (string.strip(ISBN_text)))

		c.setFillColor(black)


	elif cover_style == "Type 3":

		#"Type 3" =     modelled on Barnes and Noble Classic editions
		#               - blue bars at top and bottom, book name in white (CAPS),
		#               author name in white italics (both at top), grey bar down left
		#               see sample '9781593081386_p0_v3_s550x406.jpg' ( A Tale of Two Cities)
		#				(pic here: https://www.barnesandnoble.com/w/a-tale-of-two-cities-barnes-noble-classics-series-charles-dickens/1106017525 )

		newblue = (56, 104, 140, 1)

		c.setFillColorRGB(56/255.0, 104/255.0, 140/255.0, 1)
		c.setStrokeColorRGB(56/255.0, 104/255.0, 140/255.0, 1)
		c.rect(0,0,A4[0],A4[1], fill=1)

		xpos = 2*cm
		ypos = A4[1] - 2.5*cm

		blurb = prettify(blurb)

		newline2 = prettify(bookname)

		c.setFont("Gentium Basic Bold", 24)
		c.setFillColorRGB(0.95, 0.95, 0.95, 0.95)

		newline2dwidth = stringWidth(newline2, "Gentium Basic Bold", 24, "latin-1")

		if newline2dwidth < (A4[0] - 4*cm):
			xpos = (A4[0]/2.0) - (stringWidth(newline2, "Gentium Basic Bold", 24, "latin-1")/2.0)
			c.drawString(xpos, ypos, "%s" % (string.strip(newline2)))
		else:
			newline = ""
			for word in newline2.split():
				newline2 = "%s %s" % (newline, word)
				newline2dwidth = stringWidth(newline2, "Gentium Basic Bold", 24, "latin-1")
				if newline2dwidth > (A4[0] - 4*cm):
				#if newline2dwidth > (A4[0] - 2*cm):
					xpos = (A4[0]/2.0) - (stringWidth(newline, "Gentium Basic Bold", 24, "latin-1")/2.0)
					c.drawString(xpos, ypos, "%s" % (string.strip(newline)))
					newline = "%s" % word
					ypos = ypos-20
				else:
					newline= newline2
			xpos = (A4[0]/2.0) - (stringWidth(string.strip(newline), "Gentium Basic Bold", 24, "latin-1")/2.0)
			c.drawString(xpos, ypos, "%s" % (string.strip(newline)))

		c.setFont("Gentium Basic", 16)

		ypos = ypos - 1.25*cm
		xpos = 2*cm

		for line in blurb.split("\n"):

			linewidth = stringWidth(line, "Gentium Basic", 16, "latin-1")
			c.setFont("Gentium Basic", 16)

			if linewidth < (A4[0] - 4*cm):
			#if linewidth < (A4[0] - 2*cm):
				xpos = 2*cm
				ypos = ypos - 18

				if ypos < 2*cm:
					c.showPage()
					ypos = (A4[1] - 2 * cm)

				try:
					line=line.decode("utf-8")
					line=line.encode("latin-1","ignore")
				except:
					pass
				c.drawString(xpos, ypos, "%s" % (string.strip(line)))
			else:
				newline = ""
				for word in line.split():
					newline2 = "%s %s" % (newline, word)

					newline2dwidth = stringWidth(newline2, "Gentium Basic", 16, "latin-1")

					if newline2dwidth > (A4[0] - 4*cm):
					#if newline2dwidth > (A4[0] - 2*cm):
						c.drawString(xpos, ypos, "%s" % (string.strip(newline)))
						newline = "%s" % word
						ypos = ypos-20
					else:
						newline= newline2
				c.drawString(xpos, ypos, "%s" % (string.strip(newline)))
				if ypos < 2*cm:
					c.showPage()
					#d.pagenum = d.pagenum + 1
					ypos = A4[1] - 2*cm

		ypos = ypos-20

		ypos = ypos-0.05*cm

		#do critics' quotes...

		thisblurbnum = 0

		#try and avoid repeats...
		used_blurbs = []

		while ypos > 192:
			if DEBUG == 1:
				print
				print "--==******==--"
				print "...YPOS STILL MORE THAN 182..."
				print "--==******==--"
				print

			thisblurb = blurbwriter.do_blurb(quotechar='"', author=author, characters=None, 
											 main_character=None, bookname=bookname, num_blurbs=1,
											 thisblurb=thisblurbnum)

			while thisblurb in used_blurbs:
				thisblurb = blurbwriter.do_blurb(quotechar='"', author=author, characters=None, 
												 main_character=None, bookname=bookname, num_blurbs=1,
												 thisblurb=thisblurbnum)
			used_blurbs.append(thisblurb)

			thisblurbnum = thisblurbnum + 1

			thisblurb = prettify(thisblurb)
			if DEBUG == 1:
				print "========================="
				print "created new blurb..."
				print "thisblurb:"
				try:
					print "'%s'" % thisblurb.decode("ascii", "ignore")
				except:
					print "'%s'" % thisblurb.encode("ascii", "ignore")
				print "'ypos: %s'" % ypos
				print "========================="
			
			c.setFont("Gentium Basic", 14)
			thisblurbwidth = stringWidth(thisblurb, "Gentium Basic", 14, "latin-1")

			if string.find(thisblurb, "\n") > -1:
				if DEBUG == 1:
					print "FOUND A NEWLINE...."
					print "thisblurb:"
					try:
						print "'%s'" % thisblurb.decode("ascii", "ignore")
					except:
						print "'%s'" % thisblurb.encode("ascii", "ignore")
					print
				for line in thisblurb.split("\n"):
					line = string.strip(line)
					if line in ["", "\n", None]:
						pass
					else:
						thislinewidth = stringWidth(line, "Gentium Basic", 14, "latin-1")
						if thislinewidth < (A4[0] - 4*cm):
							#it's a short line...
							#if string.find(newline2, "(") > -1:
							if string.find(line, "(") > -1:
								if DEBUG == 1:
									print "!!! FOUND OPENING BRACKET..."
								#if string.find(newline2, ")") > -1:
								if string.find(line, ")") > -1:
									if DEBUG == 1:
										print "!!!!! FOUND CLOSING BRACKET! ..."
									#opening AND closing brackets probably mean that it's a newspaper attribution line...
									if DEBUG == 1:
										print "FOUND AN ATTRIBUTION LINE... SETTING FONT TO BOLD ITALIC..."
									c.setFont("Gentium Basic Bold Italic", 14)
									if string.find(line, "interesting") > -1:
										if DEBUG == 1:
											print '... oh, it was "interesting"... SETTING FONT TO back to BASIC...'
										c.setFont("Gentium Basic", 14)
								else:
									if DEBUG == 1:
										print "ATTRIBUTION LINE NOT FOUND... SETTING FONT TO BASIC..."
									c.setFont("Gentium Basic", 14)
							else:
								if DEBUG == 1:
									print "ATTRIBUTION LINE NOT FOUND... SETTING FONT TO BASIC..."
								c.setFont("Gentium Basic", 14)
							c.drawString(xpos, ypos, "%s" % (string.strip(line)))
						else:
							#it's a long line...
							newlineslist = []
							#with multi-line quotes, if we just add them line-by-line, the first line may be in a good
							#position, but the second or third goes under the ISBN box. Add them to a list,
							#and if it's still OK once we've checked all the lines, add the whole quote at the end...
							newline = ""
							fontset = None

							for word in line.split():
								newline2 = "%s %s" % (newline, word)
								newline2dwidth = stringWidth(newline2, "Gentium Basic", 14, "latin-1")
								if newline2dwidth > (A4[0] - 4*cm):
								#if newline2dwidth > (A4[0] - 2*cm):
									#xpos = (A4[0]/2.0) - (stringWidth(newline2, "Gentium Basic Bold", 24, "latin-1")/2.0)
									if string.find(newline2, "(") > -1:
										if string.find(newline2, ")") > -1:
											#opening AND closing brackets probably mean that it's a newspaper attribution line...
											#c.setFont("Gentium Basic Italic", 14)
											fontset = "Gentium Basic Italic"
										else:
											#c.setFont("Gentium Basic", 14)
											fontset = "Gentium Basic"
									else:
										#c.setFont("Gentium Basic", 14)
										fontset = "Gentium Basic"
									#c.drawString(xpos, ypos, "%s" % (string.strip(newline)))
									newlineslist.append([fontset, xpos, ypos, string.strip(newline)])
									newline = "%s" % word
									ypos = ypos-20
								else:
									newline= newline2
							#xpos = (A4[0]/2.0) - (stringWidth(newline2, "Gentium Basic Bold", 24, "latin-1")/2.0)

							if string.find(newline2, "(") > -1:
								if string.find(newline2, ")") > -1:
									#opening AND closing brackets probably mean that it's a newspaper attribution line...
									#c.setFont("Gentium Basic Italic", 14)
									fontset = "Gentium Basic Italic"
								else:
									#c.setFont("Gentium Basic", 14)
									fontset = "Gentium Basic"
							else:
								#c.setFont("Gentium Basic", 14)
								fontset = "Gentium Basic"

							newlineslist.append([fontset, xpos, ypos, string.strip(newline)])

							#c.setFont("Gentium Basic", 14)
							fontset = "Gentium Basic"

							#is ypos still high enough to clear the ISBN box?
							if ypos > 192:
								#I guess it is. OK, add the whole quote...
								for listybit in newlineslist:
									fontset, xpos, ypos, newline = listybit
									c.setFont(fontset, 14)
									c.drawString(xpos, ypos, newline)

						ypos = ypos-18
					
			else:

				if DEBUG == 1:
					print "NEWLINE *NOT* FOUND..."
					print "thisblurb:"
					try:
						print "'%s'" % thisblurb.decode('ascii','ignore')
					except:
						print "'%s'" % thisblurb.encode('ascii','ignore')
					print

				if thisblurbwidth < (A4[0] - 4*cm):
					#xpos = (A4[0]/2.0) - (stringWidth(newline2, "Gentium Basic Bold", 24, "latin-1")/2.0)
					c.drawString(xpos, ypos, "%s" % (string.strip(thisblurb)))
				else:
					newline = ""
					for word in thisblurb.split():
						newline2 = "%s %s" % (newline, word)
						newline2dwidth = stringWidth(newline2, "Gentium Basic", 14, "latin-1")
						if newline2 in ["", "\n", None]:
							pass
						else:
							if newline2dwidth > (A4[0] - 4*cm):
							#if newline2dwidth > (A4[0] - 2*cm):
								#xpos = (A4[0]/2.0) - (stringWidth(newline2, "Gentium Basic Bold", 24, "latin-1")/2.0)
								###c.drawString(xpos, ypos, "%s" % (string.strip(newline)))
								newline = "%s" % word
								ypos = ypos-20
							else:
								newline= newline2
					#xpos = (A4[0]/2.0) - (stringWidth(newline2, "Gentium Basic Bold", 24, "latin-1")/2.0)
					c.drawString(xpos, ypos, "%s" % (string.strip(newline)))


			blurb = "%s\n\n%s" % (blurb, thisblurb)

			if DEBUG == 1:
				print "***************"
				print "blurb (in loop)"
				try:
					print "'%s'" % blurb.decode("ascii", 'ignore')
				except:
					print "'%s'" % blurb.encode("ascii", 'ignore')
				print "***************"
				print

			ypos = ypos-20
			if DEBUG == 1:
				print
				print "--==******==--"
				print "...ENDING LOOP.... YPOS NOW %s ... " % ypos 
				print "--==******==--"
				print

		ypos = ypos-20
			
		#backing box for barcode....
		c.setFillColorRGB(243, 243, 243, 0.75)
		c.rect((A4[0]/2.0)-60, 2.35*cm, 4.3*cm, 3.425*cm, fill=1,stroke=0)
		c.setFillColor(black)

		#add the actual barcode 
		c = make_ISBN_barcode(c, string.strip(ISBN_for_barcode))

		c.setFillColorRGB(0.95, 0.95, 0.95, 0.95)

		#'Price' and 'ISBN' line
		ypos = 1.5 *cm
		xpos = 2 * cm

		#price_text = price
		price_text = u"%s\n" % price.decode('UTF-8')

		if string.find(price, "rice") == -1:
			price_text = "Price %s" % price_text

		ISBN_text = ISBN_text
		if string.find(ISBN_text, "ISBN") == -1:
			ISBN_text = "ISBN  %s" % ISBN_text

		c.setFont("Gentium Basic Bold", 24)
		c.drawString(xpos, ypos, "%s" % (string.strip(price_text)))

		c.setFont("Gentium Basic Bold", 24)
		ISBN_width = stringWidth(ISBN_text, "Gentium Basic Bold", 24, "latin-1")
		xpos = A4[0]- (2.0 * cm) - ISBN_width
		c.drawString(xpos, ypos, "%s" % (string.strip(ISBN_text)))

		c.setFillColor(black)
		c.setFont("Helvetica", 10)
		ISBN_width_2 = stringWidth(ISBN_text, "Helvetica", 10, "latin-1")
		ypos = 5.25 * cm
		xpos = (A4[0]/2.0) - (ISBN_width_2/2.0)
		c.drawString(xpos, ypos, "%s" % (string.strip(ISBN_text)))


	elif cover_style == "Type 4":
		#hacky, but saves duplicating code...
		#both back covers are black with white text.
		cover_style = "Type 2"

		make_back_cover(c=c, VERBOSE=VERBOSE, outfileName=outfileName, width=width, height=height, author=author,
						bookname=bookname, blurb=blurb, background_colour=background_colour,
						foreground_colour=foreground_colour, ISBN_text=ISBN_text, ISBN_for_barcode=ISBN_for_barcode,
						price=price, cover_style=cover_style)

	c.setFillColor(black)
	c.setFont("Gentium Basic Bold", 14)

	#if cover_style != "Type 4":
	#	c.showPage()

	return c, blurb


def make_front_cover(c, VERBOSE, outfileName, width, height, author, bookname,
					 blurb, background_colour=None, foreground_colour=None,
					 cover_style="Type 1", book_file=None):

	"Makes the front cover. Nice big picture."

	DEBUG = 0
	#DEBUG = 1

	bookname = string.strip(bookname) # are there trailing spaces that mess up our formatting?
	bookname = prettify(bookname)

	#having these capitalised looks odd...
	#Keep them in the title though.. Title Case.
	#bookname = bookname.replace(" To ", " to ")
	#bookname = bookname.replace(" Of ", " of ")
	#bookname = bookname.replace(" The ", " the ")

	newline2 = bookname
	newline2 = string.strip(newline2)
	newline2 = prettify(newline2)

	c.bookmarkPage("FrontCover")
	c.addOutlineEntry(key="FrontCover", level=1, title="Front Cover", closed=None)

	c.setFillColorRGB(background_colour[0], background_colour[1], background_colour[2])

	illustrationfn = pick_cover_pict(book_file=book_file)

	if VERBOSE == 1:
		print "\t\t\tUsing illustration :", illustrationfn

	illustration = Image.open(illustrationfn)

	if illustration.size[0] > illustration.size[1]:
		mysize = A4[0]
		wpercent = (mysize/float(illustration.size[0]))
		hsize = int((float(illustration.size[1])*float(wpercent)))
		illustration = illustration.resize((int(mysize),int(hsize)), Image.ANTIALIAS)
	else:
		mysize = A4[1]
		wpercent = (mysize/float(illustration.size[1]))
		hsize = int((float(illustration.size[0])*float(wpercent)))
		illustration = illustration.resize((int(hsize), int(mysize)), Image.ANTIALIAS)

	#resize again, to take right to the edge.
	#Because of previous resize, any distortion should be minimal.
	bleed = 50    
	illustration = illustration.resize((int(A4[0])+bleed, int(A4[1])+bleed), Image.ANTIALIAS)

# NOW DONE IN PIL - SEE BELOW...
##    c.drawInlineImage(illustration,
##                      (A4[0]/2.0 - illustration.size[0]/2.0)-(bleed/2.0),
##                      (A4[1]/2.0 - illustration.size[1]/2.0)-(bleed/2.0),
##                      width=illustration.size[0]+bleed,
##                      height=illustration.size[1]+bleed)

	newrect = Image.new("RGB",
						(int(A4[0])+bleed, int(A4[1])+bleed),
						(background_colour[0], background_colour[1],background_colour[2]))

	if cover_style == "Type 1":

		#"Type 1" =     our initial cover style
		#               coloured tint over a full page picture, white text

		#greyscale the original pic (a few are in colour - they look strange with our tint over the top)
		#ImageOps.grayscale
		illustration = ImageOps.grayscale(illustration).convert("RGB")

		newillustration = Image.blend(illustration, newrect, 0.5)

		c.drawInlineImage(newillustration,
						  (A4[0]/2.0 - newillustration.size[0]/2.0)-(bleed/2.0),
						  (A4[1]/2.0 - newillustration.size[1]/2.0)-(bleed/2.0),
						  width=newillustration.size[0]+bleed,
						  height=newillustration.size[1]+bleed)

		# do the text
		
		#do dropshadows
		shadow_increment = 3

		c.setFillColor((0.3, 0.3, 0.3, 0.5))

		#Book name (dropshadow)
		c.setFont("Gentium Basic Bold", 50)
		newline2dwidth = stringWidth(newline2, "Gentium Basic Bold", 50, "latin-1")
		xpos = ((A4[0]/2.0) - (stringWidth(newline2, "Gentium Basic Bold", 50, "latin-1")/2.0)) + shadow_increment
		ypos = (A4[1] - 4 * cm) + shadow_increment
		title_xpos = xpos
		title_ypos = ypos
		if newline2dwidth > A4[0]-(3*cm):
			n = ""
			for word in string.split(newline2):
				newline2b = "%s %s" % (n, word)
				#print "newline2b:", newline2b
				newline2bdwidth = stringWidth(newline2b, "Gentium Basic Bold", 50, "latin-1")
				if newline2bdwidth > (A4[0] - 3*cm):
					n = string.strip(n)
					xpos = (A4[0]/2.0) - (stringWidth(n, "Gentium Basic Bold", 50, "latin-1")/2.0)
					if DEBUG == 1:
						print "xpos:", xpos
						print "ypos:", ypos
						print "=====",
					c.drawString(xpos, ypos, "%s" % (string.strip(n)))
					n = "%s" % string.strip(word)
					ypos = ypos-60
				else:
					#newline2b= "%s %s" % (newline2b, n)
					n = "%s %s" % (string.strip(n), string.strip(word))
					#n = "%s %s" % (n, word)
			#ypos = ypos-32
			xpos = (A4[0]/2.0) - (stringWidth("%s" % (string.strip(n)), "Gentium Basic Bold", 50, "latin-1")/2.0)
			c.drawString(xpos, ypos, "%s" % (string.strip(n)))
		else:
			xpos = ((A4[0]/2.0) - (stringWidth(newline2, "Gentium Basic Bold", 50, "latin-1")/2.0)) + shadow_increment
			ypos = (A4[1] - 4 * cm) - shadow_increment
			c.drawString(xpos, ypos, "%s" % (string.strip(newline2)))

		# author's name at bottom of page (dropshadow)
		newline3 = author
		newline3 = string.strip(newline3)
		newline3 = prettify(newline3)

		c.setFont("Gentium Basic Bold", 32)
		newline2dwidth = stringWidth(newline2, "Gentium Basic Bold", 32, "latin-1")
		xpos = ((A4[0]/2.0) - (stringWidth(newline3, "Gentium Basic Bold", 32, "latin-1")/2.0)) + (shadow_increment-1)
		ypos = (3 * cm)  + (shadow_increment-1)
		c.drawString(xpos, ypos, "%s" % (string.strip(newline3)))

		#book title (white text)

		c.setFillColor(white)

		c.setFont("Gentium Basic Bold", 50)
		newline2dwidth = stringWidth(newline2, "Gentium Basic Bold", 50, "latin-1")

		xpos = title_xpos + shadow_increment
		ypos = title_ypos - shadow_increment
		if newline2dwidth > A4[0]-(3*cm):
			n = ""
			for word in string.split(newline2):
				newline2b = "%s %s" % (n, word)
				#print "newline2b:", newline2b
				newline2bdwidth = stringWidth(newline2b, "Gentium Basic Bold", 50, "latin-1")
				#print "newline2bdwidth:", newline2bdwidth
				if newline2bdwidth > (A4[0] - 3*cm):
					n = string.strip(n)
					xpos = (A4[0]/2.0) - (stringWidth(n, "Gentium Basic Bold", 50, "latin-1")/2.0)
					if DEBUG ==1:
						print "xpos:", xpos
						print "ypos:", ypos
						print "=====",
					#c.drawString(xpos, ypos, "%s" % (string.strip(newline2b)))
					c.drawString(xpos, ypos, "%s" % (string.strip(n)))
					n = "%s" % string.strip(word)
					ypos = ypos-60
				else:
					#n = "%s %s" % (n, word)
					n = "%s %s" % (string.strip(n), string.strip(word))
			xpos = (A4[0]/2.0) - (stringWidth("%s" % (string.strip(n)), "Gentium Basic Bold", 50, "latin-1")/2.0)
			c.drawString(xpos, ypos, "%s" % (string.strip(n)))
		else:
			xpos = (A4[0]/2.0) - (stringWidth(newline2, "Gentium Basic Bold", 50, "latin-1")/2.0)
			ypos = (A4[1] - 4 * cm)
			c.drawString(xpos, ypos, "%s" % (string.strip(newline2)))

		# author's name at bottom of page (white text)
		newline3 = author
		newline3 = string.strip(newline3)
		newline3 = prettify(newline3)

		c.setFont("Gentium Basic Bold", 32)
		newline2dwidth = stringWidth(newline2, "Gentium Basic Bold", 32, "latin-1")
		xpos = (A4[0]/2.0) - (stringWidth(newline3, "Gentium Basic Bold", 32, "latin-1")/2.0)
		#ypos = (A4[1] - 3 * cm)
		ypos = 3 * cm
		c.drawString(xpos, ypos, "%s" % (string.strip(newline3)))

		#do the decorative frame
		shadow_increment = int(shadow_increment/2)
		c.setStrokeColor((0.3, 0.3, 0.3, 0.6))
		c.setFillColor((0.3, 0.3, 0.3, 0.6))
		c.rect(1.5*cm + shadow_increment,
			   1.5*cm - shadow_increment,
			   A4[0]-(3*cm),
			   A4[1]-(3*cm),
			   fill=0)
		c.setStrokeColor((0.6, 0.6, 0.6, 0.9))
		c.setFillColor((0.6, 0.6, 0.6, 0.9))
		#c.setStrokeColor(white)
		c.rect(1.5*cm + (2 * shadow_increment),
			   1.5*cm + (shadow_increment),
			   A4[0] - (3*cm) - (2 * shadow_increment),
			   A4[1] - (3*cm) - (1 * shadow_increment),
			   fill=0)

	elif cover_style == "Type 2":

		#"Type 2" =     modelled on Penguin Classics editions
		#               - black base, author in orange (CAPS), book name in white italics, colour illustration, 
		#               white bar with 'PENGUIN CLASSIC' text (black, CAPS).
		#               see sample '5ccf136d3895d2067207a8a2.jpg' (Jane Eyre)
		#				(pic here: https://sg.carousell.com/p/jane-eyre-by-charlotte-bronte-penguin-classics-literature-book-20316303/ )

		newillustration = illustration # increase the contrast???

		c.drawInlineImage(newillustration,
						  (A4[0]/2.0 - newillustration.size[0]/2.0),
						  (A4[1]/2.0 - newillustration.size[1]/2.0)+(bleed),
						  width=newillustration.size[0],
						  height=newillustration.size[1])

		c.setFillColor((0.05, 0.05, 0.05, 1))

		#black rectangle
		c.setFillColorRGB(0.05, 0.05, 0.05, 1)
		c.rect(0,
			   0,
			   (A4[0]),
			   int(A4[1]/4.0),
			   fill=1)

		#white bar
		c.setStrokeColorRGB(0.97, 0.95, 0.95, 1)
		c.setFillColorRGB(0.97, 0.95, 0.95, 1)
		c.rect(0,
			   int(A4[1]/4.0),
			   (A4[0]),
			   int(A4[1]/20.0),
			   fill=1)

		c.setFont("Gentium Basic Bold", 50)
		newline2dwidth = stringWidth(newline2, "Gentium Basic Bold", 50, "latin-1")
		xpos = ((A4[0]/2.0) - (stringWidth(newline2, "Gentium Basic Bold", 50, "latin-1")/2.0))
		ypos = (A4[1] - 4 * cm)
		title_xpos = xpos
		title_ypos = ypos

		#book title (white text)

		c.setFillColor(white)

		newline2 = bookname
		newline2 = string.strip(newline2)
		newline2 = prettify(newline2)
		
		c.setFont("Gentium Basic Italic", 32)
		newline2dwidth = stringWidth(newline2, "Gentium Basic Italic", 32, "latin-1")

		xpos = title_xpos
		ypos = 2.75*cm
		if newline2dwidth > A4[0]-(3*cm):
			n = ""
			for word in string.split(newline2):
				newline2b = "%s %s" % (n, word)
				#print "newline2b:", newline2b
				newline2bdwidth = stringWidth(newline2b, "Gentium Basic Italic", 32, "latin-1")
				if newline2bdwidth > (A4[0] - 3*cm):
					n = string.strip(n)
					xpos = (A4[0]/2.0) - (stringWidth(n, "Gentium Basic Italic", 32, "latin-1")/2.0)
					if DEBUG ==1:
						print "xpos:", xpos
						print "ypos:", ypos
						print "=====",
					#c.drawString(xpos, ypos, "%s" % (string.strip(newline2b)))
					c.drawString(xpos, ypos, "%s" % (string.strip(n)))
					n = "%s" % string.strip(word)
					ypos = ypos-40
				else:
					#n = "%s %s" % (n, word)
					n = "%s %s" % (string.strip(n), string.strip(word))
			xpos = (A4[0]/2.0) - (stringWidth("%s" % (string.strip(n)), "Gentium Basic Italic", 32, "latin-1")/2.0)
			c.drawString(xpos, ypos, "%s" % (string.strip(n)))
		else:
			xpos = (A4[0]/2.0) - (stringWidth(newline2, "Gentium Basic Italic", 32, "latin-1")/2.0)
			ypos = 2.75 * cm
			c.drawString(xpos, ypos, "%s" % (string.strip(newline2)))

		# author's name, above book title (orange text)
		newline3 = string.upper(author)
		newline3 = string.strip(newline3)
		newline3 = prettify(newline3)

		c.setFillColor(orange)
		c.setFont("Gill Sans Nova Bold", 32)
		newline2dwidth = stringWidth(newline2, "Gill Sans Nova Bold", 32, "latin-1")
		xpos = (A4[0]/2.0) - (stringWidth(newline3, "Gill Sans Nova Bold", 32, "latin-1")/2.0)
		ypos = 4.75 * cm
		c.drawString(xpos, ypos, "%s" % (string.strip(newline3)))

		c.setFillColor(black)


	elif cover_style == "Type 3":

		#"Type 3" =     modelled on Barnes and Noble Classic editions
		#               - blue bars at top and bottom, book name in white (CAPS),
		#               author name in white italics (both at top), grey bar down left
		#               see sample '9781593081386_p0_v3_s550x406.jpg' ( A Tale of Two Cities)
		#				(pic here: https://www.barnesandnoble.com/w/a-tale-of-two-cities-barnes-noble-classics-series-charles-dickens/1106017525 )

		newblue = (56, 104, 140, 1)

		newillustration = illustration # increase the contrast???

		c.drawInlineImage(newillustration,
						  (A4[0]/2.0 - newillustration.size[0]/2.0),
						  (A4[1]/2.0 - newillustration.size[1]/2.0)+(bleed),
						  width=newillustration.size[0],
						  height=newillustration.size[1])

		#lower blue rectangle
		c.setFillColor((56/255.0, 104/255.0, 140/255.0), 1)
		c.setStrokeColor((56/255.0, 104/255.0, 140/255.0), 0)
		c.rect(-50,
			   -10,
			   A4[0]+100,
			   A4[1]/10.0,
			   fill=1)

		#upper blue rectangle
		c.setFillColor((56/255.0, 104/255.0, 140/255.0), 1)
		c.rect(-1,
			   A4[1] - (A4[1]/4.0),
			   A4[0]+50,
			   A4[1]+50,
			   fill=1)

		#left grey rectangle
		c.setFillColorRGB(100, 100, 100, 0.35)
		c.setStrokeColorRGB(100, 100, 100, 0.35)
		c.rect(0,
			   0,
			   int(A4[0]/6.0),
			   A4[1],
			   fill=1)

		c.setFont("Gentium Basic Bold", 50)
		newline2dwidth = stringWidth(newline2, "Gentium Basic Bold", 50, "latin-1")
		xpos = ((A4[0]/2.0) - (stringWidth(newline2, "Gentium Basic Bold", 50, "latin-1")/2.0))
		xpos = xpos + (3 * cm)
		#ypos = int(A4[1] - (2 * cm))
		ypos = int(A4[1] - (2.4 * cm))
		title_xpos = xpos
		title_ypos = ypos

		#book title (white text)
		c.setFillColor(white)

		#newline2 = bookname
		n = string.split(bookname, " ")
		for w in range(0,len(n)):
			if len(n[w]) >3:
				n[w]=string.upper(n[w])
			elif w in ("i", "I"):
				n[w]="I"
			else:
				n[w]=string.lower(n[w])
		newline2 = string.join(n, " ")
		newline2 = string.strip(newline2)
		newline2 = prettify(newline2)
		if newline2[0] != string.upper(newline2[0]):
			newline2 = u"%s%s" % (string.upper(newline2[0]), newline2[1:])

		c.setFont("Gentium Basic Bold", 32)
		newline2dwidth = stringWidth(newline2, "Gentium Basic Bold", 32, "latin-1")

		xpos = title_xpos
		if newline2dwidth > A4[0]-(4*cm):
			n = ""
			for word in string.split(newline2):
				newline2b = "%s %s" % (n, word)
				#print "newline2b:", newline2b
				newline2bdwidth = stringWidth(newline2b, "Gentium Basic Bold", 32, "latin-1")
				if newline2bdwidth > (A4[0] - 6*cm):
					n = string.strip(n)
					xpos = (A4[0]/2.0) - (stringWidth(n, "Gentium Basic Bold", 32, "latin-1")/2.0)
					xpos = xpos + (2 * cm)
					if DEBUG ==1:
						print "xpos:", xpos
						print "ypos:", ypos
						print "=====",
					#c.drawString(xpos, ypos, "%s" % (string.strip(newline2b)))
					c.drawString(xpos, ypos, "%s" % (string.strip(n)))
					n = "%s" % string.strip(word)
					ypos = ypos-40
				else:
					#n = "%s %s" % (n, word)
					n = "%s %s" % (string.strip(n), string.strip(word))
			xpos = (A4[0]/2.0) - (stringWidth("%s" % (string.strip(n)), "Gentium Basic Bold", 32, "latin-1")/2.0)
			xpos = xpos + (2 * cm)
			c.drawString(xpos, ypos, "%s" % (string.strip(n)))
		else:
			xpos = (A4[0]/2.0) - (stringWidth(newline2, "Gentium Basic Bold", 32, "latin-1")/2.0)
			xpos = xpos + (2 * cm)
			ypos = int(A4[1] - (2.5 * cm))
			c.drawString(xpos, ypos, "%s" % (string.strip(newline2)))

		# author's name, below book title (white text)
		newline3 = author
		newline3 = string.strip(newline3)
		newline3 = prettify(newline3)

		c.setFont("Gentium Basic", 32)
		newline2dwidth = stringWidth(newline2, "Gentium Basic", 32, "latin-1")
		xpos = (A4[0]/2.0) - (stringWidth(newline3, "Gentium Basic", 32, "latin-1")/2.0)
		xpos = xpos + (2 * cm)

		ypos = ypos - 50
		c.drawString(xpos, ypos, "%s" % (string.strip(newline3)))

		c.setFillColor(black)
		c.setStrokeColor(black)

		c.rect((1.5 * cm), A4[1]-(6.5*cm),
			   A4[0], 6*cm,
			   fill=0)
		c.rect((1.6 * cm), A4[1]-(6.4*cm),
			   A4[0], 5.8*cm,
			   fill=0)


	elif cover_style == "Type 4":

		#"Type 4" =     modelled on Wordsworth Classics editions
		#               - black base, Title in white text, author's name
		#               in white text (CAPS) below it. Colour illustration, white outline.
		#               see sample '9781840227567.jpg' ( A Christmas Carol)
		#				(pic here: https://wordsworth-editions.com/collections/classics/christmas-carol-(adult-edition) ) 

		if illustration.size[0] > illustration.size[1]:
			mysize = int(A4[0]-(4*cm))
			wpercent = (mysize/float(illustration.size[0]))
			hsize = int((float(illustration.size[1])*float(wpercent)))
			illustration = illustration.resize((int(mysize),int(hsize)), Image.ANTIALIAS)
			neww = int(mysize)
			newh = int(hsize)
		else:
			mysize = int(A4[1]-(12*cm))
			wpercent = (mysize/float(illustration.size[1]))
			hsize = int((float(illustration.size[0])*float(wpercent)))
			illustration = illustration.resize((int(hsize), int(mysize)), Image.ANTIALIAS)
			neww = int(hsize)
			newh = int(mysize)

		newillustration = illustration # increase the contrast???

		c.setFillColorRGB(0.05, 0.05, 0.05, 1)
		c.rect(0,
			   0,
			   A4[0],
			   A4[1],
			   fill=1)

		c.drawInlineImage(newillustration,
						  (A4[0]/2.0) - (int(hsize)/2.0),
						  1.5*cm,
						  #(3 * cm),
						  width=neww,
						  height=newh)

		c.setFillColorRGB(0.95, 0.55, 0.55, 1)
		c.rect((A4[0]-(1.5*cm)),
			   (A4[1]-(3*cm)),
			   width=neww,
			   height=newh,
			   fill=0)
		c.rect((A4[0]-(1.51*cm)),
			   (A4[1]-(3.01*cm)),
			   width=neww,
			   height=newh,
			   fill=0)

		# do the text

		c.setFillColor((0.05, 0.05, 0.05, 1))

		c.setFont("Gentium Basic Bold", 50)
		newline2dwidth = stringWidth(newline2, "Gentium Basic Bold", 50, "latin-1")
		xpos = ((A4[0]/2.0) - (stringWidth(newline2, "Gentium Basic Bold", 50, "latin-1")/2.0))
		ypos = (A4[1] - 4 * cm)
		title_xpos = xpos
		title_ypos = ypos

		#book title (white text)

		c.setFillColor(white)

		newline2 = string.capwords(bookname)
		newline2 = string.strip(newline2)
		newline2 = prettify(newline2)
		
		#c.setFont("Gentium Basic Italic", 32)
		c.setFont("Gentium Basic Bold", 50)
		newline2dwidth = stringWidth(newline2, "Gentium Basic Bold", 50, "latin-1")

		xpos = title_xpos
		#ypos = 2.75*cm
		ypos = A4[1] - (2.75 * cm)
		if newline2dwidth > A4[0]-(3*cm):
			n = ""
			for word in string.split(newline2):
				newline2b = "%s %s" % (n, word)
				#newline2bdwidth = stringWidth(newline2b, "Gentium Basic Italic", 32, "latin-1")
				newline2bdwidth = stringWidth(newline2b, "Gentium Basic Bold", 50, "latin-1")
				if newline2bdwidth > (A4[0] - 3*cm):
					n = string.strip(n)
					xpos = (A4[0]/2.0) - (stringWidth(n, "Gentium Basic Bold", 50, "latin-1")/2.0)
					if DEBUG ==1:
						print "xpos:", xpos
						print "ypos:", ypos
						print "=====",
					c.drawString(xpos, ypos, "%s" % (string.strip(n)))
					n = "%s" % string.strip(word)
					#ypos = ypos-40
					ypos = ypos-60
				else:
					#newline2b= "%s %s" % (newline2b, n)
					#n = "%s %s" % (n, word)
					n = "%s %s" % (string.strip(n), string.strip(word))
			#xpos = (A4[0]/2.0) - (stringWidth("%s" % (string.strip(n)), "Gentium Basic Italic", 32, "latin-1")/2.0)
			xpos = (A4[0]/2.0) - (stringWidth("%s" % (string.strip(n)), "Gentium Basic Bold", 50, "latin-1")/2.0)
			c.drawString(xpos, ypos, "%s" % (string.strip(n)))
		else:
			#xpos = (A4[0]/2.0) - (stringWidth(newline2, "Gentium Basic Italic", 32, "latin-1")/2.0)
			xpos = (A4[0]/2.0) - (stringWidth(newline2, "Gentium Basic Bold", 50, "latin-1")/2.0)
			#ypos = 2.75 * cm
			ypos = A4[1] - (2.75 * cm)
			c.drawString(xpos, ypos, "%s" % (string.strip(newline2)))

		# author's name, above book title (white text)
		newline3 = string.upper(author)
		newline3 = string.strip(newline3)
		newline3 = prettify(newline3)

		ypos = ypos - 60
		c.setFont("Gentium Basic Bold", 32)
		newline2dwidth = stringWidth(newline2, "Gentium Basic Bold", 32, "latin-1")
		xpos = (A4[0]/2.0) - (stringWidth(newline3, "Gentium Basic Bold", 32, "latin-1")/2.0)
		c.drawString(xpos, ypos, "%s" % (string.strip(newline3)))

		c.setFillColor(black)

	c.showPage()
	return c


def write_page_to_disk(outfileName, text, pagewidth=80, VERBOSE=0):
	"save an ascii version to a text file"

	outfile = open(outfileName, "a")

	newline = ""
	if text not in (None, ""):
		for line in text.split("\n"):
			if len(line) < pagewidth:
				try:
					outfile.write("%s\n" % line.decode("UTF-8", "ignore"))
				except:
					try:
						outfile.write("%s\n" % line.encode("UTF-8", "ignore"))
					except:
						outfile.write("%s\n" % line.decode("ascii", "ignore"))
			else:
				newline = ""
				for word in text.split(" "):
					newline2 = "%s %s" % (newline, word)
					newline2dwidth = len(newline2)
					if newline2dwidth > pagewidth:
						try:
							outfile.write(u"%s\n" % newline.decode('ascii', 'ignore'))
						except:
							outfile.write(u"%s\n" % newline.encode('ascii', 'ignore'))
						newline = "%s" % word
					else:
						newline= newline2
				try:
					outfile.write(u"%s\n" % string.strip(newline.decode("UTF-8", "ignore")))
				except:
					try:
						outfile.write(u"%s\n" % string.strip(newline.encode("UTF-8", "ignore")))
					except:
						try:
							outfile.write("%s\n" % newline.decode('ascii', 'ignore'))
						except:
							outfile.write("%s\n" % newline.encode('ascii', 'ignore'))
	if VERBOSE == 1:
		print "... wrote to '%s'..." % (outfileName)
	outfile.close()


def make_text_front_cover(c, VERBOSE, outfileName, width, height, author, bookname,
						  blurb, background_colour=None, foreground_colour=None):
	#DEBUG = 1
	DEBUG = 0

	startdir = os.getcwd()

	if DEBUG == 1:
		outdir = os.path.join(startdir, "TEMP")
	else:
		if os.path.isdir(os.path.join(startdir, "OUTPUT")):
			outdir = os.path.join(startdir, "OUTPUT")
		else:
			outdir = os.getcwd()

	if outfileName in (None, ""):
		fn_root = "TEST_COVERS_OUTPUT"
	else:
		fn_root = str(string.split(outfileName, ".")[0])

##	if os.path.isfile(os.path.join(outdir, "%s.txt" % fn_root)):
##		if os.path.isfile(os.path.join(outdir, "%s_OLD.txt" % fn_root)):
##			new_fname = "%s_OLD_%s.txt" % (fn_root, "%06d" % random.choice(range(0,99999)))
##		else:
##			new_fname = "%s_OLD.txt" % fn_root
##		os.rename(os.path.join(outdir, "%s.txt" % fn_root),
##				  os.path.join(outdir, new_fname))

	outfile = open(os.path.join(outdir, "%s.txt" % fn_root), "w")

	seperator = "="*20

	outfile.write(seperator)
	outfile.write("\n[FRONT COVER]\n\n")
	outfile.write("\n%s\n" % string.upper(bookname))
	outfile.write("\nby\n")
	outfile.write("\n%s\n\n" % author)
	outfile.write(seperator)

	outfile.close()
	if VERBOSE == 1:
#		print "\t\twrote text version of front cover to file '%s'" % os.path.join(outdir, "%s.txt" % outfileName)
		print "\t\twrote text version of front cover to file '%s'" % os.path.join(outdir, outfileName)


def make_text_back_cover_final_twiddles(VERBOSE=1, outfileName=None, price="£4.99", ISBN="0 9999999999999",
										pagewidth=80):

	#DEBUG = 1
	DEBUG = 0

	#have you forgotten to supply a filename? Pillock!
	#Might as well pipe it to /dev/null.
	#Oh well, give it a filename for debugging later...
	if outfileName == None:
		outfileName = "text_back_cover_final_twiddles"

	startdir = os.getcwd()

	if DEBUG == 1:
		outdir = os.path.join(startdir, "TEMP")
	else:
		if os.path.isdir(os.path.join(startdir, "OUTPUT")):
			outdir = os.path.join(startdir, "OUTPUT")
		else:
			outdir = startdir

	outfile = open(os.path.join(outdir, outfileName), "a")

	seperator = "="*20

	if price[0] not in ["$", "£"]:
		price = "£%s" % price
	if string.find(price, ".") == -1:
		price = "%s.99" % price
	if string.find(price, "Price") == -1:
		price = "Price: %s" % price

	if string.find(ISBN, "ISBN") == -1:
		ISBN = "ISBN %s" % ISBN
	num_spaces = pagewidth - (len(price) + len(ISBN))
	spaces_spaces = " " * num_spaces

	#might want to swap these round later?
	#ie have it random as to whether the price or ISBN appears first on the line?
	final_line = "%s%s%s" % (price, spaces_spaces, ISBN)
	outfile.write("\n%s\n\n" % final_line)

	outfile.write(seperator)
	outfile.write("\n\n[END]\n")


def make_text_back_cover(c, VERBOSE, outfileName, width, height, author, bookname,
						 blurb, background_colour=None, foreground_colour=None,
						 price="£4.99", ISBN="0 9999999999999"):
	#DEBUG = 1
	DEBUG = 0

	startdir = os.getcwd()

	if DEBUG == 1:
		outdir = os.path.join(startdir, "TEMP")
	else:
		if os.path.isdir(os.path.join(startdir, "OUTPUT")):
			outdir = os.path.join(startdir, "OUTPUT")
		else:
			outdir = os.getcwd()

	if outfileName == None:
		fn_root = "TEST_COVERS_OUTPUT"
	else:
		fn_root = string.split(outfileName, ".")[0]

	#assume we've aleady renamed any text file with the front cover
##	if os.path.isfile(os.path.join(outdir, "%s.txt" % fn_root)):
##		if os.path.isfile(os.path.join(outdir, "%s_OLD.txt" % fn_root)):
##			new_fname = "%s_OLD_%s.txt" % (fn_root, "%06d" % random.choice(range(0,99999)))
##		else:
##			new_fname = "%s_OLD.txt" % fn_root
##		os.rename(os.path.join(outdir, "%s.txt" % fn_root),
##				  os.path.join(outdir, new_fname))

	outfile = open(os.path.join(outdir, "%s.txt" % fn_root), "a")

	seperator = "="*20
	seperator = "%s\n\n" % seperator

	#outfile.write(seperator)
	###outfile.write("\n\n[BACK COVER]\n")
	#outfile.write(seperator)

	back_cover_text = "\n%s\n\n%s\n" % (string.upper(bookname), blurb)
	if VERBOSE > 1:
		print "back_cover_text:"
		print back_cover_text
##	write_page_to_disk(outfileName=os.path.join(outdir, "%s.txt" % fn_root),
##					   text=back_cover_text,
##					   pagewidth=80,
##					   VERBOSE=1)

	#outfile.write("\n%s\n" % string.upper(bookname))
	#outfile.write("\n%s\n\n" % string.upper(bookname))
	#outfile.write("\n%s\n" % blurb)

	#outfile.write(seperator)

	write_page_to_disk(outfileName=os.path.join(outdir, "%s.txt" % fn_root),
					   text=back_cover_text,
					   pagewidth=80,
					   VERBOSE=1)


	#sort out price and ISBN...
	make_text_back_cover_final_twiddles(VERBOSE=1, outfileName="%s.txt" % fn_root,
										price=price, ISBN=ISBN,
										pagewidth=80)

	outfile.close()
	if VERBOSE == 1:
		print "\t\twrote text version of back cover to file '%s'" % os.path.join(outdir, "%s.txt" % fn_root)


def pick_colour():

	#keys = heraldic_cols.keys()
	#thiskey = random.choice(keys)

	#Hard coded as a list rather than using the keys() method to weed out the ones that look rubbish in practie.
	psskeys = ["Murrey", "Murrey", "Tenné", "Or", "Gules", "Azure", "Vert", "Purpure"]
	thiskey = random.choice(psskeys)

	background_colour = heraldic_cols[thiskey]

	return background_colour


def pick_cover_pict(book_file=None):
	"""randomly select a picture to use for the front cover.

If we pass in a filename with the 'book_file' argument, will attempt
to find an image file using the beginning of that filename (will still
pick a random image if it fals).

"""

	this_dir= os.getcwd()

	if os.path.isdir(os.path.join(this_dir, "images", "illustrations")):
		pic_dir = os.path.join(this_dir, "images", "illustrations")

	os.chdir(pic_dir)
	if book_file != None:
		#do something clever here to pickan illustration from that book...
		if string.find(book_file, "-") > -1:
			prefix, suffix = string.split(book_file, "-", maxsplit=1)
		elif string.find(book_file, "-") > -1:
			prefix, suffix = string.split(book_file, ".", maxsplit=1)
		else:
			#give up!
			prefix = "*"
		if prefix != "*":
			prefix = "%s*" % prefix
		#print "prefix:\t '%s'" % prefix
		pattern = "%s.*" % prefix

		pics = glob.glob(pattern)

		#still found nothing... oh well.
		if pics == []:
			pics = glob.glob("*.*")
			
	else:
		pics = glob.glob("*.*")

	#pics that have shown up in testing and aren't really suitable for front cover use...
	exceptions = []

	for p in exceptions:
		buildingpics.remove(p)

	pic_to_use = random.choice(pics)
	pic_to_use = os.path.join(pic_dir, pic_to_use)



	os.chdir(this_dir)

	return pic_to_use


def get_cover_style():
	"""picks a cover style to use. Returns a string."""

	#"Type 1" =     our initial cover style
	#               coloured tint over a full page picture, white text

	#"Type 2" =     modelled on Penguin Classics editions
	#               - black base, author in orange (CAPS), book name in white italics, colour illustration, 
	#               white bar with 'PENGUIN CLASSIC' text (black, CAPS).
	#               see sample '5ccf136d3895d2067207a8a2.jpg' (Jane Eyre)

	#"Type 3" =     modelled on Barnes and Noble Classic editions
	#               - blue bars at top and bottom, book name in white (CAPS),
	#               author name in white italics (both at top), grey bar down left
	#               see sample '9781593081386_p0_v3_s550x406.jpg' ( A Tale of Two Cities)

	#"Type 4" =     modelled on Wordsworth Classics editions
	#               - black base, Title in white text, author's name
	#               in white text (CAPS) below it. Colour illustration, white outline.
	#               see sample '9781840227567.jpg' ( A Christmas Carol)

	poss_cover_styles = ["Type 1", "Type 1", "Type 2", "Type 3", "Type 4"] # make Type 1 more likely - I like it :)
	cover_style= random.choice(poss_cover_styles)

	return cover_style


def getCovers(c, VERBOSE, outfileName, width, height, author, bookname, blurb):

	DEBUG = 0
	#DEBUG = 1
	
	background_colour = pick_colour()

	if DEBUG == 1:
		print "===="
		print "background_colour (FIRST PICK):"
		print background_colour
		print 'background_colour["Name"]:'
		print background_colour["Name"]
		print "===="

	if VERBOSE == 1:
		print "\tcreating front cover..."
		#print "\t\tbackground_colour:", background_colour

	foreground_colour = pick_colour()

	cover_pic = pick_cover_pict(book_file=book_file)

	#print cover_pic

	#while background_colour == foreground_colour:
	#    foreground_colour = pick_colour()
	#print "background_colour:", background_colour
	#print "foreground_colour:", foreground_colour

	cover_style = get_cover_style()

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


	if VERBOSE == 1:
		print "\tcreating front cover..."
	c = make_front_cover(c, VERBOSE, outfileName, width, height, author, bookname,
						 blurb, background_colour=back, foreground_colour=fore,
						 cover_style=cover_style)

	make_text_front_cover(c, VERBOSE, outfileName, width, height, author, bookname,
						  blurb, background_colour=None, foreground_colour=None)

	if VERBOSE >1:
		print blurb

	if VERBOSE == 1:
		print "\t\tGenerating ISBN..."
	ISBN = make_ISBN(spacer="-")
	ISBN_for_barcode = string.strip(string.replace(string.replace(ISBN, "-", "")," ", ""))
	if VERBOSE == 1:
		print "\t\t\tISBN: '%s'" % ISBN
		print "\t\t\tISBN_for_barcode: '%s'" % ISBN_for_barcode

	price = random.choice(range(3,12))
	price = "£%s.99" % price
	if VERBOSE == 1:
		print "\t\t\tprice: '%s'" % price
		print
	
	if VERBOSE == 1:
		print "\n\tcreating back cover..."

	c, blurb = make_back_cover(c, VERBOSE, outfileName, width, height, author, bookname,
							   blurb, background_colour=back, foreground_colour=fore,
							   ISBN_text=ISBN, ISBN_for_barcode=ISBN_for_barcode, price=price,
							   cover_style=cover_style)

	make_text_back_cover(c, VERBOSE, outfileName, width, height, author, bookname,
						 blurb, background_colour=None, foreground_colour=None, ISBN=ISBN, price=price)

	c.save()

	if VERBOSE == 1:
		print "\twrote file '%s'" % outfileName
		print "DONE"

	return ISBN



def run(c, VERBOSE, outfileName, width, height, author, bookname, blurb, cover_style=None,
		book_file=None, dickens_book = None):

	DEBUG = 0
	#DEBUG = 1

	if cover_style == None:
		cover_style = get_cover_style()

	if VERBOSE == 1:
		print "\t\tcover_style:", cover_style

	foreground_colour = pick_colour()
	background_colour = pick_colour()

	if DEBUG == 1:
		print "===="
		print "background_colour:"
		print background_colour
		print 'background_colour["Name"]:'
		print background_colour["Name"]
		print "===="

	if VERBOSE == 1:
		print "\n\tcreating front cover..."
		#print "\t\tbackground_colour:", background_colour

	cover_pic = pick_cover_pict(book_file=book_file)
	print cover_pic

	#while background_colour == foreground_colour:
	#    foreground_colour = pick_colour()

	#back = background_colour["RGB Colour"]
	#fore = foreground_colour["RGB Colour"]

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


	if VERBOSE == 1:
		print "\tcreating front cover..."

	c = make_front_cover(c, VERBOSE, outfileName, width, height, author, bookname,
						 blurb, background_colour=back, foreground_colour=fore,
						 cover_style=cover_style, book_file=book_file)

	make_text_front_cover(c, VERBOSE, outfileName, width, height, author, bookname,
					 blurb, background_colour=None, foreground_colour=None)

	if VERBOSE >1:
		print blurb

	if VERBOSE == 1:
		print "\tGenerating ISBN..."

	ISBN = make_ISBN(spacer="-")
	ISBN_for_barcode = string.strip(string.replace(string.replace(ISBN, "-", "")," ", ""))

	if VERBOSE == 1:
		print "\t\tISBN: '%s'" % ISBN
		print "\t\tISBN_for_barcode: '%s'" % ISBN_for_barcode

	price = random.choice(range(3,12))
	price = "£%s.99" % price
	if VERBOSE == 1:
		print "\t\tprice: '%s'" % price
		print
	
	if VERBOSE == 1:
		print "\n\tcreating back cover..."
	c, blurb  = make_back_cover(c, VERBOSE, outfileName, width, height, author, bookname,
								blurb, background_colour=back, foreground_colour=fore,
								ISBN_text=ISBN, ISBN_for_barcode=ISBN_for_barcode, price=price,
								cover_style=cover_style, dickens_book = dickens_book)

	make_text_back_cover(c, VERBOSE, outfileName, width, height, author, bookname,
						 blurb, background_colour=None, foreground_colour=None, ISBN=ISBN, price=price)

	c.save()

	if VERBOSE == 1:
		print "\twrote file '%s'" % outfileName
	print "DONE"


if __name__ == "__main__":
	import main
	main.registerFonts(VERBOSE=1)

	thisdir=os.getcwd()
	if os.path.isdir(os.path.join(thisdir, "TEMP")):
		OUTPUTDIR = os.path.join(thisdir, "TEMP")
	else:
		OUTPUTDIR = thisdir

	for s in POSS_COVER_STYLES:
		outfileName = "covers-test-%s.pdf" % (string.upper(string.replace(s, " ", "-")))
		 
		author = names.getName()

		bookname, is_eponymous, old_eponymous_character, new_eponymous_character = main.make_title()

		bookname = string.capwords(string.strip(bookname))

		#use for testing...
		#bookname = "WHAT THE DICKENS"
		#bookname = "A Young Ladies Guide to the County of Wychshire"
		#bookname = "THIS BOOK IS A GREAT BIG PILE OF POO AND I HATE IT"

		blurb = blurbwriter.make_content_summary(author=author, characters=None, main_character=None, title=bookname)


		c = canvas.Canvas(os.path.join(OUTPUTDIR, outfileName), pagesize=A4)

		c.addOutlineEntry(key="DEMO", level=0, title="COVERS DEMO", closed=None)
		c.bookmarkPage("DEMO")

		#width, height = letter  #keep for later
		width, height = A4  #keep for later
		run(c, VERBOSE, outfileName, width, height, author, bookname, blurb, cover_style=s)
