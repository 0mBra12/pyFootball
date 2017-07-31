# pyFootball
(SOON TO BE REPLACED WITH A JAVA BASED ANDROID APP VERSION)
A python based Football (or soccer) management simulation game. Currently in development as a side project that I'll intermittently work on while learning python and working on other java projects. The game is heavily based on [Football Manager](http://www.footballmanager.com/) by Sports Interactive, and [Football Chairman](http://www.football-chairman.com/) by Underground Creative.

### Methodology
1. Team Stats
  1. Prestige - How the team supposedly fared in the past, how succesful they once were
  2. Wealth - How much money they have to spend, directly influenced by prestige
  3. Pass Capacity (PC) - How well the team is able to play their form of build up, be it short passing or long crosses
  4. xDP, xMP, xAP - expected Defense, Midfield, and Attacking performance; composite of player D/M/A stats
  5. Team Persona - How the team is viewed by the fans, the media, and the players
2. Player Stats
  1. Height & Weight for a Physicality bonus
  2. Potential Performance Rating (PPR) a number ranging from 50-100 reflecting on what a player's near maximum capable level of performance, not accounting for hidden stats or bonuses.
  3. Hidden stats: Loyalty, Consistency, Injury Proneness

### Tasks
- [x] Simulate the 10 teams, and give ownership of one team to the Player
- [x] Create 18 players for each team, giving them unique stats, transfer values, and names.
- [ ] Successfully integrate a satisfactory match engine that will provide results for each game along with simulating the other 4 games taking place each match week, including booking, sending offs, and injuries
- [ ] Create an inbox where you'll see your managerial news, team updates, and anything else relevant to the game.
- [ ] Possibly add names and stats to other managers to allow rivalries to form, and also include team rivalries due to proximity, history, similar prestige/wealth.
- [ ] Create a transfer market where you can buy and sell players, and possibly have contract expirations to your own players.

[check me out @ justnaugr.github.io](http://justnaugr.github.io) and check out my smaller project, [shellScore](https://github.com/JustnAugr/shellScore) a python based football match result script
