CREATE SCHEMA espn
    CREATE TABLE espn.Teams(teamID int PRIMARY KEY,
                            teamName text,
                            standing int,
                            projectedRank int,
                            playoffPct numeric)
                            

    CREATE TABLE espn.Matchup(matchupID  text PRIMARY KEY,
                                homeTeam text,
                                awayTeam text,
                                week int,
                                homeScore numeric,
                                awayScore numeric)
    
    CREATE TABLE espn.League(leagueID int PRIMARY KEY)

    CREATE TABLE espn.GameStats(boxScoreID int PRIMARY KEY,
                                PlayerID text,
                                leagueID int,
                                team_id text,
                                matchupID text,
                                week int,
                                player_points numeric,
                                projected_points numeric,
                                game_played int)
                                
    CREATE TABLE espn.Players(playerID int PRIMARY KEY,
                                playerName text,
                                position text,
                                posRank int,
                                fantasyTeam text,
                                injuryStatus text);
                                
                                
CREATE SCHEMA staging
    CREATE TABLE staging.TeamsStaging(teamID int PRIMARY KEY,
                            teamName text,
                            standing int,
                            projectedRank int,
                            playoffPct numeric)
                            

    CREATE TABLE staging.MatchupStaging(matchupID  text PRIMARY KEY,
                                homeTeam text,
                                awayTeam text,
                                week int,
                                homeScore numeric,
                                awayScore numeric)
    
    CREATE TABLE staging.LeagueStaging(leagueID int PRIMARY KEY)

    CREATE TABLE staging.GameStatsStaging(boxScoreID int PRIMARY KEY,
                                PlayerID text,
                                leagueID int,
                                team_id text,
                                matchupID text,
                                week int,
                                player_points numeric,
                                projected_points numeric,
                                game_played int)
                                
    CREATE TABLE staging.PlayerStaging(playerID int PRIMARY KEY,
                                playerName text,
                                position text,
                                posRank int,
                                fantasyTeam text,
                                injuryStatus text);
