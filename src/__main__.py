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
        elif start_option.lower() == 'exit':
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
        elif confirm.lower() == 'exit':
            break
        else:
            print("I didn't catch that. Make sure you enter either a Y or an N.")


def load_game():
    #TODO Load game function
    print('load game')


def team_selection():
    print("Now, which team would you like to manage? Enter their corresponding number once you've decided")
    for n in range(10):
        print(str(n + 1) + ') ' + league.team_list[n].get_name())

    while True:
        choice = input('> ')
        try:
            my_team = league.team_list[int(choice)-1]
        except ValueError:
            print("Enter a number from 1 to 10.")
            continue
        print('%s, is that your team? Y or N?' % my_team.get_name())
        confirm = input('> ')
        if confirm.upper() == 'Y':
            print('Alright. You are the now the manager of %s.' % my_team.get_name())
            my_team = gen.PlayerTeam(my_team.get_name(), my_team.prestige)    #so this creates a new type of team using the class PlayerTeam with the information from the old team
            league.team_list[int(choice)-1] = my_team #this line then replaces the old team with the new team in the list of team objects
            print(str(my_team.prestige))
            print('Here are your current players, and some information about them:')
            print('Name:'.ljust(25, ' ') + ' | ' + 'Position:'.ljust(10, ' ') + ' | ' + 'Rating:')
            for x in range(len(my_team.player_list)):
                print(my_team.player_list[x].get_name().ljust(25, ' ') + ' | ' + my_team.player_list[x].get_position().ljust(10, ' ') + ' | ' + str(my_team.player_list[x].get_PPR()))
            break
        elif confirm.upper() == 'N':
            print("Sorry! Let's try that again.")
        else:
            print("I didn't catch that. Make sure you enter either a Y or an N.")

main()
