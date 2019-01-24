# coding: utf8

import random
import datetime

BASE = ["Quinoa", "Riz", "Lentilles Coraille", "Couscous", "Boulgour", "Nouilles Chinoises"]

VEGETABLES_DICT = {
	1 : {
	    "FRESH" : ["Endive", "Oignons", "Carotte", "Choux", "Pommes", "Tomates Sechees", "Pois chiches", "Pousses de Soja", "Mais", "Haricot Rouge", "Avocat", "Mozzarella", "Champignons"],
	    "HOT" : ["Poireau", "Patate", "Carotte", "Oignon", "Patate Douce", "Oeufs"]
	},
	2 : {
	    "FRESH" : ["Tomates Sechees", "Pois chiches", "Pousses de Soja", "Mais", "Haricot Rouge", "Mozzarella", "Champignons", "Oignons", "Carotte", "Pommes", "Endive", "Choux", "Mangue", "Avocat"],
	    "HOT" : ["Poireau", "Patate", "Carotte", "Oignon", "Patate Douce", "Oeufs"]
	},
	3 : {
	    "FRESH" : ["Tomates Sechees", "Pois chiches", "Pousses de Soja", "Mais", "Haricot Rouge", "Mozzarella", "Champignons", "Oignons", "Carotte", "Pommes", "Oignons Nouveaux", "Avocat", "Mangue"],
	    "HOT" : ["Poireau", "Patate", "Carotte", "Oignon", "Patate Douce", "Oeufs", "Oignons Nouveaux"]
	},
	4 : {
	    "FRESH" : ["Tomates Sechees", "Pois chiches", "Pousses de Soja", "Mais", "Haricot Rouge", "Mozzarella", "Champignons", "Oignons", "Carotte", "Pommes", "Ail", "Asperge blanche", "Radis", "Avocat", "Mangue"],
	    "HOT" : ["Poireau", "Patate", "Carotte", "Oignon", "Patate Douce", "Oeufs", "Oignons Nouveaux"]
	},
	5 : {
	    "FRESH" : ["Tomates Sechees", "Pois chiches", "Pousses de Soja", "Mais", "Haricot Rouge", "Mozzarella", "Champignons", "Oignons", "Carotte", "Pommes", "Epinards", "Concombre", "Aubergine", "Avocat"],
	    "HOT" : ["Poireau", "Patate", "Carotte", "Oignon", "Patate Douce", "Oeufs", "Oignons Nouveaux", "Epinards"]
	},
	6 : {
	    "FRESH" : ["Tomates Sechees", "Pois chiches", "Pousses de Soja", "Mais", "Haricot Rouge", "Mozzarella", "Champignons", "Oignons", "Carotte", "Pommes", "Ail", "Epinards", "Concombre", "Asperge", "Betterave", "Brocoli", "Poivrons", "Mangue", "Tomate", "Melon"],
	    "HOT" : ["Poireau", "Patate", "Carotte", "Oignon", "Patate Douce", "Oeufs", "Aubergine", "Courgette", "Epinards", "Artichaut", "Pois Mange Tout", "Poivrons"]
	},
	7 : {
	    "FRESH" : ["Tomates Sechees", "Pois chiches", "Pousses de Soja", "Mais", "Haricot Rouge", "Mozzarella", "Champignons", "Oignons", "Carotte", "Pommes","Ail", "Epinards", "Concombre", "Asperge", "Betterave", "Brocoli", "Poivrons", "Mangue", "Tomate", "Melon"],
	    "HOT" : ["Poireau", "Patate", "Carotte", "Oignon", "Patate Douce", "Oeufs", "Aubergine", "Courgette", "Epinards", "Artichaut", "Pois Mange Tout", "Poivrons"]
	},
	8 : {
	    "FRESH" : ["Tomates Sechees", "Pois chiches", "Pousses de Soja", "Mais", "Haricot Rouge", "Mozzarella", "Champignons", "Oignons", "Carotte", "Pommes","Ail", "Epinards", "Concombre", "Asperge", "Betterave", "Brocoli", "Poivrons", "Mangue", "Tomate", "Melon"],
	    "HOT" : ["Poireau", "Patate", "Carotte", "Oignon", "Patate Douce", "Oeufs", "Aubergine", "Courgette", "Epinards", "Artichaut", "Pois Mange Tout", "Poivrons"]
	},
	9 : {
	    "FRESH" : ["Tomates Sechees", "Pois chiches", "Pousses de Soja", "Mais", "Haricot Rouge", "Mozzarella", "Champignons", "Oignons", "Carotte", "Pommes","Ail", "Epinards", "Concombre", "Asperge", "Betterave", "Brocoli", "Poivrons", "Tomate", "Melon", "Raisin", "Figue"],
	    "HOT" : ["Poireau", "Patate", "Carotte", "Oignon", "Patate Douce", "Oeufs", "Aubergine", "Courgette", "Epinards", "Artichaut", "Poivrons", "Poireau"]
	},
	10 : {
	    "FRESH" : ["Tomates Sechees", "Pois chiches", "Pousses de Soja", "Mais", "Haricot Rouge", "Mozzarella", "Champignons", "Oignons", "Carotte", "Pommes", "Epinards", "Betterave", "Brocoli", "Poivrons", "Raisin", "Figue", "Avocat"],
	    "HOT" : ["Poireau", "Patate", "Carotte", "Oignon", "Patate Douce", "Oeufs", "Epinards", "Poivrons", "Poireau", "Potimaron"]
	},
	11 : {
	    "FRESH" : ["Tomates Sechees", "Pois chiches", "Pousses de Soja", "Mais", "Haricot Rouge", "Mozzarella", "Champignons", "Oignons", "Carotte", "Pommes", "Epinards", "Avocat", "Choux"],
	    "HOT" : ["Poireau", "Patate", "Carotte", "Oignon", "Patate Douce", "Oeufs", "Epinards", "Poireau", "Potimaron", "Choux"]
	},
	12 : {
	    "FRESH" : ["Tomates Sechees", "Pois chiches", "Pousses de Soja", "Mais", "Haricot Rouge", "Mozzarella", "Champignons", "Oignons", "Carotte", "Pommes", "Avocat", "Choux"],
	    "HOT" : ["Poireau", "Patate", "Carotte", "Oignon", "Patate Douce", "Oeufs", "Poireau", "Potimaron", "Choux"]
	},
}
now = datetime.datetime.now()
print "BASE : \n"
random_base = random.choice(BASE)
print "- " + random_base
list_of_random_fresh_vegies = random.sample(VEGETABLES_DICT[now.month]["FRESH"], 4)
print "\n\n\n FRESH VEGIES :  \n"
for vegie in list_of_random_fresh_vegies:
	print "- " + vegie
print "\n\n\n HOT VEGIES : \n"
list_of_random_hot_vegies = random.sample(VEGETABLES_DICT[now.month]["HOT"], 2)
for vegie in list_of_random_hot_vegies:
	print "- " + vegie

print "\n\n\nYUUUUUM !"	

raw_input("Press Enter to exit...")