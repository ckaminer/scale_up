from __future__ import print_function
import mlbgame
import sys

seasons = [2011, 2012, 2013, 2014, 2015]
team = sys.argv[1]
training_set = []

def single_season_total(year):
    season = mlbgame.games(year, home=team)
    games = mlbgame.combine_games(season)
    runs = 0
    hits = 0
    for game in games:
        try:
            runs = runs + mlbgame.team_stats(game.game_id)["home_batting"].r
            hits = hits + mlbgame.team_stats(game.game_id)["home_batting"].h
        except:
            "n/a"
    return {"i": hits, "o": runs}

for season in seasons:
    i_o = single_season_total(season)
    training_set.append(i_o)


print(training_set)
