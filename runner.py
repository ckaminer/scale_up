from __future__ import print_function
import mlbgame
import sys

seasons = [2011, 2012, 2013, 2014, 2015]
team = sys.argv[1]
run_counts = []

def single_season_total(year):
    season = mlbgame.games(year, home=team)
    games = mlbgame.combine_games(season)
    runs = 0
    for game in games:
        try:
            runs = runs + mlbgame.team_stats(game.game_id)["home_batting"].r
        except:
            "n/a"
    return runs

for season in seasons:
    runs = single_season_total(season)
    run_counts.append(runs)

print(run_counts)
