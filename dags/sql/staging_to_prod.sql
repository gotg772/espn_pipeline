DELETE FROM espn.Teams

INSERT INTO espn.Teams
SELECT * from staging.TeamsStaging

DELETE FROM espn.Players

INSERT INTO espn.Players
SELECT * from staging.PlayersStaging



MERGE espn.matchup AS Target
USING stagin.matchup AS Source
ON Source.matchupID = Target.matchupID
WHEN NOT MATCHED BY Target THEN
    INSERT (matchupID, homeTeam ,awayTeam , week, homeScore, awayScore) 
    VALUES (Source.matchupID, Source.homeTeam ,Source.awayTeam , Source.week, Source.homeScore, Source.awayScore);

MERGE espn.gameStats AS Target
USING stagin.GameStatsStaging AS Source
ON Source.boxScoreID = Target.boxScoreID
WHEN NOT MATCHED BY Target THEN
    INSERT (matchupID, homeTeam ,awayTeam , week, homeScore, awayScore) 
    VALUES (Source.matchupID, Source.homeTeam ,Source.awayTeam , Source.week, Source.homeScore, Source.awayScore);