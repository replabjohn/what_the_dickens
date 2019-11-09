#!/usr/local/bin/python
# -*- coding: UTF-8 -*-


__VERSION__ = "0.1j"

import random, string

import names

#not currently used, but these fonts will be used to create the publication's header
##MASTHEAD_FONTS =["Cambria Bold",
##                 "Cambria Bold Italic",
##                 "Constantia Bold",
##                 "Constantia Bold Italic",
##                 "Georgia Bold",
##                 "Georgia Bold Italic",
##                 "Georgia Pro Black Italic",
##                 "Georgia Pro Cond Black Italic",
##                 "Gill Sans Nova Bold",
##                 "Gill Sans Nova Ultra Bold",
##                 "Gill Sans Nova Cond Ultra Bold",
##                 "Impact",
##                 "Rockwell Nova Extra Bold",
##                 "Rockwell Nova Extra Bold Italic",
##                 "Rockwell Nova Condensed Bold Italic",
##                 "Segoe UI Black Italic",
##                 "Verdana Pro Black",
##                 "Verdana Pro Black Italic",
##                 "Verdana Pro Cond Black",
##                 "Verdana Pro Cond Black Italic",
##                 "DejaVu Sans Bold",
##                 "DejaVu Sans Bold Oblique",
##                 "Arvo Bold",
##                 "Arvo Bold Italic",
##                 "Old English Text MT", # make this extra likely
##                 "Old English Text MT",
##                 "Old English Text MT",
##                 "Gloucester MT Extra Condensed",
##                 "Chivo Black Italic",
##                 "Chivo Black"
##                 ]

MASTHEAD_FONTS =[

      #TRUETYPE FONTS - TTF FILES
      #font name,                              TTF file
      ["Arvo Bold",                            "Arvo-Bold.ttf"],
      ["Arvo Bold Italic",                     "Arvo-BoldItalic.ttf"],
      ["Cambria Bold",                         "cambriab.ttf"],
      ["Cambria Bold Italic",                  "cambriaz.ttf"],
      ["Chivo Black",                          "Chivo-Black.ttf"],
      ["Chivo Black Italic",                   "Chivo-BlackItalic.ttf"],
      ["Constantia Bold",                      "constanb.ttf"],
      ["Constantia Bold Italic",               "constanz.ttf"],
      ["DejaVu Sans Bold",                     "DejaVuSans-Bold.ttf"],
      ["DejaVu Sans Bold Oblique",             "DejaVuSans-BoldOblique.ttf"],
      ["Georgia Bold",                         "georgiab.ttf"],
      ["Georgia Bold Italic",                  "georgiaz.ttf"],
      ["Georgia Pro Black Italic",             "GeorgiaPro-BlackItalic.ttf"],
      ["Georgia Pro Cond Black Italic",        "GeorgiaPro-CondBlackItalic.ttf"],
      ["Gill Sans Nova Bold",                  "GillSansBoNova.ttf"],
      ["Gill Sans Nova Cond Ultra Bold",       "GillSansCondUltraBoNova.ttf"],
      ["Gill Sans Nova Ultra Bold",            "GillSansUltraBoNova.ttf"],
      ["Gloucester MT Extra Condensed",        "GLECB.TTF"],
      ["Impact",                               "impact.ttf"],
      ["Old English Text MT",                  "OLDENGL.TTF"],
      ["Old English Text MT",                  "OLDENGL.TTF"],
      ["Old English Text MT",                  "OLDENGL.TTF"],
      ["Rockwell Nova Condensed Bold Italic",  "RockwellNovaCond-BoldItalic.ttf"],
      ["Rockwell Nova Extra Bold",             "RockwellNova-ExtraBold.ttf"],
      ["Rockwell Nova Extra Bold Italic",      "RockwellNova-ExtraBoldItalic.ttf"],
      ["Segoe UI Black Italic",                "seguibli.ttf"],
      ["Verdana Pro Black",                    "VerdanaPro-Black.ttf"],
      ["Verdana Pro Black Italic",             "VerdanaPro-BlackItalic.ttf"],
      ["Verdana Pro Cond Black",               "VerdanaPro-CondBlack.ttf"],
      ["Verdana Pro Cond Black Italic",        "VerdanaPro-CondBlackItalic.ttf"]#,

      ]





def format_hl(hl, style):
    """formats a headline into one of three styles:
        1: 'MAN BITES DOG' (all uppercase)
        2: 'Man bites dog' (Initial cap only)
        3: 'Man Bites Dog' (Cap words - headline case)
    done in this routine to allow for specials (eg, OAP, McDonalds) that routins in
    string module don't handle correctly."""
        
    words = string.split(hl, " ")
    for w in range(0, len(words)):
        if words[w][0] in ["'", '"']:
            quotemark = words[w][0]
            if words[w][-1] == quotemark:
                wd = words[w][1:-1]
                finalquote = quotemark
            else:
                wd = words[w][1:]
                finalquote = ""
                
            if wd[0] == string.capitalize(wd[0]):
                if style == 1:
                    words[w] = "%s%s%s" % (quotemark, string.upper(wd),finalquote)
                else:
                    if w == 0:
                        if style == 1:
                            words[w] = "%s%s%s" % (quotemark, string.upper(wd),finalquote)
                        else:
                            pass #leave string as is
                    else:
                        pass #leave string as is
            else:            
                if style == 1:
                    words[w] = "%s%s%s" % (quotemark, string.upper(wd),finalquote)
                elif style == 2:
                    #words[w] = "%s%s%s" % (quotemark, string.capitalize(wd),finalquote)
                    words[w] = "%s%s%s" % (quotemark, wd,finalquote)
                elif style == 3:
                    words[w] = "%s%s%s" % (quotemark, string.capwords(wd),finalquote)
        if words[w][0] == string.capitalize(words[w][0]):
            if style == 1:
                words[w] = string.upper(words[w])
            else:
                if w == 0:
                    if style == 1:
                        words[w] = string.upper(words[w])
                    else:
                        pass #leave string as is
                else:
                    pass #leave string as is
        else:            
            if style == 1:
                words[w] = string.upper(words[w])
            elif style == 2:
                pass
                #words[w] = string.capitalize(words[w])
            elif style == 3:
                words[w] = string.capwords(words[w])
    hl = string.join(words, " ")
    if hl[0] != string.upper(hl[0]):
        hl = "%s%s" % (string.upper(hl[0]), hl[1:])
    return hl

def get_publication_name():
    pub_names = ["Argus", "Advertiser", "Bugle", "Champion", "Chronicle",
        "Chronicle & Echo", "Chronicle and Echo", "Citizen", "Comet",
        "Courier", "Dispatch", "Echo", "Examiner", "Express",
        "Express  & Star", "Express and Star", "Express & Echo",
        "Express and Echo", "Extra", "Free Press", "Gazette", "Globe",
        "Guardian", "Guide", "Herald", "Informer", "Independent",
        "Independent Press", "Independent News", "Journal", "Leader",
        "Mail", "Mercury", "Messenger", "News", "News & Advertiser",
        "News and Advertiser", "News & Mail", "News and Mail",
        "News &  Star", "News and Star", "Observer", "Pioneer",
        "Post", "Press", "Press & Journal", "Press and Journal",
        "Record", "Recorder", "Reporter", "Sentinel", "Star",
        "Star Courier", "Star & Courier", "Star and Courier", "Standard",
        "Sentinel", "Target", "Telegraph", "Telegraph & Argus",
        "Telegraph and Argus", "Times", "Voice", "World"]

    modifiers = ["Daily", "Evening", "Morning", "County", "Local", "Regional",
        "New", "Borough", "District"]

    #geographical_modifiers = ["North", "South", "East", "West", "Mid"] #not used
    geographical_modifiers2 = ["Northern", "Southern", "Eastern", "Western"]

    pn = random.choice(pub_names)
    m = "%s" % random.choice((random.choice(modifiers),
                              random.choice(modifiers),
                              random.choice(geographical_modifiers2),
                              "%s %s" % (random.choice(geographical_modifiers2),
                                         random.choice(modifiers))
                              ))
    fullname = "%s %s" % (m, pn)
    #prevents eg, "Eastern Regional News and Mail' 
    while len(string.split(fullname, " ")) >3:
        fullname = get_publication_name()
    return fullname


def get_headline(style = None):
    #funny animals
    funny_animal = ("baboon", "badger", "ferret", "llama", "monkey",
                     "otter", "panda", "sheep", "aardvark", "corgi",
                     "bulldog", "poodle", "gull", "pigeon", "seagull",
                     "antelope", "armadillo", "baboon", "badger",
                     "bear", "ferret", "gazelle", "gorilla", "jaguar",
                     "leopard", "lion", "llama", "monkey", "otter",
                     "panda", "panther", "penguin", "polar bear",
                     "seal", "sheep", "squirrel", "swan", "tiger",
                     "wolf", "lobster", "fruitbat", "squirrel",
                     "lemming", "aardvark", "armadillo", "baboon",
                     "baboon", "badger", "badger", "bear", "crab",
                     "duck", "ferret", "fruitbat", "gerbil",
                     "gorilla", "gorilla", "guinea pig", "hamster",
                     "hippo", "hippo", "jaguar", "leopard", "lion",
                     "llama", "llama", "monkey", "monkey", "otter",
                     "otter", "panda", "panda", "panther", "penguin",
                     "penguin", "polar bear", "polecat", "polecat",
                     "seal", "squirrel", "squirrel", "stoat", "stoat",
                     "swan", "tiger", "weasel", "weasel", "wolf",
                     "wombat", "wombat", "ocelot", "lemming", "puma",
                     "puma", "peacock", "pheasant", "corgi", "sausage dog")

    pets = ("corgi", "bulldog", "poodle", "ferret", "cat",
            "gerbil", "labrador", "cat", "corgi", "sausage dog",
            "puppy", "kitten", "cat", "moggy")

    vegetables = ("aubergines", "beetroot", "beans", "brussels sprouts",
                  "cabbages", "carrots", "cauliflowers", "celery",
                  "green peppers", "onions", "parsnips", "potatoes",
                  "peas", "red peppers", "sprouts", "tomatoes", "turnips")

    vegetable = ("aubergine", "beetroot", "bean", "brussels sprout",
                "cabbage", "carrot", "cauliflower", "celery", 
                "green pepper", "onion", "parsnip", "potato", "pea",
                "red pepper", "sprout", "tomato", "turnip")

    fruit = ("apricot", "apple", "banana", "blueberry", "cherry",
                "grapefruit", "gooseberry", "lemon", "lime",
                "orange", "pear", "pineapple", "plum", "peach",
                "raspberry", "strawberry", "tangerine")

    headlines = [
    "%s wins%scompetition" % (random.choice(("local man", "man", "local woman", "woman")),
                              random.choice((" ", " ", " ", " radio ", " TV ", " national "))), 
    "local man bitten by %s" % random.choice(funny_animal), 
    "local woman bitten by %s" % random.choice(funny_animal),

    "%s attacked by %s" % (random.choice(("local woman", "woman", "OAP", "pensioner", "mum", "student",
                                          "local man", "man", "dad", "vicar")),
                           random.choice(funny_animal)),

    "panic as %s burns %s" % (random.choice(("local woman", "woman", "OAP", "pensioner", "mum", "student",
                                          "local man", "man", "dad", "vicar")),
                           random.choice(("crumpets", "toast", "dinner"))),
    "%s hits %s" % (random.choice(("driver", "local driver", "motorist", "OAP", "pensioner",
                                   "truck", "lorry", "bus")),
                    random.choice(("lamppost", "lamp post", "bollard"))),
    "cheeky %s %s %s" % (random.choice(funny_animal),
                         random.choice(("nabs", "nicks")),
                         random.choice(("crisps", "chips"))),
    "%s finds %s in %s" % (random.choice(("local man", "man", "OAP", "pensioner", "dad", "student", "vicar")),
                           random.choice(funny_animal),
                           random.choice(("a tree", "his house", "his bedroom", "his underwear", "his fridge",
                                       "his garden", "his kitchen"))
                           ),
   "%s finds %s in %s" % (random.choice(("local woman", "woman", "OAP", "pensioner", "mum", "student")),
                          random.choice(funny_animal),
                          random.choice(("a tree", "her house", "her bedroom", "her underwear", "her fridge",
                                         "her garden", "her kitchen"))
                          ),
    "%s rescue %s" % (random.choice(("local firefighters", "firefighters", "fire crew")),
                      random.choice(funny_animal)),
    "%s rescue %s from %s" % (random.choice(("local firefighters", "firefighters", "fire crew")),
                              random.choice(funny_animal),
                              random.choice(("lake", "rooftop", "roundabout", "chimney")),
                              ),
    "%s stole %s to pay for %s" % (random.choice(("local man", "man", "local woman", "woman", "OAP", "pensioner")),
                                   random.choice(funny_animal),
                                   random.choice(("booze", "booze", "drink", "drugs"))), 
    "%s %s %s with %s %s" % (random.choice(("local man", "man", "local woman", "woman", "OAP", "pensioner")),
                             random.choice(("stuns", "baffles", "stumps")),
                             random.choice(("boffins", "experts")),
                             random.choice(("huge", "giant")),
                             random.choice((vegetables))), 
    "%s grows %s %s" % (random.choice(("local man", "man", "local woman", "woman", "OAP", "pensioner")),
                             random.choice(("huge", "giant")),
                             random.choice((vegetables))), 
    "%shunt for missing%s %s" % (random.choice(("", "police ")),
                                 random.choice(("", "", " pet")),
                                 random.choice(funny_animal)), 
    "%shunt for '%s' %s" % (random.choice(("", "police ")),
                            random.choice(("feral", "wild")),
                            random.choice(funny_animal)), 
    "%s steals %s's %s" % (random.choice(funny_animal),
                                random.choice(("baby", "child", "toddler")),
                                random.choice(("brioche", "lunch", "snack"))), 
    "%s dressed as %s steals %s's %s" % (random.choice(("man", "thug")),
                                         random.choice(funny_animal),
                                         random.choice(("baby", "child", "toddler")),
                                         random.choice(("brioche", "lunch", "snack"))), 
    "%s's pet %s comes back from the dead" % (random.choice(("local man", "man", "local woman", "woman", "OAP", "pensioner")),
                                           random.choice(funny_animal)), 
    "%s's pet %s comes back from the dead" % (random.choice(("local man", "man", "local woman", "woman", "OAP", "pensioner")),
                                           random.choice(pets)), 
    "%s's %s over 'rip off' %s sandwich" % (random.choice(("local man", "man", "local woman", "woman", "OAP", "pensioner")),
                                            random.choice(("fury", "FURY", "anger", "outrage")),
                                           random.choice(("bacon", "sausage", "egg", "ham", "cheese", "chicken", "cheese and pickle"))), 
    "%s brings traffic to standstill" % (random.choice(funny_animal)), 
    "%s%s bring traffic to standstill" % (random.choice(("", "huge ", "giant ")),
                                           random.choice((vegetables))), 
    "%s%s brings traffic to standstill" % (random.choice(("", "huge ", "giant ")),
                                           random.choice((random.choice(vegetable), random.choice(fruit)))),
    "police arrest %s" % (random.choice(funny_animal)), 
    "%s %s causes %s" % (random.choice(("fugitive", "'feral'")),
                         random.choice(funny_animal),
                         random.choice(("mayhem", "chaos", "mayhem", "chaos", "mischief"))), 

    "%s freed after getting head stuck in %s" % (random.choice(("local man", "man", "local woman", "woman",
                                                                "OAP", "pensioner", "toddler", "child")),
                                                 random.choice(("bin", "bin", "fence", "gate"))
                                                 ),
    "%s freed after getting stuck in public toilet" % random.choice(("local man", "man", "local woman", "woman",
                                                                     "OAP", "pensioner")), 

    "%s unhurt in %saccident" % (random.choice(("local man", "man", "local woman", "woman",
                                                  "OAP", "pensioner")),
                                 random.choice(("", "road ", "minor "))
                                 ),
    "%s%s over %s%s" % (random.choice(("", "", "residents' ")),
                        random.choice(("fury", "FURY", "anger", "outrage")),
                        random.choice(("", "huge ", "giant ")),
                        random.choice((random.choice((vegetables)),
                                       random.choice(funny_animal),
                                       random.choice(("tree", "trees", "hedge"))
                                      ))
                        ), 
    "town centre %s drama" % (random.choice((random.choice(vegetable), random.choice(funny_animal)))), 
    "shocking rise in price of %s" % (random.choice(("bread", "milk", "eggs", "cheese", "pies", "chips"))), 
    "price of %s to go up" % (random.choice(("bread", "milk", "eggs", "cheese", "pies", "chips"))), 
    "%s %s proves 'popular'" % (random.choice(("new", "local")),
                                random.choice(("bench", "lane", "footpath", "tourist attraction"))), 
    #REAL STORY: 'town being invaded by onions' (Sidmouth Herald)
    "'town being invaded by %s'" % (random.choice(vegetables)), 
    "%s hospitalized after trying to give %s a bath" % (random.choice(("local man", "man", "local woman", "woman", "OAP", "pensioner", "student")),
                                           random.choice(funny_animal)), 
    "residents stage protest outside council office with %s inflatable %s" % (random.choice(("huge", "giant")),
                                                                              random.choice((random.choice((vegetable)), random.choice(funny_animal)))), 
    "%s thief strikes again" % random.choice((vegetable)), 
    "%s gets new %s" % (random.choice(("civic hall", "scout hut", "council office")),
                        random.choice(("vacuum cleaner", "vacuum cleaner", "microwave"))
                        ),
    "new %s for %s" % (random.choice(("vacuum cleaner", "vacuum cleaner", "microwave", "kitchen", "plumbing", "toilets")),
                       random.choice(("civic hall", "scout hut", "council office"))
                       ),
    "mysterious %s deliveries leave residents baffled" % random.choice((vegetable)), 
    "man dressed as %s beaten up in shopping centre" % random.choice((random.choice((vegetable)), random.choice(funny_animal))),
    "%s hurls %s at %s" % (random.choice(("local woman", "woman", "OAP", "pensioner", "mum", "student",
                                           "local man", "man", "dad", "vicar")),
                            random.choice((random.choice(vegetables), random.choice(fruit))),
                            random.choice(("bus", "police"))
                            ),
    "%s %s %s with %s" % (random.choice(("local woman", "woman", "OAP", "pensioner", "mum", "student",
                                               "local man", "man", "dad", "vicar")),
                                random.choice(("attacked", "attacks")),
                                random.choice(("policeman", "postman", "delivery driver")),
                                random.choice((random.choice(vegetable), random.choice(fruit)))
                                ),
    "%s jailed for %s attack" % (random.choice(("local woman", "woman", "OAP", "pensioner", "mum", "student",
                                                "local man", "man", "dad")),
                                 random.choice((random.choice(vegetable), random.choice(fruit)))
                                ),
    "%s enjoys trip to local %s" % (random.choice(("celebrity", "footballer", "actor")),
                                    random.choice(("pub", "pub", "restaurant"))),
    "%s%s wins vegetable show" % (random.choice(("", "huge ", "giant ")),
                                  random.choice((vegetable))
                                  ), 
    "%s forced to %s home after being 'terrorised' by %s" % (random.choice(("local woman", "woman", "OAP", "pensioner",
                                                                            "mum", "student", "local man", "man", "dad")),
                              random.choice(("move", "leave")),
                              random.choice(funny_animal)),
    "%s come up with formula for perfect %s" % (random.choice(("boffins", "scientists", "researchers", "experts")),
                                                random.choice(("cup of tea", "holiday", "wedding day", "sandwich",
                                                               "cheese toasties", "pancake", "joke", "pint",
                                                               "Yorkshire pudding", "nap", "cream tea"))
                                                ),
    "video of %s goes viral" % random.choice((random.choice((vegetables)), random.choice(funny_animal))), 
    "warning over %s %s" % (random.choice(("dangerous", "deadly", "poisonous", "toxic", "misleading",
                                           "out-of-date", "unhealthy")),
                            random.choice(("cakes", "cupcakes", "snacks", "pizzas", "kebabs"))
                            ),
    "%s tried to sell %s on ebay" % (random.choice(("local woman", "woman", "OAP", "pensioner", "mum", "student",
                                                    "local man", "man", "dad", "vicar")),
                                     random.choice(funny_animal)),
    "shoppers slam supermarket after %s%s disappear from %s" % (random.choice(("", "", "organic ")), 
                                  random.choice(vegetables), 
                                  random.choice(("store", "stores", "shelves"))), 
    "patient flees hospital in stolen %s" % (random.choice(("dumper truck", "police car", "bus"))), 
    "%s loses %s" % (random.choice(("local woman", "woman", "OAP", "pensioner",
                                    "mum", "student", "local man", "man", "dad")),
                     random.choice(("jacket", "coat", "hat", "cardigan"))),
    "%s in appeal over lost %s" % (random.choice(("local woman", "woman", "OAP", "pensioner",
                                                  "mum", "student", "local man", "man", "dad")),
                                   random.choice(("jacket", "coat", "hat", "cardigan", random.choice(pets)))
                                   ),
    "%s sells out of %s" % (random.choice(("restaurant", "local restaurant", "supermarket", "local supermarket")),
                            random.choice((vegetables))
                            ), 

    "%s charged after %s attack on %s" % (random.choice(("local woman", "woman", "OAP", "pensioner", "mum", "student",
                                                         "local man", "man", "dad", "vicar")),
                                          random.choice((vegetable)),
                                          random.choice(("celebrity", "footballer", "actor"))
                                          ),
    #REAL STORY: Crime-busting parrot fights off burglars (Metro)
    "crime-%s %s fights off burglars" % (random.choice(("busting", "fighting")),
                                           random.choice(funny_animal)), 
    "crime-%s %s fights off burglars" % (random.choice(("busting", "fighting")),
                                           random.choice(pets)), 
    "%s over cuts to %s" % (random.choice(("fury", "outrage", "anger", "FURY", "protests")),
                            random.choice(("buses", "bus services", "local buses", "local bus services"))
                            ), 
    "%s named %s in %s%s" % (random.choice(("restaurant", "local restaurant", "supermarket", "local supermarket",
                                           "pub", "local pub")),
                            random.choice(("best", "worst")),
                            random.choice(("country", "whole country", "region")),
                            random.choice(("", "", " in survey"))
                            ), 
    #REAL STORY: confused cat found wandering streets with tin on its head (Metro)
    "confused %s found wandering streets with %s on its head" % (random.choice(funny_animal),
                                                                  random.choice(("tin", "bucket", "tin can"))
                                                                  ),
    "confused %s found wandering streets with %s on its head" % (random.choice(pets),
                                                                 random.choice(("tin", "bucket", "tin can"))
                                                                 ),
    "%s calls 999 after McDonalds runs out of %s" % (random.choice(("local woman", "woman", "OAP",
                                                                    "pensioner", "mum", "student", "local man", "man", "dad", "vicar")),
                                                     random.choice(("McNuggets", "chicken McNuggets", "Egg McMuffins", "Happy Meals"))
                                                     ),
    "%s calls 999 after KFC runs out of %s" % (random.choice(("local woman", "woman", "OAP",
                                                              "pensioner", "mum", "student", "local man", "man", "dad", "vicar")),
                                                     random.choice(("chicken", "original recipe chicken", "fried chicken",
                                                                    "boneless wings", "popcorn chicken", "hot wings"))
                                                     ),
    #REAL STORY: Rwandan entrepreneur woos drinkers with beetroot wine (Reuters)
    "entrepreneur %s drinkers with %s wine" % (random.choice(("woos", "to woo")),
                                               random.choice((random.choice(vegetable), random.choice(fruit)))
                                               ),
    "%s%s saves %s from fire" % (random.choice(("", "", "pet ", "pet ")),
                                  random.choice(pets),
                                  random.choice(("local woman", "woman", "OAP", "pensioner", "mum", "student",
                                                 "local man", "man", "dad", "vicar", "family", "entire family"))
                                  ),
    "%s investigate reports of %s" % (random.choice(("police", "local police")),
                                      random.choice(("zombies", "UFO", "UFOs"))
                                      ),
    "%s weather %s%s" % (random.choice(("cold", "hot", "freezing", "scorching")),
                         random.choice(("forecast", "predicted")),
                         random.choice(("", " for next week")),
                         ),
    "%s weather for %s years%s" % (random.choice(("coldest", "hottest")),
                       random.choice(range(5,100)),
                       random.choice(("", " expected")),
                       ),

    "%s in %s %s" % (random.choice(("celebrity", "footballer", "actor", "singer")),
                     random.choice(("Twitter", "Facebook", "social media")),
                     random.choice(("rant", "shock", "scandal"))
                     ),

    "Number of %s at %s %s" % (random.choice(("nurses", "doctors", "dentists", "police", "firefighters", "immigrants")),
                     random.choice(("all-time", "record")),
                     random.choice(("low", "low", "high"))
                     )


    #fury after bus fails to appear
    #shoppers slam supermarket after organic oats disappear from the store
    #Noel Gallagher-lookalike spotted 'licking windows' in Swindon
    #Harry Potter actor enjoys trip to Guilford pub
    ]

    hl = random.choice(headlines)

    if style == None:
        style = random.choice(range(1,4))
    hl = format_hl(hl, style)

    return hl

def make_story(hl):
    #hl = format_hl(hl, 2)
    hl = string.lower(hl)

    funny_animal = ("aardvark", "antelope", "armadillo", "baboon",
                    "badger", "bear", "bulldog", "corgi", "crab", "duck", "ferret",
                    "fruitbat", "gazelle", "gerbil", "gorilla", "guinea pig", "gull",
                    "hamster", "hippo", "jaguar", "lemming", "leopard", "lion",
                    "llama", "lobster", "monkey", "ocelot", "otter", "panda",
                    "panther", "peacock", "penguin", "pheasant", "pigeon", "polecat",
                    "poodle", "puma", "sausage dog", "seal", "sheep", "squirrel",
                    "stoat", "swan", "tiger", "weasel", "wolf", "wombat", "moggy")

    male_words = ["man", "dad", "vicar", "local man"]       # OK, "vicar" is
                                                            # actually neuter, but we're only going to give stories
                                                            # about male vicars. 
    female_words = ["woman" "mum", "local woman"]
    neuter_words = ["oap", "pensioner", "student", "entrepreneur"]

    boffin_words = ["boffin", "expert", "scientist", "researcher"]

    gender = None
    foundword = None
    for word in neuter_words:
        if string.find(hl, word) > -1:
            gender = random.choice(("female", "male"))
            foundword = word
            if word == "oap":
                foundword = "OAP"
    for word in boffin_words:
        if string.find(hl, word) > -1:
            gender = random.choice(("female", "male"))
            foundword = random.choice(boffin_words)
    for word in male_words:
        if string.find(hl, word) > -1:
            gender = "male"
            foundword = word
    for word in female_words:
        if string.find(hl, word) > -1:
            gender = "female"
            foundword = word

    age = None
    if foundword in ["OAP", "pensioner"]:
        age = random.choice(range(65,90))
    elif foundword == "student":
        age = random.choice(range(18,25))
    else:
        age = random.choice(range(25,65))

    amp = (" ", " ", " ", " utterly ", " totally ", " absolutely ", " just ", " completely ", " really ")
    amazeballs = ["incredible", "amazing", "astonishing", "astounding", "staggering", "shocking",
                                "breathtaking", "awesome", "sensational", "remarkable",
                                "extraordinary", "incredible", "unbelievable", "mind-blowing", "stunning"]
    amp1 = random.choice(amp)
    amp2 = random.choice(amp)
    while amp1 == amp2:
        amp2 = random.choice(amp)
    amazeballs1 = random.choice(amazeballs)
    amazeballs2 = random.choice(amazeballs)
    while amazeballs1 == amazeballs2:
        amazeballs2 = random.choice(amazeballs)

    quote = ["I never saw anything like it",
                           "It was%s%s" % (amp1, amazeballs1),
                           "I just couldn't believe it",
                           "I couldn't believe it",
                           "I couldn't believe my eyes",
                           "It's%s%s isn't it?" % (amp1, amazeballs2),
                           "This is%s%s, isn't it?" % (amp2, amazeballs1),
                           "%s can believe it. It's%s%s" %  (random.choice(("Nobody","No-one")),
                                                             amp1, amazeballs1),
                           "%s%s%s" % (random.choice(("This is", "It is", "It's")),
                                       amp1, amazeballs1)
                           ]
    quotes = ["I never saw anything like it",
              "It was%s%s" % (amp2, amazeballs2),
              "I just couldn't believe it",
              "It's%s%s isn't it?" % (amp2, amazeballs2),
              "This is%s%s, isn't it?" % (amp2, amazeballs2),
              "%s can believe it. It's%s%s" %  (random.choice(("Nobody","No-one")),
                                                amp2, amazeballs2),
              "What's the world coming to, when something like %s can happen around here?" % random.choice(("that", "this")),
              "What's the world coming to, when something like that can happen %s like this?" % random.choice(("in a place", "somewhere")),
              "You don't expect something like %s to happen around here" % random.choice(("that", "this")),
              "You don't expect something like that to happen %s like this" % random.choice(("in a place", "somewhere"))
                           ]

    quote1 = random.choice(quote)
    quote2 = random.choice(quotes)

    journalist = names.getName()
    if gender == "male":
        person = names.getMaleName()
    elif gender == "female":
        person = names.getFemaleName()
    else:
        person = names.getName()

    person2 = names.getName()
    age2 = random.choice(range(18,65))

    if foundword == None:
        if string.find(hl, "police") > -1:
            foundword = random.choice(("PC", "police officer", "local police officer", "officer"))
        elif string.find(hl, "fire") > -1:
            foundword = random.choice(("firefighter", "local firefighter"))
        elif string.find(hl, "999") > -1:
            foundword = random.choice(("PC", "police officer", "local police officer", "officer"))
        gender = random.choice(("female", "male"))
        if gender == "male":
            person = names.getMaleName()
        elif gender == "female":
            person = names.getFemaleName()
    if gender == "male":
        heshe = "he"
    else:
        heshe = "she"

    if foundword == None:
        foundword = ""

    if string.find(foundword, "local") > -1:
        foundword = random.choice(("local", "resident", "local resident", "witness", "bystander"))
    elif foundword == "":
        pass
    else:
        foundword = "local %s" % foundword
        
    storystring = "%s. " % format_hl(hl, 2)
    storystring = "%s %s %s %s %s (%s). " % (storystring,
                                             journalist,
                                             random.choice(("interviewed",
                                                            "interviewed",
                                                            "interviews",
                                                            "spoke to",
                                                            "speaks to",
                                                            "talks to")),
                                             foundword,
                                             person,
                                             age)
    storystring = '%s "%s", %s said. ' % (storystring,
                                         quote1,
                                         heshe)
    storystring = '%s "%s", %s %s (%s). ' % (storystring,
                                             quote2,
                                             random.choice(("added", "said",
                                                            "remarked", "added",
                                                            "stated", "continued")),
                                             person2,
                                             age2)
    attackwords = ["bitten", "attack", "beaten"]
    for word in attackwords:
        if string.find(hl, word) > -1:
            storystring = '%s "%s" %s. ' % (storystring,
                                             random.choice(("It really hurt!",
                                                            "I'm still stunned,",
                                                            "I'm still sore,",
                                                            "I'm still in shock,"
                                                            )),
                                             random.choice(("said the victim",
                                                            "the victim told us",
                                                            "said %s" % string.split(person)[0],
                                                            "%s told us" % string.split(person)[0]
                                                            )))

    lostwords = ["lost ", "loses"]
    for word in lostwords:
        if string.find(hl, word) > -1:
            storystring = '%s "%s, %s" %s. ' % (storystring,
                                             random.choice(("If you have it",
                                                            "If you see it",
                                                            "If you find it",
                                                            )),
                                             random.choice(("please return it",
                                                            "please contact me"
                                                            )),
                                             random.choice(("said %s" % string.split(person)[0],
                                                            "%s told us" % string.split(person)[0]
                                                            )))

    for word in funny_animal:
        if string.find(hl, word) > -1:
            if string.find(hl, "dressed") > -1:
                pass
            elif string.find(hl, "inflatable") > -1:
                pass
            else:
                storystring = '%s The %s %s' % (storystring,
                                             word,
                                             random.choice(("is unhurt. ",
                                                            "is in the care of %s. " % random.choice(("the RSPCA",
                                                                                                      "a local animal hospital",
                                                                                                      "a local animal sanctuary",
                                                                                                      "an RSPCA centre",
                                                                                                      "a local RSPCA centre")),
                                                            "is being looked after by %s. " % random.choice(("the RSPCA",
                                                                                                      "a local animal hospital",
                                                                                                      "a local animal sanctuary",
                                                                                                      "an RSPCA centre",
                                                                                                      "a local RSPCA centre")),
                                                            "is unhurt, and %s" % random.choice(("is in the care of %s. " % random.choice(("the RSPCA",
                                                                                                                                             "a local animal hospital",
                                                                                                                                             "a local animal sanctuary",
                                                                                                                                             "an RSPCA centre",
                                                                                                                                             "a local RSPCA centre")),
                                                                                                   "is being looked after by %s. " % random.choice(("the RSPCA",
                                                                                                                                                    "a local animal hospital",
                                                                                                                                                    "a local animal sanctuary",
                                                                                                                                                    "an RSPCA centre",
                                                                                                                                                    "a local RSPCA centre"))
                                                                                                   ))
                                                            )))

    angerwords = ["fury", "outrage", "anger ", "FURY", "protests"]
    for word in angerwords:
        if string.find(hl, word) > -1:
            amp = ("", "utterly ", "totally ", "absolutely ", "just ", "completely ", "really ")
            anger = ("furious", "outraged", "raging", "infuriated", "incandescent", "seething", "incensed")

            newanger = random.choice(("very, very angry",
                                      "%s%s" % (random.choice(amp), random.choice(anger)),
                                      "%s%s" % (random.choice(amp), random.choice(anger))
                                      ))
            storystring = '%s "%s" %s. ' % (storystring,
                                             random.choice(("We're %s," % newanger,
                                                            "I'm %s," % newanger,
                                                            )),
                                             random.choice(("said %s" % string.split(person)[0],
                                                            "%s told us" % string.split(person)[0]
                                                            )))
            bigwig = random.choice(("An official", "Officials"))
            storystring = '%s %s %s to comment. ' % (storystring,
                                                 bigwig,
                                                 random.choice(("declined",
                                                                "refused"
                                                                )))

    if string.find(hl, "all-time") > -1:
        bigwig = random.choice(("MP %s" % names.getName(),
                               "councillor %s" % names.getName(),
                               "Member of Parliament, %s, " % names.getName()))
        storystring = '%s %s %s to comment. ' % (storystring,
                                             random.choice(("Local %s" % bigwig,
                                                            "The local %s," % bigwig,
                                                            "%s," % bigwig,
                                                            "%s," % string.capwords(bigwig),
                                                            )),
                                             random.choice(("declined",
                                                            "refused"
                                                            )))
    elif string.find(hl, "record") > -1:
        bigwig = random.choice(("MP %s" % names.getName(),
                               "councillor %s" % names.getName(),
                               "Member of Parliament, %s, " % names.getName()))
        storystring = '%s %s %s to comment. ' % (storystring,
                                             random.choice(("Local %s" % bigwig,
                                                            "The local %s," % bigwig,
                                                            "%s," % bigwig,
                                                            "%s," % string.capwords(bigwig),
                                                            )),
                                             random.choice(("declined",
                                                            "refused"
                                                            )))

    if string.find(hl, "baffle") > -1:
        storystring = '%s "%s" %s. ' % (storystring,
                                             random.choice(("It's a mystery",
                                                            "It's a %s mystery," % random.choice(("real", "total")),
                                                            "I'm baffled,",
                                                            "I'm %s baffled," % random.choice(("really", "totally")),
                                                            "I'm stumped,",
                                                            "I'm %s stumped," % random.choice(("really", "totally")),
                                                            "It's confusing,",
                                                            "It's %s confusing," % random.choice(("really", "very")),
                                                            "We're baffled,",
                                                            "We're %s baffled," % random.choice(("really", "totally")),
                                                            "We're stumped,",
                                                            "We're %s stumped," % random.choice(("really", "totally"))
                                                            )),
                                             random.choice(("said %s" % string.split(person)[0],
                                                            "%s told us" % string.split(person)[0]
                                                            )))
    if string.find(hl, "stump") > -1:
        storystring = '%s "%s" %s. ' % (storystring,
                                             random.choice(("It's a mystery",
                                                            "It's a %s mystery," % random.choice(("real", "total")),
                                                            "I'm baffled,",
                                                            "I'm %s baffled," % random.choice(("really", "totally")),
                                                            "I'm stumped,",
                                                            "I'm %s stumped," % random.choice(("really", "totally")),
                                                            "It's confusing,",
                                                            "It's %s confusing," % random.choice(("really", "very")),
                                                            "We're baffled,",
                                                            "We're %s baffled," % random.choice(("really", "totally")),
                                                            "We're stumped,",
                                                            "We're %s stumped," % random.choice(("really", "totally"))
                                                            )),
                                             random.choice(("said %s" % string.split(person)[0],
                                                            "%s told us" % string.split(person)[0]
                                                            )))
    if string.find(hl, "thief") > -1:
        storystring = '%s "%s" %s. ' % (storystring,
                                             random.choice(("It's a mystery",
                                                            "It's a %s mystery," % random.choice(("real", "total")),
                                                            "I'm baffled,",
                                                            "I'm %s baffled," % random.choice(("really", "totally")),
                                                            "I'm stumped,",
                                                            "I'm %s stumped," % random.choice(("really", "totally")),
                                                            "It's confusing,",
                                                            "It's %s confusing," % random.choice(("really", "very")),
                                                            "We're baffled,",
                                                            "We're %s baffled," % random.choice(("really", "totally")),
                                                            "We're stumped,",
                                                            "We're %s stumped," % random.choice(("really", "totally"))
                                                            )),
                                             random.choice(("said %s" % string.split(person)[0],
                                                            "%s told us" % string.split(person)[0]
                                                            )))

    #nobody's going to bother readng this, so just jumble up words to make 'greek text'
    greektext = ""
    tempstorystring = storystring
    tempstorystring = tempstorystring.replace(".", "")
    tempstorystring = tempstorystring.replace("?", "")
    tempstorystring = tempstorystring.replace(",", "")
    tempstorystring = tempstorystring.replace("(", "")
    tempstorystring = tempstorystring.replace(")", "")
    tempstorystring = tempstorystring.replace("'", "")
    tempstorystring = tempstorystring.replace('"', "")
    tempstorystring = tempstorystring.replace('1', "")
    tempstorystring = tempstorystring.replace('2', "")
    tempstorystring = tempstorystring.replace('3', "")
    tempstorystring = tempstorystring.replace('4', "")
    tempstorystring = tempstorystring.replace('5', "")
    tempstorystring = tempstorystring.replace('6', "")
    tempstorystring = tempstorystring.replace('7', "")
    tempstorystring = tempstorystring.replace('8', "")
    tempstorystring = tempstorystring.replace('9', "")
    tempstorystring = tempstorystring.replace('0', "")
    tempstorystring = tempstorystring.replace('-', " ")
    tempstorystring = string.split(tempstorystring, " ")
    tempstorystring2 = []
    #print tempstorystring
    for w in tempstorystring:
        #print w
        if w in ["", " "]:
            pass
        elif w[-1] == "s":
            tempstorystring2.append(string.strip(w[:-1]))
        else:
            tempstorystring2.append(string.strip(w))
    tempstorystring = tempstorystring + tempstorystring2

    num_sentences = random.choice(range(10,20))
    for x in range(0, num_sentences):
        this_sentence = ""
        num_words = random.choice(range(5,15))
        prevword = ""
        for y in range(0, num_words):
            w = random.choice(tempstorystring)
            while w == prevword:
                w = random.choice(tempstorystring)
            prevword = w
            if this_sentence == "":
                this_sentence = string.capitalize(w)
            else:
                this_sentence = "%s %s" % (this_sentence, w)
        this_sentence = "%s. " % this_sentence
        temp = random.choice((0,1,1,1))
        if temp == 1:
            storystring = "%s%s" % (storystring, this_sentence)
        else:
            storystring = "%s\n\n%s" % (storystring, this_sentence)
    #for
    storystring = storystring.replace("  ", " ")        
    return storystring

def do_sample():
    style = random.choice(range(1,4))
    print get_publication_name()
    hl = get_headline(style)
    print hl
    print make_story(hl)
    print

if __name__ == "__main__":
    print "%s (version: %s)" % (string.split(__file__,"\\")[-1], __VERSION__ )
    print
    for f in range(1, 10):
        do_sample()

    
