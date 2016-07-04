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
			# 16 players: 2 goalkeepers, 5 Defenders, 5 Midfielders, 4 Attackers
			# position where (0 : goalie, 1 : def, 2 : mid, 3 : att)
			if n < 2:
				position = 0
			elif n < 7:
				position = 1
			elif n < 12:
				position = 2
			else:
				position = 3
			full_name = first_names.pop() + ' ' + last_names.pop()
			self.player_list.append(Player(self, full_name, position))
		

		#TODO make player generation have a certain # of each position, and have balanced stats based on prestige

	def get_name(self):
		return self.name

	def get_prestige(self):
		return self.prestige


class PlayerTeam(Team):
	def add_player_list(self, player_list):
		self.player_list = player_list


class Player():
	def __init__(self, team, name, position):
		#TODO add position, rating, and other stats
		self.team = team
		self.name = name
		self.position = position
		self.set_PPR()

	def get_name(self):
		return self.name

	def get_team(self):
		return self.team

	def get_position(self):
		if self.position == 0:
			return 'Goalkeeper'
		elif self.position == 1:
			return 'Defender'
		elif self.position == 2:
			return 'Midfielder'
		elif self.position == 3:
			return 'Attacker'

	def set_PPR(self):
		team_prestige = self.team.get_prestige()
		self.PPR_INIT_SET = True
		#TODO based on team prestige give each player a PPR, with a % chance based on PPR that the player is very good/amazing
		#PPR stands for Potential Performance Rating and signifies their near maximum capable level of performance
		rand_val = random.randint(1,100)
		if team_prestige == 0: # 80% 50-59, 14% chance 60-69, 3% chance 70-79, 2% chance 80-89, 1% chance 90-100
			if rand_val <= 80:
				self.PPR = random.randint(50,59)
			elif rand_val <= 94:
				self.PPR = random.randint(60,69)
			elif rand_val <= 97:
				self.PPR = random.randint(70,79)
			elif rand_val <= 99:
				self.PPR = random.randint(80,89)
			elif rand_val == 100:
				self.PPR = random.randint(90,100)
		elif team_prestige == 1: # 70% chance 60-69, 24% 50-59, 3% chance 70-79, 2% chance 80-89, 1% chance 90-100
			if rand_val <= 70:
				self.PPR = random.randint(60,69)
			elif rand_val <= 94:
				self.PPR = random.randint(50,59)
			elif rand_val <= 97:
				self.PPR = random.randint(70,79)
			elif rand_val <= 99:
				self.PPR = random.randint(80,89)
			elif rand_val == 100:
				self.PPR = random.randint(90,100)
		elif team_prestige == 2: # 61% chance 70-79, 20% chance 60-69, 10% chance 50-59, 5% chance 80-89, 4% chance 90-100
			if rand_val <= 61:
				self.PPR = random.randint(70,79)
			elif rand_val <= 81:
				self.PPR = random.randint(60,69)
			elif rand_val <= 91:
				self.PPR = random.randint(50,59)
			elif rand_val <= 96:
				self.PPR = random.randint(80,89)
			elif rand_val <= 100:
				self.PPR = random.randint(90,100)
		elif team_prestige == 3: # 80% chance 80-89, 10% chance 90-100, 10% chance 70-79
			if rand_val <= 80:
				self.PPR = random.randint(80,89)
			elif rand_val <= 90:
				self.PPR = random.randint(90,100)
			elif rand_val <= 100:
				self.PPR = random.randint(70,79)

	def get_PPR(self):
		return self.PPR

