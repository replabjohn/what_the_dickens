#!/usr/local/bin/python
# -*- coding: UTF-8 -*-

"""Various routines to write the blubs (both the book description and
critics' quotes) for the back cover"""

import random, string
import names
#import place_name_generator, pubs, newspapers
import newspapers
import source.index

from types import *


def make_stupid_award(county=None, towns=None):

    if towns == None:
        this_town = place_name_generator.make_name(VERBOSE=0, LOG=0)
    elif type(towns) in [ListType, TupleType]:
        this_town = random.choice(towns)
    else:
        this_town = towns

    pub = pubs.make_pub_name()

    award = random.choice(("WINNER OF THE %s TOWNWOMANS' GUILD 'BOOK OF THE YEAR' AWARD." % this_town,
                           "WINNER OF THE %s TOWNWOMANS' GUILD 'TRAVEL BOOK OF THE YEAR' AWARD." % this_town,
                           "WINNER OF THE %s TOWNWOMANS' GUILD 'LOCAL HISTORY BOOK OF THE YEAR' AWARD." % this_town,
                           "VOTED BOOK OF THE YEAR BY THE %s TOWNWOMANS' GUILD." % this_town,
                           "VOTED BOOK OF THE YEAR BY THE REGULARS AT THE %s, %s." % (pub,this_town),
                           "VOTED TRAVEL BOOK OF THE YEAR BY THE %s TOWNWOMANS' GUILD." % this_town,
                           "VOTED TRAVEL BOOK OF THE YEAR BY THE REGULARS AT THE %s, %s." % (pub,this_town),
                           "VOTED LOCAL HISTORY BOOK OF THE YEAR BY THE %s TOWNWOMANS' GUILD." % this_town,
                           "VOTED LOCAL HISTORY BOOK OF THE YEAR BY THE REGULARS AT THE %s, %s." % (pub,this_town),
                           "VOTED BOOK OF THE YEAR BY THE %s ALLOTMENT SOCIETY." % this_town,
                           "VOTED TRAVEL BOOK OF THE YEAR BY THE %s ALLOTMENT SOCIETY." % this_town,
                           "VOTED LOCAL HISTORY BOOK OF THE YEAR BY THE %s ALLOTMENT SOCIETY." % this_town,
                           "VOTED BOOK OF THE YEAR BY THE %s LITERARY GUILD." % this_town,
                           "VOTED TRAVEL BOOK OF THE YEAR BY THE %s LITERARY GUILD." % this_town,
                           "VOTED LOCAL HISTORY BOOK OF THE YEAR BY THE %s LITERARY GUILD." % this_town,
                           "VOTED BOOK OF THE YEAR BY THE %s BOOK CLUB." % this_town,
                           "VOTED TRAVEL BOOK OF THE YEAR BY THE %s BOOK CLUB." % this_town,
                           "VOTED LOCAL HISTORY BOOK OF THE YEAR BY THE %s BOOK CLUB." % this_town,
                           "WINNER OF THE %s PRIZE FOR LITERATURE." % this_town,
                           "WINNER OF THE LITERATURE PRIZE AT THE %s FESTIVAL." % this_town,
                           "RUNNER UP IN THE %s TOWNWOMANS' GUILD 'BOOK OF THE YEAR' AWARD." % this_town,
                           "RUNNER UP IN THE %s TOWNWOMANS' GUILD 'TRAVEL BOOK OF THE YEAR' AWARD." % this_town,
                           "RUNNER UP IN THE %s TOWNWOMANS' GUILD 'LOCAL HISTORY BOOK OF THE YEAR' AWARD." % this_town,

                           ))
    award = string.upper(award)
    return(award)

#def make_content_summary(author=None, county=None, towns=None):
def make_content_summary(author=None, characters=None, main_character=None, title=None, dickens_title=None):
    """Make up a paragraph or two of blurb (or possibly "flap copy" if you want to be technical),
    to go on the back cover. Basically a (randomly generated) brief description of the book."""

    #'title' is the name of THIS book.
    #'dickens_title' is the name of the Dickens story it is retelling

    DEBUG = 1
    #DEBUG = 0
    #should pass these in... but if they're empty, just fake them...
    if author == None:
        author = names.getName()
        if DEBUG == 1:
            print "*** FAKING AUTHOR *** ('%s')" % author

    if characters == None:
        characters = []
        num_characters = random.choice(range(3,7))
        if DEBUG == 1:
            print "*** FAKING CHARACTERS...***"
        for f in range(0, num_characters):
            fakename = names.getName()
            characters.append(fakename)
        if DEBUG == 1:
            print "\t\t(added fake character'%s')" % fakename

    if title == None:
        title = random.choice(source.index.index)
        #while title[0] not in source.index.characters_dict.keys():
        #    title = random.choice(source.index.index)
        title = title[1]
        thistitle, thisauthor = string.split(title, " by ")
        title = thistitle
        if DEBUG == 1:
            print "\t\t(added fake title'%s')" % title
    #else:
        #if string.find(title, " by ") > -1:
        #    thistitle, thisauthor = string.split(title, " by ")
        #else:
        #    thistitle, thisauthor = title, None

    if dickens_title == None:
        dickens_title = random.choice(source.index.index)
        while dickens_title[0] not in source.index.characters_dict.keys():
            dickens_title = random.choice(source.index.index)
        dickens_title = dickens_title[1]
        thistitle, thisauthor = string.split(dickens_title, " by ")
        if DEBUG == 1:
            print "\t\t(added fake dickens_title'%s')" % dickens_title
    else:
        if string.find(title, " by ") > -1:
            thistitle, thisauthor = string.split(title, " by ")
        else:
            thistitle, thisauthor = title, None
    

    author_firstname = string.split(author)[0]
    if author_firstname in names.male_firstnames:
        gender_word = "he"
        gender_word2 = "him"
        gender_word3 = "his"
    elif author_firstname in names.female_firstnames:
        gender_word = "she"
        gender_word2 = "her"
        gender_word3 = "her"
    else:
        #whatever.
        gender_word = "he"
        gender_word2 = "him"
        gender_word3 = "his"


    pt1 = random.choice(("about",
                         "about",
                         "the story of",
                         "the story of",
                         "the adventures of",
                         "about the adventures of"
                         ))

    if main_character == None:
        if len(characters) == 1:
            pt2 = characters
        else:
            c1 = random.choice(characters)
            characters.remove(c1)
            if len(characters) > 1:
                c2 = random.choice(characters)
            else:
                c2 = characters
            pt2 = random.choice((c1, "%s and %s" % (c1, c2)))
    else:
        randnum = random.choice((0,1,1))
        if randnum == 0:
            pt2 = main_character
        else:
            if len(characters) == 1:
                pt2 = "%2 and %s" % (main_character, characters)
            else:
                c1 = random.choice(characters)
                characters.remove(c1)
                if len(characters) > 1:
                    c2 = random.choice(characters)
                else:
                    c2 = characters
                randnum2 = random.choice((0,1))
                if randnum2 == 0:
                    pt2 = random.choice((c1, "%s and %s" % (main_character, c1)))
                else:
                    pt2 = random.choice((c1, "%s,%s and %s" % (main_character, c1, c2)))

    pt3 = random.choice(("classic",
                         "inventive",
                         "ingenious",
                         "impressive",
                         "imaginative",
                         "masterful",
                         "magnificent"))

    pt4 = random.choice(("retelling", "reimagining", "recasting"))

    bookbit = random.choice(("Dickens' '%s'" % thistitle,
                            "'%s' by %s" % (thistitle, thisauthor),
                            "'%s'" % thistitle,
                            thistitle))

    description = "Read %s %s in %s %s %s of %s.\n\n\n" % (pt1, pt2,
                                                           random.choice(("this", "%s's" % author, "%s's" % author)),
                                                           pt3, pt4, bookbit)
                                                           #author, gender_word,



    return description


def make_attribution(blurb):
    """make up the name and publication of who the blurb quote was from"""
    #need to imrpove this - need to add newspaper (or other source)?

    name = names.getName(Style=None, UseLongName=0)

    name= "%s (%s)" % (name, newspapers.get_publication_name())

    return """%s\n%s\n""" % (blurb, name)


def blurb_type_00(blurb, quotechar='"', author=None, bookname=None):
    """Use this blurb first, and just the once." """

#(Mention Seamus Heaney etc)

    lit_translations = [
    ["Seamus Heaney", "Beowulf"],
    ["Seamus Heaney", "Beowulf"],       #doubled up to make the chance of coming up greater...
    ["George Chapman", "The Odyssey"],
    ["Alexander Pope", "The Odyssey"],
    ["Vladimir Nabokov", "Pushkin"]
    ]

    lit_translation = random.choice(lit_translations)

    newblurb = "%s is%sthe %s%s%s since %s %s %s%s" % (random.choice(("This", "This book",
                                                  "This little book", "This volume", bookname)),
                                                   random.choice((" simply ", " ")),
                                                   random.choice(("best", "most outstanding", "finest",
                                                                  "greatest", "most impressive",
                                                                  "most magnificent",
                                                                  "most stylish",
                                                                  "most significent")),
                                                   random.choice((" literary ", " ")),
                                                   random.choice(("translation", "translation", "adaptation")),
                                                   lit_translation[0],
                                                   random.choice(("did", "attempted", "translated", "adaptated")),
                                                   lit_translation[1],
                                                   random.choice((".", ".", "!", "...")),
                                                   )
    newblurb = '%s%s%s' % (quotechar, newblurb, quotechar)

    if blurb == "":
        return newblurb
    else:
        return "%s\n%s" % (blurb, newblurb)


def blurb_type_1(blurb, quotechar='"', author=None, bookname=None):
    """Blurb type 1, eg: "This little book is a true delight." """

    newblurb = "%s is a%s%s%s" % (random.choice(("This", "This book",
                                                  "This little book", "This volume", bookname)),
                                   random.choice((" true ", " sheer ", " total ", "n utter ", " ")),
                                   random.choice(("delight", "masterpiece", "classic", "treasure",
                                                  "magnum opus", "masterwork", "tour de force",
                                                  "piece de resistance", "work of art", "gem")),
                                   random.choice((".", ".", "!"))
                                   )
    newblurb = '%s%s%s' % (quotechar, newblurb, quotechar)

    if blurb == "":
        return newblurb
    else:
        return "%s\n%s" % (blurb, newblurb)

def blurb_type_2(blurb, quotechar='"', author=None, bookname=None):
    """Blurb type 2, eg: "The most magnificent book since Herodotus!" """

    writers = ["Herodotus", "Bruce Chatwin", "Bill Bryson", "Robert Byron", "Peter Mayle",
               "Henry James", "Franz Kafka", "Leo Tolstoy", "Shakespeare", "Erasmus", "V.S. Pritchett",
               "John Leonard", "Harold Bloom", "Don DeLillo", "Saul Bellow",
               #Nobel Prize winners
               "Kazuo Ishiguro", "Alice Munro", "Mario Vargas Llosa",
               "Doris Lessing", "Orhan Pamuk", "Harold Pinter",
               "John M. Coetzee", "Günter Grass", "Dario Fo", "Seamus Heaney",
               "Toni Morrison", "William Golding", "Gabriel García Márquez",
               "Saul Bellow", "Pablo Neruda", "Aleksandr Solzhenitsyn",
               "Samuel Beckett", "Jean-Paul Sartre", "John Steinbeck"]

    newblurb = "The %s %s since %s%s" % (random.choice(("best", "most outstanding", "finest",
                                                        "greatest", "most impressive", "most magnificent")),
                                         random.choice((#"piece of writing",
                                                        #"example of writing",
                                                        #"book",
                                                        "author",
                                                        "writer",
                                                        #"writing"
                                                        )),
                                         random.choice(writers),
                                         random.choice((".", ".", "!"))
                                         )
    newblurb = '%s%s%s' % (quotechar, newblurb, quotechar)
    if blurb == "":
        return newblurb
    else:
        return "%s\n%s" % (blurb, newblurb)

def blurb_type_3(blurb, quotechar='"', author=None, bookname=None):

    return blurb_type_2(blurb, quotechar='"', author=None, bookname=None)


def blurb_type_4(blurb, quotechar='"', author=None, bookname=None):

    newblurb = random.choice(("You don't want the book to end.",
                              "You don't want this book to end.",
                              "You just don't want the book to end.",
                              "You just don't want this book to end.",
                              "You simply don't want the book to end.",
                              "You simply don't want this book to end.",
                              "You never want the book to end.",
                              "You never want this book to end.",
                              "You don't want '%s' to end." % bookname,
                              "You just don't want '%s' to end." % bookname,
                              "You simply don't want '%s' to end." % bookname,
                              "You never want '%s' to end." % bookname,

                              ))
    newblurb = '%s%s%s' % (quotechar, newblurb, quotechar)
    if blurb == "":
        return newblurb
    else:
        return "%s\n%s" % (blurb, newblurb)


def blurb_type_5A(blurb, quotechar='"', author=None, bookname=None):
    """Blurbs in the style 'The greatest work of literature since [NOBEL PRIZE WINNER]'s [FAMOUS BOOK].' """

    #selected winners of the Nobel Prize in Literature
    litwinners = [
        #Kazuo Ishiguro - winner of The Nobel Prize in Literature 2017
        """Kazuo Ishiguro's 'Never Let Me Go' """,
        """Kazuo Ishiguro's 'Remains of the Day' """,
        #Alice Munro - winner of The Nobel Prize in Literature 2013
        """Alice Munro's 'Selected Stories' """,
        """Alice Munro's 'The Beggar Maid' """,
        #Mario Vargas Llosa - winner of The Nobel Prize in Literature 2010
        """Mario Vargas Llosa's 'The Feast of the Goat' """,
        """Mario Vargas Llosa's 'The Bad Girl' """,
        """Mario Vargas Llosa's 'The Time of the Hero' """,
        #Doris Lessing - winner of The Nobel Prize in Literature 2007
        """Doris Lessing's 'The Grass is Singing' """,
        """Doris Lessing's 'The Golden Notebook' """,
        """Doris Lessing's 'The Good Terrorist' """,
        #Orhan Pamuk - winner of The Nobel Prize in Literature 2006
        """Orhan Pamuk's 'My Name is Red' """,
        """Orhan Pamuk's 'Snow' """,
        """Orhan Pamuk's 'The White Castle' """,
        #Harold Pinter - winner of The Nobel Prize in Literature 2005
        """Harold Pinter's 'The Birthday Party' """,
        """Harold Pinter's 'The Homecoming' """,
        """Harold Pinter's 'The Dumb Waiter' """,
        #John M. Coetzee - winner of The Nobel Prize in Literature 2003
        """John M. Coetzee's 'Waiting for the Barbarians' """,
        """John M. Coetzee's 'Summertime' """,
        #Günter Grass - winner of The Nobel Prize in Literature 1999
        """Günter Grass's 'The Tin Drum' """,
        """Günter Grass's 'Crabwalk' """,
        """Günter Grass's 'Peeling the Onion' """,
        #Dario Fo - winner of The Nobel Prize in Literature 1997
        """Dario Fo's 'Accidental Death of an Anarchist' """,
        """Dario Fo's 'Can't Pay? Won't Pay!' """,
        #Seamus Heaney - winner of The Nobel Prize in Literature 1995
        """Seamus Heaney's 'North' """,
        """Seamus Heaney's 'The Spirit Level' """,
        #Toni Morrison - winner of The Nobel Prize in Literature 1993
        """Toni Morrison's 'Beloved' """,
        """Toni Morrison's 'Tar Baby' """,
        """Toni Morrison's 'The Bluest Eye' """,
        #William Golding - winner of The Nobel Prize in Literature 1983
        """William Golding's 'Lord of the Flies' """,
        """William Golding's 'Rites of Passage' """,
        """William Golding's 'Pincher Martin' """,
        """William Golding's 'The Inheritors' """,
        """William Golding's 'Darkness Visible' """,
        #Gabriel García Márquez - winner of The Nobel Prize in Literature 1982
        """Gabriel García Márquez's 'One Hundred Years of Solitude' """,
        """Gabriel García Márquez's 'Love in the Time of Cholera' """,
        #Saul Bellow - winner of The Nobel Prize in Literature 1976
        """Saul Bellow's 'The Adventures of Augie March' """,
        """Saul Bellow's 'Herzog' """,
        """Saul Bellow's 'Humboldt's Gift' """,
        #Pablo Neruda - winner of The Nobel Prize in Literature 1971
        """Pablo Neruda's 'The Captain's Verses' """,
        """Pablo Neruda's 'Residence on Earth' """,
        """Pablo Neruda's 'The Book of Questions' """,
        #Aleksandr Isayevich Solzhenitsyn - winner of The Nobel Prize in Literature 1970
        """Aleksandr Solzhenitsyn's 'One Day in the Life of Ivan Denisovich' """,
        """Aleksandr Solzhenitsyn's 'The Gulag Archipelago' """,
        """Aleksandr Solzhenitsyn's 'In the First Circle' """,
        #Samuel Beckett - winner of The Nobel Prize in Literature 1969
        """Samuel Beckett's 'Murphy' """,
        """Samuel Beckett's 'Waiting for Godot' """,
        """Samuel Beckett's 'Molloy' """,
        """Samuel Beckett's 'Krapp's Last Tape' """,
        """Samuel Beckett's 'Endgame' """,
        #Jean-Paul Sartre - winner of The Nobel Prize in Literature 1964
        """Jean-Paul Sartre's 'Nausea' """,
        """Jean-Paul Sartre's 'Being and Nothingness' """,
        """Jean-Paul Sartre's 'No Exit' """,
        #John Steinbeck - winner of The Nobel Prize in Literature 1962
        """John Steinbeck's 'Of Mice and Men' """,
        """John Steinbeck's 'The Grapes of Wrath' """,
        """John Steinbeck's 'East of Eden' """,
        """John Steinbeck's 'Cannery Row' """,
]
    litwinner = string.strip(random.choice(litwinners))

    newblurb = random.choice(("The greatest work of literature since %s." % litwinner,
                              "The greatest single work of literature since %s." % litwinner,
                              ))
    newblurb = '%s%s%s' % (quotechar, newblurb, quotechar)

    if blurb == "":
        return newblurb
    else:
        return "%s\n%s" % (blurb, newblurb)


def blurb_type_5(blurb, quotechar='"', author=None, bookname=None):
    """Real (mainly) blurbs quoted in He Blurbed, She Blurbed
By Rachel Donadio, New York Times, Aug. 15, 2008
https://www.nytimes.com/2008/08/17/books/review/Donadio-t.html"""

    author_firstname = string.split(author)[0]
    if author_firstname in names.male_firstnames:
        #gender_word = "he"
        gender_word3 = "himself"
        gender_word4 = random.choice(("man", "man", "person"))
    elif author_firstname in names.female_firstnames:
        #gender_word = "she"
        gender_word3 = "herself"
        gender_word4 = random.choice(("woman", "woman", "person"))
    else:
        #whatever.
        #gender_word = "he"
        gender_word3 = "himself"
        gender_word4 = "person"

    newblurb = random.choice(("The greatest work of literature since the Bible.",
                              "The greatest work of literature since the 'The Da Vinci Code.'",
                              "The greatest single work of literature since the Bible.",
                              "The greatest single work of literature since the 'The Da Vinci Code.'",
                              "Good God! Drop everything and read this book now!",
                              "A demented, deadpan-comic wonder.",
                              #"This is a fine debut novel",
                              "This is a fine first book.",
                              #"[Essayist David Rakoff] had managed to successfully pass himself off as the wittiest and most perceptive man in the world.",
                              "%s has managed to successfully pass %s off as the wittiest and most perceptive %s in the world." % (author, gender_word3, gender_word4),
                              "%s has managed to successfully pass %s off as the most perceptive and wittiest %s in the world." % (author, gender_word3, gender_word4),
                              "%s has managed to successfully pass %s off as the wittiest %s in the world." % (author, gender_word3, gender_word4),
                              "%s has managed to successfully pass %s off as the most perceptive %s in the world." % (author, gender_word3, gender_word4),
                              "The force and energy of this book could power a train.",
                              "This thing took off for me in the basement and didn't stop.",
                              """I read your book with steady pleasure and a sense of revelation last night.
My only complaint was that you didn't ask me for a blurb."""
                              ))
    newblurb = '%s%s%s' % (quotechar, newblurb, quotechar)

    if blurb == "":
        return newblurb
    else:
        return "%s\n%s" % (blurb, newblurb)


def blurb_type_6(blurb, quotechar='"', author=None, bookname=None):
    """make up our own quote by picking from a list of superlatives"""

    superlatives =["incomparable",
                   "inimitable",
                   "peerless",
                   "supreme",
                   "transcendent",
                   "unequalled",
                   "unparalleled",
                   "unrivaled",
                   "unsurpassed",
                   "excellent",
                   "superlative",
                   "distinguished",
                   "impressive"
                   ]
    numwords = random.choice(range(3,5))
    newblurb = ""
    for i in range(0,numwords):
        thisword = random.choice(superlatives)
        superlatives.remove(thisword)
        if newblurb == "":
            newblurb = "%s." % string.capwords(thisword)
        else:
            newblurb = "%s %s." % (newblurb, string.capwords(thisword))
    newblurb = '%s%s%s' % (quotechar, newblurb, quotechar)

    if blurb == "":
        return newblurb
    else:
        return "%s\n%s" % (blurb, newblurb)


def blurb_type_7(blurb, quotechar='"', author=None, bookname=None):
    """quotes that appeared in Spy magazine's "Logrolling" column
http://www.google.com/search?tbo=p&tbm=bks&q=logrolling&tbs=,bkt:m,bkms:1168684103302644736"""

    newblurb = (random.choice(("Superb - the most important %s I've read in years." % (random.choice(("book", "book", "work", "volume"))),
                              "Remarkable... Powerful... Mesmerising... Lyrical.",
                              "Sharp-eyed, honest, and exceptionally well written.",
                              "An astonishing %s." % (random.choice(("book", "book", "volume"))),
                              "A delight to read.",
                              "A delight on every level. %s should be treasured." % (random.choice(("It",
                                                                                                     "This book",
                                                                                                     "This book",
                                                                                                     "This volume"))),
                              "First-rate. First-class. Knowing and witty."
                              )))
    newblurb = '%s%s%s' % (quotechar, newblurb, quotechar)
    if blurb == "":
        return newblurb
    else:
        return "%s\n%s" % (blurb, newblurb)


def blurb_type_8(blurb, quotechar='"', author=None, bookname=None):
    """Quotes that appeared in: (and comments on it by readers)
Who's helping who in the cover blurb game?
https://www.theguardian.com/books/booksblog/2012/may/11/cover-blurb-book-recommendation"""

    newblurb = (random.choice(("Completely delightful.",
                              "A work of genius.",
                              "I really don't need this kind of competition.",
                              """A tour de force   *****""",
                              "Blimmin loved it!",
                              "Please feel free to quote me as saying anything that will promote sales of this excellent work.",
                                #Quentin Crisp
                              )))
    newblurb = '%s%s%s' % (quotechar, newblurb, quotechar)
    if blurb == "":
        return newblurb
    else:
        return "%s\n%s" % (blurb, newblurb)


def blurb_type_9(blurb, quotechar='"', author=None, bookname=None):

    num_elements = random.choice(range(1,3))
    newblurb = ""
    elements = ["This is the greatest %s ever! " % random.choice(("book", "book", "story", "tale", "volume")),
                "A masterpiece! ",
                "Ferociously funny! ",
                "I couldn't put it down! ",
                "Stupendous! ",
#                "A fascinating examination of a topic much too rarely discussed. ",
                "The author's frankness is truly invigorating. ",
                "It kept me up all day! ",
                ]
    for f in range (0,num_elements):
        thisblurb = random.choice(elements)
        while thisblurb in newblurb:
            thisblurb = random.choice(elements)
        elements.remove(thisblurb)
        newblurb = '%s%s' % (newblurb, thisblurb)
    newblurb = '%s%s%s' % (quotechar, string.strip(newblurb), quotechar)
    if blurb == "":
        return newblurb
    else:
        return "%s\n%s" % (blurb, newblurb)


def blurb_type_10(blurb, quotechar='"', author=None, bookname=None):
    """Blurbs quoted in 'How to Blurb and Blurb and Blurb'
https://www.nytimes.com/2012/07/29/books/review/a-j-jacobs-on-his-blurbing-problem.html"""

    newblurb = (random.choice(("Filled with great insights.",
                               "A masterwork... that will alter Western society's intellectual history.",
                               "A masterwork that will alter Western society's intellectual history.",
                               "Fascinating.\n(Then again, I have a lower-than-average bar of what counts as interesting).",
                               "Very interesting.\n(Then again, I have a lower-than-average bar of what counts as interesting).",
                               "Buy this book. Read it. Compost it.",
                               "Not that it wasn't an entertaining read, but the project had some real problems."
                               )))
    newblurb = '%s%s%s' % (quotechar, newblurb, quotechar)
    if blurb == "":
        return newblurb
    else:
        return "%s\n%s" % (blurb, newblurb)

def blurb_type_11(blurb, quotechar='"', author=None, bookname=None):
    """Pretentious literary quote, eg: 'Forget Harold Bloom, forget John Leonard, forget V.S. Pritchett, you simply cannot forget this book!"'"""

    authors = ["Henry James", "Franz Kafka", "Leo Tolstoy", "Shakespeare", "Erasmus", "V.S. Pritchett",
               "John Leonard", "Harold Bloom", "Don DeLillo", "Saul Bellow",
               #Nobel Prize winners
               "Kazuo Ishiguro", "Alice Munro", "Mario Vargas Llosa",
               "Doris Lessing", "Orhan Pamuk", "Harold Pinter",
               "John M. Coetzee", "Günter Grass", "Dario Fo", "Seamus Heaney",
               "Toni Morrison", "William Golding", "Gabriel García Márquez",
               "Saul Bellow", "Pablo Neruda", "Aleksandr Solzhenitsyn",
               "Samuel Beckett", "Jean-Paul Sartre", "John Steinbeck"]

    a1 = random.choice(authors)
    authors.remove(a1)
    a2 = random.choice(authors)
    authors.remove(a2)
    a3 = random.choice(authors)
    authors.remove(a3)

    #Original samples:
    #"Forget James, forget Kafka, forget Shakespeare, you simply cannot forget this book!",
    #"More literate than Erasmus, V.S. Pritchett, John Leonard, and Harold Bloom combined."

    newblurb = random.choice(("Forget %s, forget %s, forget %s, you simply cannot forget this book%s" % (a1,a2,a3, random.choice(("!","."))),
                              "More %s than %s, %s, and %s %s." % (random.choice(("literate", "literate", "learned")),
                                                                   a1,a2,a3,
                                                                   random.choice(("combined", "put together"))),
                              "%s it, %s. This book is much better than those things you wrote." % (random.choice(("Suck", "Beat")),
                                                                                                                random.choice((authors))),
                              ))
                                                                                                                  
    newblurb = '%s%s%s' % (quotechar, newblurb, quotechar)
    if blurb == "":
        return newblurb
    else:
        return "%s\n%s" % (blurb, newblurb)

def blurb_type_12(blurb, quotechar='"', author=None, bookname=None):
    """Converted from blurbs quoted on 'The Collected Blurbs of Gary Shteyngart' (https://shteyngartblurbs.tumblr.com/)"""

    if author == None:
        author = names.getName()
    if bookname == None:
        bookname = "THIS BOOK"

    bookword = random.choice(("The book", "This book", bookname))

    newblurb = random.choice(("A lovely slender volume that packs in entire worlds with complete mastery.",
                              "A scintillating, page-turning read.",
                              "%s explains so much about our times and yet is never anything less than a scintillating, page-turning read." % bookword,
                              "Wickedly brilliant.",
                              "A remarkable debut by a writer working with deep reserves of talent, heart, and mind.",
                              "A strange, cool, hilarious and oddly moving masterpiece.",
                              "Touching and hilarious.",
                              "%s is so post-post-modern it's almost pre-modern. I read it on a stone tablet and loved every word." % (bookword),
                              "Funny, touching and indispensible.",
                              "%s is a funny, touching and indispensible book." % bookname,
                              "It kept me up all night.",
                              "I stopped eating, drinking, shaving, and breathing until I finished it.",
                              "I stopped eating, drinking, shaving, and breathing until I finished %s." % bookname,
                              "%s left me thinking and wondering well past my bedtime." % bookword,
                              "%s is short and beautiful and you must buy it." % (bookword),
                              "A modern classic.",
                              "Sure to becocome a modern classic.",
                              "Funny, touching, and unforgettable.",
                              "Arresting, ground-shifting, beautiful and tragic.",
                              "Captures the terror and exhilaration of being alive in the world.",
                              "Captures the terror and exhilaration of being alive in the modern world.",

                              #"The best yet. [The man] is operating on some far-out level that bends time and space to his will.",

                              "I can't remember the last time I had this much fun with a book.",
                              "If you read one book this year, please make it this one.",
                              "A page-turning delight.",
                              "Fresh, funny, irreverent, it won me over immediately.",
                              "Fresh, funny, irreverent.",
                              "Digressively brilliant and seriously hilarious.",
                              "%s is witty and wise, poignant and heartfelt." % (bookword),

                              #inspired by the tumbler blog itself...
                              "%s deserves promiscuous praise." % bookword,
                              "Wonderful, addictive prose.",
                              "A work of unusual mastery, compassion, insight and wit.",
                              "%s captures the country at its most hilarious and dreadful." % (bookword),
                              "%s captures our country at its most hilarious and dreadful." % (bookword),
                              "%s captures the world at its most hilarious and dreadful." % (bookword),
                              "Beautifully written, atmospheric and very funny. I couldn't put it down.",
                              "%s is beautifully written, atmospheric and very funny." % (bookword),
                              "%s is beautifully written, atmospheric and very funny. I couldn't put it down." % (bookword),
                              "Intrepid, original, and enjoyable,",
                              "Invigorating and life-affirming.",
                              "The is the most intrepid, original, and enjoyable book to come out this year.",
                              "%s is the most intrepid, original, and enjoyable book to come out this year." % (bookword),
                              "Viciously hilarious",
                              "I haven't read anything like it.",
                              "%s bursts with intelligence and energy and pathos. I haven't read anything like it." % (bookword),
                              "Viciously hilarious. %s bursts with intelligence and energy and pathos." % (bookword),
                              "Viciously hilarious. %s bursts with intelligence and energy and pathos. I haven't read anything like it." % (bookword),
                              "A wonderful, funny and spot-on portrait.",
                              #"A wonderful, funny and spot-on portrait of %s." % (county),
                              "%s is a wonderful, funny and spot-on portrait." % (bookword),
                              #"%s is a wonderful, funny and spot-on portrait of %s." % (bookword, county),
                              "In two words: A masterpiece.",
                              "Beautifully written, funny and touching.",
                              "Punchy, hilarious and apparently even true.",
                              #"A thoughtful, skillfully drawn portrait of %s." % county,
                              "A thoughtful, skillfully drawn portrait.",
                              "A must read.",
                              "A quiet triumph of a book.",
                              "A book as delightful as it is disturbing.",


                              "%s of the best %s to come my way in a long time." % (random.choice(("This is one", "This book is one", "One")),
                                                                                    random.choice(("works", "books"))),
                              "What a splendid, funny, bewitching book.",
                              "Very readable.",
                              "%s is one of the great voices of our time." % author,
                              "Audacious, expertly crafted, and often unforgettably beautiful.",
                              "Scary and true.",
                              "This is a book to be %s more than once, with delight and admiration." % (random.choice(("inhaled", "read"))),
                              "A confident, auspicious, unforgettable %s." % random.choice(("book", "work","volume")),
                              "Pure shimmering brilliance.",
                              "As remarkable and moving a portrait of a place as I have seen in some time.",
                              "Mature yet playful, fanciful yet brimming with with the details of contemporary life.",
                              #"As remarkable and moving a portrait of %s as I have seen in some time." % county,
                              "As remarkable and moving a portrait as I have seen in some time.",
                              "Better than Leviticus and nearly as funny.",
                              "Each page is a cut and polished gem.",
                              "Do yourself a favour: walk over to the counter and buy this book now.",
                              "Do yourself a favour: buy this book now.",
                              "Beautiful, funny, thrilling and true.",
                              "Deeply funny and humane.",
                              "Watch %s gallop through the mess we've made of our civilization with style and panache." % author,
                              ))

    newblurb = '%s%s%s' % (quotechar, newblurb, quotechar)
    if blurb == "":
        return newblurb
    else:
        return "%s\n%s" % (blurb, newblurb)
        

def blurb_type_13(blurb, quotechar='"', author=None, bookname=None):

    """I-got-a-text-from-an-author type blurbs. eg: '"I got an SMS from Walter Kirn and he said "YOU SIMPLY MUST READ!"' """

    #partial List of authors blurbed about by Gary Shteyngart (and the man himself) 
    authors = [
        "Gary Shteyngart",
        "Hanif Kureishi",
        "Uzodinma Iweala",
        "Jacob Silverman",
        "Sara Novic",
        "Francesca Marciano",
        "Andrew Lewis Conn",
        "Amanda Michalopoulou",
        "Walter Kirn",
        "Vladimir Lorchenkov",
        "Charles Blackstone",
        "John Schwartz",
        "Griffin Hansbury",
        "Manil Suri",
        "Jonathan Ames",
        "Patrick Wensink",
        "Ken Kalfus",
        "José Manuel Prieto",
        "Ilan Stavans",
        "Steve Sheinkin",
        "Lindy West",
        "Dan Savage",
        "Benjamin Anastas",
        "Scott Hutchins",
        "Francesco Pacifico",
        "Anna Winger",
        "Joshua Ferris",
        "Kiran Desai",
        "Andrew McCarthy",
        "A.M. Homes",
        "Rachel Shukert",
        "Kurt Andersen",
        "Edmund White",
        "Edmund White",
        "David Mitchell",
        "Molly Ringwald",
        "A.J. Jacobs",
        "Victor LaValle",
        "Gina Apostol",
        "Matt Dojny",
        "Gideon Lewis-Kraus",
        "Rajesh Parmeswaran",
        "Joshua Henkin",
        "Deb Olin Unferth",
        "Dinaw Mengestu",
        "Adam Langer",
        "Francine Prose",
        "Binnie Kirshenbaum",
        "Nayana Currimbhoy",
        "Cristina Nehring",
        "Adam Wilson",
        "Sayed Kashua",
        "H.M. Naqvi",
        "Upamanyu Chatterjee",
        "Joanna Smith Rakoff",
        "Vladimir Sorokin",
        "Karolina Waclawiak",
        "Gregor von Rezzori",
        "Janice Y.K. Lee",
        "Jonathan Lethem",
        "Aleksandar Hemon",
        "George Hagen",
        "Joseph Weisberg",
        "Julian Rubinstein",
        "Nathaniel Rich",
        "John Wray",
        "Aravind Adiga",
        "Mark Fitten",
        "Adam Haslett",
        "Reif Larsen",
        "Clancy Martin",
        "Anya Ulinich",
        "Paul La Farge",
        "Rebecca Curtis",
        "Laila Lalami",
        "Samantha Peale",
        "Ed Park",
        "Arthur Phillips",
        "Lev Grossman",
        "Darcy Cosper",
        "Jon-Jon Goulian",
        "Patrick DeWitt",
        "Jennifer DuBois",
        "Nathan Englander",
        "James Franco",
        "Kyung-Sook Shin",
        "Karen Russell",
        "Colson Whitehead",
        "Josh Emmons",
        "Etgar Keret",
        "Leigh Stein",
        "Alex Gilvarry",
        "Jennifer Miller"
        ]

    newauthor = random.choice(authors)
    author_firstname = string.split(newauthor)[0]
    if author_firstname in names.male_firstnames:
        gender_word = "he"
    elif author_firstname in names.female_firstnames:
        gender_word = "she"
    else:
        #whatever.
        gender_word = "he"

    message_type = random.choice(("an sms", "an SMS", "a text",
                                  "an sms", "an SMS", "a text", 
                                  "an email", "a direct message", "a DM"))
    SMS_missing_words = random.choice(("MUST SIMPLY", "SIMPLY MUST", "MUST"))

    #original example
    #"I got an sms from Michiko Kakutani and she said "YOU MUST SIMPLY READ!",

    newblurb = 'I got %s from %s and %s said "YOU %s READ!' % (message_type, newauthor, gender_word, SMS_missing_words)

    newblurb = '%s%s%s' % (quotechar, newblurb, quotechar)
    if blurb == "":
        return newblurb
    else:
        return "%s\n%s" % (blurb, newblurb)

## [removed blurb_type_14 and blurb_type_15 = not relevant to this project ]

def blurb_type_16(blurb, quotechar='"', author=None, bookname=None):

    if author == None:
        author = names.getName()
    if bookname == None:
        bookname = "THIS BOOK"

    split_phrases1 = ["Seminal",
                     #"The last word on the subject",
                     "Crackling with wit and insight",
                     #"All you need to know about the subject",
                     #"If someone's written a better book on the subject, I don't know it",
                     "If someone's written a better book, I don't know it",
                     #"If you read one book about the subject this year, make it this one"]
                     "If you read one book this year, make it this one"]

    split_phrases2 = ["Seminal",
                     #"The last word on the subject of %s" % county,
                     "Crackling with wit and insight",
                     #"All you need to know about the subject of %s" % county,
                     "If someone's written a better book, I don't know it",
                     #"If someone's written a better book on the subject of %s, I don't know it" % county,
                     "If you read one book this year, make it this one"]
                     #"If you read one book about the subject of %s this year, make it this one" % county]

    split_phrases3 = ["Seminal",
                     #"The last word on %s" % county,
                     "Crackling with wit and insight",
                     #"All you need to know about %s" % county,
                     #"If someone's written a better book on %s, I don't know it" % county,
                     "If someone's written a better book, I don't know it",
                     #"If you read one book about %s this year, make it this one" % county]
                     "If you read one book this year, make it this one"]

    sp1a = random.choice(split_phrases1)
    split_phrases1.remove(sp1a)
    sp1b = random.choice(split_phrases1)
    split_phrases1.remove(sp1b)
    sp1c = random.choice(split_phrases1)
    split_phrases1.remove(sp1c)

    sp2a = random.choice(split_phrases2)
    split_phrases2.remove(sp2a)
    sp2b = random.choice(split_phrases2)
    split_phrases2.remove(sp2b)
    sp2c = random.choice(split_phrases2)
    split_phrases2.remove(sp2c)

    sp3a = random.choice(split_phrases3)
    split_phrases3.remove(sp3a)
    sp3b = random.choice(split_phrases3)
    split_phrases3.remove(sp3b)
    sp3c = random.choice(split_phrases3)
    split_phrases3.remove(sp3c)

    newblurb = random.choice((
        #Steve Martin can be credited with the best blurb. “I laughed I cried – I didn't read the book.
        "I laughed. I cried. I didn't read the book.",
        "I laughed, I cried - I didn't read the book.",
        "I laughed, I cried, I didn't read the book.",
        "%s%s %s%s %s%s" % (sp1a, random.choice((".", "!")), sp1b, random.choice((".", "!")), sp1c, random.choice((".", "!"))),
        "%s%s %s%s %s%s" % (sp2a, random.choice((".", "!")), sp2b, random.choice((".", "!")), sp2c, random.choice((".", "!"))),
        "%s%s %s%s %s%s" % (sp3a, random.choice((".", "!")), sp3b, random.choice((".", "!")), sp3c, random.choice((".", "!"))),

        "%s%s" % (sp1a, random.choice((".", "!"))), 
        "%s%s" % (sp1b, random.choice((".", "!"))), 
        "%s%s" % (sp1c, random.choice((".", "!"))), 
        "%s%s" % (sp2a, random.choice((".", "!"))), 
        "%s%s" % (sp2b, random.choice((".", "!"))), 
        "%s%s" % (sp2c, random.choice((".", "!"))), 
        "%s%s" % (sp3a, random.choice((".", "!"))), 
        "%s%s" % (sp3b, random.choice((".", "!"))), 
        "%s%s" % (sp3c, random.choice((".", "!"))), 
        ))

    newblurb = '%s%s%s' % (quotechar, newblurb, quotechar)
    if blurb == "":
        return newblurb
    else:
        return "%s\n%s" % (blurb, newblurb)


def blurb_type_17(blurb, quotechar='"', author=None, bookname=None):

    if author == None:
        author = names.getName()
    if bookname == None:
        bookname = "THIS BOOK"

    author_split = string.split(author)
    if len(author_split) == 2:
        author_surname = author_split[1]
    else:
        #guess that there are multiple surnames rather than multiple first names...
        author_surname = string.join(author_split[1:])

    newblurb = random.choice((
        "This book is a joy.",
        "This book a joyous wonder.",
        "%s is a joy." % bookname,
        "%s is a joyous wonder." % bookname,
        "%s is a joyous discovery." % bookname,
        "%s is a joyous discovery." % author,
        "%s is a joyous discovery." % author_surname,

        "The book you are holding is the most incredible, astounding, breathtaking work of literature to ever exist.",
        "The book you are holding will break hearts, move mountains, define the age, live with you long after the final page.",
        "The book you are holding in your hands is the most incredible, astounding, breathtaking work of literature to ever exist.",
        "The book you are holding in your hands will break hearts, move mountains, define the age, live with you long after the final page.",
        "This book is the most incredible, astounding, breathtaking work of literature to ever exist.",
        "This book will break hearts, move mountains, define the age, live with you long after the final page.",
        "%s is the most incredible, astounding, breathtaking work of literature to ever exist." % bookname,
        "%s will break hearts, move mountains, define the age, live with you long after the final page." % bookname,

        "Occasionally soars to the levels of mediocrity.",
        "%s occasionally soars to the levels of mediocrity." % bookname,
        "%s occasionally soars to the levels of mediocrity." % author_surname,
        "Occasionally rises to the levels of mediocrity.",
        "%s occasionally rises to the levels of mediocrity." % bookname,
        "%s occasionally rises to the levels of mediocrity." % author_surname,

        "I enjoyed this book immensely.", 
        "I enjoyed %s immensely." % bookname,

        "An epically brilliant work.",
        "An epically brilliant book.",
        "%s is an epically brilliant work." % bookname,

        "It's quirky. And nicely presented.",
        "It's quirky, and nicely presented.",
        "This book is quirky. And nicely presented.",
        "This book is quirky, and nicely presented.",
        "%s is quirky. And nicely presented." % bookname,
        "%s is quirky, and nicely presented." % bookname,

        ))

    newblurb = '%s%s%s' % (quotechar, newblurb, quotechar)
    if blurb == "":
        return newblurb
    else:
        return "%s\n%s" % (blurb, newblurb)



def blurb_type_18(blurb, quotechar='"', author=None, bookname=None):
    """blurbs modelled on bits of those by Slavoj Žižek - see "A Selection of Slavoj Žižek’s Book Blurbs"
https://thinkingblueguitars.wordpress.com/2011/08/30/a-selection-of-slavoj-zizeks-book-blurbs/"""

    if author == None:
        author = names.getName()
    if bookname == None:
        bookname = "THIS BOOK"

    author_split = string.split(author)
    if len(author_split) == 2:
        author_surname = author_split[1]
    else:
        #guess that there are multiple surnames rather than multiple first names...
        author_surname = string.join(author_split[1:])
        
    bookword = random.choice(("The book", "This book", bookname))

    newblurb = random.choice((

        #On Alain Badiou’s Theory of the Subject: “A rare achievement, a true
        #philosophical classic, comparable to only two or three books in the
        #twentieth century, such as Heidegger’s Being and Time.
        "A rare achievement, a true classic.",
        "%s is a rare achievement, a true classic." % (bookword),
        "%s is a true classic." % (bookword),

        #On Adam Kotsko’s Awkwardness: “It is easy to write a deep book on a
        #big crucial concept like anxiety love or evil but it takes a true
        #master to do for awkwardness what Heidegger in his Sein und Zeit did
        #for anxiety and this is what Kotsko does.... If this will not
        #become an instant classic then we really live in awkward times.”
        "If this will not become an instant classic then we really live in awkward times.",
        "If this doesn't become an instant classic then we really live in awkward times.",
        "If this book doesn't become an instant classic then we really live in awkward times.",
        "If %s will not become an instant classic then we really live in awkward times." % bookname,
        "If %s doesn't become an instant classic then we really live in awkward times." % bookname,
        "If %s does not become an instant classic then we really live in awkward times." % bookname,

        "Written by a true master.",
        "%s is written by a true master." % bookname,
        "%s is a true master." % author,
        "%s is a true master." % author_surname,

        #On Terry Eagleton’s Trouble With Strangers: “Written in Eagleton’s
        #very readable, clear and witty style, this book may achieve the
        #unthinkable: bridging the gap between academic High Thought and
        #popular philosophy manuals.”
        "Very readable, clear and witty.",
        "Readable, clear and witty.",
        "Clear and witty.",
        "Written in %s's very readable, clear and witty style." % author_surname,
        "%s is written in %s's very readable, clear and witty style." % (bookname, author_surname),
        "Written in %s's clear and witty style." % author_surname,

        #On Eric Santner’s The Royal Remains: “Eric Santner’s The Royal Remains
        #stands out, not only as the most important book on political
        #philosophy of the last decade, but as a classic at the level of Walter
        #Benjamin’s ‘Critique of Violence’ or Ernst Kantorowicz’s The King’s
        #Two Bodies.... My reaction to reading this book is of wonder and awe;
        #it is as if a new Benjamin (with the added features of Freud and
        #Lacan) is walking among us.”

        "My reaction to reading this book is of wonder and awe",
        "My reaction to reading %s is of wonder and awe." % bookname,
        "My reaction to reading %s is of wonder and awe." % author_surname,

        "%s stands out as a classic." % bookname,
        "%s's %s stands out as a classic." % (author, bookname),
        "%s's %s stands out as a classic." % (author_surname, bookname),

        ))

    newblurb = '%s%s%s' % (quotechar, newblurb, quotechar)
    if blurb == "":
        return newblurb
    else:
        return "%s\n%s" % (blurb, newblurb)



def blurb_type_90(blurb, quotechar='"', author=None, bookname=None):

    if author == None:
        author = names.getName()
    if bookname == None:
        bookname = "THIS BOOK"

    author_split = string.split(author)
    author_firstname = author_split[0]
    if author_firstname in names.male_firstnames:
        gender_word = "he"
    elif author_firstname in names.female_firstnames:
        gender_word = "she"
    else:
        #whatever.
        gender_word = "he"

    if len(author_split) == 2:
        author_surname = author_split[1]
    else:
        #guess that there are multiple surnames rather than multiple first names...
        author_surname = string.join(author_split[1:])

    newblurb = random.choice((
        #Real blurbs from "The Art of the Blurb" (Publishers Weekly)
        #https://www.publishersweekly.com/pw/by-topic/columns-and-blogs/soapbox/article/13598-the-art-of-the-blurb.html

        #Robert McCrum considers the blurb so hyperbolic a form as to
        #require an anti-lexicon. "Intense," he argues, really means "quite
        #boring" and "magisterial" translates to "too long."
        "Intense and magisterial.",
        #"%s has done us all an immense service by compiling this collection." % author,
        #"%s has done us all an immense service by compiling this book." % author,
        "%s has done us all an immense service by writing this book." % author_surname,
        #"%s has done us all an immense service by compiling this book." % author_surname,
        #"Roy is the Obi-Wan Kenobi of [writing teachers]."
        "%s is the Obi-Wan Kenobi of writing." % author,
        "%s is the Obi-Wan Kenobi of writing." % author_surname,
        "%s is beautifully carpentered, the prose equivalent of a Shaker table." % random.choice(("The book", "This book", bookname)),

        #"This is the most useful book of its kind I've seen since
        #William Zinsser's On Writing Well. The format is lucid and concise.
        #The examples are brilliantly chosen."
        #"[Roy Peter Clark] knows more about [writing] than anybody I know who is not currently dead."
        "%s knows more about writing than anybody I know who is not dead." % (author_surname),
        "%s knows more about writing than anybody I know who is not currently dead." % (author_surname),
        "%s knows more about writing than anybody I know who is not dead." % (author_surname),
        "%s knows more about writing than anybody I know who is not currently dead." % (author_surname),

        "You can hear %s's heart thumping on every page." % (author_surname),
        "You can hear %s's heart thumping away on every page." % (author),
        "You can hear %s's heart thumping feverishly on every page." % (author_surname),
        "You can hear %s's heart thumping feverishly on every page." % (author),
        #misquoting Egger's blurb for Nathan Englander's What We Talk About When We Talk About Anne Frank.
        #blurb from the Sunday Times, quoted by George Orwell in 1936 :
        "If you can read this book and not shriek with delight, your soul is dead.",
        #William F. Buckley relates how publishers provided him with sample
        #blurb templates (1):
        "I was stunned by the power of %s. This book will change your life." % bookname,
        #William F. Buckley relates how publishers provided him with sample
        #blurb templates (2):
        "%s expresses an emotional depth that moves me beyond anything I have experienced in a book." % (bookname),
        "I couldn't put %s book down." % (random.choice(("the", "this"))),
        #"I couldn't put the book down.” % random.choice(("the", "this")),
        #"[Mr. Levinovitz]'s effort is certainly an entertaining and worthy one.",
        "%s's effort is certainly an entertaining and worthy one." % author,
        ))

    newblurb = '%s%s%s' % (quotechar, newblurb, quotechar)
    if blurb == "":
        return newblurb
    else:
        return "%s\n%s" % (blurb, newblurb)


def blurb_type_91(blurb, quotechar='"', author=None, bookname=None):
    descriptions = ["beautiful", "well composed", "eloquent", "life affirming", "inspiring",
                    "bitter-sweet", "genre defining"]

    d1 = random.choice(descriptions)
    descriptions.remove(d1)
    d2 = random.choice(descriptions)
    descriptions.remove(d2)
    d3 = random.choice(descriptions)
    descriptions.remove(d3)

    newblurb = "The most %s, %s, %s, %s I have ever had the good fortune to %s." % (d1, d2,d3,
                                                                                    random.choice(("book",
                                                                                                   "book",
                                                                                                   "work")),
                                                                                    random.choice(("come across",
                                                                                                   "hold in my hands")))

    newblurb = '%s%s%s' % (quotechar, newblurb, quotechar)
    if blurb == "":
        return newblurb
    else:
        return "%s\n%s" % (blurb, newblurb)


def blurb_type_92(blurb, quotechar='"', author=None, bookname=None):
    """blurbs quoted in either the following article or comments on it in the comments section:
https://www.theguardian.com/books/booksblog/2010/jul/06/david-grossman-nicole-krauss-blurb"""

    if author == None:
        author = names.getName()
    if bookname == None:
        bookname = "THIS BOOK"

    author_split = string.split(author)
    if len(author_split) == 2:
        author_surname = author_split[1]
    else:
        #guess that there are multiple surnames rather than multiple first names...
        author_surname = string.join(author_split[1:])

    author_firstname = author_split[0]
    if author_firstname in names.male_firstnames:
        gender_word = "he"
    elif author_firstname in names.female_firstnames:
        gender_word = "she"
    else:
        #whatever.
        gender_word = "he"

    newblurb = random.choice((
                              #Nicole Krauss's praise for David Grossman's To the End of the Land...
                              "The most gifted writer I've ever read.",
                              "%s is the most gifted writer I've ever read." % author,
                              "%s may be the most gifted writer I've ever read." % author,
                              "%s is the most gifted writer I've ever read." % author_surname,
                              "%s may be the most gifted writer I've ever read." % author_surname,
                              "I devoured this %s in a feverish trance." % random.choice(("volume",
                                                                                          "book",
                                                                                          #"collection",
                                                                                          "book",
                                                                                          "work")),
                              "The mystery of this book is why ownership of a copy has not been made mandatory by law.",
                              "I was enamoured, beguiled and enraptured on reading %s, Therefore, I also urge you to." % (random.choice(("it", bookname))),
                              "I was %s on reading %s, Therefore, I also urge you to." % (random.choice(("enamoured",
                                                                                                         "beguiled",
                                                                                                         "enraptured")),
                                                                                          random.choice(("it",
                                                                                                         bookname))),
                              "%s doesn't just write like a god, %s is one!" % (author, gender_word),
                              "To call %s the best %s I've ever read belittles it: it is one of the best books I've ever been fortunate enough to hold in my hands." % (random.choice(("it", bookname)),
                                                                                                                                                                        random.choice(("first book",
                                                                                                                                                                                       "non-fiction book"))),
                              #Zadie Smith's White Teeth, reviewed by The Times
                              "Do believe the hype, buy into it, curl up with it, savour every sentence, then turn around and reread.",
                              #...of anything that contained words.
                              ))
    newblurb = '%s%s%s' % (quotechar, newblurb, quotechar)
    if blurb == "":
        return newblurb
    else:
        return "%s\n%s" % (blurb, newblurb)


def blurb_type_93(blurb, quotechar='"', author=None, bookname=None):
    """blurbs made up from variations on the following quote:
    'Great in parts, awful in others. Probably the most entertaining
    ludicrous, funny, idiotic, boring and fascinating book of the
    year.'"""

    if author == None:
        author = names.getName()
    if bookname == None:
        bookname = "THIS BOOK"

    newblurb = random.choice(("Great in parts, awful in others. Probably the most entertaining ludicrous, funny, idiotic, boring and fascinating book of the year.",
                              "Probably the most entertaining, ludicrous, funny, idiotic, boring and fascinating book of the year.",
                              "Great in parts, awful in others.",
                              "Probably the most entertaining... funny... fascinating book of the year.",
                              "%s is great in parts, awful in others. Probably the most entertaining ludicrous, funny, idiotic, boring and fascinating book of the year." % bookname,
                              "%s is probably the most entertaining, ludicrous, funny, idiotic, boring and fascinating book of the year." % bookname,
                              "%s is great in parts, awful in others." % bookname,
                              "%s is probably the most entertaining... funny... fascinating book of the year." % bookname,
                              ))
    newblurb = '%s%s%s' % (quotechar, newblurb, quotechar)
    if blurb == "":
        return newblurb
    else:
        return "%s\n%s" % (blurb, newblurb)


def blurb_type_94(blurb, quotechar='"', author=None, bookname=None):

    if author == None:
        author = names.getName()
    if bookname == None:
        bookname = "THIS BOOK"

    author_firstname = string.split(author)[0]
    if author_firstname in names.male_firstnames:
        gender_word2 = "he"
        gender_word4 = "his"
    elif author_firstname in names.female_firstnames:
        gender_word2 = "she"
        gender_word4 = "her"
    else:
        #whatever.
        gender_word2 = "he"
        gender_word4 = "his"

    newblurb = random.choice(("Entertaining, enlightening and, occasionally, hilarious.",
                              '%s is so good it physically aroused me. FIVE STARS!' % bookname,
                              "Huge, important, dazzling, incandescent.",
                              'So good it physically aroused me. FIVE STARS!',
                              "The greatest living writer.",
                              "%s is the greatest living writer." % author,
                              "Swell Book! Loved It!",
                              "I would read %s on the history of Quonset huts." % author,
                              "I would read %s on the properties of concrete." % author,
                              #"The fact that %s wrote this in 20 minutes, hung over in bed and dressed in %s rubber-ducky pajamas, bespeaks of his superior talent." % (author,gender_word4),
                              "The fact that %s wrote this in %s, hung over in bed and dressed in %s rubber-ducky pajamas, bespeaks of %s superior talent." % (random.choice((author,gender_word2)),
                                                                                                                                                               random.choice(("an hour",
                                                                                                                                                                              "a few hours",
                                                                                                                                                                              "a couple of hours")),
                                                                                                                                                               gender_word4,
                                                                                                                                                               gender_word4)


        ))

    newblurb = '%s%s%s' % (quotechar, newblurb, quotechar)
    if blurb == "":
        return newblurb
    else:
        return "%s\n%s" % (blurb, newblurb)


def blurb_type_95(blurb, quotechar='"', author=None, bookname=None):

    if author == None:
        author = names.getName()

    newblurb = random.choice(("This book will change your life.",
                              "This book will change the way you see things.",
                              "Excellent, original and very enjoyable.",
                              "Meticulously crafted... doesn't pull any punches.",
                              "Meticulously crafted.",
                              "Doesn't pull any punches.",
                              "The best book I have read this year.",
                              #The great spirit of [Frank McGuinness] radiates in this magnificent [novel].",
                              "The great spirit of %s radiates in this magnificent %s." % (author, random.choice(("book", "book", "work", "volume"))),
                              #"[Madden] is the constant genius of [Irish letters].",
                              "%s is the constant genius of writing." % (author),
                              "%s is the constant genius of literature." % (author),
                              "Could any book be better? Did it even need to be as tremendous as this?",
                              "Could any book be better?",
                              "Did it even need to be as tremendous as this?",
                              "I mean, I like a good book, but this is ridiculous.",
                              "Engaging, funny and inventive.",
                              "Terrific. Engaging, funny and inventive.",
                              "Intensely engaging, and indefatigably inventive.",
                              "Intensely engaging, riotously funny and, indefatigably inventive.",
                              "Revelatory and groundbreaking.",
                              "This book is actually pretty good, as it turns out.",

                          ))

    newblurb = '%s%s%s' % (quotechar, newblurb, quotechar)
    if blurb == "":
        return newblurb
    else:
        return "%s\n%s" % (blurb, newblurb)


def blurb_type_96(blurb, quotechar='"', author=None, bookname=None):
    """Collection of various random blurbs"""

    if author == None:
        author = names.getName()
    tempsep = random.choice((", ", ", ", " - "))
    newblurb = random.choice(("A masterpiece of luminous writing.",
                              "A consumate example of luminous writing.",
                              #"A consumate example of writing.",
                              "%s is a certified genius and %s is a revelation." % (author, bookname),
                              "%s is a certified genius and this book is a revelation!" % author,

                              "Run%sdon't walk%sto buy this book%s" % (tempsep,
                                                                       tempsep,
                                                                       random.choice(("!","!","."))),
                              "Run%sdon't walk%sto buy %s%s" % (tempsep,
                                                                tempsep,
                                                                bookname,
                                                                random.choice(("!","!","."))),

                              ))

    newblurb = '%s%s%s' % (quotechar, newblurb, quotechar)
    if blurb == "":
        return newblurb
    else:
        return "%s\n%s" % (blurb, newblurb)


def blurb_type_97(blurb, quotechar='"', author=None, bookname=None):
    """One-word blurbs."""

    newblurb = random.choice(("Brilliant",
                               "Engrossing",
                               "Profound",
                               "Compelling",
                               "Riveting",
                               "Electrifying",
                               "Huge",
                               "Important",
                               "Dazzling",
                               "Incandescent",
                               "Flawless"
                               ))
    endchar = random.choice(("!", "!", "."))
    newblurb = '%s%s%s%s' % (quotechar, newblurb, endchar, quotechar)
    if blurb == "":
        return newblurb
    else:
        return "%s\n%s" % (blurb, newblurb)


def blurb_type_98(blurb, quotechar='"', author=None, bookname=None):
    """ 'True reader reactions' :)..."""

    newblurb = (random.choice(("I hated this.",
                               "Unbelievably tedious.",
                               "Disappointingly mediocre.",
                               "Probably the most repulsive thing I have ever read.",
                               "Absurdly overrated.",
                               "Badly written and full of cliches."
                               )))
    newblurb = '%s%s%s' % (quotechar, newblurb, quotechar)
    if blurb == "":
        return newblurb
    else:
        return "%s\n%s" % (blurb, newblurb)

def blurb_type_99(blurb, quotechar='"', author=None, bookname=None):
    """Random nonsense..."""
    
    newblurb = (random.choice(("The best use of neural networks since Star Trek's Commander Data.",
                               "Contains Barely Any Nanobots At All.",
                               "Does anyone actually read these blurbs?",
                               "Does anyone read these blurbs?",
                               "Does anybody actually read these blurbs?",
                               "Does anybody read these blurbs?"
                               )))
    newblurb = '%s%s%s' % (quotechar, newblurb, quotechar)
    if blurb == "":
        return newblurb
    else:
        return "%s\n%s" % (blurb, newblurb)




def do_blurb(quotechar='"', author=None, characters=None, main_character=None, bookname=None, num_blurbs=10, thisblurb=0):

    DEBUG = 1
    #DEBUG = 0

    if author == None:
        author = names.getName()

    if bookname == None:
        title = random.choice(source.index.index)
        while title[0] not in source.index.characters_dict.keys():
            title = random.choice(source.index.index)
        title = title[1]
        bookname, thisauthor = string.split(title, " by ")


    #num_blurbs = 1
    poss_types =["Type 1", "Type 2", "Type 3", "Type 4", "Type 5", "Type 6",
                 "Type 7", "Type 8", "Type 9", "Type 10", "Type 11", "Type 12",
                 #"Type 13", "Type 14", "Type 15", "Type 16", "Type 17", "Type 18",
                 "Type 13", "Type 16", "Type 17", "Type 18",
                 "Type 90", "Type 91", "Type 92", "Type 93", "Type 94",
                 "Type 95", "Type 96", "Type 97", "Type 98", "Type 99",
                 "Type 5A"]

    blurbs = ""
    b=""

    inner_poss_types = list(poss_types)

    for i in range(0, num_blurbs):
        thisblurb = thisblurb + 1
        if thisblurb == 1:
            b = blurb_type_00(b, quotechar=quotechar, author=author, bookname=bookname)
        #if i == 0:
            #b = blurb_type_00(b, quotechar=quotechar, author=author, bookname=bookname)
        else:
            blurbtype = random.choice(inner_poss_types)
            inner_poss_types.remove(blurbtype)
            if inner_poss_types == []:
                inner_poss_types = list(poss_types)

            if blurbtype == "Type 1":
                b = blurb_type_1(b, quotechar=quotechar, author=author, bookname=bookname)
            elif blurbtype == "Type 2":
                b = blurb_type_2(b, quotechar=quotechar, author=author, bookname=bookname)
            elif blurbtype == "Type 3":
                b = blurb_type_3(b, quotechar=quotechar, author=author, bookname=bookname)
            elif blurbtype == "Type 4":
                b = blurb_type_4(b, quotechar=quotechar, author=author, bookname=bookname)
            elif blurbtype == "Type 5":
                b = blurb_type_5(b, quotechar=quotechar, author=author, bookname=bookname)
            elif blurbtype == "Type 6":
                b = blurb_type_6(b, quotechar=quotechar, author=author, bookname=bookname)
            elif blurbtype == "Type 7":
                b = blurb_type_7(b, quotechar=quotechar, author=author, bookname=bookname)
            elif blurbtype == "Type 8":
                b = blurb_type_8(b, quotechar=quotechar, author=author, bookname=bookname)
            elif blurbtype == "Type 9":
                b = blurb_type_9(b, quotechar=quotechar, author=author, bookname=bookname)
            elif blurbtype == "Type 10":
                b = blurb_type_10(b, quotechar=quotechar, author=author, bookname=bookname)
            elif blurbtype == "Type 11":
                b = blurb_type_11(b, quotechar=quotechar, author=author, bookname=bookname)
            elif blurbtype == "Type 12":
                b = blurb_type_12(b, quotechar=quotechar, author=author, bookname=bookname)
            elif blurbtype == "Type 13":
                b = blurb_type_13(b, quotechar=quotechar, author=author, bookname=bookname)

            #stripped out "Type 14" and "Type 15" - not relevant to this project

            elif blurbtype == "Type 16":
                b = blurb_type_16(b, quotechar=quotechar, author=author, bookname=bookname)
            elif blurbtype == "Type 17":
                b = blurb_type_17(b, quotechar=quotechar, author=author, bookname=bookname)
            elif blurbtype == "Type 18":
                b = blurb_type_18(b, quotechar=quotechar, author=author, bookname=bookname)

            elif blurbtype == "Type 90":
                b = blurb_type_90(b, quotechar=quotechar, author=author, bookname=bookname)
            elif blurbtype == "Type 91":
                b = blurb_type_91(b, quotechar=quotechar, author=author, bookname=bookname)
            elif blurbtype == "Type 92":
                b = blurb_type_92(b, quotechar=quotechar, author=author, bookname=bookname)
            elif blurbtype == "Type 93":
                b = blurb_type_93(b, quotechar=quotechar, author=author, bookname=bookname)
            elif blurbtype == "Type 94":
                b = blurb_type_94(b, quotechar=quotechar, author=author, bookname=bookname)
            elif blurbtype == "Type 95":
                b = blurb_type_95(b, quotechar=quotechar, author=author, bookname=bookname)
            elif blurbtype == "Type 96":
                b = blurb_type_96(b, quotechar=quotechar, author=author, bookname=bookname)
            elif blurbtype == "Type 97":
                b = blurb_type_97(b, quotechar=quotechar, author=author, bookname=bookname)
            elif blurbtype == "Type 98":
                b = blurb_type_98(b, quotechar=quotechar, author=author, bookname=bookname)
            elif blurbtype == "Type 99":
                b = blurb_type_99(b, quotechar=quotechar, author=author, bookname=bookname)
            elif blurbtype == "Type 5A":
                b = blurb_type_5A(b, quotechar=quotechar, author=author, bookname=bookname)
            else:
                if DEBUG == 1:
                    print "ERROR!"
                    print "blurbtype: '%s'" % blurbtype
                    import sys;sys.exit(-01)
                else:
                    pass

            if DEBUG == 1:
                if b in ["", "\n", " ", "\n\n", None]:
                    print "ERROR!"
                    import sys;sys.exit(-01)
                 
        b = make_attribution(b)

        if blurbs != "":
            blurbs = b
        else:
            blurbs = "%s\n\n%s" % (blurbs, b)
    return blurbs
    #print b

def make_cover_copy(author, characters, main_character, bookname):
    """Convenience function. Calls make_content_summary and do_blurb.
    Returns a string"""

    covercopy = ""
    covercopy = make_content_summary(author=author, characters=characters, main_character=main_character, title=bookname)
    covercopy = "%s\n%s" % (covercopy, do_blurb('"', author=author, characters=characters, main_character=main_character, bookname=bookname))

    return covercopy


if __name__ == "__main__":

    author = names.getName()

    bookname = "THIS BOOK" # placeholders - should be replaced if used for an actual book...

    covercopy = make_cover_copy(author=author, characters=None, main_character=None, bookname=None)

    print "\n"
    print covercopy


