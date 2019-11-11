#!/usr/local/bin/python
# -*- coding: UTF-8 -*-

#bibliography.py

"""This file creates 'bibliography.py' - A bibliography of everything Charles Dickens ever wrote.

Used when creating titles using Markov chains.

"""

import string


#from https://www.charlesdickensinfo.com/novels/complete-works/
#Charles Dickens Info - List of Works by Charles Dickens
#The 15 Novels by Charles Dickens Listed by Publication Date

list1 = """
The Pickwick Papers
The Posthumous Papers of the Pickwick Club
Oliver Twist
Oliver Twist; or, The Parish Boy's Progress
Nicholas Nickleby
The Old Curiosity Shop
Barnaby Rudge
Martin Chuzzlewit
Dombey and Son
David Copperfield
Bleak House
Hard Times
Little Dorrit
A Tale of Two Cities
Great Expectations
Our Mutual Friend
The Mystery of Edwin Drood
"""


#from https://www.charlesdickensinfo.com/novels/complete-works/
#Charles Dickens Info - Partial Listing of Novellas, Short Stories and Other Works by Charles Dickens in Alphabetical Order

list1A = """

The Battle of Life
A Child's Dream of a Star
The Chimes: A Goblin Story
A Christmas Carol
A Christmas Tree
The Cricket on the Hearth: A Fairy Tale of Home
A Dinner at Poplar Walk
Doctor Marigold's Prescriptions
A Flight
Frozen Deep
George Silverman's Explanation
Going into Society
The Haunted Man
A Holiday Romance
The Holly-Tree
Hunted Down
The Lamplighter
The Long Voyage
Master Humphrey's Clock
A Message from the Sea
Mrs. Lirriper's Legacy
Mrs. Lirriper's Lodgings
No Thoroughfare
Nobody's Story
Public Life of Mr. Trumble, Once Mayor of Mudfog
Sketches by Boz
The Story of the Goblins Who Stole a Sexton
The Goblins Who Stole A Sexton
Sunday under Three Heads
Tom Tiddler's Ground
Travelling Abroad
The Uncommercial Traveller
Wreck of the Golden Mary
"""

#from http://www.dickens-online.info/charles-dickens-bibliography.htm
#Charles Dickens online - Bibliography

list2 = """
Sketches by Boz
The Pickwick Papers
Oliver Twist
Nicholas Nickleby
The Old Curiosity Shop
Barnaby Rudge
Master Humphrey's Clock
A Christmas Carol
The Chimes
American Notes
The Life and Adventures of Martin Chuzzlewit
Christmas Books
Pictures from Italy
The Cricket on the Hearth
The Battle of Life
Dombey and Son
The Haunted Man and the Ghost's Bargain
David Copperfield
A Child's History of England
Bleak House
Hard Times
Little Dorrit
The Wreck of the Golden Mary
The Perils of Certain English Prisoners
A Tale of Two Cities
Hunted Down
The Uncommercial Traveller
A Message from the Sea
Great Expectations
Reprinted Pieces
Tom Tiddler's Ground
The Haunted House
Somebody's Luggage
Mrs Lirriper's Lodgings
Mrs Lirriper's Legacy
Our Mutual Friends
Doctor Marigold
The Trial for Murder
Mugby Junction
The Signal-Man
No Thoroughfare
The Mystery of Edwin Drood
The Mudfog Papers
The Lazy Tour of Two Idle Apprentices
To Be Read At Dusk

A Christmas Carol
A Tale of Two Cities
Barnaby Rudge
Bleak House
David Copperfield
Dombey and Son
Great Expectations
Hard Times
Little Dorrit
Martin Chuzzlewit
The Life and Adventures of Martin Chuzzlewit
Nicholas Nickleby
Oliver Twist
Our Mutual Friend
The Mystery of Edwin Drood
The Old Curiosity Shop
The Pickwick Papers

A Holiday Romance
A Message From the Sea
Doctor Marigold
George Silvermans Explanation
Hunted Down
Master Humphrey's Clock
Mrs. Lirriper's Legacy
Mrs. Lirriper's Lodgings
Mudfog and Other Sketches
Public Life Of Mr. Tulrumble
The First Meeting of Mudfog
The Pantomime of Life
A Lion
Mugby Junction
Reprinted Pieces
The Long Voyage
The Begging-Letter Writer
A Child's Dream of a Star
Our English Watering-Place
Sketches by Boz
Sketches of Young Couples
Sketches of Young Gentlemen
Some Short Christmas Stories
A Christmas Tree
The Child's Story
The Schoolboy's Story
Nobody's Story
The Poor Relation's Story
Somebody's Luggage
Sunday Under Three Heads
The Battle of Life
The Chimes
The Cricket on the Hearth
The Haunted House
The Haunted Man and the Ghost's Bargain
The Holly Tree
The Lamplighter
The Lazy Tour of Two Idle Apprentices
The Perils of Certain English Prisoners
The Seven Poor Travellers
The Signal Man
The Trial For Murder
The Wreck of the Golden Mary
To Be Read At Dusk
Tom Tiddler's Ground
A Childs History of England
All The Year Round
The Poor Man and his Beer
Landor's Life
The Late Mr. Stanfield
American Notes
Miscellaneous Papers
Pictures From Italy
Speeches: Literary and Social
The Uncommercial Traveller
A Christmas Carol
A Tale of Two Cities
Barnaby Rudge
Bleak House
David Copperfield
Dombey and Son
Great Expectations
Hard Times
Little Dorrit
Nicholas Nickleby
Oliver Twist
Our Mutual Friend
Martin Chuzzlewit
The Mystery of Edwin Drood
The Old Curiosity Shop
The Pickwick Papers
"""


#from https://en.wikipedia.org/wiki/Charles_Dickens_bibliography
#From Wikipedia, the free encyclopedia - Charles Dickens bibliography

list3 = """

The Pickwick Papers	
Oliver Twist
Nicholas Nickleby
The Old Curiosity Shop
Barnaby Rudge
Martin Chuzzlewit
A Christmas Carol
The Chimes
The Cricket on the Hearth
The Battle of Life
The Haunted Man and the Ghost's Bargain
Dombey and Son
David Copperfield
Bleak House
Hard Times
Little Dorrit
A Tale of Two Cities
Great Expectations
Our Mutual Friend
The Mystery of Edwin Drood

The Lamplighter
A Child's Dream of a Star
Captain Murderer
To be Read at Dusk
The Long Voyage
Prince Bull
Thousand and One Humbugs
Hunted Down
The Signal-Man
George Silverman's Explanation
Holiday Romance
The Queer Chair
The Ghosts of the Mail
The Baron of Grogzwig
A Madman's Manuscript
A Ghost in the Bride's Chamber
The Lazy Tour of Two Idle Apprentices
The Goblins who Stole a Sexton
The Pickwick Papers

A Christmas Tree
What Christmas is, as We Grow Older
The Poor Relation's Story
The Child's Story
The Schoolboy's Story
Nobody's Story
The Seven Poor Travellers
The Holly-tree Inn
The Wreck of the Golden Mary
The Perils of Certain English Prisoners
Going into Society
A Message from the Sea
Tom Tiddler's Ground
Somebody's Luggage
Mrs Lirriper's Lodgings
Mrs Lirriper's Legacy
Doctor Marigold's Prescriptions
The Trial for Murder
Mugby Junction
The Signal-Man
No Thoroughfare

The Seven Poor Travellers
The Holly-tree Inn
The Wreck of the Golden Mary
The Perils of Certain English Prisoners
The Lazy Tour of Two Idle Apprentices
A House to Let
The Haunted House
A Message from the Sea
Tom Tiddler's Ground
Mrs Lirriper's Lodgings
Mrs Lirriper's Legacy
The Trial for Murder
Mugby Junction
No Thoroughfare

Sketches by Boz
Sketches of Young Gentlemen
Sketches of Young Couples
Master Humphrey's Clock
Boots at the Holly-tree Inn: And Other Stories
Reprinted Pieces
The Mudfog Papers
Mudfog and Other Sketches

Sunday Under Three Heads
The Strange Gentleman
The Village Coquettes
The Fine Old English Gentleman
American Notes: For General Circulation
Pictures from Italy
The Life of Our Lord: As written for his children
A Child's History of England
The Frozen Deep
The Uncommercial Traveller
Speeches, Letters and Sayings
Letters of Charles Dickens to Wilkie Collins
The Complete Poems of Charles Dickens

A Coal Miner's Evidence
Frauds on the Fairies
In Memoriam W. M. Thackeray the first!
The Lost Arctic Voyagers
"""

#from https://en.wikipedia.org/wiki/Charles_Dickens_bibliography
#From Wikipedia, the free encyclopedia - Bibliography
list4 = """

The Pickwick Papers
Oliver Twist
Nicholas Nickleby
The Old Curiosity Shop
Barnaby Rudge
Martin Chuzzlewit
Dombey and Son
David Copperfield
Bleak House
Hard Times
Little Dorrit
A Tale of Two Cities
Great Expectations
Our Mutual Friend
The Mystery of Edwin Drood

A Christmas Carol
The Chimes
The Cricket on the Hearth
The Battle of Life
The Haunted Man and the Ghost's Bargain

The Long Voyage
The Signal-Man

Sketches by Boz
The Mudfog Papers
Master Humphrey's Clock

American Notes
Pictures from Italy
The Life of Our Lord
A Child's History of England
The Uncommercial Traveller

The Frozen Deep
No Thoroughfare

Bentley's Miscellany
Master Humphrey's Clock
The Daily News
Household Words
All the Year Round

A House to Let
The Haunted House
A Message from the Sea
Mugby Junction
No Thoroughfare
"""

#from https://www.biblio.com/charles-dickens/author/3
#Biblio - Authors - Charles Dickens books

list5 = """
The Adventures of Oliver Twist
A Christmas Carol
A Tale of Two Cities
Great Expectations

Hunted Down: The Detective Stories of Charles Dickens
A Christmas Carol in Prose Being a Ghost Story of Christmas
The posthumous papers of the Picwick club
A Tale Of Two Cities, Complete and Unabridged
The Bagman's Story
The Story Of the Bagman's Uncle
A Budget Of Christmas Tales

A Child's Dream Of a Star
A Child's History Of England
American Notes
Pictures From Italy

A Christmas Carol
A Christmas Carol Deluxe
A Christmas Carol and Other Christmas Books
A Christmas Carol and Other Christmas Stories
A Christmas Carol and Other Christmas Writings
A Christmas Carol and Other Haunting Tales
A Christmas Carol and Other Holiday Tales
A Christmas Carol and Other Short Stories
A Christmas Carol and Other Stories
A Christmas Carol and The Cricket On the Hearth
A Christmas Carol and Two Other Christmas Books

A Christmas Carol In Prose
A Christmas Carol In Prose Being a Ghost Story Of Yule-Tide
A Christmas Carol In Prose, Being a Ghost Story Of Christmas
A Christmas Carol In Prose, Being a Ghost Story Of Yule-Tide

A Christmas Carol, a Ghost Story Of Christmas
A Christmas Carol, and The Chimes
A Christmas Carol, Being a Ghost Story Of Christmas

A Christmas Dinner
A Christmas Tree

A House To Let
A Message From the Sea

A Plated Article

A Pottery Story
A Rosy Path
A Round Of Stories By the Christmas Fire

A Tale Of Two Cities
A Tale Of Two Cities a Story Of the French Revolution

All the Year Round
American Notes
Pictures From Italy

American Notes For General Circulation

An Account Of a Wedding
An Account Of a Wedding, Excerpts From the Pickwick Papers
Another Round Of Stories By the Christmas Fire

Barnaby Rudge
Barnaby Rudge, a Tale Of the Riots Of Eighty
Barnaby Rudge, a Tale Of the Riots Of '80

Baron Of Grogzwig
Beautiful Stories About Children

Bentley's Miscellany
Best Ghost Stories
Bleak House
Bleak House or Poor Jo

Boots At the Holly Tree Inn
Boots At the Holly-Tree Inn and Other Stories

Captain Boldheart
Captain Boldheart the Magic Fishbone
Captain Boldheart and The Latin-Grammar Master
Captain Boldheart the Magic Fishbone
Captain Grant's Children
Captain Murderer

Oliver Twist
Stories From the Christmas Numbers
Four Complete Novels
Four Novels

Pickwick Papers
Great Expectations
a Tale Of Two Cities
Book Of Memoranda
Children Stories
Christmas Stories
Complete Works
David Copperfield
Hard Times
the Chimes
Three Short Stories

Mrs Lirriper's Lodgings

Chops the Dwarf

Christmas At Dingley Dell
The Christmas Stories
Christmas Eve With the Spirits
Christmas Ghost Stories
Christmas Short Stories
Christmas Stories

Christmas Tales
Christmas Tales Of Fantasy

Complete Ghost Stories
Complete Works

Courts Of Europe

David Cooperfield
David Coperfield
David Copperfield
David Copperfield a Reading In Five Chapters
David Copperfield the Younger

Dealings With the Firm Of Dombey and Son
Dealings With the Firm Of Dombey and Son Wholesale, Retail and For Exportation
December Vision

Dialogues From Dickens
Dictionary Of Paris, 1882 an Unconventional Handbook

Christmas Spirits
Dictionary Of London 1888
Dreadful Almanac
Dictionary Of London
Dictionary Of London, 1885
Dictionary Of Paris
Dictionary Of the Thames
Dictionary Of the Thames, 1887

Doctor Marigold
Doctor Marigold's Prescriptions

Dombey and Son
Dombey and Sons
Dominoes

Dr Blimber's School
Drawn From Life

Edwin Drood

Florence Dombey

George Silverman's Explanation

Ghostly Christmas
Going Into Society

Great Expectaions
Great Expectatations
Great Expectations

Hard Times

Hard Times For These Times

Haunted Man and The Ghost's Bargain

Holiday Romance
Holiday Tales
Holly Berries
Household Words

Hunted Down

Inspector Bucket's Job
Is She His Wife or Something Singular
Is She His Wife
Something Singular

John Jasper's Secret

Lazy Tour Of Two Idle Apprentices

Life and Adventures Of Martin Chuzzlewit
Life and Adventures Of Nicholas Nickelby

Life's Little Handbook Of Wisdom
Little Dorrit

Little Dorritt
Little Nell
Little Nell From the Old Curiosity-Shop
Little Paul Domby

Magic Fishbone

Martin Chuzzlewit

Master Humphrey's Clock

Miscellaneous Papers
Miscellaneous Tales
Miscellaneous Tales, and Sketches

Mr Nightingale's Diary
Mr Pickwick
Mr Pickwick's Christmas
Mrs Gamp
Mrs Lirriper
Mrs Lirriper and Other Stories
Mrs Lirriper's Legacy
Mrs LirriperS Lodgings
Mrs Orange
Mudfog and Other Sketches
Mugby Junction
Mugby Junction and Other Stories
Murder and Mystery
My Early Times
Nell and Her Grandfather
Nicholas Nickelby
Nicholas Nickleby
Nicolas Nickleby
Night Walks
Nikolaus Nickleby
No Thoroughfare
Old Curiosity Shop
Old Lamps For New Ones
Old Lamps For New Ones and Other Sketches and Essays
Old Lamps For New Ones and Other Sketches and Essays Hitherto Uncollected
Old Lamps For New Ones and Other Sketches and Essays, Hitherto Uncollected
Oliver Twist
Oliver Twist Or, the Parish Boy's Progress
Oliver Twist, Complete and Unabridged
Olivier Twist
On London
On Poverty
On Travel
One Dinner a Week and Travels In the East
Our Mutual Friend
Paul Dombey
Pearl-Fishing
Pickwick Club
Pickwick Papers
Pickwick Papers the Posthumous Papers Of the Pickwick Club
Pictures From Italy
Reprinted Pieces
Scenes Of London Life
Sketches
Sketches By Boz
Sketches By Boz Illustrative Of Every-Day Life and Every-Day People
Sketches Of Young Couples
Sketches Of Young Gentlemen
Sketches Of Young Gentlemen and Young Couples
Sketches Of Young Gentlemen, Dedicated To the Young Ladies

Some Christmas Stories
Some Short Christmas Stories
Somebody's Luggage
Sunday Under Three Heads
Tale Of 2 Cities

The Adventures Of Oliver Twist

The Bagman's Story
The Battle Of Life
The Battle Of Life - a Love Story

The Child Wife
The Child's Story

The Childhood Of David Copperfield
The Children's David Copperfield

The Chimes
The Chimes a Goblin Story
The Chimes a Goblin Story Of Some Bells That Rang an Old Year Out and A New Year In
The Christmas Books

The Cricket On the Hearth
The Cricket On the Hearth a Fairy Tale Of Home
The D Case

The Haunted House
The Haunted Man
The Haunted Man and The Ghost's Bargain
The Haunted Man and The Ghosts Bargin

The Holly Tree
The Holly Tree Inn
The Holly-Tree and Other Christmas Stories
The Holly-Tree Inn
The Holly-Tree Inn
The Household Narrative Of Current Events
The Illustrated Life Adventures Of Nicholas Nickleby

The Lamplighter
The Lamplighter's Story

The Life Adventures Of Martin Chuzzlewit
The Life and Adventures Of Martin Chuzzlewit
The Life and Adventures Of Martin Chuzzlewit His Relatives Friends and Enemies

The Life and Adventures Of Nicholas Nickleby

The Life and Adveture
The Life Of Our Lord
The Life Of Our Lord Written Expressly For His Children
The Life Of Our Lord Written For His Children During the Years 1846-1849

The Loving Ballad Of Lord Bateman
The Manuscript Of Great Expectations
The Mudfog Papers
The Mudfog Papers Etc Now First Collected
The Mudfog Papers, Etc
The Mudfrog Papers
The Mystery Of Edwin Drood

The Old Curiosity Shop
The Old Curiousity Shop
The Perils Of Certain English Prisoners
The Personal History and Experience Of David Copperfield
The Personal History and Experience Of David Copperfield the Younger
The Personal History Of David Copperfield
The Personal History, Adventures, Experience Observation Of David Copperfield the Younger Of Blunderstone Rookery
The Personal History, Experience and Observation Of David Copperfield
The Pickwick Papers
The Pickwick Papers, Vol 1
The Pickwick Papers, Volume II

The Poor Traveller

The Posthumous Papers
The Posthumous Papers Of the Pickwick Club
The Posthumous Papers Of the Pickwick Club Vol 1
The Posthumous Papers Of the Pickwick Club Volume II
The Posthumous Papers Of the Pickwick Club, Volume 1
The Posthumous Papers Of the Pickwick Club, Volume 2
The Posthumous Papers Of the Pickwick Club, Volume 3
The Posthumous Papers Of the Pickwick Club, Volume I
The Posthumous Papers Of the Pickwick Papers
The Postumous Papers Of the Pickwick Club
The Public Readings

The Seven Poor Travelers
The Seven Poor Travellers

The Signalman
The Signalman Other Ghost Stories

The Story Of Little Dombey
The Story Of Little Nell
The Story Of Oliver Twist

The Story Of Richard Doubledick

The Strange Gentleman

The Trial Of William Tinkling

The Uncommercial Traveler
The Uncommercial Traveller

The Village Coquettes
The Wedding Bells

The World Here and There
The Wreck Of the Golden Mary

To Be Read At Dusk

Tom Tiddler's Ground

Twice-Told Tales
Two Boxes Of Gold
Two Boxes Of Gold and Other Stories

What Christmas Is As We Grow Older
What Christmas Is As We Grow Older, and Other Stories

"""



def run():
    header = '''#!/usr/local/bin/python
# -*- coding: UTF-8 -*-

#bibliography.py


"""A full bibliography of everything Charles Dickens ever wrote.

Used when creating titles using Markov chains.

Sources:
    -   https://www.charlesdickensinfo.com/novels/complete-works/
    -   http://www.dickens-online.info/charles-dickens-bibliography.htm
    -   https://en.wikipedia.org/wiki/Charles_Dickens_bibliography
    -   https://www.biblio.com/charles-dickens/author/3    
"""



'''
    subheader = """publications = [

"""
    footer = """\t]

# END OF FILE

"""

    known_publications = []
    
    sources = [list1, list1A, list2, list3, list4, list5]

    outfn = "bibliography.py"
    OUTFILE = open(outfn,"w")
    OUTFILE.write(header)

    for src in sources:
        for line in src.split("\n"):
            line = string.strip(line)
            #print line
            if line != "":
                if line not in known_publications:
                    known_publications.append(line)
            print ".",

    print
    known_publications.sort()

    subheader = """# %s publications listed.

%s
""" % (len(known_publications), subheader)

    OUTFILE.write(subheader)


    for p in known_publications:
        OUTFILE.write('\t"%s",\n' % p)
    

    OUTFILE.write(footer)
    OUTFILE.close()
    print "Done."
    print "Wrote '%s'." % outfn

if __name__ == "__main__":
    run()

