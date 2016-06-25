import gen

def main():
    print('Hello and welcome to pyFootball! Would you like to: ')
    print('1) Start a new game')
    print('2) Load a saved game')
    while True:
        start_option = input('> ')
        if start_option == '1':
            new_game()
            break
        elif start_option == '2':
            load_game()
            break
        else:
            print('Sorry, you have to either press 1 to start a new game, or press 2 to load a saved game.')


def new_game():
    global player
    global league

    while True:
        print('Congratulations on becoming a manager! What is your name?')
        name = input('> ')
        print('%s, is that your name? Y or N?' % name)
        confirm = input('> ')
        if confirm.upper() == 'Y':
            player = gen.Manager(name)
            league = gen.League()
            team_selection()
            break
        elif confirm.upper() == 'N':
            print("Sorry! Let's try that again.")
        else:
            print("I didn't catch that. Make sure you enter either a Y or an N.")


def load_game():
    #TODO Load game function
    print('load game')


def team_selection():
    print("Now, which team would you like to manage? Enter their corresponding number once you've decided")
    for n in range(10):
        print(str(n+1) + ') ' + league.team_list[n].get_name())

    while True:
        choice = input('> ')
        my_team = league.team_list[int(choice)-1]
        print('%s, is that your team? Y or N?' % my_team.get_name())
        confirm = input('> ')
        if confirm.upper() == 'Y':
            print('Alright. You are the now the manager of %s' % my_team.get_name())
            team = gen.PlayerTeam('Testing', my_team.prestige)    #so this creates a new type of team using the class PlayerTeam with the information from the old team
            league.team_list[int(choice)-1] = team #this line then replaces the old team with the new team in the list of team objects

            break
        elif confirm.upper() == 'N':
            print("Sorry! Let's try that again.")
        else:
            print("I didn't catch that. Make sure you enter either a Y or an N.")


main()
