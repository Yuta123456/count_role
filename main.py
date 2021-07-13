import sys
import re
import numpy
import os
import matplotlib.pyplot as plt
filepath = sys.argv[1]
data = []
count = 0
if not os.path.exists(filepath):
    print("ERROR: file not found error")
players = {}
with open(filepath) as f:
    for line in f:
        line = line.rstrip('\n')
        # Answerではない場合追加
        if (line.startswith("Answer:") or line == ""):
            continue
        roles = line.split(" ")
        for role in roles:
            # final(role(medium,11))
            role, player = role[len("final(role("):-len("))")].split(',')
            player = int(player)
            if player not in players:
                players[player] = {}
            if role not in players[player]:
                players[player][role] = 0
            players[player][role] += 1
if os.path.exists(sys.argv[1][:-4]):
    print("ERROR: dir is exists")
    key = input("Do you want to continue processing ? y/n : ")
    if (key != "y"):
        exit()
else:
    os.mkdir(sys.argv[1][:-4])

for p in range(1, len(players)+1):
    player = "player{}".format(p)
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1,
                         title=player)
    ax.bar(players[p].keys(), [players[p][role] for role in players[p]])
    ax.set_title(player)
    ax.set_xlabel('role')
    ax.set_ylabel('freq')
    print("./{}/{}.jpg".format(sys.argv[1][:-4], player), " saved")
    fig.savefig("./{}/{}.jpg".format(sys.argv[1][:-4], player))
