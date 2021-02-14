**Queries with answers also in Part3_answers.ipynb**

#1
```sql
SELECT home_team_api_id, team_long_name AS home_team_name, home_team_goal
FROM Match LEFT JOIN Team ON Match.home_team_api_id = Team.team_api_id
ORDER BY home_team_goal DESC
LIMIT 5
```

#2
```sql
SELECT away_team_api_id, team_long_name AS away_team_name, away_team_goal
FROM Match LEFT JOIN Team ON Match.away_team_api_id = Team.team_api_id
ORDER BY away_team_goal DESC
LIMIT 5
```

#3
```sql
SELECT Count(*) as num_ties
FROM Match
WHERE home_team_goal = away_team_goal
```

#4
Number of Smiths:
```sql
SELECT Count(*) as "Number of Smiths"
FROM Player
WHERE player_name LIKE '% Smith'
```

Number of players with smith in name:
```sql
SELECT Count(*) as "Number with smith in name"
FROM Player
WHERE player_name LIKE '%smith%'
```
#5
```sql
With tie_scores AS(SELECT home_team_goal as tie_score
FROM Match
WHERE home_team_goal = away_team_goal
ORDER BY tie_score)

SELECT AVG(tie_score) as "Median tie score"
FROM (SELECT tie_score
      FROM tie_scores
      ORDER BY tie_score
      LIMIT 2 - (SELECT COUNT(*) FROM tie_scores) % 2
      OFFSET (SELECT (COUNT(*) - 1) / 2
              FROM tie_scores))
```

#6
```sql
WITH right AS (SELECT player_api_id, preferred_foot
FROM Player_Attributes
GROUP BY player_api_id
HAVING preferred_foot='right')

SELECT CAST((SELECT COUNT(*) FROM right) as float) / CAST((SELECT COUNT(*) FROM Player)AS float)*100 as pct_right,
100-CAST((SELECT COUNT(*) FROM right) as float) / CAST((SELECT COUNT(*) FROM Player)AS float)*100 as pct_left

```

