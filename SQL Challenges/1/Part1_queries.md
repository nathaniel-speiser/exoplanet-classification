#1
```sql
SELECT * FROM Customers WHERE Country='UK';
```

#2
```sql
SELECT Customers.CustomerName, COUNT(*)
FROM Orders LEFT JOIN Customers ON Orders.CustomerID = Customers.CustomerID
GROUP BY Orders.CustomerID
ORDER BY COUNT(*) DESC
LIMIT 1
```

#3
```sql
SELECT Products.SupplierID, Suppliers.SupplierName, AVG(Products.Price)
From Products LEFT JOIN Suppliers on Products.SupplierID = Suppliers.SupplierID
Group By Products.SupplierID
ORDER BY AVG(Price) DESC
```

#4
```sql
SELECT COUNT(DISTINCT Country) FROM Customers
```

#5
```sql
SELECT Categories.CategoryName, COUNT(*)
FROM OrderDetails LEFT JOIN Products ON OrderDetails.ProductID = Products.ProductID LEFT JOIN Categories on Products.CategoryID = Categories.CategoryID
GROUP BY Categories.CategoryName
ORDER BY COUNT(*) DESC
```

#6
```sql
SELECT OrderID, SUM(OrderDetails.Quantity * Products.Price) as SumTotalPrice
FROM OrderDetails LEFT JOIN Products ON OrderDetails.ProductID = Products.ProductID
GROUP BY OrderID
```

#7
```sql
WITH OrderTotals AS(
SELECT OrderID, SUM(OrderDetails.Quantity * Products.Price) as SumTotalPrice
FROM OrderDetails LEFT JOIN Products ON OrderDetails.ProductID = Products.ProductID
GROUP BY OrderID)
SELECT Employees.EmployeeID, LastName, Firstname, SUM(SumTotalPrice) as AllSales
FROM OrderTotals LEFT JOIN Orders on OrderTotals.OrderID = Orders.OrderID LEFT JOIN Employees on Orders.EmployeeID = Employees.EmployeeID
GROUP BY Employees.EmployeeID
ORDER BY AllSales DESC
```

#8
```sql
SELECT Count(*) FROM Employees
WHERE Notes LIKE '%BS%'
```

#9
```sql
SELECT SupplierID, COUNT(ProductID), AVG(Price)
FROM Products
GROUP BY SupplierID
HAVING COUNT(ProductID) >= 3
ORDER BY AVG(Price) DESC
```
