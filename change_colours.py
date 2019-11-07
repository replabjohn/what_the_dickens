#!/usr/local/bin/python
# -*- coding: UTF-8 -*-

__VERSION__ = "0.9.2a"

DEBUG = 0
#DEBUG = 1

GRAPHICSMODE = "PIL"

#standard imports
import random, string
import os, glob, sys

from types import *

rootdir = os.getcwd()

import PIL
import PIL.Image as PilImage #to avoid nameclashes with Renpy functions
import PIL.ImageFilter as ImageFilter

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

def change_Main_Color (im, newcolor):
    """changes white in supplied image (im) to specified colour (newcolour)"""
    DEBUG = 0
    #DEBUG = 1

    if DEBUG == 1:
        print "newcolor:", newcolor
        print "im:", im
    
    THRESHOLD = 225 # Doesn't rely on colour being exactly 255,255,255

    im.convert("RGBA")
    newimdata = []
    for color in im.getdata():
        if color[0] > THRESHOLD:
            if color[1] > THRESHOLD:
                if color[2] > THRESHOLD:
                    if color[3] > THRESHOLD:
                        newimdata.append(newcolor)
                    else:
                        newimdata.append(color)
                else:
                    newimdata.append(color)
            else:
                newimdata.append(color)
        else:
            newimdata.append(color)

    newim = PilImage.new("RGBA",im.size)
    newim.putdata(newimdata)

    return newim


def change_Other_Color(im, newcolor):
    #DEBUGS = 0
    DEBUG = 1

    im.convert("RGBA")
    newimdata = []
    CHANGECOLOR = (204,204,204,255) # RGB + ALPHA CHANNEL
    for color in im.getdata():
        if color == CHANGECOLOR:
            newimdata.append(newcolor)
        else:
            newimdata.append(color)
    newim = PilImage.new("RGBA",im.size)
    newim.putdata(newimdata)

    return newim


def change_Black_Outline_Color(im, newcolor):
    DEBUG = 0
    im.convert("RGBA")
    newimdata = []

    THRESHOLD = 25
    for color in im.getdata():
        if color[0] < THRESHOLD:
            if color[1] < THRESHOLD:
                if color[2] < THRESHOLD:
                    if color[3] > 200:
                        newimdata.append(newcolor)
                    else:
                        newimdata.append(color)
                else:
                    newimdata.append(color)
            else:
                newimdata.append(color)
        else:
            newimdata.append(color)
    newim = PilImage.new("RGBA",im.size)
    newim.putdata(newimdata)

    return newim



if __name__ == "__main__":
    print "%s (version: %s)" % (string.split(__file__,"\\")[-1], __VERSION__ )
    print

    c = heraldic_cols[random.choice(heraldic_cols.keys())]
    print c["Colour"]
                      
