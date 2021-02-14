**Queries with answers also in Part2_answers.ipynb**

#1
```sql
SELECT yearID, teamID, SUM(salary) as TotalSalaries
FROM salaries
GROUP BY yearID, teamID;
```

#2
```sql
SELECT playerID, MIN(yearID) as firstYear, MAX(yearID) as LastYear
FROM fielding
GROUP BY playerID
```

#3
```sql
SELECT playerID, COUNT(gameID) as numAllstars
FROM allstarfull
GROUP BY playerID
ORDER BY numAllStars DESC

```

#4
```sql
SELECT schoolID, count(DISTINCT playerID) as distPlayers
FROM collegeplaying
GROUP BY schoolID
ORDER BY distPlayers DESC
```

#5
```sql
SELECT playerID, Cast((JulianDay(finalgame_date)-JulianDay(debut_date)) as Float)/365 AS careerLength
FROM people
```

#6
```sql
SELECT Cast(strftime('%m', debut)AS Integer) AS Month, COUNT(*) as numDebuts
FROM people
GROUP BY Month
```

#7
```sql
SELECT AVG(salary)
FROM people LEFT JOIN salaries on people.playerID = salaries.playerID
```

```sql
SELECT AVG(salary)
FROM salaries LEFT JOIN people ON salaries.playerID = people.playerID
```

#9
```sql
SELECT SupplierID, COUNT(ProductID), AVG(Price)
FROM Products
GROUP BY SupplierID
HAVING COUNT(ProductID) >= 3
ORDER BY AVG(Price) DESC
```
