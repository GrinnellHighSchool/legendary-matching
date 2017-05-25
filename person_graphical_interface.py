from graphics import *

import random

def Match():
	name_list_girl = ["Sophia", "Emma", "Olivia", "Ava", "Mia", "Isabella", "Riley", "Aria",
					"Zoe", "Charlotte", "Lily", "Layla", "Amelia", "Emily", "Madelyn", "Aubrey",
					"Adalyn", "Madison", "Chloe", "Harper", "Abigail", "Aaliyah", "Avery",
					"Evelyn", "Kaylee", "Ella", "Ellie", "Scarlett", "Arianna", "Hailey",
					"Nora", "Addison", "Brooklyn", "Hannah", "Mila", "Leah", "Elizabeth",
					"Sarah", "Eliana", "Mackenzie", "Peyton", "Maria", "Grace", "Adeline",
					"Elena", "Anna", "Victoria", "Camilla", "Lillian", "Natalie"]

	name_list_boy = ["Jackson", "Aiden", "Lucas", "Liam", "Noah", "Ethan", "Mason", "Caden",
					"Oliver", "Elijah", "Grayson", "Jacob", "Michael", "Benjamin", "Carter",
					"James", "Jayden", "Logan", "Alexander", "Caleb", "Ryan", "Luke", "Daniel",
					"Jack", "William", "Owen", "Gabriel", "Matthew", "Connor", "Jayce", "Isaac",
					"Sebastian", "Henry", "Muhammad", "Cameron", "Wyatt", "Dylan", "Nathan",
					"Nicholas", "Julian", "Eli", "Levi", "Isaiah", "Landon", "David", "Christian",
					"Andrew", "Brayden", "John", "Lincoln"]

	amount_of_people = int(input("Amount: "))

	girl_dictionary = {}
	boy_dictionary = {}

	ranking_girl = []
	ranking_boy = []
	
	girl_names = random.sample(name_list_girl, amount_of_people)
	ranking_boy = random.sample(name_list_boy, amount_of_people)
	for girl in girl_names:
		shuffled_boy_list = [str(w) for w in random.sample(ranking_boy, len(ranking_boy))]
		girl_dictionary.update({(girl): shuffled_boy_list})

	boy_names = random.sample(name_list_boy, amount_of_people)
	ranking_girl = random.sample(name_list_girl, amount_of_people)
	for boy in boy_names:
		shuffled_girl_list = [str(w) for w in random.sample(ranking_girl, len(ranking_girl))]
		boy_dictionary.update({(boy): shuffled_girl_list})
	return(girl_dictionary,boy_dictionary)

girls,boys = Match()

girlsKeys = list(girls.keys())
boysKeys = list(boys.keys())

girlsList = []
boysList = []

def drawer(personList):
	for x in range(len(personList)):
		for y in range(len(personList[x])):
			personList[x][y].draw(screen)

spacing = 15
screen = GraphWin("My Circle", 50*(len(girlsKeys)+1), len(girlsKeys)*2.5*spacing,autoflush=False)
offsety = 7
offsetx = 25
offSetOfBoys = len(girlsKeys)*15+30

def maker(passedList,passedKeys,kind,typeOffset = 0):
	for type in range(len(passedKeys)):
		passedList.append([])
		passedList[type] = [Text(Point(0+offsetx,(type*spacing)+offsety+typeOffset),passedKeys[type])]
		for item in range(len(kind[passedKeys[type]])):
			passedList[type].append(Text(Point((item*50)+50+offsetx,(type*spacing)+offsety+typeOffset),kind[passedKeys[type]][item]))

maker(girlsList,girlsKeys,girls)
maker(boysList,boysKeys,boys,offSetOfBoys)

"""for girl in range(len(girlsKeys)):
	girlsList.append([])
	girlsList[girl] = [Text(Point(0+offsetx,(girl*spacing)+offsety),girlsKeys[girl])]
	for item in range(len(girls[girlsKeys[girl]])):
		girlsList[girl].append(Text(Point((item*50)+50+offsetx,(girl*spacing)+offsety),girls[girlsKeys[girl]][item]))


for boy in range(len(boysKeys)):
	item = Text(Point(0+offsetx,(boy*spacing)+offsety+spacing*1.5*len(boysKeys)),boysKeys[boy])
	item.draw(screen)"""

drawer(girlsList)
drawer(boysList)

update()
screen.getMouse()