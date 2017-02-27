# Scale Up - Linear Regression Python Spike

For my module 4 project, Scale Up, at Turing, I decided to do a Python spike.  This repo is my first crack at coding a Linear Regression from scratch as well as my first time working with Python.  

The goal was use a linear regression algorithm to predict the amount of runs a team would score at home based on the number of hits they record.

The runner file gathers the necessary data from a Python API called `mlbgame`.  As of right now, it simply gathers and formats the needed data for the given team.  The goal is to hook this up to the regression algorithm to gather, format, and then provide results in one shot.  I am waiting until the regression algorithm is working properly before hooking it up to the runner.

The rest of the code consists of a hypothesis function, cost function, and regression that should be able to calculate the slope and intercept of the best fit line.  Right now this is only working for training sets whose line of best fit has a slope greater than one.  

Final steps for completion involves figuring out why this only works for best fits with slopes greater than one, refactor, and hook up to the runner.

To run locally:
- clone down repo
- cd into the repo

#### To view the training set for a given team:
```
python runner.py "<team name here in quotes"
```

Example:
```
python runner.py "Red Sox"
```

#### To preview the regression analysis:
```
python linear_regression.py
```
NOTE: Regression file currently has hard-coded training sets at bottom of file for testing purposes.
