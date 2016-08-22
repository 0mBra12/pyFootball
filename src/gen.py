import os, random


class Manager():
	#TODO add manager stats and things
	def __init__(self, name):
		self.name = name
		self.league = League()

	def get_name(self):
		return self.name

	def get_league(self):
		return self.league

	def set_team(self,my_team):
		self.team = my_team

	def get_team(self):
		return self.team

		

class League():
	def __init__(self):
		#txt_path = os.getcwd() + '\db\teams.txt'
		self.team_list = []
		lines = [line.rstrip('\n') for line in open('db/teams.txt')]
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


		self.matchday = 0

	def matchday_inc(self):
		if self.matchday < 18:
			self.matchday += 1
		else:
			#TODO end the season
			self.matchday = 0

	def get_team_list(self):
		return self.team_list



class Team():
	def __init__(self, name, prestige):
		#todo set_passCap
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
		self.set_xperf()


	def gen_players(self):
		self.player_list = []
		names = [line.rstrip('\n') for line in open('db/players.txt')]
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

	def set_xperf(self):
		xDP_list = []
		xMP_list = []
		xAP_list = []
		for player in self.player_list:
			if player.get_position() == 'Goalkeeper':
				xDP_list.append(player.get_PPR())
			elif player.get_position() == 'Defender':
				xDP_list.append(player.get_PPR())
			elif player.get_position() == 'Midfielder':
				xMP_list.append(player.get_PPR())
			elif player.get_position() == 'Attacker':
				xAP_list.append(player.get_PPR())
		self.xDP = int(sum(xDP_list) / len(xDP_list))
		self.xMP = int(sum(xMP_list) / len(xMP_list))
		self.xAP = int(sum(xAP_list) / len(xAP_list))

	def get_xperf(self, perf):
		if perf == 'xDP':
			return self.xDP
		elif perf == 'xMP':
			return self.xMP
		elif perf == 'xAP':
			return self.xAP
		
	def get_name(self):
		return self.name

	def get_prestige(self):
		return self.prestige


class PlayerTeam(Team):
	def add_player_list(self, player_list):
		self.player_list = player_list
	def get_player_list(self):
		return self.player_list


class Player():
	def __init__(self, team, name, position):
		#TODO add transfer value,
		self.team = team
		self.name = name
		self.position = position
		self.set_PPR()
		self.set_hidden_stats()
		self.phys = 0

	def get_name(self, firstlast):
		if firstlast == 'f':
			return self.name.split()[0]
		elif firstlast == 'l':
			return self.name.split()[1]
		elif firstlast == 'fl':
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

	def set_physicals(self):
		if self.position == 0:
			#heights are given in inches, weights in lbs
			#weights are calculated by randomly generating a height based on the heights certain professional players in real life and the position being played, then generating
			#a random BMI between a certain range and finding the height that corresponds with the generated BMI and height
			#phys could be: if height < thresh, speed bonus. if weight < thresh, nimble bonus. if height > thresh, aerial bonus. if weight > thresh, strength bonus.
			#bonus could be added to PPR during random matches
			self.height = random.randint(73,79)
			self.weight = int(24*self.height*self.height/703) # based on neuer, szczesny, courtouis, buffon, de gea, and casillas
		elif self.position == 1:
			self.height = random.randint(71,76)
			self.weight = int(random.randint(21,24)*self.height*self.height/703) # based on boateng, koscielny, kompany, mertesacker, benatia, and hummels
		elif self.position == 2:
			self.height = random.randint(66,73)
			self.weight = int(random.randint(22,24)*self.height*self.height/703) # based on cazorla, iniesta, xhaka, coquellin, rakitic, and modric
		elif self.position == 3:
			self.height = random.randint(67,76)
			self.weight = int(random.randint(23,25)*self.height*self.height/703) # based on ronaldo, peter crouch, bale, messi, and giroud

		if self.height < 68: # 'Cazorla' Bonus
			self.phys += 1
		if self.weight < 150: # 'Walcott' Bonus
			self.phys +=1
		if self.height > 75: # 'Giroud' Bonus
			self.phys +=1
		if self.weight > 195: # 'Akinfenwa' Bonus
			self.phys += 1


	def set_PPR(self):
		team_prestige = self.team.get_prestige()
		#based on team prestige give each player a PPR, with a % chance based on PPR that the player is very good/amazing
		#PPR stands for Potential Performance Rating and signifies their near maximum capable level of performance
		rand_val = random.randint(1,100)
		if team_prestige == 0: # 80% 50-59, 15% chance 60-69, 5% chance 70-79, 0% chance 80-89, 0% chance 90-100
			if rand_val <= 80:
				self.PPR = random.randint(50,59)
			elif rand_val <= 95:
				self.PPR = random.randint(60,69)
			elif rand_val <= 100:
				self.PPR = random.randint(70,79)
		elif team_prestige == 1: # 80% chance 60-69, 15% 50-59, 4% chance 70-79, 1% chance 80-89, 0% chance 90-100
			if rand_val <= 80:
				self.PPR = random.randint(60,69)
			elif rand_val <= 95:
				self.PPR = random.randint(50,59)
			elif rand_val <= 99:
				self.PPR = random.randint(70,79)
			elif rand_val <= 100:
				self.PPR = random.randint(80,89)
		elif team_prestige == 2: # 84% chance 70-79, 10% chance 60-69, 3% chance 50-59, 2% chance 80-89, 1% chance 90-100
			if rand_val <= 84:
				self.PPR = random.randint(70,79)
			elif rand_val <= 94:
				self.PPR = random.randint(60,69)
			elif rand_val <= 97:
				self.PPR = random.randint(50,59)
			elif rand_val <= 99:
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

	def set_hidden_stats(self):
		self.consistency = random.randint(0,9)
		self.loyalty = random.randint(0,9)
		self.inj_prone = random.randint(0,9)

	def get_gameday_perf(self):
		#todo make a game performance rating based on consistency, ppr, and physicality bonuses
		pass
		