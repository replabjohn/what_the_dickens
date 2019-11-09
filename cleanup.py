#!/usr/local/bin/python
# -*- coding: UTF-8 -*-

#cleanup.py

"""
A module to remove some of the tautology, redundancy, repepititon,
purple prose and annoying phrases that Dickens is prone to... or at
least, those that we can catch.

"""

VERBOSE = 1
VERBOSE = 0

import string, io, StringIO
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

                #remove underscores indicating italics...
                #We'll just ignore them.
                "_":    {
                    "phrase"        :   "_",
                    "replacement"   :   ""
                    },

                #HACK!
                #Fix for a placeholder mangled by the above...
                "[INTROEND]":    {
                    "phrase"        :   "[INTROEND]",
                    "replacement"   :   "[INTRO_END]"
                    },

}

##TO ADD LATER...

#"jingled and jingled" -> "jingled"
#	#remove any instances of "X and X"?

#"alive this day" -> "alive today"
#	#remove some other instances of "this day"...?

#By-and-bye

#????
#"a Chinaman", 
#"a Lascar"

#Chinamen
#Lascars

def cleanup(text, VERBOSE=0, use_log=0):
    if use_log == 1:
        #LOGFILE = open("CLEANUP_LOG.txt", "w")
        LOGFILE = open("CLEANUP_LOG.txt", "a")
    for key in phrases_dict.keys():
        IN = phrases_dict[key]["phrase"]
        OUT = phrases_dict[key]["replacement"]
        if string.find(text, phrases_dict[key]["phrase"]):
            text = string.replace(text, IN, OUT)
            if VERBOSE == 1:
                print "\t REPLACED '%s' WITH '%s'" % (IN, OUT)
            if use_log == 1:
                LOGFILE.write("\t REPLACED '%s' WITH '%s'\n" % (IN, OUT))
        if string.find(text, string.capitalize(phrases_dict[key]["phrase"])):
            text = string.replace(text, string.capitalize(IN), string.capitalize(OUT))
            if VERBOSE == 1:
                print "\t REPLACED '%s' WITH '%s'" % (string.capitalize(IN), string.capitalize(OUT))
            if use_log == 1:
                LOGFILE.write("\t REPLACED '%s' WITH '%s'\n" % (string.capitalize(IN), string.capitalize(OUT)))
        if string.find(text, string.capwords(phrases_dict[key]["phrase"])):
            text = string.replace(text, string.capwords(IN), string.capwords(OUT))
            if VERBOSE == 1:
                print "\t REPLACED '%s' WITH '%s'" % (string.capwords(IN), string.capwords(OUT))
            if use_log == 1:
                LOGFILE.write("\t REPLACED '%s' WITH '%s'\n" % (string.capwords(IN), string.capwords(OUT)))
        if string.find(text, string.upper(phrases_dict[key]["phrase"])):
            text = string.replace(text, string.upper(IN), string.upper(OUT))
            if VERBOSE == 1:
                print "\t REPLACED '%s' WITH '%s'" % (string.upper(IN), string.upper(OUT))
            if use_log == 1:
                LOGFILE.write("\t REPLACED '%s' WITH '%s'\n" % (string.upper(IN), string.upper(OUT)))
        if use_log == 1:
            LOGFILE.write("\n")
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
