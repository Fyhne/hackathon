import requests
import json
import gzip
import shutil
from io import BytesIO

S3BucketGamesDatabase = "https://power-rankings-dataset-gprhack.s3.us-west-2.amazonaws.com/games/{}.json.gz" #.format should be used along with fileName to provide the specific file being searched for

def getFile(file_name):
    response = requests.get(S3BucketGamesDatabase.format(file_name))
    gzipBytes = BytesIO(response.content)
    with gzip.GzipFile(fileobj = gzipBytes, mode = 'rb') as gzipped_file:
        with open(f"currentgame.json", 'wb') as output_file:
            shutil.copyfileobj(gzipped_file, output_file)

def getSummonerNames():
    with open(r"C:\Users\Caeden\currentgame.json") as f:
        gameData = json.load(f)

    for event in gameData:
        if 'game_info' == event.get('eventType'):
            for participant in event['participants']:
                with open(r"C:\Users\Caeden\Hackathon\playerList.json", 'w') as writeFile:
                    json.dumps(participant.get('summonerName'))

def getGameInfo():
    with open(r'C:\Users\Caeden\Hackathon\esports-data\tournaments.json') as f:
        data = json.load(f)
    with open(r"C:\Users\Caeden\Hackathon\esports-data\mapping_data.json") as m:
        mappingData = json.load(m)

    mappings = {
        esports_game["esportsGameId"]: esports_game for esports_game in mappingData
    }

    for tournament in data:
        qual = '#2 Summer 2023'
        if qual == tournament.get("name"):
            for stage in tournament['stages']:
                for section in stage['sections']:
                    for match in section['matches']:
                        for game in match['games']:
                            if game['state'] == 'completed':
                                try:
                                    gameFileName = mappings[game["id"]]["platformGameId"]
                                    print(gameFileName)
                                    getFile(gameFileName)
                                    getSummonerNames()
                                    exit()
                                except KeyError:
                                    print('not found')
                                    continue

getGameInfo()