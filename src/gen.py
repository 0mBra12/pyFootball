import os, random


class Manager():
	#TODO add manager stats and things
	def __init__(self, name):
		self.name = name

	def get_name(self):
		return self.name
		

class League():
	def __init__(self):
		#txt_path = os.getcwd() + '\db\teams.txt'
		self.team_list = []
		lines = [line.rstrip('\n') for line in open('../db/teams.txt')]
		random.shuffle(lines)

		for n in range(10):
			if n < 2:
				prestige = 0
			elif n < 5:
				prestige = 1
			elif n < 8:
				prestige = 2
			elif n < 10:
				prestige = 3
			self.team_list.append(Team(lines.pop(), prestige))
			random.shuffle(self.team_list)


		self.games_played = 0

	def game_played(self):
		if self.games_played < 18:
			self.games_played += 1
		else:
			#TODO end the season
			self.games_played = 0



class Team():
	def __init__(self, name, prestige):
		self.name = name
		self.prestige = prestige
		if self.prestige == 0:
			wealth = random.randint(1000000,2500000)
		elif self.prestige == 1:
			wealth = random.randint(2500001,5000000)
		elif self.prestige == 2:
			wealth = random.randint(5000001,7500000)
		elif self.prestige == 3:
			wealth = random.randint(7500001,10000000)
		self.wealth = wealth	
		self.stadium = self.name + ' Stadium'
		gen_players()

	def gen_players(self):
		self.player_list = []
		lines = [line.rstrip('\n') for line in open('../db/players.txt')]
		random.shuffle(lines)
		#TODO finish the player generation, and create a player class

	def get_name(self):
		return self.name

class PlayerTeam(Team):
	def add_player_list(self, player_list):
		self.player_list = player_list

