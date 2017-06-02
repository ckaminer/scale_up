from __future__ import print_function
import mlbgame
import sys
import json
from hypothesis_function import HypothesisFunction
from linear_regression import LinearRegression

seasons = [2011, 2012, 2013, 2014, 2015, 2016]
team = sys.argv[1]
training_set = []

def single_season_total(year):
    season = mlbgame.games(year, home = team, away = team, months=5)
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

def read_totals_file():
    return json.load(open("teamTotals.txt"))

def write_totals_file():
    json.dump(teamTotals, open("teamTotals.txt", 'w'))

teamTotals = read_totals_file()

if team in teamTotals.keys():
    print("team found")
    training_set = teamTotals[team]
else:
    print("team not found")
    for season in seasons:
        i_o = single_season_total(season)
        training_set.append(i_o)
    teamTotals[team] = training_set
    write_totals_file()

print("The %s recorded the following number of hits('i') and runs('o') at home from 2011-2016: \n%s\n" % (team, training_set))

lr = LinearRegression(training_set)
h = HypothesisFunction()
best_fit = lr.find_best_fit(h, .000001, .000005, 100)
print("The line of best fit was found to have y-intercept: %s, and slope: %s.\n" % (best_fit["b"], best_fit["m"]))

result_function = HypothesisFunction(best_fit["b"], best_fit["m"])
print("Based off of these findings, if the %s were to record 1000 hits at home next year, we can predict that they would score %s runs." % (team, int(result_function.result(1000))))
