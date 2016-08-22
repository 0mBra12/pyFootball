import click

def main(user, flag):
	global _user
	global _league
	_user = user
	_league = user.get_league()
	if flag:
		click.clear()
		print('%s Managerial office' % _user.get_team().get_name())
		print('-'.ljust(39,'-'))	
	nav = click.prompt('What would you like to do?', type=click.Choice(['help','inbox','schedule','squad','standings','personal', 'save', 'exit']))
	if nav == 'help':
		print('\nWhile in your office, you have a variety of resources available to you. You may:\n\n'
				'inbox      :  access any new mail you\'ve received, whether they be newsletters, injury news, player communications, or transfer offers\n'
				'schedule   :  take a look at upcoming games and past results of both your team and other teams in the league\n'
				'squad      :  check on how your players are doing, including their stats based on recent training sessions\n'
				'standings  :  see how your team ranks up on the table, along with other useful information and stats\n'
				'personal   :  see your own personal stats and information\n'
				'save       :  save your in-game progress\n'
				'exit       :  exit out of the game, although why would you do that?\n')
		main(_user, False)
	elif nav == 'exit':
		pass
	elif nav == 'inbox':
		inbox()
	elif nav == 'schedule':
		schedule()
	elif nav == 'squad':
		squad()
	elif nav == 'standings':
		standings()
	elif nav == 'personal':
		personal()
	elif nav == 'save':
		save()

def inbox():
	click.clear()


if __name__ == '__main__':
    main()