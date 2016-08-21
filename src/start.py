import click
import gen
import office

global user

def new_game():
    global user
    name = click.prompt('\nCongratulations on becoming a manager! What is your name?', confirmation_prompt=True)
    user = gen.Manager(name)
    print('\n')
    click.clear()
    print('Here are the list of teams in the league:')
    for n in range(10):
       click.echo(str(n + 1) + ') ' + user.get_league().get_team_list()[n].get_name())
    team_selection()

def load_game():
    #TODO Load game function
    print('load game')

def team_selection():

    team = click.prompt('\nWhich team would you like to manage?', type=str)
    global my_team
    global temp

    n=0
    for option in user.get_league().get_team_list():
        if team.lower() in option.get_name().lower():
            temp = option
            my_team = option
        else:
            n+=1
    if n==10:
        print('Uh oh, we didn\'t find that team. Just type in some, or all of its name as it appears on your screen.')
        team_selection()
    if click.confirm('Is %s the team you want to manage?' % my_team.get_name()):
        print('\nAlright. You are the now the manager of %s.' % my_team.get_name())
        my_team = gen.PlayerTeam(my_team.get_name(), my_team.prestige)    #so this creates a new type of team using the class PlayerTeam with the information from the old team
        user.get_league().get_team_list()[user.get_league().get_team_list().index(temp)] = my_team        #this line then replaces the old team with the new team in the list of team objects
        user.set_team(my_team)
        print('Here are your current players, and some information about them:\n')
        print('Name:'.ljust(25, ' ') + ' | ' + 'Position:'.ljust(10, ' ') + ' | ' + 'Rating:')
        for x in range(len(my_team.player_list)):
            print(my_team.player_list[x].get_name('fl').ljust(25, ' ') + ' | ' + my_team.player_list[x].get_position().ljust(10, ' ') + ' | ' + str(my_team.player_list[x].get_PPR()))
        while True:    
            if click.confirm('\nRead to move on?'):
                print('Let\'s head on over to your new office!')
                man_office()
                break
            else:
                print('Just tell me when you\'re ready.')
            
    else:
        team_selection()

def man_office():
    office.main(user, True)

@click.command()
@click.help_option()
def main():
    """pyFootball v.1 Early Alpha

    A python based football management simulator,
    very similar to and heavily based on Football Manager created by Sports
    Interactive.

    To start or load a game, run this file without any parameters.

    Coded by Justin Auger
    http://justnaugr.github.io\n
    Credits to Click for the great CLI.


    """
    start = click.prompt('Would you like to start a new game or load a saved game?', type=click.Choice(['new','load']))
    if start=='new':
        new_game()
    elif start=='load':
        load_game()


if __name__ == '__main__':
    main()
