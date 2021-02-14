**Queries with answers also in Part4_answers.ipynb**
#1
```sql
WITH all_matches AS (
SELECT *, 'ausmen' as tournament FROM aus_men
UNION ALL
SELECT *, 'frenchmen' as tournament FROM french_men
UNION ALL
SELECT *, 'usmen' as tournament FROM us_men
UNION ALL
SELECT *, 'auswomen' as tournament FROM aus_women
UNION ALL
SELECT *, 'frenchwomen' as tournament FROM french_women
UNION ALL
SELECT *, 'uswomen' as tournament FROM us_women
UNION ALL
SELECT *, 'wimbeldonmen' as tournament FROM wimbledon_men
UNION ALL
SELECT *, 'wimbeldonwomen' as tournament FROM wimbledon_women
),
players as (
SELECT all_matches."Player1" as player, all_matches."tournament" as tournament
FROM all_matches
UNION ALL
SELECT all_matches."Player2" as player, all_matches."tournament" as tournament
FROM all_matches)

SELECT player,tournament, count(*) as "matches in tournament"
FROM players
GROUP BY player,tournament
ORDER BY "matches in tournament" DESC
```

#2
Women:
```sql
WITH all_matches AS (
SELECT * FROM aus_women
UNION ALL
SELECT * FROM french_women
UNION ALL
SELECT * FROM us_women
),
players as (
SELECT all_matches."Player1" as player
FROM all_matches
UNION ALL
SELECT all_matches."Player2" as player
FROM all_matches)

SELECT player, Count(*) as num_matches
FROM players
GROUP BY player
ORDER BY num_matches DESC

```
Men:
```sql
WITH all_matches AS (
SELECT * FROM aus_men
UNION ALL
SELECT * FROM french_men
UNION ALL
SELECT * FROM us_men
),
players as (
SELECT all_matches."Player1" as player
FROM all_matches
UNION ALL
SELECT all_matches."Player2" as player
FROM all_matches)

SELECT player, Count(*) as num_matches
FROM players
GROUP BY player
ORDER BY num_matches DESC


```

#3
```sql
WITH all_matches AS (
SELECT * FROM aus_men
UNION ALL
SELECT * FROM french_men
UNION ALL
SELECT * FROM us_men
UNION ALL
SELECT * FROM aus_women
UNION ALL
SELECT * FROM french_women
UNION ALL
SELECT * FROM us_women
),
fsps as (
SELECT all_matches."Player1" as player, all_matches."FSP.1" as fsp
FROM all_matches
UNION ALL
SELECT all_matches."Player2" as player, all_matches."FSP.2" as fsp
FROM all_matches)

SELECT *
FROM fsps
ORDER BY fsp DESC
LIMIT 1

```

#4
```sql
WITH all_matches AS (
SELECT * FROM aus_men
UNION ALL
SELECT * FROM french_men
UNION ALL
SELECT * FROM us_men
UNION ALL
SELECT * FROM aus_women
UNION ALL
SELECT * FROM french_women
UNION ALL
SELECT * FROM us_women
),
info as (
SELECT all_matches."Player1" as player, all_matches."UFE.1" as unforced_errors, all_matches."TPW.1" as points_won,
CASE WHEN all_matches."Result" = 1 THEN 1 ELSE 0 END AS win
FROM all_matches
UNION ALL
SELECT all_matches."Player2" as player, all_matches."UFE.2" as unforced_errors, all_matches."TPW.2" as points_won,
CASE WHEN all_matches."Result" = 0 THEN 1 ELSE 0 END AS win
FROM all_matches)

SELECT player, SUM(unforced_errors)/SUM(points_won)*100 as ufe_percent, SUM(win) as wins
FROM info
GROUP BY player
ORDER BY wins DESC
LIMIT 4

```

