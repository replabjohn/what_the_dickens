#use_nltk.py

import string, os, random

from types import StringType, UnicodeType, ListType, TupleType

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


__VERSION__ = "0.05a"



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
    """check (and hopefully correct) for irregular and/or mangled
    words."""

    #probably better way to generalise this...
    #Use a dict?

    #-ed words
    if   word == "abandonned": return "abandoned"
    elif word == "abeted": return "abetted"
    elif word == "ablazed": return "ablaze"
    elif word == "abouted": return "near"
    elif word == "abstainned": return "abstained"
    elif word == "accreditted": return "accredited"
    elif word == "acclaimmed": return "acclaimed"
    elif word == "acquited": return "acquitted"
    elif word == "adjoinned": return "adjoined"
    elif word == "administerred": return "administered"
    elif word == "admited": return "admitted"
    elif word == "afraidded": return "afraid"
    elif word == "afraided": return "afraid"
    elif word == "aghasted": return "aghast"
    elif word == "aimmed": return "aimed"
    elif word == "airheadeds": return "airheaded"
    elif word == "airred": return "aired"
    elif word == "allowwed": return "allowed"
    elif word == "alterred": return "altered"
    elif word == "amucked": return "amuck"
    elif word == "anchorred": return "anchored"
    elif word == "annoied": return "annoyed"
    elif word == "answerred": return "answered"
    elif word == "appareled": return "apparelled"
    elif word == "appealled": return "appealed"
    elif word == "appearred": return "appeared"
    elif word == "applaudded": return "applauded"
    elif word == "arised": return "arose"
    elif word == "ascertainned": return "ascertained"
    elif word == "assailled": return "assailed"
    elif word == "auditted": return "audited"
    elif word == "availled": return "availed"
    elif word == "avoidded": return "avoided"
    elif word == "avowwed": return "avowed"
    elif word == "awakenned": return "awakened"
    elif word == "awfuled": return "awful"
    elif word == "baby-sitted": return "baby-sat"
    elif word == "badgerred": return "badgered"
    elif word == "battenned": return "battened"
    elif word == "beammed": return "beamed"
    elif word == "beared": return "born"
    elif word == "bearred": return "bore"
    elif word == "beated": return "beaten"
    elif word == "beatted": return "beat"
    elif word == "beckonned": return "beckoned"
    elif word == "becomed": return "became"
    elif word == "befited": return "befitted"
    elif word == "beged": return "begged"
    elif word == "beggarred": return "beggared"
    elif word == "begined": return "began"
    elif word == "beginned": return "began"
    elif word == "beholded": return "beheld"
    elif word == "bejeweled": return "bejewelled"
    elif word == "bellowwed": return "bellowed"
    elif word == "bented": return "bent"
    elif word == "beseted": return "beset"
    elif word == "besetted": return "beset"
    elif word == "bespeaked": return "bespoke"
    elif word == "bespeakked": return "bespoke"
    elif word == "bespoked": return "bespoke"
    elif word == "bestired": return "bestirred"
    elif word == "bestowwed": return "bestowed"
    elif word == "betraied": return "betrayed"
    elif word == "betterred": return "bettered"
    elif word == "betweenned": return "between"
    elif word == "bewilderred": return "bewildered"
    elif word == "bied": return "past"
    elif word == "billowwed": return "billowed"
    elif word == "binded": return "bound"
    elif word == "binded": return "bound"
    elif word == "bited": return "bit"
    elif word == "bitted": return "bit"
    elif word == "blisterred": return "blistered"
    elif word == "bloommed": return "bloomed"
    elif word == "blossommed": return "blossomed"
    elif word == "bloted": return "blotted"
    elif word == "blowed": return "blew"
    elif word == "blowned": return "blown"
    elif word == "blowwed": return "blowed"
    elif word == "blured": return "blurred"
    elif word == "boilled": return "boiled"
    elif word == "bookked": return "booked"
    elif word == "boommed": return "boomed"
    elif word == "borderred": return "bordered"
    elif word == "borned": return "born"
    elif word == "borrowwed": return "borrowed"
    elif word == "botherred": return "bothered"
    elif word == "bowwed": return "bowed"
    elif word == "boxxed": return "boxed"
    elif word == "braidded": return "braided"
    elif word == "braied": return "brayed"
    elif word == "breaked": return "broke"
    elif word == "breakked": return "broke"
    elif word == "brighted": return "bright"
    elif word == "brightenned": return "brightened"
    elif word == "bringed": return "brought"
    elif word == "brokened": return "broken"
    elif word == "brokenned": return "broken"
    elif word == "broodded": return "brooded"
    elif word == "buied": return "bought"
    elif word == "builded": return "built"
    elif word == "builted": return "built"
    elif word == "buoied": return "buoyed"
    elif word == "buryed": return "buried"
    elif word == "butterred": return "buttered"
    elif word == "buttonned": return "buttoned"
    elif word == "canceled": return "cancelled"
    elif word == "canterred": return "cantered"
    elif word == "careworned": return "careworn"
    elif word == "careworned": return "careworn"
    elif word == "cast-offed": return "cast-off"
    elif word == "casted": return "cast"
    elif word == "catched": return "caught"
    elif word == "cautionned": return "cautioned"
    elif word == "chainned": return "chained"
    elif word == "chainned": return "chained"
    elif word == "championned": return "championed"
    elif word == "chared": return "charred"
    elif word == "chatterred": return "chattered"
    elif word == "cheatted": return "cheated"
    elif word == "cheerred": return "cheered"
    elif word == "choosed": return "chose"
    elif word == "claimmed": return "claimed"
    elif word == "clamberred": return "clambered"
    elif word == "claped": return "clapped"
    elif word == "clatterred": return "clattered"
    elif word == "cleanned": return "cleaned"
    elif word == "clearred": return "cleared"
    elif word == "clearred": return "clearred"
    elif word == "clinged": return "clung"
    elif word == "cloged": return "clogged"
    elif word == "cloudded": return "clouded"
    elif word == "clusterred": return "clustered"
    elif word == "coilled": return "coiled"
    elif word == "colded": return "cold"
    elif word == "collarred": return "collared"
    elif word == "comed": return "came"
    elif word == "commissionned": return "commissioned"
    elif word == "commited": return "committed"
    elif word == "compeled": return "compelled"
    elif word == "complainned": return "complained"
    elif word == "concealled": return "concealed"
    elif word == "confered": return "conferred"
    elif word == "conquerred": return "conquered"
    elif word == "considerred": return "considered"
    elif word == "containned": return "contained"
    elif word == "controled": return "controlled"
    elif word == "conveied": return "conveyed"
    elif word == "cookings": return "cooking"
    elif word == "cookked": return "cooked"
    elif word == "coolled": return "cooled"
    elif word == "coverred": return "covered"
    elif word == "cramed": return "crammed"
    elif word == "creammed": return "creamed"
    elif word == "creeped": return "crept"
    elif word == "creepped": return "crept"
    elif word == "crimsonned": return "crimsoned"
    elif word == "croakked": return "croaked"
    elif word == "crookked": return "crooked"
    elif word == "croonned": return "crooned"
    elif word == "croped": return "cropped"
    elif word == "crowwed": return "crowed"
    elif word == "cushionned": return "cushioned"
    elif word == "cuted": return "cut"
    elif word == "cutted": return "cut"
    elif word == "dampenned": return "dampened"
    elif word == "darkenned": return "darkened"
    elif word == "daubbed": return "daubed"
    elif word == "deadded": return "dead"
    elif word == "deaded": return "dead"
    elif word == "deadenned": return "deadened"
    elif word == "deafed": return "deaf"
    elif word == "dealed": return "dealt"
    elif word == "dealled": return "dealt"
    elif word == "decaied": return "decayed"
    elif word == "decipherred": return "deciphered"
    elif word == "declaimmed": return "declaimed"
    elif word == "deemmed": return "deemed"
    elif word == "deep-seted": return "deep-set"
    elif word == "deepenned": return "deepened"
    elif word == "delaied": return "delayed"
    elif word == "deliverred": return "delivered"
    elif word == "demured": return "demurred"
    elif word == "depositted": return "deposited"
    elif word == "destroied": return "destroyed"
    elif word == "destroied": return "destroyed"
    elif word == "detailled": return "detailed"
    elif word == "detered": return "deterred"
    elif word == "developped": return "developed"
    elif word == "devourred": return "devoured"
    elif word == "diged": return "dug"
    elif word == "digged": return "dug"
    elif word == "dimed": return "dimmed"
    elif word == "diped": return "dipped"
    elif word == "disappearred": return "disappeared"
    elif word == "discoverred": return "discovered"
    elif word == "disemboweled": return "disembowelled"
    elif word == "disheveled": return "dishevelled"
    elif word == "disinheritted": return "disinherited"
    elif word == "dismaied": return "dismayed"
    elif word == "disorderred": return "disordered"
    elif word == "displaied": return "displayed"
    elif word == "ditherred": return "dithered"
    elif word == "doed": return "did"
    elif word == "doned": return "done"
    elif word == "doommed": return "doomed"
    elif word == "downcasted": return "downcast"
    elif word == "draged": return "dragged"
    elif word == "drainned": return "drained"
    elif word == "drawed": return "drew"
    elif word == "drawned": return "drawn"
    elif word == "drawwed": return "drew"
    elif word == "dreammed": return "dreamed"
    elif word == "drewed": return "drew"
    elif word == "drewwed": return "drew"
    elif word == "dried-uped": return "dried-up"
    elif word == "drinked": return "drank"
    elif word == "driped": return "dripped"
    elif word == "drived": return "drove"
    elif word == "driveled": return "drivelled"
    elif word == "drivened": return "driven"
    elif word == "drivenned": return "driven"
    elif word == "droopped": return "drooped"
    elif word == "droped": return "dropped"
    elif word == "drumed": return "drummed"
    elif word == "drunked": return "drunk"
    elif word == "duged": return "dug"
    elif word == "dwelled": return "dwelt"
    elif word == "eated": return "ate"
    elif word == "eatted": return "ate"
    elif word == "editted": return "edited"
    elif word == "embitterred": return "embittered"
    elif word == "embroilled": return "embroiled"
    elif word == "emited": return "emitted"
    elif word == "endangerred": return "endangered"
    elif word == "endowwed": return "endowed"
    elif word == "engenderred": return "engendered"
    elif word == "enjoied": return "enjoyed"
    elif word == "enlightenned": return "enlightened"
    elif word == "entailled": return "entailed"
    elif word == "enterred": return "entered"
    elif word == "enterred": return "entered"
    elif word == "entertainned": return "entertained"
    elif word == "envelopped": return "enveloped"
    elif word == "envisionned": return "envisioned"
    elif word == "equaled": return "equalled"
    elif word == "equiped": return "equipped"
    elif word == "esteemmed": return "esteemed"
    elif word == "exceled": return "excelled"
    elif word == "exclaimmed": return "exclaimed"
    elif word == "exhibitted": return "exhibited"
    elif word == "exitted": return "exited"
    elif word == "explainned": return "explained"
    elif word == "exploitted": return "exploited"
    elif word == "failled": return "failed"
    elif word == "falled": return "fell"
    elif word == "falterred": return "faltered"
    elif word == "faned": return "fanned"
    elif word == "fashionned": return "fashioned"
    elif word == "fastenned": return "fastened"
    elif word == "fathommed": return "fathomed"
    elif word == "fearred": return "feared"
    elif word == "feeled": return "felt"
    elif word == "feelled": return "felt"
    elif word == "feelled": return "felt"
    elif word == "felted": return "felt"
    elif word == "festerred": return "festered"
    elif word == "fighted": return "fought"
    elif word == "finded": return "found"
    elif word == "fited": return "fitted"
    elif word == "fixxed": return "fixed"
    elif word == "flattenned": return "flattened"
    elif word == "flatterred": return "flattered"
    elif word == "fleed": return "fled"
    elif word == "flexxed": return "flexed"
    elif word == "flickerred": return "flickered"
    elif word == "flied": return "flew"
    elif word == "flinged": return "flung"
    elif word == "fliped": return "flipped"
    elif word == "flited": return "flitted"
    elif word == "floatted": return "floated"
    elif word == "flowwed": return "flowed"
    elif word == "flusterred": return "flustered"
    elif word == "flutterred": return "fluttered"
    elif word == "foammed": return "foamed"
    elif word == "followwed": return "followed"
    elif word == "footted": return "footed"
    elif word == "forbidded": return "forbade"
    elif word == "forbided": return "forbade"
    elif word == "foresweared": return "foreswore"
    elif word == "foreswearred": return "foreswore"
    elif word == "forgeted": return "forgot"
    elif word == "forgetted": return "forgot"
    elif word == "forgived": return "forgave"
    elif word == "formated": return "formatted"
    elif word == "fosterred": return "fostered"
    elif word == "founderred": return "foundered"
    elif word == "freewheelled": return "freewheeled"
    elif word == "freezed": return "froze"
    elif word == "freshenned": return "freshened"
    elif word == "freted": return "fretted"
    elif word == "frightenned": return "frightened"
    elif word == "fritterred": return "frittered"
    elif word == "frolicced": return "frolicked"
    elif word == "froliced": return "frolicked"
    elif word == "functionned": return "functioned"
    elif word == "fured": return "furred"
    elif word == "furrowwed": return "furrowed"
    elif word == "gaged": return "gagged"
    elif word == "gaied": return "merry"
    elif word == "gainned": return "gained"
    elif word == "gallopped": return "galloped"
    elif word == "gatherred": return "gathered"
    elif word == "geted": return "got"
    elif word == "getted": return "got"
    elif word == "gived": return "gave"
    elif word == "givened": return "given"
    elif word == "gladdenned": return "gladdened"
    elif word == "gleammed": return "gleamed"
    elif word == "glitterred": return "glittered"
    elif word == "gloatted": return "gloated"
    elif word == "glowerred": return "glowered"
    elif word == "glowwed": return "glowed"
    elif word == "gnawwed": return "gnawed"
    elif word == "goadded": return "goaded"
    elif word == "goed": return "went"
    elif word == "grabed": return "grabbed"
    elif word == "graied": return "grayed"
    elif word == "greetted": return "greeted"
    elif word == "greied": return "greyed"
    elif word == "grinded": return "ground"
    elif word == "groanned": return "groaned"
    elif word == "growed": return "grew"
    elif word == "growwed": return "grew"
    elif word == "gutterred": return "guttered"
    elif word == "hailled": return "hailed"
    elif word == "halfed": return "halved"
    elif word == "hammerred": return "hammered"
    elif word == "handbuilded": return "handbuilt"
    elif word == "hankerred": return "hankered"
    elif word == "happenned": return "happened"
    elif word == "haulled": return "hauled"
    elif word == "haved": return "had"
    elif word == "headded": return "headed"
    elif word == "heapped": return "heaped"
    elif word == "hearded": return "heard"
    elif word == "heared": return "heard"
    elif word == "hearred": return "heard"
    elif word == "heatted": return "heated"
    elif word == "heelled": return "heeled"
    elif word == "heightenned": return "heightened"
    elif word == "hemed": return "hemmed"
    elif word == "hewwed": return "hewed"
    elif word == "hided": return "hid"
    elif word == "hited": return "hit"
    elif word == "hitted": return "hit"
    elif word == "holded": return "held"
    elif word == "hoodded": return "hooded"
    elif word == "hookked": return "hooked"
    elif word == "hoopped": return "hooped"
    elif word == "hootted": return "hooted"
    elif word == "hoverred": return "hovered"
    elif word == "huged": return "hugged"
    elif word == "humed": return "hummed"
    elif word == "hurted": return "hurt"
    elif word == "impairred": return "impaired"
    elif word == "impeled": return "impelled"
    elif word == "imprisonned": return "imprisoned"
    elif word == "inhabitted": return "inhabited"
    elif word == "inheritted": return "inherited"
    elif word == "inhibitted": return "inhibited"
    elif word == "injuried": return "injured"
    elif word == "interpretted": return "interpreted"
    elif word == "interviewwed": return "interviewed"
    elif word == "ironned": return "ironed"
    elif word == "jabed": return "jabbed"
    elif word == "jamed": return "jammed"
    elif word == "joged": return "jogged"
    elif word == "joied": return "joyed"
    elif word == "joinned": return "joined"
    elif word == "judderred": return "juddered"
    elif word == "keeped": return "kept"
    elif word == "keepped": return "kept"
    elif word == "kidnaped": return "kidnapped"
    elif word == "kneadded": return "kneaded"
    elif word == "kneelled": return "kneeled"
    elif word == "knited": return "knitted"
    elif word == "knowed": return "knew"
    elif word == "knowed": return "knew"
    elif word == "knowned": return "knew"
    elif word == "knowwed": return "knew"
    elif word == "labeled": return "labelled"
    elif word == "ladderred": return "laddered"
    elif word == "laidded": return "laid"
    elif word == "laided": return "laid"
    elif word == "laied": return "laid"
    elif word == "laudded": return "lauded"
    #elif word == "leadded": return "leaded"
    elif word == "leadded": return "led"
    elif word == "leakked": return "leaked"
    elif word == "leanned": return "leaned"
    elif word == "leapped": return "leaped"
    elif word == "leaved": return "left"
    elif word == "leerred": return "leered"
    elif word == "lefted": return "left"
    elif word == "lended": return "lent"
    elif word == "leted": return "let"
    elif word == "letted": return "let"
    elif word == "leveled": return "levelled"
    elif word == "libeled": return "libelled"
    elif word == "lightenned": return "lightened"
    elif word == "limitted": return "limited"
    elif word == "lingerred": return "lingered"
    elif word == "listenned": return "listened"
    elif word == "litterred": return "littered"
    elif word == "loadded": return "loaded"
    elif word == "loging": return "logging"
    elif word == "loiterred": return "loitered"
    elif word == "lookked": return "looked"
    elif word == "loommed": return "loomed"
    elif word == "loosenned": return "loosened"
    elif word == "lootted": return "looted"
    elif word == "losed": return "lost"
    elif word == "losted": return "lost"
    elif word == "lowerred": return "lowered"
    elif word == "lumberred": return "lumbered"
    elif word == "maded": return "made"
    elif word == "mailled": return "mailed"
    elif word == "maimmed": return "maimed"
    elif word == "maintainned": return "maintained"
    elif word == "maked": return "made"
    elif word == "maped": return "mapped"
    elif word == "mared": return "marred"
    elif word == "maritaled": return "married"
    elif word == "maritalled": return "married"
    elif word == "meaned": return "meant"
    elif word == "meanned": return "meant"
    elif word == "meeted": return "met"
    elif word == "meetted": return "met"
    elif word == "mellowwed": return "mellowed"
    elif word == "mentionned": return "mentioned"
    elif word == "meterred": return "metered"
    elif word == "mimicced": return "mimicked"
    elif word == "ministerred": return "ministered"
    elif word == "mirrorred": return "mirrored"
    elif word == "miserabled": return "miserable"
    elif word == "mislaided": return "mislaid"
    elif word == "misleaded": return "misled"
    elif word == "mistreatted": return "mistreated"
    elif word == "mixxed": return "mixed"
    elif word == "modeled": return "modelled"
    elif word == "moistenned": return "moistened"
    elif word == "moorred": return "moored"
    elif word == "murderred": return "murdered"
    elif word == "murmurred": return "murmured"
    elif word == "musterred": return "mustered"
    elif word == "nailled": return "nailed"
    elif word == "neted": return "netted"
    elif word == "niped": return "nipped"
    elif word == "noded": return "nodded"
    elif word == "numberred": return "numbered"
    elif word == "obeied": return "obeyed"
    elif word == "obtainned": return "obtained"
    elif word == "obtainned": return "obtained"
    elif word == "occasionned": return "occasioned"
    elif word == "occured": return "occurred"
    elif word == "offerred": return "offered"
    elif word == "openned": return "opened"
    elif word == "opinionned": return "opinioned"
    elif word == "ordainned": return "ordained"
    elif word == "orderred": return "ordered"
    elif word == "outgrowed": return "outgrew"
    elif word == "outspreadded": return "outspread"
    elif word == "outspreaded": return "outspread"
    elif word == "overcomed": return "overcame"
    elif word == "overdoed": return "overdid"
    elif word == "overflowwed": return "overflowed"
    elif word == "overjoied": return "overjoyed"
    elif word == "overlaied": return "overlaid"
    elif word == "overlookked": return "overlooked"
    elif word == "overpaied": return "overpaid"
    elif word == "overpowerred": return "overpowered"
    elif word == "overruned": return "overran"
    elif word == "overseed": return "oversaw"
    elif word == "overseing": return "overseeing"
    elif word == "overshadowwed": return "overshadowed"
    elif word == "overtaked": return "overtook"
    elif word == "overthrowed": return "overthrew"
    elif word == "overthrowwed": return "overthrew"
    elif word == "paded": return "padded"
    elif word == "paidded": return "paid"
    elif word == "paided": return "paid"
    elif word == "paied": return "paid"
    elif word == "painned": return "pained"
    elif word == "pamperred": return "pampered"
    elif word == "paneled": return "panelled"
    elif word == "panickied": return "panicked"
    elif word == "pardonned": return "pardoned"
    elif word == "partaked": return "partook"
    elif word == "partitionned": return "partitioned"
    elif word == "patterred": return "pattered"
    elif word == "peepped": return "peeped"
    elif word == "peerred": return "peered"
    elif word == "penciled": return "pencilled"
    elif word == "pepperred": return "peppered"
    elif word == "perennialed": return "perennial"
    elif word == "permited": return "permitted"
    elif word == "perplexxed": return "perplexed"
    elif word == "pilferred": return "pilfered"
    elif word == "pillowwed": return "pillowed"
    elif word == "pinionned": return "pinioned"
    elif word == "pited": return "pitted"
    elif word == "plaied": return "played"
    elif word == "pleadded": return "pleaded"
    elif word == "ploted": return "plotted"
    elif word == "pluged": return "plugged"
    elif word == "plunderred": return "plundered"
    elif word == "pocketted": return "pocketed"
    elif word == "poisonned": return "poisoned"
    elif word == "portraied": return "portrayed"
    elif word == "pourred": return "poured"
    elif word == "poutted": return "pouted"
    elif word == "praied": return "prayed"
    elif word == "preenned": return "preened"
    elif word == "prefered": return "preferred"
    elif word == "preied": return "preyed"
    elif word == "prevailled": return "prevailed"
    elif word == "proclaimmed": return "proclaimed"
    elif word == "proded": return "prodded"
    elif word == "profitted": return "profited"
    elif word == "profounded": return "profound"
    elif word == "propeled": return "propelled"
    elif word == "puckerred": return "puckered"
    elif word == "puted": return "put"
    elif word == "putted": return "put"
    elif word == "quarreled": return "quarrelled"
    elif word == "quarterred": return "quartered"
    elif word == "quaverred": return "quavered"
    elif word == "questionned": return "questioned"
    elif word == "quickenned": return "quickened"
    elif word == "quietenned": return "quietened"
    elif word == "quietted": return "quieted"
    elif word == "quiverred": return "quivered"
    elif word == "rainned": return "rained"
    elif word == "ramed": return "rammed"
    elif word == "readded": return "read"
    elif word == "readed": return "read"
    elif word == "reappearred": return "reappeared"
    elif word == "reapped": return "reaped"
    elif word == "rearred": return "reared"
    elif word == "reasonned": return "reasoned"
    elif word == "rebeled": return "rebelled"
    elif word == "rebuilded": return "rebuilt"
    elif word == "reckonned": return "reckoned"
    elif word == "reclaimmed": return "reclaimed"
    elif word == "recoverred": return "recovered"
    elif word == "recruitted": return "recruited"
    elif word == "recured": return "recurred"
    elif word == "reddenned": return "reddened"
    elif word == "reelled": return "reeled"
    elif word == "refered": return "referred"
    elif word == "refered": return "referred"
    elif word == "registerred": return "registered"
    elif word == "regreted": return "regretted"
    elif word == "rejoinned": return "rejoined"
    elif word == "relaxxed": return "relaxed"
    elif word == "remainned": return "remained"
    elif word == "rememberred": return "remembered"
    elif word == "rememberred": return "remembered"
    elif word == "remited": return "remitted"
    elif word == "renderred": return "rendered"
    elif word == "reopenned": return "reopened"
    elif word == "repairred": return "repaired"
    elif word == "repeatted": return "repeated"
    elif word == "repeled": return "repelled"
    elif word == "restrainned": return "restrained"
    elif word == "retainned": return "retained"
    elif word == "retoolled": return "retooled"
    elif word == "retreatted": return "retreated"
    elif word == "revealled": return "revealed"
    elif word == "reveled": return "revelled"
    elif word == "reviewwed": return "reviewed"
    elif word == "rided": return "rode"
    elif word == "riged": return "rigged"
    elif word == "riped": return "ripped"
    elif word == "ripenned": return "ripened"
    elif word == "rised": return "rose"
    elif word == "rivetted": return "riveted"
    elif word == "roarred": return "roared"
    elif word == "rootted": return "rooted"
    elif word == "rosed": return "rose"
    elif word == "rubed": return "rubbed"
    elif word == "ruinned": return "ruined"
    elif word == "runed": return "ran"      #assuming past tense of 'run' is more common than anything involving runes
    elif word == "runned": return "ran"
    elif word == "saged": return "sagged"
    elif word == "saied": return "said"
    elif word == "sailled": return "sailed"
    elif word == "sandbaged": return "sandbagged"
    elif word == "sandpaperred": return "sandpapered"
    elif word == "saturdaied": return "sat"
    elif word == "sawed": return "saw"
    elif word == "sawwed": return "sawed"
    elif word == "scaned": return "scanned"
    elif word == "scatterred": return "scattered"
    elif word == "scourred": return "scoured"
    elif word == "scoutted": return "scouted"
    elif word == "screammed": return "screamed"
    elif word == "screwwed": return "screwed"
    elif word == "sealled": return "sealed"
    elif word == "seammed": return "seamed"
    elif word == "seasonned": return "seasoned"
    elif word == "seatted": return "seated"
    elif word == "seed": return "saw"
    elif word == "seekked": return "sought"
    elif word == "seemmed": return "seemed"
    elif word == "selled": return "sold"
    elif word == "sended": return "sent"
    elif word == "seted": return "set"
    elif word == "setted": return "set"
    elif word == "severred": return "severed"
    elif word == "shadowwed": return "shadowed"
    elif word == "shaked": return "shook"
    elif word == "sharpenned": return "sharpened"
    elif word == "shatterred": return "shattered"
    elif word == "sheerred": return "sheered"
    elif word == "shelterred": return "sheltered"
    elif word == "shiped": return "shipped"
    elif word == "shiverred": return "shivered"
    elif word == "shooked": return "shook"
    elif word == "shookked": return "shook"
    elif word == "shooted": return "shot"
    elif word == "shootted": return "shot"
    elif word == "shoulderred": return "shouldered"
    elif word == "shoutted": return "shouted"
    elif word == "showerred": return "showered"
    elif word == "showwed": return "showed"
    elif word == "shriekked": return "shrieked"
    elif word == "shrinked": return "shrank"
    elif word == "shriveled": return "shrivelled"
    elif word == "shroudded": return "shrouded"
    elif word == "shudderred": return "shuddered"
    elif word == "shuted": return "shut"
    elif word == "shutted": return "shut"
    elif word == "sickenned": return "sickened"
    elif word == "sined": return "sinned"
    elif word == "singed": return "sang"
    elif word == "sinked": return "sank"
    elif word == "sitted": return "sat"
    elif word == "skimed": return "skimmed"
    elif word == "slackenned": return "slackened"
    elif word == "sleeped": return "slept"
    elif word == "sleepped": return "slept"
    elif word == "slimed": return "slimmed"
    elif word == "slinged": return "slung"
    elif word == "sliped": return "slipped"
    elif word == "slitherred": return "slithered"
    elif word == "sloged": return "slogged"
    elif word == "smearred": return "smeared"
    elif word == "smittened": return "smitten"
    elif word == "smittenned": return "smitten"
    elif word == "smotherred": return "smothered"
    elif word == "snaped": return "snapped"
    elif word == "sneakied": return "sneaked"
    elif word == "sneakked": return "sneaked"
    elif word == "sniveled": return "snivelled"
    elif word == "snowwed": return "snowed"
    elif word == "snubed": return "snubbed"
    elif word == "soarred": return "soared"
    elif word == "sobed": return "sobbed"
    elif word == "softenned": return "softened"
    elif word == "solded": return "sold"
    elif word == "solicitted": return "solicited"
    elif word == "sorrowwed": return "sorrowed"
    elif word == "soughted": return "sought"
    elif word == "sourred": return "soured"
    elif word == "spatterred": return "spattered"
    elif word == "speaked": return "spoke"
    elif word == "speakked": return "spoke"
    elif word == "spended": return "spent"
    elif word == "splutterred": return "spluttered"
    elif word == "spoilled": return "spoiled"
    elif word == "spoked": return "spoke"
    elif word == "sponsorred": return "sponsored"
    elif word == "spoted": return "spotted"
    elif word == "spreadded": return "spread"
    elif word == "spreaded": return "spread"
    elif word == "springed": return "sprang"
    #elif word == "springed": return "sprung"
    elif word == "spured": return "spurred"
    elif word == "sputterred": return "sputtered"
    elif word == "squated": return "squatted"
    elif word == "staggerred": return "staggered"
    elif word == "staied": return "stayed"
    elif word == "stainned": return "stained"
    elif word == "standed": return "stood"
    elif word == "stationned": return "stationed"
    elif word == "stealed": return "stole"
    elif word == "stealled": return "stole"
    elif word == "steammed": return "steamed"
    elif word == "steelled": return "steeled"
    elif word == "steepped": return "steeped"
    elif word == "steerred": return "steered"
    elif word == "stemed": return "stemmed"
    elif word == "steped": return "stepped"
    elif word == "sticked": return "stuck"
    elif word == "stiffenned": return "stiffened"
    elif word == "stired": return "stirred"
    elif word == "stoled": return "stole"
    elif word == "stoopped": return "stooped"
    elif word == "stoped": return "stopped"
    elif word == "stowwed": return "stowed"
    elif word == "straied": return "strayed"
    elif word == "strainned": return "strained"
    elif word == "streammed": return "streamed"
    elif word == "strengthenned": return "strengthened"
    elif word == "strewwed": return "strewed"
    elif word == "strided": return "strode"
    elif word == "striked": return "struck"
    elif word == "stucked": return "stuck"
    elif word == "stuned": return "stunned"
    elif word == "submited": return "submitted"
    elif word == "sufferred": return "suffered"
    elif word == "suitted": return "suited"
    elif word == "summonned": return "summoned"
    elif word == "sunged": return "sang"
    elif word == "surrenderred": return "surrendered"
    elif word == "surveied": return "surveyed"
    elif word == "sustainned": return "sustained"
    elif word == "swaggerred": return "swaggered"
    elif word == "swallowwed": return "swallowed"
    elif word == "sweared": return "swore"
    elif word == "sweeped": return "swept"
    elif word == "sweepped": return "swept"
    elif word == "sweetenned": return "sweetened"
    elif word == "swepted": return "swept"
    elif word == "swimed": return "swam"
    elif word == "swinged": return "swung"
    elif word == "tailled": return "tailed"
    elif word == "taked": return "taken"
    elif word == "takened": return "taken"
    elif word == "taxxed": return "taxed"
    elif word == "teached": return "taught"
    elif word == "teared": return "torn"
    elif word == "tearred": return "tore"
    elif word == "teemmed": return "teemed"
    elif word == "telled": return "told"
    elif word == "temperred": return "tempered"
    elif word == "tenderred": return "tendered"
    elif word == "thickenned": return "thickened"
    elif word == "thinked": return "thought"
    elif word == "thoughted": return "thought"
    elif word == "threatenned": return "threatened"
    elif word == "throwed": return "threw"
    elif word == "throwwed": return "threw"
    elif word == "thunderred": return "thundered"
    elif word == "tightenned": return "tightened"
    elif word == "toied": return "toyed"
    elif word == "toped": return "topped"
    elif word == "totaled": return "totalled"
    elif word == "towwed": return "towed"
    elif word == "trailled": return "trailed"
    elif word == "trainned": return "trained"
    elif word == "transfered": return "transferred"
    elif word == "transmited": return "transmitted"
    elif word == "traped": return "trapped"
    elif word == "traveled": return "travelled"
    elif word == "travelers": return "travellers"
    elif word == "treadded": return "trod"
    elif word == "treaded": return "trod"
    elif word == "treatted": return "treated"
    elif word == "tremorred": return "tremored"
    elif word == "trimed": return "trimmed"
    elif word == "triped": return "tripped"
    elif word == "troted": return "trotted"
    elif word == "tuged": return "tugged"
    elif word == "typeseted": return "typeset"
    elif word == "unbosommed": return "unbosomed"
    elif word == "unbrokened": return "unbroken"
    elif word == "unbrokenned": return "unbroken"
    elif word == "uncoverred": return "uncovered"
    elif word == "undergoed": return "underwent"
    elif word == "understanded": return "understood"
    elif word == "understoodded": return "understood"
    elif word == "understooded": return "understood"
    elif word == "undertaked": return "undertook"
    elif word == "unknowned": return "unknown"
    elif word == "unpluged": return "unplugged"
    elif word == "unscrewwed": return "unscrewed"
    elif word == "untrammeled": return "untrammelled"
    elif word == "unwraped": return "unwrapped"
    elif word == "upholded": return "upheld"
    elif word == "uprootted": return "uprooted"
    elif word == "upseted": return "upset"
    elif word == "upsetted": return "upset"
    elif word == "usherred": return "ushered"
    elif word == "utterred": return "uttered"
    elif word == "veilled": return "veiled"
    elif word == "viewwed": return "viewed"
    elif word == "visitted": return "visited"
    elif word == "volunteerred": return "volunteered"
    elif word == "vomitted": return "vomited"
    elif word == "vowwed": return "vowed"
    elif word == "vowwed": return "vowed"
    elif word == "wailled": return "wailed"
    elif word == "waitted": return "waited"
    elif word == "wallowwed": return "wallowed"
    elif word == "wallpaperred": return "wallpapered"
    elif word == "wanderred": return "wandered"
    elif word == "waxxed": return "waxed"
    elif word == "weared": return "wore"
    elif word == "wearred": return "wore"
    elif word == "weatherred": return "weathered"
    elif word == "wheelled": return "wheeled"
    elif word == "whisperred": return "whispered"
    elif word == "widenned": return "widened"
    elif word == "winnowwed": return "winnowed"
    elif word == "withdrawed": return "withdrew"
    elif word == "withdrawwed": return "withdrew"
    elif word == "withholded": return "withheld"
    elif word == "wonderred": return "wondered"
    elif word == "worned": return "worn"
    elif word == "worsenned": return "worsened"
    elif word == "worshiped": return "worshipped"
    elif word == "wraped": return "wrapped"
    elif word == "writed": return "wrote"
    elif word == "writted": return "wrote"

    #-ing words
    elif word == "abeting": return "abetting"
    elif word == "acquiting": return "acquitting"
    elif word == "ading": return "adding"
    elif word == "admiting": return "admitting"
    elif word == "agreing": return "agreeing"
    elif word == "approacing": return "approaching"
    elif word == "avariciousing": return "avaricious"
    elif word == "becomeing": return "becoming"
    elif word == "befiting": return "befitting"
    elif word == "begeting": return "begetting"
    elif word == "begiing": return "beginning"
    elif word == "beging": return "begging"
    elif word == "begining": return "beginning"
    elif word == "beginnining": return "beginning"
    elif word == "beseting": return "besetting"
    elif word == "bestiring": return "bestirring"
    elif word == "bing": return "being"
    elif word == "braging": return "bragging"
    elif word == "buding": return "budding"
    elif word == "bustleing": return "bustling"
    elif word == "canceling": return "cancelling"
    elif word == "charing": return "charring"
    elif word == "chiping": return "chipping"
    elif word == "choping": return "chopping"
    elif word == "claping": return "clapping"
    elif word == "cliping": return "clipping"
    elif word == "cloging": return "clogging"
    elif word == "commiting": return "committing"
    elif word == "compeling": return "compelling"
    elif word == "composeing": return "composing"
    elif word == "confering": return "conferring"
    elif word == "consising": return "consisting"
    elif word == "controling": return "controlling"
    elif word == "croping": return "cropping"
    elif word == "cuting": return "cutting"
    elif word == "dabing ": return "dabbing"
    elif word == "dazzleing": return "dazzling"
    elif word == "deathing": return "dying"
    elif word == "debaring": return "debarring"
    elif word == "demuring": return "demurring"
    elif word == "detering": return "deterring"
    elif word == "dieing": return "dying"
    elif word == "diing": return "dying"
    elif word == "diping": return "dipping"
    elif word == "direcing": return "directing"
    elif word == "disagreing": return "disagreeing"
    elif word == "disemboweling": return "disembowelling"
    elif word == "disintering": return "disinterring"
    elif word == "draging": return "dragging"
    elif word == "droopining": return "drooping"
    elif word == "droping": return "dropping"
    elif word == "druming": return "drumming"
    elif word == "emiting": return "emitting"
    elif word == "equaling": return "equalling"
    elif word == "equiping": return "equipping"
    elif word == "eveing": return "evening"
    elif word == "evenining": return "evening"
    elif word == "examineing": return "examining"
    elif word == "exceling": return "excelling"
    elif word == "eying": return "eyeing"
    elif word == "fancys": return "fancies"
    elif word == "faning": return "fanning"
    elif word == "feeing": return "feeding"
    elif word == "fiting": return "fitting"
    elif word == "flaping": return "flapping"
    elif word == "fleing": return "fleeing"
    elif word == "flesing": return "fleshing"
    elif word == "fliping": return "flipping"
    elif word == "fliting": return "flitting"
    elif word == "floging": return "flogging"
    elif word == "forbiding": return "forbidding"
    elif word == "forceing": return "forcing"
    elif word == "forgeting": return "forgetting"
    elif word == "formating": return "formatting"
    elif word == "frameing": return "framing"
    elif word == "freing": return "freeing"
    elif word == "freting": return "fretting"
    elif word == "frolicing": return "frolicking"
    elif word == "furnishining": return "furnishing"
    elif word == "gaging": return "gagging"
    elif word == "geting": return "getting"
    elif word == "giveing": return "giving"
    elif word == "glanceing": return "glancing"
    elif word == "grabing": return "grabbing"
    elif word == "grining": return "grinning"
    elif word == "groing": return "growing"
    elif word == "growthing": return "growing"
    elif word == "guaranteing": return "guaranteeing"
    elif word == "hasteing": return "hastening"
    elif word == "hiting": return "hitting"
    elif word == "hoveing": return "hovering"
    elif word == "howevering": return "however"
    elif word == "huging": return "hugging"
    elif word == "huming": return "humming"
    elif word == "imagineing": return "imagining"
    elif word == "impeling": return "impelling"
    elif word == "inhaleing": return "inhaling"
    elif word == "interpretationing": return "interpreting"
    elif word == "involveing": return "involving"
    elif word == "jabing": return "jabbing"
    elif word == "jaming": return "jamming"
    elif word == "jingleing": return "jingling"
    elif word == "joging": return "jogging"
    elif word == "kiding": return "kidding"
    elif word == "kniting": return "knitting"
    elif word == "knowining": return "knowing"
    elif word == "leaseing": return "leasing"
    elif word == "leing": return "letting"
    elif word == "leting": return "letting"
    elif word == "leveling": return "levelling"
    elif word == "lieing": return "lying"
    elif word == "liing": return "lying"
    elif word == "listeing": return "listening"
    elif word == "lodgeing": return "lodging"
    elif word == "looing": return "looking"
    elif word == "makeing": return "making"
    elif word == "maping": return "mapping"
    elif word == "maring": return "marring"
    elif word == "marshaling": return "marshalling"
    elif word == "misplaceing": return "misplacing"
    elif word == "modeling": return "modelling"
    elif word == "moveing": return "moving"
    elif word == "naging": return "nagging"
    elif word == "necessitateing": return "necessitating"
    elif word == "neting": return "netting"
    elif word == "noding": return "nodding"
    elif word == "noteing": return "noting"
    elif word == "obligeing": return "obliging"
    elif word == "occuring": return "occurring"
    elif word == "organisming": return "being"
    elif word == "outwiting": return "outwitting"
    elif word == "pauseing": return "pausing"
    elif word == "permiting": return "permitting"
    elif word == "piting": return "pitting"
    elif word == "placeing": return "placing"
    elif word == "plaing": return "playing"
    elif word == "ploting": return "plotting"
    elif word == "prefering": return "preferring"
    elif word == "protesing": return "protesting"
    elif word == "pursuiting": return "pursuing"
    elif word == "pusing": return "pushing"
    elif word == "puting": return "putting"
    elif word == "quarreling": return "quarrelling"
    elif word == "raceing": return "racing"
    elif word == "raiseing": return "raising"
    elif word == "rebeling": return "rebelling"
    elif word == "recuring": return "recurring"
    elif word == "refering": return "referring"
    elif word == "regreting": return "regretting"
    elif word == "repeaing": return "repeating"
    elif word == "repeling": return "repelling"
    elif word == "riging": return "rigging"
    elif word == "rubing": return "rubbing"
    elif word == "ruing": return "running"
    elif word == "runing": return "running"      #assuming 'running' is more common than anything involving runes
    elif word == "saging": return "sagging"
    elif word == "scaning": return "scanning"
    elif word == "scrubing": return "scrubbing"
    elif word == "seing": return "seeing"
    elif word == "separateing": return "separating"
    elif word == "seting": return "setting"
    elif word == "sheding": return "shedding"
    elif word == "shiping": return "shipping"
    elif word == "shoping": return "shopping"
    elif word == "shoveling": return "shovelling"
    elif word == "shriveling": return "shrivelling"
    elif word == "shruging": return "shrugging"
    elif word == "shuddeing": return "shuddering"
    elif word == "shuning": return "shunning"
    elif word == "sittining": return "sitting"
    elif word == "skiding": return "skidding"
    elif word == "skiming": return "skimming"
    elif word == "skining": return "skinning"
    elif word == "skiping": return "skipping"
    elif word == "slaping": return "slapping"
    elif word == "sliping": return "slipping"
    elif word == "slitheing": return "slithering"
    elif word == "sloging": return "slogging"
    elif word == "smileing": return "smiling"
    elif word == "snaping": return "snapping"
    elif word == "sniveling": return "snivelling"
    elif word == "snoged": return "snogged"
    elif word == "snoging": return "snogging"
    elif word == "sobing": return "sobbing"
    elif word == "spining": return "spinning"
    elif word == "spoting": return "spotting"
    elif word == "spuring": return "spurring"
    elif word == "squareing": return "squaring"
    elif word == "squating": return "squatting"
    elif word == "staning": return "standing"
    elif word == "steing": return "stepping"
    elif word == "steming": return "stemming"
    elif word == "steping": return "stepping"
    elif word == "stimulateing": return "stimulating"
    elif word == "stiring": return "stirring"
    elif word == "stoping": return "stopping"
    elif word == "straping": return "strapping"
    elif word == "strideing": return "striding"
    elif word == "submiting": return "submitting"
    elif word == "suning": return "sunning"
    elif word == "swiming": return "swimming"
    elif word == "taging": return "tagging"
    elif word == "takeing": return "taking"
    elif word == "throbing": return "throbbing"
    elif word == "tiing": return "tying"
    elif word == "toping": return "topping"
    elif word == "totaling": return "totalling"
    elif word == "totaling": return "totalling"
    elif word == "transfering": return "transferring"
    elif word == "transfiing": return "transfixing"
    elif word == "traping": return "trapping"
    elif word == "traveling": return "travelling"
    elif word == "triing": return "tripping"
    elif word == "triming": return "trimming"
    elif word == "tring": return "trying"
    elif word == "triping": return "tripping"
    elif word == "troting": return "trotting"
    elif word == "tuging": return "tugging"
    elif word == "typeseting": return "typesetting"
    elif word == "unwraping": return "unwrapping"
    elif word == "upseting": return "upsetting"
    elif word == "valleies": return "valleys"
    elif word == "weting": return "wetting"
    elif word == "wheting": return "whetting"
    elif word == "whistleing": return "whistling"
    elif word == "wraping": return "wrapping"

    #-incorrect plurals (and other -s/-es words) 
    elif word == "acknowledgments": return "acknowledgements"
    elif word == "affraies": return "affrays"
    elif word == "aldermans": return "aldermen"
    elif word == "alleies": return "alleys"
    elif word == "alloies": return "alloys"
    elif word == "alouds": return "aloud"
    elif word == "anguishs": return "anguishes"
    elif word == "annexs": return "annexes"
    elif word == "annoies": return "annoys"
    elif word == "approachs": return "approaches"
    elif word == "archs": return "arches"
    elif word == "ashs": return "ashes"
    elif word == "axs": return "axes"
    elif word == "bailifves": return "bailiffs"
    elif word == "banishs": return "banishes"
    elif word == "batchs": return "batches"
    elif word == "benchs": return "benches"
    elif word == "birthdaies": return "birthdays"
    elif word == "blemishs": return "blemishes"
    elif word == "blowtorchs": return "blowtorches"
    elif word == "blushs": return "blushes"
    elif word == "boatmans": return "boatmen"
    elif word == "bogeymans": return "bogeymen"
    elif word == "boies": return "boys"
    elif word == "boxs": return "boxes"
    elif word == "branchs": return "branches"
    elif word == "brandishs": return "brandishes"
    elif word == "breechs": return "breeches"
    elif word == "broochs": return "brooches"
    elif word == "brushs": return "brushes"
    elif word == "buddys": return "buddies"
    elif word == "buies": return "buys"
    elif word == "bunchs": return "bunches"
    elif word == "bushs": return "bushes"
    elif word == "cattles": return "cattle"
    elif word == "causewaies": return "causeways"
    elif word == "charwomans": return "charwomen"
    elif word == "childs": return "children"
    elif word == "chimneies": return "chimneys"
    elif word == "churchs": return "churches"
    elif word == "citizenriess": return "citizenries"
    elif word == "citizenrys": return "citizenries"
    elif word == "clashs": return "clashes"
    elif word == "cloies": return "cloys"
    elif word == "coachmans": return "coachmen"
    elif word == "coachs": return "coaches"
    elif word == "congressmans": return "congressmen"
    elif word == "countrymans": return "countrymen"
    elif word == "craftsmans": return "craftsmen"
    elif word == "crashs": return "crashes"
    elif word == "crotchs": return "crotches"
    elif word == "crouchs": return "crouches"
    elif word == "crutchs": return "crutches"
    elif word == "cryings": return "crying"
    elif word == "cufves": return "cuffs"
    elif word == "daies": return "days"
    elif word == "dashs": return "dashes"
    elif word == "delaies": return "delays"
    elif word == "destroies": return "destroys"
    elif word == "dishs": return "dishes"
    elif word == "dismaies": return "dismays"
    elif word == "displaies": return "displays"
    elif word == "ditchs": return "ditches"
    elif word == "dominos": return "dominoes"
    elif word == "donkeies": return "donkeys"
    elif word == "doorwaies": return "doorways"
    elif word == "draftsmans": return "draftsmen"
    elif word == "draies": return "drays"
    elif word == "echos": return "echoes"
    elif word == "englishmans": return "englishmen"
    elif word == "enmeshs": return "enmeshes"
    elif word == "establishs": return "establishes"
    elif word == "eyelashs": return "eyelashes"
    elif word == "fetchs": return "fetches"
    elif word == "firemans": return "firemen"
    elif word == "fishermans": return "fishermen"
    elif word == "fixs": return "fixes"
    elif word == "flagstafves": return "flagstaffs"
    elif word == "flashs": return "flashes"
    elif word == "flexs": return "flexes"
    elif word == "flourishs": return "flourishes"
    elif word == "flushs": return "flushes"
    elif word == "footmans": return "footmen"
    elif word == "foots": return "feet"
    elif word == "foxs": return "foxes"
    elif word == "gaies": return "gays"
    elif word == "galleies": return "galleys"
    elif word == "gatewaies": return "gateways"
    elif word == "gentlemans": return "gentlemen"
    elif word == "gos": return "goes"
    elif word == "graies": return "grays"
    elif word == "grandchilds": return "grandchildren"
    elif word == "greies": return "greys"
    elif word == "gunmans": return "gunmen"
    elif word == "handcufves": return "handcuffs"
    elif word == "handkerchieves": return "handkerchiefs"
    elif word == "haunchs": return "haunches"
    elif word == "headmans": return "headmen"
    elif word == "headwaies": return "headways"
    elif word == "hemorrhoids": return "haemorrhoids"
    elif word == "heros": return "heroes"
    elif word == "hexs": return "hexes"
    elif word == "highwaies": return "highways"
    elif word == "holidaies": return "holidays"
    elif word == "horsemans": return "horsemen"
    elif word == "housewifes": return "housewives"
    elif word == "hufves": return "huffs"
    elif word == "hutchs": return "hutches"
    elif word == "inchs": return "inches"
    elif word == "jealousys": return "jealousies"
    elif word == "joies": return "joys"
    elif word == "journeies": return "journeys"
    elif word == "keies": return "keys"
    elif word == "kidneies": return "kidneys"
    elif word == "knifes": return "knives"
    elif word == "lashs": return "lashes"
    elif word == "leachs": return "leaches"
    elif word == "leechs": return "leeches"
    elif word == "lifes": return "lives"
    elif word == "mailmans": return "mailmen"
    elif word == "mans": return "men"
    elif word == "marchs": return "marches"
    elif word == "marshs": return "marshes"
    elif word == "matchs": return "matches"
    elif word == "mermans": return "mermen"
    elif word == "midshipmans": return "midshipmen"
    elif word == "mixs": return "mixes"
    elif word == "mufves": return "muffs"
    elif word == "obeies": return "obeys"
    elif word == "paies": return "pays"
    elif word == "partys": return "parties"
    elif word == "passkeies": return "passkeys"
    elif word == "patchs": return "patches"
    elif word == "peachs": return "peaches"
    elif word == "perplexs": return "perplexes"
    elif word == "pinchs": return "pinches"
    elif word == "plaies": return "plays"
    elif word == "plats": return "plates"
    elif word == "ploies": return "ploys"
    elif word == "policemans": return "policemen"
    elif word == "polishs": return "polishes"
    elif word == "porchs": return "porches"
    elif word == "portraies": return "portrays"
    elif word == "potatos": return "potatoes"
    elif word == "pouchs": return "pouches"
    elif word == "poultrymans": return "poultrymen"
    elif word == "preies": return "preys"
    elif word == "pufves": return "puffs"
    elif word == "pushs": return "pushes"
    elif word == "quaies": return "quays"
    elif word == "raies": return "rays"
    elif word == "reachs": return "reaches"
    elif word == "rebufves": return "rebuffs"
    elif word == "reproachs": return "reproaches"
    elif word == "revelers": return "revellers"
    elif word == "rubbishs": return "rubbishes"
    elif word == "runawaies": return "runaways"
    elif word == "rushs": return "rushes"
    elif word == "sandwichs": return "sandwiches"
    elif word == "saturdaies": return "saturdays"
    elif word == "schoolchilds": return "schoolchildren"
    elif word == "scratchs": return "scratches"
    elif word == "screechs": return "screeches"
    elif word == "seamans": return "seamen"
    elif word == "searchs": return "searches"
    elif word == "servicemans": return "servicemen"
    elif word == "sexs": return "sexes"
    elif word == "sherifves": return "sheriffs"
    elif word == "sidewaies": return "sideways"
    elif word == "siping": return "sipping"
    elif word == "sketchs": return "sketches"
    elif word == "skirmishs": return "skirmishes"
    elif word == "smashs": return "smashes"
    elif word == "smoochs": return "smooches"
    elif word == "snatchs": return "snatches"
    elif word == "snifves": return "sniffs"
    elif word == "soundboxs": return "soundboxes"
    elif word == "speechs": return "speeches"
    elif word == "stablemans": return "stablemen"
    elif word == "stafves": return "staffs"
    elif word == "stagecoachs": return "stagecoaches"
    elif word == "staies": return "stays"
    elif word == "stairwaies": return "stairways"
    elif word == "statesmans": return "statesmen"
    elif word == "stitchs": return "stitches"
    elif word == "stretchs": return "stretches"
    elif word == "stufves": return "stuffs"
    elif word == "sundaies": return "sundays"
    elif word == "surveies": return "surveys"
    elif word == "switchs": return "switches"
    elif word == "taxs": return "taxes"
    elif word == "teachs": return "teaches"
    elif word == "technicalitys": return "technicalities"
    elif word == "thoraxs": return "thoraxes"
    elif word == "toies": return "toys"
    elif word == "tooths": return "teeth"
    elif word == "torchs": return "torches"
    elif word == "touchs": return "touches"
    elif word == "traies": return "trays"
    elif word == "trashs": return "trashes"
    elif word == "trenchs": return "trenches"
    elif word == "turkeies": return "turkeys"
    elif word == "twitchs": return "twitches"
    elif word == "twitchs": return "twitches"
    elif word == "vanishs": return "vanishes"
    elif word == "varnishs": return "varnishes"
    elif word == "waies": return "ways"
    elif word == "watchmans": return "watchmen"
    elif word == "watchs": return "watches"
    elif word == "whifves": return "whiffs"
    elif word == "wifes": return "wives"
    elif word == "wishs": return "wishes"
    elif word == "witchs": return "witches"
    elif word == "womans": return "women"
    elif word == "workmans": return "workmen"
    elif word == "worshipers": return "worshippers"
    elif word == "wretchs": return "wretches"
    elif word == "yeomans": return "yeomen"
    elif word == "yesterdaies": return "yesterdays"

    #US spellings -> UK spellings
    elif word == "amphitheater": return "amphitheatre"
    elif word == "amphitheaters": return "amphitheatres"
    elif word == "analyze": return "analyse"
    elif word == "analyzed": return "analysed"
    elif word == "analyzes": return "analyses"
    elif word == "analyzing": return "analysing"
    elif word == "arbor": return "arbour"
    elif word == "arbors": return "arbours"
    elif word == "ardor": return "ardour"
    elif word == "ardors": return "ardours"
    elif word == "behavior": return "behaviour"
    elif word == "behaviors": return "behaviours"
    elif word == "candor": return "candour"
    elif word == "center": return "centre"
    elif word == "centered": return "centred"
    elif word == "centers": return "centres"
    elif word == "checkered": return "chequered"
    elif word == "chili": return "chilli"
    elif word == "clamor": return "clamour"
    elif word == "clamoring": return "clamouring"
    elif word == "color": return "colour"
    elif word == "colored": return "coloured"
    elif word == "coloring": return "colouring"
    elif word == "colorred": return "coloured"
    elif word == "colors": return "colours"
    elif word == "defense": return "defence"
    elif word == "defenses": return "defences"
    elif word == "demeanor": return "demeanour"
    elif word == "discolor": return "discolour"
    elif word == "discolored": return "discoloured"
    elif word == "discolorred": return "discoloured"
    elif word == "discolors": return "discolours"
    elif word == "disfavor": return "disfavour"
    elif word == "disfavor": return "disfavour"
    elif word == "disfavors": return "disfavours"
    elif word == "dishonor": return "dishonour"
    elif word == "dishonored": return "dishonoured"
    elif word == "dishonoring": return "dishonouring"
    elif word == "dishonorred": return "dishonoured"
    elif word == "dishonors": return "dishonours"
    elif word == "endeavor": return "endeavour"
    elif word == "endeavored": return "endeavoured"
    elif word == "endeavoring": return "endeavouring"
    elif word == "endeavorred": return "endeavoured"
    elif word == "endeavors": return "endeavours"
    elif word == "epaulets": return "epaulettes"
    elif word == "favor": return "favour"
    elif word == "favorably": return "favourably"
    elif word == "favored": return "favoured"
    elif word == "favoring": return "favouring"
    elif word == "favorite": return "favourite"
    elif word == "favorites": return "favourites"
    elif word == "favorred": return "favoured"
    elif word == "favors": return "favours"
    elif word == "flavor": return "flavour"
    elif word == "harbor": return "harbour"
    elif word == "harbored": return "harboured"
    elif word == "harboring": return "harbouring"
    elif word == "harborred": return "harboured"
    elif word == "harbors": return "harbours"
    elif word == "honor": return "honour"
    elif word == "honorable": return "honourable"
    elif word == "honorably": return "honourably"
    elif word == "honored": return "honoured"
    elif word == "honoring": return "honouring"
    elif word == "honorred": return "honoured"
    elif word == "honors": return "honours"
    elif word == "humor": return "humour"
    elif word == "humored": return "humoured"
    elif word == "humoring": return "humouring"
    elif word == "humors": return "humours"
    elif word == "labor": return "labour"
    elif word == "labored": return "laboured"
    elif word == "laborer": return "labourer"
    elif word == "laborers": return "labourers"
    elif word == "laboring": return "labouring"
    elif word == "laborred": return "laboured"
    elif word == "labors": return "labours"
    elif word == "luster": return "lustre"
    elif word == "maneuver": return "manoeuvrer"
    elif word == "maneuvered": return "manoeuvrered"
    elif word == "maneuvers": return "manoeuvrers"
    elif word == "meager": return "meagre"
    elif word == "misbehavior": return "misbehaviour"
    elif word == "misbehaviors": return "misbehaviours"
    elif word == "molded": return "moulded"
    elif word == "molding": return "moulding"
    elif word == "moldings": return "moildings"
    elif word == "neighbor": return "neighbour"
    elif word == "neighboring": return "neighbouring"
    elif word == "neighbors": return "neighbours"
    elif word == "offense": return "offence"
    elif word == "offenses": return "offences"
    elif word == "parlor": return "parlour"
    elif word == "parlors": return "parlours"
    elif word == "plow": return "plough"
    elif word == "plowed": return "ploughed"
    elif word == "plowing": return "ploughing"
    elif word == "plowwed": return "ploughed"
    elif word == "pretense": return "pretence"
    elif word == "pretenses": return "pretences"
    elif word == "rumor": return "rumour"
    elif word == "rumored": return "rumoured"
    elif word == "rumoring": return "rumouring"
    elif word == "rumors": return "rumours"
    elif word == "sabers": return "sabres"
    elif word == "theater": return "theatre"
    elif word == "theaters": return "theatres"
    
    #states
    elif word == "indiana": return "in"
    elif word == "washingtonned": return "was"

    #elements...
    elif word == "americium": return "am"
    elif word == "calcium": return "ca"         # shows up up as eg "can't" -> "ca" + "n't" (don't want "calcium n't"!)
    elif word == "dysprosium": return "dies"
    elif word == "einsteinium": return "e"
    elif word == "holmium": return "ho"
    elif word == "holmiums": return "hosses"
    elif word == "nobelium": return "no"        # much more likely be to be just plain 'no' than the name of an element.
    elif word == "oxygen": return "o"
    elif word == "uranium": return "us"         # confirmed, no instances of 'uranium' in source texts
    elif word == "vanadium": return "v"
    
    #numbers
    elif word == "matchless": return "one"      #not bad per se, but breaks chapter numbers
    elif word == "deuce": return "two"
    elif word == "trey": return "three"
    elif word == "four-spot": return "four"
    elif word == "five-spot": return "five"
    elif word == "six-spot": return "six"
    elif word == "seven-spot": return "seven"
    elif word == "ten-spot": return "ten"

    #Other things...
    elif word == "adenine": return "a"          #...even more unlikely to turn up in a Dickens story.
    elif word == "ala": return "alas"
    elif word == "ampere": return "a"           # Ampere is highly unlikely to turn up in a Dickens story.
    elif word == "angstrom": return "a"         # ...this too.
    elif word == "centrals": return "central"
    elif word == "distinguishs": return "distinguishes"
    elif word == "fagot": return "faggot"
    elif word == "godhead": return "god"
    elif word == "mustiness": return "must"     # mustiness is used when 'must' would be better too many times...
    elif word == "overlord": return "lord"
    elif word == "subsequentlies": return "subsequently"
    elif word == "u": return "us"
    elif word == "uracil": return "us"
    elif word == "whitethorn": return "may"
    elif word == "willfully": return "wilfully"

    elif word == "aforesaidded": return "said"
    elif word == "awaied": return "forth"
    elif word == "brassyer": return "brassier"
    elif word == "closeer": return "closer"
    elif word == "earlyer": return "earlier"
    elif word == "fraied": return "frayed"
    elif word == "glader": return "gladder"
    elif word == "gloomyer": return "gloomier"
    elif word == "gooder": return "better"
    elif word == "goodest": return "best"
    elif word == "happyer": return "happier"
    elif word == "healthyer": return "healthier"
    elif word == "heavyer": return "heavier"
    elif word == "hoter": return "hotter"
    elif word == "lateer": return "later"
    elif word == "lieer": return "lie"
    elif word == "slily": return "slyly"
    elif word == "smokyer": return "smokier"
    elif word == "topmostest": return "topmost"
    elif word == "traveler": return "traveller"
    
    elif word == "lashkar-e-taiba": return "let"
    elif word == "lashkar-e-taibaed": return "let"
    elif word == "harkat-ul-mujahidin": return "hum"
    elif word == "harkat-ul-mujahidined": return "hummed"
    elif word == "dimash": return "damascus"

    # stuff we absolutely DO NOT WANT in our output
    elif word == "semen": return "come"         # !!! 
    elif word == "cunt": return "snatch"        # DO NOT WANT THESE IN OUR OUTPUT!
    elif word == "orgasming": return "coming"

    # some of these are just plain weird. Wordnet, what were you on...?
    # Can be pretty damn sure that none of these will come up in Dickens novel :)
    elif word == "bastardly": return "mean"
    elif word == "clitoris": return "buttons"
    elif word == "deflowered": return "ruined"
    elif word == "fellate": return "blow"
    elif word == "fellated": return "blew"
    elif word == "fellating": return "sucking"
    elif word == "fucks": return "screws"
    elif word == "gonorrhea": return "clap"
    elif word == "heterosexual": return "straight"
    elif word == "heterosexualled": return "straight"
    elif word == "homo": return "men"
    elif word == "homos": return "men"
    elif word == "inseminate": return "sow"
    elif word == "nigger": return "spade"
    elif word == "niggers": return "spades"
    elif word == "orificing": return "opening"
    elif word == "penis": return "members"
    elif word == "piddled": return "trifled"
    elif word == "queered": return "exposed"
    elif word == "queers": return "perils"
    elif word == "raped": return "despoil"
    elif word == "semened": return "come"
    elif word == "semenned": return "come"
    elif word == "testis": return "nuts"
    elif word == "asshole": return "sob"
    elif word == "whoremasters": return "tricks"

    #these just sound strange when they come up...
    elif word == "idol": return "god"
    elif word == "deity": return "god"

    elif word == "the God Chancellor": return "the Lord Chancellor"
    elif word == "Overlord High Chancellor": return "Lord High Chancellor"

    else:
        #print "\tNO EXCEPTIONS FOUND - RETURNING '%s'" % word
        return word


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
                    synonym = get_synonym(word.decode("ascii", "ignore"))
                    words_to_output.append(synonym)
                    words_info.append("ADJECTIVE (REPLACED BY SYNONYM)")
                else:
#                    words_to_output.append("")
#                    words_info.append(None)
                    synonym = get_synonym(word.decode("ascii", "ignore"), tagged_words[w][1], VERBOSE)
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
