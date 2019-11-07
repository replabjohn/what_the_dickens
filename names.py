#!/usr/local/bin/python
# -*- coding: UTF-8 -*-
# author: John Precedo (replabjohn@googlemail.com)

__VERSION__ = '0.3.2g'

"""
John Precedo's names library.

This file contains:
    * 824 male first names in the tuple names_first_male
    * 1070 female first names in the tuple names_first_female
    * 3069 surnames in the tuple surnames

It exposes the following functions
    * getMaleFirstName(): returns a random man's first name
    * getFemaleFirstName(): returns a random woman's first name
    * getSurname(): returns a surname
    * getMaleName: returns a random man's name - firstname and surname
    * getFemaleName(): returns a random woman's name - firstname and surname
    * getName(): returns a random name - first name and surname
    * test(): prints an example of each.

"""


import random, string, sys

STYLES = (None, "English", "Standard", "English_1", "Standard_1", "English_2", "Standard_2",
          "Spanish", "Italian", "French", "German", "Russian",
          "Chinese", "Japanese", "Korean", "Indian", 
          "Scots_Gaelic")
#styles to include:
#Icelandic
#Danish
#Irish Gaelic

#STYLES = (None, "English", "Standard", "French", "Italian", "Spanish", "Chinese", "Japanese", "Korean", "Russian", "Scottish", "Irish")


# taken from work on chatbot Alex (written April 2002-February 2003)
# 824 male first names.
male_firstnames =("Aaron", "Adam", "Adam", "Aden", "Adrian", "Aiden", "Aidan", "Al",
        "Alaister", "Alan", "Alasdair", "Alastair", "Albert", "Alec", "Alec", "Alex",
        "Alex", "Alexander", "Alistair", "Alfred", "Allan", "Allen", "Alvin", "Andre",
        "Andrew", "Andy", "Angus", "Anton", "Antonio", "Anthony", "Antony", "Archie",
        "Arnold", "Arthur", "Austin", "Abraham", "Alexei", "Alf", "Arnie", "Barnard",
        "Barney", "Barry", "Basil", "Ben", "Ben", "Benedict", "Benjamin", "Benny",
        "Bernard", "Bernie", "Bertram", "Bertrand", "Bill", "Bill", "Billy", "Blake",
        "Bob", "Bob", "Bobby", "Boris", "Brad", "Bram", "Brandon", "Brendan", "Bret",
        "Brian", "Brian", "Bruce", "Bruno", "Bryan", "Burt", "Barnabas", "Barnaby",
        "Bartholomew", "Bradley", "Caleb", "Calum", "Callum", "Calvin", "Cameron",
        "Carl", "Carlo", "Carlos", "Cecil", "Charles", "Charles", "Charlie", "Chris",
        "Christopher", "Cliff", "Clifford", "Clive", "Colin", "Conor", "Connor",
        "Conrad", "Corey", "Cormac", "Cornelius", "Craig", "Curtis", "Cyril", "Cal",
        "Caspar", "Casper", "Chas", "Chester", "Clark", "Claude", "Collin", "Corwin",
        "Cosmo", "Cristopher", "Curt", "Damian", "Damien", "Damon", "Dan", "Dan", "Daniel",
        "Danny", "Dario", "Darrell", "Darren", "Dave", "Dave", "David", "David", "Dean",
        "Declan", "Denis", "Dennis", "Derek", "Des", "Desmond", "Dexter", "Dick", "Dom",
        "Dominic", "Don", "Donald", "Doug", "Dougal", "Douglas", "Duane", "Duncan", "Dylan",
        "Dale", "Davey", "Davy", "Del", "Delbert", "Desmund", "Dirk", "Dominick", "Donnie",
        "Donny", "Donovan", "Dougie", "Dudley", "Dustin", "Dwight", "Eamonn", "Ed", "Eddie",
        "Eddie", "Edgar", "Edward", "Edmund", "Edwin", "Emile", "Eric", "Eric", "Erik",
        "Erich", "Ernest", "Ernie", "Errol", "Ethan", "Euan", "Eugene", "Evan", "Ewan",
        "Ewen", "Ezra", "Edmond", "Eli", "Elias", "Elijah", "Elisha", "Elliot", "Elliott",
        "Ellis", "Elmer", "Elmore", "Elroy", "Elton", "Emil", "Emilio", "Emmet", "Emmett",
        "Enrico", "Everett", "Fabio", "Felix", "Fergus", "Ford", "Francis", "Francisco",
        "Frank", "Franz", "Fraser", "Fred", "Frederic", "Frederick", "Fritz", "Fletcher",
        "Frankie", "Franklin", "Freddie", "Freddy", "Gabriel", "Gareth", "Gary", "Gavin",
        "Geoff", "Geoffrey", "George", "Gene", "Gerald", "Gerard", "Gerry", "Gervase",
        "Gilbert", "Godfrey", "Gordon", "Graeme", "Graham", "Grant", "Greg", "Gregor",
        "Gregory", "Gunter", "Gus", "Gustav", "Guy", "Garth", "Gideon", "Gil", "Giles",
        "Glenn", "Glynn", "Grover", "Hal", "Hans", "Harold", "Harry", "Harry", "Hector", "Henri",
        "Henry", "Henry", "Herb", "Herbert", "Herman", "Horatio", "Howard", "Hugh", "Hugh",
        "Hugo", "Hywel", "Hamish", "Hari", "Harlan", "Harvey", "Horace", "Huey", "Iain",
        "Ian", "Ira", "Isaac", "Ivor", "Isaak", "Jack", "Jake", "James", "James", "Jamie",
        "Jared", "Jason", "Jason", "Jasper", "Jay", "Jeff", "Jeffery", "Jeffrey", "Jeremy",
        "Jerome", "Jerry", "Jesse", "Jim", "Jimmy", "Joe", "Joel", "John", "Johnnie",
        "Johnny", "Jon", "Jonathan", "Jordan", "Jorge", "Joseph", "Josh", "Joshua", "Jude",
        "Julian", "Justin", "Jacob", "Jarvis", "Jimmie", "Joey", "Josef", "Karl", "Keith",
        "Ken", "Ken", "Kenneth", "Kenny", "Kevin", "Kieran", "Konrad", "Kurt", "Kyle",
        "Kelvin", "Kirk", "Lance", "Larry", "Laurence", "Lawrence", "Lee", "Len", "Lenard",
        "Leo", "Leon", "Leonard", "Lenny", "Les", "Lester", "Lewis", "Liam", "Linus", "Lionel",
        "Louis", "Lucian", "Lucien", "Luke", "Lennie", "Leonardo", "Lloyd", "Lou", "Louie",
        "Lucas", "Malcolm", "Marc", "Marcel", "Marcus", "Mario", "Mark", "Mark", "Martin",
        "Marvin", "Matt", "Mathew", "Matthew", "Maurice", "Max", "Melvin", "Melvyn", "Michael",
        "Mickey", "Mike", "Miles", "Magnus", "Marlon", "Marty", "Mick", "Mickie", "Micky",
        "Milo", "Morgan", "Morris", "Mort", "Mortimer", "Nathan", "Nathaniel", "Neal", "Ned",
        "Neil", "Nevil", "Neville", "Niall", "Nicholas", "Nick", "Nick", "Nicky", "Nigel",
        "Nino", "Norman", "Nelson", "Nicolas", "Noel", "Norm", "Oberon", "Oliver", "Omar",
        "Oscar", "Owen", "Otto", "Pablo", "Pat", "Patrick", "Paul", "Paulo", "Pavel", "Pete",
        "Peter", "Phil", "Philip", "Phillip", "Piers", "Patric", "Percy", "Quentin", "Rafael",
        "Ralph", "Ramsey", "Ray", "Ray", "Raymond", "Reece", "Rex", "Rhys", "Ric",
        "Richard", "Richard", "Richie", "Rick", "Rick", "Ricky", "Ritch", "Rob", "Rob",
        "Robert", "Robbie", "Robin", "Rod", "Roddie", "Roddy", "Roderick", "Rodger", "Rodney",
        "Rog", "Roger", "Roger", "Roland", "Rolf", "Rollo", "Ron", "Ronald", "Ronan", "Ronnie",
        "Rory", "Ross", "Roy", "Rudolf", "Rudy", "Rufus", "Rupert", "Russ", "Russell", "Ryan",
        "Ralf", "Reggie", "Reginald", "Rik", "Russel", "Sam", "Sam", "Samuel", "Sandy",
        "Saul", "Scott", "Seamus", "Sean", "Sebastian", "Seth", "Shane", "Shaun", "Shawn",
        "Siegfried", "Sid", "Sidney", "Sigmund", "Simon", "Stan", "Stanley", "Stephan",
        "Stephen", "Steve", "Steven", "Stuart", "Sylvester", "Sammy", "Silvester", "Spike",
        "Stefan", "Stewart", "Stu", "Ted", "Terence", "Terrence", "Terry", "Theo", "Theodore",
        "Thom", "Thomas", "Tim", "Tim", "Timothy", "Tobe", "Tobias", "Toby", "Todd", "Tom",
        "Tom", "Tommy", "Tony", "Travis", "Trevor", "Troy", "Valentine", "Victor", "Vince",
        "Vincent", "Vic", "Vick", "Vinnie", "Waldo", "Wallie", "Wally", "Walt", "Walter",
        "Warren", "Wayne", "Wilbur", "Wilf", "Wilfred", "Will", "William", "Willie", "Winston",
        "Woody", "William", "Wallace", "Wes", "Wesley", "Wyatt", "Xavier", "Yuri", "Zack",
        "Zak", "Zane",
        #new - journalists etc
        'Ambrose', 'Anders', 'Ant', 'Bo', 'Buck', 'Bud', 'Clint', 'Clinton',
        'Daryl', 'Delroy', 'Diego', 'Dimitri', 'Donal', 'Egon',
        'Enzo', 'Eoin', 'Ephraim', 'Ferdinand', 'Fernando', 'Hiram',
        'Humphrey', 'Ivan', 'Javier', 'Jean-Michel', 'Jenson',
        'Jermaine', 'Johann', 'Jose', 'Juan', 'Kieron', 'Leopold',
        'Luis', 'Manuel', 'Martyn', 'Mauricio', 'Miklos', 'Obadiah',
        'Olaf', 'Padraic', 'Paolo', 'Ridley', 'Stieg', 'Wendell',
        'Willi', 'Zaphod', 'Zebedee',
        #new - names derived from the 1990 US Census
        'Abdul', 'Ahmed', 'Alberto', 'Aldo', 'Alejandro', 'Alfonso',
        'Alfredo', 'Alonzo', 'Alphonse', 'Amos', 'Angelo', 'Antoine',
        'Armand', 'Armando', 'Art', 'Arturo', 'Aubrey', 'Aurelio',
        'Avery', 'Bart', 'Barton', 'Benito', 'Bert', 'Bradly',
        'Branden', 'Brent', 'Brett', 'Burl', 'Byron', 'Carlton',
        'Cary', 'Cedric', 'Cesar', 'Chad', 'Christian', 'Chuck',
        'Clarence', 'Clayton', 'Clement', 'Cletus', 'Clyde', 'Cody',
        'Cory', 'Cyrus', 'Dane', 'Dante', 'Darin', 'Darius', 'Darrel',
        'Darryl', 'Demetrius', 'Devon', 'Domingo', 'Doyle', 'Drew',
        'Dwain', 'Dwayne', 'Earl', 'Earnest', 'Eduardo', 'Elmo',
        'Elwood', 'Emmanuel', 'Enrique', 'Erwin', 'Esteban',
        'Faustino', 'Federico', 'Felipe', 'Fidel', 'Floyd', 'Foster',
        'Fredric', 'Fredrick', 'Freeman', 'Galen', 'Garfield',
        'Garry', 'Giuseppe', 'Gregg', 'Guillermo', 'Hank', 'Harley',
        'Hassan', 'Heath', 'Homer', 'Hubert', 'Hunter', 'Ignacio',
        'Irving', 'Isaiah', 'Ishmael', 'Isiah', 'Jamaal', 'Jarred',
        'Jefferey', 'Jefferson', 'Jeffry', 'Jeremiah', 'Jerrod',
        'Joaquin', 'Jonas', 'Jonathon', 'Jules', 'Julio', 'Julius',
        'Kareem', 'Kent', 'Kenton', 'Kris', 'Kristopher', 'Landon',
        'Leland', 'Lemuel', 'Leroy', 'Lonnie', 'Lorenzo', 'Luciano',
        'Luther', 'Lyle', 'Lyndon', 'Mack', 'Marcelo', 'Marco',
        'Marcos', 'Marshall', 'Maxwell', 'Miguel', 'Milton', 'Mitch',
        'Mohammad', 'Mohammed', 'Monty', 'Moses', 'Murray', 'Newton',
        'Noah', 'Norbert', 'Orlando', 'Orville', 'Otis', 'Pedro',
        'Perry', 'Pierre', 'Preston', 'Quincy', 'Quinn', 'Ramon',
        'Randall', 'Randolph', 'Raphael', 'Raul', 'Ricardo', 'Riley',
        'Robby', 'Roberto', 'Roman', 'Roscoe', 'Ruben', 'Rudolph',
        'Rusty', 'Salvador', 'Scot', 'Sergio', 'Seymour', 'Sheldon',
        'Sherman', 'Silas', 'Solomon', 'Sonny', 'Spencer', 'Sydney',
        'Tad', 'Teddy', 'Terrance', 'Terrell', 'Thad', 'Tod', 'Tomas',
        'Trent', 'Trey', 'Tristan', 'Tyler', 'Tyrell', 'Tyrone',
        'Tyson', 'Ulysses', 'Van', 'Vaughn', 'Vern', 'Vernon',
        'Vicente', 'Virgil', 'Vito', 'Wade', 'Walker', 'Werner',
        'Willard', 'Willis', 'Wilmer', 'Wilson', 'Wilton', 'Woodrow',
        'Zachariah', 'Zachary', 'Zachery'
                   )


# 1070 female first names.
female_firstnames = ("Abbey", "Abbie", "Abby", "Abigail", "Ada", "Adele", "Adelle",
        "Adrienne", "Agatha", "Aileen", "Aimee", "Alana", "Alanah", "Alanna",
        "Alannah", "Alexa", "Alexandra", "Alice", "Alicia", "Alisa", "Alison",
        "Alissa", "Allegra", "Allie", "Allison", "Allissa", "Ally",
        "Althea", "Alysa", "Alyson", "Alyssa", "Amanda", "Amber",
        "Amelia", "Amy", "Anabella", "Anabelle", "Anais", "Analise",
        "Anastasia", "Andrea", "Angela", "Angelica", "Angelina",
        "Angie", "Anita", "Ann", "Ann-Marie", "Anna", "Annabelle",
        "Anne", "Annette", "Annie", "Anthea", "Anthia", "Antonia",
        "Anya", "April", "Arabela", "Arabella", "Aretha", "Arleen",
        "Arlene", "Ashleigh", "Astrid", "Audrey", "Ava", "Averil",
        "Avis", "Avril", "Ayn", "Babs", "Barb", "Barbara", "Bea",
        "Beatrice", "Beatrix", "Becca", "Beckie", "Becky", "Belinda",
        "Bella", "Belle", "Bernadette", "Bernice", "Beryl", "Bess",
        "Bessie", "Bessy", "Beth", "Bethany", "Bettany", "Betty",
        "Bev", "Beverley", "Beverly", "Bianca", "Bonnie", "Brenda",
        "Bridget", "Brigette", "Brigid", "Brigit", "Brigitte",
        "Bronwen", "Bronwyn", "Brooke", "Caitlin", "Camila", "Camile",
        "Camilla", "Camille", "Candice", "Cara", "Carla", "Carlotta",
        "Carly", "Carmen", "Carol", "Carole", "Caroline", "Carolyn",
        "Carrie", "Cassandra", "Cassie", "Cate", "Cath", "Catharine",
        "Catherin", "Catherine", "Catheryn", "Cathie", "Cathleen",
        "Cathrine", "Cathryn", "Cathy", "Catriona", "Celia", "Celine",
        "Charleen", "Charlene", "Charlotte", "Cheryl", "Chloe",
        "Chris", "Chrissie", "Chrissy", "Christa", "Christianna",
        "Christina", "Christine", "Ciara", "Cindi", "Cindie", "Cindy",
        "Clair", "Claire", "Clara", "Clare", "Clarice", "Clarisa",
        "Clarissa", "Claudette", "Claudia", "Cleo", "Colette",
        "Colleen", "Collete", "Collette", "Connie", "Constance",
        "Coralie", "Cordelia", "Corine", "Corinne", "Corrine",
        "Corrinne", "Courtney", "Crissie", "Crissy", "Cristina",
        "Cybil", "Cyndi", "Cynthia", "Daisy", "Dana", "Dani",
        "Daniella", "Danielle", "Danni", "Daphne", "Daria", "Darla",
        "Darleen", "Darlene", "Davina", "Dawn", "Dayna", "Deanna",
        "Deb", "Debbi", "Debbie", "Deborah", "Dee", "Deirdre",
        "Delia", "Denise", "Desiree", "Diana", "Diane", "Dianna",
        "Dianne", "Dita", "Dona", "Donna", "Dora", "Doreen", "Doris",
        "Dorothy", "Dot", "Drusilla", "Edith", "Edwina", "Eileen",
        "Elaine", "Eleanor", "Elena", "Elinor", "Eliza", "Elizabeth",
        "Ella", "Elle", "Ellen", "Ellie", "Eloise", "Elsa", "Elspeth",
        "Emilia", "Emily", "Emma", "Enid", "Erica", "Erin", "Esme",
        "Estelle", "Esther", "Eunice", "Eva", "Eve", "Evelyn",
        "Faith", "Fatima", "Fay", "Faye", "Felicia", "Felicity",
        "Fiona", "Fionna", "Flora", "Florence", "Fran", "Frances",
        "Francesca", "Francine", "Francisca", "Gabrielle", "Gail",
        "Gale", "Gayle", "Gemma", "Genevieve", "Georgia", "Georgina",
        "Geraldine", "Geri", "Gillian", "Gina", "Ginger", "Glenda",
        "Gloria", "Glynis", "Grace", "Gracie", "Greta", "Gwen",
        "Gwendolen", "Gwendolin", "Gwendolyn", "Gwenn", "Hanna",
        "Hannah", "Harmony", "Harriet", "Hayley", "Hazel", "Heather",
        "Helen", "Helena", "Helga", "Hellen", "Hermione", "Hilary",
        "Hillary", "Hollie", "Holly", "Honor", "Hope", "Imogen",
        "Ingrid", "Irene", "Irina", "Iris", "Irma", "Isabel",
        "Isabella", "Isadora", "Isla", "Isobel", "Ivy", "Jackie",
        "Jacqueline", "Jade", "Jan", "Jancis", "Jane", "Janet",
        "Janice", "Janie", "Janine", "Janis", "Jasmin", "Jasmine",
        "Jayne", "Jean", "Jeanette", "Jenna", "Jennifer", "Jenny",
        "Jessica", "Jill", "Jillie", "Jilly", "Jo", "Joan", "Joanna",
        "Joanne", "Jocelyn", "Jodi", "Jodie", "Jody", "Jola", "Joni",
        "Josephine", "Josie", "Joy", "Joyce", "Judi", "Judie",
        "Judith", "Judy", "Julia", "Julie", "Juliet", "June",
        "Justine", "Kara", "Karen", "Kat", "Katarina", "Kate",
        "Katelyn", "Katerina", "Katey", "Kath", "Katharina",
        "Katharine", "Katharyn", "Katherine", "Kathleen", "Kathryn",
        "Kathy", "Katie", "Katrina", "Katy", "Kayleigh", "Kelly",
        "Keri", "Keridwen", "Kerri", "Kerrie", "Kerry", "Kim",
        "Kimberley", "Kimberly", "Kira", "Kirsten", "Kirstin",
        "Kirsty", "Kitty", "Krista", "Kristen", "Kristin", "Kym",
        "Lana", "Lara", "Laura", "Laurell", "Lauren", "Lauryn",
        "Lavinia", "Lea", "Leah", "Leanne", "Lee", "Leia", "Lela",
        "Lena", "Lesley", "Letitia", "Lidia", "Lila", "Lilian",
        "Lilith", "Lillian", "Lilly", "Lily", "Linda", "Lindi",
        "Lisa", "Lita", "Livia", "Liz", "Liza", "Lois", "Lola",
        "Loraine", "Loretta", "Lori", "Lorina", "Lorna", "Lorraine",
        "Lorren", "Lotte", "Lotti", "Lottie", "Louisa", "Louise",
        "Lucia", "Lucille", "Lucinda", "Lucy", "Luisa", "Lydia",
        "Lyla", "Lyn", "Lynette", "Lynn", "Lynne", "Maddy",
        "Madeleine", "Mae", "Maeve", "Maggi", "Maggie", "Maisie",
        "Maive", "Mandi", "Mandy", "Mara", "Marcela", "Marcella",
        "Marci", "Marcia", "Marcie", "Margaret", "Marge", "Margery",
        "Margot", "Margret", "Mari", "Maria", "Marian", "Marianne",
        "Marie", "Marilyn", "Marina", "Marion", "Marjorie",
        "Marjorie", "Marla", "Marleen", "Marlena", "Marlene",
        "Marsha", "Martha", "Martina", "Mary", "Maud", "Maureen",
        "Maxine", "May", "Meagan", "Meave", "Meg", "Megan", "Meghan",
        "Mel", "Melanie", "Melinda", "Melisa", "Melissa", "Melody",
        "Mia", "Michaela", "Michaella", "Michelle", "Millie", "Milly",
        "Mira", "Miranda", "Miriam", "Moira", "Mollie", "Molly",
        "Mona", "Monica", "Muriel", "Nadia", "Nadine", "Nancy",
        "Naomi", "Natalia", "Natalie", "Natallia", "Natallie",
        "Natalya", "Natasha", "Natasha", "Nell", "Nicci", "Nicola",
        "Nicole", "Nicolle", "Nikki", "Nina", "Noelle", "Nora",
        "Octavia", "Olga", "Olive", "Olivia", "Olympia", "Ophelia",
        "Page", "Paige", "Pam", "Pamela", "Pamella", "Pandora", "Pat",
        "Patricia", "Patsy", "Patti", "Paula", "Paulina", "Pauline",
        "Pearl", "Peggy", "Penelope", "Penny", "Peta", "Petra",
        "Philipa", "Philippa", "Phoebe", "Phylis", "Phyllis", "Pippa",
        "Polly", "Poppy", "Portia", "Priscilla", "Pru", "Rachel",
        "Rachel", "Ramona", "Raquel", "Rayna", "Rebecca", "Rebecca",
        "Rebekah", "Regan", "Rhea", "Rita", "Robbyn", "Roberta",
        "Robyn", "Rochelle", "Roisin", "Ros", "Rosa", "Rosalind",
        "Rosaline", "Rosamund", "Rose", "Rosemary", "Rosie", "Rowena",
        "Roxane", "Roxanne", "Roz", "Ruby", "Ruth", "Ruthie",
        "Sabina", "Sabrina", "Sadie", "Saffron", "Sally", "Samantha",
        "Sandi", "Sandie", "Sandra", "Sara", "Sarah", "Saskia",
        "Selena", "Selina", "Selma", "Serena", "Shannon", "Sharon",
        "Sheena", "Sheila", "Sherilyn", "Sheryl", "Shirley", "Shona",
        "Silvia", "Simone", "Sinead", "Siobhan", "Sofia", "Sonia",
        "Sonja", "Sonya", "Sophia", "Sophie", "Stacey", "Staci",
        "Stacy", "Stella", "Stephanie", "Sue", "Susan", "Susanna",
        "Susannah", "Susie", "Suzanne", "Suzi", "Suzie", "Sylvia",
        "Sylvie", "Tabitha", "Tama", "Tamara", "Tammy", "Tania",
        "Tanya", "Tara", "Tasha", "Tatiana", "Teena", "Teresa",
        "Teri", "Terri", "Tess", "Tessa", "Thelma", "Theresa",
        "Therese", "Tiffani", "Tiffany", "Tina", "Toni", "Tonia",
        "Tonya", "Tori", "Tracey", "Traci", "Tracy", "Tricia",
        "Trish", "Trisha", "Trudi", "Trudie", "Trudy", "Una",
        "Ursula", "Val", "Valentina", "Valerie", "Valerie", "Vanessa",
        "Vanessa", "Vera", "Veronica", "Vicki", "Vickie", "Vicky",
        "Victoria", "Vikki", "Vikky", "Violet", "Virginia", "Vita",
        "Vonda", "Wanda", "Wendi", "Wendy", "Wilma", "Yolanda",
        "Yvette", "Yvonne", "Zara", "Zoe",
        #new - journalists etc
        'Albertine', 'Angeline', 'Anjali', 'Anna-Marie', 'Annabel',
        'Antonella', 'Ashlee', 'Becka', 'Bettina', 'Bryony',
        'Candida', 'Carina', 'Chelsey', 'Cherie', 'Claudine',
        'Clemmie', 'Clodagh', 'Coleen', 'Colene', 'Dannii', 'Danuta',
        'Delphine', 'Dominique', 'Edina', 'Emiko', 'Emiliya', 'Fanny',
        'Flic', 'Freya', 'Frida', 'Ginni', 'Jacqui', 'Jemma',
        'Jennie', 'Julietta', 'Keeleigh', 'Kesia', 'Laurette',
        'Leonora', 'Lianne', 'Lisette', 'Lizzie', 'Lucrezia', 'Maia',
        'Margareta', 'Marietta', 'Matilda', 'Michiyo', 'Mina',
        'Morwenna', 'Nathalie', 'Norma', 'Patience', 'Prue',
        'Rafaela', 'River', 'Rowan', 'Sharlene', 'Sindy', 'Skye',
        'Stevie', 'Suzy', 'Tanith', 'Winifred',
        #new - names derived from the 1990 US Census
        'Adeline', 'Adriana', 'Agnes', 'Aida', 'Alberta',
        'Alexandria', 'Alexis', 'Alisha', 'Alma', 'Alva', 'Alyce',
        'Andria', 'Angelia', 'Angelique', 'Annamarie', 'Annetta',
        'Ariana', 'Ariel', 'Arline', 'Augusta', 'Aurelia', 'Aurora',
        'Bertha', 'Betsy', 'Bette', 'Bettie', 'Billie', 'Blanche',
        'Bobbi', 'Bonita', 'Brandi', 'Breanna', 'Briana', 'Brianna',
        'Brianne', 'Britney', 'Brittany', 'Carmela', 'Carmella',
        'Carolina', 'Casandra', 'Catrina', 'Cecelia', 'Cecile',
        'Cecilia', 'Celeste', 'Celestine', 'Celina', 'Charline',
        'Charmaine', 'Chelsea', 'Cheri', 'Christen', 'Christi',
        'Clementine', 'Consuelo', 'Cora', 'Corina', 'Daniela',
        'Danna', 'Debi', 'Debra', 'Deidra', 'Deidre', 'Delores',
        'Deloris', 'Demetria', 'Dina', 'Dionne', 'Dolores', 'Dorcas',
        'Edna', 'Eleanore', 'Elisabeth', 'Elise', 'Elma', 'Elnora',
        'Elouise', 'Elsie', 'Elvira', 'Erika', 'Estella', 'Ethel',
        'Etta', 'Eugenia', 'Eulalia', 'Evangeline', 'Felecia', 'Fern',
        'Freda', 'Freida', 'Frieda', 'Gabriela', 'Gabriella',
        'Georgiana', 'Gertrude', 'Ginny', 'Gladys', 'Gretchen',
        'Griselda', 'Hattie', 'Heidi', 'Helene', 'Henrietta', 'Hilda',
        'Ida', 'Imelda', 'Imogene', 'Isabelle', 'Jaclyn', 'Jacquelin',
        'Jacquelyn', 'Jaime', 'Jami', 'Jana', 'Janette', 'Janna',
        'Jeanine', 'Jeanne', 'Jeannette', 'Jena', 'Jenifer', 'Jerri',
        'Jesica', 'Jessie', 'Joelle', 'Jolene', 'Josette', 'Juana',
        'Juanita', 'Juli', 'Juliana', 'Julianne', 'Justina',
        'Kaitlin', 'Karin', 'Karla', 'Kathi', 'Kathie', 'Kathrine',
        'Kayla', 'Keisha', 'Kelli', 'Kendra', 'Kesha', 'Kristi',
        'Kristie', 'Kristina', 'Kristine', 'Kylie', 'Latonya',
        'Latoya', 'Laurel', 'Lauretta', 'Laurie', 'Lavern', 'Laverne',
        'Lenora', 'Leona', 'Leta', 'Leticia', 'Lilia', 'Liliana',
        'Lizette', 'Lolita', 'Lorena', 'Lorene', 'Louella', 'Lucila',
        'Lucile', 'Luella', 'Lula', 'Lynda', 'Mabel', 'Madeline',
        'Madelyn', 'Magda', 'Magdalena', 'Majorie', 'Malinda',
        'Malissa', 'Mamie', 'Manuela', 'Marcy', 'Margarita', 'Margie',
        'Margo', 'Marguerite', 'Mariana', 'Marianna', 'Maribel',
        'Marilynn', 'Marisa', 'Marisol', 'Marissa', 'Marta',
        'Marybeth', 'Maude', 'Mavis', 'Maya', 'Mellissa', 'Melodie',
        'Mercedes', 'Michele', 'Mildred', 'Mimi', 'Mindy', 'Minerva',
        'Minnie', 'Misti', 'Misty', 'Monika', 'Monique', 'Myra',
        'Nanette', 'Nellie', 'Nelly', 'Nettie', 'Nichole', 'Niki',
        'Nikita', 'Nita', 'Nola', 'Noreen', 'Ofelia', 'Patrica',
        'Patrice', 'Pattie', 'Patty', 'Paulette', 'Philomena',
        'Pilar', 'Pricilla', 'Rachael', 'Rachelle', 'Reba', 'Regina',
        'Rena', 'Renee', 'Rhoda', 'Rhonda', 'Rosalie', 'Rosalina',
        'Rosalyn', 'Rosanne', 'Rosario', 'Roselyn', 'Rosemarie',
        'Rosetta', 'Roxann', 'Roxanna', 'Roxie', 'Samatha', 'Shari',
        'Sheri', 'Sherri', 'Sondra', 'Stacie', 'Stefanie', 'Summer',
        'Susana', 'Susanne', 'Suzan', 'Suzanna', 'Suzette', 'Sybil',
        'Tami', 'Tammi', 'Tammie', 'Tessie', 'Tia', 'Tracie', 'Tyra',
        'Valarie', 'Valorie', 'Velma', 'Viola', 'Violeta', 'Whitney',
        'Winona'
                      )
all_firstnames = male_firstnames+female_firstnames

# 3069 surnames
surnames = ("D'Arcy", "D'Silva", "D'Soto", "D'Souza", "O'Brian", "O'Brien", "O'Connell",
     "O'Connor", "O'Donnell", "O'Donovan", "O'Farrell", "O'Flinn", "O'Grady", "O'Hara",
     "O'Hare", "O'Hea", "O'Keefe", "O'Leary", "O'Neal", "O'Neill", "O'Reilly",
     "O'Rourke", "O'Shea", "O'Sullivan", "O'Toole",
     'Abbot', 'Abbott', 'Abrams', 'Acheson', 'Acker', 'Ackland', 'Ackerman', 'Ackroyd',
     'Acland', 'Acton', 'Adair', 'Adam', 'Adams', 'Adamski', 'Adamson',
     'Adcock', 'Addison', 'Adkins', 'Adler', 'Agate', 'Aherne', 'Ainsworth',
     'Aitken', 'Alan', 'Albright', 'Alcock', 'Alcott', 'Alden', 'Aldington',
     'Aldred', 'Aldrich', 'Aldridge', 'Alexander', 'Allan', 'Allen', 'Allerton',
     'Allgood', 'Allison', 'Allman', 'Alston', 'Altman', 'Altmann', 'Alvarez',
     'Andersen', 'Anderson', 'Anderson', 'Anderton', 'Andress', 'Andrews',
     'Anson', 'Aniston', 'Appleby', 'Applegate', 'Appleyard', 'Archer', 'Arctor',
     'Arkin', 'Arkwright', 'Armitage', 'Armstrong', 'Armstrong', 'Arnold',
     'Arnott', 'Arundel', 'Ash', 'Ashbee', 'Ashberry', 'Ashbrook', 'Ashby',
     'Ashcroft', 'Ashdown', 'Asher', 'Asherman', 'Ashford', 'Ashton',
     'Ashwood-Smith', 'Astley', 'Astor', 'Atcheson', 'Atherton', 'Atkins',
     'Atkinson', 'Attenborough', 'Atwater', 'Auerbach', 'Austen', 'Austin',
     'Avery', 'Ayer', 'Ayers', 'Ayles', 'Ayre', 'Ayres', 'Aykroyd',
     'Babcock', 'Bachelor', 'Backhouse', 'Backus', 'Bacon', 'Badger',
     'Bagshaw', 'Bailes', 'Bailey', 'Bailis', 'Baines', 'Bains', 'Baird',
     'Baker', 'Baldridge', 'Baldwin', 'Ball', 'Ballantine', 'Ballard', 'Balmer',
     'Bancroft', 'Banks', 'Bankhead', 'Bannan', 'Bannister', 'Barber',
     'Barbour', 'Barclay', 'Barker', 'Barker', 'Barkley', 'Barlow', 'Barnaby',
     'Barnes', 'Barnett', 'Baron', 'Barr', 'Barris', 'Barraclough', 'Barrat', 'Barrett',
     'Barrie', 'Barrington', 'Barrows', 'Barry', 'Barrymore', 'Bartlett','Barton',
     'Bascombe', 'Basinger', 'Baskin', 'Bassett', 'Bateman', 'Bates', 'Bauer',
     'Baxendale', 'Baxter', 'Bayless', 'Baylis', 'Beach', 'Beal', 'Beale',
     'Beals', 'Beard', 'Beasley', 'Beaton', 'Beattie', 'Beattie-Hillier',
     'Beatty', 'Beck', 'Becke', 'Becker', 'Beckett', 'Beckham', 'Beckman',
     'Bedford', 'Begley', 'Belcher', 'Bell', 'Belling', 'Bennet', 'Bennett',
     'Benning', 'Benson', 'Bentley', 'Benton', 'Bergman', 'Bergstrom', 'Berkeley',
     'Berkley', 'Berry', 'Best', 'Bester', 'Bevan', 'Beveridge', 'Biggs',
     'Billings', 'Billingsley', 'Billington', 'Binns', 'Bingham', 'Birch', 'Bird',
     'Birkin', 'Bishop', 'Black', 'Blackburn', 'Blackwell', 'Blaine', 'Blair',
     'Blaire', 'Blake', 'Blakemore', 'Blount', 'Blunt', 'Blyth', 'Bolton',
     'Bond', 'Bonfield', 'Bonner', 'Bonneville', 'Bonney', 'Booker', 'Boone',
     'Booth', 'Boothman', 'Boothroyd', 'Boroughs', 'Boswell', 'Boswick', 'Bottomley',
     'Boucher', 'Bounds', 'Bourne', 'Bovey', 'Bowden', 'Bowen', 'Bowles', 'Bowman',
     'Bowyer', 'Box', 'Boyce', 'Boyd', 'Boyes', 'Boyle', 'Bradbury', 'Braddock',
     'Bradfield', 'Bradley', 'Bradshaw', 'Brady', 'Bragg', 'Braidwood', 'Bramson',
     'Brand', 'Brandon', 'Branigan', 'Braxton', 'Bray', 'Bremner', 'Brendon',
     'Brennan', 'Brennan', 'Brenner', 'Brent', 'Brett', 'Brewer', 'Brewster',
     'Brice', 'Bridges', 'Brierley', 'Briers', 'Briggs', 'Bristow', 'Britten',
     'Brock', 'Brodie', 'Bronson', 'Brooke', 'Brooker', 'Brookes', 'Brooks',
     'Brookshire', 'Brosnan', 'Brown', 'Browne', 'Browning', 'Brubaker', 'Bruce',
     'Brunner', 'Bryant', 'Bryson', 'Buchanan', 'Buckingham', 'Buckley', 'Buckner', 'Budd',
     'Bulmer', 'Burgess', 'Burke', 'Burnett', 'Burns', 'Burnside', 'Burr', 'Burrell',
     'Burrows', 'Burton', 'Bushell', 'Bushnell', 'Butcher', 'Butler', 'Butt',
     'Byers', 'Byrd', 'Byrne', 'Byrnes', 'Cable', 'Cade', 'Caine', 'Caines', 'Calder',
     'Caldwell', 'Callaghan', 'Callahan', 'Callander', 'Callard', 'Callow', 'Calloway',
     'Cameron', 'Campbell', 'Cane', 'Canning', 'Cannings', 'Cantor', 'Capes', 'Capshaw',
     'Carfax', 'Cargill', 'Carlin', 'Carling', 'Carlyle', 'Carpenter', 'Carr',
     'Carruthers', 'Carson', 'Carter', 'Cartwright', 'Carver', 'Casey', 'Cassidy',
     'Cavanagh', 'Cawley', 'Chalker', 'Chalmers', 'Chamberlain', 'Chambers',
     'Champion', 'Chapman', 'Charlton', 'Chase', 'Chester', 'Childs', 'Chisholm',
     'Christensen', 'Christie', 'Claiborne', 'Clairmont', 'Clancy', 'Clark', 'Clarke',
     'Clarkson', 'Clary', 'Clayton', 'Cleary', 'Clement', 'Clinton', 'Clooney',
     'Clough', 'Clysdale', 'Coade', 'Coates', 'Cobb', 'Cochran', 'Cochrane', 'Code',
     'Cody', 'Coe', 'Coen', 'Coffey', 'Cogan', 'Coghlan', 'Colbert', 'Colby', 'Cole',
     'Coleman', 'Coles', 'Collier', 'Collins', 'Colton', 'Coltrane', 'Compton',
     'Conley', 'Conlon', 'Connell', 'Connelly', 'Conners', 'Connery', 'Connolly',
     'Connor', 'Connors', 'Conolly', 'Conroy', 'Constable', 'Constantine', 'Conway',
     'Coogan', 'Cook', 'Cooke', 'Coombs', 'Cooper', 'Copeland', 'Copley', 'Corbett',
     'Corbin', 'Corbitt', 'Corcoran', 'Corrigan', 'Cosgrove', 'Costa', 'Costello',
     'Costelloe', 'Cottrell', 'Coudray', 'Cousins', 'Coverdale', 'Covington',
     'Cowdray', 'Cowdrey', 'Cowederoy', 'Cowley', 'Cox', 'Craig', 'Crane', 'Craven',
     'Crawford', 'Creswell', 'Crick', 'Crisp', 'Cromwell', 'Crook', 'Crookes',
     'Crosby', 'Cross', 'Crosswell', 'Crowe', 'Crowle', 'Crowley', 'Cruickshank',
     'Cullen', 'Cummings', 'Cunningham', 'Curran', 'Currie', 'Currier', 'Curry',
     'Curtis', 'Cusson', 'Dacre', 'Dahl', 'Dahlquist', 'Dale', 'Daley', 'Dallas', 'Dalloway',
     'Dalton', 'Dalrymple', 'Daly', 'Dalyell', 'Dalziel', 'Danforth', 'Daniell',
     'Daniels', 'Dare', 'Darling', 'Davenport', 'Davey', 'Davidson', 'Davies',
     'Davies', 'Davis', 'Davison', 'Davy', 'Dawkins', 'Dawson', 'Day', 'De Havilland',
     'Deakin', 'Dean', 'Decker', 'Delaney', 'Delefield', 'Demarco', 'Dempsey',
     'Dempster', 'Dempsy', 'Denis', 'Dennis', 'Dent', 'Denton', 'Derbyshire',
     'Desoto', 'Dickinson', 'Dickson', 'Digby', 'Dillard', 'Dillon', 'Dimbleby', 'Dixon',
     'Dobb', 'Dobbs', 'Docherty', 'Dodd', 'Dodds', 'Dodgson', 'Dodson', 'Doherty',
     'Dolan', 'Donaghue', 'Donahue', 'Donaldson', 'Donegan', 'Donnelly', 'Donovan',
     'Dormer', 'Dorrell', 'Dougherty', 'Douglas', 'Dowding', 'Dowling', 'Downes',
     'Downey', 'Doyle', 'Drake', 'Draper', 'Drew', 'Drewett', 'Drexler', 'Driscoll', 'Drummond',
     'Drury', 'Dryer', 'Duane', 'Duff', 'Duffy', 'Duke', 'Dunaway', 'Duncan', 'Dunn',
     'Dunne', 'Dyson', 'Eakins', 'Earl', 'Earle', 'East', 'Eastman', 'Easton', 'Eaton',
     'Edgerton', 'Edmonds', 'Edmondson', 'Edmunds', 'Edwards', 'Eggers', 'Eldridge',
     'Eldritch', 'Eliot', 'Eliott', 'Ellington', 'Elliot', 'Elliott', 'Ellis', 'Ellison',
     'Elms', 'Elrick', 'Emerson', 'Enfield', 'Ennion', 'Entwistle', 'Epstein', 'Ericson',
     'Erisman', 'Eugenius', 'Eustace', 'Evans', 'Eveleigh', 'Everard', 'Everett',
     'Everitt', 'Ewan', 'Ewer', 'Ewing', 'Eyre', 'Faber', 'Fahey', 'Fairbairn',
     'Fairchild', 'Fairclough', 'Fairfax', 'Falconer', 'Falkner', 'Fane', 'Faringdon',
     'Farley', 'Farmer', 'Farnham', 'Farnon', 'Farnsworth', 'Farquhar', 'Farr',
     'Farrell', 'Farrer', 'Ferris',  'Farrow', 'Faulkner', 'Fawcett', 'Fell', 'Ferguson',
     'Fergusson', 'Fiddian', 'Fidgeon', 'Field', 'Fielding', 'Fields', 'Finch',
     'Finch', 'Findlay', 'Finlay', 'Finn', 'Finnegan', 'Finney', 'Finnighan',
     'Firth', 'Fischer', 'Fisher', 'Fitzgerald', 'Fitzpatrick', 'Flaherty',
     'Flanagan', 'Flanders', 'Flannery', 'Flatley', 'Fleishman', 'Fleming', 'Fletcher', 'Flores',
     'Flower', 'Floyd', 'Flynn', 'Foale', 'Foley', 'Follett', 'Foot', 'Forbes',
     'Ford', 'Foreman', 'Forester', 'Forrester', 'Forster', 'Forsythe', 'Fortescue',
     'Fortey',  'Foss', 'Foster', 'Fothergill', 'Fowler', 'Fox', 'Franklin', 'Franks', 'Fraser',
     'Frasier', 'Frazier', 'Freeman', 'French', 'Frewer', 'Frink', 'Frobisher',
     'Frost', 'Fry', 'Fryer', 'Fulford', 'Fuller', 'Furnival',
     'Fussell', 'Gaffney', 'Gage', 'Gagnier', 'Gaines', 'Gale', 'Gallagher',
     'Galloway', 'Galt', 'Gant', 'Gardener', 'Gardiner', 'Gardner', 'Garland',
     'Garner', 'Garr', 'Garrard', 'Garrett', 'Garrod', 'Garton', 'Gates', 'Gaunt',
     'Gay', 'Gernsback', 'Geare', 'Gerard', 'Gere', 'Gibb', 'Gibbon', 'Gibbs',
     'Gibson', 'Gifford', 'Gilbert', 'Giles', 'Gillespie', 'Gilmour', 'Glenn',
     'Glover', 'Godard', 'Godber', 'Goddard', 'Godfrey', 'Godwin', 'Gomm',
     'Gooch', 'Goodman', 'Goodrich', 'Goodridge', 'Goodwin', 'Gordon', 'Gorman',
     'Goss', 'Gough', 'Gould', 'Gower', 'Gowers', 'Grade', 'Graham', 'Granger', 'Grant',
     'Graves', 'Gray', 'Grayson', 'Greaves', 'Green', 'Greenberg', 'Greene',
     'Greenham', 'Greenstreet', 'Greenway', 'Greer', 'Greig', 'Grieve', 'Griffith',
     'Griffiths', 'Grigg', 'Grimes', 'Grissom', 'Grogan', 'Grossman', 'Grover',
     'Groves', 'Gruber', 'Guest', 'Gurney', 'Guthrie', 'Gutteridge', 'Hackett', 'Hadley',
     'Haggard', 'Hahn', 'Haigh', 'Hailey', 'Hale', 'Haley', 'Hall', 'Halley',
     'Halliday', 'Halpin', 'Hamilton', 'Hammond', 'Hancock', 'Hannigan', 'Hanley',
     'Hann', 'Hansen', 'Hanson', 'Hardcastle', 'Hardin', 'Harding', 'Hardwick',
     'Hardy', 'Hargraves', 'Hargreaves', 'Harman', 'Harmon', 'Harper', 'Harriman',
     'Harrington', 'Harris', 'Harrison', 'Hart', 'Harte', 'Hartell', 'Hartley',
     'Hartman', 'Harvey', 'Harwood', 'Haskins', 'Hastings', 'Hatcher', 'Havelock',
     'Hawke', 'Hawker', 'Hawkes', 'Hawkins', 'Hawley', 'Hawthorne', 'Hay',
     'Hayden', 'Haydon', 'Hayes', 'Haynes', 'Hays', 'Hayward', 'Hazelton',
     'Hazlett', 'Hearn', 'Hearne', 'Heaton', 'Henderson', 'Hendricks', 'Hendricksen', 'Hennet',
     'Henry', 'Henshaw','Henson', 'Hepburn', 'Herbert', 'Hesketh', 'Heslop',
     'Hewett', 'Hewitt', 'Heyward', 'Hickman', 'Hicks', 'Higginbotham', 'Higgins',
     'Higginson', 'Highsmith', 'Hill', 'Hiller', 'Hillman', 'Hinchcliffe', 'Hinds',
     'Hirst', 'Hislop', 'Hitchcock', 'Hitchings', 'Hoag', 'Hobbs', 'Hobgood',
     'Hoch', 'Hodges', 'Hodgson', 'Hoff', 'Hoffman', 'Hoffmann', 'Hofmann',
     'Hogan', 'Hogg', 'Holcroft', 'Holden', 'Holland', 'Holman', 'Holmes',
     'Holness', 'Holt', 'Hook', 'Hooke', 'Hooper', 'Hope', 'Hopkins', 'Hopkirk',
     'Hopper', 'Horne', 'Hoskins', 'Howard', 'Howe', 'Howell', 'Howells',
     'Howes', 'Hubbard', 'Hudson', 'Hughes', 'Humphreys', 'Humphries', 'Hunt',
     'Hunter', 'Huntley', 'Hurd', 'Hurt', 'Hussey', 'Hutchinson', 'Hutton', 'Hyde',
     'Ibbetson', 'Impey', 'Ince','Ingersoll', 'Ingham', 'Inglis', 'Ingram',
     'Ingrams', 'Inkpen', 'Innes', 'Irvine', 'Irving', 'Irwin', 'Isaacs',
     'Isham', 'Ives', 'Jackett', 'Jackson', 'Jacobs', 'Jacobson', 'Jamison',
     'Jakes', 'James', 'Jameson', 'Jamison', 'Jansen', 'Janssen', 'Jarman',
     'Jarrott', 'Jarvis', 'Jay', 'Jefferson', 'Jeffries', 'Jenkin', 'Jenkins',
     'Jenkinson', 'Jenner', 'Jennings', 'Jensen', 'Jerrold', 'Jervis', 'Johannessen',
     'Johannsen', 'Johansen', 'Johanson', 'Johnsen', 'Johnson', 'Johnson', 'Johnston',
     'Johnstone', 'Jolliffe', 'Jones', 'Joplin', 'Jordan', 'Joyce', 'Judd',
     'Justice', 'Kahn','Kane', 'Kantor', 'Kaplan','Katz', 'Kaufman', 'Kauffman',
     'Kavanagh', 'Kay', 'Kean', 'Keane', 'Kearney', 'Kearns', 'Keating', 'Keaton',
     'Keats', 'Keel', 'Keeler', 'Keenan', 'Keene', 'Keith', 'Kelleher',
     'Keller', 'Kellerman', 'Kelley', 'Kelly', 'Kelso', 'Kemp', 'Kendall',
     'Kennedy', 'Kenny', 'Kent', 'Keogh', 'Kerr', 'Ketley', 'Kew',
     'Key', 'Keyes', 'Kidd', 'Kidd', 'Kiernan', 'Killegrew', 'Kimble',
     'King', 'Kinnersley', 'Kirby', 'Kirk', 'Kirkman', 'Kirton', 'Klein',
     'Kline', 'Knapp', 'Knappe', 'Knight', 'Knowles', 'Knox', 'Knutson',
     'Kochanski', 'Kogan', 'Kohl', 'Koontz', 'Korda', 'Kovacs', 'Kramer',
     'Kuhn', 'Kuhns', 'Kurton', 'Kurtz', 'Kyle', 'Lacy', 'Lafferty', 'Laine',
     'Laing', 'Laker', 'Lamb', 'Lamb', 'Lambert', 'Lamborn', 'Lamont',
     'Lancaster', 'Landers', 'Landon', 'Landry', 'Lane', 'Lang', 'Langdon',
     'Langford', 'Langley', 'Langton', 'Lansdale', 'Larkin', 'Larkins', 'Larsen',
     'Larson', 'Latham', 'Latimer', 'Lauder', 'Laughlin', 'Laughton', 'Laurence',
     'Laurent', 'Laurie', 'Lavigne', 'Law', 'Lawler', 'Lawless', 'Lawley', 'Lawn',
     'Lawrence', 'Lawrie', 'Lawson', 'Lay', 'Le Strange', 'Lea', 'Leader',
     'Leary', 'Lee', 'Leeson', 'Leggatt', 'Leibovitz', 'Leibowitz', 'Leigh',
     'Leighton', 'Lennon', 'Lennox', 'Lenox', 'Leslie', 'Lester', 'Lethbridge',
     'Levin', 'Levine', 'Lewellen', 'Lewis', 'Lightbody', 'Lindquist', 'Lindstrom',
     'Linklater', 'Lister', 'Livingston', 'Livingstone', 'Llewelyn', 'Llewellyn', 'Lloyd',
     'Locke', 'Locke', 'Lockhart', 'Lockwood', 'Lodge', 'Loftus', 'Logan', 'Lomas',
     'Lomax', 'Long', 'Lonsdale', 'Lord', 'Low', 'Lowe', 'Lucas', 'Lucas', 'Luckman',
     'Lumley', 'Lumsden', 'Lunn', 'Luscombe', 'Lye', 'Lynch', 'Lyons', 'MacDonald',
     'MacDowell', 'MacFadyen', 'MacGregor', 'MacGuire', 'Macdonald', 'Macgregor',
     'Macguire', 'Mackay', 'Mackenzie', 'Maclachlan', 'MacLachlan', 'MacLaine', 'Maclean',
     'Macleod', 'Macmillan', 'MacMurray', 'MacNee', 'MacReady', 'Mackintosh',
     'Macy', 'Maddox', 'Magnuson', 'Magnussen', 'Magnusson', 'Magrath', 'Maguire',
     'Mainwaring', 'Maitland', 'Makinson', 'Mallett', 'Mallory', 'Malone', 'Mandrake',
     'Mann', 'Manners', 'Manning', 'Mansel', 'Mansell', 'Manson', 'Marcus', 'Margulies',
     'Markham', 'Marks', 'Marlow', 'Marr', 'Marriott', 'Marsden', 'Marsh', 'Marshall',
     'Martin', 'Martin', 'Martinez', 'Mason', 'Massey', 'Masters', 'Masterton', 'Matheson',
     'Matthews', 'Maurice', 'McBride', 'McCammon', 'McCarthy', 'McCauley', 'McCloud',
     'McConnell', 'McCoy', 'McDonagh', 'McDonald', 'McDonough', 'McDougall', 'McGowan',
     'McGrath', 'McGregor', 'McIntyre', 'McKay', 'McKenzie', 'McLachlan', 'McLaren',
     'McLaughlin', 'McLean', 'McLean', 'McLeod', 'McMannus', 'McMillan', 'McNulty',
     'McPartland', 'McPhee', 'McReady', 'Mead', 'Meade', 'Menzies', 'Meriwether',
     'Merril', 'Methuen', 'Meynell', 'Miles', 'Millar', 'Miller', 'Milligan', 'Mills',
     'Milne', 'Minter', 'Minton', 'Mitchell', 'Molyneux', 'Montague', 'Monroe',
     'Montgomery', 'Moor', 'Moore', 'Moran', 'Morcant', 'Morgan', 'Morgunn',
     'Morris', 'Morrison', 'Mortimer', 'Morton', 'Morwood', 'Moss', 'Muir',
     'Munro', 'Murphy', 'Murray', 'Myers', 'Nairn', 'Napier', 'Nash',
     'Naughton', 'Neal', 'Neeson', 'Nelson', 'Neville', 'Newcome', 'Newell',
     'Newland', 'Newman', 'Newton', 'Nichols', 'Nichols', 'Nicolson', 'Nicholson',
     'Niven', 'Nixon', 'Nobbs', 'Nolan', 'Norman', 'Norris', 'Norton', 'Nugent',
     'Nunn', 'Nutter', 'Oakes', 'Oates', 'Offley', 'Oldfield', 'Oldham', 'Oldman',
     'Oldridge', 'Oldroyd', 'Oliphant', 'Oliver', 'Onions', 'Orlebar', 'Osborn',
     'Osborne', 'Osbourne', 'Osmond', 'Owen', 'Owens', 'Pack', 'Page', 'Paige',
     'Paine', 'Palmer', 'Palmer', 'Pankhurst', 'Pargiter', 'Parker', 'Parnell',
     'Parrot', 'Parry', 'Parsons', 'Paterson', 'Patterson', 'Payne', 'Paxton',
     'Peake', 'Pearce', 'Pearson', 'Peck', 'Penn', 'Penrose', 'Peppard', 'Pepper',
     'Percival', 'Percy', 'Perkins', 'Perry', 'Peters', 'Peterson', 'Pettit',
     'Peverell', 'Philips', 'Phillips', 'Pickering', 'Pickford', 'Pickles',
     'Pierce', 'Pike', 'Pilgrim', 'Piper', 'Platt', 'Plummer', 'Polkington', 'Pole',
     'Pollard', 'Poole', 'Porter', 'Portman', 'Potter', 'Potts', 'Powell', 'Power',
     'Pratt', 'Preston', 'Price', 'Priest', 'Priestley', 'Probert', 'Proctor', 'Pryce',
     'Pugh', 'Purvis', 'Quaid', 'Quale', 'Quartermain', 'Quayle', 'Quin', 'Quincey',
     'Quinn', 'Quintin', 'Radcliffe', 'Rafferty', 'Ramsay', 'Ramsbotham',
     'Ramsbottom', 'Ramsey', 'Randal', 'Randall', 'Randle', 'Ray', 'Read',
     'Redgrave', 'Reece', 'Reed', 'Rees', 'Reeves', 'Regan', 'Reid', 'Reilly',
     'Reiss', 'Reynolds', 'Rhodes', 'Rice', 'Rich', 'Richards', 'Richardson', 'Rider',
     'Riley', 'Ritchie', 'Rivera', 'Roberts', 'Robertson', 'Robbins', 'Robinson',
     'Rockwell', 'Rogers', 'Rose', 'Rooney', 'Ross', 'Roth', 'Row', 'Rowntree',
     'Ruskin', 'Russell', 'Rutherford', 'Ryan', 'Ryder', 'Sackville',
     'Sadler', 'Sales', 'Sallis', 'Salmond', 'Salomon', 'Salter', 'Sammonds',
     'Sampson', 'Sanders', 'Sandoval', 'Sands', 'Sargent', 'Saunders', 'Savile',
     'Sawyer', 'Saxton', 'Sayle', 'Schofield', 'Scott', 'Scully', 'Seagrave',
     'Sellars', 'Sewell', 'Seymour', 'Sharman', 'Sharwood', 'Sharpe', 'Shaw',
     'Shea', 'Shelton', 'Shepard', 'Shepherd', 'Short', 'Simmons', 'Simpson',
     'Sinclair', 'Singer', 'Skinner', 'Slater', 'Sloman', 'Smedley', 'Smith',
     'Smithee', 'Smythe', 'Snow', 'Somerville', 'Sparke', 'Spencer', 'Spencer', 'Spinks', 'Spinoza',
     'Spooner', 'Stacey', 'Standish', 'Stanhope', 'Stanley', 'Steele', 'Steiner', 'Stephens',
     'Stevens', 'Stevenson', 'Stewart', 'Stibson', 'Stoker', 'Stone', 'Stoppard',
     'Stranger', 'Strong', 'Stuart', 'Stubbs', 'Sullivan', 'Summers', 'Sutcliffe',
     'Sutherland', 'Sutton', 'Swan', 'Sweeney', 'Swift', 'Sykes', 'Symonds',
     'Taine', 'Tait', 'Tate', 'Taylor', 'Telfer', 'Telford', 'Tempest',
     'Temple', 'Tennant', 'Thaw', 'Thomas', 'Thompson', 'Thomson', 'Thorn', 'Thorne',
     'Thornton', 'Thorpe', 'Thurlow', 'Tindall', 'Todd', 'Todhunter', 'Tomkinson',
     'Tomlinson', 'Townsend', 'Townsley', 'Tracy', 'Travers', 'Tremaine', 'Trelawney', 'Trumbull',
     'Tucker', 'Tucker', 'Tunbridge', 'Turnbull', 'Turner', 'Turvey', 'Tyler',
     'Tynan', 'Underhill', 'Underwood', 'Upjohn', 'Upton', 'Usher', 'Valentine',
     'Vane', 'Vassal', 'Vaughan', 'Vaughn', 'Vavasour', 'Venables', 'Vernon',
     'Vickers', 'Villiers', 'Von Braun', 'von Bronckhorst', 'Voss', 'Vyner', 'Wade', 
     'Wadham', 'Wagner', 'Wagstaff', 'Waite', 'Wakeman', 'Walker', 'Wallace', 'Waller',
     'Wallis', 'Walsh', 'Walters', 'Walton', 'Ward', 'Warner', 'Warren', 'Warwick',
     'Waters', 'Watkins', 'Watson', 'Watt', 'Watts', 'Weaver', 'Webb', 'Webb', 'Webber',
     'Weber', 'Webster', 'Welch', 'Weller', 'Wells', 'Wentworth', 'Wesley',
     'West', 'Westbrook', 'Westbrooke', 'Westmore', 'Weston', 'Wheeler', 'Whelan',
     'Whitaker', 'White', 'Whitfield', 'Whitney', 'Wier', 'Wilder', 'Wilkinson',
     'Williams', 'Williamson', 'Willis', 'Wilson', 'Winn', 'Winslow', 'Winter',
     'Winterson', 'Wise', 'Wiseman', 'Witherspoon', 'Witt', 'Wood', 'Woods',
     'Woodward', 'Wooley', 'Worcester', 'Wright', 'Wyatt', 'Wyndham',
     'Yale', 'Yarborough', 'Yates', 'Yaxley', 'Yeo', 'Yeoman', 'York',
     'Youel', 'Youle', 'Young', 'Younger', 'Yule', 'Zachary', 'Zouche',
     #new - journalists,  pirates, fiction etc
     'Aaronovitch', 'Aldrick', 'Allen-Mills', 'Allsopp', 'Altmeyer',
     'Arbuckle', 'Armitstead', 'Bagshawe', 'Baillie', 'Baldrick',
     'Barrow', 'Batty', 'Bayer', 'Bearman', 'Beaumont', 'Beckenbauer',
     'Beckford', 'Bellamy', 'Bentham', 'Berlowitz', 'Bernays',
     'Betts', 'Billingham', 'Blackadder', 'Blacker', 'Blanchflower',
     'Bleakley', 'Blenkinsop', 'Bloom', 'Bloomfield', 'Blunkett',
     'Borgia', 'Boulton', 'Bower', 'Bracchi', 'Branagan', 'Brignall',
     'Brogan', 'Brough', 'Buchan', 'Buckland', 'Bullmore', 'Buncombe',
     'Burchill', 'Burleigh', 'Burnham', 'Button', 'Bywater',
     'Cacciola', 'Cainer', 'Caldecott', 'Campion', 'Cardella',
     'Carey', 'Carmichael', 'Carville', 'Cauchi', 'Cavazza',
     'Cavendish', 'Chang', 'Charlton-Weedy', 'Churchill', 'Chynoweth',
     'Ciancio', 'Clare', 'Clifton', 'Cockburn', 'Cohen', 'Conaghan',
     'Coney', 'Conner', 'Cookney', 'Copping', 'Copps', 'Cordeiro',
     'Corugedo', 'Coughlin', 'Cradock', 'Creasey', 'Creighton',
     'Crichton', 'Crippen', 'Croft', 'Cryer', 'Cumberbatch',
     'Cumming', 'Cunningham-Reid', 'Dade', 'Dadswell', 'Dawe',
     'Dawes', 'Derham', 'Devine', 'Dewar', 'Dimmock', 'Dobson',
     'Dorfman', 'Drogba', 'Duckworth', 'Dunkerley', 'Dunkley',
     'Durston', 'Duval', 'Dyke', 'Eccles', 'Eddy',
     'Edgecliffe-Johnson', 'Egan', 'Ehrlich', 'Elkins', 'Engel',
     'English', 'Espinosa', 'Espinoza', 'Estridge', 'Etheridge',
     'Evans-Pritchard', 'Fagan', 'Falkes', 'Fallowfield', 'Fandino',
     'Feltz', 'Fenby', 'Fennell', 'Fernandez', 'Finnigan',
     'Flamsteed', 'Flashman', 'Fowles', 'Foxwell', 'Frankel',
     'Freedland', 'Freud', 'Fricker', 'Furillo', 'Gallacher', 'Gallo',
     'Garrahan', 'Gascoyne', 'Gaskin', 'Geffen', 'Gelles', 'Gerken',
     'Gersen', 'Gilchrist', 'Gill', 'Gillan', 'Glancey', 'Godson',
     'Goff', 'Golding', 'Gormley', 'Gosling', 'Grainge', 'Grainger',
     'Greenslade', 'Grey', 'Grytpipe-Thynne', 'Gyllenhaal', 'Hague',
     'Halligan', 'Hanbury', 'Hanlon', 'Hart-Davis', 'Haslam',
     'Hattersley', 'Hazell', 'Hazlehurst', 'Heckmondwike', 'Hegarty',
     'Hendy', 'Hennigan', 'Herne', 'Hilton', 'Hiscott', 'Hitchens',
     'Hobsbawm', 'Hodgkinson', 'Hoey', 'Holliday', 'Hollingshead',
     'Horton', 'Hossain', 'Hoyle', 'Huckabee', 'Huggins', 'Huhne',
     'Humphrys', 'Hurst', 'Janacek', 'Jardine', 'Jarre', 'Jellicoe',
     'Kahlo', 'Keegan', 'Kelsey', 'Kerrigan', 'Kerwin', 'Kidd',
     'Kinsella', 'Kirtley', 'Knibb', 'Koltrowitz', 'Kruger',
     'Larsson', 'Laverne', 'Lawton', 'Leahy', 'Legg', 'Legge',
     'Leith', 'Leonard', 'Leroux', 'Lessing', 'Letts', 'Liddle',
     'Lightfoot', 'Lineker', 'Linge', 'Littlejohn', 'Lovatt',
     'Luyten', 'Lyle', 'Lyndon', 'Lyttelton', 'Lytton', 'MacArthur',
     'MacAskill', 'MacDonell', 'MacFarlane', 'MacGinty', 'MacIntyre',
     'MacManus', 'MacRae', 'Macfarlane', 'Macrae', 'Maddock',
     'Maddocks', 'Manville', 'Mascherano', 'Mayhew', 'McAlonan',
     'McAlpine', 'McAuley', 'McCabe', 'McColm', 'McGahey', 'McGarret',
     'McGuinness', 'McInerney', 'McKessick', 'McKinstry',
     'McKittrick', 'McNab', 'McPartlin', 'McQuillan', 'McSmith',
     'McVeigh', 'Mellon', 'Merrick', 'Meyer', 'Midgley', 'Minogue',
     'Mizuki', 'Moir', 'Monaghan', 'Monbiot', 'Moncrieff',
     'Montagu-Smith', 'Moodie', 'Moore-Bridger', 'Morgan', 'Morley',
     'Moxley', 'Mulholland', 'Murrison', 'Murtagh', 'Mychasuk',
     'Nakamoto', 'Nevin', 'Nicks', "O'Callaghan", 'Odone', 'Ogg',
     'Ogilvy', 'Orr', 'Otway', 'Packer', 'Pagano', 'Pagnamenta',
     'Panton', 'Paphides', 'Parke', 'Partridge', 'Pasternak', 'Patel',
     'Paton', 'Pellegrini', 'Pellegrino', 'Pelling', 'Pereira',
     'Pitman', 'Plumridge', 'Pollitt', 'Ponting', 'Poulter',
     'Prestridge', 'Prince', 'Pringle', 'Prosser', 'Pryer', 'Prynn',
     'Purdie', 'Quigley', 'Quirke', 'Rasmussen', 'Reitman', 'Rentoul',
     'Rigby', 'Rimmer', 'Robins', 'Roddick', 'Rodriguez', 'Roebuck',
     'Ronay', 'Rothman', 'Rothschild', 'Rothwell', 'Rowley', 'Rudd',
     'Ruddick', 'Rumbelow', 'Rumbold', 'Sanderson', 'Sants',
     'Saramago', 'Savage', 'Scargill', 'Schmid', 'Schulz',
     'Scott-Fowler', 'Scurr', 'Seagoon', 'Seyfried', 'Shannon',
     'Sharapova', 'Sheppard', 'Sherwood', 'Shipman', 'Shreeve',
     'Siegle', 'Siggerson', 'Silva', 'Simonian', 'Singleton',
     'Smellie', 'Smithers', 'Solman', 'Sorrell', 'Southgate',
     'Spadger', 'Spall', 'Spanier', 'Spiro', 'Springer', 'Stanford',
     'Stephen', 'Stephenson', 'Stevenson', 'Stock', 'Stocks',
     'Strachan', 'Strauss', 'Street-Porter', 'Stringer', 'Sutterby',
     'Tappin', 'Teach', 'Tebbit', 'Templeton', 'Tenison', 'Terazono',
     'Thornhill', 'Tickle', 'Timmins', 'Titchen', 'Tobin', 'Tong',
     'Torrance', 'Torres', 'Trapp', 'Trimingham', 'Trotsky', 'Tully',
     'Tweedie', 'Usborne', 'Vance', 'Venner', 'Vetter', 'Vidalon',
     'Villa', 'Vranica', 'Waddle', 'Waghorne', 'Walden', 'Wang',
     'Waterhouse', 'Watters', 'Weiss', 'Wheatcroft', 'Wheatley',
     'Whittle', 'Wilce', 'Wild', 'Wilkie', 'Winfield', 'Winterton',
     'Wolpert', 'Wong', 'Wylie', 'Zagzoule', 'Zanelli', 'Zapatero',
     'Zarkov', 'Ziemer', 'Ziermer',
     'Ogg', 'Wetherwax', 'Ridcully', 'Beeblebrox',
     #new - names derived from the 1990 US Census
     'Albertson', 'Alderman', 'Alford', 'Ames', 'Andersen', 'Bachman',
     'Baptiste', 'Bartley', 'Batista', 'Baum', 'Beauchamp',
     'Beckwith', 'Beltran', 'Benedict', 'Berg', 'Berger', 'Berman',
     'Biddle', 'Bigelow', 'Blakely', 'Blalock', 'Blodgett', 'Blum',
     'Bock', 'Boggs', 'Bonds', 'Borges', 'Bowens', 'Bowers', 'Bowie',
     'Boyer', 'Braden', 'Bradford', 'Brandt', 'Braun', 'Brinkley',
     'Broderick', 'Broughton', 'Brumfield', 'Brunson', 'Buford',
     'Bullock', 'Bunn', 'Burch', 'Burden', 'Burroughs', 'Busch',
     'Bush', 'Cady', 'Cain', 'Calhoun', 'Calvert', 'Calvin', 'Cannon',
     'Cantrell', 'Cardwell', 'Carlson', 'Carter-Brown', 'Cash',
     'Castaneda', 'Castillo', 'Castro', 'Cates', 'Cato', 'Cave',
     'Cervantes', 'Chadwick', 'Chan', 'Chance', 'Chandler', 'Chaney',
     'Chappell', 'Chavez', 'Chen', 'Cheney', 'Chester-Page',
     'Childress', 'Chin', 'Cho', 'Choi', 'Chow', 'Christenson',
     'Christiansen', 'Christopher', 'Church', 'Clark-Taylor',
     'Clemens', 'Clements', 'Cleveland', 'Cline', 'Cobbs', 'Coburn',
     'Cockrell', 'Coker', 'Colburn', 'Combs', 'Comstock', 'Condon',
     'Cooley', 'Cope', 'Cornelius', 'Cornell', 'Cornish', 'Cornwell',
     'Cortes', 'Cortez', 'Cotton', 'Coulter', 'Courtney', 'Cowan',
     'Cowart', 'Crabtree', 'Cramer', 'Crocker', 'Crouch', 'Custer',
     'Cutler', 'Dailey', 'Danielson', 'Danner', 'Darby', 'Darnell',
     'Delacruz', 'Delgado', 'Denham', 'Devries', 'Dewey', 'Dewitt',
     'Dexter', 'Dickens', 'Dickerson', 'Dominguez', 'Dorn', 'Dorsey',
     'Dowd', 'Downing', 'Driver', 'Dubois', 'Dunbar', 'Dupont',
     'Duran', 'Durant', 'Durham', 'Dutton', 'Duvall', 'Dwyer', 'Dyer',
     'Eaves', 'Ebert', 'Elias', 'Engle', 'Erickson', 'Escobar',
     'Estrada', 'Fairbanks', 'Falk', 'Farris', 'Faulk', 'Feldman',
     'Fernandes', 'Fink', 'Finley', 'Fisk', 'Flood', 'Flowers',
     'Fogle', 'Foote', 'Forman', 'Forrest', 'Forsyth', 'Fort',
     'Forte', 'Fortune', 'Fournier', 'Franco', 'Friedman', 'Frye',
     'Fuentes', 'Fulton', 'Funk', 'Garcia', 'Garrison', 'Gaskins',
     'Gaston', 'Geiger', 'Gentry', 'Gerber', 'Gibbons', 'Gillette',
     'Gilliam', 'Gillis', 'Gilmore', 'Giordano', 'Givens', 'Glass',
     'Gleason', 'Goldberg', 'Goldman', 'Goldstein', 'Gomez',
     'Gonzales', 'Gonzalez', 'Goode', 'Goodson', 'Gore', 'Gossett',
     'Grady', 'Grantham', 'Greenfield', 'Greenwood', 'Gresham',
     'Grier', 'Griffin', 'Griggs', 'Grimm', 'Grooms', 'Grove',
     'Grubb', 'Grubbs', 'Guerrero', 'Guevara', 'Gunn', 'Haas',
     'Hacker', 'Haines', 'Hampton', 'Hanks', 'Hannon', 'Hargrove',
     'Harley', 'Harlow', 'Hatch', 'Hathaway', 'Hawks', 'Haywood',
     'Healy', 'Heath', 'Helms', 'Hendrick', 'Hendrickson', 'Hendrix',
     'Hernandez', 'Herron', 'Hess', 'Hester', 'Hickey', 'Hightower',
     'Hildebrand', 'Hills', 'Hines', 'Hodge', 'Holbrook', 'Holcomb',
     'Holder', 'Hollins', 'Holm', 'Honeycutt', 'Hood', 'Hooker',
     'Horn', 'Horner', 'Houser', 'Hoyt', 'Huang', 'Huffman', 'Hummel',
     'Hunter-Thompson', 'Hurley', 'Hutcherson', 'Hutchins',
     'Hutchison', 'Hutson', 'Hyatt', 'Inman', 'Iverson',
     'Jackson-Carter', 'Jacobsen', 'Jarrett', 'Jeter', 'Jett',
     'Jewell', 'Jimenez', 'Johnson-Mann', 'Jolly', 'Judge', 'Kang',
     'Karr', 'Keeton', 'Kellogg', 'Kendrick', 'Kilgore', 'Kilpatrick',
     'Kinsey', 'Kirkpatrick', 'Koch', 'Kohler', 'Kraft', 'Kraus',
     'Krause', 'Lacey', 'Laird', 'Lake', 'Landis', 'Lanier',
     'Lankford', 'Lassiter', 'Lear', 'Leblanc', 'Ledbetter',
     'Lehmann', 'Lindberg', 'Littlefield', 'Lloyd-Gardner', 'Lockett',
     'Lombardo', 'Lopez', 'Lorenz', 'Lorenzo', 'Lott', 'Lovelace',
     'Lovell', 'Lovett', 'Luckett', 'Lund', 'Lundy', 'Madden',
     'Madison', 'Madsen', 'Magee', 'Mahoney', 'Majors', 'Malloy',
     'Mansfield', 'Marin', 'Marquez', 'Mathis', 'Matlock', 'Maxwell',
     'Mayer', 'Mayes', 'Mayfield', 'Maynard', 'Maynard-Ramos', 'Mayo',
     'Mays', 'McAdams', 'McAlister', 'McAllister', 'McBride',
     'Mcbride-Bradley', 'Mccain', 'Mccain-Saunders', 'McCall',
     'McCann', 'McCarthy', 'McCartney', 'McCarty', 'McCormack',
     'McCormick', 'McCoy', 'McCracken', 'McDermott', 'McDonald',
     'McDowell', 'McFadden', 'McFarland', 'McGee', 'McGill',
     'McGinnis', 'McGowan', 'McGrath', 'McGraw', 'McGrew', 'McGuire',
     'McIntire', 'McIntosh', 'McIntyre', 'McKay', 'McKenna',
     'McKenzie', 'McKinley', 'McKinnon', 'McLean', 'McLeod',
     'McMahon', 'McMillan', 'McMillian', 'McMullen', 'McNally',
     'McNamara', 'McNeal', 'McNeil', 'McNeill', 'McNulty',
     'McPherson', 'McRae', 'McWilliams', 'Meadows', 'Medeiros',
     'Meeks', 'Melendez', 'Melton', 'Mendez', 'Mendoza', 'Mercer',
     'Merchant', 'Meyers', 'Michaels', 'Middleton', 'Milton',
     'Molina', 'Monson', 'Montanez', 'Montoya', 'Moody', 'Mooney',
     'Morales', 'Moreau', 'Moreland', 'Moreno', 'Morrow', 'Moseley',
     'Mosley', 'Motley', 'Mott', 'Moya', 'Mueller', 'Mullen',
     'Muller', 'Mulligan', 'Mullins', 'Muniz', 'Munoz', 'Murillo',
     'Navarro', 'Naylor', 'Nesbitt', 'Nettles', 'Neumann', 'Newcomb',
     'Newsom', 'Newsome', 'Ng', 'Nguyen', 'Nielsen', 'Noble', 'Nolen',
     'North', 'Norwood', 'Nowak', 'Oakley', "O'Brien", "O'Connell",
     "O'Connor", "O'Donnell", 'Ogden', "O'Keefe", "O'Leary",
     'Olivares', 'Olsen', 'Olson', "O'Neal", "O'Neil", "O'Neill",
     'Ortega', 'Ortiz', "O'Toole", 'Overton', 'Padgett', 'Painter',
     'Parker-Brennan', 'Parks', 'Parrish', 'Parson', 'Patton',
     'Paulsen', 'Paulson', 'Payton', 'Peacock', 'Pease', 'Peebles',
     'Pendleton', 'Pennington', 'Peoples', 'Perez', 'Perryman',
     'Peterman', 'Petersen', 'Petty', 'Phelps', 'Phipps', 'Pickens',
     'Pickett', 'Pierson', 'Pinto', 'Pittman', 'Pitts', 'Plunkett',
     'Poe', 'Polk', 'Pollock', 'Portillo', 'Powers', 'Prescott',
     'Presley', 'Pritchard', 'Pritchett', 'Pryor', 'Puente',
     'Purcell', 'Putnam', 'Pyle', 'Quick', 'Quintero', 'Radford',
     'Raines', 'Ramirez', 'Rankin', 'Rawlings', 'Reagan', 'Reardon',
     'Redmond', 'Reese', 'Reis', 'Reyes', 'Ricci', 'Ricketts', 'Rico',
     'Riddle', 'Rigsby', 'Rinehart', 'Ritter', 'Rivas', 'Rivers',
     'Roach', 'Rocha', 'Roche', 'Rodgers', 'Rodrigues', 'Roe',
     'Rollins', 'Romano', 'Romero', 'Roper', 'Rosado', 'Rosales',
     'Rosario', 'Rosen', 'Rosenberg', 'Rossi', 'Rouse', 'Rowe',
     'Rowell', 'Rowland', 'Rubin', 'Rubio', 'Ruffin', 'Ruiz',
     'Runyon', 'Rush', 'Russo', 'Rutledge', 'Saenz', 'Salazar',
     'Samson', 'Sanchez', 'Sanford', 'Santana', 'Santiago', 'Santos',
     'Santos-Brown', 'Scanlon', 'Schaefer', 'Schaeffer', 'Schilling',
     'Schmidt', 'Schmitt', 'Schneider', 'Schroeder', 'Schultz',
     'Schwartz', 'Scroggins', 'Sears', 'Self', 'Sellers', 'Seward',
     'Sexton', 'Shafer', 'Shaffer', 'Shanks', 'Shapiro', 'Sharp',
     'Shearer', 'Shelby', 'Sheldon', 'Sherman', 'Shields', 'Shultz',
     'Siegel', 'Silver', 'Simms', 'Simons', 'Simpkins', 'Singh',
     'Skelton', 'Slade', 'Sloan', 'Slocum', 'Smalls', 'Smallwood',
     'Snell', 'Snider', 'Snodgrass', 'Snowden', 'Snyder', 'Sorensen',
     'Sorenson', 'Soto', 'Sousa', 'South', 'Souza', 'Sowell',
     'Sowers', 'Sparks', 'Spaulding', 'Speer', 'Spence', 'Spicer',
     'Sprague', 'Squires', 'Stafford', 'Stahl', 'Stallings',
     'Stallworth', 'Stanfield', 'Stanton', 'Staples', 'Stapleton',
     'Stark', 'Starkey', 'Starr', 'Stearns', 'Steen', 'Stein',
     'Sterling', 'Stiles', 'Stinson', 'Stoddard', 'Stokes', 'Storey',
     'Stovall', 'Strand', 'Strange', 'Stratton', 'Street', 'Streeter',
     'Strickland', 'Strother', 'Stuckey', 'Suarez', 'Suggs', 'Sumner',
     'Swafford', 'Swain', 'Swann', 'Swanson', 'Swenson', 'Sykes-Fox',
     'Tackett', 'Taft', 'Talbot', 'Tan', 'Tang', 'Tanner', 'Tatum',
     'Tavares', 'Taylor-Brown', 'Terrell', 'Thurman', 'Thurston',
     'Tillman', 'Tipton', 'Tisdale', 'Toler', 'Trammell', 'Tran',
     'Travis', 'Trent', 'Trevino', 'Trimble', 'Tripp', 'Trotter',
     'Troutman', 'Truitt', 'Trujillo', 'Truong', 'Tubbs', 'Tuttle',
     'Tyson', 'Unger', 'Valdes', 'Valdez', 'Varela', 'Vargas',
     'Vasquez', 'Vazquez', 'Velasquez', 'Ventura', 'Vidal', 'Vines',
     'Vogel', 'Waddell', 'Wadsworth', 'Waldron', 'Washburn',
     'Washington', 'Waterman', 'Weeks', 'Weir', 'Wendt',
     'Westmoreland', 'Whaley', 'Wharton', 'Whitehead', 'Whiting',
     'Whittington', 'Wicks', 'Wiggins', 'Wilcox', 'Wiley', 'Wilkes',
     'Wilkins', 'Wilks', 'Willett', 'Willey', 'Willingham', 'Willson',
     'Wing', 'Winkler', 'Winters', 'Withers', 'Wolf', 'Wolfe',
     'Wolff', 'Womack', 'Woodall', 'Woodard', 'Woodcock', 'Woodson',
     'Worrell', 'Worthington', 'Wray', 'Wu', 'Wyman', 'Wynn',
     'Yancey', 'Yang', 'Yang-Rivera', 'Yeager', 'Zapata', 'Zeigler',
     'Ziegler', 'Zielinski', 'Zimmer', 'Zimmerman',
     'Aquino', 'Baez', 'Batchelor', 'Bean', 'Benitez', 'Binder',
     'Blackman', 'Bledsoe', 'Breen', 'Bullard', 'Bundy', 'Callaway',
     'Carlisle', 'Carlton', 'Feliciano', 'Carroll', 'Carter-Johnson',
     'Case', 'Castle', 'Chavis', 'Cheng', 'Cherry', 'Christianson',
     'Chu', 'Chun', 'Chung', 'Clifford', 'Coats', 'Coley', 'Correa',
     'Cosby', 'Coyle', 'Crandall', 'Cronin', 'Cummins', 'Dobbins',
     'Dooley', 'Dudley', 'Dugan', 'Dupre', 'Dupree', 'Edmond',
     'Elmore', 'Emery', 'Ennis', 'Enriquez', 'Erwin', 'Eubanks',
     'Everett-Smith', 'Falcon', 'Fanning', 'Felton', 'Fenton',
     'Ferrara', 'Ferrell', 'Francisco', 'Frey', 'Friend', 'Fuchs',
     'Gable', 'Gabriel', 'Gann', 'Gil', 'Goetz', 'Goldsmith', 'Gomes',
     'Gregg', 'Guinn', 'Gustafson', 'Guzman', 'Hagan', 'Hagen',
     'Hardesty', 'Hare', 'Harlan', 'Hauser', 'Hawes', 'Herrera',
     'Herrick', 'Hilliard', 'Hollis', 'Holloway', 'Hong', 'Hoover',
     'Houston', 'Huston', 'Hutchings', 'Jaeger', 'Jeffers', 'Johns',
     'Jorgensen', 'Jung', 'Kaminski', 'Kessler', 'Keys', 'Khan',
     'Killian', 'Kim', 'Kimball', 'Kimbrough', 'King-Hale',
     'King-Marr', 'Kinney', 'Knott', 'Koenig', 'Krueger', 'Ladd',
     'Lamm', 'Lange', 'Layman', 'Lentz', 'Lenz', 'Leon', 'Levy',
     'Lilley', 'Lim', 'Lincoln', 'Lind', 'Lindley', 'Lindsay',
     'Lindsey', 'Liu', 'London', 'Longoria', 'Loomis', 'Lopes',
     'Lowery', 'Lowry', 'Loyd', 'Lucero', 'Luther', 'Lyman', 'Lynn',
     'Maher', 'Mahon', 'Maloney', 'Manley', 'Martell', 'McAdams',
     'McArthur', 'Meek', 'Meier', 'Merrill', 'Milburn', 'Monk',
     'Murdock', 'Myles', 'Novak', 'Noyes', 'Nunez', 'Palumbo',
     'Paradis', 'Paris', 'Park', 'Patten', 'Pedersen', 'Pemberton',
     'Pendergrass', 'Pfeiffer', 'Picard', 'Pickard', 'Purdy', 'Ramos',
     'Reddick', 'Ricks', 'Riggs', 'Rizzo', 'Robles', 'Root', 'Rowan',
     'Rucker', 'Schaffer', 'Schubert', 'Schuler', 'Schwarz', 'Scruggs',
     'Seaman', 'Shah', 'Sheridan', 'Shipley', 'Sikes', 'Sizemore',
     'Smalley', 'Somers', 'Sommers', 'Spears', 'Starling', 'StClair',
     'Stern', 'Tinsley', 'Tobias', 'Torrez', 'Ulrich', 'Vallejo',
     'Vandyke', 'Varney', 'Velez', 'Vickery', 'Waugh', 'Werner',
     'Whatley', 'Whitman', 'Wren', 'Zamora'
              )


names_short = {"Alaister"        : "Al",
                "Alan"           : "Al",
                "Alasdair"       : "Al",
                "Alastair"       : "Al",
                "Albert"         : ["Al", "Al", "Bert"],
                "Alexander"      : "Alex",
                "Alfred"         : ["Al", "Al", "Fred"],
                "Alvin"          : "Al",
                "Andrew"         : "Andy",
                "Anton"          : "Tony",
                "Antonio"        : "Tony",
                "Anthony"        : "Tony",
                "Antony"         : "Tony",
                "Arnold"         : "Arnie",
                "Benedict"       : ["Ben", "Ben", "Benny", "Bennie"],
                "Benjamin"       : ["Ben", "Ben", "Benny", "Bennie"],
                "Bernard"        : "Bernie",
                "Bertram"        : "Bert",
                "Bertrand"       : "Bert",
                "Bradley"        : "Brad",
                "Caleb"          : "Cal",
                "Calvin"         : "Cal",
                "Clifford"       : "Cliff",
                "Christopher"    : "Chris",
                "Daniel"         : ["Dan", "Dan", "Danny"],
                "David"          : "Dave",
                "Desmond"        : "Des",
                "Dominic"        : ["Dom", "Nick"],
                "Donald"         : "Don",
                "Douglas"        : "Doug",
                "Edgar"          : ["Ed", "Ed", "Eddie", "Eddie"],
                "Edward"         : ["Ed", "Ed", "Eddie", "Eddie", "Ted"],
                "Edmund"         : ["Ed", "Ed", "Eddie", "Eddie"],
                "Edwin"          : ["Ed", "Ed", "Eddie", "Eddie"],
                "Ernest"         : "Ernie",
                "Eugene"         : "Gene",
                "Francis"        : "Frank",
                "Francisco"      : "Frank",
                "Frederic"       : "Fred",
                "Frederick"      : "Fred",
                "Gareth"         : "Gary",
                "Geoffrey"       : ["Geoff", "Jeff"],
                "Georgia"        : "George",
                "Georgina"       : "George",
                "Geraldine"      : "Geri",
                "Gerald"         : ["Gerry", "Jerry"],
                "Gerard"         : ["Gerry", "Jerry"],
                "Gervase"        : ["Gerry", "Jerry"],
                "Gilbert"        : "Bert",
                "Gregory"        : "Greg",
                "Gustav"         : "Gus",
                "Harold"         : "Harry",
                "Henry"          : ["Harry", "Harry", "Hal"],
                "James"          : ["Jim", "Jamie"],
                "Jeffery"        : "Jeff",
                "Jeffrey"        : "Jeff",
                "Jeremy"         : "Jerry",
                "Jerome"         : "Jerry",
                "Joel"           : "Joe",
                "Jonathan"       : ["John", "John", "Jon"],
                "Joseph"         : "Joe",
                "Joshua"         : "Josh",
                "Kenneth"        : ["Ken", "Ken", "Kenny"],
                "Laurence"       : "Larry",
                "Lawrence"       : "Larry",
                "Lenard"         : ["Len", "Lenny"],
                "Leonard"        : ["Len", "Lenny"],
                "Lester"         : "Les",
                "Marcel"         : "Marc",
                "Marcus"         : "Marc",
                "Mathew"         : "Matt",
                "Matthew"        : "Matt",
                "Melvin"         : "Mel",
                "Michael"        : ["Mike", "Mike", "Mick", "Mickey"],
                "Nicholas"       : "Nick",
                "Patrick"        : "Pat",
                "Peter"          : "Pete",
                "Philip"         : "Phil",
                "Phillip"        : "Phil",
                "Raymond"        : "Ray",
                "Richard"        : ["Rick", "Rick", "Dick", "Richie", "Ricky", "Ritch", "Richie"],
                "Robert"         : ["Bob", "Bob", "Rob", "Bobby"],
                "Robin"          : "Rob",
                "Roderick"       : ["Rod", "Roddie", "Roddy"],
                "Rodger"         : ["Rod", "Roddie", "Roddy", "Rog"],
                "Roger"          : ["Rod", "Roddie", "Roddy", "Rog"],
                "Ronald"         : "Ron",
                "Ronan"          : "Ron",
                "Russel"         : "Russ",
                "Samuel"         : "Sam",
                "Sidney"         : "Sid",
                "Stanley"        : "Stan",
                "Stephan"        : "Steve",
                "Stephen"        : "Steve",
                "Steven"         : "Steve",
                "Terence"        : "Terry",
                "Terrence"       : "Terry",
                "Theodore"       : ["Theo", "Ted"],
                "Thomas"         : ["Tom", "Tom", "Thom", "Tommy"],
                "Timothy"        : "Tim",
                "Tobias"         : "Toby",
                "Vincent"        : "Vince",
                "Wilbur"         : "Will",
                "Wilfred"        : "Will",
                "Walter"         : ["Wallie", "Wally", "Walt"],
                "William"        : ["Bill", "Bill", "Billy", "Will"],
                "Abigail"        : "Abbie",
                "Amanda"         : "Mandy",
                "Annabelle"      : "Belle",
                "Angela"         : "Angie",
                "Angelica"       : "Angie",
                "Angelina"       : "Angie",
                "Antonia"        : "Toni",
                "Arabella"       : ["Bel", "Bella", "Bella", "Belle"],
                "Barbara"        : ["Barb", "Babs"],
                "Beatrice"       : "Bea",
                "Beatrix"        : "Bea",
                "Bernice"        : "Bernie",
                "Beverley"       : "Bev",
                "Caroline"       : ["Carrie", "Carol"],
                "Carolyn"        : ["Carrie", "Carol"],
                "Cassandra"      : "Cassie",
                "Catharine"      : ["Cath", "Cathy", "Kate"],
                "Catherin"       : ["Cath", "Cathy", "Kate"],
                "Catherine"      : ["Cath", "Cathy", "Kate"],
                "Catheryn"       : ["Cath", "Cathy", "Kate"],
                "Cathryn"        : ["Cath", "Cathy", "Kate"],
                "Catriona"       : "Cat",
                "Christianna"    : ["Chris", "Chrissie"],
                "Christina"      : ["Chris", "Chrissie", "Tina"],
                "Christine"      : ["Chris", "Chrissie", "Tina"],
                "Constance"      : "Connie",
                "Cristina"       : ["Chris", "Chrissie", "Tina"],
                "Danielle"       : ["Dani", "Danni"],
                "Diana"          : "Di",
                "Diane"          : "Di",
                "Dina"           : "Di",
                "Deborah"        : "Debbie",
                "Elizabeth"      : ["Beth", "Betty", "Brenda", "Liz", "Liz", "Lisa"],
                "Florence"       : "Flo",
                "Gwendolen"      : "Gwen",
                "Jancis"         : "Jan",
                "Janet"          : "Jan",
                "Janice"         : "Jan",
                "Janine"         : "Jan",
                "Janis"          : "Jan",
                "Jacqueline"     : "Jackie",
                "Jeanette"       : "Jenny",
                "Jennifer"       : "Jenny",
                "Josephine"      : ["Josie", "Josie", "Jo"],
                "Judith"         : "Judy",
                "Katarina"       : ["Kate", "Kate", "Kat"],
                "Katelyn"        : ["Kate", "Kate", "Kat"],
                "Katerina"       : ["Kate", "Kate", "Kat"],
                "Katharina"      : ["Kate", "Kate", "Kat", "Kathy", "Cathy", "Kath"],
                "Katharine"      : ["Kate", "Kate", "Kat", "Kathy", "Cathy", "Kath"],
                "Katharyn"       : ["Kate", "Kate", "Kat", "Kathy", "Cathy", "Kath"],
                "Katherine"      : ["Kate", "Kate", "Kat", "Kathy", "Cathy", "Kath"],
                "Kathleen"       : ["Kate", "Kate", "Kat", "Kathy", "Cathy", "Kath"],
                "Kathryn"        : ["Kate", "Kate", "Kat", "Kathy", "Cathy", "Kath"],
                "Katrina"        : ["Kate", "Kat", "Kat"],
                "Keridwen"       : ["Kerrie", "Kerry"],
                "Kimberley"      : "Kim",
                "Kimberly"       : "Kim",
                "Kirsten"        : "Kirsty",
                "Lilian"         : ["Lily", "Lilly"],
                "Lucille"        : "Lucy",
                "Lucinda"        : "Lucy",
                "Lynette"        : "Lynn",
                "Majorie"        : "Maggie",
                "Margery"        : "Maggie",
                "Margaret"       : "Maggie",
                "Meagan"         : "Meg",
                "Megan"          : "Meg",
                "Meghan"         : "Meg",
                "Melanie"        : "Mel",
                "Melinda"        : "Mel",
                "Melisa"         : "Mel",
                "Melissa"        : "Mel",
                "Natasha"        : ["Tasha", "Tasha", "Nat"],
                "Nicola"         : ["Nicci", "Nicci", "Nikki", "Nic"],
                "Nicole"         : ["Nicci", "Nicci", "Nikki", "Nic"],
                "Pamela"         : "Pam",
                "Patricia"       : ["Pat", "Trish", "Trisha", "Trisha", "Tricia"],
                "Penelope"       : "Penny",
                "Rebecca"        : "Becky",
                "Roberta"        : "Bobbi",
                "Rosalind"       : ["Ros", "Roz"],
                "Rosaline"       : ["Ros", "Roz"],
                "Rosamund"       : ["Ros", "Roz"],
                "Rosemarie"      : ["Ros", "Ros", "Rose", "Rosie"],
                "Rowena"         : ["Ros", "Roz"],
                "Samantha"       : "Sam",
                "Susan"          : ["Sue", "Sue", "Susie", "Suzie"],
                "Susanna"        : ["Sue", "Sue", "Susie", "Suzie"],
                "Suzanne"        : ["Sue", "Sue", "Susie", "Suzie"],
                "Tama"           : "Tammy",
                "Tamara"         : "Tammy",
                "Teresa"         : "Teri",
                "Theresa"        : "Teri",
                "Therese"        : "Teri",
                "Valentina"      : "Val",
                "Valerie"        : "Val",
                "Valerie"        : "Val",
                "Victoria"       : ["Vickie", "Vicky", "Vicki", "Vikki"]
              }



# new for 2016 - names derived from UK journalists, MPs and blue plaque holders
# added so we can have a similar but different set of English names for a different civilisation...
# 456 male first names.
male_firstnames_2 = ("Adam", "Adrian", "Aidan", "Al", "Alan",
        "Alasdair", "Alastair", "Albert", "Alberto", "Alec", "Alex",
        "Alexander", "Alfred", "Alistair", "Allan", "Allen", "Ambrose",
        "Andrew", "Andy", "Angus", "Anthony", "Anton", "Archie", "Arnold",
        "Arthur", "Aubrey", "Austin", "Barney", "Barry", "Basil", "Ben",
        "Benedict", "Benjamin", "Bernard", "Bert", "Bertrand", "Bill",
        "Billy", "Bob", "Boris", "Bradley", "Brandon", "Brendan", "Bruce",
        "Bruno", "Bryan", "Byron", "Callum", "Calum", "Caspar", "Cecil",
        "Charles", "Charlie", "Chris", "Christian", "Christopher", "Clement",
        "Clive", "Conor", "Craig", "Damian", "Dan", "Daniel", "Danny",
        "Darren", "Dave", "David", "Dean", "Denis", "Dennis", "Derek",
        "Desmond", "Dick", "Dominic", "Don", "Donald", "Doug", "Douglas",
        "Drew", "Duncan", "Dylan", "Ed", "Edgar", "Edmond", "Edmund",
        "Edward", "Edwin", "Elliot", "Elroy", "Emile", "Eric", "Ernest",
        "Evan", "Ewan", "Ewen", "Ezra", "Felix", "Ford", "Francis", "Frank",
        "Fred", "Freddie", "Frederic", "Frederick", "Gabriel", "Gareth",
        "Gary", "Gavin", "Geoff", "Geoffrey", "George", "Gerald", "Gerard",
        "Gideon", "Gilbert", "Giles", "Gordon", "Graeme", "Graham", "Grant",
        "Greg", "Gregory", "Gus", "Gustav", "Guy", "Hans", "Harold", "Harry",
        "Hector", "Henry", "Herbert", "Herman", "Hiram", "Horace", "Horatio",
        "Howard", "Hubert", "Hugh", "Hugo", "Humphrey", "Hywel", "Iain",
        "Ian", "Ira", "Isaac", "Ivan", "Ivor", "Jack", "Jacob", "Jake",
        "James", "Jamie", "Jason", "Jay", "Jeff", "Jeffrey", "Jeremy",
        "Jerome", "Jesse", "Jim", "Jimmy", "Joe", "John", "John-Paul",
        "Johnny", "Jon", "Jonathan", "Joseph", "Josh", "Joshua", "Jude",
        "Julian", "Julius", "Justin", "Karl", "Keith", "Kelvin", "Ken",
        "Kenneth", "Kenny", "Kevin", "Kieran", "Kris", "Kurt", "Kyle",
        "Larry", "Laurence", "Lawrence", "Lee", "Leonard", "Les", "Lewis",
        "Liam", "Lionel", "Lloyd", "Louis", "Lucien", "Luke", "Malcolm",
        "Marc", "Marcus", "Mark", "Martin", "Martyn", "Matt", "Matthew",
        "Max", "Michael", "Mick", "Mickey", "Mike", "Morgan", "Mortimer",
        "Murray", "Nathan", "Nathaniel", "Neal", "Neil", "Neville",
        "Nicholas", "Nick", "Nicky", "Nigel", "Noel", "Norman", "Oliver",
        "Orlando", "Oscar", "Owen", "Pat", "Patrick", "Paul", "Percy", "Pete",
        "Peter", "Phil", "Philip", "Phillip", "Pierre", "Quentin", "Rafael",
        "Ralph", "Ramon", "Randolph", "Raymond", "Rex", "Richard", "Rob",
        "Robbie", "Robert", "Robin", "Rod", "Roger", "Roland", "Ronald",
        "Ronnie", "Rory", "Roy", "Rufus", "Rupert", "Russell", "Ryan", "Sam",
        "Sammy", "Samuel", "Scott", "Sean", "Sebastian", "Shane", "Shaun",
        "Shawn", "Sid", "Sidney", "Siegfried", "Sigmund", "Simon", "Spencer",
        "Stanley", "Stephen", "Steve", "Steven", "Stewart", "Stuart",
        "Sydney", "Ted", "Terence", "Terry", "Theodore", "Thomas", "Tim",
        "Timothy", "Tobias", "Toby", "Tom", "Tommy", "Tony", "Trevor",
        "Tyler", "Vernon", "Victor", "Vincent", "Walter", "Warren", "Wayne",
        "Wes", "Will", "William", "Wilson", "Winston", "Zachary",
        "Alain", "Aldous", "Alexi", "Algernon", "Allister",
        "Aloysius", "Alun", "Andreas", "Andres", "Aneurin",
        "Archibald", "Augustus", "Beau", "Bela", "Charles", "Crispin",
        "Demetri", "Ebenezer", "Edvard", "Emeric", "Emery", "Ernst",
        "Fabian", "Geraint","Glyn", "Grahame", "Gwilym", "Harold",
        "Havelock", "Hilaire", "Huw", "Jimi", "Keir", "Kevan",
        "Ludovic", "Mervyn", "Mikey", "Morten", "Myles", "Nic",
        "Nikolaus", "Ollie", "Olly", "Osbert", "Quintin", "Rhodri",
        "Robert", "Robinson", "Rowland", "Royston", "Rudyard", "Seb",
        "Simeon","Theodor", "Thomas", "Tristram", "Wilfrid",
        "William", "Willy", "Wolfgang", "Zac",
        "Garry", "Glen", "Leo", "Lucian", "Roderick",
        "Asa",      # Asa Bennett (Daily Telegraph)
        "Aditya",   # Aditya Chakrabortty (The Guardian}
        "Alain",    # Alain Tolhurst (The Sun)
        "Aldous",   # Aldous Huxley (blue Plaque)
        "Alexi",    # Alexi Mostrous (The Times)
        "Algernon", # Algernon Swinburne (blue plaque)
        "Ali",      # Ali Martin (The Guardian)
        "Allister", # Allister Heath (The Telegraph)
        "Aloysius", # Aloysius Hansom (blue plaque)
        "Alun",     # Alun Cairns (MP, Conservative)
        "Andreas",  # Andreas Paleit (Financial Times)
        "Andres",   # Andres Schipani (The Guardian)
        "Aneurin",  # Aneurin Bevan (blue plaque)
        "Archibald",# Archibald McIndoe (blue plaque)
        "Augustus", # Augustus John, Augustus Pitt (both blue plaques)
        "Beau",     # Beau Brummell (blue plaque)
        "Bela",     # Bela Bartok (blue plaque)
        "Bryce",    # Bryce Elder (Financial Times)
        "Constant", # Constant Lambert (blue plaque)
        "Crispin",  # Crispin Blunt (MP, Conservative)
        "Demetri",  # Demetri Smith
        "Ebenezer",
        "Edvard",   # Edvard Benes, Edvard Grieg (both blue plaques)
        "Emeric",   # Emeric Pressburger (blue plaque)
        "Emery",    # Emery Walker (blue plaque)
        "Ernst",    # Ernst Chamberlain (blue plaque)
        "Fabian",   # Fabian Ware (blue plaque)
        "Francie",  # Francie Molloy (MP, Sinn Fein)
        "Geraint",  # Geraint Davies (MP, Labour)
        "Glyn",     # Glyn Davies (MP, Conservative)	
        "Grahame",  # Grahame Morris (MP, Labour)
        "Gwilym",   # Gwilym Mumford (The Guardian)
        "Harold",   # Harold Knight, Harold Gilbert, Harold Gillies, Harold Abrahams etc (blue plaques)
        "Havelock", # Havelock Ellis (blue plaque)
        "Hilaire",  # Hilaire Belloc (blue plaque)
        "Huw",      # Huw Merriman (MP, Conservative)
        "Jeevan",   # Jeevan Vasagar (The Guardian)
        "Jimi",     # Jimi Hendrix (blue plaque)
        "Jolyon",   # Jolyon Attwooll (The Daily Telegraph)
        "Kaya",     # Kaya Burgess (The Times)
        "Keir",     # Keir Starmer (MP, Labour)
        "Kevan",    # Kevan Jones (MP, Labour)
        "Kiran",    # Kiran Stacey (Financial Times)
        "Kit",      # Kit Malthouse (MP, Conservative)
        "Lanre",    # Lanre Baker (The Guardian)
        "Learie",   # Learie Constantine (blue plaque)
        "Leigh",    # Leigh Holmwood (The Guardian)
        "Lincoln",  # Lincoln Stanhope Wainwright (blue plaque)
        "Lindesay", # Lindesay Irvine (The Guardian)
        "Ludovic",  # Ludovic Hunter-Tilney (Financial Times)
        "Ludo",     # Ludo Hunter-Tilney (Financial Times)
        "Mati",     # Mati Milstein (Daily Mail) 
        "Mervyn",   # Mervyn Peake (blue plaque) 
        "Mikey",    # Mikey Smith (Daily Mirror)
        "Morten",   # Morten Nilsson (Chairman, NOW: Pensions)
        "Myles",    #
        "Nic",      # Nic Fildes (The Times)
        "Nikolaus", # Nikolaus Pevsner (blue plaque)
        "Ollie",    # Ollie Gillman (Daily Mail)
        "Olly",     # Olly Wainwright (The Guardian)
        "Osbert",   # Osbert Lancaster (blue plaque)
        "Phelim",   # Phelim O'Neill (The Guardian)
        "Quintin",  # Quintin Hogg (blue plaque)
        "Rhodri",   # Rhodri Phillips (The Sun)
        "Rowland",  # Rowland Hill (blue plaque)
        "Royston",  # Royston Smith (MP, Conservative)
        "Rudyard",  # Rudyard Kipling (blue plaque)
        "Seb",      # Seb Morton-Clark (Financial Times)
        "Severin",  # Severin Carrell (The Guardian)
        "Simeon",   # Simeon Kerr (Financial Times)
        "Theodor",  # Theodor Fontane (blue plaque)
        "Topham",   # Topham Beauclerk (blue plaque)
        "Tristram", # Tristram Hunt (MP, Labour)	
        "Vivian",   # Vivian Forbes (blue plaque)
        "Washington",# Washington Irving (blue plaque)
        "Wilfrid",  # Wilfrid Blunt (blue plaque)
        "Willy",    # Willy Clarkson (blue plaque)
        "Wolfgang", # Wolfgang Munchau (Financial Times)
        "Xan",      # Xan Brooks (The Guardian)
        "Zac"       # Zac Goldsmith (MP, Conservative)
)

# 465 female first names.
female_firstnames_2 = ("Abby", "Ada", "Agatha", "Alexandra", "Alexis",
        "Alice", "Alison", "Alva", "Amanda", "Amber", "Amelia", "Amy",
        "Andrea", "Angela", "Angelique", "Ann", "Anna", "Anne", "Anne-Marie",
        "Anne-Sylvaine", "Annie", "Ariana", "Barbara", "Beatrice", "Becca",
        "Becky", "Bella", "Bridget", "Brooke", "Bryony", "Caitlin", "Camilla",
        "Candice", "Cara", "Carly", "Carol", "Carole", "Caroline", "Carolyn",
        "Carrie", "Catherine", "Cathy", "Celia", "Charlotte", "Cheryl",
        "Chloe", "Chris", "Christina", "Christine", "Claire", "Clara",
        "Clare", "Clemmie", "Coleen", "Colleen", "Constance", "Cordelia",
        "Courtney", "Daisy", "Dana", "Danielle", "Daphne", "Dawn", "Debbie",
        "Deborah", "Deidre", "Deirdre", "Diana", "Diane", "Dina", "Dominique",
        "Donna", "Dorothy", "Edith", "Edwina", "Elaine", "Eleanor", "Elena",
        "Elisabeth", "Elizabeth", "Ellen", "Ellie", "Emily", "Emma", "Enid",
        "Erika", "Esther", "Ethel", "Eva", "Eve", "Evelyn", "Faith", "Fay",
        "Felicity", "Fiona", "Florence", "Frances", "Francesca", "Gemma",
        "Georgia", "Georgina", "Geraldine", "Gillian", "Gloria", "Grace",
        "Gracie", "Gretchen", "Hannah", "Harriet", "Hazel", "Heather",
        "Heidi", "Helen", "Helena", "Helene", "Henrietta", "Hilary", "Holly",
        "Ida", "Imogen", "Ivy", "Jackie", "Jade", "Jana", "Jane", "Janice",
        "Jasmine", "Jayne", "Jean", "Jeannette", "Jennie", "Jennifer",
        "Jenny", "Jessica", "Jessie", "Jill", "Jo", "Joan", "Joanna",
        "Joanne", "Josephine", "Joy", "Joyce", "Judith", "Judy", "Julia",
        "Julie", "Justine", "Kara", "Karen", "Karin", "Kate", "Katharine",
        "Katherine", "Kathleen", "Kathy", "Katie", "Katrina", "Katy", "Kelly",
        "Kerry", "Kira", "Kirsten", "Kirsty", "Laura", "Lauren", "Leah",
        "Leanne", "Lee", "Lilian", "Lisa", "Liz", "Lizzie", "Lois", "Louise",
        "Lucia", "Lucy", "Lydia", "Lyn", "Madeleine", "Mae", "Maeve",
        "Maggie", "Margaret", "Margareta", "Margery", "Margot", "Maria",
        "Marie", "Marie-Claire", "Marina", "Marion", "Martina", "Mary",
        "Maud", "Meg", "Megan", "Mel", "Melanie", "Melissa", "Michelle",
        "Miranda", "Molly", "Mona", "Myra", "Nadine", "Nancy", "Naomi",
        "Natalie", "Natasha", "Nellie", "Nicola", "Nicole", "Nikki",
        "Octavia", "Olive", "Olivia", "Pat", "Patricia", "Paula", "Pauline",
        "Peggy", "Penny", "Philippa", "Polly", "Rachael", "Rachel", "Rebecca",
        "Roberta", "Ros", "Rosalind", "Rose", "Rosemary", "Rosie", "Rowena",
        "Ruth", "Sadie", "Saffron", "Sally", "Samantha", "Sandra", "Sara",
        "Sarah", "Sarah-Jane", "Shannon", "Sharlene", "Sharon", "Sheila",
        "Sinead", "Sophia", "Sophie", "Stella", "Stephanie", "Sue", "Susan",
        "Susannah", "Suzanne", "Suzie", "Suzy", "Sybil", "Sylvia", "Tamara",
        "Tania", "Tanya", "Tara", "Teresa", "Theresa", "Toni", "Tracey",
        "Tracy", "Val", "Valerie", "Vanessa", "Vera", "Vicki", "Vicky",
        "Victoria", "Vikki", "Violet", "Virginia", "Vita", "Wendy",
        "Winifred", "Yvette", "Zoe",
        "Aditya", "Aine", "Aislinn", "Aneeta", "Anjli", "Antoinette",
        "Anushka", "Ariella", "Arielle", "Attracta", "Bethan",
        "Bridie", "Carlene", "Carola", "Cat", "Caty", "Christabel",
        "Claer", "Clementia", "Dinah", "Dorothea", "Emmeline",
        "Flick", "Frederika", "Gaby", "Gay", "Georgette", "Georgie",
        "Gisela", "Hadley", "Harriett", "Hertha", "Iona", "Izabella",
        "Jemima", "Jen", "Jenn", "Jenni", "Jess", "Jillian",
        "Juliette", "Kaya", "Keiligh", "Libby", "Lillie", "Lizzy",
        "Luciana", "Lucie", "Madlen", "Mhairi", "Millicent",
        "Natascha", "Nigella", "Ninette", "Olinka", "Ottoline",
        "Pilita", "Rhiannon", "Sali", "Sasha", "Scheherazade",
        "Seraphine", "Shami", "Sherry", "Sheryll", "Siobhain", "Sian",
        "Sophy", "Talya", "Therese", "Violette", "Xanthe", "Zlata", "Talya",
        "Carey", "Decca", "Leonie", "Oonagh", "Clair", "Clementine",
        "Davina", "Lana", "Lynn", "Marianne", "May", "Robyn",
        "Aine",     # Aine McCarthy (The Independent)
        "Aislinn",  # Aislinn Laing (Daily Telegraph)
        "Aneeta",   # Aneeta Bole
        "Anjli",    # Anjli Raval (Financial Times)
        "Antoinette",# Antoinette Sandbach (MP, Conservative)
        "Anushka",  # Anushka Asthana (The Guardian)
        "Ariella",  # Ariella Budick (Financial Times)
        "Arielle",  # Arielle Richardson
        "Ashley",   # Ashley Collman (Daily Mail), Ashley Armstrong (Daily Telegraph)
        "Attracta", # Attracta Mooney (Financial Times)
        "Bethan",   # Bethan McKernan (The Independent), Bethan Ryder (The Telegraph)
        "Bridie",   # Bridie Jabour (The Guardian), Bridie Jenkins (???)
        "Carlene",  # Carlene Bailey-Thomas (The Guardian)
        "Carola",   # Carola Hoyos (Financial Times)
        "Cat",      # Cat Smith (MP, Labour)
        "Caty",     # Caty Enders (The Guardian)
        "Ceri",     # Ceri Jones (Pensions World)
        "Cherrill", # Cherrill Hicks (Daily Telegraph)
        "Christabel",# Christabel Pankhurst (blue plaque)
        "Claer",    # Claer Barrett (Financial Times)
        "Clementia",# Clementia Taylor (blue plaque)
        "Corri",    # Corri Wilson (MP, Scottish National Party)
        "Corraine", # Corraine 'Corri' Wilson (MP, Scottish National Party)
        "Darcy",    # Darcy Keller (Financial Times)
        "Dinah",    # Dinah Turner (Daily Mail)
        "Dorothea", # Dorothea Chambers (blue plaque)
        "Emmeline", # Emmeline Pankhurst (blue plaque)
        "Frederika",# Frederika Whitehead (The Guardian)
        "Gaby",     # Gaby Hinsliff (The Guardian)
        "Gay",      # Gay Alcorn (The Guardian)
        "Georgette",# Georgette Heyer (blue plaque)
        "Georgie",  # Georgie Ellmore-Jones (real life)
        "Gerri",    # Gerri Peev (Daily Mail)
        "Gill",     # Gill Furniss (MP, Labour)
        "Gisela",   # Gisela Stuart (MP, Labour)
        "Hadley",   # Hadley Freeman (The Guardian)
        "Harriett", # Harriett Baldwin (MP, Conservative)
        "Hertha",   # Hertha Ayrton (blue plaque)
        "Iona",     # Iona Craig (The Times)
        "Izabella", # Izabella Kaminska (Financial Times)
        "Jemima",   # Jemima Sissons (Financial Times), Jemima Lamont
        "Jen",      # Jen Blackburn (The Sun)
        "Jenn",     # Jenn Selby (The Independent)
        "Jenna",    # Jenna Gadhavi (Pensions Insight)
        "Jenni",    # Jenni Russell (The Times)
        "Jess",     # Jess Cartner-Morley (The Guardian)
        "Jillian",  # Jillian Ambrose (The Telegraph)
        "Juliette", # Juliette Garside (The Guardian)
        "Kat",      # Kat Romero (Daily Express}
        "Keiligh",  # Keiligh Baker (Daily Mail)
        "Khaleda",  # Khaleda Rahman (Daily Mail)
        "Kinvara",  # Kinvara Balfour (Daily Telegraph)
        "Leonie",   # Leonie Roderick (The Independent, Marketing Week)
        "Leslie",   # Leslie Hook (Financial Times)
        "Libby",    # Libby Brooks (The Guardian)
        "Lillie",   # Lillie Langtry (blue plaque)
        "Lindsay",  # Lindsay McIntosh (The Times)
        "Lizzy",    # Lizzy Davies (The Guardian)
        "Luciana",  # Luciana Berger (MP, Labour)
        "Lucie",    # Dame Lucie Rie (blue plaque)
        "Lyndsey",  # Lyndsey Telford (The Telegraph)
        "Lynsey",   # Lynsey Haywood (The Sun)
        "Madlen",   # Madlen Davies (Daily Mail)
        "Merope",   # Merope Mills (The Guardian)
        "Mhairi",   # Mhairi Black (MP, Scottish National Party)
        "Millicent",# Millicent Fawcett (blue plaque)
        "Natascha", # Natascha Engel (MP, Labour)
        "Nia",      # Nia Griffith (MP, Labour)
        "Nigella",  # Nigella Lawson
        "Ninette",  # Ninette De Valois (blue plaque)
        "Olinka",   # Olinka Koster (Evening Standard, Daily Mail)
        "Ottoline", # Ottoline Morrell (blue plaque)
        "Pilita",   # Pilita Clark (Financial Times)
        "Rhiannon", # Rhiannon Williams (The Telegraph)
        "Sali",     # Sali Hughes (The Guardian)
        "Sasha",    # Sasha Koren (The Guardian)
        "Scheherazade",# Scheherazade Daneshkhu (Financial Times)
        "Seema",    # Seema Kennedy (MP, Conservative)
        "Seraphine",# Seraphine Astafieva (blue plaque)
        "Shami",    # Shami Chakrabarti
        "Sherry",   # Sherry Pruitt (The Sun)
        "Sheryll",  # Sheryll Murray (MP, Conservative)	South East Cornwall
        "Siobhain", # Siobhain McDonagh (MP, Labour)
        "Siân",     # Siân Berry (Green party), Sian Williams (BBC)
        "Sian",     # Siân Berry (Green party), Sian Williams (BBC)
        "Sophy",    # Sophy Ridge (The Telegraph, Sky News)
        "Sylvaine", # Anne-Sylvaine Chassany (Financial Times)
        "Talya",    # Talya Misiri (Pensions Age, Retail Gazette)
        "Thérèse",  #
        "Therese",  #                   
        "Violette", # Violette Szabo (blue plaque)
        "Vivien",   # Vivien Leigh (blue plaque)
        "Xanthe",   # Xanthe Clay (The Telegraph)
        "Zlata",     # Zlata Rodionova (The Independent)
        "Fenella"                       
)

all_firstnames_2 = male_firstnames_2+female_firstnames_2

# 1978 surnames.
surnames_2 = ("Aaronovitch", "Abbott", "Abraham", "Abrahams",
        "Abramson", "Ackerman", "Adam", "Adams", "Adamson", "Addams",
        "Addison", "Addley", "Aglionby", "Agnew", "Aiden", "Alcock",
        "Alcorn", "Aldous", "Aldrick", "Aldridge", "Alexander",
        "Allan", "Allardice", "Allen", "Allenby", "Allison",
        "Altmann", "Ambrose", "Amess", "Anderson", "Andrew",
        "Andrews", "Ansell", "Anthony", "Archer", "Argar", "Arkless",
        "Arkwright", "Armitage", "Armstrong", "Arne", "Arnold",
        "Ashby", "Ashdown", "Ashley", "Ashworth", "Aspinall",
        "Asquith", "Astafieva", "Asthana", "Astor", "Atherton",
        "Atkins", "Attlee", "Attwooll", "Austin", "Authers", "Ayrton",
        "Bachelor", "Bacon", "Baden", "Bader", "Bagehot", "Bagnold",
        "Bagot", "Bailey", "Baillie", "Bainbridge", "Baird",
        "Bairnsfather", "Baker", "Balcon", "Baldwin", "Balfe",
        "Ballantyne", "Banfield", "Banks", "Bannerman", "Banning",
        "Barber", "Barbon", "Barclay", "Bardell", "Baring", "Barker",
        "Barkham", "Barlow", "Barmby", "Barnardo", "Barnes",
        "Barnett", "Barnicoat", "Baron", "Barrett", "Barrie",
        "Barron", "Barry", "Bartlett", "Bartok", "Barwell", "Basevi",
        "Bateman", "Batey", "Batty", "Bax", "Baxter", "Bayes",
        "Baylis", "Bazalgette", "Beard", "Beardsley", "Beatson",
        "Beattie", "Beatty", "Beauclerk", "Beaufort", "Beaumont",
        "Beck", "Beckett", "Beecham", "Beedle", "Beerbohm", "Beesley",
        "Beeston", "Behr", "Belam", "Bell", "Bellingham", "Bello",
        "Belloc", "Belton", "Benedict", "Benes", "Benn", "Bennett",
        "Benson", "Bentham", "Bentley", "Benyon", "Bercow",
        "Beresford", "Berger", "Bergman", "Berlioz", "Bernal",
        "Berry", "Besant", "Bestall", "Betjeman", "Betts", "Bevan",
        "Bevin", "Billen", "Billington", "Bingham", "Bintliff",
        "Bird", "Birrell", "Bischoff", "Bixby", "Black", "Blackburn",
        "Blackden", "Blackett", "Blackford", "Blackie", "Blackman",
        "Blackwood", "Blair", "Blake", "Blanchard", "Bland",
        "Blenkinsop", "Bligh", "Bliss", "Blitz", "Blomfield", "Bloom",
        "Blumlein", "Blunt", "Blyton", "Boden", "Bodley", "Bole",
        "Boles", "Bolivar", "Bomberg", "Bond", "Bone", "Bonham",
        "Booker", "Boone", "Booth", "Borger", "Borough", "Borrow",
        "Borwick", "Boseley", "Boswell", "Bottomley", "Boult",
        "Boulton", "Bowater", "Bowd", "Bowen", "Bowers", "Bowlly",
        "Boyce", "Boyde", "Boyle", "Bracchi", "Bradley", "Bradshaw",
        "Brady", "Brailsford", "Brain", "Braithwaite", "Brake",
        "Brampton", "Brandt", "Brangwyn", "Branigan", "Brazier",
        "Bream", "Bremner", "Brennan", "Bridge", "Bridgeman",
        "Bridgen", "Briggs", "Bright", "Brine", "Brinkley",
        "Brittain", "Britten", "Brock", "Brockes", "Brodbeck",
        "Brokenshire", "Brooke", "Brooker", "Brooks", "Brooks Adams",
        "Broughton", "Brown", "Browne", "Browning", "Bruce", "Brule",
        "Brummell", "Brummer", "Brunel", "Bruning", "Brunsden",
        "Bryant", "Buck", "Buckland", "Budick", "Bull", "Bullmore",
        "Bullock", "Buncombe", "Bunting", "Burden", "Burgess",
        "Burgon", "Burgoyne", "Burke", "Burkeman", "Burn", "Burne",
        "Burnett", "Burney", "Burnham", "Burns", "Burnton",
        "Burrowes", "Burt", "Burton", "Buss", "Bussmann", "Butler",
        "Butt", "Butterfield", "Byrne", "Cadbury", "Cadman", "Cahill",
        "Cairns", "Caldecott", "Caldwell", "Cameron", "Campbell",
        "Canning", "Carlile", "Carlyle", "Carmichael", "Carnegy",
        "Carpenter", "Carpentier", "Carrell", "Carrington", "Carroll",
        "Carswell", "Carter", "Cartlidge", "Cartner", "Cary", "Cash",
        "Caslon", "Caulfield", "Caulkin", "Cavell", "Cavendish",
        "Cayley", "Cecil", "Chadwick", "Chaffin", "Chakrabarti",
        "Chakrabortty", "Chalabi", "Chalk", "Chamberlain", "Chambers",
        "Champion", "Chandler", "Change", "Chapman", "Charter",
        "Chassany", "Chazan", "Chen", "Cherry", "Chesshyre",
        "Chester", "Chesters", "Chesterton", "Child", "Childs",
        "Chilton", "Chilvers", "Chippendale", "Chisholm", "Chope",
        "Chorley", "Christenson", "Christie", "Churchill", "Clancy",
        "Clapp", "Clark", "Clarke", "Clarkson", "Clay", "Clayton",
        "Cleary", "Clegg", "Clements", "Cleverly", "Clews", "Clifton",
        "Clive", "Clough", "Clover", "Clwyd", "Coaker", "Coates",
        "Cobden", "Cobham", "Cochrane", "Cockcroft", "Cockerell",
        "Cockerton", "Coffey", "Coghlan", "Cohen", "Coke", "Colback",
        "Cole", "Coleman", "Coleridge", "Collin", "Collins",
        "Collinson", "Collman", "Colvile", "Compton", "Coney",
        "Conlan", "Conn", "Connor", "Conrad", "Constable",
        "Constantine", "Cook", "Cookson", "Cooper", "Copeman",
        "Corbyn", "Corden", "Coren", "Corrigan", "Costolo",
        "Cotterill", "Coverdale", "Cowan", "Coward", "Cowie",
        "Cowing", "Cox", "Coyle", "Crabb", "Crabtree", "Craig",
        "Crane", "Crausby", "Crawford", "Crawley", "Creagh", "Creasy",
        "Creed", "Cribb", "Crilly", "Crompton", "Crookes", "Crooks",
        "Crosby", "Cross", "Crouch", "Crow", "Cruddas", "Cruikshank",
        "Cryer", "Cubitt", "Cumbo", "Cumming", "Cummings", "Cummins",
        "Cunningham", "Curtis", "Curzon", "Cusack", "Dakers", "Dakin",
        "Dale", "Dance", "Danczuk", "Daneshkhu", "Daniel", "Daniell",
        "Daniels", "Dart", "Darwin", "David", "Davidson", "Davies",
        "Davis", "Dawson", "Day", "De Havilland", "De Morgan",
        "De Piero", "De Quincey", "De Valois", "Dean", "Deans",
        "Dearden", "Defoe", "Degasquet", "Deighton", "Delingpole",
        "Delius", "Demetriou", "Dempster", "Denham", "Dennis", "Dent",
        "Derbyshire", "Devant", "Deveney", "Devine", "Devlin", "Diaz",
        "Dick", "Dickens", "Dickin", "Dickinson", "Dickson",
        "Dimbleby", "Dinenage", "Dishman", "Dobson", "Docherty",
        "Dodds", "Doherty", "Dolman", "Dombey", "Don", "Donald",
        "Donaldson", "Donat", "Donegan", "Donelan", "Donnan",
        "Donnelly", "Dooley", "Dorn", "Dorries", "Dorsey", "Dougherty",
        "Doughty", "Douglas", "Dowd", "Dowden", "Dowling", "Doyle",
        "Drake", "Drax", "Dredge", "Driver", "Dromey", "Drummond",
        "Dryden", "Drysdale", "Du Maurier", "Duddridge", "Dudley",
        "Duff", "Duffy", "Dugan", "Dugdale", "Dugher", "Duke",
        "Duncan", "Dunham", "Dunkley", "Dunn", "Dunne", "Durkan",
        "Durrant", "Dyer", "Dyson", "Eagle", "Earley", "Earnshaw",
        "Eastlake", "Eccles", "Eddington", "Edgar", "Edgecliffe",
        "Edwards", "Efford", "Effron", "Ehrenberg", "Elder", "Elen",
        "Eley", "Elgar", "Elgot", "Eliot", "Elkins", "Elliott",
        "Ellis", "Ellison", "Ellman", "Ellmore", "Ellson", "Ellwood",
        "Elmore", "Elphicke", "Enders", "Engel", "England",
        "Esterson", "Etheridge", "Etty", "Eustice", "Evans",
        "Evennett", "Ewart", "Fabricant", "Facey", "Fahey", "Fallon",
        "Faraday", "Farchy", "Farmer", "Farquharson", "Farr",
        "Farrell", "Farrelly", "Farron", "Fawcett", "Fearn",
        "Fellows", "Fenton", "Fenwick", "Fernyhough", "Ferrier",
        "Fick", "Field", "Fielding", "Fields", "Fifield", "Fildes",
        "Finch", "Finkelstein", "Firn", "Fisher", "Fister", "FitzRoy",
        "Fitzpatrick", "Flanagan", "Flaxman", "Flecker", "Fleming",
        "Fletcher", "Flinders", "Flint", "Flood", "Flynn", "Foley",
        "Fontane", "Fontanella", "Forbes", "Ford", "Forester",
        "Forster", "Forsyth", "Fortune", "Foster", "Fotheringham",
        "Fox", "Foxcroft", "Foy", "Frampton", "Francois", "Franklin",
        "Fraser", "Frazer", "Freake", "Frean", "Freedland", "Freeman",
        "Freer", "French", "Freud", "Fricker", "Friedberg", "Frith",
        "Frizell", "Frobisher", "Froude", "Fry", "Fuller", "Furness",
        "Furniss", "Fuseli", "Fysh", "Gabor", "Gaffney", "Gage",
        "Gainsborough", "Gaitskell", "Gale", "Galsworthy", "Galton",
        "Gandy", "Gapper", "Gardiner", "Gardner", "Garnier",
        "Garrahan", "Garrett", "Garrick", "Garside", "Garthwaite",
        "Garvey", "Gascoyne", "Gaskell", "Gauke", "Geary", "Geddes",
        "Gee", "Geidroyc", "Gerner", "Gertler", "Gestetner",
        "Gethins", "Gibb", "Gibbon", "Gibbs", "Gibson", "Gilbert",
        "Gilbey", "Giles", "Gillan", "Gillbe", "Gillford", "Gillies",
        "Gillman", "Gillmor", "Gilmour", "Ginsberg", "Gissing",
        "Gladstone", "Glaisher", "Glanfield", "Glass", "Glen",
        "Glendenning", "Glendinning", "Glenza", "Glicksman",
        "Glindon", "Glover", "Godfree", "Godfrey", "Godley",
        "Godsiff", "Godwin", "Goff", "Goldenberg", "Goldsmith",
        "Gombrich", "Good", "Goodall", "Goodman", "Gordon", "Gosden",
        "Gosse", "Gould", "Gounod", "Govan", "Gove", "Grace", "Grady",
        "Graham", "Grahame", "Grainger", "Grant", "Graves", "Gray",
        "Grayling", "Greathead", "Greaves", "Greechan", "Green",
        "Greenaway", "Greene", "Greening", "Greenslade", "Greenwell",
        "Greenwood", "Gregory", "Grene", "Grenfell", "Gresley",
        "Grew", "Grey", "Grieg", "Grierson", "Grieve", "Griffin",
        "Griffith", "Griffiths", "Grimaldi", "Grimes", "Groom",
        "Grossmith", "Grote", "Guest", "Gummer", "Gunther", "Guthrie",
        "Gwynne", "Habblett", "Haggard", "Haigh", "Haldane", "Hale",
        "Halfon", "Hall", "Hallam", "Halliday", "Halls", "Hamilton",
        "Hammond", "Hampton", "Hancock", "Handel", "Handley", "Hands",
        "Hanman", "Hann", "Hanna", "Hannam", "Hansen", "Hansom",
        "Hanson", "Harding", "Hardy", "Harford", "Harker", "Harley",
        "Harman", "Harmsworth", "Harper", "Harries", "Harrington",
        "Harris", "Harrison", "Hart", "Harte", "Hartley", "Hartnell",
        "Harvey", "Haselhurst", "Hattenstone", "Hawkes", "Hawkins",
        "Hawthorne", "Hay", "Haydon", "Hayes", "Hayler", "Hayman",
        "Haynes", "Hayward", "Haywood", "Hazell", "Hazlitt", "Heal",
        "Healey", "Heappey", "Heartfield", "Heath", "Heaton", "Helm",
        "Heming", "Henderson", "Hendrick", "Hendrix", "Hendry",
        "Henley", "Henry", "Hepburn", "Herbert", "Herford", "Hern",
        "Hetherington", "Heyer", "Hickey", "Hicks", "Hide", "Higgins",
        "Hill", "Hillier", "Hilton", "Hinds", "Hinsliff", "Hipwell",
        "Hiscott", "Hitchcock", "Hix", "Hoad", "Hoare", "Hobbs",
        "Hodal", "Hodge", "Hodgekiss", "Hodges", "Hodgkin", "Hodgson",
        "Hoey", "Hofmann", "Hogg", "Hoggins", "Hollern",
        "Hollingbery", "Hollinger", "Hollinrake", "Hollinshead",
        "Hollobone", "Holloway", "Hollywood", "Holman", "Holmwood",
        "Holst", "Holt", "Holtby", "Hood", "Hook", "Hooper", "Hooton",
        "Hope", "Hopkins", "Hornby", "Horniman", "Horton", "Hosie",
        "Hosking", "Houlder", "Hoult", "Housman", "Howard", "Howarth",
        "Howell", "Howlett", "Hoyle", "Hoyos", "Huddleston", "Hudson",
        "Hughes", "Hull", "Hume", "Hunt", "Hunter", "Huntingford",
        "Hurd", "Hurley", "Hurst", "Huskisson", "Hutchings",
        "Hutchinson", "Huxley", "Hyde", "Hyndman", "Hyslop", "Ide",
        "Ingle", "Inman", "Innes", "Ireland", "Irvine", "Irving",
        "Isaacs", "Jack", "Jackson", "Jacobs", "Jagger", "James",
        "Jameson", "Jamieson", "Jarvis", "Jefferies", "Jefford",
        "Jellicoe", "Jenkin", "Jenkins", "Jenkyns", "Jennings",
        "Jerome", "John", "Johnson", "Johnston", "Jones", "Jonze",
        "Jopson", "Jordan", "Jordison", "Joyce", "Kalinic",
        "Kaminska", "Kamm", "Kane", "Kao", "Kardew", "Katz",
        "Kaufman", "Kazmin", "Keats", "Keaveny", "Keeley", "Kellaway",
        "Keller", "Kelly", "Kempe", "Kendall", "Kennedy", "Kenyon",
        "Keohane", "Kerevan", "Kerr", "Kettle", "Keynes", "Kidd",
        "Kinahan", "King", "Kingsley", "Kinnock", "Kipling", "Kirby",
        "Kirkup", "Kitchener", "Kitson", "Klein", "Klimes", "Knapman",
        "Knapton", "Knight", "Korda", "Koren", "Koster", "Kuchler",
        "Kwong", "Kyle", "Laermer", "Laing", "Laitner", "Laity",
        "Lamb", "Lambert", "Lammin", "Lamont", "Lancaster", "Lang",
        "Langtry", "Lapinski", "Lascelles", "Laski", "Latham",
        "Lauder", "Laughland", "Laughton", "Laurance", "Lavery",
        "Law", "Lawrence", "Lawrenson", "Lawson", "Lea", "Leadsom",
        "Lear", "Lecky", "Lee", "Lefroy", "Leigh", "Lennon", "Leno",
        "Leroux", "Leslie", "Lethaby", "Letts", "Letwin", "Lever",
        "Lewell", "Lewis", "Leybourne", "Liddell", "Lidington",
        "Lilia", "Lilley", "Lind", "Lindley", "Lindsay", "Lindsey",
        "Linnell", "Lipton", "Lister", "Liston", "Lloyd", "Loach",
        "Lockyer", "Long", "Lord", "Lorincz", "Loudon", "Loughton",
        "Lovelace", "Lover", "Lovett", "Low", "Lowe", "Lowes",
        "Lubbock", "Lucan", "Lucas", "Luce", "Ludlow", "Lugard",
        "Lumley", "Lusher", "Lutyens", "Lutz", "Lyell", "Lynch",
        "Lyons", "Lythe", "Lytton", "Maber", "MacDonald", "MacDonogh",
        "MacInnes", "MacKenzie", "MacNeice", "MacNeil", "Macalister",
        "Macaskill", "Macaulay", "Macdonald", "Macintyre",
        "Mackenzie", "Mackie", "Mackinlay", "Mackintosh", "Macklin",
        "Mackrell", "Macmillan", "Mactaggart", "Madders", "Maddocks",
        "Maggs", "Maguire", "Mahoney", "Main", "Mairs", "Maitland",
        "Mak", "Makepeace", "Mallet", "Mallon", "Malone", "Malthouse",
        "Malvern", "Manby", "Mance", "Mangan", "Manger", "Mann",
        "Manning", "Mansbridge", "Mansfield", "Manson", "Marc",
        "Margetson", "Margolis", "Marlow", "Marris", "Marryat",
        "Marsden", "Marsh", "Martin", "Martinson", "Martosko", "Marx",
        "Masefield", "Maskell", "Maskey", "Mason", "Masters",
        "Matheson", "Mathias", "Matthay", "Matthewson", "Matthias",
        "Maugham", "Maurice", "Maxim", "Maxwell", "May", "Mayer",
        "Mayhew", "Maynard", "Mc Nally", "McAlinden", "McCabe",
        "McCaig", "McCann", "McCarthy", "McCartney", "McConnell",
        "McCormack", "McCormick", "McCrum", "McCullin", "McCurry",
        "McDonagh", "McDonald", "McDonnell", "McFadden", "McGarry",
        "McGee", "McGill", "McGinn", "McGoogan", "McGovern",
        "McGreal", "McGuire", "McIndoe", "McInnes", "McIntosh",
        "McKinnell", "McKnight", "McLannahan", "McLaughlin",
        "McLoughlin", "McMahon", "McMillan", "McMullan", "McNeill",
        "McPartland", "McPhee", "McRae", "McVeigh", "Mckernan",
        "Mcveigh", "Meade", "Meale", "Mearns", "Medawar", "Mee",
        "Melba", "Melville", "Mendelssohn", "Menzies", "Mercer",
        "Meredith", "Merrick", "Merriman", "Metcalfe", "Mews",
        "Meyer", "Meynell", "Michel", "Midgley", "Milburn",
        "Miliband", "Mill", "Millais", "Miller", "Milling", "Mills",
        "Millward", "Milman", "Milne", "Milner", "Milstein", "Milton",
        "Minot", "Misiri", "Mitchell", "Mitford", "Moffat", "Mogg",
        "Molloy", "Monaghan", "Monbiot", "Monckton", "Monk",
        "Montgomerie", "Moodie", "Moody", "Moon", "Mooney", "Moore",
        "Moorhead", "Moran", "Mordaunt", "Morden", "Morgan", "Morley",
        "Morrell", "Morris", "Morrison", "Morrissey", "Morse",
        "Mortimer", "Morton", "Moseley", "Moss", "Mostrous", "Moules",
        "Mountbatten", "Mowat", "Moynihan", "Muir", "Muirhead",
        "Mulholland", "Mullen", "Mullin", "Mumford", "Mundell",
        "Mundy", "Munk", "Munro", "Murdoch", "Murphy", "Murray",
        "Murrison", "Murrow", "Murry", "Musson", "Myall", "Myers",
        "Nandy", "Nardelli", "Nash", "Nauman", "Neate", "Needham",
        "Neill", "Nelson", "Newall", "Newbolt", "Newlands", "Newman",
        "Newton", "Nicholl", "Nicholls", "Nicholson", "Nicoll",
        "Nicolson", "Nightingale", "Nilsson", "Noble", "Noblett",
        "Nokes", "Nolan", "Nollekens", "Noonan", "Norman",
        "Northcliffe", "Northedge", "Novello", "Nuttall", "O'Carroll",
        "O'Casey", "O'Connell", "O'Connor", "O'Hara", "O'Higgins",
        "O'Neill", "O'Sullivan", "Offord", "Ogden", "Oldfield",
        "Oliphant", "Oliver", "Onslow", "Opperman", "Orpen", "Orr",
        "Ortiz", "Orwell", "Osamor", "Osborne", "Osterberg", "Oswald",
        "Owen", "O'Donovan", "O'Grady", "Pagano", "Page",
        "Paisley", "Paleit", "Paley", "Palgrave", "Palmer",
        "Pankhurst", "Parish", "Parker", "Parkinson", "Parr",
        "Parrish", "Parry", "Parsons", "Paterson", "Patron", "Pauley",
        "Pauli", "Pavia", "Pawsey", "Payne", "Peabody", "Peake",
        "Pearce", "Pearson", "Peel", "Peev", "Pelham", "Pemberton",
        "Penning", "Pennycook", "Penrose", "Perceval", "Percy",
        "Perkins", "Perrone", "Perry", "Peters", "Petridis", "Petrie",
        "Petty", "Pevsner", "Pflanz", "Phelps", "Philby", "Phillips",
        "Phillipson", "Philp", "Philpot", "Phipps", "Pick", "Pickard",
        "Pickles", "Pickover", "Pilkington", "Pilling", "Pincher",
        "Pinker", "Pisa", "Pissarro", "Pitcher", "Pitt", "Place",
        "Plath", "Platt", "Playfair", "Plunkett", "Politi", "Pollack",
        "Poole", "Pooler", "Pope", "Popper", "Porter", "Potton",
        "Poulter", "Pound", "Pow", "Powell", "Powley", "Precedo",
        "Prentis", "Prescott", "Pressburger", "Price", "Priestley",
        "Prigg", "Primrose", "Prince", "Prior", "Prisk", "Pritchard",
        "Protheroe", "Pruitt", "Pryde", "Prynne", "Pugh", "Pulham",
        "Pulver", "Pursglove", "Quin", "Quince", "Quine", "Quinn",
        "Raab", "Rachman", "Rackham", "Radcliffe", "Raeside",
        "Raffensperger", "Rahman", "Ralph", "Ram", "Rambert",
        "Ramsay", "Randall", "Randerson", "Rank", "Rathbone",
        "Rattigan", "Raval", "Rawnsley", "Rayner", "Redden",
        "Redmayne", "Redwood", "Reed", "Rees", "Reeves", "Reilly",
        "Reith", "Relph", "Rennison", "Rentoul", "Reynolds", "Rhys",
        "Ricardo", "Richard Green", "Richards", "Richardson",
        "Richmond", "Rickard", "Ricketts", "Rickman", "Riddell",
        "Ridge", "Rifkind", "Rigby", "Riley", "Rimmer", "Ritchie",
        "Roberts", "Robertson", "Robeson", "Robey", "Robinson",
        "Robson", "Roderick", "Rodionova", "Roe", "Rogers", "Rolls",
        "Romilly", "Romney", "Rose", "Rosenberg", "Rosindell", "Ross",
        "Rossetti", "Rossi", "Rossington", "Rothenstein", "Rotheram",
        "Rovnick", "Rowlandson", "Rowley", "Roy", "Rudd", "Ruddick",
        "Runcie", "Rushe", "Rushton", "Ruskin", "Russell",
        "Rutherford", "Rutley", "Ryan", "Ryder", "Sabbagh",
        "Sackville", "Salmond", "Salter", "Salvin", "Sample",
        "Samson", "Samuel", "Sandbach", "Sanderson", "Santley",
        "Sargent", "Sassoon", "Saul", "Saunders", "Savage", "Saville",
        "Sawer", "Sawyer", "Sayers", "Scaggs", "Schipani",
        "Schlesinger", "Schofield", "Schulz", "Schwab", "Scoggins",
        "Scott", "Scully", "Seacole", "Seamons", "Seddon", "Segars",
        "Segrave", "Selby", "Selfridge", "Selous", "Service",
        "Shackleton", "Shainin", "Shannon", "Shapiro", "Shapps",
        "Sharp", "Shaw", "Shearlaw", "Sheen", "Sheerman", "Sheffield",
        "Shelbrooke", "Shelley", "Shenker", "Shepard", "Shepherd",
        "Sheppard", "Sheraton", "Sheridan", "Sherlock", "Sherriff",
        "Short", "Shrimsley", "Shubber", "Sibun", "Sickert", "Silver",
        "Silverman", "Sim", "Simon", "Simons", "Simpson", "Sims",
        "Sissons", "Sitwell", "Skidmore", "Skinner", "Skypala",
        "Slaughter", "Sloane", "Smart", "Smeeth", "Smillie", "Smirke",
        "Smith", "Smithers", "Smithson", "Smollett", "Smyth", "Snell",
        "Snoddy", "Snowdon", "Soames", "Solloway", "Solomon",
        "Solomons", "Sopwith", "Sorrell", "Soubry", "Sparrow",
        "Spellar", "Spelman", "Spence", "Spencer", "Sperling",
        "Spiegel", "Spilsbury", "Spink", "Spolar", "Spry", "Spurgeon",
        "Squires", "Stabe", "Stacey", "Stafford", "Stanfield",
        "Stanford", "Stanhope", "Stanley", "Starkey", "Starmer",
        "Staunton", "Steer", "Steiner", "Stephen", "Stephens",
        "Stephenson", "Stern", "Stevens", "Stevenson", "Stewart",
        "Stidder", "Still", "Stoddart", "Stoker", "Stone", "Stones",
        "Stopes", "Stothard", "Strang", "Straus", "Street",
        "Streeter", "Streeting", "Stride", "Stringer", "Strydom",
        "Stuart", "Studemann", "Sturdy", "Sunderland", "Swaine",
        "Swarbrick", "Swash", "Swayne", "Sweeney", "Sweney",
        "Swinburne", "Swinford", "Swire", "Sylvester", "Symonds",
        "Syms", "Szabo", "Tait", "Tallis", "Tami", "Tapsfield",
        "Tarrant", "Tassell", "Taylor", "Telford", "Tempest",
        "Temple", "Tennyson", "Terry", "Tertis", "Tett", "Thackeray",
        "Thewliss", "Thomas", "Thompson", "Thomson", "Thornberry",
        "Thorndike", "Thorne", "Thornhill", "Thornycroft", "Thorpe",
        "Throup", "Tickel", "Tilbury", "Tilney", "Timm", "Timms",
        "Timpson", "Titcomb", "Titmuss", "Tobin", "Tolhurst",
        "Tomlinson", "Toonkel", "Topping", "Tovey", "Townley",
        "Toynbee", "Tracey", "Travis", "Treanor", "Tredinnick",
        "Tremlett", "Trevelyan", "Treves", "Trickett", "Trollope",
        "Trombetta", "Troughton", "Truss", "Tuck", "Tucker", "Turing",
        "Turley", "Turnbull", "Turner", "Twain", "Tweed", "Twigg",
        "Tyrie", "Underhill", "Unwin", "Usborne", "Uttley", "Valenti",
        "Vane", "Vara", "Vasagar", "Vaughan", "Ventris", "Vickers",
        "Vidal", "Villiers", "Vincent", "Vine", "Viner", "Von Hugel",
        "Voysey", "Wade", "Wainwright", "Waithe", "Wakley", "Walker",
        "Wallace", "Waller", "Wallis", "Walpole", "Walport", "Walsh",
        "Walter", "Walters", "Walton", "Wang", "Warburton", "Ward",
        "Ware", "Warlock", "Warman", "Warner", "Warrell", "Warwick",
        "Waterfield", "Waterhouse", "Waters", "Watkins", "Watkinson",
        "Watson", "Watts", "Waugh", "Weale", "Wearden", "Weaver",
        "Webb", "Webster", "Weinberg", "Weinland", "Weir", "Weisz",
        "Welch", "Wellcome", "Wells", "Wembridge", "Wentworth",
        "Wesley", "West", "Westmacott", "Wharton", "Whateley",
        "Whately", "Wheatley", "Wheatstone", "Wheeler", "Whipple",
        "Whistler", "Whitaker", "White", "Whiteford", "Whitehead",
        "Whitelaw", "Whitelocks", "Whitford", "Whittaker", "Whittell",
        "Whittingdale", "Whittle", "Whitworth", "Whyld", "Wiggin",
        "Wigglesworth", "Wilberforce", "Wilde", "Willan", "Williams",
        "Williamson", "Willis", "Willoughby", "Wilson", "Winant",
        "Winch", "Wingfield", "Winnick", "Winslet", "Winter",
        "Winterton", "Wintour", "Wiseman", "Wishart", "Withnall",
        "Wodehouse", "Wolf", "Wolfe", "Wolff", "Wolffe", "Wollaston",
        "Wolseley", "Wood", "Woodcock", "Woode", "Wooding", "Woods",
        "Woolf", "Woolley", "Wootton", "Worroll", "Wragg", "Wren",
        "Wright", "Wroe", "Wyatt", "Wyett", "Wyndham", "Wynne",
        "Yates", "Yeats", "Yeo", "Yeomans", "Young", "Younge",
        "Zeichner", "Ziegler", "Zola", "d'Ancona", "de Bono",
        "de Bruxelles", "de Klerk", "van der Post",
        "Aitkenhead", "Armitstead", "Arterton", "Bates",
        "Beckerman", "Benwell", "Binns", "Brennan", "Buckley",
        "Cairnie", "Carr", "Coddington", "Collingridge", "Crisp",
        "Cusk", "Deacon", "Foote", "Fordham", "Greer", "Grice",
        "Harrowing", "Howse", "Mallinson", "McKinstry", "McCall",
        "McDonagh", "Montgomery", "Mountford", "Mulligan", "O'Brien",
        "O'Donnell", "O'Toole", "O’Grady", "Patterson", "Peach",
        "Reid", "Rudgard", "Serota", "Shute", "Simnett",
        "Slater", "Slater", "Snowden", "Steele", "Tindall",
        "Titchener", "Tully", "Vinter", "Washtell", "Winfield", 
        "Woodward", "Worthington", "Balfour", "Ellmore-Jones",
        "Feeley", "Gadhavi", "Romero", "Thatcher",
        #added for 2019
        #from the Nigel Molesworth/St Custards books               
        "Molesworth", # Nigel Molesworth, the self-styled "curse of st custards" and "gorila of 3B"
        "Peason", # Molesworth's "grate frend"
        "Gillibrand", # another of Molesworth's classmates
        "Grabber", # Head boy of the School, "captane of everything" (especially "foopball") and "winer of the mrs joyful prize for rafia work".
        "Fotherington-Tomas", # A goody-goody, a wet and a weed.
        "Grimes", # Headmaster GRIMES [sic]. 
        "Arbuthnot" # Sigismund Arbuthnot, the mad maths master
              )


#### SPANISH NAMES ####

# 115 Spanish female first names.
female_firstnames_Spanish = (
        #Students of the World
        #http://www.studentsoftheworld.info/penpals/stats.php3?Pays=ESP
        #Top 100 Spanish names - Spain 
        "Adriana", "Aida", "Aina", "Ainhoa", "Ainoa", "Alejandra", "Alexandra",
        "Alicia", "Almudena", "Amanda", "Ana", "Ana María", "Anabel", "Andrea", "Ane", "Angela",
        "Anna", "Ariadna", "Aurora", "Bea", "Beatriz", "Belen", "Blanca", "Carla", "Carmen",
        "Carolina", "Celia", "Clara", "Clàudia", "Cristina", "Daniela", "Diana", "Elena", "Emma",
        "Esther", "Eva", "Fatima", "Gema", "Gloria", "Helena", "Inma", "Inés", "Irati", "Irene",
        "Isa", "Isabel", "Jennifer", "Jessica", "Judit", "Judith", "Julia", "Laia", "Lara", "Laura",
        "Leire", "Lidia", "Lorena", "Lucia", "Luna", "Maite", "Mar", "Mari", "Maria", "Marina", "Marta",
        "Mery", "Mireia", "Miriam", "Mònica", "Naiara", "Natalia", "Nerea", "Noelia", "Nora", "Nuria",
        "Olga", "Paloma", "Patri", "Patricia", "Paula", "Pàola", "Raquel", "Rocío", "Rosa", "Sandra",
        "Sara", "Silvia", "Sofía", "Sonia", "Stella", "Tamara", "Tania", "Uxue", "Vanessa", "Verónica",
        "Vicky", "Victoria", "Yaiza",
        #from famous_spaniards
        "Adelina", "Amaia", "Conchita", "Dolores", "Federica", "Lola", "Lolita", "Lydia",
        "Margarita", "María", "Niña", "Susana", "Teresa",
        #more from famous_spaniards
        "Elia", "Icíar", "Luz", "Pilar")

# 165 Spanish male first names.
male_firstnames_Spanish = (
        #Students of the World
        #http://www.studentsoftheworld.info/penpals/stats.php3?Pays=ESP
        #Top 100 Spanish names - Spain 
        #Boys first names
        "Adrian", "Aimar", "Albert", "Alberto", "Alejandro", "Alex", "Ander",
        "Andrés", "Andy", "Angel", "Antonio", "Arnau", "Asier", "Beñat", "Borja", "Bruno",
        "Carlos", "Christian", "Cristian", "Dani", "Daniel", "Dario", "David", "Diego",
        "Domingo", "Egoitz", "Eneko", "Enrique", "Fernando", "Fran", "Francisco", "Gabriel",
        "Gonzalo", "Gorka", "Guille", "Guillermo", "Hugo", "Ibai", "Ignacio", "Iker",
        "Ismael", "Ivan", "Jaime", "Javi", "Javier", "Jesús", "Joaquin", "Jon", "Jorge", "Jose",
        "Jose Luis", "Jose Manuel", "Jose Miguel", "Josep", "Juan", "Juan Carlos", "Juanma",
        "Julen", "Kevin", "Lucas", "Luis", "Manolo", "Manu", "Manuel", "Marc", "Marcelo", "Marco",
        "Marcos", "Mario", "Martin", "Mateo", "Max", "Miguel", "Miguel Angel", "Mohamed", "Nacho",
        "Nicolas", "Pablo", "Paco", "Paul", "Pedro", "Pepe", "Pol", "Rafa", "Rafael", "Raul",
        "Roberto", "Ruben", "Samuel", "Santi", "Saul", "Sergi", "Sergio", "Tomas", "Toni",
        "Unai", "Victor", "Álvaro", "Óscar",
        #from famous_spaniards
        "Adolfo", "Alfredo", "Alonso", "Ambrosio", "Arturo", "Baltasar", "Bartolomé", "Benito", 
        "Bernardo", "Bernardino", "Camilo", "Celestino", "César", "Damián", "Eduardo", "Esteban", 
        "Felipe", "Félix", "Garcilaso", "Gerardo", "Gonzalo", "Gregorio", "Hernando", "Iván", 
        "Jerónimo", "Joaquín", "José", "Julián", "Juan Carlos", "Julio", "Leopoldo", "Nicolás", 
        "Rodrigo", "Salvador", "Vicente",  "Víctor", "Wifredo", "Xavier", "Eduardo", "Florentino",
        "Francesco", "Sebastián",
        #more from famous_spaniards
        "Agustí", "Ángel", "Buenaventura", "Dámaso", "Ferran", "Gaspar", "Hernán", "Hipólito",
        "Jacinto", "Jaume", "Joanot", "Jordi", "Mariano", "Mateu", "Montxo", "Narcís", "Nino",
        "Pedrarias", "Pío", "Santiago", "Severo", "Blas", "Camarón", "Camilo")

# 390 Spanish male first names.
surnames_Spanish = (
        #296 Spanish Surnames
        #from http://surnames.behindthename.com/names/usage/spanish
        "Abarca", "Abaroa", "Abascal", "Abasolo", "Abel", "Abelló", "Abraham",
        "Abreu", "Acosta", "Agramunt", "Agua", "Aguado", "Aiza", "Alamilla", "Albert",
        "Aldana", "Alfaro", "Alvarado", "Álvarez", "Amador", "Andrés", "Andreu", "Antúnez",
        "Aquino", "Araujo", "Araya", "Arce", "Arechavaleta", "Arenas", "Aritza", "Armando",
        "Arreola", "Arriola", "Asís", "Asturias", "Azarola", "Banderas", "Barros", "Basurto",
        "Bautista", "Bello", "Belmonte", "Bengochea", "Benitez", "Bermúdez", "Blanco",
        "Blanxart", "Bolívar", "Bonaventura", "Bosque", "Bustillo", "Busto", "Bustos",
        "Cabello", "Cabrera", "Campo", "Campos", "Capello", "Cardona", "Caro", "Casales",
        "Castell", "Castellano", "Castillion", "Castillo", "Castro", "Chavarría", "Chavez",
        "Colón", "Costa", "Crespo", "Cruz", "Cuéllar", "Cuesta", "Cuevas", "D'cruz", "D'cruze",
        "Delgado", "Díaz", "Dominguez", "Duarte", "Durante", "Echevarría", "Echeverría", "Elizondo",
        "Escamilla", "Escárcega", "Escarrà", "Esparza", "Espina", "Espino", "Espinosa", "Espinoza",
        "Estévez", "Etxebarria", "Etxeberria", "Félix", "Fernández", "Ferrer", "Fierro", "Flores",
        "Fonseca", "Franco", "Fuentes", "Gallego", "Gallo", "García", "Garrastazu", "Garza", "Gaspar",
        "Gebara", "Gomez", "Gonzales", "Gonzalez", "Grec", "Guadarrama", "Guerra", "Guerrero", "Guerrera",
        "Gutiérrez", "Gutierrez", "Hernandez", "Herrera", "Herrero", "Hierro", "Holguín", "Huerta",
        "Ibáñez", "Ibarra", "Iñíguez", "Iturburua", "Jaso", "Jasso", "Jimenez", "Jordà", "Juárez",
        "Lobo", "Lopez", "Losa", "Loyola", "Lucas", "Machado", "Macías", "Maradona", "María", "Marino",
        "Márquez", "Martell", "Martí", "Martínez", "Means", "Martinez", "Mas", "Mata", "Mateu",
        "Medina", "Melendez", "Méndez", "Mendoza", "Menendez", "Merlo", "Michel", "Mingo",
        "Moles", "Molina", "Montero", "Morales", "Moralez", "Moreno", "Narváez", "Nieves",
        "Noguerra", "Núñez", "Obando", "Ochoa", "Ojeda", "Ola", "Oleastro", "Olguin",
        "Oliver", "Olmos", "Oquendo", "Orellana", "Oriol", "Ortega", "Ortiz", "Palomo", "Paredes",
        "Pavia", "Peláez", "Peña", "Pérez", "Perez", "Petit", "Picasso", "Porra", "Porras", "Prieto",
        "Puerta", "Puga", "Puig", "Quinones", "Quintana", "Quirós", "Ramírez", "Ramos", "Rana",
        "Rendón", "Rey", "Reyes", "Rios", "Rivera", "Rivero", "Robledo", "Robles", "Rocha", "Rodríguez",
        "Rodriquez", "Roig", "Rojas", "Rojo", "Roldán", "Romà", "Romà", "Romero", "Rosa", "Rosales",
        "Rubio", "Ruiz", "Sala", "Salamanca", "Salazar", "Salcedo", "Salinas", "Sanchez", "Sandoval",
        "San Nicolas", "Santana", "Santiago", "Santillian", "Santos", "Sastre", "Sepúlveda", "Sierra",
        "Silva", "Soler", "Solo", "Solos", "Soto", "Suárez", "Suero", "Tapia", "Terrazas", "Tomàs",
        "Torres", "Tos", "Tosell", "Toset", "Travieso", "Trujillo", "Ubina", "Urbina", "Ureña",
        "Valdez", "Valencia", "Varela", "Vargas", "Vásquez", "Vega", "Vela", "Vela", "Velazquez",
        "Ventura", "Vicario", "Vilaró", "Villa", "Villalobos", "Villanueva", "Villaverde", "Viola",
        "Viteri", "Vivas", "Vives", "Ybarra", "Zabala", "Zambrano", "Zamorano", "Zapatero", "Zavala",
        "Zubizarreta", "Zuñiga",
        #from famous_spaniards
        "Algué", "Aragón", "Aznar", "Ballester", "Bardem", "Barraquer", "Bautista", "Bayona", "Bazán",
        "Bécquer", "Berlanga", "Borau", "Botas", "Cabrillo", "Calderón", "Carandell", "Casado", "Castañón",
        "Castaños", "Cela", "Churruca", "Cidon", "Corominas", "Cortés", "Cruz", "Díaz", "Díaz", "Díez",
        "Domínguez", "Dragó", "Durán", "Elcano", "Espinosa", "Figuerola", "Gaite", "Galdós", "Galván",
        "Gaona", "García", "Gómez", "González", "Guerrero", "Gutiérrez", "Herrera", "Hortega", "Ibáñez",
        "Iriarte", "Jiménez", "Jiménez", "Lorca", "Martínez", "Méndez", "Menéndez", "Montalbán", "Montes",
        "Montiel", "Moreto", "Motiño", "Mutis", "Nágera", "Navarro", "Núñez", "Núñez", "Núñez", "Ocaña",
        "Ordinas", "Ortega", "Ortega", "Osorio", "Pacheco", "Palacios", "Pelayo", "Perales", "Pérez",
        "Pidal", "Pinzón", "Quevedo", "Ramírez", "Robusté", "Rodriguez", "Rodríguez", "Ruiz", "Sáenz",
        "Samaniego", "Sánchez", "Sanz", "Sasturain", "Serrat", "Torres", "Trujillo", "Vallejo", "Vasquez", 
        "Vásquez", "Vidal", "Vila", "Yanes", "Zafón", "Zapatero", "Zorrilla")

#Spaniards often have two surnames, or surnames made up of multiple words...
surnames_Spanish_long = ("Comas i Solà", "de Aguirre", "de Alarcón", "de Almagro", "de Anza", "de Ávila",
        "de Ayanz y Beaumont", "de Balboa", "de Bazán", "de Belalcázar", "de Berlanga", "de Burgos",
        "de Castilla", "de Castro", "de Cervantes", "de Chomón", "de Córdoba", "de Coronado", "de Elhúyar",
        "de Enzinas", "de Espinosa", "de Espronceda", "de Falla", "de Gálvez", "de Góngora", "de Heredia",
        "de Jovellanos", "de la Barca", "de la Cierva", "De La Cruz", "de la Fuente", "De La Fuente",
        "de la Iglesia", "de la Isla", "de la Serna", "de la Vega", "de la Vega", "de Larra", "de Larrocha",
        "de Las Casas", "de Laserna", "de Legazpi", "De Leon", "de León", "de Lezo", "de los Ángeles",
        "de Lucía", "de Madariaga", "De Miranda", "de Molina", "de Moratín", "de Nebrija", "de Orellana",
        "de Pablo", "de Portilla y Esquivel", "de Portolà", "de Quevedo", "de Rojas", "de Sahagún",
        "de San Martin", "De Santigo", "de Soto", "de Tena", "de Ulloa", "de Unamuno", "de Valdivia",
        "de Victoria", "de Vivar", "de Zayas y Sotomayor", "del Alcázar", "Del Bosque", "Del Olmo",
        "del Pópulo", "del Río", "del Rio", "Gabriel y Galán", "León de Aranoa", "Lope de Vega",
        "Martín y Soler", "Moreto y Cavana", "Ortega y Gasset", "Pi i Margall", "Pi y Arsuaga",
        "Ponce de León", "Primo de Rivera", "Ramón y Cajal", "Terradas i Illa", "Zorrilla y Moral")

# famous Spaniards
# pulled from Wikipedia...
# https://en.wikipedia.org/wiki/List_of_Spaniards
# 336 famous Spanish people
# USE FOR SHIP NAMING ETC
famous_spaniards = ("Abraham Castanho", "Adelina Patti", "Adolfo Suárez", "Aguas Santas Ocaña Navarro",
        "Agustí Villaronga", "Agustín Díaz Pacheco", "Agustín Díaz Yanes", "Agustín Moreto y Cavana",
        "Agustín Sánchez Vidal", "Alberto Vázquez-Figueroa", "Alejandro Amenábar", "Alejandro Casona",
        "Alejandro Sanz", "Álex de la Iglesia", "Alexander Farnese", "Alfredo Kraus", "Alicia de Larrocha",
        "Alonso Vázquez", "Álvar Núñez Cabeza de Vaca", "Álvaro de Bazán", "Álvaro Navia-Osorio Vigil",
        "Amaia Montero", "Amancio Ortega Gaona", "Amando de Ossorio", "Amaro Rodríguez Felipe",
        "Ambrosio Spinola", "Ana Belén", "Ana Maiques", "Ana Torroja", "Andrés Manuel del Río",
        "Andrés Segovia", "Ángel Cabrera", "Antonio Buero Vallejo", "Antonio Corti", "Antonio de Nebrija",
        "Antonio de Ulloa", "Antonio Escohotado Espinosa", "Antonio Gala", "Antonio José Cortés",
        "Antonio Machado", "Antonio Soler", "Arturo Pérez-Reverte", "Baltasar del Alcázar",
        "Baltasar Gracián", "Bartolomé de Las Casas", "Bartolomé Ruiz", "Benito Pérez Galdós",
        "Benito Zambrano", "Bernardino de Sahagún", "Bernardo de Gálvez", "Bernardo Hernández",
        "Bigas Luna","Blas de Laserna", "Blas de Lezo", "Buenaventura Durruti", "Camarón de la Isla",
        "Camilo José Cela", "Camilo Sesto", "Carlos Atanes", "Carlos D. Cidon", "Carlos Fernández Casado",
        "Carlos Jiménez Díaz", "Carlos Marín", "Carlos Núñez", "Carlos Rojas Vila", "Carlos Ruiz Zafón",
        "Carlos Saura", "Carmen Martín Gaite", "Casto Méndez Núñez", "César Mallorquí", "Conchita Supervía",
        "Cosme Damián Churruca", "Dámaso Alonso", "David Bisbal", "David Trueba", "Diego de Almagro",
        "Diego Salcedo", "Dolores Ibárruri", "Dolores Soler-Espiauba", "Eduardo Mendoza", "Eduardo Torroja",
        "Elia Barceló", "Emilia Pardo Bazán", "Enrique Granados", "Enrique Iglesias", "Enrique Jordá",
        "Enrique Rojas Montes", "Enrique Tierno Galván", "Enrique Urquijo", "Esteban Terradas i Illa",
        "Esther Cañadas", "Eva Amaral", "Federica Montseny", "Federico García Lorca", "Felipe González",
        "Félix Lope de Vega", "Félix María Samaniego", "Félix Rodríguez de la Fuente", "Fernando de Rojas",
        "Fernando Fernán Gómez", "Fernando León de Aranoa", "Fernando Sánchez Dragó", "Fernando Savater",
        "Fernando Trueba", "Fernando Trujillo Sanz", "Ferran Adrià", "Francesc Pi i Margall", "Francisco Ayala",
        "Francisco de Enzinas", "Francisco de Orellana", "Francisco de Quevedo", "Francisco de Rojas Zorrilla",
        "Francisco Franco", "Francisco Hernández", "Francisco Javier Castaños", "Francisco Lara",
        "Francisco Martínez Motiño", "Francisco Pi y Arsuaga", "Francisco Pizarro", "Francisco Suárez",
        "Francisco Tárrega", "Francisco Vásquez de Coronado", "Francisco Viñas", "Fray Luis de León",
        "Fray Tomás de Berlanga", "Gabriel de Castilla", "Garcilaso de la Vega", "Gaspar de Espinosa",
        "Gaspar de Portolà", "Gaspar Melchor de Jovellanos", "Gaspar Sanz", "George Santayana",
        "Gerardo Diego", "Gonzalo Fernández de Córdoba", "Gonzalo Torrente Ballester", "Gregorio Marañón",
        "Gustavo Adolfo Bécquer", "Hernán Cortés", "Hernando de Soto", "Hipólito Lázaro", "Icíar Bollaín",
        "Ignacio Aldecoa", "Ignacio Barraquer", "José Ignacio Barraquer", "Inés Sastre", "Isaac Albéniz",
        "Isaac Peral", "Isabel Coixet", "Isabel Pantoja", "Iván Zulueta", "Jacinto Benavente", "Jaime Ferrán",
        "Jaume Balagueró", "Javier Cosnava", "Javier Marías", "Javier Solana", "Jerónimo de Ayanz y Beaumont",
        "Jesús Franco", "Joan Manuel Serrat", "Joan Oró", "Joanot Martorell", "Joaquín Cortés", "Joaquín Rodrigo",
        "Joaquín Sabina", "Joaquín Turina", "Jon Juaristi", "Jon Kortajarena", "Jordi Savall", "Jorge Guillén",
        "Jorge Juan y Santacilia", "Jorge Manrique", "Jose Andrés", "José Antonio Primo de Rivera",
        "José Carreras", "José Celestino Bruno Mutis", "José de Espronceda", "José Echegaray", "José Luis Borau",
        "José Luis Garci", "José Luis Perales", "José Luis Perales", "José Luis Rodríguez Zapatero",
        "José Luis Sáenz de Heredia", "José Mallorquí Figuerola", "José Manuel Castañón", "José María Algué",
        "José María Aznar", "José María Gabriel y Galán", "José Martínez Ruiz", "José Monje Cruz",
        "José Ortega y Gasset", "José Zorrilla y Moral", "Josep Comas i Solà", "Josep Trueta",
        "Juan Antonio Bardem", "Juan Antonio Bayona", "Juan Antonio Ramírez Domínguez",
        "Juan Antonio Vallejo-Nágera Botas", "Juan Bautista de Anza", "Juan Bermúdez", "Juan de la Cierva",
        "Juan García Hortelano", "Juan González Mesa", "Juan Goyanarte", "Juan Ignacio Cirac Sasturain",
        "Juan José de Elhúyar", "Juan Luis Vives", "Juan March Ordinas", "Juan Marsé", "Juan Martín Díez",
        "Juan Ponce de León", "Juan Pujol", "Juan Ramón Jiménez", "Juan Rodríguez Cabrillo",
        "Juan Ruiz de Alarcón", "Juan Sebastián Elcano", "Juanma Bajo Ulloa", "Judit Mascó", "Julián Marías",
        "Julio Iglesias", "Julio Médem", "Julio Palacios Martínez", "Julio Rey Pastor",
        "Leandro Fernández de Moratín", "Leonardo Torres Quevedo", "Leopoldo Alas", "Leopoldo Calvo-Sotelo",
        "Lola Flores", "Lolita Flores", "Lope de Aguirre", "Luis Buñuel", "Luis Carandell Robusté",
        "Luis de Góngora", "Luis de Pablo", "Luis García Berlanga", "Luis Romero", "Luz Casal",
        "Lydia Zimmermann", "Manolo García", "Manuel Azaña", "Manuel de Falla", "Manuel del Pópulo Vicente García",
        "Manuel Gutiérrez Aragón", "Manuel Jalón Corominas", "Manuel Vázquez Montalbán", "Marcelino Menéndez Pelayo",
        "Margarita Salas", "María de Zayas y Sotomayor", "María Dueñas", "María Gay", "María José Montiel",
        "María Rosa García", "María Teresa Fernández de la Vega", "Mariano José de Larra", "Mariano Rajoy",
        "Marina Pérez", "Mario Camus", "Mateo Alemán", "Mateu Orfila", "Miguel Bosé", "Miguel de Cervantes",
        "Miguel de Portilla y Esquivel", "Miguel de Unamuno", "Miguel Delibes", "Miguel Hernández",
        "Miguel López de Legazpi", "Miguel Servet", "Montxo Armendáriz", "Nancy Fabiola Herrera",
        "Narcís Monturiol", "Nicolás Cabrera", "Niña Pastori", "Nino Bravo", "Pablo Alboran", "Pablo Casals",
        "Paco de Lucía", "Paloma San Basilio", "Paul Naschy", "Pedrarias Dávila", "Pedro Almodóvar",
        "Pedro Arias de Ávila", "Pedro Calderón de la Barca", "Pedro de Valdivia", "Pedro Duque",
        "Fausto de Elhúyar", "Pedro Navarro", "Pedro Salinas", "Pepe Rodríguez", "Pilar Miró", "Pío Baroja",
        "Pío del Río Hortega", "Plácido Domingo", "Rafael Alvarado Ballester", "Rafael Dieste",
        "Rafael Frühbeck de Burgos", "Rafael Gambra Ciudad", "Ramón Gómez de la Serna", "Ramón J. Sender",
        "Ramón María del Valle-Inclán", "Ramón Menéndez Pidal", "Ricardo Baeza Durán", "Rocío Dúrcal",
        "Rocío Jurado", "Rodrigo Rato", "Rodrigo Díaz de Vivar", "Ruy Díaz de Vivar", "Rosalía de Castro",
        "Salvador Bacarisse", "Salvador de Madariaga", "Salvador Fidalgo", "Santiago Calatrava",
        "Santiago Carrillo", "Santiago Ramón y Cajal", "Santiago Segura", "Sebastián de Belalcázar",
        "Segundo de Chomón", "Severo Ochoa", "Sheila Marquez", "Susana Agustí", "Tamara Rojo",
        "Teresa Berganza", "Tirso de Molina", "Tomás Luis de Victoria", "Torcuato Luca de Tena",
        "Vasco Núñez de Balboa", "Vicente Aleixandre", "Vicente Blasco Ibáñez", "Vicente Espinel",
        "Vicente Martín y Soler", "Vicente Yáñez Pinzón", "Víctor Erice", "Víctor Manuel",
        "Víctor Ruiz Iriarte", "Victoria de los Ángeles", "Wifredo Ricart", "Xavier Zubiri")




#### ITALIAN NAMES ####

# 116 Italian female first names.
female_firstnames_Italian = (
        #Students of the World
        # http://www.studentsoftheworld.info/penpals/stats.php3?Pays=ITA
        # Top 100 Italian names - Italy
        # Girls first names
        "Adele", "Alessandra", "Alessia", "Alice", "Angela",
        "Angelica", "Anita", "Anna", "Annalisa", "Antonella",
        "Arianna", "Aurora", "Barbara", "Beatrice", "Benedetta",
        "Bianca", "Camilla", "Carlotta", "Caterina", "Cecilia",
        "Chiara", "Claudia", "Cristina", "Daniela", "Daniele",
        "Debora", "Diana", "Elena", "Eleonora", "Elisa", "Elisabetta",
        "Emanuela", "Emma", "Erica", "Erika", "Eva", "Federica",
        "Francesca", "Gabriele", "Gabriella", "Gaia", "Giada",
        "Ginevra", "Gioia", "Giorgia", "Giovanna", "Giulia", "Giusy",
        "Gloria", "Greta", "Ilaria", "Ilenia", "Irene", "Isabella",
        "Jessica", "Julia", "Laura", "Letizia", "Linda", "Lisa",
        "Lucia", "Lucrezia", "Ludovica", "Luisa", "Manuela",
        "Margherita", "Maria", "Marika", "Marina", "Marta", "Martina",
        "Mary", "Marzia", "Matilde", "Melissa", "Michela", "Miriam",
        "Monica", "Nadia", "Nicole", "Noemi", "Paola", "Rachele",
        "Rebecca", "Roberta", "Rosa", "Sabrina", "Samantha", "Sara",
        "Sarah", "Serena", "Silvia", "Simona", "Sofia", "Sonia",
        "Stefania", "Teresa", "Valentina", "Valeria", "Vanessa",
        "Veronica", "Viola",
        #from famous_italians
        "Adelina", "Alida", "Catherine", "Clara", "Evangelista", "Gina", "Lina", "Mariangela", "Ornella",
        "Sandra", "Silvana", "Simonetta", "Sophia", "Virna") 

# 147 Italian female first names.
male_firstnames_Italian = (
        #Students of the World
        # http://www.studentsoftheworld.info/penpals/stats.php3?Pays=ITA
        # Top 100 Italian names - Italy
        #Boys first names
        #"Andrea",
        "Alberto", "Ale", "Alessandro", "Alessio", "Alex", "Angelo",
        "Antonio", "Carlo", "Carmine", "Christian", "Claudio",
        "Cristian", "Cristiano", "Cyril", "Damiano", "Daniel",
        "Dario", "Davide", "Denis", "Diego", "Domenico", "Edoardo",
        "Elia", "Elias", "Emanuele", "Emiliano", "Enrico", "Enzo",
        "Fabio", "Fabrizio", "Federico", "Filippo", "Flavio",
        "Francesco", "Gabriel", "Giacomo", "Gianluca", "Gianmarco",
        "Giorgio", "Giovanni", "Giulio", "Giuseppe", "Guido", "Ivan",
        "Jacopo", "John", "Kevin", "Leo", "Leonardo", "Lorenzo",
        "Luca", "Luciano", "Luigi", "Manuel", "Marco", "Mario",
        "Mark", "Martin", "Massimo", "Matteo", "Mattia", "Maurizio",
        "Mauro", "Max", "Michael", "Michele", "Mike", "Mirko",
        "Nicholas", "Nicola", "Nicolò", "Paolo", "Patrick", "Pier",
        "Piero", "Pietro", "Raffaele", "Riccardo", "Roberto",
        "Rosario", "Salvatore", "Samuel", "Samuele", "Saverio",
        "Sergio", "Simon", "Simone", "Stefano", "Thomas", "Tiziano",
        "Tom", "Tommaso", "Umberto", "Valerio", "Vincenzo", "Vito",
        "Vittorio",
        #from famous_italians
        "Achille", "Adolfo", "Aldo", "Alfredo", "Amedeo", "Bartolomeo", "Bernardo", "Bruno", "Camillo",
        "Cosimo", "Cristoforo", "Eduardo", "Elio", "Emilio", "Ettore", "Filippino", "Filoteo", "Fortunato",
        "Franco", "Gaspare", "Gian", "Giancarlo", "Gino", "Giordano", "Girolamo", "Guglielmo", "Ignazio",
        "Italo", "Leonetto", "Lodovico", "Luchino", "Marcello", "Muzio", "Niccolò", "Nino", "Onofrio",
        "Primo", "Rafael", "Romano", "Rosso", "Salvador", "Salvo", "Sandro", "Sebastiano", "Silvano",
        "Silvio", "Tomaso", "Ugo", "Vilfredo", "Vittore")

# 856 Italian surnames.
surnames_Italian = (
        #702 Italian Surnames
        #http://surnames.behindthename.com/names/usage/italian
        "Abano", "Abatangelo", "Abatantuono", "Abate","Abategiovanni",
        "Abatescianni", "Abbà", "Abbadelli", "Abbandonato",
        "Abbascia", "Abbatangelo", "Abbatantuono", "Abbate",
        "Abbatelli", "Abbaticchio", "Abbiati", "Abelli", "Abrami",
        "Abramo", "Acardi", "Accardi", "Accardo", "Acciai", "Acciaio",
        "Acciaioli", "Acconci", "Acconcio", "Accorsi", "Accorso",
        "Accursio", "Acerbi", "Acone", "Acqua", "Acquafredda",
        "Acquarone", "Acquati", "Adami", "Adamo", "Adamoli",
        "Addario", "Adelardi", "Adesso", "Adimari", "Adriatico",
        "Affini", "Africani", "Africano", "Agani", "Aggio", "Agli",
        "Agnelli", "Agnellini", "Agnusdei", "Agosti", "Agostini",
        "Agresta", "Agricola", "Aiello", "Aiolfi", "Airaldi", "Airò",
        "Aita", "Ajello", "Alagona", "Alamanni", "Albanesi", "Albani",
        "Albano", "Alberghi", "Alberghini", "Alberici", "Alberighi",
        "Albero", "Albini", "Albricci", "Albrici", "Aldebrandi",
        "Alderisi", "Alduino", "Alemagna", "Aleppo", "Alesci",
        "Alescio", "Alesi", "Alesini", "Alesio", "Alessandri",
        "Alessi", "Alfero", "Aliberti", "Alinari", "Aliprandi",
        "Allegri", "Allegro", "Alò", "Aloi","Aloia", "Aloisi",
        "Altamura", "Altimari", "Altoviti", "Alunni", "Amadei",
        "Amadori", "Amalberti", "Amantea", "Amato", "Amatore",
        "Ambrogi", "Ambrosi", "Amerighi", "Amoretto", "Angioli",
        "Ansaldi", "Anselmetti", "Anselmi", "Antonelli", "Antonini",
        "Antonino", "Aquila", "Aquino", "Arbore", "Ardiccioni",
        "Ardizzone", "Ardovini", "Arena", "Arlotti", "Armando",
        "Armani", "Armati", "Arnolfi", "Arnoni", "Arrighetti",
        "Arrighi", "Arrigucci", "Azzarà", "Baggi", "Baggio", "Baglio",
        "Bagni", "Bagnoli", "Balboni", "Baldi", "Baldini",
        "Baldinotti", "Baldovini", "Bandini", "Bandoni", "Barbieri",
        "Barone", "Barsetti", "Bartalotti", "Bartolomei",
        "Bartolomeo", "Barzetti", "Basile", "Bassanelli", "Bassani",
        "Bassi", "Basso", "Basurto", "Battaglia", "Bazzoli",
        "Bellandi", "Bellandini", "Bellincioni", "Bellini", "Bello",
        "Bellomi", "Belloni", "Belluomi", "Belmonte", "Bencivenni",
        "Benedetti", "Benenati", "Benetton", "Benini", "Benivieni",
        "Benvenuti", "Berardi", "Bergamaschi", "Berti", "Bertolini",
        "Biagi", "Biancardi", "Bianchi", "Bicchieri", "Biondi",
        "Biondo", "Boerio", "Bologna", "Bonaccorsi", "Bonaccorso",
        "Bondesan", "Bonomo", "Borghi", "Borgnino", "Borgogni",
        "Bosco", "Bove", "Bovér", "Boveri", "Brambani", "Brambilla",
        "Breda", "Brioschi", "Brivio", "Brunetti", "Bruno", "Buffone",
        "Bulgarelli", "Bulgari", "Buonarroti", "Busto", "Caiazzo",
        "Caito", "Caivano", "Calabrese", "Calligaris", "Campana",
        "Campo", "Cantu", "Capello", "Capitani", "Carbone", "Carboni",
        "Carideo", "Carlevaro", "Caro", "Carracci", "Carrara",
        "Caruso", "Cassano", "Castro", "Catalano", "Cattaneo",
        "Cavalcante", "Cavallo", "Cingolani", "Cino", "Cipriani",
        "Cisternino", "Coiro", "Cola", "Colombera", "Colombo",
        "Columbo", "Como", "Confortola", "Conti", "Corna", "Corti",
        "Corvi", "Costa", "Costantini", "Costanzo", "Cracchiolo",
        "Cremaschi", "Cremona", "Cremonesi", "Crespo", "Croce",
        "Crocetti", "Cucinotta", "Cuocco", "Cuoco", "D'ambrosio",
        "Damiani", "D'amore", "D'angelo", "D'antonio", "De Angelis",
        "De Campo", "De Felice", "De Filippis", "De Fiore", 
        "De Laurentis", "De Luca", "De Palma", "De Rege", "De Santis",
        "De Vitis", "Di Antonio", "Di Caprio", "Di Mercurio", "Dinapoli",
        "Dioli", "Di Pasqua", "Di Pietro", "Di Stefano", "Donati",
        "D'onofrio", "Drago", "Durante", "Elena", "Episcopo",
        "Ermacora", "Esposito", "Evangelista", "Fabbri", "Fabbro",
        "Falco", "Faraldo", "Farina", "Farro", "Fattore", "Fausti",
        "Fava", "Favero", "Fermi", "Ferrara", "Ferrari", "Ferraro",
        "Ferro", "Fierro", "Filippi", "Fini", "Fiore", "Fiscella",
        "Fonda", "Fontana", "Fortunato", "Franco", "Franzese",
        "Furlan", "Gabrielli", "Gagliardi", "Gallo" "Ganza",
        "Garfagnini", "Garofalo", "Gaspari", "Gatti", "Genovese",
        "Gentile", "Germano", "Giannino", "Gimondi", "Giordano",
        "Gismondi", "Giùgovaz", "Giunta", "Goretti", "Gori", "Greco",
        "Grillo", "Grimaldi", "Gronchi", "Guarneri", "Guerra",
        "Guerriero", "Guidi", "Guttuso", "Idoni", "Innocenti",
        "Labriola", "Làconi", "Laganà", "Lagomarsìno", "Lagorio",
        "Laguardia", "Lama", "Lamberti", "Lamon", "Landi", "Lando",
        "Landolfi", "Laterza", "Laurito", "Lazzari", "Lecce",
        "Leccese", "Leggièri", "Lèmmi", "Leone", "Leoni", "Lippi",
        "Locatelli", "Lombardi", "Longo", "Lupo", "Luzzatto",
        "Maestri", "Magro", "Mancini", "Manco", "Mancuso", "Manfredi",
        "Manfredonia", "Mantovani", "Marchegiano", "Marchesi",
        "Marchetti", "Marchioni", "Marconi", "Mari", "Maria",
        "Mariani", "Marino", "Marmo", "Martelli", "Martinelli",
        "Masi", "Masin", "Mazza", "Merlo", "Messana", "Micheli",
        "Milani", "Milano", "Modugno", "Mondadori", "Mondo",
        "Montagna", "Montana", "Montanari", "Monte", "Monti",
        "Morandi", "Morello", "Moretti", "Morra", "Moschella",
        "Mosconi", "Motta", "Muggia", "Muraro", "Murgia", "Murtas",
        "Nacar", "Naggi", "Naggia", "Naldi", "Nana", "Nani", "Nanni",
        "Nannini", "Napoleoni", "Napoletani", "Napoliello", "Nardi",
        "Nardo", "Nardovino", "Nasato", "Nascimbene", "Nascimbeni",
        "Natale", "Nave", "Nazario", "Necchi", "Negri", "Negrini",
        "Nelli", "Nenci", "Nepi", "Neri", "Neroni", "Nervetti",
        "Nervi", "Nespola", "Nicastro", "Nicchi", "Nicodemo",
        "Nicolai", "Nicolosi", "Nicosia", "Nicotera", "Nieddu",
        "Nieri", "Nigro", "Nisi", "Nizzola", "Noschese", "Notaro",
        "Notoriano", "Oberti", "Oberto", "Ongaro", "Orlando",
        "Orsini", "Pace", "Padovan", "Padovano", "Pagani", "Pagano",
        "Palladino", "Palmisano", "Palumbo", "Panzavecchia", "Parisi",
        "Parma", "Parodi", "Parri", "Parrino", "Passerini", "Pastore",
        "Paternoster", "Pavesi", "Pavone", "Pavoni", "Pecora",
        "Pedrotti", "Pellegrino", "Perugia", "Pesaresi", "Pesaro",
        "Pesce", "Petri", "Pherigo", "Piazza", "Piccirillo",
        "Piccoli", "Pierno", "Pietri", "Pini", "Piovene", "Piraino",
        "Pisani", "Pittaluga", "Poggi", "Poggio", "Poletti",
        "Pontecorvo", "Portelli", "Porto", "Portoghese", "Potenza",
        "Pozzi", "Profeta", "Prosdocimi", "Provenza", "Provenzano",
        "Pugliese", "Quaranta", "Quattrocchi", "Ragno", "Raimondi",
        "Rais", "Rana", "Raneri", "Rao", "Rapallino", "Ratti",
        "Ravenna", "Ricchetti", "Ricci", "Riggi", "Righi", "Rinaldi",
        "Riva", "Rizzo", "Robustelli", "Rocca", "Rocchi", "Rocco",
        "Roma", "Romagna", "Romagnoli", "Romano", "Romano", "Romero",
        "Roncalli", "Ronchi", "Rosa", "Rossi", "Rossini", "Rotolo",
        "Rovigatti", "Ruggeri", "Russo", "Rustici", "Ruzzier",
        "Sabbadin", "Sacco", "Sala", "Salomon", "Salucci", "Salvaggi",
        "Salvai", "Salvail", "Salvatici", "Salvay", "Sanna",
        "Sansone", "Santini", "Santoro", "Sapienti", "Sarno", "Sarti",
        "Sartini", "Sarto", "Savona", "Scarpa", "Scarsi", "Scavo",
        "Sciacca", "Sciacchitano", "Sciarra", "Scordato", "Scotti",
        "Scutese", "Sebastiani", "Sebastino", "Segreti", "Selmone",
        "Selvaggio", "Serafin", "Serafini", "Serpico", "Sessa",
        "Sgro", "Siena", "Silvestri", "Sinagra", "Sinagra", "Soldati",
        "Somma", "Sordi", "Soriano", "Sorrentino", "Spada", "Spanò",
        "Sparacello", "Speziale", "Spini", "Stabile", "Stablum",
        "Stilo", "Sultana", "Tafani", "Tamàro", "Tamboia", "Tanzi",
        "Tarantino", "Taverna", "Tedesco", "Terranova", "Terzi",
        "Tessaro", "Testa", "Tiraboschi", "Tivoli", "Todaro",
        "Toloni", "Tornincasa", "Toselli", "Tosetti", "Tosi", "Tosto",
        "Trapani", "Traversa", "Traversi", "Traversini", "Traverso",
        "Trucco", "Trudu", "Tumicelli", "Turati", "Turchi", "Uberti",
        "Uccello", "Uggeri", "Ughi", "Ungaretti", "Ungaro", "Vacca",
        "Vaccaro", "Valenti", "Valentini", "Valerio", "Varano ",
        "Ventimiglia", "Ventura", "Verona", "Veronesi", "Vescovi",
        "Vespa", "Vestri", "Vicario", "Vico", "Vigo", "Villa",
        "Vinci", "Viola", "Vitali", "Viteri", "Voltolini", "Zanetti",
        "Zangari", "Zappa", "Zeni", "Zini", "Zino", "Zunino",
        #from famous_italians
        "Alberini", "Albinoni", "Alighieri", "Andreotti", "Antonioni", "Arduino", "Argento", "Arieti",
        "Battista", "Caproni", "Donati", "Piranesi", "Venturi", "Bellucci", "Benigni", "Berio",
        "Berlinguer", "Berlusconi", "Bernardi", "Bertolucci", "Boccaccio", "Boccioni", "Bocelli",
        "Bombieri", "Botticelli", "Branca", "Brotzu", "Brunelleschi", "Bugatti", "Caboto", "Calamai",
        "Calvino", "Campagnola", "Cannizzaro", "Capasso", "Cappiello", "Cardinale", "Carissimi", "Carpaccio",
        "Castiglioni", "Catacchio", "Catalani", "Cavalli", "Cellini", "Cervi", "Cesti", "Cherubini",
        "Cimarosa", "Clemente", "Clementi", "Comencini", "Corelli", "Crispi", "Crivello", "De Filippo",
        "Deodato", "Donatelli", "Donizetti", "Duse", "Eco", "Eustachi", "Falloppio", "Fanzago", "Felice",
        "Fellini", "Fibonacci", "Filopanti", "Fiorentino", "Forlanini", "Foscolo", "Galilei", "Galvani",
        "Gardella", "Garibaldi", "Garrone", "Gentileschi", "Germi", "Giacconi", "Giannini", "Golino",
        "Gramsci", "Laurana", "Levi", "Lisi", "Livraghi", "Lollobrigida", "Loren", "Lorenzetti", "Bernini",
        "Luria", "Machiavelli", "Magnani", "Mangano", "Manzoni", "Marchiori", "Marochetti", "Mastroianni",
        "Mazzanti", "Mazzini", "Melato", "Milo", "Modigliani", "Montalbano", "Montessori", "Muti",
        "Muzio", "Negrelli", "Nobile", "Olivetti", "Pacini", "Pacinotti", "Paganini", "Palladio", "Paoli",
        "Pasolini", "Pareto", "Pasero", "Piazzi", "Pirandello", "Pisano", "Portoghesi", "Pozzo", "Prodi",
        "Puccini", "Ramazzotti", "Rosi", "Rosselli", "Rossellini", "Rubbia", "Sabatini", "Salieri",
        "Samonà", "Savonarola", "Scarlatti", "Schiaparelli", "Segrè", "Severini", "Soavi", "Spontini",
        "Strozzi", "Svevo", "Tognazzi", "Tornatore", "Torricelli", "Troisi", "Urbani", "Valadier", "Valli",
        "Veneziano", "Verdi", "Vespucci", "Visconti", "Vivaldi", "Volta", "Zamboni", "Zeffirelli", "Zipoli",
        "da Lentini", "da Vinci", "de Carolis", "de Vico", "de' Medici", "della Francesca")

# famous Italians
# pulled from Wikipedia...
# https://en.wikipedia.org/wiki/List_of_Italians
# 204 famous Italian people
# USE FOR SHIP NAMING ETC
famous_italians = ("Gino Cervi", "Roberto Benigni", "Eduardo De Filippo", "Elio Germano",
        "Giancarlo Giannini", "Nino Manfredi", "Marcello Mastroianni", "Alberto Sordi",
        "Ugo Tognazzi", "Massimo Troisi", "Clara Calamai", "Claudia Cardinale", "Eleonora Duse",
        "Virna Lisi", "Gina Lollobrigida", "Sophia Loren", "Anna Magnani", "Silvana Mangano",
        "Mariangela Melato", "Sandra Milo", "Alida Valli", "Monica Bellucci", "Ornella Muti",
        "Valeria Golino", "Filippo Brunelleschi", "Domenico Fontana", "Luciano Laurana",
        "Andrea Palladio", "Cosimo Fanzago", "Giovanni Battista Piranesi", "Giuseppe Valadier",
        "Franco Albini", "Achille Castiglioni", "Ignazio Gardella", "Luigi Moretti", "Giovanni Muzio",
        "Paolo Portoghesi", "Aldo Rossi", "Giuseppe Samonà", "Enrico Bernardi", "Giovanni Branca",
        "Giovanni Battista Caproni", "Ettore Bugatti", "Luigi Negrelli", "Enrico Forlanini",
        "Leonardo da Vinci", "Riccardo Morandi", "Camillo Olivetti", "Giovanni Caboto",
        "Sebastiano Caboto", "Cristoforo Colombo", "Umberto Nobile", "Marco Polo", "Simonetta Vespucci",
        "Amerigo Vespucci", "Salvo Montalbano", "Filoteo Alberini", "Michelangelo Antonioni", "Dario Argento",
        "Bernardo Bertolucci", "Luigi Comencini", "Ruggero Deodato", "Federico Fellini", "Matteo Garrone",
        "Pietro Germi", "Sergio Leone", "Pier Paolo Pasolini", "Gillo Pontecorvo", "Francesco Rosi",
        "Roberto Rossellini", "Michele Soavi", "Giuseppe Tornatore", "Luchino Visconti", "Lina Wertmüller",
        "Franco Zeffirelli", "Leonetto Cappiello", "Adolfo de Carolis", "Onofrio Catacchio", "Max Crivello",
        "Franco Donatelli", "Virginio Livraghi", "Enrico Mazzanti", "Alessandro de' Medici", "Catherine de' Medici",
        "Cosimo de' Medici", "Lorenzo de' Medici", "Francesco Crispi", "Giuseppe Garibaldi", "Antonio Gramsci",
        "Giuseppe Mazzini", "Carlo Rosselli", "Giulio Andreotti", "Enrico Berlinguer", "Silvio Berlusconi",
        "Romano Prodi", "Tomaso Albinoni", "Giacomo Carissimi", "Francesco Cavalli", "Antonio Cesti",
        "Pietro Locatelli", "Alessandro Scarlatti", "Domenico Scarlatti", "Barbara Strozzi", "Antonio Vivaldi",
        "Domenico Zipoli", "Domenico Cimarosa", "Antonio Salieri", "Vincenzo Bellini", "Alfredo Catalani",
        "Luigi Cherubini", "Muzio Clementi", "Gaetano Donizetti", "Niccolò Paganini", "Gioachino Rossini",
        "Gaspare Spontini", "Giuseppe Verdi", "Luciano Berio", "Umberto Giordano", "Giacomo Puccini",
        "Riccardo Muti", "Gino Paoli", "Eros Ramazzotti", "Nicolò Grimaldi", "Claudia Muzio", "Andrea Bocelli",
        "Enrico Caruso", "Franco Corelli", "Tancredi Pasero", "Pietro Lorenzetti", "Giunta Pisano", "Gentile Bellini",
        "Giovanni Bellini", "Jacopo Bellini", "Sandro Botticelli", "Vittore Carpaccio", "Rosso Fiorentino",
        "Filippino Lippi", "Piero della Francesca", "Artemisia Gentileschi", "Andrea Pozzo", "Umberto Boccioni",
        "Francesco Clemente", "Francesco Clemente", "Gino Severini", "Amedeo Modigliani", "Fortunato Felice",
        "Giulio Campagnola", "Lodovico Carracci", "Giovanni Arduino", "Silvano Arieti", "Laura Bassi",
        "Enrico Bombieri", "Giuseppe Brotzu", "Stanislao Cannizzaro", "Federico Capasso", "Francesco de Vico",
        "Giovanni Battista Donati", "Bartolomeo Eustachi", "Gabriele Falloppio", "Enrico Fermi",
        "Lodovico Ferrari", "Leonardo Fibonacci", "Quirico Filopanti", "Galileo Galilei", "Luigi Galvani", 
        "Riccardo Giacconi", "Salvador Luria", "Massimo Marchiori", "Guglielmo Marconi", "Maria Montessori", 
        "Filippo Pacini", "Antonio Pacinotti", "Vilfredo Pareto", "Giuseppe Piazzi", "Bruno Rossi", "Carlo Rubbia",
        "Giovanni Schiaparelli", "Emilio Segrè", "Evangelista Torricelli", "Carlo Urbani", "Gabriele Veneziano",
        "Giovanni Battista Venturi", "Alessandro Volta", "Giuseppe Zamboni", "Gian Lorenzo Bernini", "Umberto Boccioni",
        "Benvenuto Cellini", "Andrea Pisano", "Dante Alighieri", "Giacomo da Lentini", "Giovanni Boccaccio",
        "Giordano Bruno", "Niccolò Machiavelli", "Ugo Foscolo", "Alessandro Manzoni", "Italo Calvino",
        "Umberto Eco", "Dario Fo", "Primo Levi", "Luigi Pirandello", "Rafael Sabatini", "Italo Svevo",
        "Giovanni Agnelli", "Girolamo Savonarola")


#### FRENCH NAMES ####

# 109 French female first names.
female_firstnames_French = (
        #Students of the World
        # http://www.studentsoftheworld.info/penpals/stats.php3?Pays=FRA
        # Top 100 French names - France
        #Girls first names
        "Agathe", "Alexandra", "Alexia", "Alice", "Alicia", "Amandine", "Ambre", "Amélie", "Anaelle",
        "Anaïs", "Andréa", "Angélique", "Anna", "Audrey", "Aurélie", "Aurore", "Axelle", "Camille",
        "Carla", "Caroline", "Cassandra", "Cécile", "Célia", "Céline", "Charlène", "Charlotte", "Chloé",
        "Cindy", "Claire", "Clara", "Clémence", "Clementine", "Coline", "Coralie", "Elisa", "Elise",
        "Elodie", "Éloïse", "Elsa", "Emeline", "Emilie", "Emma", "Estelle", "Eva", "Fanny", "Gaelle",
        "Helene", "Heloise", "Inès", "Jade", "Jeanne", "Jessica", "Julia", "Julie", "Juliette", "Justine",
        "Laëtitia", "Laura", "Laure", "Laurie", "Laurine", "Léa", "Léna", "Lisa", "Lola", "Lou", "Louise",
        "Lucie", "Lucile", "Ludivine", "Maëlle", "Maéva", "Manon", "Margaux", "Margot", "Marie", "Marina",
        "Marine", "Marion", "Mathilde", "Mélanie", "Melissa", "Morgane", "Myriam", "Nina", "Noémie",
        "Océane", "Ophélie", "Pauline", "Romane", "Sabrina", "Salomé", "Sandra", "Sara", "Sarah",
        "Solène", "Sophie", "Valentine", "Victoria", "Zoé",
        #from famous_french
        "Brigitte", "Béatrice", "Catherine", "Danièle", "Emmanuelle", "Isabelle", 
        "Vanessa", "Édith", "Élisabeth")    
        
# 128 French male first names.
male_firstnames_French = (
        #Students of the World
        # http://www.studentsoftheworld.info/penpals/stats.php3?Pays=FRA
        # Top 100 French names - France
        #Boys first names
        "Adam", "Adrien", "Alan", "Alex", "Alexandre", "Alexis", "Anthony", "Antoine", "Antonin",
        "Arnaud", "Arthur", "Aurélien", "Axel", "Baptiste", "Bastien", "Benjamin", "Benoit", "Cédric",
        "Charles", "Christophe", "Christopher", "Clement", "Corentin", "Cyril", "Damien", "David",
        "Dorian", "Dylan", "Enzo", "Erwan", "Fabien", "Florent", "Florian", "Franck", "François",
        "Gabriel", "Gaëtan", "Grégory", "Guillaume", "Hugo", "Jean", "Jérémy", "Jérôme", "Jonathan",
        "Jordan", "Jules", "Julien", "Kevin", "Laurent", "Léo", "Loïc", "Louis", "Lucas", "Ludovic",
        "Mael", "Marc", "Martin", "Mathieu", "Mathis", "Matthieu", "Max", "Maxence", "Maxime",
        "Mehdi", "Mickael", "Mohamed", "Morgan", "Nathan", "Nicolas", "Olivier", "Paul", "Philippe",
        "Pierre", "Quentin", "Raphael", "Rémi", "Rémy", "Robin", "Romain", "Samuel", "Sebastien",
        "Simon", "Stephane", "Steven", "Sylvain", "Tanguy", "Theo", "Thibault", "Thibaut", "Thomas",
        "Tom", "Tony", "Tristan", "Valentin", "Victor", "Vincent", "William", "Xavier", "Yanis", "Yann",
        #from famous_french
        "Alain", "Albert", "André", "Armand", "Auguste", "Claude", "Denis", "Edgar", 
        "Eugène", "Gaston", "Georges", "Gustave", "Guy", "Gérard", "Henri", "Honoré", 
        "Jacques", "Jean-Baptiste", "Jean-Jacques", "Jean-Luc", "Jean-Paul", "Luc", "Marcel", "Michel", 
        "René", "Roland", "Serge", "Édouard")    

# 992 French surnames.
surnames_French = (
        #1000 French Surnames
        #http://surnames.behindthename.com/top/lists/france/2005
        "Abadie", "Adam", "Albert", "Alexandre", "Alix", "Allain",
        "Allard", "Allemand", "Alonso", "Alvarez", "Alves", "Andre",
        "Andrieu", "Andrieux", "Antoine", "Armand", "Arnaud", "Arnould",
        "Arnoux", "Astier", "Aubert", "Aubin", "Aubry", "Auffret", "Auge",
        "Auger", "Auvray", "Avril", "Babin", "Bachelet", "Bailleul",
        "Bailly", "Barbe", "Barbier", "Barbot", "Bardet", "Bardin",
        "Baron", "Barraud", "Barre", "Barreau", "Barret", "Barriere",
        "Barthelemy", "Basset", "Bastien", "Bataille", "Baud", "Baudet",
        "Baudin", "Baudoin", "Baudouin", "Baudry", "Bauer", "Bayle",
        "Bazin", "Beau", "Beaufils", "Beaulieu", "Beaumont", "Beauvais",
        "Beck", "Becker", "Begue", "Beguin", "Belin", "Bellanger",
        "Bellec", "Bellet", "Benard", "Benoist", "Benoit", "Berard",
        "Berger", "Bernard", "Bernier", "Berry", "Berthe", "Berthelot",
        "Berthet", "Berthier", "Bertin", "Bertrand", "Besnard", "Besse",
        "Besson", "Bianchi", "Bidault", "Billard", "Billet", "Billy",
        "Binet", "Blaise", "Blanc", "Blanchard", "Blanchet", "Blandin",
        "Blin", "Blondeau", "Blondel", "Bocquet", "Bodin", "Bois",
        "Boisseau", "Boisson", "Boivin", "Bonhomme", "Bonin", "Bonnard",
        "Bonnaud", "Bonneau", "Bonnefoy", "Bonnet", "Bonnin", "Bontemps",
        "Bordes", "Bossard", "Bouchard", "Bouche", "Boucher", "Bouchet",
        "Bouchez", "Boudet", "Bouillon", "Boulanger", "Boulay", "Boulet",
        "Bouquet", "Bour", "Bourbon", "Bourdin", "Bourdon", "Bourgeois",
        "Bourgoin", "Bourguignon", "Bousquet", "Boutet", "Boutin",
        "Bouton", "Bouvet", "Bouvier", "Boyer", "Brault", "Braun",
        "Bresson", "Bret", "Breton", "Briand", "Briere", "Brisset",
        "Brochard", "Brossard", "Brun", "Bruneau", "Brunel", "Brunet",
        "Bruno", "Bruyere", "Buisson", "Burel", "Busson", "Cadiou",
        "Caillaud", "Caillet", "Calvet", "Calvez", "Camus", "Cano",
        "Capelle", "Cardon", "Cariou", "Carlier", "Caron", "Carpentier",
        "Carre", "Carrere", "Carriere", "Cartier", "Carton", "Carvalho",
        "Casanova", "Castel", "Chabert", "Chambon", "Champion",
        "Chapelle", "Chapuis", "Charbonnier", "Chardon", "Charles",
        "Charlet", "Charlier", "Charlot", "Charpentier", "Charrier",
        "Chartier", "Charton", "Chateau", "Chatelain", "Chauveau",
        "Chauvet", "Chauvin", "Chemin", "Chene", "Cheron", "Chevalier",
        "Chevallier", "Chevrier", "Chiron", "Chollet", "Chopin",
        "Chretien", "Christophe", "Claudel", "Clement", "Clerc",
        "Cloarec", "Cochet", "Cohen", "Colas", "Colin", "Collet",
        "Collignon", "Collin", "Combe", "Combes", "Comte", "Conte",
        "Cordier", "Cormier", "Cornet", "Cornu", "Corre", "Coste",
        "Cottin", "Couderc", "Coudert", "Coulon", "Courtin", "Courtois",
        "Cousin", "Coutant", "Couturier", "Crepin", "Crouzet", "Cuvelier",
        "Da Silva", "Daniel", "Darras", "Dauphin", "De Oliveira", "De Sousa",
        "Debray", "Delage", "Delahaye", "Delamare", "Delannoy",
        "Delaporte", "Delarue", "Delattre", "Delaunay", "Delcroix",
        "Delhaye", "Delmas", "Delorme", "Demange", "Denis", "Derrien",
        "Desbois", "Descamps", "Deschamps", "Deshayes", "Despres",
        "Devaux", "Deville", "Devos", "Dias", "Diaz", "Didier", "Diot",
        "Dore", "Dos Santos", "Doucet", "Drouet", "Drouin", "Dubois",
        "Dubos", "Dubost", "Dubourg", "Dubreuil", "Dubus", "Duchemin",
        "Duchene", "Duchesne", "Duclos", "Ducrocq", "Dufour", "Duhamel",
        "Dujardin", "Dumas", "Dumont", "Dumortier", "Dumoulin", "Dupin",
        "Dupond", "Dupont", "Duprat", "Dupre", "Dupuis", "Dupuy",
        "Duquesne", "Durand", "Durant", "Duret", "Durieux", "Duriez",
        "Dutertre", "Duval", "Esnault", "Esteve", "Etienne", "Evrard",
        "Fabre", "Faivre", "Faucher", "Faure", "Favier", "Favre",
        "Favreau", "Fayolle", "Felix", "Fernandes", "Fernandez",
        "Ferrand", "Ferrari", "Ferre", "Ferreira", "Ferrer", "Ferrier",
        "Fevre", "Fevrier", "Fievet", "Fischer", "Flament", "Fleury",
        "Floch", "Fontaine", "Forestier", "Fortin", "Foucault", "Foucher",
        "Foulon", "Fouquet", "Fourcade", "Fournier", "Fraisse", "Franco",
        "Francois", "Fremont", "Frey", "Froment", "Gabriel", "Gaillard",
        "Gallais", "Galland", "Gallet", "Gallois", "Garin", "Garnier",
        "Garreau", "Gasnier", "Gaudin", "Gauthier", "Gautier", "Gay",
        "Geffroy", "Genet", "Genin", "Gentil", "Geoffroy", "Georges",
        "Gerard", "Germain", "Gervais", "Gibert", "Gicquel", "Gilbert",
        "Gilles", "Gillet", "Gillot", "Gimenez", "Girard", "Giraud",
        "Girault", "Gobert", "Godard", "Godart", "Godefroy", "Godet",
        "Godin", "Gomes", "Gomez", "Gonçalves", "Gonzales", "Gonzalez",
        "Gosselin", "Gosset", "Goujon", "Grand", "Grandjean", "Grange",
        "Granger", "Granier", "Gregoire", "Grenier", "Grimaud", "Gros",
        "Grosjean", "Gross", "Guegan", "Gueguen", "Guerin", "Guery",
        "Guibert", "Guichard", "Guignard", "Guilbaud", "Guilbert",
        "Guillard", "Guillaume", "Guillemin", "Guillemot", "Guillet",
        "Guillon", "Guillot", "Guillou", "Guiraud", "Guitton", "Guyard",
        "Guyon", "Guyot", "Hamel", "Hamelin", "Hamon", "Hardouin",
        "Hebert", "Hennequin", "Henri", "Henry", "Herault", "Hernandez",
        "Herve", "Hoarau", "Hoffmann", "Honore", "Hubert", "Huet",
        "Hugues", "Huguet", "Humbert", "Husson", "Imbert", "Jacob",
        "Jacquemin", "Jacques", "Jacquet", "Jacquin", "Jacquot", "Jamet",
        "Janin", "Janvier", "Jaouen", "Jardin", "Jarry", "Jean", "Jeanne",
        "Jegou", "Jolivet", "Joly", "Joseph", "Josse", "Jouan", "Joubert",
        "Jourdain", "Jourdan", "Jouve", "Julien", "Jullien", "Klein",
        "Labat", "Labbe", "Laborde", "Lacaze", "Lacombe", "Lacoste",
        "Lacour", "Lacroix", "Lafon", "Lafond", "Lafont", "Lagarde",
        "Lagrange", "Laine", "Lalanne", "Lallemand", "Lallement",
        "Lambert", "Lamotte", "Lamour", "Lamy", "Landais", "Lang",
        "Langlais", "Langlois", "Lapeyre", "Lapierre", "Laporte",
        "Larcher", "Laroche", "Larue", "Lassalle", "Lasserre", "Latour",
        "Launay", "Laurent", "Laval", "Lavaud", "Lavergne", "Lavigne",
        "Le Bars", "Le Berre", "Le Bihan", "Le Borgne", "Le Bras",
        "Le Breton", "Le Bris", "Le Corre", "Le Floch", "Le Gal", "Le Gall",
        "Le Goff", "Le Guen", "Le Meur", "Le Roux", "Le Roy", "Lebas",
        "Lebeau", "Leblanc", "Leblond", "Lebon", "Lebreton", "Lebrun",
        "Leclerc", "Leclercq", "Leclere", "Lecocq", "Lecoeur", "Lecomte",
        "Leconte", "Lecoq", "Lecuyer", "Ledoux", "Leduc", "Lefebvre",
        "Lefeuvre", "Lefevre", "Lefort", "Lefranc", "Lefrancois", "Legay",
        "Legendre", "Leger", "Legrand", "Legras", "Legros", "Lejeune",
        "Leleu", "Lelievre", "Lelong", "Leloup", "Lemaire", "Lemaitre",
        "Lemarchand", "Lemercier", "Lemoine", "Lemonnier", "Lenoir",
        "Lepage", "Lepine", "Lepretre", "Leray", "Leriche", "Leroux",
        "Leroy", "Lesage", "Lesueur", "Letellier", "Levasseur", "Leveque",
        "Levy", "Lienard", "Loiseau", "Loisel", "Loison", "Lombard",
        "Lopes", "Lopez", "Louis", "Louvet", "Loyer", "Lucas", "Mace",
        "Madec", "Magne", "Magnier", "Magnin", "Mahe", "Mahieu",
        "Maillard", "Maillet", "Maillot", "Maire", "Maitre", "Mallet",
        "Mangin", "Marais", "Marc", "Marchal", "Marchand", "Marechal",
        "Marie", "Marin", "Marion", "Marques", "Marquet", "Marteau",
        "Martel", "Martin", "Martineau", "Martinet", "Martinez",
        "Martins", "Marty", "Masse", "Masson", "Mathieu", "Mathis",
        "Mauger", "Maurel", "Maurice", "Maurin", "Maury", "Mayer",
        "Menard", "Mendes", "Mercier", "Merle", "Merlin", "Metais",
        "Metayer", "Meunier", "Meyer", "Michaud", "Michaux", "Michel",
        "Michon", "Mignot", "Mille", "Millet", "Millot", "Miquel",
        "Moine", "Molina", "Monier", "Monin", "Monnet", "Monnier",
        "Montagne", "Monteil", "Mora", "Morand", "Moreau", "Morel",
        "Moreno", "Moret", "Morice", "Morin", "Morvan", "Motte", "Moulin",
        "Mounier", "Mouton", "Muller", "Munier", "Munoz", "Navarro",
        "Nedelec", "Neveu", "Nguyen", "Nicolas", "Nicolle", "Noel",
        "Nogues", "Normand", "Oger", "Olivier", "Ollivier", "Page",
        "Pages", "Paillard", "Papin", "Paquet", "Paris", "Parisot",
        "Parmentier", "Pascal", "Pasquet", "Pasquier", "Pastor", "Paul",
        "Payen", "Payet", "Pelissier", "Pellerin", "Pelletier", "Peltier",
        "Pepin", "Pereira", "Peres", "Perin", "Pernot", "Peron", "Perret",
        "Perrier", "Perrin", "Perron", "Perrot", "Petit", "Petitjean",
        "Peyre", "Pham", "Philippe", "Philippon", "Philippot", "Picard",
        "Pichard", "Pichon", "Picot", "Pierron", "Pillet",
        "Pineau", "Pinel", "Pinson", "Pinto", "Piquet", "Pires",
        "Poirier", "Poirot", "Poisson", "Pollet", "Pommier", "Poncet",
        "Pons", "Portal", "Porte", "Portier", "Potier", "Pottier",
        "Pouget", "Poulain", "Poulet", "Pouliquen", "Prat", "Prevost",
        "Prevot", "Prieur", "Prigent", "Prost", "Proust", "Provost",
        "Pruvost", "Puech", "Pujol", "Quentin", "Quere", "Raffin",
        "Ragot", "Ramos", "Raoul", "Rault", "Raymond", "Raynal",
        "Raynaud", "Reboul", "Regnier", "Remond", "Remy", "Renard",
        "Renaud", "Renaudin", "Renault", "Renou", "Revel", "Rey",
        "Reynaud", "Ribeiro", "Ricard", "Richard", "Rigal", "Rigaud",
        "Riou", "Riviere", "Robert", "Robillard", "Robin", "Robinet",
        "Roche", "Rocher", "Rodier", "Rodrigues", "Rodriguez", "Roger",
        "Roland", "Rolland", "Rollet", "Rollin", "Romain", "Romero",
        "Rondeau", "Roques", "Rossi", "Rossignol", "Roth", "Rougier",
        "Rousseau", "Roussel", "Rousselle", "Rousset", "Roux", "Rouxel",
        "Rouyer", "Roy", "Royer", "Ruiz", "Sabatier", "Salaun", "Salle",
        "Salles", "Salmon", "Salomon", "Samson", "Sanchez", "Santos",
        "Sarrazin", "Saulnier", "Saunier", "Sauvage", "Savary",
        "Schaeffer", "Schmitt", "Schneider", "Seguin", "Sellier",
        "Senechal", "Sergent", "Serra", "Serrano", "Serre", "Serres",
        "Sicard", "Simon", "Simonin", "Simonnet", "Soler", "Soulie",
        "Soulier", "Stephan", "Tanguy", "Tardy", "Tavernier", "Teixeira",
        "Tellier", "Terrier", "Tessier", "Texier", "Teyssier", "Thebault",
        "Thery", "Thevenet", "Thevenin", "Thibault", "Thiebaut",
        "Thierry", "Thiery", "Thomas", "Thuillier", "Tison", "Tisserand",
        "Tissier", "Tissot", "Tixier", "Tournier", "Toussaint", "Tran",
        "Turpin", "Vacher", "Vaillant", "Valentin", "Valette", "Vallee",
        "Vallet", "Vannier", "Varin", "Vasseur", "Verdier", "Verger",
        "Vernet", "Vernier", "Veron", "Verrier", "Vial", "Viard", "Viaud",
        "Vidal", "Vigier", "Vignal", "Vigneron", "Vignon", "Vigouroux",
        "Viguier", "Vilain", "Villain", "Villard", "Villeneuve",
        "Villette", "Vincent", "Vivier", "Voisin", "Weber", "Wolff",
        "Zimmermann",
        #from famous_french
        "Adjani", "Althusser", "Balzac", "Bardot", "Barthes", "Beaumarchais", "Beauvoir", 
        "Belmondo", "Binoche", "Blériot", "Braque", "Béart", "Canet", "Carré", "Chirac", 
        "Cocteau", "Cotillard", "Cousteau", "Dalle", "Debord", "Delacroix", "Delon", 
        "Delpy", "Deneuve", "Derrida", "Duchamp", "Fragonard", "Garros", "Gaulle", 
        "Huppert", "Mallarmé", "Montaigne", "Montand", "Paradis", "Perec", "Perrault", 
        "Piaf", "Piaget", "Pigalle", "Réage", "Seurat", "Tati", "Tautou", "Truffaut", 
        "Verlaine", "Verne", "Zola", "de Balzac", "de Beauvoir", "de Maupassant", 
        "de Montaigne")    

# famous French
# pulled from Wikipedia...
# https://en.wikipedia.org/wiki/List_of_French_people
# 116 famous French people
# USE FOR SHIP NAMING ETC
famous_french = ("Isabelle Adjani", "Charles Aznavour", "Brigitte Bardot", "Emmanuelle Béart",
        "Jean-Paul Belmondo", "Juliette Binoche", "Guillaume Canet", "Isabelle Carré", "Marion Cotillard",
        "Béatrice Dalle", "Alain Delon", "Danièle Delorme", "Julie Delpy", "Catherine Deneuve",
        "Élisabeth Depardieu", "Gérard Depardieu", "Michel Drucker", "Jean Dujardin", "Isabelle Huppert",
        "Yves Montand", "Audrey Tautou", "Gustave Eiffel", "Henri Cartier-Bresson",
        "François Boucher", "Georges Braque", "Paul Cézanne", "Edgar Degas", "Eugène Delacroix",
        "Marcel Duchamp", "Jean-Honoré Fragonard", "Édouard Manet", "Henri Matisse", "Claude Monet",
        "Camille Pissarro", "Nicolas Poussin", "Pierre-Auguste Renoir", "Henri Rousseau",
        "Georges Seurat", "Henri de Toulouse-Lautrec", "Jean-Baptiste Pigalle", "Auguste Rodin",
        "Guillaume Apollinaire", "Honoré de Balzac", "Charles Baudelaire",
        "Pierre Beaumarchais", "Simone de Beauvoir", "Cyrano de Bergerac",
        "Albert Camus", "Jean Cocteau", "Denis Diderot", "Alexandre Dumas", "Gustave Flaubert",
        "Anatole France", "Jean Genet", "Victor Hugo", "Jean de La Fontaine", "Gaston Leroux",
        "Stéphane Mallarmé", "Guy de Maupassant", "Anaïs Nin", "Charles Perrault", "Georges Perec",
        "Jean Piaget", "Marcel Proust", "François Rabelais", "Jean Racine", "Pauline Réage", "Arthur Rimbaud",
        "Jean-Paul Sartre", "Antoine de Saint-Exupery", "François Truffaut", "Paul Verlaine", "Jules Verne",
        "Émile Zola", "Louis Blériot", "René Fonck", "Roland Garros", "Ettore Bugatti",
        "André Citroën", "Marcel Dassault", "Armand Peugeot", "Marcel Renault",
        "Luc Besson", "Jean Cocteau", "Jacques Cousteau", "Jean-Luc Godard",
        "Georges Méliès", "Jean Renoir", "Jacques Tati", "François Truffaut",
        "Claude Debussy", "Sacha Distel", "Charlotte Gainsbourg", "Serge Gainsbourg",
        "Vanessa Paradis", "Édith Piaf", "Louis Althusser", "Roland Barthes", "Jean Baudrillard",
        "Guy Debord", "Jacques Derrida", "René Descartes", "Denis Diderot", "Michel Foucault",
        "Michel de Montaigne", "Blaise Pascal", "Jean-Jacques Rousseau", "Jean-Paul Sartre",
        "Jacques Chirac", "Georges Clemenceau", "Charles de Gaulle", "Simone de Beauvoir",
        "Louis Braille,", "Gustave Eiffel", "René Lalique", "Maximilien Robespierre")    



#### GERMAN NAMES ####

# 101 German female first names.
female_firstnames_German = (
        #Students of the World
        # http://www.studentsoftheworld.info/penpals/stats.php3?Pays=GER
        # Top 100 German names - Germany
        #Girls first names
        "Alexandra", "Alice", "Alina", "Amelie", "Andrea", "Anja",
        "Anna", "Anne", "Anni", "Annika", "Antonia", "Carina",
        "Carolin", "Céline", "Charlotte", "Christina", "Clara",
        "Denise", "Elena", "Elisa", "Elisabeth", "Ella", "Elli",
        "Emily", "Emma", "Eva", "Fabienne", "Fiona", "Franzi",
        "Franziska", "Hanna", "Hannah", "Ina", "Isabel", "Jacqueline",
        "Jana", "Janina", "Janine", "Jasmin", "Jennifer", "Jenny",
        "Jessica", "Johanna", "Jule", "Julia", "Julie", "Katharina",
        "Kathi", "Kathrin", "Katja", "Kim", "Kira", "Lara", "Larissa",
        "Laura", "Lea", "Lena", "Leonie", "Lina", "Linda", "Lisa",
        "Louisa", "Luisa", "Mara", "Maria", "Marie", "Marina",
        "Melanie", "Melina", "Melissa", "Merle", "Mia", "Michelle",
        "Mona", "Nadine", "Nadja", "Natalie", "Natascha", "Nele",
        "Nicole", "Nina", "Paula", "Pauline", "Pia", "Rebecca",
        "Sabrina", "Sandra", "Sara", "Sarah", "Sina", "Sophia",
        "Sophie", "Stefanie", "Steffi", "Stella", "Svenja", "Tamara",
        "Theresa", "Vanessa", "Verena",
        #from famous_germans
        "Claudia", "Diane", "Heidi", "Hildegard", "Marlene", "Melitta",
        "Nastassja", "Ulrike", "Ursula")    

# 101 German male first names.
male_firstnames_German = (
        #Students of the World
        # http://www.studentsoftheworld.info/penpals/stats.php3?Pays=GER
        # Top 100 German names - Germany
        #Boys first names
        "Adrian", "Alex", "Alexander", "Ali", "Alihan", "Andre",
        "Andreas", "Anton", "Arthur", "Artur", "Bako", "Ben", "Brian",
        "Chris", "Christian", "Christoph", "Christopher", "Daniel",
        "David", "Dennis", "Dominik", "Dustin", "Erik", "Fabian",
        "Fabio", "Felix", "Florian", "Frank", "Gabriel", "Gerrit",
        "Hendrik", "Jakob", "Jan", "Janis", "Jannik", "Jason", "Jens",
        "Jeremy", "Jesse", "Johannes", "Jonas", "Jonathan", "Julian",
        "Kai", "Kevin", "Konrad", "Konstantin", "Lasse", "Leo",
        "Leon", "Luca", "Lucas", "Ludwig", "Luis", "Lukas", "Marc",
        "Marcel", "Marco", "Mario", "Mark", "Markus", "Martin",
        "Marvin", "Matthias", "Max", "Maximilian", "Michael",
        "Mohamed", "Moritz", "Muhammed", "Nick", "Nico", "Niels",
        "Niklas", "Nils", "Noah", "Oliver", "Patrick", "Paul",
        "Peter", "Phil", "Philipp", "Pierre", "René", "Ricardo",
        "Sebastian", "Simon", "Stefan", "Sven", "Tamino", "Thomas",
        "Till", "Tim", "Timo", "Tobias", "Tom", "Victor", "Vincent",
        "William", 
        #from famous_germans
        "Albrecht", "Bertolt", "Carl", "Dieter", "Egon", "Erich", "Ernst", "Ferdinand",
        "Friedrich", "Fritz", "Georg", "George", "Gerhard", "Gottfried", "Gottlieb",
        "Günter", "Hans", "Heinrich", "Helmut", "Hermann", "Karl", "Klaus", "Kurt",
        "Manfred", "Otto", "Rainer", "Werner", "Wilhelm", "Wim", "Wolfgang")    

# 379 German surnames.
surnames_German = (
        #100 German Surnames
        #http://german.about.com/od/names/a/German-Surnames.htm
        "Albrecht", "Arnold", "Bach", "Bäcker", "Bauer", "Baumann",
        "Beck", "Becker", "Berger", "Bergmann", "Böhm", "Brandt", "Braun",
        "Busch", "Dietrich", "Engel", "Fischer", "Frank", "Franke",
        "Friedrich", "Fuchs", "Graf", "Groß", "Günther", "Haas", "Hahn",
        "Hartmann", "Heinrich", "Herrmann", "Hoffmann", "Hofmann", "Horn",
        "Huber", "Jäger", "Jung", "Kaiser", "Keller", "Klein", "Koch",
        "Köhler", "König", "Krämer", "Kraus", "Krause", "Krüger", "Kuhn",
        "Kühn", "Lang", "Lange", "Lehmann", "Lorenz", "Ludwig", "Maier",
        "Martin", "Mayer", "Meier", "Meyer", "Möller", "Müller",
        "Neumann", "Otto", "Peters", "Pfeiffer", "Pohl", "Richter",
        "Roth", "Sauer", "Schäfer", "Schmid", "Schmidt", "Schmitt",
        "Schmitz", "Schneider", "Scholz", "Schreiber", "Schröder",
        "Schubert", "Schulte", "Schulz", "Schulze", "Schumacher",
        "Schuster", "Schwarz", "Seidel", "Simon", "Sommer", "Stein",
        "Thomas", "Vogel", "Vogt", "Voigt", "Wagner", "Walter", "Weber",
        "Weiß", "Werner", "Winkler", "Winter", "Wolf", "Wolff", "Ziegler",
        "Zimmermann",
        #http://german.about.com/od/culture/fl/German-Last-Names-and-Their-English-Meanings.htm
        "Aachen", "Achen", "Abend", "Abendroth", "Ackerman", "Adler",
        "Amsel", "Austerlitz", "Bach", "Bachmeier", "Bader", "Baader",
        "Baecker", "Becker", "Baer", "Bar", "Barth", "Bauer", "Baum",
        "Baumgaertner", "Baumgartner", "Bumgarner", "Bayer", "Baier",
        "Beyer", "Beckenbauer", "Beich", "Beike", "Berg", "Bergmann",
        "Bieber", "Biermann", "Blau", "Boehm", "Bohm", "Brandt", "Brauer",
        "Braun", "Bürger", "Burger", "Busch", "Bosch", "Daecher",
        "Decker", "Diederich", "Dietrich", "Drechsler", "Dreher",
        "Dresdner", "Dresner", "Drescher", "Duerr", "Durr", "Ebersbach",
        "Ebersbacher", "Eberhardt", "Eberhart", "Eichel", "Eichelberger",
        "Eichmann", "Ehrlichmann", "Eisenberg", "Eisenhauer",
        "Eisenhower", "Egger", "Eggers", "Engel", "Faber", "Faerber",
        "Farber", "Fassbinder", "Faust", "Feierabend", "Fenstermacher",
        "Fiedler", "Fink", "Finkel", "Fischer", "Fisher", "Fleischer",
        "Foerster", "Frankfurter", "Frei", "Frey", "Freitag", "Freytag",
        "Freud", "Fried", "Friedmann", "Friedman", "Frueh", "Freeh",
        "Fruehauf", "Fuchs", "Fuerst", "Furst", "Fuhrmann", "Gaertner",
        "Gärtner", "Gerber", "Gerste", "Gersten", "Gloeckner", "Glockner",
        "Goldschmidt", "Gottlieb", "Gottschalk", "Gruenewald",
        "Grunewald", "Grunwald", "Hahn", "Herrmann", "Herman", "Hertz",
        "Herz", "Hertzog", "Herzog", "Himmel", "Himmelreich", "Hirsch",
        "Hoch", "Hoffmann", "Hofmann", "Holtzmann", "Holzman", "Hueber",
        "Huber", "Hoover", "Jaeger", "Jager", "Jung", "Junker", "Kaiser",
        "Kalb", "Kaestner", "Kastner", "Kappel", "Kaufmann", "Keller",
        "Kirsch", "Klein", "Klug", "Kluge", "Koch", "Kohl", "Cole",
        "Kohler", "Koehler", "Koenig", "Konig", "Krause", "Krueger",
        "Kruger", "Kuefer", "Kuester", "Kuster", "Kuhn", "Kunze",
        "Koertig", "Kortig", "Lang", "Lehmann", "Lemann", "Lehrer",
        "Loewe", "Lowe", "Luft", "Mahler", "Mehler", "Maier", "Meier",
        "Meyer", "Mauer", "Maur", "Maurer", "Meister", "Metzger", "Meier",
        "Meyer", "Maier", "Mueller", "Muller", "Moench", "Muench",
        "Nacht", "Nadel", "Nagel", "Naumann", "Neumann", "Neudorf",
        "Neustadt", "Nussbaum", "Oster", "Osterhagen", "Ostermann",
        "Pabst", "Papst", "Pfaff", "Pfeffer", "Pfeifer", "Pfeiffer",
        "Probst", "Propst", "Reinhard", "Reinhardt", "Reiniger",
        "Richter", "Ritter", "Roth", "Rothschild", "Rothstein",
        "Saenger", "Sanger", "Sankt", "Schäfer", "Schaefer", "Scherer",
        "Schiffer", "Schmidt", "Schmitt", "Schneider", "Scholz",
        "Schulze", "Schreiber", "Schreiner", "Schroeder", "Schroder",
        "Schuhmacher", "Schultheiss", "Schultz", "Schulz", "Schulze",
        "Scholz", "Schuster", "Shuster", "Schwab", "Schwartz", "Schwarz",
        "Schweitzer", "Schweizer", "Seiler", "Somme", "Strauss",
        "Thalberg", "Theiss", "Theissen", "Traugott", "Trommler", "Unger",
        "Urner", "Vogel", "Vogler", "Vogt", "Waechter", "Wagner",
        "Wannemaker", "Weber", "Wechsler", "Wexler", "Weiss", "Weisz",
        "Weissmuller", "Werfel", "Wurfel", "Winkel", "Wirth", "Wirtz",
        "Wolf", "Wulf", "Wurfel", "Werfel", "Ziegler", "Zimmer",
        "Zimmermann", "Zimmerman", "Zweig",
        #from famous_germans
        "Adenauer", "Arendt", "Brecht", "Cantor", "Clausewitz", "Dürer", "Ehrlich", 
        "Emmerich", "Engels", "Ernst", "Gauss", "Furtwängler", "Geiger", "Goethe", 
        "Gropius", "Grosz", "Heidegger", "Hesse", "Honecker", "Humboldt", "Janssen", 
        "Kant", "Kinski", "Klee", "Klum", "Krenz", "Leibniz", "Rohe", "Schiller", 
        "Scholl", "Schwitters", "Schäuble", "Weill", "Wenders", 
        "Fassbinder", "Leibniz", "Wix", "Zuse", "Richthofen")    



# famous Germans
# https://en.wikipedia.org/wiki/List_of_Germans
# 80 famous German people
# USE FOR SHIP NAMING ETC
famous_germans = ("Albrecht Dürer", "Alexander von Humboldt", "Arthur Schopenhauer", "Bertolt Brecht",
        "Carl Friedrich Gauss", "Carl Orff", "Carl von Clausewitz",
        "Clara Schumann", "Claudia Schiffer", "David Hilbert", "Diane Kruger",
        "Dieter Roth", "Erich Maria Remarque", "Ernst Heinkel", "Felix Mendelssohn",
        "Ferdinand Porsche", "Ferdinand von Zeppelin", "Friedrich Engels", "Friedrich Nietzsche",
        "Friedrich Schiller", "Fritz Lang", "Georg Cantor", "Georg Friedrich Händel",
        "Georg Ohm", "George Grosz", "Gottfried Leibniz", "Gottfried Wilhelm Leibniz",
        "Gottlieb Daimler", "Günter Grass", "Hannah Arendt", "Hannah Höch", "Hans Geiger",
        "Hans Holbein", "Heidi Klum", "Heinrich Rudolf Hertz", "Hermann Hesse",
        "Horst Janssen", "Immanuel Kant", "Johann Pachelbel", "Johann Sebastian Bach",
        "Johann Wolfgang von Goethe", "Johannes Brahms", "Johannes Kepler", "Karl Benz",
        "Karl Marx", "Karlheinz Stockhausen", "Klaus Kinski", "Konrad Adenauer", "Konrad Zuse",
        "Kurt Schwitters", "Kurt Weill", "Ludwig Mies van der Rohe", "Ludwig van Beethoven",
        "Manfred von Richthofen", "Marlene Dietrich", "Martin Heidegger", "Max Ernst",
        "Max Planck", "Nastassja Kinski", "Otto Lilienthal", "Otto von Bismarck", "Otto Wix",
        "Paul Ehrlich", "Paul Klee", "Philipp Furtwängler", "Rainer Maria Rilke",
        "Rainer Werner Fassbinder", "Richard Strauss", "Richard Wagner", "Robert Schumann",
        "Roland Emmerich", "Romy Schneider", "Sophie Scholl", "Thomas Mann", "Walter Gropius",
        "Werner Herzog", "Werner Karl Heisenberg", "Wernher von Braun", "Wilhelm Röntgen",
        "Wim Wenders")

#### RUSSIAN NAMES ####

##http://surnames.behindthename.com/glossary/view/russian_names
##
#The complete Russian name is formed of a given name, patronymic, and a
#family name, in that order. The given names can each have several
#different diminutives. For example for Anastasiya there is Nastya,
#Stasya, Tasya, Nastenka, and more.
#
#Russian given names are often taken from the names of saints,
#especially those from Eastern Orthodox tradition, which are often of
#Greek origin. In the last century traditional Slavic names have again
#come into use. See European names.
#
#Russian names are normally written in the Cyrillic alphabet, the usual
#alphabet of the Russian language. When they are represented in the
#Latin alphabet (of English and other western European languages) they
#are transcribed, which can result in multiple spellings for a single
#name depending on the transcription. For example Дмитрийcan be
#rendered Dmitriy, Dmitri, or Dmitrii.


female_firstnames_Russian = (
        #Students of the World
        # http://www.studentsoftheworld.info/penpals/stats.php3?Pays=RUS
        # Top 100 Russian names - Russia
        #Girls first names
        "Albina", "Alena", "Alexandra", "Alice", "Alina", "Alisa",
        "Alyona", "Anastasia", "Anastasiya", "Angelina", "Ann",
        "Anna", "Anya", "Arina", "Asya", "Catherine", "Christina",
        "Daria", "Darya", "Dasha", "Diana", "Dina", "Ekaterina",
        "Elena", "Elizabeth", "Eva", "Evgeniya", "Galina", "Helen",
        "Helena", "Inna", "Ira", "Irene", "Irina", "Jane", "Julia",
        "Juliya", "Karina", "Kate", "Katerina", "Katherine", "Katya",
        "Kira", "Kristina", "Ksenia", "Kseniya", "Ksenya", "Ksusha",
        "Lena", "Lera", "Lina", "Lisa", "Liza", "Lyuba", "Madina",
        "Margarita", "Maria", "Marina", "Mariya", "Marta", "Mary",
        "Masha", "Nastia", "Nastya", "Natalia", "Natalie", "Nataly",
        "Natalya", "Natasha", "Nina", "Oksana", "Olesya", "Olga",
        "Olya", "Polina", "Polly", "Sasha", "Sofia", "Sonya",
        "Sophia", "Sveta", "Svetlana", "Tanya", "Tatiana", "Tatyana",
        "Ulyana", "Valentina", "Valeria", "Vasilisa", "Vera",
        "Veronica", "Veronika", "Victoria", "Vika", "Viktoria",
        "Viktoriya", "Vlada", "Yana", "Yulia", "Zhenya",
        #Note from (see above)
        #http://surnames.behindthename.com/glossary/view/russian_names
        "Anastasiya", "Nastenka", "Nastya", "Stasya", "Tasya"#, 
        #from famous_russians
        #""
        #FILL IN LATER??
        )    

male_firstnames_Russian = (
        #Students of the World
        # http://www.studentsoftheworld.info/penpals/stats.php3?Pays=RUS
        # Top 100 Russian names - Russia
        #Boys first names
        "Adam", "Aleksandr", "Aleksei", "Aleksey", "Alex",
        "Alexander", "Alexandr", "Alexey", "Anatoly", "Andrei",
        "Andrew", "Andrey", "Andru", "Anton", "Artem", "Arthur",
        "Artiom", "Artur", "Bogdan", "Boris", "Dan", "Daniel",
        "Daniil", "Danil", "Danila", "David", "Denis", "Dima",
        "Dmitriy", "Dmitry", "Egor", "Eugene", "Evgeny", "Fedor",
        "George", "Gleb", "Gosha", "Gregory", "Grisha", "Igor",
        "Ilya", "Ivan", "Kirill", "Kolya", "Konstantin", "Kostya",
        "Leo", "Leonid", "Maksim", "Mansur", "Mark", "Matvey", "Max",
        "Maxim", "Michael", "Mikhail", "Misha", "Nick", "Nikita",
        "Niko", "Nikolai", "Nikolay", "Oleg", "Pasha", "Paul",
        "Pavel", "Petr", "Rafit", "Renat", "Roma", "Roman", "Ruslan",
        "Sasha", "Serge", "Sergei", "Sergey", "Slava", "Stanislav",
        "Timur", "Vadim", "Valentin", "Vasiliy", "Vitaliy", "Vlad",
        "Vladimir", "Vladislav", "Vova", "Yaroslav", "Yegor", "Yura",
        "Zahar", "Zhenya"#,
        #from famous_russians
        #""
        #FILL IN LATER???
        )    

surnames_Russian = (
        #36 Russian Surnames
        #http://surnames.behindthename.com/names/usage/russian
        "Aleksandrov", "Alekseev", "Bogdanov", "Bogomolov",
        "Filippov", "Fyodorov", "Ivanov", "Konstantinov", "Kozlov",
        "Krupin", "Kuznetsov", "Lagounov", "Lagunov", "Maksimov",
        "Markov", "Matveev", "Mihaylov", "Mikhailov", "Naoumov", "Naumov",
        "Nikolaev", "Orlov", "Pajari", "Pasternak", "Pavlov", "Petrov",
        "Polzin", "Popov", "Romanov", "Sokoloff", "Sokolov", "Utkin",
        "Vasilyev", "Volkov", "Yakovlev", "Zima"#,
        #from famous_russians
        #""
        #FILL IN LATER???
        )    

# famous Russians
# https://en.wikipedia.org/wiki/List_of_Russian_people
# XXX famous Russian people
# USE FOR SHIP NAMING ETC
#female and male surnames in Russian seem to work differently, so split into male and female lists...
famous_russians_male = ("Aleksandr Pushkin", "Aleksandr Solzhenitsyn", "Aleksandr Zaitsev", "Aleksei Leonov",
        "Aleksey Nikolayevich Tolstoy", "Alexander Belyayev", "Alexander Bogdanov", "Alexander Borodin",
        "Alexander Borodin", "Alexander Kazakov", "Alexander Nevsky", "Alexander Ostrovsky", "Alexander Prokhorov",
        "Alexander Rodchenko", "Alexei Tupolev", "Anatoly Karpov", "Andrei Sakharov", "Andrei Tarkovsky",
        "Andrei Tupolev", "Andrey Markov", "Anton Chekhov", "Artem Mikoyan", "Boris Pasternak", "Boris Podolsky",
        "Boris Slutsky", "Dmitri Ivanenko", "Dmitri Mendeleyev", "Dmitri Shostakovich", "Dmitry Ivanovsky",
        "Fedor Alekseev", "Fedor Tokarev", "Fyodor Dostoyevsky", "Fyodor Sologub", "Garry Kasparov",
        "Georgy Babakin", "Georgy Zhukov", "Gherman Titov", "Igor Kurchatov", "Igor Sikorsky", "Igor Stravinsky",
        "Ilya Mechnikov", "Ivan Bunin", "Ivan Chersky", "Ivan Pavlov", "Ivan Turgenev", "Kir Bulychev",
        "Konstantin Novoselov", "Konstantin Stanislavski", "Konstantin Tsiolkovsky", "Kurbat Ivanov",
        "Leo Tolstoy", "Leon Trotsky", "Lev Artsimovich", "Lyudmila Pavlichenko", "Maxim Gorky",
        "Mikhail Bakunin", "Mikhail Bulgakov", "Mikhail Glinka", "Mikhail Gurevich", "Mikhail Lermontov",
        "Mikhail Lomonosov", "Mikhail Sholokhov", "Mikhail Somov", "Modest Mussorgsky", "Nikolai Chernykh",
        "Nikolai Gogol", "Nikolai Kardashev", "Nikolai Lobachevsky", "Nikolai Nekrasov", "Nikolai Polikarpov",
        "Nikolai Zhukovsky", "Nikolai Zhukovsky", "Nikolay Basov", "Nikolay Basov", "Nikolay Zabolotsky",
        "Oleg Antonov", "Oleg Gazenko", "Pavel Cherenkov", "Pavel Sukhoi", "Peter Carl Fabergé",
        "Peter Kropotkin", "Pyotr Kapitsa", "Pyotr Nesterov", "Pyotr Tchaikovsky", "Rudolf Nureyev",
        "Sergei Bondarchuk", "Sergei Diaghilev", "Sergei Eisenstein", "Sergei Korolev", "Sergei Korolyov",
        "Sergei Prokofiev", "Sergei Rachmaninoff", "Sergei Yesenin", "Sergey Ilyushin", "Sergey Korsakov",
        "Sergey Lebedev", "Sergey Lukyanenko", "Stepan Makarov", "Valery Chkalov", "Vasily Chuikov",
        "Viktor Pugachyov", "Viktor Safronov", "Vladimir Ilyushin", "Vladimir Kokkinaki", "Vladimir Komarov",
        "Vladimir Lenin", "Vladimir Nabokov", "Vladimir Solovyov", "Yevgeny Kaspersky", "Yuri Gagarin")

famous_russians_female = ("Alexandra Kosteniuk", "Anna Akhmatova", "Anna Kournikova", "Bella Akhmadulina",
        "Elena Oznobkina", "Gavrila Derzhavin", "Irina Dvorovenko", "Lydia Litvyak", "Lyudmila Chernykh",
        "Maria Pronchishcheva", "Maria Sharapova", "Marina Tsvetaeva", "Milla Jovovich", "Natalia Makarova",
        "Natalia Shaposhnikova", "Oxana Fedorova", "Sofia Kovalevskaya", "Sofia Kovalevskaya",
        "Svetlana Savitskaya", "Tamara Karsavina", "Tatiana Riabouchinska", "Tatyana Tolstaya",
        "Tatyana Ustinova", "Valentina Grizodubova", "Valentina Tereshkova", "Yekaterina Budanova",
        "Yekaterina Zelenko", "Yelena Davydova", "Yevgeniya Rudneva", "Zinaida Serebriakova")

famous_russians = famous_russians_male + famous_russians_female

other_russians = ("Alexander Brullov", "Alexander Kokorinov", "Alexey Dushkin", "Alexey Fedchenko",
        "Anatoly Polyansky", "Andrey Popov", "Boris Orlovsky", "Evgeny Velikhov", "Fedot Popov",
        "Fyodor Pirotsky", "Fyodor Tolstoy", "Ilya Kabakov", "Matvei Kazakov", "Matvei Kazakov",
        "Mikhail Bulgakov", "Mikhail Gerasimov", "Mikhail Lazarev", "Nikolai Ladovsky", "Nikolai Tomsky",
        "Pyotr Kozlov", "Stanislav Smirnov", "Stepan Makarov", "Taras Shevchenko", "Vassili Poyarkov")




#### CHINESE NAMES ####

female_firstnames_Chinese = (
        #Students of the World
        # http://www.studentsoftheworld.info/penpals/stats.php3?Pays=CHN
        # Top 100 Chinese names - China
        #Girls first names
        "Alice", "Amanda", "Amber", "Amy", "Angel", "Angela", "Ann",
        "Anna", "Annie", "April", "Bella", "Betty", "Candy", "Carol",
        "Caroline", "Catherine", "Cathy", "Charlotte", "Chen",
        "Cherry", "Christina", "Cindy", "Claire", "Coco", "Crystal",
        "Daisy", "Diana", "Doris", "Echo", "Elaine", "Emily", "Emma",
        "Eva", "Fiona", "Grace", "Han", "Helen", "Huang", "Iris",
        "Ivy", "Jane", "Jasmine", "Jenny", "Jessica", "Jing", "Joy",
        "Joyce", "Katherine", "Kelly", "Lee", "Li", "Lily", "Lin",
        "Linda", "Ling", "Lisa", "Liu", "Lu", "Lucy", "Mary", "May",
        "Nancy", "Nicole", "Olivia", "Rachel", "Rebecca", "Sharon",
        "Sherry", "Shirley", "Sophia", "Sophie", "Sue", "Summer",
        "Sun", "Sunny", "Tang", "Tiffany", "Tina", "Vicky",
        "Victoria", "Vivian", "Wang", "Wendy", "Wu", "Xu", "Yan",
        "Yang", "Yi", "Ying", "Yu", "Yuan", "Zhang", "Zhao", "Zhou",
        "Zhu", "Zoe"#,
        #from famous_chineses
        #"" # MAYBE FILL IN LATER?
        )    

male_firstnames_Chinese = (
        #Students of the World
        # http://www.studentsoftheworld.info/penpals/stats.php3?Pays=CHN
        # Top 100 Chinese names - China
        #Boys first names
        "Alan", "Alex", "Allen", "Andy", "Ben", "Bob", "Bruce",
        "Chan", "Chao", "Charles", "Chen", "Cheng", "Chris", "Daniel",
        "David", "Deng", "Ding", "Dong", "Edison", "Edward", "Eric",
        "Feng", "Frank", "Gao", "George", "Guo", "Han", "Hao",
        "Harry", "He", "Hu", "Huang", "Jack", "James", "Jason",
        "Jerry", "Jiang", "Jim", "Jin", "Joe", "John", "Justin",
        "Kai", "Ken", "Kevin", "King", "Lee", "Lei", "Leo", "Li",
        "Liang", "Lin", "Liu", "Lu", "Luo", "Ma", "Mark", "Michael",
        "Mike", "Ni", "Nick", "Peng", "Peter", "Sam", "Sean", "Simon",
        "Song", "Steven", "Sun", "Tang", "Tian", "Tom", "Tony",
        "Vincent", "Wang", "Wei", "Will", "William", "Wu", "Xiang",
        "Xiao", "Xie", "Xu", "Yan", "Yang", "Yao", "Ye", "Yu", "Yuan",
        "Zeng", "Zhang", "Zhao", "Zheng", "Zhou", "Zhu"#,
        #from famous_chinese
        #"" # MAYBE FILL IN LATER?
        )    

surnames_Chinese = (
        #from https://en.wikipedia.org/wiki/List_of_most_common_surnames_in_Asia
        "Chan", "Chén", "Cheung", "Chow", "Gāo", "Guō", "Hé", "Ho", "Hú", "Huáng", "Kwok",
        "Lam", "Lau", "Lee", "Lǐ", "Lín", "Liú", "Luó" "Mǎ", "Ng", "Sūn", "Wáng", "Wong",
        "Wong", "Wú", "Xú", "Yáng", "Zhāng", "Zhào", "Zhōu", "Zhū"#,
        #from famous_chinese
        #"" # MAYBE FILL IN LATER?
        )    

# famous Chinese
# XXX famous Chinese people
# USE FOR SHIP NAMING ETC
famous_chinese = ("""Bruce Lee

Cao Xueqin
Cao Cao
Chiang Kai-shek

Lao Tzu
Liu Xiaobo
Mo Yan
Sun Tzu
Tsung-Dao Lee
Yip Man
""",
        "")

# other Chinese
other_chinese = ("Cao Jianguo",
        "Huang Xiangmo",
        "Li Fangyong",
        "Li Yuan",
        "Lin Baifeng",
        "Liu Xiaoming",
        "Tang Xianzu",
        "Tian Yiyan",
        "Xi Jinping",
        "Zhang Qingwei",
        "Zheng Mingguang",
        "Zhu Minshen")




#### JAPANESE NAMES ####

female_firstnames_Japanese = (
        #Students of the World
        # http://www.studentsoftheworld.info/penpals/stats.php3?Pays=JAP
        # Top 100 Japanese names - Japan
        #Girls first names
        "Ai", "Aika", "Airi", "Akane", "Akari", "Aki", "Anna",
        "Arisa", "Asami", "Asuka", "Asumi", "Aya", "Ayaka", "Ayana",
        "Ayano", "Ayumi", "Chie", "Chiharu", "Chihiro", "Chisato",
        "Emi", "Eri", "Erika", "Eriko", "Hana", "Haru", "Haruka",
        "Haruna", "Hina", "Hiromi", "Kaho", "Kana", "Kanako", "Kaori",
        "Kay", "Kei", "Keiko", "Mai", "Maki", "Mami", "Manami", "Mao",
        "Mari", "Marina", "Mayu", "Mayumi", "Megumi", "Mei", "Miho",
        "Mika", "Miki", "Mina", "Minami", "Minori", "Mio", "Misa",
        "Misaki", "Miyu", "Mizuki", "Moe", "Moeka", "Momoko",
        "Nagisa", "Nana", "Nanako", "Nanami", "Nao", "Narumi",
        "Natsuki", "Natsumi", "Nozomi", "Rei", "Rika", "Rin", "Rina",
        "Risa", "Rui", "Sae", "Saki", "Sakura", "Satomi", "Saya",
        "Sayaka", "Shiho", "Shiori", "Tomo", "Tomoko", "Tomomi",
        "Yoko", "Yui", "Yuka", "Yuki", "Yukiko", "Yume", "Yumi",
        "Yuna", "Yuri"#,
        #from famous_japanese
        #"" #MAYBE FILL IN LATER?
        )    

male_firstnames_Japanese = (
        #Students of the World
        # http://www.studentsoftheworld.info/penpals/stats.php3?Pays=JAP
        # Top 100 Japanese names - Japan
        #Boys first names
        "Aki", "Akira", "Alex", "Areshi", "Ari", "Atsushi", "Berry",
        "Brad", "Daichi", "Daiki", "Daisuke", "Evan", "Genki",
        "Hajime", "Haru", "Haruki", "Hayato", "Hikaru", "Hiko-Ki",
        "Hiro", "Hiroaki", "Hiroki", "Hoohi", "Issei", "Jack",
        "Jason", "Junya", "Kaito", "Katsuki", "Kazu", "Kazuki",
        "Kazuma", "Kazuya", "Kei", "Keita", "Ken", "Kenta", "Kento",
        "Kinzo", "Kiyomori", "Ko", "Kotaro", "Kouki", "Kuma",
        "Kyohei", "Makoto", "Masa", "Masaki", "Matt", "Minato",
        "Motoi", "Naoki", "Naoto", "Naoya", "Purna", "Raichi", "Ren",
        "Ryo", "Ryosuke", "Ryota", "Ryu", "Ryuki", "Shinji", "Shinya",
        "Sho", "Shota", "Shuhei", "Shun", "Shuto", "Steven", "Taichi",
        "Taiyo", "Taka", "Takahiro", "Takaya", "Take", "Takumi",
        "Takuya", "Taro", "Tatsuki", "Tatsuya", "Thomas", "Tohru",
        "Tom", "Tomohiro", "Tomoki", "Tomoya", "Toshi", "Wataru",
        "You", "Yu", "Yuichiro", "Yuki", "Yuma", "Yusuke", "Yuta",
        "Yuto", "Yuuki", "Yuya",
        #from famous_japanese
        "Eiji Mori",    # Eiji Mori (sake sommelier)
        "Kentaro",      # Kentaro Hamada (reporter)
        )    

surnames_Japanese = (
        #from https://en.wikipedia.org/wiki/List_of_most_common_surnames_in_Asia
        "Abe", "Andō", "Aoki", "Arai", "Chiba", "Endō", "Fujii", "Fujita", "Fujiwara", "Fujihara",
        "Fukuda", "Gotō", "Hara", "Harada", "Hasegawa", "Hashimoto", "Hayashi", "Hirano", "Ichikawa",
        "Ikeda", "Imai", "Inoue", "Ishida", "Ishii", "Ishikawa", "Itō", "Iwasaki", "Kaneko", "Katō",
        "Kikuchi", "Kimura", "Kinoshita", "Kobayashi", "Kojima", "Kondō", "Kōno", "Kawano", "Koyama",
        "Oyama", "Kudō", "Maeda", "Maruyama", "Masuda", "Matsuda", "Matsui", "Matsumoto", "Miura",
        "Miyamoto", "Miyazaki", "Miyasaki", "Mori", "Morita", "Murakami", "Murata", "Nakagawa",
        "Nakajima", "Nakashima", "Nakamura", "Nakano", "Nakayama", "Nishimura", "Noguchi", "Nomura",
        "Ogawa", "Okada", "Okamoto", "Ono", "Ōno", "Ōta", "Ōtsuka", "Saitō", "Saitō", "Sakai",
        "Sakamoto", "Sakurai", "Sano", "Sasaki", "Satō", "Shibata", "Shimada", "Shimizu", "Sugawara",
        "Sugahara", "Sugiyama", "Suzuki", "Takada", "Takata", "Takagi", "Takaki", "Takahashi", "Takeda",
        "Taketa", "Takeuchi", "Tamura", "Tanaka", "Taniguchi", "Uchida", "Ueda", "Ueta", "Ueno", "Wada",
        "Watanabe", "Watanabe", "Watabe", "Yamada", "Yamaguchi", "Yamamoto", "Yamashita", "Yamazaki",
        "Yamasaki", "Yokoyama", "Yoshida",
        #from famous_japanese
        "Hamada")    

#famous Japanese
#from:
# en.m.wikipedia.org/wiki/List_of_Japanese_people
# en.m.wikipedia.org/wiki/List_of_Japanese_artists
# en.m.wikipedia.org/wiki/List_of_manga_artists
# XXX famous Japanese people
# USE FOR SHIP NAMING ETC
famous_japanese = ("Akira Itō", "Akira Toriyama", "Atsushi Ōkubo", "Aya Takano",
        "Daisuke Moriyama", "Fumino Hayashi", "Funatsu Kazuki", "Hidari Jingorō",
        "Hidekaz Himaruya", "Hinako Takanaga", "Hiro Mashima", "Hiromu Arakawa",
        "Hiroshi Takashige", "Hiroshi Tomihari", "Hisashi Hirai", "Hishikawa Moronobu",
        "Kawai Kanjirō", "Kazuki Takahashi", "Ken Akamatsu", "Kenzo Okada", "Koji Ishikawa",
        "Kotaro Takamura", "Kouta Hirano", "Kume Keiichiro", "Kuroda Seiki", "Maki Murakami",
        "Mariko Mori", "Masashi Kishimoto", "Naitō Toyomasa", "Naoko Takeuchi", "Naoyuki Kato",
        "Osamu Tezuka", "Retsu Tateo", "Rumiko Takahashi", "Sakichi Toyoda", "Shigeo Fukuda",
        "Shigeru Miyamoto", "Shotaro Ishinomori", "Tachibana Higuchi", "Takashi Murakami",
        "Takashi Takeuchi", "Takeshi Obata", "Tite Kubo", "Tomoko Takahashi", "Torii Kiyonaga",
        "Toshiaki Iwashiro", "Tsugumi Ohba", "Yoko Ono")

# other Japanese
other_japanese = ("Toshio Ueno", "Eiji Mori", "Nobuchika Mori", "Nobuyuki Hirano")





#### KOREAN NAMES ####

female_firstnames_Korean = (
        #Students of the World
        # http://www.studentsoftheworld.info/penpals/stats.php3?Pays=KOR
        # Top 100 Korean names - Korea (N + S)
        #Girls first names
        "Alice", "Amy", "Anna", "Chloe", "Cho", "Choi", "Daeun", "Dahye", "Eun",
        "Eun Ji", "Eunji", "Eunseo", "Grace", "Haeun", "Han", "Hana", "Hanna", "Hannah",
        "Hansol", "Hong", "Hwang", "Hye Jin", "Hye Won", "Hyejin", "Hyemin", "Hyewon",
        "Hyun", "Hyun Ji", "Hyunji", "Jane", "Jang", "Jenny", "Jeon", "Jeong", "Ji Eun",
        "Ji Hye", "Ji Hyun", "Ji Won", "Ji Yeon", "Ji Young", "Jieun", "Jihye", "Jihyeon",
        "Jihyun", "Jimin", "Jin", "Jina", "Jisu", "Jiwon", "Jiyeon", "Jiyoon", "Jiyoung",
        "Jo", "Jung", "Kang", "Kim", "Kwon", "Lee", "Lim", "Lucy", "Min", "Min Jeong",
        "Min Ji", "Mina", "Minji", "Minju", "Oh", "Park", "Rachel", "Sarah", "Seo",
        "Seoyeon", "Shin", "So Yeon", "So Young", "Sohee", "Song", "Soyeon", "Soyoung",
        "Stella", "Su Yeon", "Subin", "Suji", "Sujin", "Sumin", "Suyeon", "Yang", "Ye Eun",
        "Ye Jin", "Yeji", "Yejin", "Yeon", "Yerim", "Yewon", "Yoon", "Yu Jin", "Yujin",
        "Yun", "Yuna", "Yuri"#,
        #from famous_koreans
        #MAYBE FILL IN LATER?
        #""
        )    

male_firstnames_Korean = (
        #Students of the World
        # http://www.studentsoftheworld.info/penpals/stats.php3?Pays=KOR
        # Top 100 Korean names - Korea (N + S)
        #Boys first names
        "Ahn", "Alex", "An", "Andrew", "Andy", "Bae", "Baek", "Cha", "Chan", "Chan Woo",
        "Changmin", "Cho", "Choi", "Chris", "Daniel", "Danny", "Dave", "David", "Dong Min",
        "Donghyun", "Eric", "Han", "Henry", "Hong", "Hoon", "Hwang", "Hyun", "Hyunwoo", "Jack",
        "Jaehyeon", "Jaehyun", "Jaewon", "Jake", "James", "Jang", "Jason", "Jay", "Jeon", "Jeong",
        "Jiho", "Jihoon", "Jihun", "Jin", "Jinwoo", "Jiwon", "Jo", "John", "Joon", "Joseph", "Ju",
        "Jun", "June", "Jung", "Junho", "Justin", "Kang", "Kevin", "Kim", "Ko", "Kwon", "Lee", "Lim",
        "Min", "Min Seok", "Minho", "Minki", "Minseok", "Minsu", "Minsung", "Moon", "Nam", "Noh",
        "Park", "Paul", "Peter", "Ryan", "Sang Min", "Sang Woo", "Sean", "Seo", "Seunghyun",
        "Shin", "Sim", "Son", "Song", "Sung", "Sung Jin", "Tommy", "Won", "Woo", "Yang",
        "Yoo", "Yoon", "Young", "Yu", "Yun"#,
        #from famous_koreans
        #""
        #MAYBE FILL IN LATER?
        )    

surnames_Korean = (
        #from https://en.wikipedia.org/wiki/List_of_most_common_surnames_in_Asia
        "Ahn", "An", "Bae", "Baek", "Bai", "Bak", "Bak", "Bhak", "Cha", "Chang",  "Chen",
        "Cheon", "Cheong", "Cho", "Cho", "Choe", "Choi", "Choo", "Chu", "Chun", "Chung",
        "Eom", "Gang", "Ghang", "Ghim", "Gim", "Go", "Goh", "Goo", "Gu", "Gwak", "Gwon",
        "Ha", "Hah", "Han", "Heo", "Her", "Hong", "Huang", "Hui", "Hur", "Hwang", "Im",
        "Im", "Jang", "Jean", "Jee", "Jen", "Jeon", "Jeon", "Jeong", "Jeong", "Ji", "Jin",
        "Jo", "Joe", "Joo", "Ju", "Jun", "Jun", "Jung", "Jung", "Juu", "Kang", "Kim", "Ko",
        "Koak", "Koh", "Koo", "Kuen", "Kwak", "Kwon", "La", "Lau", "Lee", "Lim", "Liu",
        "Min", "Mon", "Moon", "Mun", "Munn", "Na", "Nam", "Nan", "Nham", "No", "Noh", "Pae",
        "Pai", "Paik", "Pak", "Pak", "Park", "Phak", "Ra", "Rhim", "Rim", "Roh", "Ryang",
        "Ryoo", "Ryu", "Seo", "Seoh", "Seong", "Shen", "Shim", "Shin", "Shin", "Shong",
        "Shung", "Sim", "Sin", "Sin", "Sohn", "Son", "Song", "Sonn", "Suh", "Sung", "Uhm",
        "Woo", "Yang", "Yau", "Yi", "Yim", "Yoo", "Yoon", "Youn", "Yu",  "Yun", "Zhu",
        "Zuu"#,
        #from famous_koreans
        #""
        #MAYBE FILL IN LATER?
        )    

# famous Koreans
# XXX famous Korean people
# USE FOR SHIP NAMING ETC
famous_koreans = ("",
        "")

# other Koreans
other_korean = ("")




#### INDIAN NAMES ####

# 99 Indian female first names.
female_firstnames_Indian = (
        #Students of the World
        # http://www.studentsoftheworld.info/penpals/stats.php3?Pays=IND
        # Top 100 Indian names - India
        #Girls first names
        "Aashna", "Aastha", "Abigail", "Aditi", "Aishwarya", "Akansha", "Anamika", "Ananya",
        "Angel", "Anisha", "Anjali", "Anjana", "Anu", "Anusha", "Anushri", "Archita", "Arti",
        "Arusha", "Arya", "Aswini", "Ayushi", "Chandralekha", "Crowny", "Dawn", "Debbie", "Deepa",
        "Dia", "Diksha", "Dilmini", "Divya", "Diya", "Gayatri", "Indhumathi", "Ira", "Isha", "Ishika",
        "Ishita", "Juvina", "Kalyani", "Kamalika", "Katherine", "Kavya", "Khushi", "Krithika", "Lavanya",
        "Leah", "Lily", "Mahima", "Manisha", "Mary", "Mitali", "Priyanka", "Natasha", "Neelam", "Neha",
        "Niharika", "Nikita", "Nisha", "Nishi", "Nishita", "Niti", "Pavithra", "Prachi", "Priya", "Priyanka",
        "Radhika", "Ramya", "Rashi", "Rhea", "Ria", "Rishita", "Riya", "Rutuja", "Sadaf", "Sakshi", "Sam",
        "Sanjana", "Sara", "Sarah", "Sasashy", "Seema", "Shivangi", "Shivani", "Shreya", "Shrinidhi", "Simran",
        "Siya", "Sneha", "Suhani", "Swati", "Tanu", "Tanvi", "Tanya", "Tisha", "Vaishnavi", "Vani", "Varsha",
        "Vidhya"#,
        #from famous_indians
        #""
        #MAYBE FILL IN LATER?
        )    

# 101 Indian male first names.
male_firstnames_Indian = (
        #Students of the World
        # http://www.studentsoftheworld.info/penpals/stats.php3?Pays=IND
        # Top 100 Indian names - India
        #Boys first names
        "Aaditya", "Abdul", "Abhi", "Abhinav", "Abhishek", "Aditya", "Ajay", "Ajeet", "Ajith", "Akash",
        "Akshay", "Alok", "Amit", "Aniket", "Anil", "Anirudh", "Anish", "Ankit", "Ankur", "Anubhav", "Anurag",
        "Arjun", "Arun", "Aryan", "Ashish", "Atul", "Avi", "Avinash", "Deep", "Deepak", "Deepro", "Dhruv",
        "Dinesh", "Girish", "Gokul", "Harish", "Jatin", "Jay", "John", "Karan", "Kartik", "Krish", "Krishna",
        "Kumar", "Kunal", "Mahesh", "Manish", "Manoj", "Manu", "Mayank", "Mayur", "Mohit", "Naveen", "Neeraj",
        "Nikhil", "Nishant", "Nitin", "Paaus", "Parth", "Pawan", "Pranav", "Prashant", "Prateek", "Pratik",
        "Prince", "Raghav", "Rahul", "Raj", "Rajeev", "Raju", "Rakesh", "Ram", "Ramanan", "Rishabh", "Rohan",
        "Rohit", "Sam", "Sanchit", "Sanjay", "Shaan", "Shail", "Shashank", "Shekhar", "Shivam", "Shyam",
        "Siddharth", "Soham", "Sumit", "Sunil", "Sunny", "Suresh", "Tushar", "Vaibhav", "Varun", "Vedant",
        "Vikas", "Vinay", "Vishal", "Vivek", "Yash"#,
        #from famous_indians
        #""
        #MAYBE FILL IN LATER?
        )    

# 725 Indian surnames
surnames_Indian = (
        #from https://en.wikipedia.org/wiki/List_of_most_common_surnames_in_Asia
        "Devi", "Singh", "Kumar", "Das", "Kaur",
        #from https://en.wikipedia.org/wiki/Indian_name
        # In Andhra Pradesh:
        "Rao", "Kumar", "Chowdary", "Reddy", "Naidu", "Raju", "Varma", "Achari", "Sharma", "Chari", "Sharma",
        # In Arunachal Pradesh, Sikkim and northern West Bengal: 
        "Tenzin", "Tashi", "Dolma", "Passang", "Pema", "Metok", "Dhundup", "Lhamo", "Sangyal", "Yangkey",
        "Tsomo", "Rabten", "Phuntsok", "Rabgyal", "Rigzin", "Jangchup", "Tsundue", "Jorden", "Bhakto",
        "Namgyal", "Wangchuk", "Khando", "Rangdol", "Nyima", "Pemba", "Dawa", "Tsering", "Bhuti",
        "Konchok", "Gyatso", "Kelsang", "Karma", "Gyurmey", "Rinchen", "Namdol", "Choedon", "Rigsang",
        "Sonam", "Padma", "Paljor", "Namdak", "Kunga", "Norbu", "Chokphel", "Dorjee", "Jungney",
        "Dema", "Damchoe", "Dickey", "Dolkar", "Lhawang", "Legshey", "Dharma", "Bhuchung", "Lhakpa",
        "Samten", "Choenyi", "Samdup", "Ngonga", "Jampa", "Woeser", "Woeten", "Wangyal",
        "Woenang", "Wangmo",
        # Bengali Hindu names:
        "Basu", "Bose", "Dutta", "Ghosh", "Guha", "Gain", "Mitra", "Singh", "Sinha", "Sen", "Pal", "Deb",
        "Dev", "Palit", "Chanda", "Chandra", "Das", "Dam", "Kar", "Nandi", "Nag", "Som", 
        "Mukherjee", "Banerjee", "Chatterjee", "Ganguly", "Ghoshal", "Goswami", "Chakravarti", "Bhattacharya",
        "Sengupta", "Dasgupta", "Duttagupta", "Gupta", "Sen-Sharma",
        "Purkayastha", "Chaudhuri", "Roy Chaudhuri",
        "Tagore", "Thakur", "Gain", "Gayen", "Majumdar", "Mazumdar", "Biswas", "Guha-Thakurta", "Bhowmick",
        "Bhaumik", "Sarkar", "Deb-Roy", "Bakshi", "Mallick", "Malik", "Sanyal", "Bhuinya", "Banik", "Bera",
        "Debnath", "Deria", "Dawn", "Dolui", "Nath", "Munshi", "Das-Munshi", "Dewanji", "Kannungo", "Qannungoh",
        "Mahalanobis", "Majhi", "Garai", "Haldar", "Hazra", "Hati", "Jana", "Kundu", "Konar", "Kapali",
        "Maity", "Manna", "Malakar", "Makur", "Mondal", "Panja", "Sikdar", "Samanta", "Sasmal", "Sardar",
        "Sil", "Shil",
        # Assamese:
        "Barua", "Bhagawati", "Bhattacharya", "Bhattacharjee", "Borthakur", "Chakraborty", "Chakravarthi",
        "Gayen", "Gain", "Katakey", "SarmaSharma", "Thakur", "Gotras", "Chaudhary", "Das", "Kalita", "Barua",
        # Bodo Kachari:
        "Basumatary", "Bwisumatary", "Basumata", "Brahma", "Boro", "Baro", "Bodo", "Bodosa", "Baglary",
        "Borgoyary", "Chamframary", "Daimari", "Goyary", "Hajowary", "Hazary", "Iswary", "Islary", "Kachary",
        "Karjee", "Lahary", "Mandal", "Mushahary", "Mochary", "Mohilary", "Mech", "Narzary", "Narjinary",
        "Owary", "Ramchiary", "Sainary", "Swargiary", "Saiba", "Subba", "Thakur", "Wary",
        # Bihar:
        "Singh", "Yadav", "Jha", "Prasad", "Paswan", "Khan", "Gupta", "Kumar", "Choudhary", "Manjhi",
        # Gujarat
        "Ahir", "Amin", "Sisodiya", "Chawda", "Shah", "Rana", "Patel", "Shroff", "Bhakta", "Soni", "Mehta",
        "Jani", "Modi", "Desai", "Parekh", "Doshi", "Mistry", "Bhanushali", "Chotaliya", "Rathod", "Merchant",
        "Modhwadiya", "Bapodra", "Odedara", "Chudasama",
        # Haryana:
        "Choudhary", "Gujjar", "Tanwar", "Gupta", "Aggarwal", "Jain", "Hooda", "Malik", "Kataria", "Singh",
        "Yadav", "Rao",
        # Kashmir:
        "Razdan", "Nehru", "Beigh", "Baig", "Khan", "Drabu", "Wani", "Mattoo", "Fazali", "Bhat", "Shah",
        "Durrani", "Khan", "Dedmari", "Misger", "Kumar", "Mir", "Adalti", "Agha", "Aima", "Ambardar",
        "Atal", "Banday", "Bazaaz", "Bhan", "Budshah", "Bhagati", "Bhat", "Chedda", "Chetan", "Daftari",
        "Darbari", "Dar", "Dhar", "Durani", "Farash", "Fotedar", "Ganju", "Garyali", "Gilani", "Haak",
        "Hangal", "Handoo", "Jalla", "Jalali", "Jitan", "Jeetan", "Kandhari", "Kaul", "Koul", "Khemu", "Kher",
        "Khar", "Khandaar", "Kilam", "Kokiloo", "Mattoo", "Moza", "Mozaz", "Mujoo", "Nadeer", "Nadeem",
        "Naik", "Nakhasi", "Nakshband", "Nehru", "Ogra", "Pandit", "Panjabi", "Parimoo", "Pir", "Qasba",
        "Qazi", "Qasid", "Raina", "Razdan", "Shaw", "Safaya", "Sapru", "Saproo", "Saraaf", "Sultan",
        "Thusoo", "Thusu", "Thussu", "Thussoo", "Tikku", "Tickoo", "Toshkhani", "Toorki", "Turki",
        "Trakroo", "Tufchi", "Wazir", "Wakil", "Wali", "Wuthoo", "Zalpuri", "Zarabi", "Zutshi",
        #  Karnataka:   
        "Gowda", "Urs", "Shastri", "Rao", "Bhat", "Desai",
        "Hegde", "Hegade", "Shenoy", "Shett", "Shetty", "Mallya", "Kini", "Pai", "Kamath", "Rai", "Kudva",
        "Bhandary", "Baliga", "Padukone", "Mogaveera", "Adiga", "Alva", "Payyade", "Kothari", "Kadamba",
        "Bajpe", "Ullal", "Udupa", "Amin", "Anchan", "Baidya", "Baishya", "Banan", "Bangera", "Gujran",
        "Jathann", "Jathanna", "Karkera", "Kirodian", "Kotian", "Kukian", "Kukiyan", "Palan", "Palanna",
        "Poojary", "Salian", "Sanil", "Suvarna", "Talwar", "Upiyan",
        "Goudar", "Cariappa", "Bhai", "Garagad", "Biradar", "Kattimani", "Hiremath", "Chikkamatha",
        # Kerala:
        "Menon", "Nair", "Nambiar", "Pillai", "Varma", "Variar", "Nambeesan", "Kurup", "Panicker", "Thampi",
        "Thampan", "Pisharody", "Valiathan", "Kaimal", "Vaidyan", "Muthalaly",
        # Maharashtra:
        "Rane", "Kulkarni", "Soman", "Joshi", "Deshpande", "Deshmukh", "Desai", "Gaekwad", "Pawar",
        "Kale", "Wankhade", "Chaudhary", "Kolte", "Kadam", "Jadhav", "Shinde", "Ingle", "Patil",
        "Chavan", "Bhat", "Bhatt",
        "Kelkar", "Gavaskar", "Tendulkar", "Mangeshkar", "Savarkar", "Mainkar", "Madgulkar", "Mayekar",
        "Agarkar", "Pendharkar", "Bidkar", "Acharekar", "Shekatkar", "Khanvilkar", "Kamerkar", "Navalkar",
        "Naralkar", "Joglekar", "Juhekar", "Deuskar", "Manglokar", "Chindarkar", "Nagpurkar", "Sarvankar",
        "Mankar", "Matondkar", "Shegaonkar", "Maindalkar", "Medhekar", "Sukenkar", "Mondkar", "Mhaiskar",
        "Bhosale", "Gokhale", "Kale", "Bhave", "Thakre", "Mohite", "Deshpande", "Kakde", "Gore", "Rahane",
        "Rande", "Navle",
        # Odisha (Orissa):
        "Rath", "Acharya", "Kar", "Singh", "Sabat", "Pati", "Patro", "Mishra", "Misra", "Gahana", "Mund",
        "Padhy", "Padhi", "Mohapatra", "Dash", "Das", "Diwedi", "Trivedi", "Purohit", "Sarangi", "Nanda",
        "Ratha", "Panda", "Pattjoshi", "Negi", "Joshi", "Khamari", "Majhi", "Babu", "Sambalpur", "Kalahandi",
        "Balangir", "Praharaj", "Satyapathy", "Behera", "Panigrahi", "Tripathy", "Muni", "Upadhya", "Dwivedi",
        "Chaturvedi", "Hota", "Mavinkurve",
        "Bal", "Biswal", "Behera", "Dalai", "Dalei", "Palai", "Palei", "Patra", "Parida", "Pradhan", "Puhan",
        "Sha", "Pati", "Samal", "Paikaray", "Srichandan", "Samantaray", "Samanta", "Dalasingharay",
        "Jujharsingh", "Gumansingh", "Gachhayat", "Samatasinghar", "Sundarray", "Jagdev", "Jena",
        "Baliarsingh", "Harichandan", "Mangaraj", "Mardaraj", "Nayak", "Senapati", "Rao", "Rout",
        "Swain", "Sahoo", "Routaray", "Pratihari", "Chhotaray", "Champatiray", "Samantaray",
        "Khandayatray", "Raj", "Pattasani", "Satrusalya", "Danadapatta", "Mansingh", "Dalei", "Dalabehera",
        "Badajena", "Jena", "Bidyadhara", "Khuntia", "Khatua", "Mohapatra", "Mohanty", "Bhanayat", "Khandayat",
        "Sahu", "Sahoo", "Agarwal", "Samal", "Jena", "Maheshwari",
        "Mohanty", "Pattnaik", "Kar", "Das",
        "Raulo", "Rawlo", "Mali",
        #  Punjab:
        "Sodhi", "Sidana", "Sadana", "Sardana", "Chhabra", "Ichpujani", "Saluja", "Khanna", "Mattu", "Waraich",
        "Virk", "Bedi", "Bhatia", "Chambal", "Cheema", "Chauhan", "Kaleka", "Arora", "Sumag", "Smagh", "Batra",
        "Luthra", "Agnihotri", "Sood", "Bhola", "Jindal", "Kapoor", "Sachdeva", "Grover", "Chadha", "Chopra",
        "Chaudhary", "Johar", "Khanna", "Khurmi", "Malhotra", "Mehta", "Grewal", "Khangura", "Garewal",
        "Dhillon", "Ahluwalia", "Randhawa", "Gill", "Sekhon", "Brar", "Dhawan", "Soni", "Sahota", "Dhaliwal",
        "Chahal", "Shoker", "Dhariwal", "Deol", "Duggal", "Nanda", "Rattu", "Singla", "Seth", "Garg", "Ghuman",
        "Bansal", "Saini", "Sharma", "Toor", "Sidhu", "Wahi", "Singh", "Sobti", "Sinha", "Sahgal", "Sehgal",
        "Saigal", "Kaur", "Salh", "Sandhu", "Hothi", "Mehroul", "Sethi", "Shergill", "Vansil", "Chowlia",
        "Chawla", "Matharoo", "Matharu", "Atwal",
        # Uttar Pradesh:
        "Singh", "Yadav", "Singh", "Sharma", "Pandit", "Khan", "Gupta", "Choudhary", "Jatav", "Geelal",
        "Kumar", "Prasad", "Shukla", "Dubey", "Pandey"#,
        #from famous_indians
        #""
        #MAYBE FILL IN LATER?
        )    

# famous Indians
# XXX famous Indian people
# USE FOR SHIP NAMING ETC
famous_indians = ("",
        "")

# other Indians
other_indians = ("")





#### SCOTTISH NAMES     ####
#### SCOTS GAELIC NAMES ####

#List of Scottish Gaelic given names

#List of feminine Scottish Gaelic and English names
#from Wikipedia, the free encyclopedia:
#https://en.wikipedia.org/wiki/List_of_Scottish_Gaelic_given_names

female_firstnames_Scots_Gaelic = (
        #Scots Gaelic   # English equivalent
        "Ailios",       # Alice
        "Ailis",        # Alice
        "Aimil",        # Amelia, Emily
        "Aingealag",    # Angelica
        "Anabla",       # Annabella
        "Anna",         # Ann, Anne, Annie
        "Aoife",        # Eva
        "Barabal",      # Barbara
        "Baraball",     # Barbara
        "Barabla",      # Barbara
        "Bearnas",      # Bernice
        "Beasag",       # Bessy, Bessie, Betsie, Betty
        "Beathag",      # Becky, Beth, Rebecca,Sophia, Sophie
        "Beileag",      # 
        "Beitidh",      # Betty
        "Beitiris",     # Beatrice
        "Beitris",      # Beatrice
        "Bhioctoria",   # Victoria
        "Brighde",      # Bride, Bridget
        "Brìghde",      # Bride, Bridget
        "Brìde",        # Bridget
        "Cairistiòna",  # Christine
        "Cairistìne",   # Christina
        "Cairistìona",  # Christina, Christine
        "Caitir",       # Catherine, Clarissa
        "Caitlin",      # Cathleen, Kathleen
        "Caitrìona",    # Catherine, Catrina, Catriona, Katherine
        "Calaminag", 
        "Catrìona",     # Catherine, Catriona,Katherine
        "Ceana",        # Kenna
        "Ceit",         # Kate, Katie
        "Ceiteag",      # Katie, Katy, Kitty
        "Ceitidh",      # Katie
        "Ciorsdan",     # Christina
        "Ciorstag",     # Kirsty
        "Ciorstaidh",   # Kirsty
        "Ciorstan",     # Kirsty
        "Cotrìona",     # Catherine
        "Criosaidh",    # Chrissie
        "Curstag",      # Kirsty
        "Curstaidh",    # Kirsty
        "Deirdre",      # Deirdre
        "Deòiridh",     # Dorcas
        "Deònaidh",
        "Dior-bhorgàil",# Dorothy
        "Diorbhail",    # Devorgilla, Dorothy
        "Dior-bhail",   # Devorgilla, Dorothy
        "Dior-bhàil",   # Devorgilla, Dorothy
        "Dìorbhail",    # Devorgilla, Dorothy
        "Doileag",      # Dolina
        "Doilidh",      # Dolly
        "Doirin",       # Doreen
        "Dolag",        # Dolina, Dolly
        "Ealasaid",     # Elizabeth
        "Eamhair",      # Evir
        "Eilidh",       # Ailie, Ellen, Ellie, Helen
        "Eimhir",
        "Eiric",
        "Eithrig",
        "Eubh",         # Eve
        "Eubha",        # Eva, Eve
        "Èibhlin",      # Evelyn
        "Fionnaghal",   # Fiona, Flora
        "Fionnuala",    # Fenella, Finella, Finola
        "Floireans",    # Florence
        "Flòraidh",     # Flora
        "Frangag",      # Frances
        "Giorsail",     # Grace
        "Giorsal",      # Grace, Griselda, Grizzel
        "Gormall",      # Gormelia
        "Gormlaith",
        "Isbeil",       # Isobel, Isabella
        "Iseabail",     # Isabel, Isabella, Ishbel, Isobel
        "Iseabal",      # Isabella
        "Leagsaidh",    # Lexie, Lexi
        "Leitis",       # Letitia
        "Lili",         # Lilias, Lily
        "Liùsaidh",     # Louisa, Lucy
        "Lucrais",      # Lucretia
        "Lìosa",        # Lisa
        "Magaidh",      # Maggie
        "Maighread",    # Margaret
        "Mairead",      # Maretta, Margaret, Marietta
        "Mairearad",    # Margaret
        "Malamhìn",     # Malavina
        "Malmhìn",      # Malvina
        "Marsail",      # Marjory
        "Marsaili",     # Marcella, Margery, Marjory
        "Marta",        # Martha
        "Milread",      # Mildred
        "Moibeal",      # Mabel
        "Moire",        # Mary
        "Moireach",     # Martha
        "Muire",        # Mary
        "Muireall",     # Marion, Muriel
        "Màili",        # Mary, May, Molly
        "Màiri",        # Mary
        "Mòr",          # Marion
        "Mòrag",        # Morag, Marion, Sarah
        "Nansaidh",     # Nancy
        "Oighrig",      # Africa, Effie, Efric, Erica, Etta, Euphemia, Henrietta
        "Olibhia",      # Olivia
        "Peanaidh",     # Penny
        "Peigi",        # Peggy
        "Raghnaid",     # Rachel
        "Raodhailt",    # Rachel
        "Raonaid",      # Rachel
        "Raonaild",     # Rachel
        "Rut",          # Ruth
        "Seasaìdh",     # Jessie
        "Seonag",       # Joan, Shona
        "Seònaid",      # Janet, Jessie, Seona, Shona
        "Simeag",       # Jemima
        "Siubhan",      # Johann, Judith
        "Siùbhan",      # Johann, Judith
        "Siùsaidh",     # Susan, Susanna,Susie, Susy
        "Siùsan",       # Susanna, Susan
        "Sorcha",       # Claire, Clara, Sarah,Sorche
        "Stineag",
        "Sìle",         # Cecilia, Cecily, Celia, Cicily, Julia, Judith, Sheila
        "Sìleas",       # Julia
        "Sìlis",        # Cicely, Julia
        "Sìne",         # Jane, Jean, Jenny,Sheena
        "Sìneag",       # Jeanie
        "Sìonag",       # Jeannie
        "Teasag",       # Jessie
        "Teàrlag",      # Caroline, Charlotte
        "Ùna",          # Agnes, Winifred, Euna, Una
        "Una"           # Agnes, Winifred, Euna, Una
        )

#List of masculine Scottish Gaelic names
#from Wikipedia, the free encyclopedia:
#https://en.wikipedia.org/wiki/List_of_Scottish_Gaelic_given_names

male_firstnames_Scots_Gaelic = (
        #Scots Gaelic   # English equivalent
        "Adaidh",       # Adie, Addie
        "Adhamh",       # Adam
        "Àdhamh",       # Adam
        "Ailbeart",     # Albert
        "Ailean",       # Alan, Allan
        "Ailig",        # Alec, Alex, Alick
        "Ailpean",      # Alpin
        "Ailpein",      # Alpin, Alpine
        "Aindrea",      # Andrew
        "Aindreas",     # Andrew
        "Alasdair",     # Alasdair, Alastair, Alexander,Allaster, Alistair
        "Amhladh",      # Aulay
        "Amhlaibh",     # Aulay
        "Amhlaidh",     # Aulay
        "Amhlaigh",     # Aulay
        "Angaidh",      # Angie
        "Anndra",       # Andrew
        "Anndrais",     # Andrew
        "Aodh",         # Hugh
        "Aonghas",      # Aeneas, Angus, Innes
        "Aonghus",      # Angus
        "Arailt",       # Harold
        "Artair",       # Arthur
        "Artur",        # Arthur
        "Asgall",       # Askill
        "Àaron",        # Aaron
        "Baltair",      # Walter
        "Bearnard",     # Bernard
        "Beathan",      # Bean, Benjamin
        "Beistean",
        "Benneit",      # Benedict
        "Bhaltair",     # Walter
        "Bhatair",      # Walter
        "Brian",        # Brian
        "Cailean",      # Colin
        "Calum",        # Calum, Malcolm
        "Caomhainn",    # Kevin
        "Cathal",       # Cathal, Cathel, Charles,Kathel
        "Ciaran",       # Kieran
        "Cliamain",     # Clement
        "Coinneach",    # Kenneth
        "Colla",        # Coll
        "Colum Cille",  # Columba
        "Comhnall",     # Conal
        "Conall",       # Connal
        "Conn",         # Con, Conn
        "Cormac",       # Cormac
        "Cormag",
        "Crìsdean",     # Christopher, Christian
        "Cuithbeart",   # Cuthbert
        "Daibhidh",     # David, Davie
        "Dàibhidh",     # David, Davie
        "Daidh",        # David
        "Daniel",       # Daniel
        "Deorsa",       # George
        "Deòrsa",       # George
        "Diarmad",      # Dermid, Dermot,Diarmid
        "Domhnall",     # Donald
        "Dòmhnall",     # Donald
        "Domhnull",     # Donald
        "Dòmhnull",     # Donald
        "Donaidh",      # Donnie
        "Donnchadh",    # Duncan
        "Dubh",         # Duff
        "Dubh-shìth",   # Duffie
        "Dubhghall",    # Dougal, Dugal, Dugald
        "Dànaidh",      # Danny
        "Dùghall",      # Dougal, Dugal, Dugald
        "Dùghlas",      # Douglas
        "Eachann",      # Hector
        "Eacharn",      # Hector
        "Eairdsidh",    # Archie
        "Ealar",        # Ellar
        "Eanraig",      # Henry
        "Eanruig",      # Henry
        "Eideard",      # Edward
        "Eirdsidh",     # Archie
        "Ellair",       # Ellar
        "Eoghann",      # Ewan, Ewen, Hugh
        "Eòghann",      # Ewan, Ewen, Hugh
        "Eioghnn",      # Ewan, Ewen, Hugh
        "Eumann",       # Edmund
        "Eòghan",       # Ewan, Hugh
        "Eòin",         # John, Jonathan
        "Eòsaph",       # Joseph
        "Faolan",       # Fillan
        "Fearchar",     # Farquhar
        "Fearghas",     # Fergus
        "Filib",        # Philip, Phillip
        "Fionn",        # Fingal
        "Fionnghall",   # Fingal, Fingall
        "Fionnghan",    # Fingan
        "Fionnlagh",    # Findlay, Finlay, Finley
        "Frang",        # Frank
        "Frangan",      # Francis
        "Frangean",     # Frankin
        "Friseal",      # Fraser
        "Gill-easbuig", # Archibald
        "Gilleasbuig",  # Archibald
        "Gill-Eathain", # Gillean
        "Gill-Eòin",    # Gillean
        "Gill-Iosa",    #Gillies
        "Gillìosa",     #Gillies 
        "Gille-Aindreis",# Gillanders
        "Gille-Brìdhde",# Gilbert
        "Gille-Caluim", # Malcolm
        "Gille-Crìosd", # Christopher, Gillchrist
        "Gilleasbaig",  # Archibald, Gillespie
        "Gillebeart",   # Gilbert
        "Gillebrìde",   # Gilbert
        "Goiridh",      # Godfrey, Geoffrey
        "Goraidh",      # Godfrey, Geoffrey
        "Grannd",       # Grant
        "Greum",        # Graeme, Graham
        "Griogair",     # Gregor, Gregory, Grigor
        "Guaidre",      # Godfrey
        "Gòrdan",       # Gordon
        "Hamish",       # James
        "Harailt",      # Harold
        "Horas",        # Horace
        "Hùisdean",
        "Iagan",
        "Iain",         # John, Iain, Ian, Jock, Jack
        "Ianatan",      # Jonathan
        "Iomhair",      # Iver, Ivor, Edward, Evander
        "Iomhar",       # Ivor
        "Isaac",        # Isaac
        "Iàcob",        # Jacob
        "Iòna",         # Jonah
        "Iòsaph",       # Joseph
        "Labhrann",     # Laurence, Lawrence
        "Labhruinn",    # Lawrence
        "Lachlann",     # Lachlan
        "Laomann",      # Lamont
        "Luthais",      # Lewis, Louis
        "Lùcas",        # Luke
        "Maoilios",     # Myles
        "Maol-Chaluim", # Malcolm
        "Maol-Domhnuich",# Ludovic
        "Maol-Dòmhnuich",# Ludovic
        "Maol-Iosa",    # Malise
        "Maol-Moire",   # Miles, Myles
        "Maoldònaich",  # Ludovic
        "Maolmhuire",   # Myles
        "Maolruibh",    # Milroy
        "Marc",         # Mark
        "Marcas",       # Mark
        "Martainn",     # Martin
        "Màrtainn",     # Martin
        "Mata",         # Matthew
        "Micheil",      # Michael
        "Morgan",       # Morgan
        "Muireach",     # Murdoch
        "Munga",        # Mungo
        "Mungan",       # Mungo
        "Murchadh",     # Murdo, Murdoch
        "Mànas",        # Magnus
        "Mànus",        # Magnus
        "Mìcheal",      # Michael
        "Mìcheil",      # Michael
        "Neacal",       # Nicol, Nicholas
        "Neachdainn",   # Nechtan
        "Niall",        # Neal, Neale, Neil, Niall
        "Niallghus",
        "Oilbhreis",    # Oliver
        "Oisean",       # Ossian
        "Padean",       # Paton
        "Padruig",      # Patrick
        "Para",         # Pat, Pete
        "Peadair",      # Peter
        "Peadar",       # Peter
        "Peadaran",     # Peterkin
        "Peadrus",      # Petrus
        "Prainnseas",   # Francis
        "Pàdair",       # Patrick, Peter
        "Pàdraig",      # Patrick, Peter
        "Pàdruig",      # Patrick
        "Pàl",          # Paul
        "Pàra",         # Patrick
        "Pàrlan",       # Bartholemew, Parlan
        "Pòl",          # Paul
        "Raghnall",     # Ranald, Randal, Ronald
        "Raibeart",     # Robert
        "Raonull",      # Ranald, Ronald
        "Ringean",      # Ninian, Ringan
        "Risteard",     # Richard
        "Rob",          # Rob, Robert
        "Roibeart",     # Robert
        "Ruairidh",     # Derrick, Roderick, Rory
        "Ruaraidh",     # Derrick, Roderick, Rory
        "Ruiseart",     # Richard
        "Ràild",        # Harold
        "Sachairi",     # Zachary
        "Samuel",       # Samuel
        "Sandaidh",     # Sandy
        "Seaghdh",      # Seth, Shaw
        "Seathan",      # John
        "Seoc",         # Jack, Jock
        "Seocan",       # Jock
        "Seonaidh",     # Johnnie, Johnny
        "Seoras",       # George
        "Seumas",       # Hamish, James
        "Seòras",       # George
        "Seòsaidh",     # Joseph
        "Sgàire",       # Zachary
        "Sim",          # Simon
        "Simidh",       # Simon
        "Solamh",       # Solomon
        "Somhairle",    # Samuel, Somerled, Sorley
        "Steaphan",     # Stephen, Steven
        "Stiùbhard",    # Stuart, Stewart
        "Stiùbhart",    # Stewart
        "Sìm",          # Sime, Simon
        "Sìomon",       # Simon
        "Tadhg",        # Tad, Teague, Teigue
        "Tamhas",       # Thomas
        "Taog",         # Teague
        "Tasgall",      # Taskill
        "Tearlach",     # Charles
        "Teàrlach",     # Charles
        "Tiobaid",      # Theobald
        "Tomag",        # Tommy
        "Tomaidh",      # Tommy
        "Torcadall",    # Torquil
        "Torcall",      # Torquil
        "Torcull",      # Torquil
        "Tormod",       # Norman
        "Tormoid",      # Norman
        "Tàmhas",       # Thomas
        "Tòmachan",     # Tommy
        "Tòmas",        # Thomas
        "Uailean",      # Valentine
        "Ualan",        # Valentine
        "Ualraig",      # Walrick
        "Uarraig",      # Kennedy
        "Uilleachan",   # Willie
        "Uilleam",      # William
        "Uisdean",      # Eugene, Hugh
        "Ùisdean"       # Eugene, Hugh
        )


#List of Scottish Gaelic surnames
#From Wikipedia, the free encyclopedia:
#https://en.wikipedia.org/wiki/List_of_Scottish_Gaelic_surnames

surnames_Scots_Gaelic = (
        #Scots Gaelic   # English equivalent
        "Aileanach",    # Allan, Allanach, MacCallan
        "Ailpeanach",   # MacAlpine
        "Allanach",     # Allan, Allanach, MacCallan
        "Ambarsan",     # Anderson
        "Andarsan",     # Anderson
        "Anndrasdan",   # Anderson
        "Arasgain",     # Erskine
        "Bànach",       # Bain
        "Baran",        # Barron
        "Barrach",      # Dunbar
        "Beitean",      # Beaton, Bethune
        "Bhàsa",        # Vass
        "Bhodhsa",      # Vass
        "Blacach",      # Black
        "Blàr",         # Blair
        "Blàrach",      # Blair, Muir
        "Bochanan",     # Buchanan
        "Boid",         # Boyd
        "Bòid",         # Boyd
        "Bòideach",     # Boyd
        "Bràigheach",   # MacGillivray
        "Breac",        # Breck
        "Breathnach",   # Galbraith, Walsh, Welsh
        "Brothaigh",    # Brodie
        "Bruis",        # Bruce
        "Brùn",         # Broun, Brown
        "Brus",         # Bruce
        "Buideach",     # Budge
        "Buidheach",    # Bowie, Buie
        "Buids",        # Budge
        "Buiseid",      # Bisset
        "Cailbhin",     # Calvin
        "Caileanach",   # Callanach, MacCallan
        "Caimbeul",     # Campbell
        "Caimbeulach",  # Campbell
        "Camran",       # Cameron
        "Camshron",     # Cameron
        "Camshronach",  # Cameron
        "Cananach",     # Buchanan
        "Canonach",     # Buchanan, MacPherson
        "Caoidheach",   # Kay, MacKay
        "Caolaisdean",  # Kelso
        "Catach",       # Catach, Catto
        "Catan",        # Cattenach
        "Catanach",     # Cattenach
        "Ceallach",     # Kelly
        "Ceanadach",    # Kennedy
        "Ceannaideach", # Kennedy
        "Cearrach",     # Kerr
        "Ceiteach",     # Keith
        "Ciar",         # Keir
        "Ciarach",      # Keir
        "Ciogach",      # Eggo
        "Coineagan",    # Cunningham
        "Crannach",     # Cranna
        "Criatharach",  # Crerar
        "Cuimeanach",   # Comyn, Cumming
        "Cuimein",      # Comyn, Cumming
        "Cuimeineach",  # Comyn, Cumming
        "Càidh",        # Caie, Kay, Keith
        "Cèamp",        # Kemp
        "Cèampach",     # Kemp
        "Còmhan",       # Cowan, MacCowan
        "Creag",        # Craig
        "Creagach",     # Craig
        "Dalais",       # Dallas
        "Deòir",        # Dewar
        "Deòireach",    # Dewar
        "Dòmhnallach",  # MacDonald
        "Dòmhnullach",  # MacDonald
        "Druimeanach",  # Drummond
        "Druimein",     # Drummond
        "Druimeineach", # Drummond
        "Druiminn",     # Drummond
        "Dubh",         # Dow, Black
        "Dubhach",      # MacDuff
        "Dùbhghlas",    # Douglas
        "Dùghallach",   # Coull, Dowell, MacDougall, MacDowall
        "Dùghlas",      # Douglas
        "Dùghlasach",   # Douglas
        "Dunaid",       # Dunnet
        "Dunaidh",      # Downie
        "Eabarcrombaigh",# Abercrombie
        "Fearghasdan",  # Ferguson
        "Fionnlasdan",  # Finlayson
        "Flimean",      # Fleming
        "Foirbeis",     # Forbes
        "Foirbeiseach", # Forbes
        "Forsàidh",     # Forsyth
        "Fòlais",       # Foulis, Fowlis
        "Friseal",      # Fraser, Frazer
        "Frisealach",   # Fraser, Frazer
        "Gall",         # Gall
        "Gallach",      # Gall, Gallie, Gollach
        "Geadais",      # Geddes
        "Geadasach",    # Geddes
        "Gearailteach", # Fitzgerald
        "Gilios",       # Gillies
        "GillAndrais",  # Gillanders
        "GillEasbaig",  # Archbold, Archibald, Bishop, Gillespie
        "GillEasbuig",  # Gillespie, Archibald
        "GilleChriosd", # Gilchrist, Christie
        "GilleChrìost", # Gilchrist, Christie
        "Gill'Iosa",    # Gillies
        "Giobsan",      # Gibson
        "Glas",         # Glass, Gray
        "Gobha",        # Gow, Smith
        "Grannd",       # Grant
        "Grannda",      # Grant
        "Granndach",    # Grant
        "Greum",        # Graeme, Graham
        "Greumach",     # Graeme, Graham
        "Griogal",      # MacGregor
        "Griogalach",   # MacGregor
        "Griogarach",   # Gregg, Greig, Greer, Grierson, MacGregor
        "Guaire",       # Noble
        "Guinne",       # Gunn
        "Gunnach",      # Gunn
        "Gutraidh",     # Guthrie
        "Gòrdan",       # Gordon
        "Gòrdanach",    # Gordon
        "Ìomharach",    # Iverach, Ivory
        "Latharnach",   # Larnach
        "Lathurna",     # Lorne
        "Leamhanach",   # Lennox
        "Leamhnach",    # Lennox
        "Leòideach",    # Cloud, MacLeod
        "Lobhdain",     # Lothian
        "Loganach",     # Logan
        "Loudain",      # Lothian
        "Lìos",         # Lees
        "Lìosach",      # Gillies, Lees
        "Lùtair",       # Luther
        "Mac a' Bhacstair",     # Baker, Baxter, MacVaxter
        "Mac a' Bhacastair",    # Baker, Baxter, MacVaxter
        "Mac a' Bhàird",        # Baird, Ward
        "Mac a' Bhàirling",     # MacFarlane
        "Mac a' Bharain",       # Barron, Warren
        "Mac a' Bhiataich",     # MacCavity, MacVitie
        "Mac a' Bhiocair",      # MacVicar
        "Mac a' Bhreatannaich", # Braithnoch, Bratney, Bratnie, Bretnoch, Calbraith, Galbraith, MacBratney
        "Mac a' Bhreatnaich",   # Galbraith, Bratney, Cretney
        "Mac a' Bhruthainn",    # MacBrayne, Brown
        "Mac a' Chananaich",    # Buchanan
        "Mac a' Charraige",     # Craig
        "Mac a' Chléirich",     # Clark etc., MacClery, MacLerie, Clerie
        "Mac a' Chombaich",     # Colquhoun, MacCombie
        "Mac a' Chriathrair",   # Crerar
        "Mac a' Chrosain",      # MacCrossan
        "Mac a' Chruiteir",     # Harper, MacWhirter
        "Mac a' Ghniomhaid",    # Agnew
        "Mac a' Ghobhainn",     # MacGavin, MacGowan, Smith, Gow
        "Mac a' Ghoill",        # Gall, MacGill
        "Mac a' Ghreidheir",    # Grieve, Grierson
        "Mac a' Ghreusaiche",   # Grassick, Grassie, Soutar
        "Mac a' Ghrùdair",      # Brewster, Gruer, MacGruer, MacGruther, Magruder
        "Mac a' Leòra",         # MacClure, MacLure
        "Mac a' Lìos",          # Lees, MacLeish
        "Mac a' Mhaighstir",    # MacMaster
        "Mac a' Mhaoilein",     # MacMillan, MacWhillan, Quillan
        "Mac a' Mhaoir",        # Mair, Weir
        "Mac a' Mhiadhaich",    # May, Omay, Omey
        "Mac a' Mhuilleir",     # Millar, Milne
        "Mac a' Phearsain",     # MacPherson
        "Mac a' Phì",           # Fee, MacPhee, MacCaffey
        "Mac an Aba",           # Abbot, Abbotson, Macnab
        "Mac an Airgid",        # Sillars
        "Mac an Deòir",         # Dewar, Macindeoir
        "Mac an Deòraidh",      # Major, Jorie, MacJarrow
        "Mac an Dorsair",       # Dorward, Durward
        "Mac an Duibh",         # Macindoe
        "Mac an Fhigheadair",   # MacNider
        "Mac an Fhilidh",       # MacNeillie, Neil
        "Mac an Fhleisteir",    # Fletcher, Leslie
        "Mac an Fhoirbhich",    # Munro
        "Mac an Fhùcadair",     # MacKnockater, MacNucator, Walker
        "Mac an Fhuibhir",      # MacNair, Weir
        "Mac an Iasgair",       # Fisher, MacInesker.
        "Mac an Lamhaich",      # Lennie
        "Mac an Làmhaich",      # Lennie
        "Mac an Leighe",        # MacLeay
        "Mac an Lèigh",         # Beaton, Livingston, Livingstone, MacLeay
        "Mac an Luaimh",        # Mulloy
        "Mac an Oighre",        # MacNair
        "Mac an Ollaimh",       # MacInally, MacNally
        "Mac an Rìgh",          # MacNee, King
        "Mac an Rothaich",      # Munro
        "Mac an Ruaidh",        # Macanroy, Macinroy, Roy
        "Mac an Sporain",       # MacSporran, Purser, Purcell
        "Mac an Tàilleir",      # Taylor
        "Mac an Tòisich",       # Mackintosh, Macintosh, Tosh
        "Mac an t-Sagairt",     # MacTaggart, Taggart
        "Mac an t-Saoir",       # Macintyre, MacTear, Tyre, Wright
        "Mac an t-Sealgair",    # Hunter
        "Mac an t-Srònaich",    # Stronach
        "Mac an Tuairneir",     # Turner
        "Mac an Uidhir",        # MacNair Weir
        "Mac Iain Bhallaich",   # Malloch
        "Mac Iain Duibh",       # MacIndoe
        "Mac Iain Ruaidh",      # MacInroy, MacAnroy
        "Mac Iain Uidhir",      # MacNair
        "Mac na Carraige",      # Craig
        "Mac na Ceàrda",        # Caird, Sinclair
        "Mac na Ceàrdaich",     # Caird, Sinclair
        "Mac na Maoile",        # MacMillan
        "Mac O' Dreain",        # Drain
        "Mac O' Seannaig",      # Shannon
        "Mac'Ill'Anndrais",     # Anderson, MacAndrew, Gillanders
        "Mac'IlleBhreac",       # Breck
        "Mac'Ill'Eathainn",     # MacLean
        "Mac'Ill'Fhinnein",     # MacLennan
        "Mac'Ill'Fhinntain",    # Clinton, MacLinton
        "Mac'Ill'Fhionndaig",   # MacClintock
        "Mac'Ill'Iosa",         # Gillies, MacLeish
        "Mac'Ill'Oig",          # Ogg, Young
        "Mac'Ille na Brataich", # Bannerman
        "Mac'IlleBhàin",        # Bain, Micklewain, Milwain, Whyte
        "Mac'IlleBhuidh",       # Bowie, Buie, Ogilvy
        "Mac'IlleChiar",        # Kerr, Keir
        "Mac'IlleDhuibh",       # Black, Blackie, Dow
        "Mac'IlleMhìcheil",     # Carmichael, Gilmichael
        "Mac'IlleMhòire",       # Gilmour, Gilmore
        "Mac'IlleNaoimh",       # MacNiven
        "Mac'IlleRiabhaich",    # Darach, Darroch etc., Reoch, Revie, Riach
        "Mac'IlleRuaidh",       # Gilroy, MacIroy, Reid, Roy
        "Mac'Uirigh",           # Currie
        "MacAbhra",             # MacAra
        "MacAbhsalain",         # Causland, MacAuslan
        "MacAdaidh",    # MacAdie, MacCadie, Munro
        "MacÀdaidh",    # MacAdie, MacCadie, Munro
        "MacAdhaimh",   # Adam, Adamson, MacAdam, MacCaw, MacKeggie
        "MacÀdhaimh",   # Adam, Adamson, MacAdam, MacCaw, MacKeggie
        "MacÀidh",      # MacKay
        "MacAididh",    # MacAdie
        "MacAilein",    # Allan, Allanson, Callan, MacAllan
        "MacAilpein",   # Alpine, MacAlpine
        "MacAlasdair",  # Alexander, MacAlister, MacAllister,MacAndie, McElshender
        "MacAmbrais",   # Cambridge, Chambers, MacCambridge
        "MacAmhalghaidh",# Cowley, MacAulay, Oliver
        "MacAmhlaidh",  # MacAulay
        "MacAmhlaigh",  # Cowley, MacAulay
        "MacAnndaidh",  # Andie, MacAndie
        "MacAnndra",    # Anderson, Andrew, MacAndrew
        "MacAnndrais",  # Anderson, Andrew, MacAndrew
        "MacAodhagain", # MacKeegan
        "MacAoidh",     # Kay, MacGhie, MacHeth, MacKay,MacHugh, MacKee, MacKie
        "MacAoidhein",  # MacQuien
        "MacAomalain",  # Bannatyne
        "MacAonghais",  # Angus, Canch, MacAinsh,MacCance, MacInnes, Innes
        "MacAra",       # MacAra
        "MacArtain",    # MacArthur, MacCartney
        "MacArtair",    # Arthur, Carter, MacArthur
        "MacAsgaidh",   # Caskie, MacCaskie
        "MacAsgaill",   # MacAskill
        "MacAsgain",    # MacAskin
        "MacBeatha",    # Beaton, Bethune, MacBeath, MacBeth, MacBey
        "MacBeathag",   # MacBeth
        "MacBhàididh",  # MacWattie, Watson, Watt
        "MacBharrais",  # MacVarish
        "MacBhàtair",   # MacWalter, Qualtrough, Watson, Watt, Watters
        "MacBheatha",   # MacBeth, MacVeigh, MacVey,Beith
        "MacBheathaig", # MacBeth, MacBethock
        "MacBheathain", # MacBain, MacBean, MacVean
        "MacBhigein",   # MacFigan, Little
        "MacBhiocair",  # MacVicar
        "MacBhlàthain", # Blain, Blane
        "MacBhradain",  # Braden, Salmon(d)
        "MacBhraonaigh",# Burnie
        "MacBhrìghdeinn",# Bryden, MacBridan
        "MacCàba",      # MacCabe
        "MacCaibe",     # MacCabe
        "MacCailein",   # Colinson, Cullen, MacCallan
        "MacCain",      # MacCann, MacCain, MacKean
        "MacCaisgein",  # MacAskin
        "MacCalmain",   # MacCalman, Murchison
        "MacCaluim",    # MacCallum, Malcolm(son)
        "MacCaog",      # MacCaig
        "MacCaoig",     # Caig, MacCaig
        "MacCardaidh",  # Hardie, MacHardie, MacHardy
        "MacCarmaig",   # Cormack, MacCormick
        "MacCathachaidh",# MacCarthy
        "MacCathail",   # Cail, MacAll, MacCail, MacCall, MacKail
        "MacCathbhaidh",# MacCaffie, MacHaffie, Mahaffie
        "MacCathain",   # MacCann, MacKean, MacCain
        "MacCathasaigh",# Cassie
        "MacCathbharra",# MacAffer, MacCaffer
        "MacCeallaig",  # MacKellaig
        "MacCeallaigh", # Kelly
        "MacCeallair",  # MacKellar
        "MacCearnaigh", # Cairnie
        "MacCearraich", # MacKerrow
        "MacCeasain",   # Kesson
        "MacChoinnich", # MacKenzie
        "MacCianain",   # Keenan
        "MacCiarain",   # MacKerron
        "MacCiomalain", # Bannatyne
        "MacCionadha",  # MacKenna, MacKinnie
        "MacCinidh",    # MacKenna, MacKinnie
        "MacClambroch", # Landsburgh
        "MacCnaimhin",  # MacNevin
        "MacCnusachainn",# Kennedy
        "MacCodrum",    # MacCodrum
        "MacCoinnich",  # Kynoch, Mackenzie, MacKinnie
        "MacCoinnigh",  # MacWhinnie
        "MacColla",     # MacColl
        "MacComhainn",  # Cowan, MacCowan
        "MacConaill",   # MacConnell, MacWhannell
        "MacConnain",   # Connon
        "MacCosgraigh", # MacCoskrie
        "MacCorcadail", # MacCorquodale
        "MacCormaig",   # MacCormack, MacCormick
        "MacCrain",     # MacCrain, Crane
        "MacCreamhain", # Crawford, Crawfurd
        "MacCriomain",  # Grimond, MacCrimmon
        "MacCrithein",  # MacNiven
        "MacCrosain",   # Crossan, MacCrossan
        "MacCruimein",  # Grimmond, MacCrimmon
        "MacCrìsdein",  # Christie, Chrystal, MacCrystal
        "MacCròin",     # MacCrone
        "MacCuaig",     # Cook, MacCuaig
        "MacCuidhein",  # MacDonald
        "MacCuilcein",  # MacQuilken, Wilkins, Wilkinson
        "MacCuinn",     # Conn, MacQueen, Quinn
        "MacCuinnleis", # Candlish, Chandlish, MacCandlish
        "MacCuirc",     # MacGurk, Quirk
        "MacCuithein",  # MacDonald, MacQueen, MacQuien
        "MacCullach",   # MacCulloch
        "MacCullaich",  # MacCulloch
        "MacCumasgaigh",# Comiskey
        "MacCumhais",   # MacCuish
        "MacCuthais",   # MacCuidh
        "MacCòiseam",   # MacCoshin, MacDonald
        "MacCòmhain",   # Cowan, MacCowan
        "MacCòmhghan",  # MacCowan
        "MacCùga",      # Cook
        "MacDheòrsa",   # MacGeorge, Major
        "MacDhiarmaid", # MacDermid, MacDiarmid, Campbell
        "MacDhonnchaidh",# Duncan, MacConnachie, Robertson
        "MacDhrostain", # MacRostie
        "MacDhubhaich", # MacDuff, Duffy, MacDuthy
        "MacDhubhaig",  # MacCuaig
        "MacDhubhShìth",# Duffy, Fee, MacDuffie, MacFee
        "MacDhubhthaich",# MacDuff, Duffy, MacDuthy
        "MacDhuibh",    # MacDuff, MacDui
        "MacDhunlèibhe",# Livingstone
        "MacDiarmaid",  # MacDermid, Campbell
        "MacDhàibhidh", # Davie, Davidson, Day, Deason
        "MacDhòmhnaill",# Donald, Donaldson, MacConnell,MacDonald
        "MacDhùghaill", # Coles, Coull, Dowall, MacDougall, MacDowell
        "MacDhùnShléibhe", # Livingston, MacLeay
        "MacEachaidh ",  # McGeachie, MacGeachie, McGeachy, MacGeachy 
        "MacEachainn",   # MacEachen, MacGeachen, McGeechan
        "MacEachairn",   # MacEachern, MacKechnie
        "MacEacharna",   # Cochrane, MacEachern,MacKechnie
        "MacEalair",     # MacKellar, Quiller
        "MacEalar",      # Mackellar, Quiller
        "MacEamailinn",  # Bannatyne
        "MacEanain",     # MacKinnon
        "MacEanraig",    # Henderson, Hendry, Henry, MacKendrick
        "MacEanraig",    # Henderson, Hendry, Henry, MacKendrick
        "MacEòghainn",   # MacEwan, MacEwen, Ewing, MacHugh, Owen
        "MacFhearchair", # Carrocher, Farquhar, Farquharson, Kerracher, MacErchar, MacFarquhar, MacKerracher, Mackerchar
        "MacFhearghail", # MacKerral
        "MacFhearghais", # Fergus, Ferguson, Fergusson,Ferries, MacFerries, MacKerras,MacKerruish
        "MacFhilib",     # MacGilp, MacKillop, Philp
        "MacFhiongain",  # MacKinnon
        "MacFhionghain", # MacKinnon
        "MacFhionghuin", # MacKinnon
        "MacFhionnlaigh",# Findlay, Finlayson, Macinlay,MacIntosh, Mackinlay
        "MacFhitheachain",      # MacIchan, Mackichan
        "MacFhlaithbheartaich", # MacLafferty, MacLarty, MacLaverty
        "MacFhraing",    # Rankin
        "MacFhraingein", # MacCracken, Rankin
        "MacFigeinn",    # Little, Littleson, MacFigan
        "MacFrìdeinn",   # Brydan, MacBridan
        "MacFuirigh",    # MacVurich
        "MacGairbheith", # Garvie, Jarvie, MacGarva, MacGarvie
        "MacGaradh",     # Hay, MacGarrie
        "MacGhearailt",  # Fitzgerald
        "MacGill-Eain",  # MacLean
        "MacGhille",     # MacGill
        "MacGill'Earnain",      # MacLearnan
        "MacGill'Easbaig",      # Archbold, Archibald, Bishop, Gillespie
        "MacGill'Eòin",         # Meiklejohn
        "MacGill'Fhaolagain",   # MacKilligan
        "MacGill'Fhiontag",     # MacLintock
        "MacGill'Oig",          # Ogg, Young
        "MacGill'Onaidh",       # MacGillony
        "MacGille",             # MacGillivray
        "MacGilleBhàin",        # Bain, Bayne, MacBain, Micklewain, Milvain, Wayne, Whyte
        "MacGilleBhràth",       # MacGillivray
        "MacGilleBhreac",       # Breck
        "MacGilleBhrìghde",     # Gibb, Gibson, Gilbert, Gilbride, MacBryde
        "MacGilleChaluim",      # MacLeod
        "MacGilleChrìosd",      # MacGilchrist, Christie
        "MacGilleDhonaghart",   # MacDonald
        "MacGilleathain",       # Clean, Gellion, Gilzean, Lane, MacLaine, MacLean
        "MacGilleDhuibh",       # Black, Blackie
        "MacGilleFhialain",     # MacLellan
        "MacGilleGhlais",       # Glass, Gray
        "MacGillIosa",          # Gillies, MacLeish
        "MacGilleMhartainn",    # Gilmartin
        "MacGilleRiabhaich",    # Darroch, MacIlwraith, Reoch, Revie, Riach
        "MacGilleSeathanaich",  # Shaw
        "MacGiobain",           # Cubbin, MacGibbon, Gibson
        "MacGlaisein",          # Glashan, MacGlashan
        "MacGoraidh",           # Gorrie, MacGorrie, Godfrey, Jeffrey(s)
        "MacGobhainn",          # MacCowan, MacGowan, Smith
        "MacGoraidh",           # Gorrie, MacGorrie, Godfrey, Jeffrey(s)
        "MacGriogair",          # Gregory, Grigor, MacGregor, Greig, Gregg, Grierson
        "MacGuaire",            # Curry, MacGuire, MacQuarrie, Noble
        "MacGumaraid",          # Montgomery
        "MacIain",              # Johnson, Johnston, Kean, MacIan,MacKean, MacDonald
        "MacIllAnndrais",       # Anderson, Gillanders, MacAndrew
        "MacIllAodhagain",      # MacLagan
        "MacIllDheòra",         # MacClure, MacLure
        "MacIllEarnain",        # MacLearnan
        "MacIllEasbaig",        # Archibald, Gillespie
        "MacIllEathain",        # Clean, Gellion, Gilzean, Lane, MacLaine, MacLean
        "MacIlleBhàin",         # Bain, Bayne, MacBain, Micklewain, Milvain, Whyte
        "MacIlleBheathain",     # MacIlvain, MacIlwaine, Wayne
        "MacIlleBhlàthain",     # Blain, Blane, MacBlane
        "MacIlleBhràth",        # MacGillivray
        "MacIlleBhrìghde",      # Gibb, Gilbert, Gilbride, MacBryde
        "MacIlleBhris",         # MacElfrish
        "MacIlleBhuidhe",       # Bowie, Buie, Ogilvie
        "MacIlleChaluim",       # MacCallum, Malcolm(son)
        "MacIlleChatain",       # Hatton
        "MacIlleChathbhaidh",   # MacCaffie, MacHaffie, Mahaffie
        "MacIlleChiar",         # Keir, Kerr
        "MacIlleChiarain",      # MacIlherran, MacKerron, Herron, Sharpe
        "MacIlleChomhghain",    # Cowan, MacCowan
        "MacIlleChonaill",      # MacWhannell
        "MacIlleChrìosd",       # Gilchrist
        "MacIlleChruim",        # Crum, MacCrum
        "MacIlleDhòmhnaich",    # Downie, MacIldownie
        "MacIlleDhonaghart",    # MacDonald
        "MacIlleDhubhthaich",   # Duthie, Maduthy
        "MacIlleDhuibh",        # Black, Dow, Dowie, Howie, Huie
        "MacIlleDhuinn",        # Brown, Donn, Dunn
        "MacIlleGhlais",        # Glass, Gray
        "MacIlleGhuinnein",     # Winning
        "MacIlleGhuirm",        # Blue
        "MacIll'Éidich",        # MacLatchie, MacLetchie
        "MacIll'Eòin",          # Meiklejohn
        "MacIlleMhaoil",        # Bell, MacGill, MacMillan
        "MacIlleMhàrtainn",     # MacMartin, Gilmartin
        "MacIlleMhearnaig",     # Warnock
        "MacIlleMhìcheil",      # Carmichael, MacMichael
        "MacIlleMhoire",        # Gilmore, Gilmour, Morrison
        "MacIlleNaoimh",        # MacNiven
        "MacIllePhàdraig",      # Milfrederick
        "MacIllePheadair",      # MacFater, MacPhater, Paterson, Peters
        "MacIlleRiabhaich",     # Darroch, MacIlwraith, Reoch, Revie, Riach
        "MacIlleRuaidh",        # Gilroy, MacIlroy, Milroy, Reid, Roy
        "MacIlleSheathain",     # MacCheyne, MacShane, Sheen
        "MacIlleSheathanaich",  # Shaw
        "MacIlleSheathnaich",   # Shaw
        "MacIlleThòmhais",      # Hosier, MacLehose, Mucklehose
        "MacIllFhaolagain",     # MacKilligan
        "MacIll'Fhaolain",      # Cleland, Gilfillan, Gilliland, MacClelland, MacLellan
        "MacIllFheargain",      # MacLergan
        "MacIll'Fhialain",      # MacLellan
        "MacIll'Fhinnein",      # MacLennan
        "MacIll'Fhionndaig",    # Lindsay, MacClintock, MacLintock
        "MacIllFhionndain",     # Clinton, MacLinton
        "MacIllIanain",         # MacLennan
        "MacIllÌmheir",         # MacLiver, Oliver
        "MacIllIomchadha",      # MacClumpha, MacLumpha
        "MacIllÌosa",           # Gillies, Lees, MacLeish
        "MacIllOnchon",         # Clanachan, Clenachan, MacClanachan
        "MacIllOnfhaidh",       # MacAlonie, MacGillonie
        "MacIll'osa",           # Gillies, MacLeish
        "MacIllUidhir",         # MacClure, MacLure
        "MacIomhair",           # MacIver
        "MacÌomhair",           # MacIver
        "MacIonmhainn",         # Love, MacKinven
        "MacIosaig",            # MacIsaac, MacKessock
        "MacÌosaig",            # MacIsaac, MacKessock
        "MacLabhrainn",         # MacLaren, MacLaurin, Lawrie
        "MacLabhruinn",         # MacLaren, Laurie
        "MacLachlainn",         # MacLachlan, MacLauchlan
        "MacLagain",            # MacLagan
        "MacLamraich",          # Landsborough
        "MacLaomainn",          # Lamond, Lamont, MacLeman
        "MacLathagain",         # MacLagan
        "MacLeòid",             # Cloud, MacLeod
        "MacLeòir",             # MacClure, MacLure
        "MacLianain",           # MacLennan
        "MacLothaidh",          # Fullarton, Fulton, MacCloy
        "MacLiuthar",           # McLure
        "MacLughaidh",          # Fullarton, Fulton, MacClew, MacCloy, MacCluie, MacLoy
        "MacLuinge",            # MacClung, MacLung
        "MacLuirg",             # MacLurg
        "MacLulaich",           # MacCulloch, MacLullich
        "MacLùcaidh",           # MacLuckie
        "MacLùcais",            # Luke, MacDougall, MacLucas,MacLugash
        "MacMhaighstir",        # MacMaster
        "MacMhanachain",        # Monk
        "MacMhannain",          # MacVannan
        "MacMhaoilein",         # MacMillan
        "MacMhaoirn",           # Mearns
        "MacMhaolagain",        # MacMillan. Milligan, Milliken
        "MacMhaolain",          # MacMillan, MacMullen
        "MacMhaolBheatha",      # MacBean
        "MacMhaolChaluim",      # Callum, Malcolm
        "MacMhaolDòmhnaich",    # MacIldonich
        "MacMhaolÌosa",         # Mellis, Mellish, Melluish
        "MacMharais",           # MacVarish
        "MacMharcais",          # Marquis
        "MacMhata",             # Mathewson, Mathieson
        "MacMhatha",            # Matheson
        "MacMhathain",          # MacMann, Matheson
        "MacMhàrtainn",         # MacMartin, Martin
        "MacMhànais",           # Mains, Manson, MacManus, MacVanish
        "MacMhèinn",            # MacMinn, Menzies
        "MacMhiadhchain",       # MacMeeken, Meechan
        "MacMhìcheil",          # Carmichael, MacMichael
        "MacMhoirein",          # MacMorran, Morran, Morrison
        "MacMhòrdha",           # Mair, Moore, Muir
        "MacMhorgain",          # Morgan
        "MacMhuircheartaich",   # MacKirdy, MacMurray (but not Murray)
        "MacMhuirich",  # Currie,MacMurray, MacVurich, Murchison, Murdoch, Murray
        "MacMhunna",    # Munn
        "MacMhurardaich",# MacCurdy
        "MacMhurchaidh",# MacMurchie, MacMurchy, MacMurdo, MacMurray, Murchie, Murchison, Murdoch, MacMorrow, Morrow, Murphy
        "MacNaois",     # MacNeish, MacNish
        "MacNaomhain",  # MacNiven, Niven
        "MacNeacail",   # MacNicol Nicolson, Nicholson
        "MacNeachdain", # MacCracken, MacNaughton
        "MacNeis",      # MacNeish, MacNish
        "MacNèill",     # MacNeill, MacNeil, Nelson, Neilson
        "MacNia",       # MacNee, MacConie
        "MacNiallghais",# MacNeilage
        "MacNiallghuis",# MacNeilage
        "MacNìll",      # MacNeil, Neilson, Nelson
        "MacNiocail",   # MacKrycul, MacNichol, Nicolson
        "MacNobaill",   # Noble
        "MacPhaid",     # Faed, MacFeat, Peat
        "MacPhaidein",  # MacFadyen MacFadzean
        "MacPhail",     # MacFall, MacPhail, Quayle
        "MacPhàil",     # MacFall, MacPhail, Quayle
        "MacPhairce",   # Park
        "MacPhàdraig",  # Paterson, MacPhatrick
        "MacPhàic",     # MacKillop, Park
        "MacPhàidein",  # MacFadyen, MacFadzean
        "MacPhàil",     # MacFall, MacPhail, Quayle
        "MacPhàrlain",  # MacFarlane, MacPartland, MacPharlane
        "MacPheadair",  # MacFater, MacPhater, Paterson, Peters
        "MacPheadarain",# MacPhedran
        "MacPheadrais", # MacFetridge
        "MacPheidearain",# Fletcher, MacPhedran
        "MacPhilip",    # Mackillop, Philp
        "MacPhòil",     # Polson, MacPhail
        "MacRabaidh",   # Crabbie, MacRobbie
        "MacRaghnaill", # MacCrindle, MacRaild, Randall
        "MacRaibeirt",  # Corbett, MacRobert MacRobbie
        "MacRaoimhin",  # MacNiven
        "MacRaoiridh",  # MacCririe, MacRyrie, Ryrie
        "MacRaonaill",  # MacRanald, Ranaldson, Randall
        "MacRath",      # Cray, MacRae, Machray
        "MacRàild",     # MacRaild
        "MacRiada",     # MacCreadie
        "MacRiocaird",  # Crockett
        "MacRisnidh",   # MacRitchie, Ritchie, Dickson
        "MacRìdeinn",   # Bryden, MacBridan
        "MacRìgh",      # King, MacNee
        "MacRob",       # MacRobb
        "MacRobaidh",   # MacRobbie
        "MacRoibeirt",  # Corbett, MacRobert, MacRobbie, Robertson
        "MacRoithridh", # MacRyrie
        "MacRuairidh",  # MacRory, MacRury
        "MacRusachainn",# Kennedy
        "MacShanndaidh",# Andie, MacAndie
        "MacShealbhaigh",# MacKelvie
        "MacSheòrais",  # MacGeorge, Major
        "MacSheòrsa",   # Cuthbertson
        "MacShimidh",   # Jamieson, Lovat, MacKimmie, Sim, Simpson
        "MacShithich",  # Keith, Shaw, Shiach
        "MacShitrig",   # MacKettrick
        "MacShìm",      # MacKim, Simpson
        "MacShomhairle",# MacCurley, MacSorley
        "MacShuibhne",  # MacQueen, MacSween
        "MacSiridh",    # MacKinnon, MacSherry
        "MacSporain",   # MacSporran, Purser, Purcell
        "MacSuain",     # MacSwan, MacSween, Swanson
        "MacSual",      # Maxwell
        "MacThaidhg",   # MacCaig
        "MacTheàrlaich",# Charleson, MacKerlich
        "MacThom",      # MacComb, Thom
        "MacThomaidh",  # MacCombie
        "MacThorcadail",# MacCorkindale, MacCorquodale
        "MacThorcaill", # Corkhill, MacCorkill
        "MacThàmhais",  # MacTavish Tawse, Thomson
        "MacThòmais",   # Comish, Thomson
        "MacTiridh",    # MacKinnon
        "MacTuirc",     # MacTurk
        "MacUalraig",   # Kennedy, Ulrick
        "MacUaraig",    # Kennedy
        "MacUchtraigh", # MacAughtrie, Ochiltree, Coulthard
        "MacUilleim",   # MacWilliam, Quilliam, Wilson, Williamson
        "MacUirigh",    # Currie, MacVurich
        "MacUisdein",   # Hugston, Hutcheon, Hutcheson, MacCutcheon, MacHugh, MacHutcheon, Whiston
        "MacUrardaidh", # Mackirdy
        "MacUrardaigh", # MacKirdie
        "MacUrchadain", # Orchard, Orchardson
        "MacUrchaidh",  # MacMurchie
        "MacUsbaig",    # MacUsbaig
        "MacÙisdein",   # Hutcheon, Hutcheson, MacCutcheon, MacHugh, MacHutcheon, Whiston
        "Maoileanach",  # MacMillan
        "Maolanach",    # MacMillan
        "MaolIosa",     # Mellis
        "Matasan",      # Matheson
        "Mathanach",    # Matheson, Moannach
        "Matharnach",   # Matheson, Mathewson
        "Mawr",         # Maver, Mavor
        "Maor",         # Maver, Mavor
        "Moireach",     # Moray, Murray
        "Moireasdan",   # Morrison
        "Moireasdanach",# Morrison
        "Morgan",       # Morgan
        "Morganach",    # MacKay, Morgan
        "Munna",        # Munn
        "Màrnach",      # Marno, Marnoch
        "Màrr",         # Marr
        "Màrtainn",     # Martin
        "Mèinn",        # Menzies, Main
        "Mèinnearach",  # Menzies
        "Niocalsan",    # Nic(h)olson
        "O' Brolchain", # Bradley, Brodie, Brolochan
        "O' Cain",      # O' Kean
        "O' Luingeachain",# Laing, Lang, Loynachan
        "Padarsan",     # Paterson
        "Paorach",      # Power
        "Peadarsan",    # Paterson
        "Peucag",       # Peacock
        "Peutan",       # Beaton, Bethune
        "Preas",        # Birse
        "Puidreach",    # Buttar, Butter
        "Rathais",      # Rothes
        "Robasan",      # Robertson, Robson Robison
        "Robasdan",     # Robertson, Robson Robison
        "Roid",         # Reid
        "Roideach",     # Reid
        "Ros",          # Ross
        "Ròs",          # Rose
        "Rosach",       # Ross
        "Ròsach",       # Rose
        "Rothach",      # Munro
        "Ruadh",        # Reid, Roy
        "Ruiseal",      # Russell
        "Sailcirc",     # Selkirk
        "Salmond",      # Salmond
        "Seadh",        # Shaw
        "Seadhg",       # Shaw
        "Seagha",       # Shaw
        "Seaghach",     # Shaw
        "Seathanach",   # Shaw
        "Sgèin",        # Skene
        "Sginnearach",  # Skinner
        "Sgot",         # Scott
        "Singleir",     # Sinclair
        "Siosal",       # Chisholm
        "Siosalach",    # Chisholm
        "Smios",        # Smith
        "Stiùbhart",    # Stewart, Stuart
        "Stiùbhartach", # Stewart, Stuart
        "Sùdrach",      # Soutar
        "Sutharlainn",  # Sutherland
        "Sutharlan",    # Sutherland
        "Suthurlanach", # Sutherland
        "Tod",          # Todd
        "Todt",         # Todd
        "Talmhach",     # Tolmie
        "Tolmach",      # Tolmie
        "Tuairnear",    # Turner
        "Tàileach",     # Tallach
        "Tàillear",     # Taylor
        "Tulach",       # Tulloch, Tough
        "Ualas",        # Wallace
        "Umphraidh",    # Humphrey
        "Urchadainn",   # Urquhart
        "Urchardan"     # Urquhart
        )



def getMaleFirstName(Style=None):
    if Style in (None, "English", "Standard", "English_1", "Standard_1"):
        return random.choice(male_firstnames)
    elif Style in ("English_2", "Standard_2"):
        return random.choice(male_firstnames_2)
    elif Style == "Spanish":
        return random.choice(male_firstnames_Spanish)
    elif Style == "Italian":
        return random.choice(male_firstnames_Italian)
    elif Style == "French":
        return random.choice(male_firstnames_French)
    elif Style == "German":
        return random.choice(male_firstnames_German)
    elif Style == "Russian":
        return random.choice(male_firstnames_Russian)

    elif Style == "Korean":
        return random.choice(male_firstnames_Korean)

    elif Style == "Japanese":
        return random.choice(male_firstnames_Japanese)

    elif Style == "Indian":
        return random.choice(male_firstnames_Indian)

    elif Style == "Chinese":
        return random.choice(male_firstnames_Chinese)

    elif Style == "Scots_Gaelic":
        return random.choice(male_firstnames_Scots_Gaelic)

def getFemaleFirstName(Style=None):
    if Style in (None, "English", "Standard", "English_1", "Standard_1"):
        return random.choice(female_firstnames)
    elif Style in ("English_2", "Standard_2"):
        return random.choice(female_firstnames_2)
    elif Style == "Spanish":
        return random.choice(female_firstnames_Spanish)
    elif Style == "Italian":
        return random.choice(female_firstnames_Italian)
    elif Style == "French":
        return random.choice(female_firstnames_French)
    elif Style == "German":
        return random.choice(female_firstnames_German)
    elif Style == "Russian":
        return random.choice(female_firstnames_Russian)

    elif Style == "Japanese":
        return random.choice(female_firstnames_Japanese)

    elif Style == "Korean":
        return random.choice(female_firstnames_Korean)

    elif Style == "Indian":
        return random.choice(female_firstnames_Indian)

    elif Style == "Chinese":
        return random.choice(female_firstnames_Chinese)

    elif Style == "Scots_Gaelic":
        return random.choice(female_firstnames_Scots_Gaelic)

def getSurname(Style=None, UseLongName=0):
    if Style == "Random":
        Style=random.choice(("English", "Standard", "English_1", "Standard_1", "English_2", "Standard_2",
          "Spanish", "Italian", "French", "German", "Russian",
          "Chinese", "Japanese", "Korean", "Indian", 
          "Scots_Gaelic")) #update this when we add more styles
    if Style in (None, "English", "Standard", "English_1", "Standard_1"):
        return random.choice(surnames)
    elif Style in ("English_2", "Standard_2"):
        return random.choice(surnames_2)
    elif Style == "Spanish":
        if UseLongName==1:
            #long forms for characters & NPCs
            return random.choice((random.choice(surnames_Spanish_long),
                                 "%s y %s" % (random.choice(surnames_Spanish),random.choice(surnames_Spanish))))
        elif UseLongName==0:
            #short forms for planets etc
            return random.choice(surnames_Spanish)
        else:
            #could be either... mix it up a bit!
            return random.choice((random.choice(surnames_Spanish),
                                 random.choice(surnames_Spanish),
                                 random.choice(surnames_Spanish_long),
                                 "%s y %s" % (random.choice(surnames_Spanish),random.choice(surnames_Spanish))))
    elif Style == "Italian":
        return random.choice(surnames_Italian)
    elif Style == "French":
        return random.choice(surnames_French)
    elif Style == "German":
        return random.choice(surnames_German)
    elif Style == "Russian":
        return random.choice(surnames_Russian)

    elif Style == "Japanese":
        return random.choice(surnames_Japanese)

    elif Style == "Korean":
        return random.choice(surnames_Korean)

    elif Style == "Indian":
        return random.choice(surnames_Indian)

    elif Style == "Scots_Gaelic":
        return random.choice(surnames_Scots_Gaelic)

    elif Style == "Chinese":
        return random.choice(surnames_Chinese)

def getMaleName(Style=None, UseLongName=None):
    if Style == "Random":
        Style=random.choice(("English", "Standard", "English_1", "Standard_1", "English_2", "Standard_2",
          "Spanish", "Italian", "French", "German", "Russian",
          "Chinese", "Japanese", "Korean", "Indian", 
          "Scots_Gaelic")) #update this when we add more styles
    if Style in (None, "English", "Standard", "English_1", "Standard_1"):
        firstName   = random.choice(male_firstnames)
        surname     = random.choice(surnames)
        #some twiddles to prevent weird combinations...
        #like 'Graham Graham', 'John Johnson' or 'Dexter Brewster'
        while firstName[:1] == surname[:1]:
            surname = random.choice(surnames)
        while firstName[-2:] == surname[-2:]:
            surname = random.choice(surnames)
    elif Style in ("English_2", "Standard_2"):
        firstName   = random.choice(male_firstnames_2)
        surname     = random.choice(surnames_2)
        #some twiddles to prevent weird combinations...
        while firstName[:1] == surname[:1]:
            surname = random.choice(surnames_2)
        while firstName[-2:] == surname[-2:]:
            surname = random.choice(surnames_2)
    elif Style == "Spanish":
        if UseLongName == 1:
            firstName   = random.choice((getMaleFirstName("Spanish"),
                                    "%s %s" % (getMaleFirstName("Spanish"),getMaleFirstName("Spanish"))))
        else:
            firstName   = getMaleFirstName("Spanish")
        surname     = getSurname("Spanish", UseLongName)
        #some twiddles to prevent weird combinations...
        while firstName[:1] == surname[:1]:
            surname = getSurname("Spanish", UseLongName)
        while firstName[-2:] == surname[-2:]:
            surname = getSurname("Spanish", UseLongName)
    elif Style == "Italian":
        firstName   = random.choice(male_firstnames_Italian)
        surname     = random.choice(surnames_Italian)
        #some twiddles to prevent weird combinations...
        while firstName[:1] == surname[:1]:
            surname = random.choice(surnames_Italian)
        while firstName[-2:] == surname[-2:]:
            surname = random.choice(surnames_Italian)
    elif Style == "French":
        firstName   = random.choice(male_firstnames_French)
        surname     = random.choice(surnames_French)
        #some twiddles to prevent weird combinations...
        while firstName[:1] == surname[:1]:
            surname = random.choice(surnames_French)
        while firstName[-2:] == surname[-2:]:
            surname = random.choice(surnames_French)
    elif Style == "German":
        firstName   = random.choice(male_firstnames_German)
        surname     = random.choice(surnames_German)
        #some twiddles to prevent weird combinations...
        while firstName[:1] == surname[:1]:
            surname = random.choice(surnames_German)
        while firstName[-2:] == surname[-2:]:
            surname = random.choice(surnames_German)
    elif Style == "Russian":
        firstName   = random.choice(male_firstnames_Russian)
        surname     = random.choice(surnames_Russian)
        #some twiddles to prevent weird combinations...
        while firstName[:1] == surname[:1]:
            surname = random.choice(surnames_Russian)
        while firstName[-2:] == surname[-2:]:
            surname = random.choice(surnames_Russian)

    elif Style == "Japanese":
        firstName   = random.choice(male_firstnames_Japanese)
        surname     = random.choice(surnames_Japanese)
        #some twiddles to prevent weird combinations...
        while firstName[:1] == surname[:1]:
            surname = random.choice(surnames_Japanese)
        while firstName[-2:] == surname[-2:]:
            surname = random.choice(surnames_Japanese)

    elif Style == "Korean":
        firstName   = random.choice(male_firstnames_Korean)
        surname     = random.choice(surnames_Korean)
        #some twiddles to prevent weird combinations...
        while firstName[:1] == surname[:1]:
            surname = random.choice(surnames_Korean)
        while firstName[-2:] == surname[-2:]:
            surname = random.choice(surnames_Korean)

    elif Style == "Indian":
        firstName   = random.choice(male_firstnames_Indian)
        surname     = random.choice(surnames_Indian)
        #some twiddles to prevent weird combinations...
        while firstName[:1] == surname[:1]:
            surname = random.choice(surnames_Indian)
        while firstName[-2:] == surname[-2:]:
            surname = random.choice(surnames_Indian)

    elif Style == "Chinese":
        firstName   = random.choice(male_firstnames_Chinese)
        surname     = random.choice(surnames_Chinese)
        #some twiddles to prevent weird combinations...
        while firstName[:1] == surname[:1]:
            surname = random.choice(surnames_Chinese)
        while firstName[-2:] == surname[-2:]:
            surname = random.choice(surnames_Chinese)

    elif Style == "Scots_Gaelic":
        firstName   = random.choice(male_firstnames_Scots_Gaelic)
        surname     = random.choice(surnames_Scots_Gaelic)
        #some twiddles to prevent weird combinations...
        while firstName[:1] == surname[:1]:
            surname = random.choice(surnames_Scots_Gaelic)
        while firstName[-2:] == surname[-2:]:
            surname = random.choice(surnames_Scots_Gaelic)
    return "%s %s" % (firstName, surname)

def getFemaleName(Style=None, UseLongName=None):
    if Style == "Random":
        Style=random.choice(("English", "Standard", "English_1", "Standard_1", "English_2", "Standard_2",
          "Spanish", "Italian", "French", "German", "Russian",
          "Chinese", "Japanese", "Korean", "Indian", 
          "Scots_Gaelic")) #update this when we add more styles
    if Style in (None, "English", "Standard"):
        firstName   = random.choice(female_firstnames)
        surname     = random.choice(surnames)
        #some twiddles to prevent weird combinations
        while firstName[:1] == surname[:1]:
            surname = random.choice(surnames)
        while firstName[-2:] == surname[-2:]:
            surname = random.choice(surnames)
        return "%s %s" % (firstName, surname)
    elif Style in ("English_2", "Standard_2"):
        firstName   = random.choice(female_firstnames_2)
        surname     = random.choice(surnames_2)
        #some twiddles to prevent weird combinations...
        #like 'Graham Graham', 'John Johnson' or 'Dexter Brewster'
        while firstName[:1] == surname[:1]:
            surname = random.choice(surnames_2)
        while firstName[-2:] == surname[-2:]:
            surname = random.choice(surnames_2)
    elif Style == "Spanish":
        if UseLongName == 1:
            firstName   = random.choice((getFemaleFirstName("Spanish"),
                                    "%s %s" % (getFemaleFirstName("Spanish"),getFemaleFirstName("Spanish"))))
        else:
            firstName   = getFemaleFirstName("Spanish")
        surname     = getSurname("Spanish", UseLongName)
        #some twiddles to prevent weird combinations...
        while firstName[:1] == surname[:1]:
            surname = getSurname("Spanish", UseLongName)
        while firstName[-2:] == surname[-2:]:
            surname = getSurname("Spanish", UseLongName)
    elif Style == "Italian":
        firstName   = random.choice(female_firstnames_Italian)
        surname     = random.choice(surnames_Italian)
        #some twiddles to prevent weird combinations...
        while firstName[:1] == surname[:1]:
            surname = random.choice(surnames_Italian)
        while firstName[-2:] == surname[-2:]:
            surname = random.choice(surnames_Italian)
    elif Style == "French":
        firstName   = random.choice(female_firstnames_French)
        surname     = random.choice(surnames_French)
        #some twiddles to prevent weird combinations...
        while firstName[:1] == surname[:1]:
            surname = random.choice(surnames_French)
        while firstName[-2:] == surname[-2:]:
            surname = random.choice(surnames_French)
    elif Style == "German":
        firstName   = random.choice(female_firstnames_German)
        surname     = random.choice(surnames_German)
        #some twiddles to prevent weird combinations...
        while firstName[:1] == surname[:1]:
            surname = random.choice(surnames_German)
        while firstName[-2:] == surname[-2:]:
            surname = random.choice(surnames_German)
    elif Style == "Russian":
        firstName   = random.choice(female_firstnames_Russian)
        surname     = random.choice(surnames_Russian)
        #some twiddles to prevent weird combinations...
        while firstName[:1] == surname[:1]:
            surname = random.choice(surnames_Russian)
        while firstName[-2:] == surname[-2:]:
            surname = random.choice(surnames_Russian)

    elif Style == "Japanese":
        firstName   = random.choice(female_firstnames_Japanese)
        surname     = random.choice(surnames_Japanese)
        #some twiddles to prevent weird combinations...
        while firstName[:1] == surname[:1]:
            surname = random.choice(surnames_Japanese)
        while firstName[-2:] == surname[-2:]:
            surname = random.choice(surnames_Japanese)

    elif Style == "Korean":
        firstName   = random.choice(female_firstnames_Korean)
        surname     = random.choice(surnames_Korean)
        #some twiddles to prevent weird combinations...
        while firstName[:1] == surname[:1]:
            surname = random.choice(surnames_Korean)
        while firstName[-2:] == surname[-2:]:
            surname = random.choice(surnames_Korean)

    elif Style == "Chinese":
        firstName   = random.choice(female_firstnames_Chinese)
        surname     = random.choice(surnames_Chinese)
        #some twiddles to prevent weird combinations...
        while firstName[:1] == surname[:1]:
            surname = random.choice(surnames_Chinese)
        while firstName[-2:] == surname[-2:]:
            surname = random.choice(surnames_Chinese)

    elif Style == "Indian":
        firstName   = random.choice(female_firstnames_Indian)
        surname     = random.choice(surnames_Indian)
        #some twiddles to prevent weird combinations...
        while firstName[:1] == surname[:1]:
            surname = random.choice(surnames_Indian)
        while firstName[-2:] == surname[-2:]:
            surname = random.choice(surnames_Indian)

    elif Style == "Scots_Gaelic":
        firstName   = random.choice(female_firstnames_Scots_Gaelic)
        surname     = random.choice(surnames_Scots_Gaelic)
        #some twiddles to prevent weird combinations...
        #like 'Graham Graham', 'John Johnson' or 'Dexter Brewster'
        while firstName[:1] == surname[:1]:
            surname = random.choice(surnames_Scots_Gaelic)
        while firstName[-2:] == surname[-2:]:
            surname = random.choice(surnames_Scots_Gaelic)
    return "%s %s" % (firstName, surname)

def getName(Style=None, UseLongName=0):
    tempvar = random.choice((0,0,1,1,1))      # slightly weight it towards men 
    if tempvar == 1:
        name=getMaleName(Style, UseLongName)
    else:
        name=getFemaleName(Style, UseLongName)
    return(name)


def demo():

    print "%s (version: %s)" % (string.split(__file__,"\\")[-1], __VERSION__ )
    print
    print "male first names in 'male_firstnames'       :  ", len(male_firstnames)
    print "female first names in 'female_firstnames'   :  ", len(female_firstnames)
    print "surnames in 'surnames'                      :  ", len(surnames)
    print
    print "male first names in 'male_firstnames_2'     :  ", len(male_firstnames_2)
    print "female first names in 'female_firstnames_2' :  ", len(female_firstnames_2)
    print "surnames in 'surnames_2'                    :  ", len(surnames_2)
    print
    print "male first names in 'male_firstnames_Spanish'    :  ", len(male_firstnames_Spanish)
    print "female first names in 'female_firstnames_Spanish':  ", len(female_firstnames_Spanish)
    print "surnames in 'surnames_Spanish'                   :  ", len(surnames_Spanish)
    print "surnames in 'surnames_Spanish_long'              :  ", len(surnames_Spanish_long)
    print
    print "male first names in 'male_firstnames_Italian'     :  ", len(male_firstnames_Italian)
    print "female first names in 'female_firstnames_Italian' :  ", len(female_firstnames_Italian)
    print "surnames in 'surnames_Italian'                    :  ", len(surnames_Italian)
    print
    print "male first names in 'male_firstnames_French'     :  ", len(male_firstnames_French)
    print "female first names in 'female_firstnames_French' :  ", len(female_firstnames_French)
    print "surnames in 'surnames_French'                    :  ", len(surnames_French)
    print
    print "male first names in 'male_firstnames_German'     :  ", len(male_firstnames_German)
    print "female first names in 'female_firstnames_German' :  ", len(female_firstnames_German)
    print "surnames in 'surnames_German'                    :  ", len(surnames_German)
    print
    print "male first names in 'male_firstnames_Russian'     :  ", len(male_firstnames_Russian)
    print "female first names in 'female_firstnames_Russian' :  ", len(female_firstnames_Russian)
    print "surnames in 'surnames_Russian'                    :  ", len(surnames_Russian)
    print

    print "male first names in 'male_firstnames_Japanese'     :  ", len(male_firstnames_Japanese)
    print "female first names in 'female_firstnames_Japanese' :  ", len(female_firstnames_Japanese)
    print "surnames in 'surnames_Japanese'                    :  ", len(surnames_Japanese)
    print

    print "male first names in 'male_firstnames_Korean'     :  ", len(male_firstnames_Korean)
    print "female first names in 'female_firstnames_Korean' :  ", len(female_firstnames_Korean)
    print "surnames in 'surnames_Korean'                    :  ", len(surnames_Korean)
    print

    print "male first names in 'male_firstnames_Indian'     :  ", len(male_firstnames_Indian)
    print "female first names in 'female_firstnames_Indian' :  ", len(female_firstnames_Indian)
    print "surnames in 'surnames_Indian'                    :  ", len(surnames_Indian)
    print

    print "male first names in 'male_firstnames_Scots_Gaelic'    :  ", len(male_firstnames_Scots_Gaelic)
    print "female first names in 'female_firstnames_Scots_Gaelic':  ", len(female_firstnames_Scots_Gaelic)
    print "surnames in 'surnames_Scots_Gaelic'                   :  ", len(surnames_Scots_Gaelic)
    print

    print "male first names in 'male_firstnames_Chinese'     :  ", len(male_firstnames_Chinese)
    print "female first names in 'female_firstnames_Chinese' :  ", len(female_firstnames_Chinese)
    print "surnames in 'surnames_Chinese'                    :  ", len(surnames_Chinese)
    print



    print "contractions/nicknames in 'names_short'     :  ", len(names_short.keys())
    print
    print "getMaleFirstName:", getMaleFirstName()
    print "getFemaleFirstName:", getFemaleFirstName()
    print "getSurname:", getSurname()
    print "getMaleName:", getMaleName()
    print "getFemaleName:", getFemaleName()
    print "getName:", getName()
    print
    print "getMaleFirstName('Standard_2'):", getMaleFirstName('Standard_2')
    print "getFemaleFirstName('Standard_2'):", getFemaleFirstName('Standard_2')
    print "getSurname('Standard_2'):", getSurname('Standard_2')
    print "getMaleName('Standard_2'):", getMaleName('Standard_2')
    print "getFemaleName('Standard_2'):", getFemaleName('Standard_2')
    print "getName('Standard_2'):", getName('Standard_2')
    print
    print "getMaleFirstName('Spanish'):", getMaleFirstName('Spanish')
    print "getFemaleFirstName('Spanish'):", getFemaleFirstName('Spanish')
    print "getSurname('Spanish'):", getSurname('Spanish')
    print "getMaleName('Spanish'):", getMaleName('Spanish')
    print "getFemaleName('Spanish'):", getFemaleName('Spanish')
    print "getName('Spanish'):", getName('Spanish')
    print
    print "getSurname('Spanish', long):", getSurname('Spanish', 1)
    print "getMaleName('Spanish', long):", getMaleName('Spanish', 1)
    print "getFemaleName('Spanish', long):", getFemaleName('Spanish', 1)
    print "getName('Spanish', long):", getName('Spanish', 1)
    print
    print "getMaleFirstName('Italian'):", getMaleFirstName('Italian')
    print "getFemaleFirstName('Italian'):", getFemaleFirstName('Italian')
    print "getSurname('Italian'):", getSurname('Italian')
    print "getMaleName('Italian'):", getMaleName('Italian')
    print "getFemaleName('Italian'):", getFemaleName('Italian')
    print "getName('Italian'):", getName('Italian')
    print
    print "getMaleFirstName('French'):", getMaleFirstName('French')
    print "getFemaleFirstName('French'):", getFemaleFirstName('French')
    print "getSurname('French'):", getSurname('French')
    print "getMaleName('French'):", getMaleName('French')
    print "getFemaleName('French'):", getFemaleName('French')
    print "getName('French'):", getName('French')
    print
    print "getMaleFirstName('German'):", getMaleFirstName('German')
    print "getFemaleFirstName('German'):", getFemaleFirstName('German')
    print "getSurname('German'):", getSurname('German')
    print "getMaleName('German'):", getMaleName('German')
    print "getFemaleName('German'):", getFemaleName('German')
    print "getName('German'):", getName('German')
    print
    print "getMaleFirstName('Russian'):", getMaleFirstName('Russian')
    print "getFemaleFirstName('Russian'):", getFemaleFirstName('Russian')
    print "getSurname('Russian'):", getSurname('Russian')
    print "getMaleName('Russian'):", getMaleName('Russian')
    print "getFemaleName('Russian'):", getFemaleName('Russian')
    print "getName('Russian'):", getName('Russian')
    print

    print "getMaleFirstName('Japanese'):", getMaleFirstName('Japanese')
    print "getFemaleFirstName('Japanese'):", getFemaleFirstName('Japanese')
    print "getSurname('Japanese'):", getSurname('Japanese')
    print "getMaleName('Japanese'):", getMaleName('Japanese')
    print "getFemaleName('Japanese'):", getFemaleName('Japanese')
    print "getName('Japanese'):", getName('Japanese')
    print

    print "getMaleFirstName('Korean'):", getMaleFirstName('Korean')
    print "getFemaleFirstName('Korean'):", getFemaleFirstName('Korean')
    print "getSurname('Korean'):", getSurname('Korean')
    print "getMaleName('Korean'):", getMaleName('Korean')
    print "getFemaleName('Korean'):", getFemaleName('Korean')
    print "getName('Korean'):", getName('Korean')
    print

    print "getMaleFirstName('Chinese'):", getMaleFirstName('Chinese')
    print "getFemaleFirstName('Chinese'):", getFemaleFirstName('Chinese')
    print "getSurname('Chinese'):", getSurname('Chinese')
    print "getMaleName('Chinese'):", getMaleName('Chinese')
    print "getFemaleName('Chinese'):", getFemaleName('Chinese')
    print "getName('Chinese'):", getName('Chinese')
    print

    print "getMaleFirstName('Indian'):", getMaleFirstName('Indian')
    print "getFemaleFirstName('Indian'):", getFemaleFirstName('Indian')
    print "getSurname('Indian'):", getSurname('Indian')
    print "getMaleName('Indian'):", getMaleName('Indian')
    print "getFemaleName('Indian'):", getFemaleName('Indian')
    print "getName('Indian'):", getName('Indian')
    print
    print "getMaleFirstName('Scots_Gaelic'):", getMaleFirstName('Scots_Gaelic')
    print "getFemaleFirstName('Scots_Gaelic'):", getFemaleFirstName('Scots_Gaelic')
    print "getSurname('Scots_Gaelic'):", getSurname('Scots_Gaelic')
    print "getMaleName('Scots_Gaelic'):", getMaleName('Scots_Gaelic')
    print "getFemaleName('Scots_Gaelic'):", getFemaleName('Scots_Gaelic')
    print "getName('Scots_Gaelic'):", getName('Scots_Gaelic')


    print
    print


def test():
    demo()

if __name__ == "__main__":
    demo()

