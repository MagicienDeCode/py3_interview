# Solutions

- [SELECT](#SELECT)
- [Basic Joins](#basic-joins)
- [Basic Aggregate Functions](#basic-aggregate-functions)


## SELECT
- [1757. Recyclable and Low Fat Products](https://leetcode.com/problems/recyclable-and-low-fat-products/description)
```sql
SELECT p.product_id
FROM Products p
WHERE p.low_fats = 'Y' AND p.recyclable = 'Y';
```

- [584. Find Customer Referee](https://leetcode.com/problems/find-customer-referee/description)
```sql
SELECT c.name
FROM Customer c
WHERE c.referee_id != 2 OR c.referee_id IS NULL;
```

- [595. Big Countries](https://leetcode.com/problems/big-countries/description)
```sql
SELECT w.name, w.population, w.area
FROM World w
WHERE w.area >= 3000000 OR w.population >= 25000000;
```

- [1148. Article Views I](https://leetcode.com/problems/article-views-i/description/?envType=study-plan-v2&envId=top-sql-50)
```sql
SELECT DISTINCT (v.author_id) AS id 
FROM Views v
WHERE v.author_id = v.viewer_id
ORDER BY v.author_id ASC;
```

- [1683. Invalid Tweets](https://leetcode.com/problems/invalid-tweets/description)
```sql
SELECT t.tweet_id 
FROM Tweets t
WHERE LENGTH(t.content) > 15; 
```

## Basic Joins

- [1378. Replace Employee ID With The Unique Identifier](https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier/description)
```sql
SELECT eu.unique_id, e.name
FROM Employees e
LEFT JOIN EmployeeUNI eu ON e.id = eu.id;
```

- [1068. Product Sales Analysis I](https://leetcode.com/problems/product-sales-analysis-i/description)
```sql
SELECT p.product_name, s.year, s.price
FROM Sales s
INNER JOIN Product p ON s.product_id = p.product_id;
```

- [1581. Customer Who Visited but Did Not Make Any Transactions](https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/description)
```sql
SELECT v.customer_id, COUNT(v.visit_id) AS count_no_trans
FROM Visits v 
LEFT JOIN Transactions t ON v.visit_id = t.visit_id
WHERE t.transaction_id IS NULL
GROUP BY v.customer_id;
```

- [197. Rising Temperature](https://leetcode.com/problems/rising-temperature/description)
```sql
SELECT w1.id
FROM Weather w1
INNER JOIN Weather w2 ON w1.recordDate = w2.recordDate + INTERVAL 1 DAY
WHERE w1.temperature > w2.temperature;
```

- [1661. Average Time of Process per Machine](https://leetcode.com/problems/average-time-of-process-per-machine/description)
```sql
SELECT a.machine_id, ROUND(AVG(a2.timestamp  - a.timestamp),3) AS processing_time
FROM Activity a 
INNER JOIN Activity a2 ON a.machine_id = a2.machine_id AND a.process_id = a2.process_id
WHERE a.activity_type = 'start' AND a2.activity_type = 'end'
GROUP BY a.machine_id;

SELECT a.machine_id, ROUND(AVG(a2.timestamp  - a.timestamp),3) AS processing_time
FROM Activity a ,
Activity a2
WHERE a.machine_id = a2.machine_id 
AND a.process_id = a2.process_id
AND a.activity_type = 'start' 
AND a2.activity_type = 'end'	
GROUP BY a.machine_id;
```

- [577. Employee Bonus](https://leetcode.com/problems/employee-bonus/description)
```sql
SELECT e.name, b.bonus
FROM Employee e
LEFT JOIN Bonus b ON e.empId = b.empId
WHERE b.bonus < 1000 OR b.bonus IS NULL;
```

- [1280. Students and Examinations](https://leetcode.com/problems/students-and-examinations/description/)
```sql
SELECT s.student_id, s.student_name, su.subject_name, COUNT(e.student_id) AS attended_exams
FROM Students s
CROSS JOIN Subjects su
LEFT JOIN Examinations e ON su.subject_name = e.subject_name AND s.student_id = e.student_id
GROUP BY s.student_id, su.subject_name
ORDER BY s.student_id, su.subject_name;
```

- []()
```sql

```

- []()
```sql

```

## Basic Aggregate Functions
- []()
```sql

```

- []()
```sql

```

- []()
```sql

```

- []()
```sql

```

- []()
```sql

```

- []()
```sql

```