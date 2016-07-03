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
		#makes a list of all the teams I have in teams.txt and then randomly shuffles them

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
			#fills team_list with Team instances, giving the first item in the list lines and a random prestige, 
			#ensurely for a certain number of prestiges in a league
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
		self.gen_players()

	def gen_players(self):
		self.player_list = []
		names = [line.rstrip('\n') for line in open('../db/players.txt')]
		first_names = names[0].split('/')
		last_names = names[1].split('/')
		random.shuffle(first_names)
		random.shuffle(last_names)
		for n in range(16):
			full_name = first_names.pop() + ' ' + last_names.pop()
			self.player_list.append(Player(self, full_name))
		

		#TODO make player generation have a certain # of each position, and have balanced stats based on prestige

	def get_name(self):
		return self.name


class PlayerTeam(Team):
	def add_player_list(self, player_list):
		self.player_list = player_list

	def test(self):
		return 'hello'


class Player():
	def __init__(self, team, name):
		#TODO add position, rating, and other stats
		self.team = team
		self.name = name

	def get_name(self):
		return self.name

	def get_team(self):
		return self.team
