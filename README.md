# Scale Up - Linear Regression Python Spike

For my module 4 project, Scale Up, at Turing, I decided to do a Python spike.  This repo is my first crack at coding a Linear Regression from scratch as well as my first time working with Python.

The goal was to use a linear regression algorithm to predict the amount of runs a team would score at home based on the number of hits they record.

The runner file gathers the necessary data from a Python API called `mlbgame`.  You can follow the commands listed below to run the algorithm for a given team. The script in the runner gathers and formats the needed data for the given team, and prints out the training set, the regression results (line of best fit), and best guess for how many runs a team would score if they recorded 1000 hits.  For next steps I would love for the user to be able to input the number of hits they would like to calculate as well as specify if they want results for home games, away games, or all games.

The rest of the code consists of a hypothesis function, cost function, and regression that should be able to calculate the slope and intercept of the best fit line. As it stands right now, the runner takes quite a bit of time to run since it must gather the data for hundreds of baseball games from the mlbgame API.  I left commented out code and comments at the bottom of the linear regression file along with some sample data sets.  If you would like to play around with the regression (learning rate, threshold, n variables) with a hard-coded training set, follow the instructions below.

To run locally:
- clone down repo
- cd into the repo

#### To install the mlbgame API that is used to gather data:
```
pip install mlbgame
```

#### To view the training set, results, and prediction for a given team:
```
python runner.py "<team name here in quotes>"
```

Example:
```
python runner.py "Red Sox"
```

#### To run the regression analysis with hard-coded data sets:

Un-comment out the code from line 41 down to the end of the file.  You may change the training set inside the parentheses on line 47.  On line 51 you can alter the second, third, or fourth arguments which represent the learning rate, adjustment threshold, and max number of adjustments, respectively.  Finally, you can change the input for the function on line 56 which represents the number of hits you want to check your results with.  Once these are set, run the following command from your terminal:

```
python linear_regression.py
```

If you have any questions/comments/recommendations I would love to hear them.  Or if you just want to talk baseball that's fine too.
