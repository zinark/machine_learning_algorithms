import json
import pandas as pd
from pandas.io.json import json_normalize
import numpy as np

with open("./LeagueStageFixture.json") as f:
    dt = json.load(f)
    dt = dt["LeagueStage"][0]["LeagueFixture"]
    dt = json_normalize(dt)

values = {
    "home" : [],
    "away" : [],
    "score": [],
}
labels = []
# print dt.head()
for i, row in dt.iterrows():
    home_name = row["HomeTeamName"]
    home_score = row["HomeTeamScore"]
    away_score = row["AwayTeamScore"]
    away_name = row["AwayTeamName"]

    score = None
    if len(home_score) > 0:
        if home_score > away_score: score = 1;
        if home_score < away_score: score = -1;
        if home_score == away_score: score = 0;

    if score is not None:
        labels.append(home_name)
        values["home"].append(home_name)
        values["away"].append(away_name)
        values["score"].append(score)

    # print u"{} - {} - {}\t{} - {}".format(
    #     row["StartDate"],
    #     home_name, home_score,
    #     away_name, away_score
    # )
data = pd.DataFrame(values)
print data
# dt = pd.read_json("LeagueStageFixture.json")
# http://www.posta.com.tr/api/LiveScore/LeagueStage?TournamentID=1&includeTable=1

