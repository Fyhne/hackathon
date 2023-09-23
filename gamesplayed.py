import requests
import json
import gzip
import shutil
from io import BytesIO
from projectPath import projectPath

with open(f'{projectPath}\\playerList.json') as f:
    playerList = json.load(f)

def playCount(playername):
    playcounter = 0
    for playerset in playerList:
        print(playerset)
        if playername in str(playerset):
            playcounter = playcounter + 1
    print(playername)
    print(playcounter)

playCount('MIR Allorim')