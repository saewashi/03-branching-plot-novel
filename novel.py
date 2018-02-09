#!/usr/bin/python3

import sys

#!/usr/bin/python3
'''


caveat emptor: This was code we wrote together in class; it is definitely not working. There will be syntax and other logic errors.
Use at your own risk



'''




def show_location(current_location):
	''' Displays the description, displays a list of options, accepts and returns user input '''
	description = current_location["description"]
	options = current_location["options"]
	results = current_location["results"]
	print(description)
	count = 1
	for o in options:
		print('[' + str(count) + '] ' + o)
		count = count + 1
	print('[q] to quit')
	choice = input("What do you choose? ")
	if choice.lower() == 'q':
		return "quit"
	new_location = results[int(choice)-1]
	return new_location




world = {
	"start":{
		"description":"You are in a Diner with Goofball Raddy and Acer Rock."
		,"options":["You can stay & eat","You can leave and starve","Stare blindlessly at the food."]
		,"results":["eat","leave","stare"]
	}



        ,"leave":{
		"description":"You decided to leave, but you have no food."
		" Acer and Raddy die of starvation. . .Way to go!"
                ,"options":["You have no options. You must quit."]
                ,"results":["q"]
	}

        ,"stare":{
		"description":"You decided just stare at the food. "
		" Acer and Raddy gaze into the window, stare blindlessly at the food, while their stomaches eat themselves."
                ,"options":["You have no options. You must quit."]
                ,"results":["q"]
	}


	,"eat":{
		"description":"You decided to stay and eat!"
                " Goofball Raddy and Acer decide to order fries."

                " Goofball Raddy wants ketchup,"
                " but Acer isn't sure if he should have it."
                 ,"options":["You give Raddy the ketchup","Don't give the ketchup","Don't do anything"]
	         ,"results":["Give","Don't give","Nothing"]
	}

        ,"Don't give":{
		"description":"You decided to not give Raddy the ketchup."
                "Raddy decides to steal the ketchup from the kitchen, "

                " but the diner calls the police and he is arrested."
                " Acer does nothing, and continues to eat fries."
                 ,"options":["You have no more options. Unless you want to visit Raddy in jail. . ."]
	         ,"results":["q"]
	}


       ,"Nothing":{
		"description":"You decided to do nothing."
                "Raddy decides to just stare at you, "

                " because he does not understand why you didn't offer any ketchup to him."
                " In revenge,  Raddy steals your fries and the ketchup, but ends up going to jail."
                 ,"options":["You have no more options. Unless you want to order more fries. . ."]
	         ,"results":["q"]
	}


        ,"Give":{
                "description":"You gave Raddy the ketchup!"
                " Goofball Raddy: 'These are some great fries! *Squarts ketchup all over face* '"
                " Oops. . .*Uses frie to wipe ketchup off of face.* "
                " Acer: 'Raddy, that's disguisting! Why would you do that? '"
                " Goofball Raddy: 'Because. . .I'M GOOFBALL RADDY FOR YA! ;D'"
                " Acer is annoyed. What do you do?"
                ,"options":["Slap him.","Squart more ketchup.","Walk away."]
		,"results":["Slap","Squart","Walk away"]

                }


        ,"Walk away":{
                "description":"You decided to walk away"
                " Goofball Raddy: Why are you leaving? "
                " Acer? Come back! AAAACCCCEEEEERRRR! D: "
                " * Acer walks out of the diner, into the abyss, and never returns.* "
                " * Goofball Raddy just watches, while eating fries."
                ,"options":["You have no more options!"]
		,"results":["q"]

                }


        ,"Squart":{
                "description":"You decided to squart Raddy with the ketchup!"
                " Goofball Raddy: MMM! more ketchup! * Raddy proceeds to eat the ketchup off his face.* "
                " Acer: D: . . .WHY ARE YOU LIKE THIS?! "
                " Goofball Raddy: It's called being yourself! ^_^ "
                " Acer: No, it's called you need psychological help."
                " Raddy: No, it's called you need to shut up!"
                " Acer: Who are you telling to shut up? "
                " Raddy: Oh, I'm sorry. Let me make it more clear. *Cough* YOOOOOOOOOOOUUUUUUU!"
                " * Acer and Raddy get into a physcial altercation, and both go to jail.* "
                ,"options":["You have no more options!"]
		,"results":["q"]

                }

        ,"Slap":{
                "description":"You slapped Raddy Ouch!"
                " Goofball Raddy:  Hey! Why'd you do that? "
                " Acer: 'Because you're stupid. '"
                " Goofball Raddy: You're mean. ;-; "
                "Now Raddy is crying!"
                ,"options":["Slap him again.","Hug him.","Buy him ice cream."]
		,"results":["Slap","Squart","Walk away"]



}}

current = "start"

while current != "quit":
        current = show_location(world[current])
