
-- Q1: Teams containing 'India'
SELECT DISTINCT team1 AS team
FROM matches
WHERE team1 LIKE '%India%';


-- Q2: All matches (no date available)
SELECT team1, team2, venue, city
FROM matches;


-- Q3: Top 10 teams by matches played
SELECT team1, COUNT(*) AS matches_played
FROM matches
GROUP BY team1
ORDER BY matches_played DESC
LIMIT 10;


-- Q4: Most used venues
SELECT venue, COUNT(*) AS total_matches
FROM matches
GROUP BY venue
ORDER BY total_matches DESC;


-- Q5: Matches played by each team
SELECT team1 AS team, COUNT(*) AS matches
FROM matches
GROUP BY team1
ORDER BY matches DESC;


-- Q6: Team appearance count
SELECT team1, COUNT(*) AS appearances
FROM matches
GROUP BY team1;


-- Q7: Team with highest matches
SELECT team1, COUNT(*) AS matches
FROM matches
GROUP BY team1
ORDER BY matches DESC
LIMIT 1;


-- Q8: All match locations
SELECT DISTINCT venue, city
FROM matches;

SELECT team1, COUNT(*) FROM matches GROUP BY team1;

-- Q9: Teams that have played more than 2 matches
SELECT team1, COUNT(*) AS total_matches
FROM matches
GROUP BY team1
HAVING COUNT(*) > 2
ORDER BY total_matches DESC;


-- Q10: Last 20 matches (no date → limit records)
SELECT team1, team2, venue, city
FROM matches
LIMIT 20;


-- Q11: Compare team participation across venues
SELECT team1, venue, COUNT(*) AS matches_played
FROM matches
GROUP BY team1, venue
ORDER BY matches_played DESC;


-- Q12: Home vs Away simulation (based on city name match)
SELECT
    team1,
    CASE
        WHEN team1 LIKE CONCAT('%', city, '%') THEN 'Home'
        ELSE 'Away'
    END AS match_type,
    COUNT(*) AS matches
FROM matches
GROUP BY team1, match_type;


-- Q13: Frequent team pair combinations
SELECT team1, team2, COUNT(*) AS matches
FROM matches
GROUP BY team1, team2
HAVING COUNT(*) >= 1
ORDER BY matches DESC;


-- Q14: Venue usage by teams
SELECT venue, team1, COUNT(*) AS matches
FROM matches
GROUP BY venue, team1
ORDER BY matches DESC;


-- Q15: Close match simulation (no score → using repeat matches)
SELECT team1, COUNT(*) AS close_matches
FROM matches
GROUP BY team1
HAVING COUNT(*) >= 2
ORDER BY close_matches DESC;


-- Q16: Team activity trends (basic grouping)
SELECT team1, COUNT(*) AS matches_played
FROM matches
GROUP BY team1
ORDER BY matches_played DESC;

SELECT team1, COUNT(*) FROM matches GROUP BY team1 HAVING COUNT(*) > 2;


-- Q17: Toss advantage simulation (using team frequency)
SELECT
    team1,
    COUNT(*) AS matches,
    ROUND((COUNT(*) * 100.0) / (SELECT COUNT(*) FROM matches), 2) AS percentage
FROM matches
GROUP BY team1
ORDER BY percentage DESC;


-- Q18: Most active teams (economical bowlers substitute)
SELECT
    team1,
    COUNT(*) AS matches_played
FROM matches
GROUP BY team1
HAVING COUNT(*) >= 2
ORDER BY matches_played DESC;


-- Q19: Consistent teams (using frequency stability)
SELECT
    team1,
    COUNT(*) AS matches,
    STDDEV(COUNT(*)) OVER () AS consistency
FROM matches
GROUP BY team1;


-- Q20: Matches played by each team across cities
SELECT
    team1,
    city,
    COUNT(*) AS matches
FROM matches
GROUP BY team1, city
ORDER BY team1;


-- Q21: Ranking teams by performance (frequency score)
SELECT
    team1,
    COUNT(*) AS matches,
    RANK() OVER (ORDER BY COUNT(*) DESC) AS rank_position
FROM matches
GROUP BY team1;


-- Q22: Head-to-head analysis between teams
SELECT
    team1,
    team2,
    COUNT(*) AS total_matches
FROM matches
GROUP BY team1, team2
HAVING COUNT(*) >= 1
ORDER BY total_matches DESC;


-- Q23: Recent performance (last 10 records)
SELECT
    team1,
    COUNT(*) AS recent_matches
FROM (
    SELECT * FROM matches LIMIT 10
) AS recent
GROUP BY team1;


-- Q24: Best venue-team combinations
SELECT
    team1,
    venue,
    COUNT(*) AS matches
FROM matches
GROUP BY team1, venue
HAVING COUNT(*) >= 1
ORDER BY matches DESC;


-- Q25: Trend analysis (city-based distribution)
SELECT
    city,
    COUNT(*) AS matches,
    CASE
        WHEN COUNT(*) >= 3 THEN 'High Activity'
        WHEN COUNT(*) = 2 THEN 'Medium Activity'
        ELSE 'Low Activity'
    END AS activity_level
FROM matches
GROUP BY city
ORDER BY matches DESC;

SELECT team1, COUNT(*) FROM matches GROUP BY team1;