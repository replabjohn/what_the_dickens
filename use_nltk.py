#use_nltk.py

import string, os, random

from types import StringType, UnicodeType, ListType, TupleType

import check_exceptions

VERBOSE = 1
#VERBOSE = 0


#print a message here if in VERBOSE mode, since importing NLTK takes
#an appreciable time...
if VERBOSE > 0:
    print "Importing NLTK..."

import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords, wordnet
from nltk.stem import PorterStemmer, WordNetLemmatizer

if VERBOSE == 1:
    print "NLTK imported OK.\n"


__VERSION__ = "0.06b"



def split_into_paras(text):
    """Simply splits text into paragraphs by splitting on the string '\n\n'"""
    paras = string.split(text, "\n\n")
    return paras

def split_into_sentences(text):
    """uses NLTK tokeniser?"""
    return sent_tokenize(text)

def split_into_words(text):
    """uses NLTK tokeniser?"""
    return word_tokenize(text)


##def replace_adjective(text):
##    """
##
##JJ: adjective or numeral, ordinal
##    third ill-mannered pre-war regrettable oiled calamitous first separable
##    ectoplasmic battery-powered participatory fourth still-to-be-named
##    multilingual multi-disciplinary ...
##JJR: adjective, comparative
##    bleaker braver breezier briefer brighter brisker broader bumper busier
##    calmer cheaper choosier cleaner clearer closer colder commoner costlier
##    cozier creamier crunchier cuter ...
##JJS: adjective, superlative
##    calmest cheapest choicest classiest cleanest clearest closest commonest
##    corniest costliest crassest creepiest crudest cutest darkest deadliest
##    dearest deepest densest dinkiest ...
##
##"""
##    #stub
##    #PLACEHOLDER
##    
##    return text
##

def get_stopwords():
    stop_words = set(stopwords.words("English"))
    return stop_words

def check_for_exceptions(word):
    """now a rwapper for check_exceptions.check_for_exceptions"""
    return check_exceptions.check_for_exceptions(word)


def get_synonym(word, POS_tag=None, VERBOSE=0):
    "uses wordnet to look up a synonym for the word 'word"""
    #VERY EXPERIMENTAL!

    #get Set of Synonmys (SynSet)
    synset = wordnet.synsets(word)
    if len(synset) == 0:
        #no synonyms found, just return the original word
        return word

    #now pick a random element to use
    element_to_use = random.choice(range(0,len(synset)))
    synonym = synset[element_to_use].lemmas()[0].name()

    if string.find(synonym, "_") > -1:
        #treat as a failure...
        #reject things like 'agate_line', 'first_gear',
        # 'basketball_team', 'universal_joint', 'sidereal_day' etc
        return word

    #These are a bit simplistic and don't allow for (some) exceptions...
    if POS_tag in ['IN', 'PRP', 'NN', 'CD', 'UH']:
        #These ones tend to screw up when supplying synonyms - just use the original.
        return word

    elif POS_tag == "VBG":
        #verb, present participle or gerund
        #telegraphing stirring focusing angering judging stalling lactating...
        #involveing -> involving
        if synonym[-1] == "e":
            synonym = "%sing" % synonym[:-1]
        #everything else...
        elif synonym[-3:] != "ing":
            synonym = "%sing" % synonym

    elif POS_tag == "VBN":
        #verb, past participle
        #multihulled dilapidated aerosolized chaired languished panelized used...
        if synonym[-2:] != "ed":
            if synonym[-1:] == "e":
                synonym = "%sd" % synonym
            elif synonym[-1] == "y":
                synonym = "%sied" % synonym[:-1]
            else:
                synonym = "%sed" % synonym

    elif POS_tag == "VBD":
        #verb, past tense
        #dipped pleaded swiped regummed soaked tidied convened halted registered...
        if synonym[-2:] != "ed":
            if synonym[-1:] == "e":
                synonym = "%sd" % synonym
            elif synonym[-1] == "y":
                synonym = "%sied" % synonym[:-1]

            elif synonym[-1] not in ["a", "e", "i", "o", "u"]:
                if synonym[-2] in ["a", "e", "i", "o", "u"]:
                    #double up final letter (eg, skim -> skimmed)
                    synonym = "%s%sed" % (synonym, synonym[-1:])
                else:
                    #... but not unless the verb ends in consonant + vowel + consonant
                    synonym = "%sed" % synonym

            else:
                synonym = "%sed" % synonym

    elif POS_tag == "NNS":
        #NNS: noun, common, plural
        #    undergraduates scotches bric-a-brac products bodyguards facets coasts...

        #party->parties etc
        if synonym[-1] == "y":
            synonym = "%sies" % synonym[:-1]
        #wolf->wolves, leaf->leaves etc 
        elif synonym[-1:] == "f":
            synonym = "%sves" % synonym[:-1]
        elif synonym[-2:] == "fs":
            synonym = "%sves" % synonym[:-2]
        #everything else
        elif synonym[-1:] != "s":
            synonym = "%ss" % synonym

    elif POS_tag == "RB":
        #adverb
        #occasionally unabatingly maddeningly adventurously professedly...
        #if synonym[-2:] != "ly":
        #    synonym = "%sly" % synonym
        pass

    elif POS_tag == "RBR":
        #adverb, comparative
        #further gloomier grander graver greater grimmer harder harsher...
        if synonym[-2:] != "er":
            synonym = "%ser" % synonym

    elif POS_tag == "RBS":
        #adverb, superlative
        #best biggest bluntest earliest farthest first furthest hardest..
        if synonym[-3:] != "est":
            synonym = "%sest" % synonym

    synonym = check_for_exceptions(string.lower(synonym))

    #check for case...
    if word == string.lower(word):
        synonym = string.lower(synonym)
    elif word == string.capwords(word):
        synonym = string.capwords(synonym)
    elif word == string.upper(word):
        synonym = string.upper(synonym)

    if VERBOSE > 0:
        if synonym != word:
            print "\tORIGINAL WORD:\t'%s'" % word
            print "\tSYNONYM:\t'%s'\n\n" % synonym

    return synonym


def get_stem(word):
    """get ths stem word for 'word'"""
    #stub
    #PLACEHOLDER

    ps = PorterStemmer()
    
    return word

def get_lemmas(word, pos=None):
    """gets the lemma for 'word'
    (similar to stem, but guaranteed to be a real word)

    pos is an optional part of speech tag"""
    #stub
    #PLACEHOLDER

    Lemmatizer = WordNetLemmatizer()
    lemma = None

    if pos != None:
        try:
            lemma = Lemmatizer.lemmatize(word, pos=pos)
        except KeyError:
           lemma = Lemmatizer.lemmatize(word) 

    return lemma


def get_pos_tags(text):
    """does Parts of Speech tagging for 'text'.

POS Tag info:

ADJ	    adjective	    new, good, high, special, big, local
ADP	    adposition	    on, of, at, with, by, into, under
ADV	    adverb	        really, already, still, early, now
CONJ	conjunction	    and, or, but, if, while, although
DET	    determiner, article	the, a, some, most, every, no, which
NOUN	noun	        year, home, costs, time, Africa
NUM	    numeral	        twenty-four, fourth, 1991, 14:24
PRT	    particle	    at, on, out, over per, that, up, with
PRON	pronoun	        he, their, her, its, my, I, us
VERB	verb	        is, say, told, given, playing, would
.	    punctuation marks	. , ; !
X	    other	        ersatz, esprit, dunno, gr8, univeristy


>>> nltk.help.upenn_tagset("..")
'': closing quotation mark
    ' ''
--: dash
    --
CC: conjunction, coordinating
    & 'n and both but either et for less minus neither nor or plus so
    therefore times v. versus vs. whether yet
CD: numeral, cardinal
    mid-1890 nine-thirty forty-two one-tenth ten million 0.5 one forty-
    seven 1987 twenty '79 zero two 78-degrees eighty-four IX '60s .025
    fifteen 271,124 dozen quintillion DM2,000 ...
DT: determiner
    all an another any both del each either every half la many much nary
    neither no some such that the them these this those
EX: existential there
    there
FW: foreign word
    gemeinschaft hund ich jeux habeas Haementeria Herr K'ang-si vous
    lutihaw alai je jour objets salutaris fille quibusdam pas trop Monte
    terram fiche oui corporis ...
IN: preposition or conjunction, subordinating
    astride among uppon whether out inside pro despite on by throughout
    below within for towards near behind atop around if like until below
    next into if beside ...
JJ: adjective or numeral, ordinal
    third ill-mannered pre-war regrettable oiled calamitous first separable
    ectoplasmic battery-powered participatory fourth still-to-be-named
    multilingual multi-disciplinary ...
JJR: adjective, comparative
    bleaker braver breezier briefer brighter brisker broader bumper busier
    calmer cheaper choosier cleaner clearer closer colder commoner costlier
    cozier creamier crunchier cuter ...
JJS: adjective, superlative
    calmest cheapest choicest classiest cleanest clearest closest commonest
    corniest costliest crassest creepiest crudest cutest darkest deadliest
    dearest deepest densest dinkiest ...
LS: list item marker
    A A. B B. C C. D E F First G H I J K One SP-44001 SP-44002 SP-44005
    SP-44007 Second Third Three Two * a b c d first five four one six three
    two
MD: modal auxiliary
    can cannot could couldn't dare may might must need ought shall should
    shouldn't will would
NN: noun, common, singular or mass
    common-carrier cabbage knuckle-duster Casino afghan shed thermostat
    investment slide humour falloff slick wind hyena override subhumanity
    machinist ...
NNP: noun, proper, singular
    Motown Venneboerger Czestochwa Ranzer Conchita Trumplane Christos
    Oceanside Escobar Kreisler Sawyer Cougar Yvette Ervin ODI Darryl CTCA
    Shannon A.K.C. Meltex Liverpool ...
NNPS: noun, proper, plural
    Americans Americas Amharas Amityvilles Amusements Anarcho-Syndicalists
    Andalusians Andes Andruses Angels Animals Anthony Antilles Antiques
    Apache Apaches Apocrypha ...
NNS: noun, common, plural
    undergraduates scotches bric-a-brac products bodyguards facets coasts
    divestitures storehouses designs clubs fragrances averages
    subjectivists apprehensions muses factory-jobs ...
PDT: pre-determiner
    all both half many quite such sure this
POS: genitive marker
    ' 's
PRP: pronoun, personal
    hers herself him himself hisself it itself me myself one oneself ours
    ourselves ownself self she thee theirs them themselves they thou thy us
PRP$: pronoun, possessive
    her his mine my our ours their thy your
RB: adverb
    occasionally unabatingly maddeningly adventurously professedly
    stirringly prominently technologically magisterially predominately
    swiftly fiscally pitilessly ...
RBR: adverb, comparative
    further gloomier grander graver greater grimmer harder harsher
    healthier heavier higher however larger later leaner lengthier less-
    perfectly lesser lonelier longer louder lower more ...
RBS: adverb, superlative
    best biggest bluntest earliest farthest first furthest hardest
    heartiest highest largest least less most nearest second tightest worst
RP: particle
    aboard about across along apart around aside at away back before behind
    by crop down ever fast for forth from go high i.e. in into just later
    low more off on open out over per pie raising start teeth that through
    under unto up up-pp upon whole with you
SYM: symbol
    % & ' '' ''. ) ). * + ,. < = > @ A[fj] U.S U.S.S.R * ** ***
TO: "to" as preposition or infinitive marker
    to
UH: interjection
    Goodbye Goody Gosh Wow Jeepers Jee-sus Hubba Hey Kee-reist Oops amen
    huh howdy uh dammit whammo shucks heck anyways whodunnit honey golly
    man baby diddle hush sonuvabitch ...
VB: verb, base form
    ask assemble assess assign assume atone attention avoid bake balkanize
    bank begin behold believe bend benefit bevel beware bless boil bomb
    boost brace break bring broil brush build ...
VBD: verb, past tense
    dipped pleaded swiped regummed soaked tidied convened halted registered
    cushioned exacted snubbed strode aimed adopted belied figgered
    speculated wore appreciated contemplated ...
VBG: verb, present participle or gerund
    telegraphing stirring focusing angering judging stalling lactating
    hankerin' alleging veering capping approaching traveling besieging
    encrypting interrupting erasing wincing ...
VBN: verb, past participle
    multihulled dilapidated aerosolized chaired languished panelized used
    experimented flourished imitated reunifed factored condensed sheared
    unsettled primed dubbed desired ...
VBP: verb, present tense, not 3rd person singular
    predominate wrap resort sue twist spill cure lengthen brush terminate
    appear tend stray glisten obtain comprise detest tease attract
    emphasize mold postpone sever return wag ...
VBZ: verb, present tense, 3rd person singular
    bases reconstructs marks mixes displeases seals carps weaves snatches
    slumps stretches authorizes smolders pictures emerges stockpiles
    seduces fizzes uses bolsters slaps speaks pleads ...
WDT: WH-determiner
    that what whatever which whichever
WP: WH-pronoun
    that what whatever whatsoever which who whom whosoever
WP$: WH-pronoun, possessive
    whose
WRB: Wh-adverb
    how however whence whenever where whereby whereever wherein whereof why
``: opening quotation mark
"""

    words = None
    tagged = None

    if type(text) in (StringType, UnicodeType):
        words = nltk.word_tokenize(text)
    elif type(text) in (ListType, TupleType):
        words = text    #assume we've already split on words...
    else:
        words = text    #assume we've already split on words...

    if words != None:
        tagged = nltk.pos_tag(words)

    return tagged



def modify_text(text, VERBOSE=0, d=None):
    """collects together all our text modification routines)"""

    stop_words = get_stopwords()

    paras = split_into_paras(text)

    paras_to_output = []

    OUTPUT = ""

    if d == None:
        chapter_dividers = "DUMMY-DUMMY-DUMMY"
        chapter_names = []
    else:
        if d.chapter_dividers == None:
            chapter_dividers = "DUMMY-DUMMY-DUMMY"
        else:
            chapter_dividers = d.chapter_dividers
        if d.chapter_names == None:
            chapter_names = []

    for para in paras:
        try:
            para = para.decode("UTF-8", "ignore")
        except:
            try:
                para = para.encode("UTF-8", "ignore")
            except:
                try:
                    para = para.decode("ascii", "ignore")
                except:
                    para = para.encode("ascii", "ignore")

        if OUTPUT != "":
            OUTPUT = "%s\n\n" % (OUTPUT)

        raw_para        = para
        para_to_output  = []
        para_with_info  = []

        raw_sentences = split_into_sentences(para)
        setences_to_output  = []
        setences_with_info  = []

        known_placeholder_elements = ["BOOK_FULL_TITLE", "BOOK_SHORT_TITLE", "BOOK_SHORT_TITLE_CAPS", "AUTHOR",
                                      "AUTHOR_CAPS", "CHARACTER_NAME_", "CHARACTER_NAME_CAPS_", "CHARACTER_",
                                      "_SURNAME", "_FIRSTNAME", "_FIRSTNAME_CAPS", "_SURNAME_CAPS"]

        for sent in raw_sentences:

            if OUTPUT != "":
                if sent != raw_sentences[0]:
                    OUTPUT = "%s " % (OUTPUT)

            if VERBOSE > 0:
                print "\n\n%s\n\n" % (20*"=")
                print "\nRAW SENTENCE:"
                print "sent:", sent

            raw_words = split_into_words(sent)
            words_to_output  = []
            words_info       = []
            words_with_info  = []
            # keep stopwords - no use to Natural Language Tool Kit,
            # but give us the 'framework' for our sentence.

            for w in range(0, len(raw_words)):
                #is it a placeholder?
                if w < len(raw_words)-1:
                    if VERBOSE > 1:
                        print "\t -- word:", raw_words[w]
                    if raw_words[w+1] == "]":
                        if w>0:
                            if raw_words[w-1] == "[":
                                word = "[%s]" % raw_words[w]
                                raw_words[w] = word
                                if VERBOSE > 1:
                                    print "!!! REPLACED '%s' WITH '[%s]' !!!" % (raw_words[w],raw_words[w])

            while "[" in raw_words:
                raw_words.remove("[")
            while "]" in raw_words:
                raw_words.remove("]")

            if VERBOSE > 0:
                print "\n\nRAW_WORDS (AFTER MODIFICATION):"
                print raw_words
                print;print

            tagged_words = get_pos_tags(raw_words)
            if VERBOSE > 0:
                print "\n\n****\nTAGGED_WORDS:\n**** %s\n\n****\n\n\n" % tagged_words

            adjective_types = ["JJR", "JJS", "JJ"]

            #JJ: adjective or numeral, ordinal
            #    third ill-mannered pre-war regrettable oiled calamitous first separable
            #JJR: adjective, comparative
            #    bleaker braver breezier briefer brighter brisker broader bumper busier
            #JJS: adjective, superlative
            #    calmest cheapest choicest classiest cleanest clearest closest commonest

            for w in range(0, len(raw_words)):
                word = raw_words[w]
                if VERBOSE >1:
                    print "tagged_words[w][1]:", tagged_words[w][1]
                    print "word:", word,

                if word in stop_words:
                    #stopwords will give the sentence its 'framework'
                    words_to_output.append(word)
                    words_info.append("STOPWORD")
                elif word in string.punctuation:
                    words_to_output.append(word)
                    words_info.append("PUNCTUATION")
                elif word[0] == "[" and word[-1] == "]":
                    #one of our placeholders.... pass through unaltered
                    words_to_output.append(word)
                    words_info.append("PLACEHOLDER")
                elif string.lower(string.strip(word)) == string.lower(string.strip(chapter_dividers)):
                    #pass through chapter headings unchanged
                    words_to_output.append(word)
                    words_info.append("CHAPTER WORD")
                elif string.strip(word) in chapter_names:
                    words_to_output.append(word)
                    words_info.append("CHAPTER WORD")
                elif tagged_words[w][1] in adjective_types:
                    try:
                        synonym = get_synonym(word.decode("ascii", "ignore"))
                    except:
                        synonym = get_synonym(word.encode("ascii", "ignore"))
                    words_to_output.append(synonym)
                    words_info.append("ADJECTIVE (REPLACED BY SYNONYM)")
                else:
#                    words_to_output.append("")
#                    words_info.append(None)
                    try:
                        synonym = get_synonym(word.decode("ascii", "ignore"), tagged_words[w][1], VERBOSE)
                    except:
                        synonym = get_synonym(word.encode("ascii", "ignore"), tagged_words[w][1], VERBOSE)
                    words_to_output.append(synonym)
                    #words_to_output.append(word)
                    words_info.append(tagged_words[w][1])

            if VERBOSE > 0:
                print "*** PARA:..."                    
                print words_to_output
                print words_info
                print "\n\n"

            for w in range(0, len(words_to_output)):
                if string.strip(words_to_output[w]) in ['s.', 's']:
                    #don't want spaces in between plurals and their final 's'
                    OUTPUT = "%s%s" % (OUTPUT, string.strip(words_to_output[w]))

                elif words_info[w] in ["PUNCTUATION", "POS"]:
                    if words_to_output[w] == "(":
                        OUTPUT = "%s %s" % (OUTPUT, string.strip(words_to_output[w]))
                    else:
                        OUTPUT = "%s%s" % (OUTPUT, string.strip(words_to_output[w]))
                    #OUTPUT = "%s%s" % (OUTPUT, string.strip(words_to_output[w]))

                elif words_info[w] == "RB":
                    #so we don't get eg "do n't" rather than "don't"
                    if string.find(words_to_output[w], "'") > -1:
                        OUTPUT = "%s%s" % (OUTPUT, string.strip(words_to_output[w]))
                    else:
                        OUTPUT = "%s %s" % (OUTPUT, string.strip(words_to_output[w]))

                elif words_info[w] == "PLACEHOLDER":
                    #OUTPUT = "%s%s " % (OUTPUT, words_to_output[w])
                    if w == 0:
                        OUTPUT = "%s%s" % (OUTPUT, string.strip(words_to_output[w]))
                    else:
                        OUTPUT = "%s %s" % (OUTPUT, string.strip(words_to_output[w]))
                else:
                    #if words_info[w-1] != "PUNCTUATION":
                    #    OUTPUT = "%s " % (OUTPUT)
                    if w == 0:
                        OUTPUT = "%s%s" % (OUTPUT, string.strip(string.capwords(words_to_output[w])))
                    else:
                        OUTPUT = "%s %s" % (OUTPUT, string.strip(words_to_output[w]))

            if VERBOSE > 1:
                print OUTPUT

    return OUTPUT


def demo(VERBOSE=0):

    """test routine, using the first three paragraphs of 'Great Expectations'."""

    sample_text = """My father's family name being [CHARACTER_001_SURNAME], and my Christian name [CHARACTER_001_FIRSTNAME], my
infant tongue could make of both names nothing longer or more explicit
than [CHARACTER_NAME_001]. So, I called myself [CHARACTER_NAME_001], and came to be called [CHARACTER_NAME_001].

I give [CHARACTER_001_SURNAME] as my father's family name, on the authority of his
tombstone and my sister, - Mrs. [CHARACTER_NAME_005], who married the blacksmith.
As I never saw my father or my mother, and never saw any likeness
of either of them (for their days were long before the days of
photographs), my first fancies regarding what they were like were
unreasonably derived from their tombstones. [CHARACTER_004_FIRSTNAME] shape of the letters on
my father's, gave me an odd idea that he was a square, stout, dark man,
with curly black hair. From the character and turn of the inscription,
"Also Georgiana Wife of the Above," I drew a childish conclusion that
my mother was freckled and sickly. To five little stone lozenges, each
about a foot and a half long, which were arranged in a neat row beside
their grave, and were sacred to the memory of five little brothers of
mine, - who gave up trying to get a living, exceedingly early in
that universal struggle, - I am indebted for a belief I religiously
entertained that they had all been born on their backs with their hands
in their trousers-pockets, and had never taken them out in this state of
existence.

Ours was the marsh country, down by the river, within, as the river
wound, twenty miles of the sea. My first most vivid and broad impression
of the identity of things seems to me to have been gained on a memorable
raw afternoon towards evening. At such a time I found out for certain
that this bleak place overgrown with nettles was the churchyard; and
that [CHARACTER_NAME_001], late of this parish, and also Georgiana wife of the
above, were dead and buried; and that Alexander, Bartholomew, Abraham,
Tobias, and Roger, infant children of the aforesaid, were also dead
and buried; and that the dark flat wilderness beyond the churchyard,
intersected with dikes and mounds and gates, with scattered cattle
feeding on it, was the marshes; and that the low leaden line beyond
was the river; and that the distant savage lair from which the wind was
rushing was the sea; and that the small bundle of shivers growing afraid
of it all and beginning to cry, was [CHARACTER_NAME_001].

"""

#split_into_para1 = string.split(sample_text, "\n\n")

#split_into_para = split_into_paras(sample_text)

#para1 = split_into_para[0]

#if split_into_para1 != split_into_para:
#    print "huh? split_into_para1 != split_into_para"

    print "\n"

    final_text = modify_text(sample_text, VERBOSE=VERBOSE)

    print "\n\n%s\n\n" % (20*"=")
    print "SAMPLE TEXT:"
    print sample_text
    print "\n\n%s\n\n" % (10*".")
    print "OUR NEW, REVISED TEXT:"
    print final_text

    print "\n\n%s\n\n" % (20*"=")




if __name__ == "__main__":
    print "\n%s (version: %s)" % (os.path.basename(__file__), __VERSION__ )
    demo(VERBOSE=VERBOSE)
