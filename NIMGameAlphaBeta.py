import random

class NIMGame():

	@classmethod
	def isTerminal(self, pile):
		if len(pile) == 0:
			return 0
		for jeton in pile:
			if jeton > 2:
				return 0
		return 1


	@classmethod
	def actions(self,state):
		act = []

		for jetons in state:
			if (jetons > 2) & ((jetons % 2) == 0):
				for i in range(1, int(jetons / 2)):
					act.append([jetons, i])
			elif (jetons > 2) & ((jetons % 2) != 0):
				for i in range(1, int(jetons / 2 + 1)):
					act.append([jetons, i])
				
		return act

	@classmethod
	def result(self, state, action):
		newState = state[:]
		newState.remove(action[0])
		newState.append(action[1])
		newState.append(action[0] - action[1])
		return newState

	@classmethod
	def max_value(self, state,alpha,beta):
		if NIMGame.isTerminal(state):
			return 0
		chance = -9999999999999
		for action in NIMGame.actions(state):
			chance = max(chance, NIMGame.min_value( NIMGame.result(state,action),alpha,beta))
			if chance >= beta:
				return chance
			alpha=max(alpha,chance)
		return chance
		
		
	@classmethod
	def min_value(self, state,alpha,beta):
		if NIMGame.isTerminal(state):
			return 1
		chance = 9999999999999
		for action in NIMGame.actions(state):
			chance = min(chance , NIMGame.max_value( NIMGame.result(state,action),alpha,beta))
			if chance <= alpha:
				return chance
				
			beta=min(beta,chance)
		return chance
		
		
			
if __name__ == "__main__":
	player_name = input("Tell me your name: ")
	print ("Hello", player_name,", Please choose the first pile to be played with")
	firstPile = int(input("Between 3 and 100: "))
	pile=[firstPile]
	pileToDivise = 0
	firstNewPile = 0
	secondNewPile = 0
	chances =0
	alpha=-9999999999999
	beta=999999999999
	print ("Great,")
	r = random.randint(1,2)
	if r == 1:
		print ("You will be player Min and you will start the game")
	else:
		print ("You will be player Max and you will start the game")
	print("Our initial pile will be : ", firstPile)
	print("Lets start :")
	if (r == 1):
		while True:
			print("it's Player Min round, you  ", player_name)
			while((pileToDivise not in pile) | (pileToDivise < 3) ):
				pileToDivise = int(input("Please enter a valid pile, that you want to divise: "))
			pile.remove(pileToDivise)
			while ([pileToDivise, firstNewPile] not in NIMGame.actions([int(pileToDivise)])):
				firstNewPile = int(input("Please enter the first new pile after division: "))
			while (pileToDivise != (firstNewPile + secondNewPile)):
				secondNewPile = int(input("Please enter the second pile after division: "))
			pile.append(firstNewPile)
			pile.append(secondNewPile)

			print("New pile : ", pile)
			if NIMGame.isTerminal(pile):
				print("YOU ARE THE WINNER!!! ")
				break;

			print("it's Player Max round ")
			acts = NIMGame.actions(pile)
			for act in acts:
				if NIMGame.max_value(act,alpha,beta):
					chances = 1;
					pile = NIMGame.result(pile,act)
			if chances == 0:
				pile = NIMGame.result(pile,acts[0])
			print("New Pile : ", pile)
			if NIMGame.isTerminal(pile):
				print("YOU LOST ")
				break;

	else:
		while True:
			print("it's Player Max round ")
			acts = NIMGame.actions(pile)
			for act in acts:
				if NIMGame.max_value(act,alpha,beta):
					chances = 1;
					pile = NIMGame.result(pile,act)
			if chances == 0:
				pile = NIMGame.result(pile,acts[0])
			print("New Pile : ", pile)
			if NIMGame.isTerminal(pile):
				print("YOU LOST")
				break;

			print("it's Player Min round, you  ", player_name)
			while((pileToDivise not in pile) | (pileToDivise < 3)):
				pileToDivise = int(input("Please enter a valid pile, that you want to divise: "))
			pile.remove(pileToDivise)
			while ([pileToDivise, firstNewPile] not in NIMGame.actions([int(pileToDivise)])):
				firstNewPile = int(input("Please enter the first new pile after division: "))
			while (pileToDivise != (firstNewPile + secondNewPile)):
				secondNewPile = int(input("Please enter the second pile after division: "))
			pile.append(firstNewPile)
			pile.append(secondNewPile)

			print("New pile : ", pile)
			if NIMGame.isTerminal(pile):
				print("YOU ARE THE WINNER!!! ")
				break;
			