# Name: Cody Durflinger
#	Prog Purpose: This Magic 8-ball code uses a Python tuple sine the 
#	user does not have the ability to change the 8-ball answers.
#	However, the program could have used a Python list instead of a tuple.
#	NOTE: Tuple use parenthese; list use square brackets.

import random
answers_8_ball = ("As I see it, yes", "Ask again later", 
	"Better not tell you now", "Cannot predict now",
	"Concentrate and ask again", "Don't count on it",
	"It is certain", "It is decidely so",
	"Most likely", "My reply is no",
	"my sources say no", "Outlook good",
	"Outlook is not so good", "Reply hazy try again",
	"Signs point to yes", "Very doubtful",
	"Without a doubt", "Yes","Yes definitely",
	"You may rely on it")

def main():

	print (" I am the Magic-8-Ball and can answer any YES or NO question!")

	another_question = True
	while another_question:
		answer = random.choice (answers_8_ball)

		print("\nShake the Magic-8-Ball")
		print ("...and no...")
		question = input("\nWhat is your YES or NO question?")
		print("The Magic-8-Ball says: + answer")

		askAgain = input("\nWould you like to ask me another question (Y or N)?:")
		if askAgain.upper() == "N" or askAgain == "n":
			another_question = False

	print("\nCome back again wher you have other important question.")
	print("...Magic-8-Ball OUT.")

main()
	
