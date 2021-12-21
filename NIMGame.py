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
			if (jetons > 2) and ((jetons % 2) == 0):
				for i in range(1, int(jetons / 2)):
					act.append([jetons, i])
			elif (jetons > 2) and ((jetons % 2) != 0):
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
	def max_value(self, state):
		if NIMGame.isTerminal(state):
			return 0
		chance = -9999999999999
		for action in NIMGame.actions(state):
			chance = max(chance, NIMGame.min_value( NIMGame.result(state,action)))
		return chance
		
		
	@classmethod
	def min_value(self, state):
		if NIMGame.isTerminal(state):
			return 1
		chance = 9999999999999
		for action in NIMGame.actions(state):
			chance = min(chance , NIMGame.max_value( NIMGame.result(state,action)))
		return chance
	
	@classmethod
	def max_value_AlphaBeta(self, state,alpha,beta):
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
	def min_value_AlphaBeta(self, state,alpha,beta):
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
	player_name = input("Player's name :")
	print ("Hello", player_name,", Choose the initial value for the game:")
	firstPile = int(input("Must be greater than 3: "))
	pile=[firstPile]
	pileToDivise = 0
	firstNewPile = 0
	secondNewPile = 0
	chances =0
	alpha=-9999999999999
	beta=999999999999
	print ("Let's start the game,")
	r = random.randint(1,2)
	if r == 1:
		print ("You will be player Min")
	else:
		print ("You will be player Max ")
	print("Our initial pile will be : ", firstPile)
	
	if (r == 1):
		while True:
			print("it's Player Min turn : ", player_name)
			while((pileToDivise not in pile) or (pileToDivise < 3) ):
				pileToDivise = int(input("Choose a valid value to divise: "))
			pile.remove(pileToDivise)
			while ([pileToDivise, firstNewPile] not in NIMGame.actions([int(pileToDivise)])):
				firstNewPile = int(input("Please indicate the first value after division: "))
			while (pileToDivise != (firstNewPile + secondNewPile)):
				secondNewPile = int(input("Please indicate the second value after division: "))
			pile.append(firstNewPile)
			pile.append(secondNewPile)

			print("New pile : ", pile)
			if NIMGame.isTerminal(pile):
				print("Congrats, you are the winner ! ")
				break;

			print("It's Player Max turn ")
			acts = NIMGame.actions(pile)
			for act in acts:
				if NIMGame.max_value(act):
					chances = 1;
					pile = NIMGame.result(pile,act)
			if chances == 0:
				pile = NIMGame.result(pile,acts[0])
			print("New Pile : ", pile)
			if NIMGame.isTerminal(pile):
				print("Sorry, you lost ")
				break;

	else:
		while True:
			print("it's Player Max turn")
			acts = NIMGame.actions(pile)
			for act in acts:
				if NIMGame.max_value(act):
					chances = 1;
					pile = NIMGame.result(pile,act)
			if chances == 0:
				pile = NIMGame.result(pile,acts[0])
			print("New Pile : ", pile)
			if NIMGame.isTerminal(pile):
				print("Sorry, you lost")
				break;

			print("it's Player Min round : ", player_name)
			while((pileToDivise not in pile) or (pileToDivise < 3)):
				pileToDivise = int(input("Choose a valid value to divise: "))
			pile.remove(pileToDivise)
			while ([pileToDivise, firstNewPile] not in NIMGame.actions([int(pileToDivise)])):
				firstNewPile = int(input("Please indicate the first value after division: "))
			while (pileToDivise != (firstNewPile + secondNewPile)):
				secondNewPile = int(input("Please indicate the second value after division:  "))
			pile.append(firstNewPile)
			pile.append(secondNewPile)

			print("New pile : ", pile)
			if NIMGame.isTerminal(pile):
				print("Congrats, you are the winner !  ")
				break;
			