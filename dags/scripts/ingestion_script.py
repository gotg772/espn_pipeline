#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 10:27:23 2022

@author: colehoward
"""

from espn_api.football import League
from player_stats_map import PLAYER_STATS_MAP
import pandas as pd
from secret.py as secret import *


import collections

def flatten(d, parent_key='', sep='_'):
    items = []
    for k, v in d.items():
        new_key = parent_key + sep + k if parent_key else k
        if isinstance(v, collections.MutableMapping):
            items.extend(flatten(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

# ESPN data ingestion script

league = League(league_id=secret.league_id, year=2022, espn_s2= secret.espn_s2, swid=secret.swid)


# League dim

league_id = league.league_id

# Date dim 

current_week = 5
nfl_week = league.nfl_week
current_league_yr = league.year

# Teams dim

league_teams = league.teams
team_columns = {'team_id':[],'name':[],'standing':[],'projected_rank': [],'playoff_pct': []}
team_rosters  = {}
for team in league_teams:
       team_columns['team_id'].append(team.team_id) 
       team_columns['name'].append(team.team_name) 
       team_columns['standing'].append(team.standing) 
       team_columns['projected_rank'].append(team.draft_projected_rank)
       team_columns['playoff_pct'].append(team.playoff_pct)
       team_rosters[team.team_name] = team.roster
       
       
    
# date dim
league_yr = league.year
league_week = league.current_week 

# box player fact table
games = league.box_scores(current_week)
game_fact_dict = {'league_id':[],'team_id':[],'matchup_id':[],'player_id':[],'week':[],'player_points':[],'projected_points':[],'game_played':[]}
for game in games:
    
          
            for away_player in game.away_lineup:
                game_fact_dict['player_points'].append(away_player.points)
                game_fact_dict['projected_points'].append(away_player.projected_points)
                game_fact_dict['game_played'].append(away_player.game_played)
                game_fact_dict['team_id'].append(game.away_team.team_id)
                game_fact_dict['player_id'].append(away_player.playerId)
                game_fact_dict['league_id'].append(league.league_id)
                game_fact_dict['week'].append(current_week)
                game_fact_dict['matchup_id'].append(game.home_team.team_abbrev+game.away_team.team_abbrev+str(current_week))
                
                
                
            for home_player in game.home_lineup:
                
                game_fact_dict['player_points'].append(home_player.points)
                game_fact_dict['projected_points'].append(home_player.projected_points)
                game_fact_dict['game_played'].append(home_player.game_played)
                game_fact_dict['team_id'].append(game.home_team.team_id)
                game_fact_dict['player_id'].append(home_player.playerId)
                game_fact_dict['league_id'].append(league.league_id)
                game_fact_dict['week'].append(current_week)
                game_fact_dict['matchup_id'].append(game.home_team.team_abbrev+game.away_team.team_abbrev+str(current_week))
                
            
            

game.away_team.team_abbrev



# Matchup dim
weekly_matchups = league.box_scores(current_week)
wk_matchups_dict = {'home_team': [],'away_team': [],'fantasy_week': [],'nfl_week':[],'year':[],'home_score':[],'away_score':[]}
for matchup in weekly_matchups:
    wk_matchups_dict['home_team'].append(matchup.home_team.team_name)
    wk_matchups_dict['away_team'].append(matchup.away_team.team_name)
    wk_matchups_dict['fantasy_week'].append(current_week)
    wk_matchups_dict['nfl_week'].append(nfl_week)
    wk_matchups_dict['year'].append(current_league_yr)
    wk_mztchups_dict['home_score'].append(matchup.home_score)
    wk_mztchups_dict['away_score'].append(matchup.away_score)
    
#player dim
player_dict = {'playerId':[],'name':[],'position':[],'proteam':[],'fantasy_team':[],'pos_rk':[]}
for team in league_teams:
        for player in team.roster:
            player_dict['name'].append(player.name)
            player_dict['playerId'].append(player.playerId)
            player_dict['position'].append(player.position)
            player_dict['proteam'].append(player.proTeam)
            player_dict['fantasy_team'].append(team.team_id)
            player_dict['pos_rk'].append(player.posRank)
    


player_df = pd.DataFrame.from_dict(player_dict)
matchups_df = pd.DataFrame.from_dict(wk_matchups_dict)
game_fact_df = pd.DataFrame.from_dict(game_fact_dict)
team_df = pd.DataFrame.from_dict(team_columns)
