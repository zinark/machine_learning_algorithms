import json
import pandas as pd
from pandas.io.json import json_normalize

with open("./LeagueStageFixture.json") as f:
    dt = json.load(f)
    dt = dt["LeagueStage"][0]["LeagueFixture"]
    dt = json_normalize(dt)

# print dt.head()
for i, row in dt.iterrows():
    print u"{} - {} - {}\t{} - {}".format(
        row["StartDate"],
        row["HomeTeamName"], row["HomeTeamScore"],
        row["AwayTeamName"], row["AwayTeamScore"]
    )

# dt = pd.read_json("LeagueStageFixture.json")
#http://www.posta.com.tr/api/LiveScore/LeagueStage?TournamentID=1&includeTable=1
