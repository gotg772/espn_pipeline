Truncate table staging.TeamsStaging;
Truncate table staging.PlayersStaging; 


COPY staging.TeamsStaging
FROM '/var/lib/postgresql/data/teams.csv' 
DELIMITER ',' 
CSV HEADER;

COPY staging.PlayersStaging
FROM '/var/lib/postgresql/data/players.csv' 
DELIMITER ',' 
CSV HEADER;

COPY staging.MatchupStaging
FROM '/var/lib/postgresql/data/matchup.csv' 
DELIMITER ',' 
CSV HEADER;

COPY staging.GameStatsStaging
FROM '/var/lib/postgresql/data/gameStats.csv' 
DELIMITER ',' 
CSV HEADER;