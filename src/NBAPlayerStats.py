##############################################################################
# 
#       Program Name: NBAPlayerStats.py
#
#       Description: Fetches NBA Player stats using NBA API and tabulates
#       carrer stats, season stats and gamelog stats 
#
#       Language: Python
#
#       Date: 4/14/2023
# 
#       Author: Joshua Farias
#
##############################################################################

#imports
from nba_api.stats.static import players
from nba_api.stats.endpoints import playercareerstats, playergamelog
from tabulate import tabulate

#promts user to enter the name of an NBA player
player_name = input("Enter player name: ")
player = players.find_players_by_full_name(player_name)[0]
player_id = player['id']

#gets the career stats from NBA player entered by user, creates dataframe, filters collumns and tabulates the data
career = playercareerstats.PlayerCareerStats(player_id=player_id)
career_df = career.get_data_frames()[0].loc[:, ['SEASON_ID', 'TEAM_ABBREVIATION', 'PLAYER_AGE', 'GP', 'GS', 'MIN', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS']]
career_table = tabulate(career_df, headers=career_df.columns, tablefmt='pretty')

#gets the season stats from NBA player entered by user, creates dataframe, filters collumns and tabulates the data
season = playercareerstats.PlayerCareerStats(player_id=player_id, per_mode36='PerGame')
season_df = season.get_data_frames()[0].loc[:, ['SEASON_ID', 'TEAM_ABBREVIATION', 'PLAYER_AGE', 'GP', 'GS', 'MIN', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS']]
season_table = tabulate(season_df, headers=season_df.columns, tablefmt='pretty')

#gets the gamelog stats from NBA player entered by user if they played in the current season, creates dataframe and tabulates the data
game_log = playergamelog.PlayerGameLog(player_id=player_id)
game_log_df = game_log.get_data_frames()[0].loc[:, ['GAME_DATE', 'MATCHUP', 'WL', 'MIN', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS']]
game_log_table = tabulate(game_log_df, headers=game_log_df.columns, tablefmt='pretty')

#prints out formated data
print("\nPlayer Name:", player['full_name'])
print("Career Stats:\n", career_table)
print("\nSeason Stats:\n", season_table)
print("\nGame Log Stats:\n", game_log_table)
