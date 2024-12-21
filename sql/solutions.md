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

- [570. Managers with at Least 5 Direct Reports](https://leetcode.com/problems/managers-with-at-least-5-direct-reports/description)
```sql
SELECT manager.name
FROM Employee emp
LEFT JOIN Employee manager ON emp.managerId = manager.id
GROUP BY manager.id
HAVING COUNT(manager.id) >= 5;
```

- [1934. Confirmation Rate](https://leetcode.com/problems/confirmation-rate/description/)
```sql
SELECT s.user_id, ROUND(AVG(IF(c.action='confirmed',1,0)),2) AS confirmation_rate
FROM Signups s
LEFT JOIN Confirmations c ON s.user_id = c.user_id
GROUP BY s.user_id;

SELECT t1.user_id, COALESCE(ROUND(t2.confirmed / t1.total,2), 0) AS confirmation_rate
FROM 
(
    SELECT s.user_id, COUNT(c.user_id) AS total
    FROM Signups s LEFT JOIN Confirmations c ON s.user_id = c.user_id
    GROUP BY s.user_id
) t1
LEFT JOIN
(
    SELECT s.user_id, COUNT(c.user_id) AS confirmed
    FROM Signups s LEFT JOIN Confirmations c ON s.user_id = c.user_id
    WHERE c.action = 'confirmed'
    GROUP BY s.user_id
) t2 ON t1.user_id = t2.user_id;
```

## Basic Aggregate Functions
- [620. Not Boring Movies](https://leetcode.com/problems/not-boring-movies/description)
```sql
SELECT c.id, c.movie, c.description, c.rating
FROM Cinema c
WHERE c.description != 'boring' 
AND c.id % 2 != 0
ORDER BY c.rating DESC;
```

- [1251. Average Selling Price](https://leetcode.com/problems/average-selling-price/description)
```sql
SELECT p.product_id,
    COALESCE(ROUND(SUM(p.price*u.units)/SUM(u.units),2),0) AS average_price
FROM Prices p
LEFT JOIN UnitsSold u ON p.product_id = u.product_id AND u.purchase_date BETWEEN p.start_date AND p.end_date
GROUP BY p.product_id;
```

- [1075. Project Employees I](https://leetcode.com/problems/project-employees-i/description)
```sql
SELECT p.project_id, ROUND(AVG(e.experience_years),2) AS average_years
FROM Project p
INNER JOIN Employee e ON p.employee_id = e.employee_id
GROUP BY p.project_id;

SELECT p.project_id, ROUND(SUM(e.experience_years) / COUNT(e.employee_id),2) AS average_years
FROM Project p
INNER JOIN Employee e ON p.employee_id = e.employee_id
GROUP BY p.project_id;
```

- [1633. Percentage of Users Attended a Contest](https://leetcode.com/problems/percentage-of-users-attended-a-contest/description)
```sql
SELECT r.contest_id, ROUND(COUNT(r.user_id)/(SELECT COUNT(u.user_id) FROM Users u),4)*100 AS percentage
FROM Register r
GROUP BY r.contest_id
ORDER BY percentage DESC,
r.contest_id ASC;
```

- [1211. Queries Quality and Percentage](https://leetcode.com/problems/queries-quality-and-percentage/description/)
```sql
SELECT q.query_name,
    ROUND(SUM(q.rating/position) / COUNT(q.query_name),2) AS quality,
    ROUND(SUM(CASE WHEN rating<3 THEN 1 ELSE 0 END) / COUNT(q.query_name),4)*100 AS poor_query_percentage
FROM Queries q
GROUP BY q.query_name;
```

- [1193. Monthly Transactions I](https://leetcode.com/problems/monthly-transactions-i/description/)
```sql
SELECT LEFT(t.trans_date,7) AS month,
    t.country,
    COUNT(t.id) AS trans_count,
    SUM(state = 'approved') AS approved_count,
    SUM(amount) AS trans_total_amount,
    SUM((state='approved')*amount) AS approved_total_amount
FROM Transactions t
GROUP BY month, t.country;
```

- [1174. Immediate Food Delivery II](https://leetcode.com/problems/immediate-food-delivery-ii/description/)
```sql
SELECT ROUND(AVG(d.order_date = d.customer_pref_delivery_date),4)*100 as immediate_percentage
FROM Delivery d
WHERE (d.customer_id, d.order_date) IN(
    SELECT d.customer_id, MIN(d.order_date) AS first
    FROM Delivery d
    GROUP BY d.customer_id
);
```

- [550. Game Play Analysis IV](https://leetcode.com/problems/game-play-analysis-iv/description)
```sql
SELECT ROUND(COUNT(a.player_id)/(SELECT COUNT(DISTINCT player_id) FROM Activity),2) AS fraction
FROM Activity a
WHERE (a.player_id, a.event_date - INTERVAL 1 DAY) IN (
    SELECT a.player_id, MIN(a.event_date)
    FROM Activity a
    GROUP BY a.player_id
);
```

## Sorting and Grouping
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