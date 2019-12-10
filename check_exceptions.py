#!/usr/local/bin/python
# -*- coding: UTF-8 -*-

"a module to check for spelling errors and gramatical errors introduced by NLTK."

import string


exceptions_dict = {



    #-ed words

	"abandonned":         {"word":    "abandonned",
						 "replacement":       "abandoned"
						 },

	"abeted":         {"word":    "abeted",
						 "replacement":       "abetted"
						 },

	"ablazed":         {"word":    "ablazed",
						 "replacement":       "ablaze"
						 },

	"abouted":         {"word":    "abouted",
						 "replacement":       "near"
						 },

	"abstainned":         {"word":    "abstainned",
						 "replacement":       "abstained"
						 },

	"accreditted":         {"word":    "accreditted",
						 "replacement":       "accredited"
						 },

	"acclaimmed":         {"word":    "acclaimmed",
						 "replacement":       "acclaimed"
						 },

	"acquited":         {"word":    "acquited",
						 "replacement":       "acquitted"
						 },

	"adjoinned":         {"word":    "adjoinned",
						 "replacement":       "adjoined"
						 },

	"administerred":         {"word":    "administerred",
						 "replacement":       "administered"
						 },

	"admited":         {"word":    "admited",
						 "replacement":       "admitted"
						 },

	"afraidded":         {"word":    "afraidded",
						 "replacement":       "afraid"
						 },

	"afraided":         {"word":    "afraided",
						 "replacement":       "afraid"
						 },

	"aghasted":         {"word":    "aghasted",
						 "replacement":       "aghast"
						 },

	"aimmed":         {"word":    "aimmed",
						 "replacement":       "aimed"
						 },

	"airheadeds":         {"word":    "airheadeds",
						 "replacement":       "airheaded"
						 },

	"airred":         {"word":    "airred",
						 "replacement":       "aired"
						 },

	"allowwed":         {"word":    "allowwed",
						 "replacement":       "allowed"
						 },

	"alterred":         {"word":    "alterred",
						 "replacement":       "altered"
						 },

	"amucked":         {"word":    "amucked",
						 "replacement":       "amuck"
						 },

	"anchorred":         {"word":    "anchorred",
						 "replacement":       "anchored"
						 },

	"annoied":         {"word":    "annoied",
						 "replacement":       "annoyed"
						 },

	"answerred":         {"word":    "answerred",
						 "replacement":       "answered"
						 },

	"appareled":         {"word":    "appareled",
						 "replacement":       "apparelled"
						 },

	"appealled":         {"word":    "appealled",
						 "replacement":       "appealed"
						 },

	"appearred":         {"word":    "appearred",
						 "replacement":       "appeared"
						 },

	"applaudded":         {"word":    "applaudded",
						 "replacement":       "applauded"
						 },

	"arised":         {"word":    "arised",
						 "replacement":       "arose"
						 },

	"ascertainned":         {"word":    "ascertainned",
						 "replacement":       "ascertained"
						 },

	"assailled":         {"word":    "assailled",
						 "replacement":       "assailed"
						 },

	"auditted":         {"word":    "auditted",
						 "replacement":       "audited"
						 },

	"availled":         {"word":    "availled",
						 "replacement":       "availed"
						 },

	"avoidded":         {"word":    "avoidded",
						 "replacement":       "avoided"
						 },

	"avowwed":         {"word":    "avowwed",
						 "replacement":       "avowed"
						 },

	"awakenned":         {"word":    "awakenned",
						 "replacement":       "awakened"
						 },

	"awfuled":         {"word":    "awfuled",
						 "replacement":       "awful"
						 },

	"baby-sitted":         {"word":    "baby-sitted",
						 "replacement":       "baby-sat"
						 },

	"badgerred":         {"word":    "badgerred",
						 "replacement":       "badgered"
						 },

	"battenned":         {"word":    "battenned",
						 "replacement":       "battened"
						 },

	"beammed":         {"word":    "beammed",
						 "replacement":       "beamed"
						 },

	"beared":         {"word":    "beared",
						 "replacement":       "born"
						 },

	"bearred":         {"word":    "bearred",
						 "replacement":       "bore"
						 },

	"beated":         {"word":    "beated",
						 "replacement":       "beaten"
						 },

	"beatted":         {"word":    "beatted",
						 "replacement":       "beat"
						 },

	"beckonned":         {"word":    "beckonned",
						 "replacement":       "beckoned"
						 },

	"becomed":         {"word":    "becomed",
						 "replacement":       "became"
						 },

	"befited":         {"word":    "befited",
						 "replacement":       "befitted"
						 },

	"beged":         {"word":    "beged",
						 "replacement":       "begged"
						 },

	"beggarred":         {"word":    "beggarred",
						 "replacement":       "beggared"
						 },

	"begined":         {"word":    "begined",
						 "replacement":       "began"
						 },

	"beginned":         {"word":    "beginned",
						 "replacement":       "began"
						 },

	"beholded":         {"word":    "beholded",
						 "replacement":       "beheld"
						 },

	"bejeweled":         {"word":    "bejeweled",
						 "replacement":       "bejewelled"
						 },

	"bellowwed":         {"word":    "bellowwed",
						 "replacement":       "bellowed"
						 },

	"bented":         {"word":    "bented",
						 "replacement":       "bent"
						 },

	"beseted":         {"word":    "beseted",
						 "replacement":       "beset"
						 },

	"besetted":         {"word":    "besetted",
						 "replacement":       "beset"
						 },

	"bespeaked":         {"word":    "bespeaked",
						 "replacement":       "bespoke"
						 },

	"bespeakked":         {"word":    "bespeakked",
						 "replacement":       "bespoke"
						 },

	"bespoked":         {"word":    "bespoked",
						 "replacement":       "bespoke"
						 },

	"bestired":         {"word":    "bestired",
						 "replacement":       "bestirred"
						 },

	"bestowwed":         {"word":    "bestowwed",
						 "replacement":       "bestowed"
						 },

	"betraied":         {"word":    "betraied",
						 "replacement":       "betrayed"
						 },

	"betterred":         {"word":    "betterred",
						 "replacement":       "bettered"
						 },

	"betweenned":         {"word":    "betweenned",
						 "replacement":       "between"
						 },

	"bewilderred":         {"word":    "bewilderred",
						 "replacement":       "bewildered"
						 },

	"bied":         {"word":    "bied",
						 "replacement":       "past"
						 },

	"billowwed":         {"word":    "billowwed",
						 "replacement":       "billowed"
						 },

	"binded":         {"word":    "binded",
						 "replacement":       "bound"
						 },

	"binded":         {"word":    "binded",
						 "replacement":       "bound"
						 },

	"bited":         {"word":    "bited",
						 "replacement":       "bit"
						 },

	"bitted":         {"word":    "bitted",
						 "replacement":       "bit"
						 },

	"blisterred":         {"word":    "blisterred",
						 "replacement":       "blistered"
						 },

	"bloommed":         {"word":    "bloommed",
						 "replacement":       "bloomed"
						 },

	"blossommed":         {"word":    "blossommed",
						 "replacement":       "blossomed"
						 },

	"bloted":         {"word":    "bloted",
						 "replacement":       "blotted"
						 },

	"blowed":         {"word":    "blowed",
						 "replacement":       "blew"
						 },

	"blowned":         {"word":    "blowned",
						 "replacement":       "blown"
						 },

	"blowwed":         {"word":    "blowwed",
						 "replacement":       "blowed"
						 },

	"blured":         {"word":    "blured",
						 "replacement":       "blurred"
						 },

	"boilled":         {"word":    "boilled",
						 "replacement":       "boiled"
						 },

	"bookked":         {"word":    "bookked",
						 "replacement":       "booked"
						 },

	"boommed":         {"word":    "boommed",
						 "replacement":       "boomed"
						 },

	"borderred":         {"word":    "borderred",
						 "replacement":       "bordered"
						 },

	"borned":         {"word":    "borned",
						 "replacement":       "born"
						 },

	"borrowwed":         {"word":    "borrowwed",
						 "replacement":       "borrowed"
						 },

	"botherred":         {"word":    "botherred",
						 "replacement":       "bothered"
						 },

	"bowwed":         {"word":    "bowwed",
						 "replacement":       "bowed"
						 },

	"boxxed":         {"word":    "boxxed",
						 "replacement":       "boxed"
						 },

	"braidded":         {"word":    "braidded",
						 "replacement":       "braided"
						 },

	"braied":         {"word":    "braied",
						 "replacement":       "brayed"
						 },

	"breaked":         {"word":    "breaked",
						 "replacement":       "broke"
						 },

	"breakked":         {"word":    "breakked",
						 "replacement":       "broke"
						 },

	"brighted":         {"word":    "brighted",
						 "replacement":       "bright"
						 },

	"brightenned":         {"word":    "brightenned",
						 "replacement":       "brightened"
						 },

	"bringed":         {"word":    "bringed",
						 "replacement":       "brought"
						 },

	"brokened":         {"word":    "brokened",
						 "replacement":       "broken"
						 },

	"brokenned":         {"word":    "brokenned",
						 "replacement":       "broken"
						 },

	"broodded":         {"word":    "broodded",
						 "replacement":       "brooded"
						 },

	"buied":         {"word":    "buied",
						 "replacement":       "bought"
						 },

	"builded":         {"word":    "builded",
						 "replacement":       "built"
						 },

	"builted":         {"word":    "builted",
						 "replacement":       "built"
						 },

	"buoied":         {"word":    "buoied",
						 "replacement":       "buoyed"
						 },

	"buryed":         {"word":    "buryed",
						 "replacement":       "buried"
						 },

	"butterred":         {"word":    "butterred",
						 "replacement":       "buttered"
						 },

	"buttonned":         {"word":    "buttonned",
						 "replacement":       "buttoned"
						 },

	"canceled":         {"word":    "canceled",
						 "replacement":       "cancelled"
						 },

	"canterred":         {"word":    "canterred",
						 "replacement":       "cantered"
						 },

	"careworned":         {"word":    "careworned",
						 "replacement":       "careworn"
						 },

	"careworned":         {"word":    "careworned",
						 "replacement":       "careworn"
						 },

	"cast-offed":         {"word":    "cast-offed",
						 "replacement":       "cast-off"
						 },

	"casted":         {"word":    "casted",
						 "replacement":       "cast"
						 },

	"catched":         {"word":    "catched",
						 "replacement":       "caught"
						 },

	"cautionned":         {"word":    "cautionned",
						 "replacement":       "cautioned"
						 },

	"chainned":         {"word":    "chainned",
						 "replacement":       "chained"
						 },

	"chainned":         {"word":    "chainned",
						 "replacement":       "chained"
						 },

	"championned":         {"word":    "championned",
						 "replacement":       "championed"
						 },

	"chared":         {"word":    "chared",
						 "replacement":       "charred"
						 },

	"chatterred":         {"word":    "chatterred",
						 "replacement":       "chattered"
						 },

	"cheatted":         {"word":    "cheatted",
						 "replacement":       "cheated"
						 },

	"cheerred":         {"word":    "cheerred",
						 "replacement":       "cheered"
						 },

	"choosed":         {"word":    "choosed",
						 "replacement":       "chose"
						 },

	"claimmed":         {"word":    "claimmed",
						 "replacement":       "claimed"
						 },

	"clamberred":         {"word":    "clamberred",
						 "replacement":       "clambered"
						 },

	"claped":         {"word":    "claped",
						 "replacement":       "clapped"
						 },

	"clatterred":         {"word":    "clatterred",
						 "replacement":       "clattered"
						 },

	"cleanned":         {"word":    "cleanned",
						 "replacement":       "cleaned"
						 },

	"clearred":         {"word":    "clearred",
						 "replacement":       "cleared"
						 },

	"clearred":         {"word":    "clearred",
						 "replacement":       "clearred"
						 },

	"clinged":         {"word":    "clinged",
						 "replacement":       "clung"
						 },

	"cloged":         {"word":    "cloged",
						 "replacement":       "clogged"
						 },

	"cloudded":         {"word":    "cloudded",
						 "replacement":       "clouded"
						 },

	"clusterred":         {"word":    "clusterred",
						 "replacement":       "clustered"
						 },

	"coilled":         {"word":    "coilled",
						 "replacement":       "coiled"
						 },

	"colded":         {"word":    "colded",
						 "replacement":       "cold"
						 },

	"collarred":         {"word":    "collarred",
						 "replacement":       "collared"
						 },

	"comed":         {"word":    "comed",
						 "replacement":       "came"
						 },

	"commissionned":         {"word":    "commissionned",
						 "replacement":       "commissioned"
						 },

	"commited":         {"word":    "commited",
						 "replacement":       "committed"
						 },

	"compeled":         {"word":    "compeled",
						 "replacement":       "compelled"
						 },

	"complainned":         {"word":    "complainned",
						 "replacement":       "complained"
						 },

	"concealled":         {"word":    "concealled",
						 "replacement":       "concealed"
						 },

	"confered":         {"word":    "confered",
						 "replacement":       "conferred"
						 },

	"conquerred":         {"word":    "conquerred",
						 "replacement":       "conquered"
						 },

	"considerred":         {"word":    "considerred",
						 "replacement":       "considered"
						 },

	"containned":         {"word":    "containned",
						 "replacement":       "contained"
						 },

	"controled":         {"word":    "controled",
						 "replacement":       "controlled"
						 },

	"conveied":         {"word":    "conveied",
						 "replacement":       "conveyed"
						 },

	"cookings":         {"word":    "cookings",
						 "replacement":       "cooking"
						 },

	"cookked":         {"word":    "cookked",
						 "replacement":       "cooked"
						 },

	"coolled":         {"word":    "coolled",
						 "replacement":       "cooled"
						 },

	"coverred":         {"word":    "coverred",
						 "replacement":       "covered"
						 },

	"cramed":         {"word":    "cramed",
						 "replacement":       "crammed"
						 },

	"creammed":         {"word":    "creammed",
						 "replacement":       "creamed"
						 },

	"creeped":         {"word":    "creeped",
						 "replacement":       "crept"
						 },

	"creepped":         {"word":    "creepped",
						 "replacement":       "crept"
						 },

	"crimsonned":         {"word":    "crimsonned",
						 "replacement":       "crimsoned"
						 },

	"croakked":         {"word":    "croakked",
						 "replacement":       "croaked"
						 },

	"crookked":         {"word":    "crookked",
						 "replacement":       "crooked"
						 },

	"croonned":         {"word":    "croonned",
						 "replacement":       "crooned"
						 },

	"croped":         {"word":    "croped",
						 "replacement":       "cropped"
						 },

	"crowwed":         {"word":    "crowwed",
						 "replacement":       "crowed"
						 },

	"cushionned":         {"word":    "cushionned",
						 "replacement":       "cushioned"
						 },

	"cuted":         {"word":    "cuted",
						 "replacement":       "cut"
						 },

	"cutted":         {"word":    "cutted",
						 "replacement":       "cut"
						 },

	"dampenned":         {"word":    "dampenned",
						 "replacement":       "dampened"
						 },

	"darkenned":         {"word":    "darkenned",
						 "replacement":       "darkened"
						 },

	"daubbed":         {"word":    "daubbed",
						 "replacement":       "daubed"
						 },

	"deadded":         {"word":    "deadded",
						 "replacement":       "dead"
						 },

	"deaded":         {"word":    "deaded",
						 "replacement":       "dead"
						 },

	"deadenned":         {"word":    "deadenned",
						 "replacement":       "deadened"
						 },

	"deafed":         {"word":    "deafed",
						 "replacement":       "deaf"
						 },

	"dealed":         {"word":    "dealed",
						 "replacement":       "dealt"
						 },

	"dealled":         {"word":    "dealled",
						 "replacement":       "dealt"
						 },

	"decaied":         {"word":    "decaied",
						 "replacement":       "decayed"
						 },

	"decipherred":         {"word":    "decipherred",
						 "replacement":       "deciphered"
						 },

	"declaimmed":         {"word":    "declaimmed",
						 "replacement":       "declaimed"
						 },

	"deemmed":         {"word":    "deemmed",
						 "replacement":       "deemed"
						 },

	"deep-seted":         {"word":    "deep-seted",
						 "replacement":       "deep-set"
						 },

	"deepenned":         {"word":    "deepenned",
						 "replacement":       "deepened"
						 },

	"delaied":         {"word":    "delaied",
						 "replacement":       "delayed"
						 },

	"deliverred":         {"word":    "deliverred",
						 "replacement":       "delivered"
						 },

	"demured":         {"word":    "demured",
						 "replacement":       "demurred"
						 },

	"depositted":         {"word":    "depositted",
						 "replacement":       "deposited"
						 },

	"destroied":         {"word":    "destroied",
						 "replacement":       "destroyed"
						 },

	"destroied":         {"word":    "destroied",
						 "replacement":       "destroyed"
						 },

	"detailled":         {"word":    "detailled",
						 "replacement":       "detailed"
						 },

	"detered":         {"word":    "detered",
						 "replacement":       "deterred"
						 },

	"developped":         {"word":    "developped",
						 "replacement":       "developed"
						 },

	"devourred":         {"word":    "devourred",
						 "replacement":       "devoured"
						 },

	"diged":         {"word":    "diged",
						 "replacement":       "dug"
						 },

	"digged":         {"word":    "digged",
						 "replacement":       "dug"
						 },

	"dimed":         {"word":    "dimed",
						 "replacement":       "dimmed"
						 },

	"diped":         {"word":    "diped",
						 "replacement":       "dipped"
						 },

	"disappearred":         {"word":    "disappearred",
						 "replacement":       "disappeared"
						 },

	"discoverred":         {"word":    "discoverred",
						 "replacement":       "discovered"
						 },

	"disemboweled":         {"word":    "disemboweled",
						 "replacement":       "disembowelled"
						 },

	"disheveled":         {"word":    "disheveled",
						 "replacement":       "dishevelled"
						 },

	"disinheritted":         {"word":    "disinheritted",
						 "replacement":       "disinherited"
						 },

	"dismaied":         {"word":    "dismaied",
						 "replacement":       "dismayed"
						 },

	"disorderred":         {"word":    "disorderred",
						 "replacement":       "disordered"
						 },

	"displaied":         {"word":    "displaied",
						 "replacement":       "displayed"
						 },

	"ditherred":         {"word":    "ditherred",
						 "replacement":       "dithered"
						 },

	"doed":         {"word":    "doed",
						 "replacement":       "did"
						 },

	"doned":         {"word":    "doned",
						 "replacement":       "done"
						 },

	"doommed":         {"word":    "doommed",
						 "replacement":       "doomed"
						 },

	"downcasted":         {"word":    "downcasted",
						 "replacement":       "downcast"
						 },

	"draged":         {"word":    "draged",
						 "replacement":       "dragged"
						 },

	"drainned":         {"word":    "drainned",
						 "replacement":       "drained"
						 },

	"drawed":         {"word":    "drawed",
						 "replacement":       "drew"
						 },

	"drawned":         {"word":    "drawned",
						 "replacement":       "drawn"
						 },

	"drawwed":         {"word":    "drawwed",
						 "replacement":       "drew"
						 },

	"dreammed":         {"word":    "dreammed",
						 "replacement":       "dreamed"
						 },

	"drewed":         {"word":    "drewed",
						 "replacement":       "drew"
						 },

	"drewwed":         {"word":    "drewwed",
						 "replacement":       "drew"
						 },

	"dried-uped":         {"word":    "dried-uped",
						 "replacement":       "dried-up"
						 },

	"drinked":         {"word":    "drinked",
						 "replacement":       "drank"
						 },

	"driped":         {"word":    "driped",
						 "replacement":       "dripped"
						 },

	"drived":         {"word":    "drived",
						 "replacement":       "drove"
						 },

	"driveled":         {"word":    "driveled",
						 "replacement":       "drivelled"
						 },

	"drivened":         {"word":    "drivened",
						 "replacement":       "driven"
						 },

	"drivenned":         {"word":    "drivenned",
						 "replacement":       "driven"
						 },

	"droopped":         {"word":    "droopped",
						 "replacement":       "drooped"
						 },

	"droped":         {"word":    "droped",
						 "replacement":       "dropped"
						 },

	"drumed":         {"word":    "drumed",
						 "replacement":       "drummed"
						 },

	"drunked":         {"word":    "drunked",
						 "replacement":       "drunk"
						 },

	"duged":         {"word":    "duged",
						 "replacement":       "dug"
						 },

	"dwelled":         {"word":    "dwelled",
						 "replacement":       "dwelt"
						 },

	"eated":         {"word":    "eated",
						 "replacement":       "ate"
						 },

	"eatted":         {"word":    "eatted",
						 "replacement":       "ate"
						 },

	"editted":         {"word":    "editted",
						 "replacement":       "edited"
						 },

	"embitterred":         {"word":    "embitterred",
						 "replacement":       "embittered"
						 },

	"embroilled":         {"word":    "embroilled",
						 "replacement":       "embroiled"
						 },

	"emited":         {"word":    "emited",
						 "replacement":       "emitted"
						 },

	"endangerred":         {"word":    "endangerred",
						 "replacement":       "endangered"
						 },

	"endowwed":         {"word":    "endowwed",
						 "replacement":       "endowed"
						 },

	"engenderred":         {"word":    "engenderred",
						 "replacement":       "engendered"
						 },

	"enjoied":         {"word":    "enjoied",
						 "replacement":       "enjoyed"
						 },

	"enlightenned":         {"word":    "enlightenned",
						 "replacement":       "enlightened"
						 },

	"entailled":         {"word":    "entailled",
						 "replacement":       "entailed"
						 },

	"enterred":         {"word":    "enterred",
						 "replacement":       "entered"
						 },

	"enterred":         {"word":    "enterred",
						 "replacement":       "entered"
						 },

	"entertainned":         {"word":    "entertainned",
						 "replacement":       "entertained"
						 },

	"envelopped":         {"word":    "envelopped",
						 "replacement":       "enveloped"
						 },

	"envisionned":         {"word":    "envisionned",
						 "replacement":       "envisioned"
						 },

	"equaled":         {"word":    "equaled",
						 "replacement":       "equalled"
						 },

	"equiped":         {"word":    "equiped",
						 "replacement":       "equipped"
						 },

	"esteemmed":         {"word":    "esteemmed",
						 "replacement":       "esteemed"
						 },

	"exceled":         {"word":    "exceled",
						 "replacement":       "excelled"
						 },

	"exclaimmed":         {"word":    "exclaimmed",
						 "replacement":       "exclaimed"
						 },

	"exhibitted":         {"word":    "exhibitted",
						 "replacement":       "exhibited"
						 },

	"exitted":         {"word":    "exitted",
						 "replacement":       "exited"
						 },

	"explainned":         {"word":    "explainned",
						 "replacement":       "explained"
						 },

	"exploitted":         {"word":    "exploitted",
						 "replacement":       "exploited"
						 },

	"failled":         {"word":    "failled",
						 "replacement":       "failed"
						 },

	"falled":         {"word":    "falled",
						 "replacement":       "fell"
						 },

	"falterred":         {"word":    "falterred",
						 "replacement":       "faltered"
						 },

	"faned":         {"word":    "faned",
						 "replacement":       "fanned"
						 },

	"fashionned":         {"word":    "fashionned",
						 "replacement":       "fashioned"
						 },

	"fastenned":         {"word":    "fastenned",
						 "replacement":       "fastened"
						 },

	"fathommed":         {"word":    "fathommed",
						 "replacement":       "fathomed"
						 },

	"fearred":         {"word":    "fearred",
						 "replacement":       "feared"
						 },

	"feeled":         {"word":    "feeled",
						 "replacement":       "felt"
						 },

	"feelled":         {"word":    "feelled",
						 "replacement":       "felt"
						 },

	"feelled":         {"word":    "feelled",
						 "replacement":       "felt"
						 },

	"felted":         {"word":    "felted",
						 "replacement":       "felt"
						 },

	"festerred":         {"word":    "festerred",
						 "replacement":       "festered"
						 },

	"fighted":         {"word":    "fighted",
						 "replacement":       "fought"
						 },

	"finded":         {"word":    "finded",
						 "replacement":       "found"
						 },

	"fited":         {"word":    "fited",
						 "replacement":       "fitted"
						 },

	"fixxed":         {"word":    "fixxed",
						 "replacement":       "fixed"
						 },

	"flattenned":         {"word":    "flattenned",
						 "replacement":       "flattened"
						 },

	"flatterred":         {"word":    "flatterred",
						 "replacement":       "flattered"
						 },

	"fleed":         {"word":    "fleed",
						 "replacement":       "fled"
						 },

	"flexxed":         {"word":    "flexxed",
						 "replacement":       "flexed"
						 },

	"flickerred":         {"word":    "flickerred",
						 "replacement":       "flickered"
						 },

	"flied":         {"word":    "flied",
						 "replacement":       "flew"
						 },

	"flinged":         {"word":    "flinged",
						 "replacement":       "flung"
						 },

	"fliped":         {"word":    "fliped",
						 "replacement":       "flipped"
						 },

	"flited":         {"word":    "flited",
						 "replacement":       "flitted"
						 },

	"floatted":         {"word":    "floatted",
						 "replacement":       "floated"
						 },

	"flowwed":         {"word":    "flowwed",
						 "replacement":       "flowed"
						 },

	"flusterred":         {"word":    "flusterred",
						 "replacement":       "flustered"
						 },

	"flutterred":         {"word":    "flutterred",
						 "replacement":       "fluttered"
						 },

	"foammed":         {"word":    "foammed",
						 "replacement":       "foamed"
						 },

	"followwed":         {"word":    "followwed",
						 "replacement":       "followed"
						 },

	"footted":         {"word":    "footted",
						 "replacement":       "footed"
						 },

	"forbidded":         {"word":    "forbidded",
						 "replacement":       "forbade"
						 },

	"forbided":         {"word":    "forbided",
						 "replacement":       "forbade"
						 },

	"foresweared":         {"word":    "foresweared",
						 "replacement":       "foreswore"
						 },

	"foreswearred":         {"word":    "foreswearred",
						 "replacement":       "foreswore"
						 },

	"forgeted":         {"word":    "forgeted",
						 "replacement":       "forgot"
						 },

	"forgetted":         {"word":    "forgetted",
						 "replacement":       "forgot"
						 },

	"forgived":         {"word":    "forgived",
						 "replacement":       "forgave"
						 },

	"formated":         {"word":    "formated",
						 "replacement":       "formatted"
						 },

	"fosterred":         {"word":    "fosterred",
						 "replacement":       "fostered"
						 },

	"founderred":         {"word":    "founderred",
						 "replacement":       "foundered"
						 },

	"freewheelled":         {"word":    "freewheelled",
						 "replacement":       "freewheeled"
						 },

	"freezed":         {"word":    "freezed",
						 "replacement":       "froze"
						 },

	"freshenned":         {"word":    "freshenned",
						 "replacement":       "freshened"
						 },

	"freted":         {"word":    "freted",
						 "replacement":       "fretted"
						 },

	"frightenned":         {"word":    "frightenned",
						 "replacement":       "frightened"
						 },

	"fritterred":         {"word":    "fritterred",
						 "replacement":       "frittered"
						 },

	"frolicced":         {"word":    "frolicced",
						 "replacement":       "frolicked"
						 },

	"froliced":         {"word":    "froliced",
						 "replacement":       "frolicked"
						 },

	"functionned":         {"word":    "functionned",
						 "replacement":       "functioned"
						 },

	"fured":         {"word":    "fured",
						 "replacement":       "furred"
						 },

	"furrowwed":         {"word":    "furrowwed",
						 "replacement":       "furrowed"
						 },

	"gaged":         {"word":    "gaged",
						 "replacement":       "gagged"
						 },

	"gaied":         {"word":    "gaied",
						 "replacement":       "merry"
						 },

	"gainned":         {"word":    "gainned",
						 "replacement":       "gained"
						 },

	"gallopped":         {"word":    "gallopped",
						 "replacement":       "galloped"
						 },

	"gatherred":         {"word":    "gatherred",
						 "replacement":       "gathered"
						 },

	"geted":         {"word":    "geted",
						 "replacement":       "got"
						 },

	"getted":         {"word":    "getted",
						 "replacement":       "got"
						 },

	"gived":         {"word":    "gived",
						 "replacement":       "gave"
						 },

	"givened":         {"word":    "givened",
						 "replacement":       "given"
						 },

	"gladdenned":         {"word":    "gladdenned",
						 "replacement":       "gladdened"
						 },

	"gleammed":         {"word":    "gleammed",
						 "replacement":       "gleamed"
						 },

	"glitterred":         {"word":    "glitterred",
						 "replacement":       "glittered"
						 },

	"gloatted":         {"word":    "gloatted",
						 "replacement":       "gloated"
						 },

	"glowerred":         {"word":    "glowerred",
						 "replacement":       "glowered"
						 },

	"glowwed":         {"word":    "glowwed",
						 "replacement":       "glowed"
						 },

	"gnawwed":         {"word":    "gnawwed",
						 "replacement":       "gnawed"
						 },

	"goadded":         {"word":    "goadded",
						 "replacement":       "goaded"
						 },

	"goed":         {"word":    "goed",
						 "replacement":       "went"
						 },

	"grabed":         {"word":    "grabed",
						 "replacement":       "grabbed"
						 },

	"graied":         {"word":    "graied",
						 "replacement":       "grayed"
						 },

	"greetted":         {"word":    "greetted",
						 "replacement":       "greeted"
						 },

	"greied":         {"word":    "greied",
						 "replacement":       "greyed"
						 },

	"grinded":         {"word":    "grinded",
						 "replacement":       "ground"
						 },

	"groanned":         {"word":    "groanned",
						 "replacement":       "groaned"
						 },

	"growed":         {"word":    "growed",
						 "replacement":       "grew"
						 },

	"growwed":         {"word":    "growwed",
						 "replacement":       "grew"
						 },

	"gutterred":         {"word":    "gutterred",
						 "replacement":       "guttered"
						 },

	"hailled":         {"word":    "hailled",
						 "replacement":       "hailed"
						 },

	"halfed":         {"word":    "halfed",
						 "replacement":       "halved"
						 },

	"hammerred":         {"word":    "hammerred",
						 "replacement":       "hammered"
						 },

	"handbuilded":         {"word":    "handbuilded",
						 "replacement":       "handbuilt"
						 },

	"hankerred":         {"word":    "hankerred",
						 "replacement":       "hankered"
						 },

	"happenned":         {"word":    "happenned",
						 "replacement":       "happened"
						 },

	"haulled":         {"word":    "haulled",
						 "replacement":       "hauled"
						 },

	"haved":         {"word":    "haved",
						 "replacement":       "had"
						 },

	"headded":         {"word":    "headded",
						 "replacement":       "headed"
						 },

	"heapped":         {"word":    "heapped",
						 "replacement":       "heaped"
						 },

	"hearded":         {"word":    "hearded",
						 "replacement":       "heard"
						 },

	"heared":         {"word":    "heared",
						 "replacement":       "heard"
						 },

	"hearred":         {"word":    "hearred",
						 "replacement":       "heard"
						 },

	"heatted":         {"word":    "heatted",
						 "replacement":       "heated"
						 },

	"heelled":         {"word":    "heelled",
						 "replacement":       "heeled"
						 },

	"heightenned":         {"word":    "heightenned",
						 "replacement":       "heightened"
						 },

	"hemed":         {"word":    "hemed",
						 "replacement":       "hemmed"
						 },

	"hewwed":         {"word":    "hewwed",
						 "replacement":       "hewed"
						 },

	"hided":         {"word":    "hided",
						 "replacement":       "hid"
						 },

	"hited":         {"word":    "hited",
						 "replacement":       "hit"
						 },

	"hitted":         {"word":    "hitted",
						 "replacement":       "hit"
						 },

	"holded":         {"word":    "holded",
						 "replacement":       "held"
						 },

	"hoodded":         {"word":    "hoodded",
						 "replacement":       "hooded"
						 },

	"hookked":         {"word":    "hookked",
						 "replacement":       "hooked"
						 },

	"hoopped":         {"word":    "hoopped",
						 "replacement":       "hooped"
						 },

	"hootted":         {"word":    "hootted",
						 "replacement":       "hooted"
						 },

	"hoverred":         {"word":    "hoverred",
						 "replacement":       "hovered"
						 },

	"huged":         {"word":    "huged",
						 "replacement":       "hugged"
						 },

	"humed":         {"word":    "humed",
						 "replacement":       "hummed"
						 },

	"hurted":         {"word":    "hurted",
						 "replacement":       "hurt"
						 },

	"impairred":         {"word":    "impairred",
						 "replacement":       "impaired"
						 },

	"impeled":         {"word":    "impeled",
						 "replacement":       "impelled"
						 },

	"imprisonned":         {"word":    "imprisonned",
						 "replacement":       "imprisoned"
						 },

	"inhabitted":         {"word":    "inhabitted",
						 "replacement":       "inhabited"
						 },

	"inheritted":         {"word":    "inheritted",
						 "replacement":       "inherited"
						 },

	"inhibitted":         {"word":    "inhibitted",
						 "replacement":       "inhibited"
						 },

	"injuried":         {"word":    "injuried",
						 "replacement":       "injured"
						 },

	"interpretted":         {"word":    "interpretted",
						 "replacement":       "interpreted"
						 },

	"interviewwed":         {"word":    "interviewwed",
						 "replacement":       "interviewed"
						 },

	"ironned":         {"word":    "ironned",
						 "replacement":       "ironed"
						 },

	"jabed":         {"word":    "jabed",
						 "replacement":       "jabbed"
						 },

	"jamed":         {"word":    "jamed",
						 "replacement":       "jammed"
						 },

	"joged":         {"word":    "joged",
						 "replacement":       "jogged"
						 },

	"joied":         {"word":    "joied",
						 "replacement":       "joyed"
						 },

	"joinned":         {"word":    "joinned",
						 "replacement":       "joined"
						 },

	"judderred":         {"word":    "judderred",
						 "replacement":       "juddered"
						 },

	"keeped":         {"word":    "keeped",
						 "replacement":       "kept"
						 },

	"keepped":         {"word":    "keepped",
						 "replacement":       "kept"
						 },

	"kidnaped":         {"word":    "kidnaped",
						 "replacement":       "kidnapped"
						 },

	"kneadded":         {"word":    "kneadded",
						 "replacement":       "kneaded"
						 },

	"kneelled":         {"word":    "kneelled",
						 "replacement":       "kneeled"
						 },

	"knited":         {"word":    "knited",
						 "replacement":       "knitted"
						 },

	"knowed":         {"word":    "knowed",
						 "replacement":       "knew"
						 },

	"knowed":         {"word":    "knowed",
						 "replacement":       "knew"
						 },

	"knowned":         {"word":    "knowned",
						 "replacement":       "knew"
						 },

	"knowwed":         {"word":    "knowwed",
						 "replacement":       "knew"
						 },

	"labeled":         {"word":    "labeled",
						 "replacement":       "labelled"
						 },

	"ladderred":         {"word":    "ladderred",
						 "replacement":       "laddered"
						 },

	"laidded":         {"word":    "laidded",
						 "replacement":       "laid"
						 },

	"laided":         {"word":    "laided",
						 "replacement":       "laid"
						 },

	"laied":         {"word":    "laied",
						 "replacement":       "laid"
						 },

	"laudded":         {"word":    "laudded",
						 "replacement":       "lauded"
						 },

	"leadded":         {"word":    "leadded",
						 "replacement":       "leaded"
						 },

	"leadded":         {"word":    "leadded",
						 "replacement":       "led"
						 },

	"leakked":         {"word":    "leakked",
						 "replacement":       "leaked"
						 },

	"leanned":         {"word":    "leanned",
						 "replacement":       "leaned"
						 },

	"leapped":         {"word":    "leapped",
						 "replacement":       "leaped"
						 },

	"leaved":         {"word":    "leaved",
						 "replacement":       "left"
						 },

	"leerred":         {"word":    "leerred",
						 "replacement":       "leered"
						 },

	"lefted":         {"word":    "lefted",
						 "replacement":       "left"
						 },

	"lended":         {"word":    "lended",
						 "replacement":       "lent"
						 },

	"leted":         {"word":    "leted",
						 "replacement":       "let"
						 },

	"letted":         {"word":    "letted",
						 "replacement":       "let"
						 },

	"leveled":         {"word":    "leveled",
						 "replacement":       "levelled"
						 },

	"libeled":         {"word":    "libeled",
						 "replacement":       "libelled"
						 },

	"lightenned":         {"word":    "lightenned",
						 "replacement":       "lightened"
						 },

	"limitted":         {"word":    "limitted",
						 "replacement":       "limited"
						 },

	"lingerred":         {"word":    "lingerred",
						 "replacement":       "lingered"
						 },

	"listenned":         {"word":    "listenned",
						 "replacement":       "listened"
						 },

	"litterred":         {"word":    "litterred",
						 "replacement":       "littered"
						 },

	"loadded":         {"word":    "loadded",
						 "replacement":       "loaded"
						 },

	"loging":         {"word":    "loging",
						 "replacement":       "logging"
						 },

	"loiterred":         {"word":    "loiterred",
						 "replacement":       "loitered"
						 },

	"lookked":         {"word":    "lookked",
						 "replacement":       "looked"
						 },

	"loommed":         {"word":    "loommed",
						 "replacement":       "loomed"
						 },

	"loosenned":         {"word":    "loosenned",
						 "replacement":       "loosened"
						 },

	"lootted":         {"word":    "lootted",
						 "replacement":       "looted"
						 },

	"losed":         {"word":    "losed",
						 "replacement":       "lost"
						 },

	"losted":         {"word":    "losted",
						 "replacement":       "lost"
						 },

	"lowerred":         {"word":    "lowerred",
						 "replacement":       "lowered"
						 },

	"lumberred":         {"word":    "lumberred",
						 "replacement":       "lumbered"
						 },

	"maded":         {"word":    "maded",
						 "replacement":       "made"
						 },

	"mailled":         {"word":    "mailled",
						 "replacement":       "mailed"
						 },

	"maimmed":         {"word":    "maimmed",
						 "replacement":       "maimed"
						 },

	"maintainned":         {"word":    "maintainned",
						 "replacement":       "maintained"
						 },

	"maked":         {"word":    "maked",
						 "replacement":       "made"
						 },

	"maped":         {"word":    "maped",
						 "replacement":       "mapped"
						 },

	"mared":         {"word":    "mared",
						 "replacement":       "marred"
						 },

	"maritaled":         {"word":    "maritaled",
						 "replacement":       "married"
						 },

	"maritalled":         {"word":    "maritalled",
						 "replacement":       "married"
						 },

	"meaned":         {"word":    "meaned",
						 "replacement":       "meant"
						 },

	"meanned":         {"word":    "meanned",
						 "replacement":       "meant"
						 },

	"meeted":         {"word":    "meeted",
						 "replacement":       "met"
						 },

	"meetted":         {"word":    "meetted",
						 "replacement":       "met"
						 },

	"mellowwed":         {"word":    "mellowwed",
						 "replacement":       "mellowed"
						 },

	"mentionned":         {"word":    "mentionned",
						 "replacement":       "mentioned"
						 },

	"meterred":         {"word":    "meterred",
						 "replacement":       "metered"
						 },

	"mimicced":         {"word":    "mimicced",
						 "replacement":       "mimicked"
						 },

	"ministerred":         {"word":    "ministerred",
						 "replacement":       "ministered"
						 },

	"mirrorred":         {"word":    "mirrorred",
						 "replacement":       "mirrored"
						 },

	"miserabled":         {"word":    "miserabled",
						 "replacement":       "miserable"
						 },

	"mislaided":         {"word":    "mislaided",
						 "replacement":       "mislaid"
						 },

	"misleaded":         {"word":    "misleaded",
						 "replacement":       "misled"
						 },

	"mistreatted":         {"word":    "mistreatted",
						 "replacement":       "mistreated"
						 },

	"mixxed":         {"word":    "mixxed",
						 "replacement":       "mixed"
						 },

	"modeled":         {"word":    "modeled",
						 "replacement":       "modelled"
						 },

	"moistenned":         {"word":    "moistenned",
						 "replacement":       "moistened"
						 },

	"moorred":         {"word":    "moorred",
						 "replacement":       "moored"
						 },

	"murderred":         {"word":    "murderred",
						 "replacement":       "murdered"
						 },

	"murmurred":         {"word":    "murmurred",
						 "replacement":       "murmured"
						 },

	"musterred":         {"word":    "musterred",
						 "replacement":       "mustered"
						 },

	"nailled":         {"word":    "nailled",
						 "replacement":       "nailed"
						 },

	"neted":         {"word":    "neted",
						 "replacement":       "netted"
						 },

	"niped":         {"word":    "niped",
						 "replacement":       "nipped"
						 },

	"noded":         {"word":    "noded",
						 "replacement":       "nodded"
						 },

	"numberred":         {"word":    "numberred",
						 "replacement":       "numbered"
						 },

	"obeied":         {"word":    "obeied",
						 "replacement":       "obeyed"
						 },

	"obtainned":         {"word":    "obtainned",
						 "replacement":       "obtained"
						 },

	"obtainned":         {"word":    "obtainned",
						 "replacement":       "obtained"
						 },

	"occasionned":         {"word":    "occasionned",
						 "replacement":       "occasioned"
						 },

	"occured":         {"word":    "occured",
						 "replacement":       "occurred"
						 },

	"offerred":         {"word":    "offerred",
						 "replacement":       "offered"
						 },

	"openned":         {"word":    "openned",
						 "replacement":       "opened"
						 },

	"opinionned":         {"word":    "opinionned",
						 "replacement":       "opinioned"
						 },

	"ordainned":         {"word":    "ordainned",
						 "replacement":       "ordained"
						 },

	"orderred":         {"word":    "orderred",
						 "replacement":       "ordered"
						 },

	"outgrowed":         {"word":    "outgrowed",
						 "replacement":       "outgrew"
						 },

	"outspreadded":         {"word":    "outspreadded",
						 "replacement":       "outspread"
						 },

	"outspreaded":         {"word":    "outspreaded",
						 "replacement":       "outspread"
						 },

	"overcomed":         {"word":    "overcomed",
						 "replacement":       "overcame"
						 },

	"overdoed":         {"word":    "overdoed",
						 "replacement":       "overdid"
						 },

	"overflowwed":         {"word":    "overflowwed",
						 "replacement":       "overflowed"
						 },

	"overjoied":         {"word":    "overjoied",
						 "replacement":       "overjoyed"
						 },

	"overlaied":         {"word":    "overlaied",
						 "replacement":       "overlaid"
						 },

	"overlookked":         {"word":    "overlookked",
						 "replacement":       "overlooked"
						 },

	"overpaied":         {"word":    "overpaied",
						 "replacement":       "overpaid"
						 },

	"overpowerred":         {"word":    "overpowerred",
						 "replacement":       "overpowered"
						 },

	"overruned":         {"word":    "overruned",
						 "replacement":       "overran"
						 },

	"overseed":         {"word":    "overseed",
						 "replacement":       "oversaw"
						 },

	"overseing":         {"word":    "overseing",
						 "replacement":       "overseeing"
						 },

	"overshadowwed":         {"word":    "overshadowwed",
						 "replacement":       "overshadowed"
						 },

	"overtaked":         {"word":    "overtaked",
						 "replacement":       "overtook"
						 },

	"overthrowed":         {"word":    "overthrowed",
						 "replacement":       "overthrew"
						 },

	"overthrowwed":         {"word":    "overthrowwed",
						 "replacement":       "overthrew"
						 },

	"paded":         {"word":    "paded",
						 "replacement":       "padded"
						 },

	"paidded":         {"word":    "paidded",
						 "replacement":       "paid"
						 },

	"paided":         {"word":    "paided",
						 "replacement":       "paid"
						 },

	"paied":         {"word":    "paied",
						 "replacement":       "paid"
						 },

	"painned":         {"word":    "painned",
						 "replacement":       "pained"
						 },

	"pamperred":         {"word":    "pamperred",
						 "replacement":       "pampered"
						 },

	"paneled":         {"word":    "paneled",
						 "replacement":       "panelled"
						 },

	"panickied":         {"word":    "panickied",
						 "replacement":       "panicked"
						 },

	"pardonned":         {"word":    "pardonned",
						 "replacement":       "pardoned"
						 },

	"partaked":         {"word":    "partaked",
						 "replacement":       "partook"
						 },

	"partitionned":         {"word":    "partitionned",
						 "replacement":       "partitioned"
						 },

	"patterred":         {"word":    "patterred",
						 "replacement":       "pattered"
						 },

	"peepped":         {"word":    "peepped",
						 "replacement":       "peeped"
						 },

	"peerred":         {"word":    "peerred",
						 "replacement":       "peered"
						 },

	"penciled":         {"word":    "penciled",
						 "replacement":       "pencilled"
						 },

	"pepperred":         {"word":    "pepperred",
						 "replacement":       "peppered"
						 },

	"perennialed":         {"word":    "perennialed",
						 "replacement":       "perennial"
						 },

	"permited":         {"word":    "permited",
						 "replacement":       "permitted"
						 },

	"perplexxed":         {"word":    "perplexxed",
						 "replacement":       "perplexed"
						 },

	"pilferred":         {"word":    "pilferred",
						 "replacement":       "pilfered"
						 },

	"pillowwed":         {"word":    "pillowwed",
						 "replacement":       "pillowed"
						 },

	"pinionned":         {"word":    "pinionned",
						 "replacement":       "pinioned"
						 },

	"pited":         {"word":    "pited",
						 "replacement":       "pitted"
						 },

	"plaied":         {"word":    "plaied",
						 "replacement":       "played"
						 },

	"pleadded":         {"word":    "pleadded",
						 "replacement":       "pleaded"
						 },

	"ploted":         {"word":    "ploted",
						 "replacement":       "plotted"
						 },

	"pluged":         {"word":    "pluged",
						 "replacement":       "plugged"
						 },

	"plunderred":         {"word":    "plunderred",
						 "replacement":       "plundered"
						 },

	"pocketted":         {"word":    "pocketted",
						 "replacement":       "pocketed"
						 },

	"poisonned":         {"word":    "poisonned",
						 "replacement":       "poisoned"
						 },

	"portraied":         {"word":    "portraied",
						 "replacement":       "portrayed"
						 },

	"pourred":         {"word":    "pourred",
						 "replacement":       "poured"
						 },

	"poutted":         {"word":    "poutted",
						 "replacement":       "pouted"
						 },

	"praied":         {"word":    "praied",
						 "replacement":       "prayed"
						 },

	"preenned":         {"word":    "preenned",
						 "replacement":       "preened"
						 },

	"prefered":         {"word":    "prefered",
						 "replacement":       "preferred"
						 },

	"preied":         {"word":    "preied",
						 "replacement":       "preyed"
						 },

	"prevailled":         {"word":    "prevailled",
						 "replacement":       "prevailed"
						 },

	"proclaimmed":         {"word":    "proclaimmed",
						 "replacement":       "proclaimed"
						 },

	"proded":         {"word":    "proded",
						 "replacement":       "prodded"
						 },

	"profitted":         {"word":    "profitted",
						 "replacement":       "profited"
						 },

	"profounded":         {"word":    "profounded",
						 "replacement":       "profound"
						 },

	"propeled":         {"word":    "propeled",
						 "replacement":       "propelled"
						 },

	"puckerred":         {"word":    "puckerred",
						 "replacement":       "puckered"
						 },

	"puted":         {"word":    "puted",
						 "replacement":       "put"
						 },

	"putted":         {"word":    "putted",
						 "replacement":       "put"
						 },

	"quarreled":         {"word":    "quarreled",
						 "replacement":       "quarrelled"
						 },

	"quarterred":         {"word":    "quarterred",
						 "replacement":       "quartered"
						 },

	"quaverred":         {"word":    "quaverred",
						 "replacement":       "quavered"
						 },

	"questionned":         {"word":    "questionned",
						 "replacement":       "questioned"
						 },

	"quickenned":         {"word":    "quickenned",
						 "replacement":       "quickened"
						 },

	"quietenned":         {"word":    "quietenned",
						 "replacement":       "quietened"
						 },

	"quietted":         {"word":    "quietted",
						 "replacement":       "quieted"
						 },

	"quiverred":         {"word":    "quiverred",
						 "replacement":       "quivered"
						 },

	"rainned":         {"word":    "rainned",
						 "replacement":       "rained"
						 },

	"ramed":         {"word":    "ramed",
						 "replacement":       "rammed"
						 },

	"readded":         {"word":    "readded",
						 "replacement":       "read"
						 },

	"readed":         {"word":    "readed",
						 "replacement":       "read"
						 },

	"reappearred":         {"word":    "reappearred",
						 "replacement":       "reappeared"
						 },

	"reapped":         {"word":    "reapped",
						 "replacement":       "reaped"
						 },

	"rearred":         {"word":    "rearred",
						 "replacement":       "reared"
						 },

	"reasonned":         {"word":    "reasonned",
						 "replacement":       "reasoned"
						 },

	"rebeled":         {"word":    "rebeled",
						 "replacement":       "rebelled"
						 },

	"rebuilded":         {"word":    "rebuilded",
						 "replacement":       "rebuilt"
						 },

	"reckonned":         {"word":    "reckonned",
						 "replacement":       "reckoned"
						 },

	"reclaimmed":         {"word":    "reclaimmed",
						 "replacement":       "reclaimed"
						 },

	"recoverred":         {"word":    "recoverred",
						 "replacement":       "recovered"
						 },

	"recruitted":         {"word":    "recruitted",
						 "replacement":       "recruited"
						 },

	"recured":         {"word":    "recured",
						 "replacement":       "recurred"
						 },

	"reddenned":         {"word":    "reddenned",
						 "replacement":       "reddened"
						 },

	"reelled":         {"word":    "reelled",
						 "replacement":       "reeled"
						 },

	"refered":         {"word":    "refered",
						 "replacement":       "referred"
						 },

	"refered":         {"word":    "refered",
						 "replacement":       "referred"
						 },

	"registerred":         {"word":    "registerred",
						 "replacement":       "registered"
						 },

	"regreted":         {"word":    "regreted",
						 "replacement":       "regretted"
						 },

	"rejoinned":         {"word":    "rejoinned",
						 "replacement":       "rejoined"
						 },

	"relaxxed":         {"word":    "relaxxed",
						 "replacement":       "relaxed"
						 },

	"remainned":         {"word":    "remainned",
						 "replacement":       "remained"
						 },

	"rememberred":         {"word":    "rememberred",
						 "replacement":       "remembered"
						 },

	"rememberred":         {"word":    "rememberred",
						 "replacement":       "remembered"
						 },

	"remited":         {"word":    "remited",
						 "replacement":       "remitted"
						 },

	"renderred":         {"word":    "renderred",
						 "replacement":       "rendered"
						 },

	"reopenned":         {"word":    "reopenned",
						 "replacement":       "reopened"
						 },

	"repairred":         {"word":    "repairred",
						 "replacement":       "repaired"
						 },

	"repeatted":         {"word":    "repeatted",
						 "replacement":       "repeated"
						 },

	"repeled":         {"word":    "repeled",
						 "replacement":       "repelled"
						 },

	"restrainned":         {"word":    "restrainned",
						 "replacement":       "restrained"
						 },

	"retainned":         {"word":    "retainned",
						 "replacement":       "retained"
						 },

	"retoolled":         {"word":    "retoolled",
						 "replacement":       "retooled"
						 },

	"retreatted":         {"word":    "retreatted",
						 "replacement":       "retreated"
						 },

	"revealled":         {"word":    "revealled",
						 "replacement":       "revealed"
						 },

	"reveled":         {"word":    "reveled",
						 "replacement":       "revelled"
						 },

	"reviewwed":         {"word":    "reviewwed",
						 "replacement":       "reviewed"
						 },

	"rided":         {"word":    "rided",
						 "replacement":       "rode"
						 },

	"riged":         {"word":    "riged",
						 "replacement":       "rigged"
						 },

	"riped":         {"word":    "riped",
						 "replacement":       "ripped"
						 },

	"ripenned":         {"word":    "ripenned",
						 "replacement":       "ripened"
						 },

	"rised":         {"word":    "rised",
						 "replacement":       "rose"
						 },

	"rivetted":         {"word":    "rivetted",
						 "replacement":       "riveted"
						 },

	"roarred":         {"word":    "roarred",
						 "replacement":       "roared"
						 },

	"rootted":         {"word":    "rootted",
						 "replacement":       "rooted"
						 },

	"rosed":         {"word":    "rosed",
						 "replacement":       "rose"
						 },

	"rubed":         {"word":    "rubed",
						 "replacement":       "rubbed"
						 },

	"ruinned":         {"word":    "ruinned",
						 "replacement":       "ruined"
						 },

	"runed":         {"word":    "runed",
						 "replacement":       "ran"
						 },

	"runned":         {"word":    "runned",
						 "replacement":       "ran"
						 },

	"saged":         {"word":    "saged",
						 "replacement":       "sagged"
						 },

	"saied":         {"word":    "saied",
						 "replacement":       "said"
						 },

	"sailled":         {"word":    "sailled",
						 "replacement":       "sailed"
						 },

	"sandbaged":         {"word":    "sandbaged",
						 "replacement":       "sandbagged"
						 },

	"sandpaperred":         {"word":    "sandpaperred",
						 "replacement":       "sandpapered"
						 },

	"saturdaied":         {"word":    "saturdaied",
						 "replacement":       "sat"
						 },

	"sawed":         {"word":    "sawed",
						 "replacement":       "saw"
						 },

	"sawwed":         {"word":    "sawwed",
						 "replacement":       "sawed"
						 },

	"scaned":         {"word":    "scaned",
						 "replacement":       "scanned"
						 },

	"scatterred":         {"word":    "scatterred",
						 "replacement":       "scattered"
						 },

	"scourred":         {"word":    "scourred",
						 "replacement":       "scoured"
						 },

	"scoutted":         {"word":    "scoutted",
						 "replacement":       "scouted"
						 },

	"screammed":         {"word":    "screammed",
						 "replacement":       "screamed"
						 },

	"screwwed":         {"word":    "screwwed",
						 "replacement":       "screwed"
						 },

	"sealled":         {"word":    "sealled",
						 "replacement":       "sealed"
						 },

	"seammed":         {"word":    "seammed",
						 "replacement":       "seamed"
						 },

	"seasonned":         {"word":    "seasonned",
						 "replacement":       "seasoned"
						 },

	"seatted":         {"word":    "seatted",
						 "replacement":       "seated"
						 },

	"seed":         {"word":    "seed",
						 "replacement":       "saw"
						 },

	"seekked":         {"word":    "seekked",
						 "replacement":       "sought"
						 },

	"seemmed":         {"word":    "seemmed",
						 "replacement":       "seemed"
						 },

	"selled":         {"word":    "selled",
						 "replacement":       "sold"
						 },

	"sended":         {"word":    "sended",
						 "replacement":       "sent"
						 },

	"seted":         {"word":    "seted",
						 "replacement":       "set"
						 },

	"setted":         {"word":    "setted",
						 "replacement":       "set"
						 },

	"severred":         {"word":    "severred",
						 "replacement":       "severed"
						 },

	"shadowwed":         {"word":    "shadowwed",
						 "replacement":       "shadowed"
						 },

	"shaked":         {"word":    "shaked",
						 "replacement":       "shook"
						 },

	"sharpenned":         {"word":    "sharpenned",
						 "replacement":       "sharpened"
						 },

	"shatterred":         {"word":    "shatterred",
						 "replacement":       "shattered"
						 },

	"sheerred":         {"word":    "sheerred",
						 "replacement":       "sheered"
						 },

	"shelterred":         {"word":    "shelterred",
						 "replacement":       "sheltered"
						 },

	"shiped":         {"word":    "shiped",
						 "replacement":       "shipped"
						 },

	"shiverred":         {"word":    "shiverred",
						 "replacement":       "shivered"
						 },

	"shooked":         {"word":    "shooked",
						 "replacement":       "shook"
						 },

	"shookked":         {"word":    "shookked",
						 "replacement":       "shook"
						 },

	"shooted":         {"word":    "shooted",
						 "replacement":       "shot"
						 },

	"shootted":         {"word":    "shootted",
						 "replacement":       "shot"
						 },

	"shoulderred":         {"word":    "shoulderred",
						 "replacement":       "shouldered"
						 },

	"shoutted":         {"word":    "shoutted",
						 "replacement":       "shouted"
						 },

	"showerred":         {"word":    "showerred",
						 "replacement":       "showered"
						 },

	"showwed":         {"word":    "showwed",
						 "replacement":       "showed"
						 },

	"shriekked":         {"word":    "shriekked",
						 "replacement":       "shrieked"
						 },

	"shrinked":         {"word":    "shrinked",
						 "replacement":       "shrank"
						 },

	"shriveled":         {"word":    "shriveled",
						 "replacement":       "shrivelled"
						 },

	"shroudded":         {"word":    "shroudded",
						 "replacement":       "shrouded"
						 },

	"shudderred":         {"word":    "shudderred",
						 "replacement":       "shuddered"
						 },

	"shuted":         {"word":    "shuted",
						 "replacement":       "shut"
						 },

	"shutted":         {"word":    "shutted",
						 "replacement":       "shut"
						 },

	"sickenned":         {"word":    "sickenned",
						 "replacement":       "sickened"
						 },

	"sined":         {"word":    "sined",
						 "replacement":       "sinned"
						 },

	"singed":         {"word":    "singed",
						 "replacement":       "sang"
						 },

	"sinked":         {"word":    "sinked",
						 "replacement":       "sank"
						 },

	"sitted":         {"word":    "sitted",
						 "replacement":       "sat"
						 },

	"skimed":         {"word":    "skimed",
						 "replacement":       "skimmed"
						 },

	"slackenned":         {"word":    "slackenned",
						 "replacement":       "slackened"
						 },

	"sleeped":         {"word":    "sleeped",
						 "replacement":       "slept"
						 },

	"sleepped":         {"word":    "sleepped",
						 "replacement":       "slept"
						 },

	"slimed":         {"word":    "slimed",
						 "replacement":       "slimmed"
						 },

	"slinged":         {"word":    "slinged",
						 "replacement":       "slung"
						 },

	"sliped":         {"word":    "sliped",
						 "replacement":       "slipped"
						 },

	"slitherred":         {"word":    "slitherred",
						 "replacement":       "slithered"
						 },

	"sloged":         {"word":    "sloged",
						 "replacement":       "slogged"
						 },

	"smearred":         {"word":    "smearred",
						 "replacement":       "smeared"
						 },

	"smittened":         {"word":    "smittened",
						 "replacement":       "smitten"
						 },

	"smittenned":         {"word":    "smittenned",
						 "replacement":       "smitten"
						 },

	"smotherred":         {"word":    "smotherred",
						 "replacement":       "smothered"
						 },

	"snaped":         {"word":    "snaped",
						 "replacement":       "snapped"
						 },

	"sneakied":         {"word":    "sneakied",
						 "replacement":       "sneaked"
						 },

	"sneakked":         {"word":    "sneakked",
						 "replacement":       "sneaked"
						 },

	"sniveled":         {"word":    "sniveled",
						 "replacement":       "snivelled"
						 },

	"snowwed":         {"word":    "snowwed",
						 "replacement":       "snowed"
						 },

	"snubed":         {"word":    "snubed",
						 "replacement":       "snubbed"
						 },

	"soarred":         {"word":    "soarred",
						 "replacement":       "soared"
						 },

	"sobed":         {"word":    "sobed",
						 "replacement":       "sobbed"
						 },

	"softenned":         {"word":    "softenned",
						 "replacement":       "softened"
						 },

	"solded":         {"word":    "solded",
						 "replacement":       "sold"
						 },

	"solicitted":         {"word":    "solicitted",
						 "replacement":       "solicited"
						 },

	"sorrowwed":         {"word":    "sorrowwed",
						 "replacement":       "sorrowed"
						 },

	"soughted":         {"word":    "soughted",
						 "replacement":       "sought"
						 },

	"sourred":         {"word":    "sourred",
						 "replacement":       "soured"
						 },

	"spatterred":         {"word":    "spatterred",
						 "replacement":       "spattered"
						 },

	"speaked":         {"word":    "speaked",
						 "replacement":       "spoke"
						 },

	"speakked":         {"word":    "speakked",
						 "replacement":       "spoke"
						 },

	"spended":         {"word":    "spended",
						 "replacement":       "spent"
						 },

	"splutterred":         {"word":    "splutterred",
						 "replacement":       "spluttered"
						 },

	"spoilled":         {"word":    "spoilled",
						 "replacement":       "spoiled"
						 },

	"spoked":         {"word":    "spoked",
						 "replacement":       "spoke"
						 },

	"sponsorred":         {"word":    "sponsorred",
						 "replacement":       "sponsored"
						 },

	"spoted":         {"word":    "spoted",
						 "replacement":       "spotted"
						 },

	"spreadded":         {"word":    "spreadded",
						 "replacement":       "spread"
						 },

	"spreaded":         {"word":    "spreaded",
						 "replacement":       "spread"
						 },

	"springed":         {"word":    "springed",
						 "replacement":       "sprang"
						 },

	"springed":         {"word":    "springed",
						 "replacement":       "sprung"
						 },

	"spured":         {"word":    "spured",
						 "replacement":       "spurred"
						 },

	"sputterred":         {"word":    "sputterred",
						 "replacement":       "sputtered"
						 },

	"squated":         {"word":    "squated",
						 "replacement":       "squatted"
						 },

	"staggerred":         {"word":    "staggerred",
						 "replacement":       "staggered"
						 },

	"staied":         {"word":    "staied",
						 "replacement":       "stayed"
						 },

	"stainned":         {"word":    "stainned",
						 "replacement":       "stained"
						 },

	"standed":         {"word":    "standed",
						 "replacement":       "stood"
						 },

	"stationned":         {"word":    "stationned",
						 "replacement":       "stationed"
						 },

	"stealed":         {"word":    "stealed",
						 "replacement":       "stole"
						 },

	"stealled":         {"word":    "stealled",
						 "replacement":       "stole"
						 },

	"steammed":         {"word":    "steammed",
						 "replacement":       "steamed"
						 },

	"steelled":         {"word":    "steelled",
						 "replacement":       "steeled"
						 },

	"steepped":         {"word":    "steepped",
						 "replacement":       "steeped"
						 },

	"steerred":         {"word":    "steerred",
						 "replacement":       "steered"
						 },

	"stemed":         {"word":    "stemed",
						 "replacement":       "stemmed"
						 },

	"steped":         {"word":    "steped",
						 "replacement":       "stepped"
						 },

	"sticked":         {"word":    "sticked",
						 "replacement":       "stuck"
						 },

	"stiffenned":         {"word":    "stiffenned",
						 "replacement":       "stiffened"
						 },

	"stired":         {"word":    "stired",
						 "replacement":       "stirred"
						 },

	"stoled":         {"word":    "stoled",
						 "replacement":       "stole"
						 },

	"stoopped":         {"word":    "stoopped",
						 "replacement":       "stooped"
						 },

	"stoped":         {"word":    "stoped",
						 "replacement":       "stopped"
						 },

	"stowwed":         {"word":    "stowwed",
						 "replacement":       "stowed"
						 },

	"straied":         {"word":    "straied",
						 "replacement":       "strayed"
						 },

	"strainned":         {"word":    "strainned",
						 "replacement":       "strained"
						 },

	"streammed":         {"word":    "streammed",
						 "replacement":       "streamed"
						 },

	"strengthenned":         {"word":    "strengthenned",
						 "replacement":       "strengthened"
						 },

	"strewwed":         {"word":    "strewwed",
						 "replacement":       "strewed"
						 },

	"strided":         {"word":    "strided",
						 "replacement":       "strode"
						 },

	"striked":         {"word":    "striked",
						 "replacement":       "struck"
						 },

	"stucked":         {"word":    "stucked",
						 "replacement":       "stuck"
						 },

	"stuned":         {"word":    "stuned",
						 "replacement":       "stunned"
						 },

	"submited":         {"word":    "submited",
						 "replacement":       "submitted"
						 },

	"sufferred":         {"word":    "sufferred",
						 "replacement":       "suffered"
						 },

	"suitted":         {"word":    "suitted",
						 "replacement":       "suited"
						 },

	"summonned":         {"word":    "summonned",
						 "replacement":       "summoned"
						 },

	"sunged":         {"word":    "sunged",
						 "replacement":       "sang"
						 },

	"surrenderred":         {"word":    "surrenderred",
						 "replacement":       "surrendered"
						 },

	"surveied":         {"word":    "surveied",
						 "replacement":       "surveyed"
						 },

	"sustainned":         {"word":    "sustainned",
						 "replacement":       "sustained"
						 },

	"swaggerred":         {"word":    "swaggerred",
						 "replacement":       "swaggered"
						 },

	"swallowwed":         {"word":    "swallowwed",
						 "replacement":       "swallowed"
						 },

	"sweared":         {"word":    "sweared",
						 "replacement":       "swore"
						 },

	"sweeped":         {"word":    "sweeped",
						 "replacement":       "swept"
						 },

	"sweepped":         {"word":    "sweepped",
						 "replacement":       "swept"
						 },

	"sweetenned":         {"word":    "sweetenned",
						 "replacement":       "sweetened"
						 },

	"swepted":         {"word":    "swepted",
						 "replacement":       "swept"
						 },

	"swimed":         {"word":    "swimed",
						 "replacement":       "swam"
						 },

	"swinged":         {"word":    "swinged",
						 "replacement":       "swung"
						 },

	"tailled":         {"word":    "tailled",
						 "replacement":       "tailed"
						 },

	"taked":         {"word":    "taked",
						 "replacement":       "taken"
						 },

	"takened":         {"word":    "takened",
						 "replacement":       "taken"
						 },

	"taxxed":         {"word":    "taxxed",
						 "replacement":       "taxed"
						 },

	"teached":         {"word":    "teached",
						 "replacement":       "taught"
						 },

	"teared":         {"word":    "teared",
						 "replacement":       "torn"
						 },

	"tearred":         {"word":    "tearred",
						 "replacement":       "tore"
						 },

	"teemmed":         {"word":    "teemmed",
						 "replacement":       "teemed"
						 },

	"telled":         {"word":    "telled",
						 "replacement":       "told"
						 },

	"temperred":         {"word":    "temperred",
						 "replacement":       "tempered"
						 },

	"tenderred":         {"word":    "tenderred",
						 "replacement":       "tendered"
						 },

	"thickenned":         {"word":    "thickenned",
						 "replacement":       "thickened"
						 },

	"thinked":         {"word":    "thinked",
						 "replacement":       "thought"
						 },

	"thoughted":         {"word":    "thoughted",
						 "replacement":       "thought"
						 },

	"threatenned":         {"word":    "threatenned",
						 "replacement":       "threatened"
						 },

	"throwed":         {"word":    "throwed",
						 "replacement":       "threw"
						 },

	"throwwed":         {"word":    "throwwed",
						 "replacement":       "threw"
						 },

	"thunderred":         {"word":    "thunderred",
						 "replacement":       "thundered"
						 },

	"tightenned":         {"word":    "tightenned",
						 "replacement":       "tightened"
						 },

	"toied":         {"word":    "toied",
						 "replacement":       "toyed"
						 },

	"toped":         {"word":    "toped",
						 "replacement":       "topped"
						 },

	"totaled":         {"word":    "totaled",
						 "replacement":       "totalled"
						 },

	"towwed":         {"word":    "towwed",
						 "replacement":       "towed"
						 },

	"trailled":         {"word":    "trailled",
						 "replacement":       "trailed"
						 },

	"trainned":         {"word":    "trainned",
						 "replacement":       "trained"
						 },

	"transfered":         {"word":    "transfered",
						 "replacement":       "transferred"
						 },

	"transmited":         {"word":    "transmited",
						 "replacement":       "transmitted"
						 },

	"traped":         {"word":    "traped",
						 "replacement":       "trapped"
						 },

	"traveled":         {"word":    "traveled",
						 "replacement":       "travelled"
						 },

	"travelers":         {"word":    "travelers",
						 "replacement":       "travellers"
						 },

	"treadded":         {"word":    "treadded",
						 "replacement":       "trod"
						 },

	"treaded":         {"word":    "treaded",
						 "replacement":       "trod"
						 },

	"treatted":         {"word":    "treatted",
						 "replacement":       "treated"
						 },

	"tremorred":         {"word":    "tremorred",
						 "replacement":       "tremored"
						 },

	"trimed":         {"word":    "trimed",
						 "replacement":       "trimmed"
						 },

	"triped":         {"word":    "triped",
						 "replacement":       "tripped"
						 },

	"troted":         {"word":    "troted",
						 "replacement":       "trotted"
						 },

	"tuged":         {"word":    "tuged",
						 "replacement":       "tugged"
						 },

	"typeseted":         {"word":    "typeseted",
						 "replacement":       "typeset"
						 },

	"unbosommed":         {"word":    "unbosommed",
						 "replacement":       "unbosomed"
						 },

	"unbrokened":         {"word":    "unbrokened",
						 "replacement":       "unbroken"
						 },

	"unbrokenned":         {"word":    "unbrokenned",
						 "replacement":       "unbroken"
						 },

	"uncoverred":         {"word":    "uncoverred",
						 "replacement":       "uncovered"
						 },

	"undergoed":         {"word":    "undergoed",
						 "replacement":       "underwent"
						 },

	"understanded":         {"word":    "understanded",
						 "replacement":       "understood"
						 },

	"understoodded":         {"word":    "understoodded",
						 "replacement":       "understood"
						 },

	"understooded":         {"word":    "understooded",
						 "replacement":       "understood"
						 },

	"undertaked":         {"word":    "undertaked",
						 "replacement":       "undertook"
						 },

	"unknowned":         {"word":    "unknowned",
						 "replacement":       "unknown"
						 },

	"unpluged":         {"word":    "unpluged",
						 "replacement":       "unplugged"
						 },

	"unscrewwed":         {"word":    "unscrewwed",
						 "replacement":       "unscrewed"
						 },

	"untrammeled":         {"word":    "untrammeled",
						 "replacement":       "untrammelled"
						 },

	"unwraped":         {"word":    "unwraped",
						 "replacement":       "unwrapped"
						 },

	"upholded":         {"word":    "upholded",
						 "replacement":       "upheld"
						 },

	"uprootted":         {"word":    "uprootted",
						 "replacement":       "uprooted"
						 },

	"upseted":         {"word":    "upseted",
						 "replacement":       "upset"
						 },

	"upsetted":         {"word":    "upsetted",
						 "replacement":       "upset"
						 },

	"usherred":         {"word":    "usherred",
						 "replacement":       "ushered"
						 },

	"utterred":         {"word":    "utterred",
						 "replacement":       "uttered"
						 },

	"veilled":         {"word":    "veilled",
						 "replacement":       "veiled"
						 },

	"viewwed":         {"word":    "viewwed",
						 "replacement":       "viewed"
						 },

	"visitted":         {"word":    "visitted",
						 "replacement":       "visited"
						 },

	"volunteerred":         {"word":    "volunteerred",
						 "replacement":       "volunteered"
						 },

	"vomitted":         {"word":    "vomitted",
						 "replacement":       "vomited"
						 },

	"vowwed":         {"word":    "vowwed",
						 "replacement":       "vowed"
						 },

	"vowwed":         {"word":    "vowwed",
						 "replacement":       "vowed"
						 },

	"wailled":         {"word":    "wailled",
						 "replacement":       "wailed"
						 },

	"waitted":         {"word":    "waitted",
						 "replacement":       "waited"
						 },

	"wallowwed":         {"word":    "wallowwed",
						 "replacement":       "wallowed"
						 },

	"wallpaperred":         {"word":    "wallpaperred",
						 "replacement":       "wallpapered"
						 },

	"wanderred":         {"word":    "wanderred",
						 "replacement":       "wandered"
						 },

	"waxxed":         {"word":    "waxxed",
						 "replacement":       "waxed"
						 },

	"weared":         {"word":    "weared",
						 "replacement":       "wore"
						 },

	"wearred":         {"word":    "wearred",
						 "replacement":       "wore"
						 },

	"weatherred":         {"word":    "weatherred",
						 "replacement":       "weathered"
						 },

	"wheelled":         {"word":    "wheelled",
						 "replacement":       "wheeled"
						 },

	"whisperred":         {"word":    "whisperred",
						 "replacement":       "whispered"
						 },

	"widenned":         {"word":    "widenned",
						 "replacement":       "widened"
						 },

	"winnowwed":         {"word":    "winnowwed",
						 "replacement":       "winnowed"
						 },

	"withdrawed":         {"word":    "withdrawed",
						 "replacement":       "withdrew"
						 },

	"withdrawwed":         {"word":    "withdrawwed",
						 "replacement":       "withdrew"
						 },

	"withholded":         {"word":    "withholded",
						 "replacement":       "withheld"
						 },

	"wonderred":         {"word":    "wonderred",
						 "replacement":       "wondered"
						 },

	"worned":         {"word":    "worned",
						 "replacement":       "worn"
						 },

	"worsenned":         {"word":    "worsenned",
						 "replacement":       "worsened"
						 },

	"worshiped":         {"word":    "worshiped",
						 "replacement":       "worshipped"
						 },

	"wraped":         {"word":    "wraped",
						 "replacement":       "wrapped"
						 },

	"writed":         {"word":    "writed",
						 "replacement":       "wrote"
						 },

	"writted":         {"word":    "writted",
						 "replacement":       "wrote"
						 },

    #-ing words

	"abeting":         {"word":    "abeting",
						 "replacement":       "abetting"
						 },

	"acquiting":         {"word":    "acquiting",
						 "replacement":       "acquitting"
						 },

	"ading":         {"word":    "ading",
						 "replacement":       "adding"
						 },

	"admiting":         {"word":    "admiting",
						 "replacement":       "admitting"
						 },

	"agreing":         {"word":    "agreing",
						 "replacement":       "agreeing"
						 },

	"approacing":         {"word":    "approacing",
						 "replacement":       "approaching"
						 },

	"avariciousing":         {"word":    "avariciousing",
						 "replacement":       "avaricious"
						 },

	"becomeing":         {"word":    "becomeing",
						 "replacement":       "becoming"
						 },

	"befiting":         {"word":    "befiting",
						 "replacement":       "befitting"
						 },

	"begeting":         {"word":    "begeting",
						 "replacement":       "begetting"
						 },

	"begiing":         {"word":    "begiing",
						 "replacement":       "beginning"
						 },

	"beging":         {"word":    "beging",
						 "replacement":       "begging"
						 },

	"begining":         {"word":    "begining",
						 "replacement":       "beginning"
						 },

	"beginnining":         {"word":    "beginnining",
						 "replacement":       "beginning"
						 },

	"beseting":         {"word":    "beseting",
						 "replacement":       "besetting"
						 },

	"bestiring":         {"word":    "bestiring",
						 "replacement":       "bestirring"
						 },

	"bing":         {"word":    "bing",
						 "replacement":       "being"
						 },

	"braging":         {"word":    "braging",
						 "replacement":       "bragging"
						 },

	"buding":         {"word":    "buding",
						 "replacement":       "budding"
						 },

	"bustleing":         {"word":    "bustleing",
						 "replacement":       "bustling"
						 },

	"canceling":         {"word":    "canceling",
						 "replacement":       "cancelling"
						 },

	"charing":         {"word":    "charing",
						 "replacement":       "charring"
						 },

	"chiping":         {"word":    "chiping",
						 "replacement":       "chipping"
						 },

	"choping":         {"word":    "choping",
						 "replacement":       "chopping"
						 },

	"claping":         {"word":    "claping",
						 "replacement":       "clapping"
						 },

	"cliping":         {"word":    "cliping",
						 "replacement":       "clipping"
						 },

	"cloging":         {"word":    "cloging",
						 "replacement":       "clogging"
						 },

	"commiting":         {"word":    "commiting",
						 "replacement":       "committing"
						 },

	"compeling":         {"word":    "compeling",
						 "replacement":       "compelling"
						 },

	"composeing":         {"word":    "composeing",
						 "replacement":       "composing"
						 },

	"confering":         {"word":    "confering",
						 "replacement":       "conferring"
						 },

	"consising":         {"word":    "consising",
						 "replacement":       "consisting"
						 },

	"controling":         {"word":    "controling",
						 "replacement":       "controlling"
						 },

	"croping":         {"word":    "croping",
						 "replacement":       "cropping"
						 },

	"cuting":         {"word":    "cuting",
						 "replacement":       "cutting"
						 },

	"dabing ":         {"word":    "dabing ",
						 "replacement":       "dabbing"
						 },

	"dazzleing":         {"word":    "dazzleing",
						 "replacement":       "dazzling"
						 },

	"deathing":         {"word":    "deathing",
						 "replacement":       "dying"
						 },

	"debaring":         {"word":    "debaring",
						 "replacement":       "debarring"
						 },

	"demuring":         {"word":    "demuring",
						 "replacement":       "demurring"
						 },

	"detering":         {"word":    "detering",
						 "replacement":       "deterring"
						 },

	"dieing":         {"word":    "dieing",
						 "replacement":       "dying"
						 },

	"diing":         {"word":    "diing",
						 "replacement":       "dying"
						 },

	"diping":         {"word":    "diping",
						 "replacement":       "dipping"
						 },

	"direcing":         {"word":    "direcing",
						 "replacement":       "directing"
						 },

	"disagreing":         {"word":    "disagreing",
						 "replacement":       "disagreeing"
						 },

	"disemboweling":         {"word":    "disemboweling",
						 "replacement":       "disembowelling"
						 },

	"disintering":         {"word":    "disintering",
						 "replacement":       "disinterring"
						 },

	"draging":         {"word":    "draging",
						 "replacement":       "dragging"
						 },

	"droopining":         {"word":    "droopining",
						 "replacement":       "drooping"
						 },

	"droping":         {"word":    "droping",
						 "replacement":       "dropping"
						 },

	"druming":         {"word":    "druming",
						 "replacement":       "drumming"
						 },

	"emiting":         {"word":    "emiting",
						 "replacement":       "emitting"
						 },

	"equaling":         {"word":    "equaling",
						 "replacement":       "equalling"
						 },

	"equiping":         {"word":    "equiping",
						 "replacement":       "equipping"
						 },

	"eveing":         {"word":    "eveing",
						 "replacement":       "evening"
						 },

	"evenining":         {"word":    "evenining",
						 "replacement":       "evening"
						 },

	"examineing":         {"word":    "examineing",
						 "replacement":       "examining"
						 },

	"exceling":         {"word":    "exceling",
						 "replacement":       "excelling"
						 },

	"eying":         {"word":    "eying",
						 "replacement":       "eyeing"
						 },

	"fancys":         {"word":    "fancys",
						 "replacement":       "fancies"
						 },

	"faning":         {"word":    "faning",
						 "replacement":       "fanning"
						 },

	"feeing":         {"word":    "feeing",
						 "replacement":       "feeding"
						 },

	"fiting":         {"word":    "fiting",
						 "replacement":       "fitting"
						 },

	"flaping":         {"word":    "flaping",
						 "replacement":       "flapping"
						 },

	"fleing":         {"word":    "fleing",
						 "replacement":       "fleeing"
						 },

	"flesing":         {"word":    "flesing",
						 "replacement":       "fleshing"
						 },

	"fliping":         {"word":    "fliping",
						 "replacement":       "flipping"
						 },

	"fliting":         {"word":    "fliting",
						 "replacement":       "flitting"
						 },

	"floging":         {"word":    "floging",
						 "replacement":       "flogging"
						 },

	"forbiding":         {"word":    "forbiding",
						 "replacement":       "forbidding"
						 },

	"forceing":         {"word":    "forceing",
						 "replacement":       "forcing"
						 },

	"forgeting":         {"word":    "forgeting",
						 "replacement":       "forgetting"
						 },

	"formating":         {"word":    "formating",
						 "replacement":       "formatting"
						 },

	"frameing":         {"word":    "frameing",
						 "replacement":       "framing"
						 },

	"freing":         {"word":    "freing",
						 "replacement":       "freeing"
						 },

	"freting":         {"word":    "freting",
						 "replacement":       "fretting"
						 },

	"frolicing":         {"word":    "frolicing",
						 "replacement":       "frolicking"
						 },

	"furnishining":         {"word":    "furnishining",
						 "replacement":       "furnishing"
						 },

	"gaging":         {"word":    "gaging",
						 "replacement":       "gagging"
						 },

	"geting":         {"word":    "geting",
						 "replacement":       "getting"
						 },

	"giveing":         {"word":    "giveing",
						 "replacement":       "giving"
						 },

	"glanceing":         {"word":    "glanceing",
						 "replacement":       "glancing"
						 },

	"grabing":         {"word":    "grabing",
						 "replacement":       "grabbing"
						 },

	"grining":         {"word":    "grining",
						 "replacement":       "grinning"
						 },

	"groing":         {"word":    "groing",
						 "replacement":       "growing"
						 },

	"growthing":         {"word":    "growthing",
						 "replacement":       "growing"
						 },

	"guaranteing":         {"word":    "guaranteing",
						 "replacement":       "guaranteeing"
						 },

	"hasteing":         {"word":    "hasteing",
						 "replacement":       "hastening"
						 },

	"hiting":         {"word":    "hiting",
						 "replacement":       "hitting"
						 },

	"hoveing":         {"word":    "hoveing",
						 "replacement":       "hovering"
						 },

	"howevering":         {"word":    "howevering",
						 "replacement":       "however"
						 },

	"huging":         {"word":    "huging",
						 "replacement":       "hugging"
						 },

	"huming":         {"word":    "huming",
						 "replacement":       "humming"
						 },

	"imagineing":         {"word":    "imagineing",
						 "replacement":       "imagining"
						 },

	"impeling":         {"word":    "impeling",
						 "replacement":       "impelling"
						 },

	"inhaleing":         {"word":    "inhaleing",
						 "replacement":       "inhaling"
						 },

	"interpretationing":         {"word":    "interpretationing",
						 "replacement":       "interpreting"
						 },

	"involveing":         {"word":    "involveing",
						 "replacement":       "involving"
						 },

	"jabing":         {"word":    "jabing",
						 "replacement":       "jabbing"
						 },

	"jaming":         {"word":    "jaming",
						 "replacement":       "jamming"
						 },

	"jingleing":         {"word":    "jingleing",
						 "replacement":       "jingling"
						 },

	"joging":         {"word":    "joging",
						 "replacement":       "jogging"
						 },

	"kiding":         {"word":    "kiding",
						 "replacement":       "kidding"
						 },

	"kniting":         {"word":    "kniting",
						 "replacement":       "knitting"
						 },

	"knowining":         {"word":    "knowining",
						 "replacement":       "knowing"
						 },

	"leaseing":         {"word":    "leaseing",
						 "replacement":       "leasing"
						 },

	"leing":         {"word":    "leing",
						 "replacement":       "letting"
						 },

	"leting":         {"word":    "leting",
						 "replacement":       "letting"
						 },

	"leveling":         {"word":    "leveling",
						 "replacement":       "levelling"
						 },

	"lieing":         {"word":    "lieing",
						 "replacement":       "lying"
						 },

	"liing":         {"word":    "liing",
						 "replacement":       "lying"
						 },

	"listeing":         {"word":    "listeing",
						 "replacement":       "listening"
						 },

	"lodgeing":         {"word":    "lodgeing",
						 "replacement":       "lodging"
						 },

	"looing":         {"word":    "looing",
						 "replacement":       "looking"
						 },

	"makeing":         {"word":    "makeing",
						 "replacement":       "making"
						 },

	"maping":         {"word":    "maping",
						 "replacement":       "mapping"
						 },

	"maring":         {"word":    "maring",
						 "replacement":       "marring"
						 },

	"marshaling":         {"word":    "marshaling",
						 "replacement":       "marshalling"
						 },

	"misplaceing":         {"word":    "misplaceing",
						 "replacement":       "misplacing"
						 },

	"modeling":         {"word":    "modeling",
						 "replacement":       "modelling"
						 },

	"moveing":         {"word":    "moveing",
						 "replacement":       "moving"
						 },

	"naging":         {"word":    "naging",
						 "replacement":       "nagging"
						 },

	"necessitateing":         {"word":    "necessitateing",
						 "replacement":       "necessitating"
						 },

	"neting":         {"word":    "neting",
						 "replacement":       "netting"
						 },

	"noding":         {"word":    "noding",
						 "replacement":       "nodding"
						 },

	"noteing":         {"word":    "noteing",
						 "replacement":       "noting"
						 },

	"obligeing":         {"word":    "obligeing",
						 "replacement":       "obliging"
						 },

	"occuring":         {"word":    "occuring",
						 "replacement":       "occurring"
						 },

	"organisming":         {"word":    "organisming",
						 "replacement":       "being"
						 },

	"outwiting":         {"word":    "outwiting",
						 "replacement":       "outwitting"
						 },

	"pauseing":         {"word":    "pauseing",
						 "replacement":       "pausing"
						 },

	"permiting":         {"word":    "permiting",
						 "replacement":       "permitting"
						 },

	"piting":         {"word":    "piting",
						 "replacement":       "pitting"
						 },

	"placeing":         {"word":    "placeing",
						 "replacement":       "placing"
						 },

	"plaing":         {"word":    "plaing",
						 "replacement":       "playing"
						 },

	"ploting":         {"word":    "ploting",
						 "replacement":       "plotting"
						 },

	"prefering":         {"word":    "prefering",
						 "replacement":       "preferring"
						 },

	"protesing":         {"word":    "protesing",
						 "replacement":       "protesting"
						 },

	"pursuiting":         {"word":    "pursuiting",
						 "replacement":       "pursuing"
						 },

	"pusing":         {"word":    "pusing",
						 "replacement":       "pushing"
						 },

	"puting":         {"word":    "puting",
						 "replacement":       "putting"
						 },

	"quarreling":         {"word":    "quarreling",
						 "replacement":       "quarrelling"
						 },

	"raceing":         {"word":    "raceing",
						 "replacement":       "racing"
						 },

	"raiseing":         {"word":    "raiseing",
						 "replacement":       "raising"
						 },

	"rebeling":         {"word":    "rebeling",
						 "replacement":       "rebelling"
						 },

	"recuring":         {"word":    "recuring",
						 "replacement":       "recurring"
						 },

	"refering":         {"word":    "refering",
						 "replacement":       "referring"
						 },

	"regreting":         {"word":    "regreting",
						 "replacement":       "regretting"
						 },

	"repeaing":         {"word":    "repeaing",
						 "replacement":       "repeating"
						 },

	"repeling":         {"word":    "repeling",
						 "replacement":       "repelling"
						 },

	"riging":         {"word":    "riging",
						 "replacement":       "rigging"
						 },

	"rubing":         {"word":    "rubing",
						 "replacement":       "rubbing"
						 },

	"ruing":         {"word":    "ruing",
						 "replacement":       "running"
						 },

	"runing":         {"word":    "runing",
						 "replacement":       "running"
						 },

	"saging":         {"word":    "saging",
						 "replacement":       "sagging"
						 },

	"scaning":         {"word":    "scaning",
						 "replacement":       "scanning"
						 },

	"scrubing":         {"word":    "scrubing",
						 "replacement":       "scrubbing"
						 },

	"seing":         {"word":    "seing",
						 "replacement":       "seeing"
						 },

	"separateing":         {"word":    "separateing",
						 "replacement":       "separating"
						 },

	"seting":         {"word":    "seting",
						 "replacement":       "setting"
						 },

	"sheding":         {"word":    "sheding",
						 "replacement":       "shedding"
						 },

	"shiping":         {"word":    "shiping",
						 "replacement":       "shipping"
						 },

	"shoping":         {"word":    "shoping",
						 "replacement":       "shopping"
						 },

	"shoveling":         {"word":    "shoveling",
						 "replacement":       "shovelling"
						 },

	"shriveling":         {"word":    "shriveling",
						 "replacement":       "shrivelling"
						 },

	"shruging":         {"word":    "shruging",
						 "replacement":       "shrugging"
						 },

	"shuddeing":         {"word":    "shuddeing",
						 "replacement":       "shuddering"
						 },

	"shuning":         {"word":    "shuning",
						 "replacement":       "shunning"
						 },

	"sittining":         {"word":    "sittining",
						 "replacement":       "sitting"
						 },

	"skiding":         {"word":    "skiding",
						 "replacement":       "skidding"
						 },

	"skiming":         {"word":    "skiming",
						 "replacement":       "skimming"
						 },

	"skining":         {"word":    "skining",
						 "replacement":       "skinning"
						 },

	"skiping":         {"word":    "skiping",
						 "replacement":       "skipping"
						 },

	"slaping":         {"word":    "slaping",
						 "replacement":       "slapping"
						 },

	"sliping":         {"word":    "sliping",
						 "replacement":       "slipping"
						 },

	"slitheing":         {"word":    "slitheing",
						 "replacement":       "slithering"
						 },

	"sloging":         {"word":    "sloging",
						 "replacement":       "slogging"
						 },

	"smileing":         {"word":    "smileing",
						 "replacement":       "smiling"
						 },

	"snaping":         {"word":    "snaping",
						 "replacement":       "snapping"
						 },

	"sniveling":         {"word":    "sniveling",
						 "replacement":       "snivelling"
						 },

	"snoged":         {"word":    "snoged",
						 "replacement":       "snogged"
						 },

	"snoging":         {"word":    "snoging",
						 "replacement":       "snogging"
						 },

	"sobing":         {"word":    "sobing",
						 "replacement":       "sobbing"
						 },

	"spining":         {"word":    "spining",
						 "replacement":       "spinning"
						 },

	"spoting":         {"word":    "spoting",
						 "replacement":       "spotting"
						 },

	"spuring":         {"word":    "spuring",
						 "replacement":       "spurring"
						 },

	"squareing":         {"word":    "squareing",
						 "replacement":       "squaring"
						 },

	"squating":         {"word":    "squating",
						 "replacement":       "squatting"
						 },

	"staning":         {"word":    "staning",
						 "replacement":       "standing"
						 },

	"steing":         {"word":    "steing",
						 "replacement":       "stepping"
						 },

	"steming":         {"word":    "steming",
						 "replacement":       "stemming"
						 },

	"steping":         {"word":    "steping",
						 "replacement":       "stepping"
						 },

	"stimulateing":         {"word":    "stimulateing",
						 "replacement":       "stimulating"
						 },

	"stiring":         {"word":    "stiring",
						 "replacement":       "stirring"
						 },

	"stoping":         {"word":    "stoping",
						 "replacement":       "stopping"
						 },

	"straping":         {"word":    "straping",
						 "replacement":       "strapping"
						 },

	"strideing":         {"word":    "strideing",
						 "replacement":       "striding"
						 },

	"submiting":         {"word":    "submiting",
						 "replacement":       "submitting"
						 },

	"suning":         {"word":    "suning",
						 "replacement":       "sunning"
						 },

	"swiming":         {"word":    "swiming",
						 "replacement":       "swimming"
						 },

	"taging":         {"word":    "taging",
						 "replacement":       "tagging"
						 },

	"takeing":         {"word":    "takeing",
						 "replacement":       "taking"
						 },

	"throbing":         {"word":    "throbing",
						 "replacement":       "throbbing"
						 },

	"tiing":         {"word":    "tiing",
						 "replacement":       "tying"
						 },

	"toping":         {"word":    "toping",
						 "replacement":       "topping"
						 },

	"totaling":         {"word":    "totaling",
						 "replacement":       "totalling"
						 },

	"totaling":         {"word":    "totaling",
						 "replacement":       "totalling"
						 },

	"transfering":         {"word":    "transfering",
						 "replacement":       "transferring"
						 },

	"transfiing":         {"word":    "transfiing",
						 "replacement":       "transfixing"
						 },

	"traping":         {"word":    "traping",
						 "replacement":       "trapping"
						 },

	"traveling":         {"word":    "traveling",
						 "replacement":       "travelling"
						 },

	"triing":         {"word":    "triing",
						 "replacement":       "tripping"
						 },

	"triming":         {"word":    "triming",
						 "replacement":       "trimming"
						 },

	"tring":         {"word":    "tring",
						 "replacement":       "trying"
						 },

	"triping":         {"word":    "triping",
						 "replacement":       "tripping"
						 },

	"troting":         {"word":    "troting",
						 "replacement":       "trotting"
						 },

	"tuging":         {"word":    "tuging",
						 "replacement":       "tugging"
						 },

	"typeseting":         {"word":    "typeseting",
						 "replacement":       "typesetting"
						 },

	"unwraping":         {"word":    "unwraping",
						 "replacement":       "unwrapping"
						 },

	"upseting":         {"word":    "upseting",
						 "replacement":       "upsetting"
						 },

	"valleies":         {"word":    "valleies",
						 "replacement":       "valleys"
						 },

	"weting":         {"word":    "weting",
						 "replacement":       "wetting"
						 },

	"wheting":         {"word":    "wheting",
						 "replacement":       "whetting"
						 },

	"whistleing":         {"word":    "whistleing",
						 "replacement":       "whistling"
						 },

	"wraping":         {"word":    "wraping",
						 "replacement":       "wrapping"
						 },

    #-incorrect plurals (and other -s/-es words) 

	"acknowledgments":         {"word":    "acknowledgments",
						 "replacement":       "acknowledgements"
						 },

	"affraies":         {"word":    "affraies",
						 "replacement":       "affrays"
						 },

	"aldermans":         {"word":    "aldermans",
						 "replacement":       "aldermen"
						 },

	"alleies":         {"word":    "alleies",
						 "replacement":       "alleys"
						 },

	"alloies":         {"word":    "alloies",
						 "replacement":       "alloys"
						 },

	"alouds":         {"word":    "alouds",
						 "replacement":       "aloud"
						 },

	"anguishs":         {"word":    "anguishs",
						 "replacement":       "anguishes"
						 },

	"annexs":         {"word":    "annexs",
						 "replacement":       "annexes"
						 },

	"annoies":         {"word":    "annoies",
						 "replacement":       "annoys"
						 },

	"approachs":         {"word":    "approachs",
						 "replacement":       "approaches"
						 },

	"archs":         {"word":    "archs",
						 "replacement":       "arches"
						 },

	"ashs":         {"word":    "ashs",
						 "replacement":       "ashes"
						 },

	"axs":         {"word":    "axs",
						 "replacement":       "axes"
						 },

	"bailifves":         {"word":    "bailifves",
						 "replacement":       "bailiffs"
						 },

	"banishs":         {"word":    "banishs",
						 "replacement":       "banishes"
						 },

	"batchs":         {"word":    "batchs",
						 "replacement":       "batches"
						 },

	"benchs":         {"word":    "benchs",
						 "replacement":       "benches"
						 },

	"birthdaies":         {"word":    "birthdaies",
						 "replacement":       "birthdays"
						 },

	"blemishs":         {"word":    "blemishs",
						 "replacement":       "blemishes"
						 },

	"blowtorchs":         {"word":    "blowtorchs",
						 "replacement":       "blowtorches"
						 },

	"blushs":         {"word":    "blushs",
						 "replacement":       "blushes"
						 },

	"boatmans":         {"word":    "boatmans",
						 "replacement":       "boatmen"
						 },

	"bogeymans":         {"word":    "bogeymans",
						 "replacement":       "bogeymen"
						 },

	"boies":         {"word":    "boies",
						 "replacement":       "boys"
						 },

	"boxs":         {"word":    "boxs",
						 "replacement":       "boxes"
						 },

	"branchs":         {"word":    "branchs",
						 "replacement":       "branches"
						 },

	"brandishs":         {"word":    "brandishs",
						 "replacement":       "brandishes"
						 },

	"breechs":         {"word":    "breechs",
						 "replacement":       "breeches"
						 },

	"broochs":         {"word":    "broochs",
						 "replacement":       "brooches"
						 },

	"brushs":         {"word":    "brushs",
						 "replacement":       "brushes"
						 },

	"buddys":         {"word":    "buddys",
						 "replacement":       "buddies"
						 },

	"buies":         {"word":    "buies",
						 "replacement":       "buys"
						 },

	"bunchs":         {"word":    "bunchs",
						 "replacement":       "bunches"
						 },

	"bushs":         {"word":    "bushs",
						 "replacement":       "bushes"
						 },

	"cattles":         {"word":    "cattles",
						 "replacement":       "cattle"
						 },

	"causewaies":         {"word":    "causewaies",
						 "replacement":       "causeways"
						 },

	"charwomans":         {"word":    "charwomans",
						 "replacement":       "charwomen"
						 },

	"childs":         {"word":    "childs",
						 "replacement":       "children"
						 },

	"chimneies":         {"word":    "chimneies",
						 "replacement":       "chimneys"
						 },

	"churchs":         {"word":    "churchs",
						 "replacement":       "churches"
						 },

	"citizenriess":         {"word":    "citizenriess",
						 "replacement":       "citizenries"
						 },

	"citizenrys":         {"word":    "citizenrys",
						 "replacement":       "citizenries"
						 },

	"clashs":         {"word":    "clashs",
						 "replacement":       "clashes"
						 },

	"cloies":         {"word":    "cloies",
						 "replacement":       "cloys"
						 },

	"coachmans":         {"word":    "coachmans",
						 "replacement":       "coachmen"
						 },

	"coachs":         {"word":    "coachs",
						 "replacement":       "coaches"
						 },

	"congressmans":         {"word":    "congressmans",
						 "replacement":       "congressmen"
						 },

	"countrymans":         {"word":    "countrymans",
						 "replacement":       "countrymen"
						 },

	"craftsmans":         {"word":    "craftsmans",
						 "replacement":       "craftsmen"
						 },

	"crashs":         {"word":    "crashs",
						 "replacement":       "crashes"
						 },

	"crotchs":         {"word":    "crotchs",
						 "replacement":       "crotches"
						 },

	"crouchs":         {"word":    "crouchs",
						 "replacement":       "crouches"
						 },

	"crutchs":         {"word":    "crutchs",
						 "replacement":       "crutches"
						 },

	"cryings":         {"word":    "cryings",
						 "replacement":       "crying"
						 },

	"cufves":         {"word":    "cufves",
						 "replacement":       "cuffs"
						 },

	"daies":         {"word":    "daies",
						 "replacement":       "days"
						 },

	"dashs":         {"word":    "dashs",
						 "replacement":       "dashes"
						 },

	"delaies":         {"word":    "delaies",
						 "replacement":       "delays"
						 },

	"destroies":         {"word":    "destroies",
						 "replacement":       "destroys"
						 },

	"dishs":         {"word":    "dishs",
						 "replacement":       "dishes"
						 },

	"dismaies":         {"word":    "dismaies",
						 "replacement":       "dismays"
						 },

	"displaies":         {"word":    "displaies",
						 "replacement":       "displays"
						 },

	"ditchs":         {"word":    "ditchs",
						 "replacement":       "ditches"
						 },

	"dominos":         {"word":    "dominos",
						 "replacement":       "dominoes"
						 },

	"donkeies":         {"word":    "donkeies",
						 "replacement":       "donkeys"
						 },

	"doorwaies":         {"word":    "doorwaies",
						 "replacement":       "doorways"
						 },

	"draftsmans":         {"word":    "draftsmans",
						 "replacement":       "draftsmen"
						 },

	"draies":         {"word":    "draies",
						 "replacement":       "drays"
						 },

	"echos":         {"word":    "echos",
						 "replacement":       "echoes"
						 },

	"englishmans":         {"word":    "englishmans",
						 "replacement":       "englishmen"
						 },

	"enmeshs":         {"word":    "enmeshs",
						 "replacement":       "enmeshes"
						 },

	"establishs":         {"word":    "establishs",
						 "replacement":       "establishes"
						 },

	"eyelashs":         {"word":    "eyelashs",
						 "replacement":       "eyelashes"
						 },

	"fetchs":         {"word":    "fetchs",
						 "replacement":       "fetches"
						 },

	"firemans":         {"word":    "firemans",
						 "replacement":       "firemen"
						 },

	"fishermans":         {"word":    "fishermans",
						 "replacement":       "fishermen"
						 },

	"fixs":         {"word":    "fixs",
						 "replacement":       "fixes"
						 },

	"flagstafves":         {"word":    "flagstafves",
						 "replacement":       "flagstaffs"
						 },

	"flashs":         {"word":    "flashs",
						 "replacement":       "flashes"
						 },

	"flexs":         {"word":    "flexs",
						 "replacement":       "flexes"
						 },

	"flourishs":         {"word":    "flourishs",
						 "replacement":       "flourishes"
						 },

	"flushs":         {"word":    "flushs",
						 "replacement":       "flushes"
						 },

	"footmans":         {"word":    "footmans",
						 "replacement":       "footmen"
						 },

	"foots":         {"word":    "foots",
						 "replacement":       "feet"
						 },

	"foxs":         {"word":    "foxs",
						 "replacement":       "foxes"
						 },

	"gaies":         {"word":    "gaies",
						 "replacement":       "gays"
						 },

	"galleies":         {"word":    "galleies",
						 "replacement":       "galleys"
						 },

	"gatewaies":         {"word":    "gatewaies",
						 "replacement":       "gateways"
						 },

	"gentlemans":         {"word":    "gentlemans",
						 "replacement":       "gentlemen"
						 },

	"gos":         {"word":    "gos",
						 "replacement":       "goes"
						 },

	"graies":         {"word":    "graies",
						 "replacement":       "grays"
						 },

	"grandchilds":         {"word":    "grandchilds",
						 "replacement":       "grandchildren"
						 },

	"greies":         {"word":    "greies",
						 "replacement":       "greys"
						 },

	"gunmans":         {"word":    "gunmans",
						 "replacement":       "gunmen"
						 },

	"handcufves":         {"word":    "handcufves",
						 "replacement":       "handcuffs"
						 },

	"handkerchieves":         {"word":    "handkerchieves",
						 "replacement":       "handkerchiefs"
						 },

	"haunchs":         {"word":    "haunchs",
						 "replacement":       "haunches"
						 },

	"headmans":         {"word":    "headmans",
						 "replacement":       "headmen"
						 },

	"headwaies":         {"word":    "headwaies",
						 "replacement":       "headways"
						 },

	"hemorrhoids":         {"word":    "hemorrhoids",
						 "replacement":       "haemorrhoids"
						 },

	"heros":         {"word":    "heros",
						 "replacement":       "heroes"
						 },

	"hexs":         {"word":    "hexs",
						 "replacement":       "hexes"
						 },

	"highwaies":         {"word":    "highwaies",
						 "replacement":       "highways"
						 },

	"holidaies":         {"word":    "holidaies",
						 "replacement":       "holidays"
						 },

	"horsemans":         {"word":    "horsemans",
						 "replacement":       "horsemen"
						 },

	"housewifes":         {"word":    "housewifes",
						 "replacement":       "housewives"
						 },

	"hufves":         {"word":    "hufves",
						 "replacement":       "huffs"
						 },

	"hutchs":         {"word":    "hutchs",
						 "replacement":       "hutches"
						 },

	"inchs":         {"word":    "inchs",
						 "replacement":       "inches"
						 },

	"jealousys":         {"word":    "jealousys",
						 "replacement":       "jealousies"
						 },

	"joies":         {"word":    "joies",
						 "replacement":       "joys"
						 },

	"journeies":         {"word":    "journeies",
						 "replacement":       "journeys"
						 },

	"keies":         {"word":    "keies",
						 "replacement":       "keys"
						 },

	"kidneies":         {"word":    "kidneies",
						 "replacement":       "kidneys"
						 },

	"knifes":         {"word":    "knifes",
						 "replacement":       "knives"
						 },

	"lashs":         {"word":    "lashs",
						 "replacement":       "lashes"
						 },

	"leachs":         {"word":    "leachs",
						 "replacement":       "leaches"
						 },

	"leechs":         {"word":    "leechs",
						 "replacement":       "leeches"
						 },

	"lifes":         {"word":    "lifes",
						 "replacement":       "lives"
						 },

	"mailmans":         {"word":    "mailmans",
						 "replacement":       "mailmen"
						 },

	"mans":         {"word":    "mans",
						 "replacement":       "men"
						 },

	"marchs":         {"word":    "marchs",
						 "replacement":       "marches"
						 },

	"marshs":         {"word":    "marshs",
						 "replacement":       "marshes"
						 },

	"matchs":         {"word":    "matchs",
						 "replacement":       "matches"
						 },

	"mermans":         {"word":    "mermans",
						 "replacement":       "mermen"
						 },

	"midshipmans":         {"word":    "midshipmans",
						 "replacement":       "midshipmen"
						 },

	"mixs":         {"word":    "mixs",
						 "replacement":       "mixes"
						 },

	"mufves":         {"word":    "mufves",
						 "replacement":       "muffs"
						 },

	"obeies":         {"word":    "obeies",
						 "replacement":       "obeys"
						 },

	"paies":         {"word":    "paies",
						 "replacement":       "pays"
						 },

	"partys":         {"word":    "partys",
						 "replacement":       "parties"
						 },

	"passkeies":         {"word":    "passkeies",
						 "replacement":       "passkeys"
						 },

	"patchs":         {"word":    "patchs",
						 "replacement":       "patches"
						 },

	"peachs":         {"word":    "peachs",
						 "replacement":       "peaches"
						 },

	"perplexs":         {"word":    "perplexs",
						 "replacement":       "perplexes"
						 },

	"pinchs":         {"word":    "pinchs",
						 "replacement":       "pinches"
						 },

	"plaies":         {"word":    "plaies",
						 "replacement":       "plays"
						 },

	"plats":         {"word":    "plats",
						 "replacement":       "plates"
						 },

	"ploies":         {"word":    "ploies",
						 "replacement":       "ploys"
						 },

	"policemans":         {"word":    "policemans",
						 "replacement":       "policemen"
						 },

	"polishs":         {"word":    "polishs",
						 "replacement":       "polishes"
						 },

	"porchs":         {"word":    "porchs",
						 "replacement":       "porches"
						 },

	"portraies":         {"word":    "portraies",
						 "replacement":       "portrays"
						 },

	"potatos":         {"word":    "potatos",
						 "replacement":       "potatoes"
						 },

	"pouchs":         {"word":    "pouchs",
						 "replacement":       "pouches"
						 },

	"poultrymans":         {"word":    "poultrymans",
						 "replacement":       "poultrymen"
						 },

	"preies":         {"word":    "preies",
						 "replacement":       "preys"
						 },

	"pufves":         {"word":    "pufves",
						 "replacement":       "puffs"
						 },

	"pushs":         {"word":    "pushs",
						 "replacement":       "pushes"
						 },

	"quaies":         {"word":    "quaies",
						 "replacement":       "quays"
						 },

	"raies":         {"word":    "raies",
						 "replacement":       "rays"
						 },

	"reachs":         {"word":    "reachs",
						 "replacement":       "reaches"
						 },

	"rebufves":         {"word":    "rebufves",
						 "replacement":       "rebuffs"
						 },

	"reproachs":         {"word":    "reproachs",
						 "replacement":       "reproaches"
						 },

	"revelers":         {"word":    "revelers",
						 "replacement":       "revellers"
						 },

	"rubbishs":         {"word":    "rubbishs",
						 "replacement":       "rubbishes"
						 },

	"runawaies":         {"word":    "runawaies",
						 "replacement":       "runaways"
						 },

	"rushs":         {"word":    "rushs",
						 "replacement":       "rushes"
						 },

	"sandwichs":         {"word":    "sandwichs",
						 "replacement":       "sandwiches"
						 },

	"saturdaies":         {"word":    "saturdaies",
						 "replacement":       "saturdays"
						 },

	"schoolchilds":         {"word":    "schoolchilds",
						 "replacement":       "schoolchildren"
						 },

	"scratchs":         {"word":    "scratchs",
						 "replacement":       "scratches"
						 },

	"screechs":         {"word":    "screechs",
						 "replacement":       "screeches"
						 },

	"seamans":         {"word":    "seamans",
						 "replacement":       "seamen"
						 },

	"searchs":         {"word":    "searchs",
						 "replacement":       "searches"
						 },

	"servicemans":         {"word":    "servicemans",
						 "replacement":       "servicemen"
						 },

	"sexs":         {"word":    "sexs",
						 "replacement":       "sexes"
						 },

	"sherifves":         {"word":    "sherifves",
						 "replacement":       "sheriffs"
						 },

	"sidewaies":         {"word":    "sidewaies",
						 "replacement":       "sideways"
						 },

	"siping":         {"word":    "siping",
						 "replacement":       "sipping"
						 },

	"sketchs":         {"word":    "sketchs",
						 "replacement":       "sketches"
						 },

	"skirmishs":         {"word":    "skirmishs",
						 "replacement":       "skirmishes"
						 },

	"smashs":         {"word":    "smashs",
						 "replacement":       "smashes"
						 },

	"smoochs":         {"word":    "smoochs",
						 "replacement":       "smooches"
						 },

	"snatchs":         {"word":    "snatchs",
						 "replacement":       "snatches"
						 },

	"snifves":         {"word":    "snifves",
						 "replacement":       "sniffs"
						 },

	"soundboxs":         {"word":    "soundboxs",
						 "replacement":       "soundboxes"
						 },

	"speechs":         {"word":    "speechs",
						 "replacement":       "speeches"
						 },

	"stablemans":         {"word":    "stablemans",
						 "replacement":       "stablemen"
						 },

	"stafves":         {"word":    "stafves",
						 "replacement":       "staffs"
						 },

	"stagecoachs":         {"word":    "stagecoachs",
						 "replacement":       "stagecoaches"
						 },

	"staies":         {"word":    "staies",
						 "replacement":       "stays"
						 },

	"stairwaies":         {"word":    "stairwaies",
						 "replacement":       "stairways"
						 },

	"statesmans":         {"word":    "statesmans",
						 "replacement":       "statesmen"
						 },

	"stitchs":         {"word":    "stitchs",
						 "replacement":       "stitches"
						 },

	"stretchs":         {"word":    "stretchs",
						 "replacement":       "stretches"
						 },

	"stufves":         {"word":    "stufves",
						 "replacement":       "stuffs"
						 },

	"sundaies":         {"word":    "sundaies",
						 "replacement":       "sundays"
						 },

	"surveies":         {"word":    "surveies",
						 "replacement":       "surveys"
						 },

	"switchs":         {"word":    "switchs",
						 "replacement":       "switches"
						 },

	"taxs":         {"word":    "taxs",
						 "replacement":       "taxes"
						 },

	"teachs":         {"word":    "teachs",
						 "replacement":       "teaches"
						 },

	"technicalitys":         {"word":    "technicalitys",
						 "replacement":       "technicalities"
						 },

	"thoraxs":         {"word":    "thoraxs",
						 "replacement":       "thoraxes"
						 },

	"toies":         {"word":    "toies",
						 "replacement":       "toys"
						 },

	"tooths":         {"word":    "tooths",
						 "replacement":       "teeth"
						 },

	"torchs":         {"word":    "torchs",
						 "replacement":       "torches"
						 },

	"touchs":         {"word":    "touchs",
						 "replacement":       "touches"
						 },

	"traies":         {"word":    "traies",
						 "replacement":       "trays"
						 },

	"trashs":         {"word":    "trashs",
						 "replacement":       "trashes"
						 },

	"trenchs":         {"word":    "trenchs",
						 "replacement":       "trenches"
						 },

	"turkeies":         {"word":    "turkeies",
						 "replacement":       "turkeys"
						 },

	"twitchs":         {"word":    "twitchs",
						 "replacement":       "twitches"
						 },

	"twitchs":         {"word":    "twitchs",
						 "replacement":       "twitches"
						 },

	"vanishs":         {"word":    "vanishs",
						 "replacement":       "vanishes"
						 },

	"varnishs":         {"word":    "varnishs",
						 "replacement":       "varnishes"
						 },

	"waies":         {"word":    "waies",
						 "replacement":       "ways"
						 },

	"watchmans":         {"word":    "watchmans",
						 "replacement":       "watchmen"
						 },

	"watchs":         {"word":    "watchs",
						 "replacement":       "watches"
						 },

	"whifves":         {"word":    "whifves",
						 "replacement":       "whiffs"
						 },

	"wifes":         {"word":    "wifes",
						 "replacement":       "wives"
						 },

	"wishs":         {"word":    "wishs",
						 "replacement":       "wishes"
						 },

	"witchs":         {"word":    "witchs",
						 "replacement":       "witches"
						 },

	"womans":         {"word":    "womans",
						 "replacement":       "women"
						 },

	"workmans":         {"word":    "workmans",
						 "replacement":       "workmen"
						 },

	"worshipers":         {"word":    "worshipers",
						 "replacement":       "worshippers"
						 },

	"wretchs":         {"word":    "wretchs",
						 "replacement":       "wretches"
						 },

	"yeomans":         {"word":    "yeomans",
						 "replacement":       "yeomen"
						 },

	"yesterdaies":         {"word":    "yesterdaies",
						 "replacement":       "yesterdays"
						 },

    #US spellings -> UK spellings

	"amphitheater":         {"word":    "amphitheater",
						 "replacement":       "amphitheatre"
						 },

	"amphitheaters":         {"word":    "amphitheaters",
						 "replacement":       "amphitheatres"
						 },

	"analyze":         {"word":    "analyze",
						 "replacement":       "analyse"
						 },

	"analyzed":         {"word":    "analyzed",
						 "replacement":       "analysed"
						 },

	"analyzes":         {"word":    "analyzes",
						 "replacement":       "analyses"
						 },

	"analyzing":         {"word":    "analyzing",
						 "replacement":       "analysing"
						 },

	"arbor":         {"word":    "arbor",
						 "replacement":       "arbour"
						 },

	"arbors":         {"word":    "arbors",
						 "replacement":       "arbours"
						 },

	"ardor":         {"word":    "ardor",
						 "replacement":       "ardour"
						 },

	"ardors":         {"word":    "ardors",
						 "replacement":       "ardours"
						 },

	"behavior":         {"word":    "behavior",
						 "replacement":       "behaviour"
						 },

	"behaviors":         {"word":    "behaviors",
						 "replacement":       "behaviours"
						 },

	"candor":         {"word":    "candor",
						 "replacement":       "candour"
						 },

	"center":         {"word":    "center",
						 "replacement":       "centre"
						 },

	"centered":         {"word":    "centered",
						 "replacement":       "centred"
						 },

	"centers":         {"word":    "centers",
						 "replacement":       "centres"
						 },

	"checkered":         {"word":    "checkered",
						 "replacement":       "chequered"
						 },

	"chili":         {"word":    "chili",
						 "replacement":       "chilli"
						 },

	"clamor":         {"word":    "clamor",
						 "replacement":       "clamour"
						 },

	"clamoring":         {"word":    "clamoring",
						 "replacement":       "clamouring"
						 },

	"color":         {"word":    "color",
						 "replacement":       "colour"
						 },

	"colored":         {"word":    "colored",
						 "replacement":       "coloured"
						 },

	"coloring":         {"word":    "coloring",
						 "replacement":       "colouring"
						 },

	"colorred":         {"word":    "colorred",
						 "replacement":       "coloured"
						 },

	"colors":         {"word":    "colors",
						 "replacement":       "colours"
						 },

	"defense":         {"word":    "defense",
						 "replacement":       "defence"
						 },

	"defenses":         {"word":    "defenses",
						 "replacement":       "defences"
						 },

	"demeanor":         {"word":    "demeanor",
						 "replacement":       "demeanour"
						 },

	"discolor":         {"word":    "discolor",
						 "replacement":       "discolour"
						 },

	"discolored":         {"word":    "discolored",
						 "replacement":       "discoloured"
						 },

	"discolorred":         {"word":    "discolorred",
						 "replacement":       "discoloured"
						 },

	"discolors":         {"word":    "discolors",
						 "replacement":       "discolours"
						 },

	"disfavor":         {"word":    "disfavor",
						 "replacement":       "disfavour"
						 },

	"disfavor":         {"word":    "disfavor",
						 "replacement":       "disfavour"
						 },

	"disfavors":         {"word":    "disfavors",
						 "replacement":       "disfavours"
						 },

	"dishonor":         {"word":    "dishonor",
						 "replacement":       "dishonour"
						 },

	"dishonored":         {"word":    "dishonored",
						 "replacement":       "dishonoured"
						 },

	"dishonoring":         {"word":    "dishonoring",
						 "replacement":       "dishonouring"
						 },

	"dishonorred":         {"word":    "dishonorred",
						 "replacement":       "dishonoured"
						 },

	"dishonors":         {"word":    "dishonors",
						 "replacement":       "dishonours"
						 },

	"endeavor":         {"word":    "endeavor",
						 "replacement":       "endeavour"
						 },

	"endeavored":         {"word":    "endeavored",
						 "replacement":       "endeavoured"
						 },

	"endeavoring":         {"word":    "endeavoring",
						 "replacement":       "endeavouring"
						 },

	"endeavorred":         {"word":    "endeavorred",
						 "replacement":       "endeavoured"
						 },

	"endeavors":         {"word":    "endeavors",
						 "replacement":       "endeavours"
						 },

	"epaulets":         {"word":    "epaulets",
						 "replacement":       "epaulettes"
						 },

	"favor":         {"word":    "favor",
						 "replacement":       "favour"
						 },

	"favorably":         {"word":    "favorably",
						 "replacement":       "favourably"
						 },

	"favored":         {"word":    "favored",
						 "replacement":       "favoured"
						 },

	"favoring":         {"word":    "favoring",
						 "replacement":       "favouring"
						 },

	"favorite":         {"word":    "favorite",
						 "replacement":       "favourite"
						 },

	"favorites":         {"word":    "favorites",
						 "replacement":       "favourites"
						 },

	"favorred":         {"word":    "favorred",
						 "replacement":       "favoured"
						 },

	"favors":         {"word":    "favors",
						 "replacement":       "favours"
						 },

	"flavor":         {"word":    "flavor",
						 "replacement":       "flavour"
						 },

	"harbor":         {"word":    "harbor",
						 "replacement":       "harbour"
						 },

	"harbored":         {"word":    "harbored",
						 "replacement":       "harboured"
						 },

	"harboring":         {"word":    "harboring",
						 "replacement":       "harbouring"
						 },

	"harborred":         {"word":    "harborred",
						 "replacement":       "harboured"
						 },

	"harbors":         {"word":    "harbors",
						 "replacement":       "harbours"
						 },

	"honor":         {"word":    "honor",
						 "replacement":       "honour"
						 },

	"honorable":         {"word":    "honorable",
						 "replacement":       "honourable"
						 },

	"honorably":         {"word":    "honorably",
						 "replacement":       "honourably"
						 },

	"honored":         {"word":    "honored",
						 "replacement":       "honoured"
						 },

	"honoring":         {"word":    "honoring",
						 "replacement":       "honouring"
						 },

	"honorred":         {"word":    "honorred",
						 "replacement":       "honoured"
						 },

	"honors":         {"word":    "honors",
						 "replacement":       "honours"
						 },

	"humor":         {"word":    "humor",
						 "replacement":       "humour"
						 },

	"humored":         {"word":    "humored",
						 "replacement":       "humoured"
						 },

	"humoring":         {"word":    "humoring",
						 "replacement":       "humouring"
						 },

	"humors":         {"word":    "humors",
						 "replacement":       "humours"
						 },

	"labor":         {"word":    "labor",
						 "replacement":       "labour"
						 },

	"labored":         {"word":    "labored",
						 "replacement":       "laboured"
						 },

	"laborer":         {"word":    "laborer",
						 "replacement":       "labourer"
						 },

	"laborers":         {"word":    "laborers",
						 "replacement":       "labourers"
						 },

	"laboring":         {"word":    "laboring",
						 "replacement":       "labouring"
						 },

	"laborred":         {"word":    "laborred",
						 "replacement":       "laboured"
						 },

	"labors":         {"word":    "labors",
						 "replacement":       "labours"
						 },

	"luster":         {"word":    "luster",
						 "replacement":       "lustre"
						 },

	"maneuver":         {"word":    "maneuver",
						 "replacement":       "manoeuvrer"
						 },

	"maneuvered":         {"word":    "maneuvered",
						 "replacement":       "manoeuvrered"
						 },

	"maneuvers":         {"word":    "maneuvers",
						 "replacement":       "manoeuvrers"
						 },

	"meager":         {"word":    "meager",
						 "replacement":       "meagre"
						 },

	"misbehavior":         {"word":    "misbehavior",
						 "replacement":       "misbehaviour"
						 },

	"misbehaviors":         {"word":    "misbehaviors",
						 "replacement":       "misbehaviours"
						 },

	"molded":         {"word":    "molded",
						 "replacement":       "moulded"
						 },

	"molding":         {"word":    "molding",
						 "replacement":       "moulding"
						 },

	"moldings":         {"word":    "moldings",
						 "replacement":       "moildings"
						 },

	"neighbor":         {"word":    "neighbor",
						 "replacement":       "neighbour"
						 },

	"neighboring":         {"word":    "neighboring",
						 "replacement":       "neighbouring"
						 },

	"neighbors":         {"word":    "neighbors",
						 "replacement":       "neighbours"
						 },

	"offense":         {"word":    "offense",
						 "replacement":       "offence"
						 },

	"offenses":         {"word":    "offenses",
						 "replacement":       "offences"
						 },

	"parlor":         {"word":    "parlor",
						 "replacement":       "parlour"
						 },

	"parlors":         {"word":    "parlors",
						 "replacement":       "parlours"
						 },

	"plow":         {"word":    "plow",
						 "replacement":       "plough"
						 },

	"plowed":         {"word":    "plowed",
						 "replacement":       "ploughed"
						 },

	"plowing":         {"word":    "plowing",
						 "replacement":       "ploughing"
						 },

	"plowwed":         {"word":    "plowwed",
						 "replacement":       "ploughed"
						 },

	"pretense":         {"word":    "pretense",
						 "replacement":       "pretence"
						 },

	"pretenses":         {"word":    "pretenses",
						 "replacement":       "pretences"
						 },

	"rumor":         {"word":    "rumor",
						 "replacement":       "rumour"
						 },

	"rumored":         {"word":    "rumored",
						 "replacement":       "rumoured"
						 },

	"rumoring":         {"word":    "rumoring",
						 "replacement":       "rumouring"
						 },

	"rumors":         {"word":    "rumors",
						 "replacement":       "rumours"
						 },

	"sabers":         {"word":    "sabers",
						 "replacement":       "sabres"
						 },

	"theater":         {"word":    "theater",
						 "replacement":       "theatre"
						 },

	"theaters":         {"word":    "theaters",
						 "replacement":       "theatres"
						 },
    
    #states

	"indiana":         {"word":    "indiana",
						 "replacement":       "in"
						 },

	"washingtonned":         {"word":    "washingtonned",
						 "replacement":       "was"
						 },

    #elements...

	"americium":         {"word":    "americium",
						 "replacement":       "am"
						 },

	"americium":         {"word":    "americium",
						 "replacement":       "am"
						 },

	"dysprosium":         {"word":    "dysprosium",
						 "replacement":       "dies"
						 },

	"einsteinium":         {"word":    "einsteinium",
						 "replacement":       "e"
						 },

	"holmium":         {"word":    "holmium",
						 "replacement":       "ho"
						 },

	"holmiums":         {"word":    "holmiums",
						 "replacement":       "hosses"
						 },

	"nobelium":         {"word":    "nobelium",
						 "replacement":       "no"
						 },

	"oxygen":         {"word":    "oxygen",
						 "replacement":       "o"
						 },

	"uranium":         {"word":    "uranium",
						 "replacement":       "us"
						 },

	"vanadium":         {"word":    "vanadium",
						 "replacement":       "v"
						 },
    
    #numbers

	"matchless":         {"word":    "matchless",
						 "replacement":       "one"
						 },

	"deuce":         {"word":    "deuce",
						 "replacement":       "two"
						 },

	"trey":         {"word":    "trey",
						 "replacement":       "three"
						 },

	"four-spot":         {"word":    "four-spot",
						 "replacement":       "four"
						 },

	"five-spot":         {"word":    "five-spot",
						 "replacement":       "five"
						 },

	"six-spot":         {"word":    "six-spot",
						 "replacement":       "six"
						 },

	"seven-spot":         {"word":    "seven-spot",
						 "replacement":       "seven"
						 },

	"ten-spot":         {"word":    "ten-spot",
						 "replacement":       "ten"
						 },

    #Other things...

	"adenine":         {"word":    "adenine",
						 "replacement":       "a"
						 },

	"ala":         {"word":    "ala",
						 "replacement":       "alas"
						 },

	"ampere":         {"word":    "ampere",
						 "replacement":       "a"
						 },

	"angstrom":         {"word":    "angstrom",
						 "replacement":       "a"
						 },

	"centrals":         {"word":    "centrals",
						 "replacement":       "central"
						 },

	"distinguishs":         {"word":    "distinguishs",
						 "replacement":       "distinguishes"
						 },

	"fagot":         {"word":    "fagot",
						 "replacement":       "faggot"
						 },

	"godhead":         {"word":    "godhead",
						 "replacement":       "god"
						 },

	"mustiness":         {"word":    "mustiness",
						 "replacement":       "must"
						 },

	"overlord":         {"word":    "overlord",
						 "replacement":       "lord"
						 },

	"subsequentlies":         {"word":    "subsequentlies",
						 "replacement":       "subsequently"
						 },

	"u":         {"word":    "u",
						 "replacement":       "us"
						 },

	"uracil":         {"word":    "uracil",
						 "replacement":       "us"
						 },

	"whitethorn":         {"word":    "whitethorn",
						 "replacement":       "may"
						 },

	"willfully":         {"word":    "willfully",
						 "replacement":       "wilfully"
						 },


	"aforesaidded":         {"word":    "aforesaidded",
						 "replacement":       "said"
						 },

	"awaied":         {"word":    "awaied",
						 "replacement":       "forth"
						 },

	"brassyer":         {"word":    "brassyer",
						 "replacement":       "brassier"
						 },

	"closeer":         {"word":    "closeer",
						 "replacement":       "closer"
						 },

	"earlyer":         {"word":    "earlyer",
						 "replacement":       "earlier"
						 },

	"fraied":         {"word":    "fraied",
						 "replacement":       "frayed"
						 },

	"glader":         {"word":    "glader",
						 "replacement":       "gladder"
						 },

	"gloomyer":         {"word":    "gloomyer",
						 "replacement":       "gloomier"
						 },

	"gooder":         {"word":    "gooder",
						 "replacement":       "better"
						 },

	"goodest":         {"word":    "goodest",
						 "replacement":       "best"
						 },

	"happyer":         {"word":    "happyer",
						 "replacement":       "happier"
						 },

	"healthyer":         {"word":    "healthyer",
						 "replacement":       "healthier"
						 },

	"heavyer":         {"word":    "heavyer",
						 "replacement":       "heavier"
						 },

	"hoter":         {"word":    "hoter",
						 "replacement":       "hotter"
						 },

	"lateer":         {"word":    "lateer",
						 "replacement":       "later"
						 },

	"lieer":         {"word":    "lieer",
						 "replacement":       "lie"
						 },

	"slily":         {"word":    "slily",
						 "replacement":       "slyly"
						 },

	"smokyer":         {"word":    "smokyer",
						 "replacement":       "smokier"
						 },

	"topmostest":         {"word":    "topmostest",
						 "replacement":       "topmost"
						 },

	"traveler":         {"word":    "traveler",
						 "replacement":       "traveller"
						 },
    

	"lashkar-e-taiba":         {"word":    "lashkar-e-taiba",
						 "replacement":       "let"
						 },

	"lashkar-e-taibaed":         {"word":    "lashkar-e-taibaed",
						 "replacement":       "let"
						 },

	"harkat-ul-mujahidin":         {"word":    "harkat-ul-mujahidin",
						 "replacement":       "hum"
						 },

	"harkat-ul-mujahidined":         {"word":    "harkat-ul-mujahidined",
						 "replacement":       "hummed"
						 },

	"dimash":         {"word":    "dimash",
						 "replacement":       "damascus"
						 },

    # stuff we absolutely DO NOT WANT in our output

	"semen":         {"word":    "semen",
						 "replacement":       "come"
						 },

	"cunt":         {"word":    "cunt",
						 "replacement":       "snatch"
						 },

	"orgasming":         {"word":    "orgasming",
						 "replacement":       "coming"
						 },

    # some of these are just plain weird. Wordnet, what were you on...?
    # Can be pretty damn sure that none of these will come up in Dickens novel :)

	"bastardly":         {"word":    "bastardly",
						 "replacement":       "mean"
						 },

	"clitoris":         {"word":    "clitoris",
						 "replacement":       "buttons"
						 },

	"deflowered":         {"word":    "deflowered",
						 "replacement":       "ruined"
						 },

	"fellate":         {"word":    "fellate",
						 "replacement":       "blow"
						 },

	"fellated":         {"word":    "fellated",
						 "replacement":       "blew"
						 },

	"fellating":         {"word":    "fellating",
						 "replacement":       "sucking"
						 },

	"fucks":         {"word":    "fucks",
						 "replacement":       "screws"
						 },

	"gonorrhea":         {"word":    "gonorrhea",
						 "replacement":       "clap"
						 },

	"heterosexual":         {"word":    "heterosexual",
						 "replacement":       "straight"
						 },

	"heterosexualled":         {"word":    "heterosexualled",
						 "replacement":       "straight"
						 },

	"homo":         {"word":    "homo",
						 "replacement":       "men"
						 },

	"homos":         {"word":    "homos",
						 "replacement":       "men"
						 },

	"inseminate":         {"word":    "inseminate",
						 "replacement":       "sow"
						 },

	"nigger":         {"word":    "nigger",
						 "replacement":       "spade"
						 },

	"niggers":         {"word":    "niggers",
						 "replacement":       "spades"
						 },

	"orificing":         {"word":    "orificing",
						 "replacement":       "opening"
						 },

	"penis":         {"word":    "penis",
						 "replacement":       "members"
						 },

	"piddled":         {"word":    "piddled",
						 "replacement":       "trifled"
						 },

	"queered":         {"word":    "queered",
						 "replacement":       "exposed"
						 },

	"queers":         {"word":    "queers",
						 "replacement":       "perils"
						 },

	"raped":         {"word":    "raped",
						 "replacement":       "despoil"
						 },

	"semened":         {"word":    "semened",
						 "replacement":       "come"
						 },

	"semenned":         {"word":    "semenned",
						 "replacement":       "come"
						 },

	"testis":         {"word":    "testis",
						 "replacement":       "nuts"
						 },

	"asshole":         {"word":    "asshole",
						 "replacement":       "sob"
						 },

	"whoremasters":         {"word":    "whoremasters",
						 "replacement":       "tricks"
						 },

    #these just sound strange when they come up...

	"idol":         {"word":    "idol",
						 "replacement":       "god"
						 },

	"deity":         {"word":    "deity",
						 "replacement":       "god"
						 },


	"the God Chancellor":         {"word":    "the God Chancellor",
						 "replacement":       "the Lord Chancellor"
						 },

	"Overlord High Chancellor":         {"word":    "Overlord High Chancellor",
						 "replacement":       "Lord High Chancellor"
						 },





}

def check_for_exceptions(word):
    """check (and hopefully correct) for irregular and/or mangled
    words."""

    #probably better way to generalise this...

    if word != string.lower(word):
        word != string.lower(word)

    if exceptions_dict.has_key(word):
        return exceptions_dict[word]["replacement"]
    else:
        #print "	NO EXCEPTIONS FOUND - RETURNING '%s'" % word
        return word



