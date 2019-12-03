#!/usr/local/bin/python
# -*- coding: UTF-8 -*-

#cleanup.py

"""
A module to remove some of the tautology, redundancy, repetiton,
purple prose and annoying phrases that Dickens is prone to... or at
least, those that we can catch.

"""

VERBOSE = 1
VERBOSE = 0

__VERSION__ = "0.3a"

import string, io
import glob, os, random
import time, re


#Dictionary of phrases to replace. Used for simple instances of when one phrase (or even just a word)
#can be replaced by something simpler.

phrases_dict = {

                #numbers

                "eight-and-forty":    {
                    "phrase"        :   "eight-and-forty",
                    "replacement"   :   "forty-eight"
                    },

                "five-and-twenty":    {
                    "phrase"        :   "five-and-twenty",
                    "replacement"   :   "twenty-five"
                    },

                "one-and-twenty":    {
                    "phrase"        :   "one-and-twenty",
                    "replacement"   :   "twenty-one"
                    },
                "eight-and-twenty":    {
                    "phrase"        :   "eight-and-twenty",
                    "replacement"   :   "twenty-eight"
                    },

                "five-and-forty":    {
                    "phrase"        :   "five-and-forty",
                    "replacement"   :   "forty-five"
                    },

                "five-and-thirty":    {
                    "phrase"        :   "five-and-thirty",
                    "replacement"   :   "thirty-five"
                    },

                "two-and-thirty":    {
                    "phrase"        :   "two-and-thirty",
                    "replacement"   :   "thirty-two"
                    },

                "two-and-twenty":    {
                    "phrase"        :   "two-and-twenty",
                    "replacement"   :   "twenty-two"
                    },

                "eight-and-fifty":    {
                    "phrase"        :   "eight-and-fifty",
                    "replacement"   :   "fifty-eight"
                    },

                "eight-and-forty":    {
                    "phrase"        :   "eight-and-forty",
                    "replacement"   :   "forty-eight"
                    },

                "eight-and-twentieth":    {
                    "phrase"        :   "eight-and-twentieth",
                    "replacement"   :   "twenty-eighth"
                    },

                "eight-and-twenty":    {
                    "phrase"        :   "eight-and-twenty",
                    "replacement"   :   "twenty-eight"
                    },

                "five-and-fifty":    {
                    "phrase"        :   "five-and-fifty",
                    "replacement"   :   "fifty-five"
                    },

                "five-and-thirty":    {
                    "phrase"        :   "five-and-thirty",
                    "replacement"   :   "thirty-five"
                    },

                "four-and-twenty":    {
                    "phrase"        :   "four-and-twenty",
                    "replacement"   :   "twenty-four"
                    },

                "nine-and-twenty":    {
                    "phrase"        :   "nine-and-twenty",
                    "replacement"   :   "twenty-nine"
                    },

                "one-and-thirty":    {
                    "phrase"        :   "one-and-thirty",
                    "replacement"   :   "thirty-one"
                    },

                "one-and-twenty":    {
                    "phrase"        :   "one-and-twenty",
                    "replacement"   :   "twenty-one"
                    },

                "pepper-and-salt":    {
                    "phrase"        :   "pepper-and-salt",
                    "replacement"   :   "salt and pepper"
                    },

                "seven-and-twenty":    {
                    "phrase"        :   "seven-and-twenty",
                    "replacement"   :   "twenty seven"
                    },

                "six-and-ninety":    {
                    "phrase"        :   "six-and-ninety",
                    "replacement"   :   "ninety-six"
                    },

                "six-and-sixty":    {
                    "phrase"        :   "six-and-sixty",
                    "replacement"   :   "sixty-six"
                    },

                "six-and-thirty":    {
                    "phrase"        :   "six-and-thirty",
                    "replacement"   :   "thirty-six"
                    },

                "six-and-twenty":    {
                    "phrase"        :   "six-and-twenty",
                    "replacement"   :   "twenty-six"
                    },

                "three-and-forty":    {
                    "phrase"        :   "three-and-forty",
                    "replacement"   :   "forty-three"
                    },

                "three-and-thirty":    {
                    "phrase"        :   "three-and-thirty",
                    "replacement"   :   "thirty-three"
                    },

                "three-and-twenty":    {
                    "phrase"        :   "three-and-twenty",
                    "replacement"   :   "twenty-three"
                    },

                "five and thirty":    {
                    "phrase"        :   "five and thirty",
                    "replacement"   :   "thirty-five"
                    },

                "two and thirty":    {
                    "phrase"        :   "two and thirty",
                    "replacement"   :   "thirty-two"
                    },

                "eight and thirty":    {
                    "phrase"        :   "eight and thirty",
                    "replacement"   :   "thirty-eight"
                    },

                "five and forty":    {
                    "phrase"        :   "five and forty",
                    "replacement"   :   "forty-five"
                    },

                "eight and forty":    {
                    "phrase"        :   "eight and forty",
                    "replacement"   :   "forty-eight"
                    },

                #years

                "one thousand eight hundred and twenty-six":    {
                    "phrase"        :   "one thousand eight hundred and twenty-six",
                    "replacement"   :   "1826"
                    },

                "one thousand eight hundred and thirty-six":    {
                    "phrase"        :   "one thousand eight hundred and thirty-six",
                    "replacement"   :   "1836"
                    },

                "one thousand eight hundred and thirty-seven":    {
                    "phrase"        :   "one thousand eight hundred and thirty-seven",
                    "replacement"   :   "1837"
                    },

                "one thousand eight hundred and forty":    {
                    "phrase"        :   "one thousand eight hundred and forty",
                    "replacement"   :   "1840"
                    },

                "one thousand eight hundred and fifty-one":    {
                    "phrase"        :   "one thousand eight hundred and fifty-one",
                    "replacement"   :   "1851"
                    },

                "one thousand eight hundred and fifty-six":    {
                    "phrase"        :   "one thousand eight hundred and fifty-six",
                    "replacement"   :   "1856"
                    },

                "one thousand eight hundred and sixty-four":    {
                    "phrase"        :   "one thousand eight hundred and sixty-four",
                    "replacement"   :   "1864"
                    },

                "the year of our Lord":    {
                    "phrase"        :   "the year of our Lord",
                    "replacement"   :   "the year"
                    },


                #half-past [X] o'clock

                "half-past one o'clock":    {
                    "phrase"        :   "half-past one o'clock",
                    "replacement"   :   "half-past one"
                    },

                "half-past two o'clock":    {
                    "phrase"        :   "half-past two o'clock",
                    "replacement"   :   "half-past two"
                    },

                "half-past three o'clock":    {
                    "phrase"        :   "half-past three o'clock",
                    "replacement"   :   "half-past three"
                    },

                "half-past four o'clock":    {
                    "phrase"        :   "half-past four o'clock",
                    "replacement"   :   "half-past four"
                    },

                "half-past five o'clock":    {
                    "phrase"        :   "half-past five o'clock",
                    "replacement"   :   "half-past five"
                    },

                "half-past six o'clock":    {
                    "phrase"        :   "half-past six o'clock",
                    "replacement"   :   "half-past six"
                    },

                "half-past seven o'clock":    {
                    "phrase"        :   "half-past seven o'clock",
                    "replacement"   :   "half-past seven"
                    },

                "half-past eight o'clock":    {
                    "phrase"        :   "half-past eight o'clock",
                    "replacement"   :   "half-past eight"
                    },

                "half-past nine o'clock":    {
                    "phrase"        :   "half-past nine o'clock",
                    "replacement"   :   "half-past nine"
                    },

                "half-past ten o'clock":    {
                    "phrase"        :   "half-past ten o'clock",
                    "replacement"   :   "half-past ten"
                    },

                "half-past eleven o'clock":    {
                    "phrase"        :   "half-past eleven o'clock",
                    "replacement"   :   "half-past eleven"
                    },

                "half-past twelve o'clock":    {
                    "phrase"        :   "half-past twelve o'clock",
                    "replacement"   :   "half-past twelve"
                    },

                #other phrases

                "It appears, at first sight not unreasonable to suppose, that,":    {
                    "phrase"        :   "It appears, at first sight not unreasonable to suppose, that,",
                    "replacement"   :   "It appears, at first sight, that,"
                    },

                "by the express order of":    {
                    "phrase"        :   "by the express order of",
                    "replacement"   :   "by the order of"
                    },

                "this auspicious and comfortable state":    {
                    "phrase"        :   "this auspicious and comfortable state",
                    "replacement"   :   random.choice(("this auspicious state",
                                                       "this comfortable state",
                                                       "this state"))
                    },

                "possessed the inestimable merit":    {
                    "phrase"        :   "possessed the inestimable merit",
                    "replacement"   :   "possessed the merit"
                    },

                "Cock-and-a-Bull":    {
                    "phrase"        :   "Cock-and-a-Bull",
                    "replacement"   :   "cock-and-bull"
                    },

                "sparkled phosphorescently":    {
                    "phrase"        :   "sparkled phosphorescently",
                    "replacement"   :   "sparkled"
                    },

                "poor me, poor me,":    {
                    "phrase"        :   "poor me, poor me,",
                    "replacement"   :   "poor me"
                    },

                "jingled and jingled":    {
                    "phrase"        :   "jingled and jingled",
                    "replacement"   :   "jingled"
                    },

                "alive this day":    {
                    "phrase"        :   "alive this day",
                    "replacement"   :   "alive today"
                    },

                "years of age":    {
                    "phrase"        :   "years of age",
                    "replacement"   :   "years old"
                    },

                "had but newly":    {
                    "phrase"        :   "had but newly",
                    "replacement"   :   "had just"
                    },

                "to-morrow":    {
                    "phrase"        :   "to-morrow",
                    "replacement"   :   "tomorrow"
                    },
                
                "a-comin’":    {
                    "phrase"        :   "a-comin’",
                    "replacement"   :   "coming"
                    },

                "a-comin'":    {
                    "phrase"        :   "a-comin'",
                    "replacement"   :   "coming"
                    },

                "three-fourths":    {
                    "phrase"        :   "three-fourths",
                    "replacement"   :   "three-quarters"
                    },

                ", nay, ":    {
                    "phrase"        :   ", nay, ",
                    "replacement"   :   ", "
                    },

                "I record that I":    {
                    "phrase"        :   "I record that I",
                    "replacement"   :   "I"
                    },

                "from head to foot":    {
                    "phrase"        :   "from head to foot",
                    "replacement"   :   "from head to toe"
                    },

                ", as I have said already, ":    {
                    "phrase"        :   ", as I have said already, ",
                    "replacement"   :   ", "
                    },

                "I solemnly":    {
                    "phrase"        :   "I solemnly",
                    "replacement"   :   "I "
                    },

                "never once":    {
                    "phrase"        :   "never once",
                    "replacement"   :   "never"
                    },

                "connexion":    {
                    "phrase"        :   "connexion",
                    "replacement"   :   "connection"
                    },

                "such-like":    {
                    "phrase"        :   "such-like",
                    "replacement"   :   "such"
                    },

                ", I am grateful to say,":    {
                    "phrase"        :   ", I am grateful to say,",
                    "replacement"   :   ", "
                    },

                "&c.":    {
                    "phrase"        :   "&c.",
                    "replacement"   :   "etc."
                    },


                ", therefore, ":    {
                    "phrase"        :   ", therefore, ",
                    "replacement"   :   ", ."
                    },


                ", decidedly, ":    {
                    "phrase"        :   ", decidedly, ",
                    "replacement"   :   ", ."
                    },


}

phrases_dict_finals = {

                #anything that can't be in phrases_dict because it interfers with other keys...

                "one thousand eight hundred and fifty":    {
                    "phrase"        :   "one thousand eight hundred and fifty",
                    "replacement"   :   "1850"
                    },

}



##TO ADD LATER...

#"alive this day" -> "alive today"
#	#remove some other instances of "this day"...?

#By-and-bye

#????
#"a Chinaman", 
#"a Lascar"

#Chinamen
#Lascars

def cleanup(text, VERBOSE=0, use_log=0):
    DEBUG = 0
    #DEBUG = 1

    if use_log == 1:
        #LOGFILE = open("CLEANUP_LOG.txt", "w")
        LOGFILE = open("CLEANUP_LOG.txt", "a")
    ORIGINAL_LENGTH = len(string.split(text, " "))

    dict_keys = phrases_dict.keys()
    dict_keys.sort()

    for key in dict_keys:
        try:
            IN = phrases_dict[key]["phrase"].decode("UTF-8", "ignore")
            OUT = phrases_dict[key]["replacement"].decode("UTF-8", "ignore")
        except:
            IN = phrases_dict[key]["phrase"].encode("UTF-8", "ignore")
            OUT = phrases_dict[key]["replacement"].encode("UTF-8", "ignore")

        try:
            if string.find(text.decode("UTF-8", "ignore"), phrases_dict[key]["phrase"].decode("UTF-8", "ignore")) > -1:
                text = string.replace(text.decode("UTF-8", "ignore"), IN.decode("UTF-8", "ignore"), OUT.decode("UTF-8", "ignore"))
                if VERBOSE == 1:
                    print "\t REPLACED '%s' WITH '%s'" % (IN.decode("UTF-8", "ignore"), OUT.decode("UTF-8", "ignore"))
                if use_log == 1:
                    LOGFILE.write("\t REPLACED '%s' WITH '%s'\n" % (IN.decode("UTF-8", "ignore"), OUT.decode("UTF-8", "ignore")))
        except:
            try:
                if string.find(text.encode("UTF-8", "ignore"), phrases_dict[key]["phrase"].encode("UTF-8", "ignore")) > -1:
                    text = string.replace(text.encode("UTF-8", "ignore"), IN.encode("UTF-8", "ignore"), OUT.encode("UTF-8", "ignore"))
                    if VERBOSE == 1:
                        print "\t REPLACED '%s' WITH '%s'" % (IN.encode("UTF-8", "ignore"), OUT.encode("UTF-8", "ignore"))
                    if use_log == 1:
                        LOGFILE.write("\t REPLACED '%s' WITH '%s'\n" % (IN.encode("UTF-8", "ignore"), OUT.encode("UTF-8", "ignore")))
            except:
                #print "text:", text.decode("ascii", "ignore")
                #print "text:", text.encode("ascii", "ignore")
                #print """phrases_dict[key]["phrase"]:""", phrases_dict[key]["phrase"].decode("ascii", "ignore")
                #print text.encode("UTF-8", "ignore")
                #print IN.encode("UTF-8", "ignore")
                #print OUT.encode("UTF-8", "ignore")
                if string.find(text.encode("ascii", "ignore"), phrases_dict[key]["phrase"].decode("ascii", "ignore")) > -1:
                    text = string.replace(text.encode("UTF-8", "ignore"), IN.encode("UTF-8", "ignore"), OUT.encode("UTF-8", "ignore"))
                    if VERBOSE == 1:
                        print "\t REPLACED '%s' WITH '%s'" % (IN.encode("ascii", "ignore"), OUT.encode("ascii", "ignore"))
                    if use_log == 1:
                        LOGFILE.write("\t REPLACED '%s' WITH '%s'\n" % (IN.encode("ascii", "ignore"), OUT.encode("ascii", "ignore")))

        try:
            if string.find(text.decode("UTF-8", "ignore"), string.capitalize(phrases_dict[key]["phrase"].decode("UTF-8", "ignore"))) > -1:
                text = string.replace(text.decode("UTF-8", "ignore"), string.capitalize(IN).decode("UTF-8", "ignore"), string.capitalize(OUT).decode("UTF-8", "ignore"))
                if VERBOSE == 1:
                    print "\t REPLACED '%s' WITH '%s'" % (string.capitalize(IN).decode("UTF-8", "ignore"), string.capitalize(OUT).decode("UTF-8", "ignore"))
                if use_log == 1:
                    LOGFILE.write("\t REPLACED '%s' WITH '%s'\n" % (string.capitalize(IN).decode("UTF-8", "ignore"), string.capitalize(OUT).decode("UTF-8", "ignore")))
        except:
            try:
                if string.find(text.encode("UTF-8", "ignore"), string.capitalize(phrases_dict[key]["phrase"].encode("UTF-8", "ignore"))) > -1:
                    text = string.replace(text.encode("UTF-8", "ignore"), string.capitalize(IN).encode("UTF-8", "ignore"), string.capitalize(OUT).encode("UTF-8", "ignore"))
                    if VERBOSE == 1:
                        print "\t REPLACED '%s' WITH '%s'" % (string.capitalize(IN).encode("UTF-8", "ignore"), string.capitalize(OUT).encode("UTF-8", "ignore"))
                    if use_log == 1:
                        LOGFILE.write("\t REPLACED '%s' WITH '%s'\n" % (string.capitalize(IN).encode("UTF-8", "ignore"), string.capitalize(OUT).encode("UTF-8", "ignore")))
            except:
                #print "text:", text.decode("ascii", "ignore")
                #print """phrases_dict[key]["phrase"]:""", phrases_dict[key]["phrase"].decode("ascii", "ignore")
                if string.find(text.decode("ascii", "ignore"), string.capitalize(phrases_dict[key]["phrase"].decode("ascii", "ignore"))) > -1:
                    #print text.decode("ascii", "ignore")
                    #print string.capitalize(IN).encode("ascii", "ignore")
                    #print string.capitalize(OUT).encode("ascii", "ignore")
                    text = string.replace(text.decode("ascii", "ignore"), string.capitalize(IN).encode("ascii", "ignore"), string.capitalize(OUT).encode("ascii", "ignore"))
                    if VERBOSE == 1:
                        print "\t REPLACED '%s' WITH '%s'" % (string.capitalize(IN).encode("ascii", "ignore"), string.capitalize(OUT).encode("ascii", "ignore"))
                    if use_log == 1:
                        LOGFILE.write("\t REPLACED '%s' WITH '%s'\n" % (string.capitalize(IN).encode("ascii", "ignore"), string.capitalize(OUT).encode("ascii", "ignore")))

        try:
            if string.find(text.decode("UTF-8", "ignore"), string.capwords(phrases_dict[key]["phrase"].decode("UTF-8", "ignore"))) > -1:
                text = string.replace(text.decode("UTF-8", "ignore"), string.capwords(IN).decode("UTF-8", "ignore"), string.capwords(OUT).decode("UTF-8", "ignore"))
                if VERBOSE == 1:
                    print "\t REPLACED '%s' WITH '%s'" % (string.capwords(IN).decode("UTF-8", "ignore"), string.capwords(OUT).decode("UTF-8", "ignore"))
                if use_log == 1:
                    LOGFILE.write("\t REPLACED '%s' WITH '%s'\n" % (string.capwords(IN), string.capwords(OUT)))
        except:
            try:
                if string.find(text.encode("UTF-8", "ignore"), string.capwords(phrases_dict[key]["phrase"].encode("UTF-8", "ignore"))):
                    text = string.replace(text.encode("UTF-8", "ignore"), string.capwords(IN).encode("UTF-8", "ignore"), string.capwords(OUT).encode("UTF-8", "ignore"))
                    if VERBOSE == 1:
                        print "\t REPLACED '%s' WITH '%s'" % (string.capwords(IN).encode("UTF-8", "ignore"), string.capwords(OUT).encode("UTF-8", "ignore"))
                    if use_log == 1:
                        LOGFILE.write("\t REPLACED '%s' WITH '%s'\n" % (string.capwords(IN).encode("UTF-8", "ignore"), string.capwords(OUT).encode("UTF-8", "ignore")))
            except:
                #print text.encode("ascii", "ignore")
                #print string.capwords(phrases_dict[key]["phrase"].decode("ascii", "ignore"))
                #print text.encode("ascii", "ignore")
                #print string.capwords(IN).encode("ascii", "ignore")
                #print string.capwords(OUT).decode("ascii", "ignore")
                if string.find(text.encode("ascii", "ignore"), string.capwords(phrases_dict[key]["phrase"].decode("ascii", "ignore"))) > -1:
                    text = string.replace(text.encode("ascii", "ignore"), string.capwords(IN).encode("ascii", "ignore"), string.capwords(OUT).decode("ascii", "ignore"))
                    if VERBOSE == 1:
                        print "\t REPLACED '%s' WITH '%s'" % (string.capwords(IN).encode("ascii", "ignore"), string.capwords(OUT).decode("ascii", "ignore"))
                    if use_log == 1:
                        LOGFILE.write("\t REPLACED '%s' WITH '%s'\n" % (string.capwords(IN).encode("ascii", "ignore"), string.capwords(OUT).decode("ascii", "ignore")))

        try:
            if string.find(text.decode("UTF-8", "ignore"), string.upper(phrases_dict[key]["phrase"].decode("UTF-8", "ignore"))) > -1:
                text = string.replace(text.decode("UTF-8", "ignore"), string.upper(IN).decode("UTF-8", "ignore"), string.upper(OUT).decode("UTF-8", "ignore"))
                if VERBOSE == 1:
                    print "\t REPLACED '%s' WITH '%s'" % (string.upper(IN).decode("UTF-8", "ignore"), string.upper(OUT).decode("UTF-8", "ignore"))
                if use_log == 1:
                    LOGFILE.write("\t REPLACED '%s' WITH '%s'\n" % (string.upper(IN).decode("UTF-8", "ignore"), string.upper(OUT).decode("UTF-8", "ignore")))
        except:
            try:
                if string.find(text.encode("UTF-8", "ignore"), string.upper(phrases_dict[key]["phrase"].encode("UTF-8", "ignore"))) > -1:
                    text = string.replace(text.encode("UTF-8", "ignore"), string.upper(IN).encode("UTF-8", "ignore"), string.upper(OUT).encode("UTF-8", "ignore"))
                    if VERBOSE == 1:
                        print "\t REPLACED '%s' WITH '%s'" % (string.upper(IN).encode("UTF-8", "ignore"), string.upper(OUT).encode("UTF-8", "ignore"))
                    if use_log == 1:
                        LOGFILE.write("\t REPLACED '%s' WITH '%s'\n" % (string.upper(IN).encode("UTF-8", "ignore"), string.upper(OUT).encode("UTF-8", "ignore")))
            except:
                #print text.encode("ascii", "ignore")
                #print string.upper(phrases_dict[key]["phrase"].decode("ascii", "ignore"))
                #print text.encode("ascii", "ignore")
                #print string.upper(IN).encode("ascii", "ignore")
                #print string.upper(OUT).encode("ascii", "ignore")
                if string.find(text.encode("ascii", "ignore"), string.upper(phrases_dict[key]["phrase"].decode("ascii", "ignore"))):
                    text = string.replace(text.encode("ascii", "ignore"), string.upper(IN).encode("ascii", "ignore"), string.upper(OUT).encode("ascii", "ignore"))
                    if VERBOSE == 1:
                        print "\t REPLACED '%s' WITH '%s'" % (string.upper(IN).encode("ascii", "ignore"), string.upper(OUT).encode("ascii", "ignore"))
                    if use_log == 1:
                        LOGFILE.write("\t REPLACED '%s' WITH '%s'\n" % (string.upper(IN).encode("ascii", "ignore"), string.upper(OUT).encode("ascii", "ignore")))

    # now do the same for phrases_dict_finals - the shorter dict of things that can't be included in phrases_dict
    # because they interfer with other keys

    for key in phrases_dict_finals.keys():
        try:
            IN = phrases_dict_finals[key]["phrase"].decode("UTF-8", "ignore")
            OUT = phrases_dict_finals[key]["replacement"].decode("UTF-8", "ignore")
        except:
            IN = phrases_dict_finals[key]["phrase"].encode("UTF-8", "ignore")
            OUT = phrases_dict_finals[key]["replacement"].encode("UTF-8", "ignore")

        try:
            if string.find(text.decode("UTF-8", "ignore"), phrases_dict_finals[key]["phrase"].decode("UTF-8", "ignore")) > -1:
                text = string.replace(text.decode("UTF-8", "ignore"), IN.decode("UTF-8", "ignore"), OUT.decode("UTF-8", "ignore"))
                if VERBOSE == 1:
                    print "\t REPLACED '%s' WITH '%s'" % (IN.decode("UTF-8", "ignore"), OUT.decode("UTF-8", "ignore"))
                if use_log == 1:
                    LOGFILE.write("\t REPLACED '%s' WITH '%s'\n" % (IN.decode("UTF-8", "ignore"), OUT.decode("UTF-8", "ignore")))
        except:
            try:
                if string.find(text.encode("UTF-8", "ignore"), phrases_dict_finals[key]["phrase"].encode("UTF-8", "ignore")) > -1:
                    text = string.replace(text.encode("UTF-8", "ignore"), IN.encode("UTF-8", "ignore"), OUT.encode("UTF-8", "ignore"))
                    if VERBOSE == 1:
                        print "\t REPLACED '%s' WITH '%s'" % (IN.encode("UTF-8", "ignore"), OUT.encode("UTF-8", "ignore"))
                    if use_log == 1:
                        LOGFILE.write("\t REPLACED '%s' WITH '%s'\n" % (IN.encode("UTF-8", "ignore"), OUT.encode("UTF-8", "ignore")))
            except:
                if string.find(text.encode("ascii", "ignore"), phrases_dict_finals[key]["phrase"].decode("ascii", "ignore")) > -1:
                    text = string.replace(text.encode("UTF-8", "ignore"), IN.encode("UTF-8", "ignore"), OUT.encode("UTF-8", "ignore"))
                    if VERBOSE == 1:
                        print "\t REPLACED '%s' WITH '%s'" % (IN.encode("ascii", "ignore"), OUT.encode("ascii", "ignore"))
                    if use_log == 1:
                        LOGFILE.write("\t REPLACED '%s' WITH '%s'\n" % (IN.encode("ascii", "ignore"), OUT.encode("ascii", "ignore")))

        try:
            if string.find(text.decode("UTF-8", "ignore"), string.capitalize(phrases_dict_finals[key]["phrase"].decode("UTF-8", "ignore"))) > -1:
                text = string.replace(text.decode("UTF-8", "ignore"), string.capitalize(IN).decode("UTF-8", "ignore"), string.capitalize(OUT).decode("UTF-8", "ignore"))
                if VERBOSE == 1:
                    print "\t REPLACED '%s' WITH '%s'" % (string.capitalize(IN).decode("UTF-8", "ignore"), string.capitalize(OUT).decode("UTF-8", "ignore"))
                if use_log == 1:
                    LOGFILE.write("\t REPLACED '%s' WITH '%s'\n" % (string.capitalize(IN).decode("UTF-8", "ignore"), string.capitalize(OUT).decode("UTF-8", "ignore")))
        except:
            try:
                if string.find(text.encode("UTF-8", "ignore"), string.capitalize(phrases_dict_finals[key]["phrase"].encode("UTF-8", "ignore"))) > -1:
                    text = string.replace(text.encode("UTF-8", "ignore"), string.capitalize(IN).encode("UTF-8", "ignore"), string.capitalize(OUT).encode("UTF-8", "ignore"))
                    if VERBOSE == 1:
                        print "\t REPLACED '%s' WITH '%s'" % (string.capitalize(IN).encode("UTF-8", "ignore"), string.capitalize(OUT).encode("UTF-8", "ignore"))
                    if use_log == 1:
                        LOGFILE.write("\t REPLACED '%s' WITH '%s'\n" % (string.capitalize(IN).encode("UTF-8", "ignore"), string.capitalize(OUT).encode("UTF-8", "ignore")))
            except:
                if string.find(text.decode("ascii", "ignore"), string.capitalize(phrases_dict_finals[key]["phrase"].decode("ascii", "ignore"))) > -1:
                    text = string.replace(text.decode("ascii", "ignore"), string.capitalize(IN).encode("ascii", "ignore"), string.capitalize(OUT).encode("ascii", "ignore"))
                    if VERBOSE == 1:
                        print "\t REPLACED '%s' WITH '%s'" % (string.capitalize(IN).encode("ascii", "ignore"), string.capitalize(OUT).encode("ascii", "ignore"))
                    if use_log == 1:
                        LOGFILE.write("\t REPLACED '%s' WITH '%s'\n" % (string.capitalize(IN).encode("ascii", "ignore"), string.capitalize(OUT).encode("ascii", "ignore")))

        try:
            if string.find(text.decode("UTF-8", "ignore"), string.capwords(phrases_dict_finals[key]["phrase"].decode("UTF-8", "ignore"))) > -1:
                text = string.replace(text.decode("UTF-8", "ignore"), string.capwords(IN).decode("UTF-8", "ignore"), string.capwords(OUT).decode("UTF-8", "ignore"))
                if VERBOSE == 1:
                    print "\t REPLACED '%s' WITH '%s'" % (string.capwords(IN).decode("UTF-8", "ignore"), string.capwords(OUT).decode("UTF-8", "ignore"))
                if use_log == 1:
                    LOGFILE.write("\t REPLACED '%s' WITH '%s'\n" % (string.capwords(IN), string.capwords(OUT)))
        except:
            try:
                if string.find(text.encode("UTF-8", "ignore"), string.capwords(phrases_dict_finals[key]["phrase"].encode("UTF-8", "ignore"))):
                    text = string.replace(text.encode("UTF-8", "ignore"), string.capwords(IN).encode("UTF-8", "ignore"), string.capwords(OUT).encode("UTF-8", "ignore"))
                    if VERBOSE == 1:
                        print "\t REPLACED '%s' WITH '%s'" % (string.capwords(IN).encode("UTF-8", "ignore"), string.capwords(OUT).encode("UTF-8", "ignore"))
                    if use_log == 1:
                        LOGFILE.write("\t REPLACED '%s' WITH '%s'\n" % (string.capwords(IN).encode("UTF-8", "ignore"), string.capwords(OUT).encode("UTF-8", "ignore")))
            except:
                #print text.encode("ascii", "ignore")
                #print string.capwords(phrases_dict_finals[key]["phrase"].decode("ascii", "ignore"))
                #print text.encode("ascii", "ignore")
                #print string.capwords(IN).encode("ascii", "ignore")
                #print string.capwords(OUT).decode("ascii", "ignore")
                if string.find(text.encode("ascii", "ignore"), string.capwords(phrases_dict_finals[key]["phrase"].decode("ascii", "ignore"))) > -1:
                    text = string.replace(text.encode("ascii", "ignore"), string.capwords(IN).encode("ascii", "ignore"), string.capwords(OUT).decode("ascii", "ignore"))
                    if VERBOSE == 1:
                        print "\t REPLACED '%s' WITH '%s'" % (string.capwords(IN).encode("ascii", "ignore"), string.capwords(OUT).decode("ascii", "ignore"))
                    if use_log == 1:
                        LOGFILE.write("\t REPLACED '%s' WITH '%s'\n" % (string.capwords(IN).encode("ascii", "ignore"), string.capwords(OUT).decode("ascii", "ignore")))

        try:
            if string.find(text.decode("UTF-8", "ignore"), string.upper(phrases_dict_finals[key]["phrase"].decode("UTF-8", "ignore"))) > -1:
                text = string.replace(text.decode("UTF-8", "ignore"), string.upper(IN).decode("UTF-8", "ignore"), string.upper(OUT).decode("UTF-8", "ignore"))
                if VERBOSE == 1:
                    print "\t REPLACED '%s' WITH '%s'" % (string.upper(IN).decode("UTF-8", "ignore"), string.upper(OUT).decode("UTF-8", "ignore"))
                if use_log == 1:
                    LOGFILE.write("\t REPLACED '%s' WITH '%s'\n" % (string.upper(IN).decode("UTF-8", "ignore"), string.upper(OUT).decode("UTF-8", "ignore")))
        except:
            try:
                if string.find(text.encode("UTF-8", "ignore"), string.upper(phrases_dict_finals[key]["phrase"].encode("UTF-8", "ignore"))) > -1:
                    text = string.replace(text.encode("UTF-8", "ignore"), string.upper(IN).encode("UTF-8", "ignore"), string.upper(OUT).encode("UTF-8", "ignore"))
                    if VERBOSE == 1:
                        print "\t REPLACED '%s' WITH '%s'" % (string.upper(IN).encode("UTF-8", "ignore"), string.upper(OUT).encode("UTF-8", "ignore"))
                    if use_log == 1:
                        LOGFILE.write("\t REPLACED '%s' WITH '%s'\n" % (string.upper(IN).encode("UTF-8", "ignore"), string.upper(OUT).encode("UTF-8", "ignore")))
            except:
                if string.find(text.encode("ascii", "ignore"), string.upper(phrases_dict_finals[key]["phrase"].decode("ascii", "ignore"))):
                    text = string.replace(text.encode("ascii", "ignore"), string.upper(IN).encode("ascii", "ignore"), string.upper(OUT).encode("ascii", "ignore"))
                    if VERBOSE == 1:
                        print "\t REPLACED '%s' WITH '%s'" % (string.upper(IN).encode("ascii", "ignore"), string.upper(OUT).encode("ascii", "ignore"))
                    if use_log == 1:
                        LOGFILE.write("\t REPLACED '%s' WITH '%s'\n" % (string.upper(IN).encode("ascii", "ignore"), string.upper(OUT).encode("ascii", "ignore")))



        if use_log == 1:
            LOGFILE.write("\n")

        #"jingled and jingled" -> "jingled"
        #	#remove any instances of "X and X"?

    #naive word split will do here. No need to tokenize it...
    words_split = string.split(text, " ")

    exceptions =["her"]

    # 'her' tends to be things like 'it lay between her and her lover' or
    #  'work-basket between her and her old attendant', which just become
    #  nonsense of you remove the "and her" bit.

    for w in range(1, len(words_split)-1):
        try:
            if words_split[w] == "and":
                if words_split[w-1] == words_split[w+1]:
                    if words_split[w-1] in exceptions:
                        pass
                    else:
                        if DEBUG == 1:
                            print "\nworking on bit '%s'..." % string.join(words_split[w-5:w+5])
                        converted = "%s %s %s" % (words_split[w-1], words_split[w], words_split[w+1])
                        converted_to = words_split[w-1]
                        if VERBOSE == 1:
                            print "\t \t ...REMOVING WORD '%s'..." % (words_split[w])
                        words_split.remove(words_split[w])
                        #we've removed words_split[w], so this removes what WAS words_split[w+1]
                        if VERBOSE == 1:
                            print "\t \t ...REMOVING WORD '%s'..." % (words_split[w])
                        words_split.remove(words_split[w])
                        
                        if VERBOSE == 1:
                            print "\t CONVERTED '%s' TO '%s'" % (converted, converted_to)
                        if use_log == 1:
                            LOGFILE.write("\t CONVERTED '%s' TO '%s'\n" % (converted, converted_to))
        except IndexError:
            #we've removed too many words. Must be at the end of the list now
            break
    text = string.join(words_split, " ")

    NEW_LENGTH = len(string.split(text, " "))
    DIFFERENCE = ORIGINAL_LENGTH - NEW_LENGTH

    if VERBOSE == 1:
        print "\n\t Original length of 'text':\t %s words" % ORIGINAL_LENGTH
        print "\t Length of revised 'text':\t %s words" % NEW_LENGTH
        print "\t Change:\t %s words" % DIFFERENCE
    if use_log == 1:
        LOGFILE.write("\n\n\t Original length of 'text':\t %s words\n" % ORIGINAL_LENGTH)
        LOGFILE.write("\t Length of revised 'text':\t %s words\n" % NEW_LENGTH)
        LOGFILE.write("\t Change:\t %s words\n\n\n" % DIFFERENCE)

    return text

def demo():
    startdir = os.getcwd()
    if os.path.isdir(os.path.join(startdir, "source", "raw")):
        os.chdir(os.path.join(startdir, "source", "raw"))
    all_samples = glob.glob("*.txt")
    example_textfn = random.choice(all_samples)
    #HACK!
    #Use Dombey and Son as a known text for testing...
    example_textfn = "821-0.txt"
    example_text = open(example_textfn, "r").read()
    os.chdir(startdir)

    LOGFILE = open("CLEANUP_LOG.txt", "w")
    LOGFILE.write("cleaning up file '%s'...\n\n" % (os.path.join(startdir, "source", "raw", example_textfn)))
    LOGFILE.close()
                   

    t = cleanup(example_text, VERBOSE=1, use_log=1)
    outfile = open("CLEANUP_SAMPLE.txt", "w")
    for line in t.split("\n"):
        outfile.write("%s\n" % line)


if __name__ == "__main__":
    demo()
