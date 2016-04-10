#The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

# The below skeleton is optional.  You can use it or you can write the script with an approach of your choice.


import csv

data = 'football.csv'
h = []
d = []

# import data
with open(data, 'rb') as infile:
    reader = csv.reader(infile)
    d = list(reader)
    h = d.pop(0)
    #print h
    #print d

# add Score Difference column
h.append('Score Difference')

# calc score_diff & append to end of data lists
for i in range(len(d)):
    score_diff = int(d[i][5]) - int(d[i][6])
    d[i].append(score_diff)

# find minimum score diff (Goals - Goals Allowed)
min_score_diff = 0
for i in range(len(d)):
    if d[i][8] < min_score_diff:
        min_score_diff = d[i][8]
print min_score_diff

# find team w/ min score diff
for i in range(len(d)):
    if d[i][8] == -34:
        print d[i][0]
