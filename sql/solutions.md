# [SQL 50](https://leetcode.com/studyplan/top-sql-50/)

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

-- better solution
SELECT m.name
FROM Employee e
INNER JOIN Employee m ON e.managerId = m.id
GROUP BY e.managerId
HAVING COUNT(e.managerId) >= 5;
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
    SELECT d2.customer_id, MIN(d2.order_date) AS first
    FROM Delivery d2
    GROUP BY d2.customer_id
);
```

- [550. Game Play Analysis IV](https://leetcode.com/problems/game-play-analysis-iv/description)
```sql
SELECT ROUND(COUNT(a.player_id)/(SELECT COUNT(DISTINCT player_id) FROM Activity),2) AS fraction
FROM Activity a
WHERE (a.player_id, a.event_date - INTERVAL 1 DAY) IN (
    SELECT a2.player_id, MIN(a2.event_date)
    FROM Activity a2
    GROUP BY a2.player_id
);
```

## Sorting and Grouping
- [2356. Number of Unique Subjects Taught by Each Teacher](https://leetcode.com/problems/number-of-unique-subjects-taught-by-each-teacher/description)
```sql
SELECT t.teacher_id, COUNT(DISTINCT t.subject_id) AS cnt
FROM Teacher t
GROUP BY t.teacher_id;
```

- [1141. User Activity for the Past 30 Days I](https://leetcode.com/problems/user-activity-for-the-past-30-days-i/description)
```sql
SELECT a.activity_date AS day, COUNT(DISTINCT a.user_id) AS active_users
FROM Activity a
WHERE a.activity_date + INTERVAL 30 DAY > '2019_07_27' AND a.activity_date <= '2019_07_27'
GROUP BY a.activity_date;
```

- [1070. Product Sales Analysis III](https://leetcode.com/problems/product-sales-analysis-iii/description)
```sql
SELECT s.product_id, s.year AS first_year, s.quantity, s.price
FROM Sales s
WHERE (s.product_id,s.year) IN (
    SELECT s2.product_id, MIN(s2.year)
    FROM Sales s2
    GROUP BY s2.product_id
);
```

- [596. Classes More Than 5 Students](https://leetcode.com/problems/classes-more-than-5-students/description)
```sql
SELECT c.class
FROM Courses c
GROUP BY c.class
HAVING COUNT(c.student) >= 5;
```

- [1729. Find Followers Count](https://leetcode.com/problems/find-followers-count/description)
```sql
SELECT f.user_id, COUNT(f.follower_id) AS followers_count
FROM Followers f
GROUP BY f.user_id
ORDER BY f.user_id ASC;
```

- [619. Biggest Single Number](https://leetcode.com/problems/biggest-single-number/description)
```sql
SELECT COALESCE((
    SELECT m.num
    FROM MyNumbers m
    GROUP BY m.num
    HAVING COUNT(m.NUM) = 1
    ORDER BY m.num DESC
    LIMIT 1
),NULL) AS num;
```

- [1045. Customers Who Bought All Products](https://leetcode.com/problems/customers-who-bought-all-products/description/)
```sql
SELECT c.customer_id
FROM Customer c
GROUP BY c.customer_id 
HAVING COUNT(DISTINCT c.product_key) = (
    SELECT COUNT(p.product_key)
    FROM Product p
);
```

## Advanced Select and Joins

- [1731. The Number of Employees Which Report to Each Employee](https://leetcode.com/problems/the-number-of-employees-which-report-to-each-employee/description)
```sql
SELECT e.employee_id , e.name, COUNT(e2.employee_id) AS reports_count, ROUND(AVG(e2.age)) AS average_age 
FROM Employees e
INNER JOIN Employees e2 ON e.employee_id = e2.reports_to
GROUP BY e.employee_id
ORDER BY e.employee_id;
```

- [1789. Primary Department for Each Employee](https://leetcode.com/problems/primary-department-for-each-employee/description)
```sql
SELECT e.employee_id, e.department_id
FROM Employee e
GROUP BY e.employee_id
HAVING COUNT(e.department_id) = 1
UNION
SELECT e.employee_id, e.department_id
FROM Employee e
WHERE e.primary_flag = 'Y';
```

- [610. Triangle Judgement](https://leetcode.com/problems/triangle-judgement/description)
```sql
SELECT t.x, t.y, t.z,
    CASE WHEN t.x+t.y > t.z AND t.x+t.z > t.y AND t.z+t.y > t.x THEN 'Yes' ELSE 'No' END AS triangle
FROM Triangle t;
```

- [180. Consecutive Numbers](https://leetcode.com/problems/consecutive-numbers/description)
```sql
SELECT DISTINCT l1.num AS ConsecutiveNums
FROM Logs l1 
INNER JOIN Logs l2 ON l1.id = l2.id - 1 AND l1.num = l2.num
INNER JOIN Logs l3 ON l2.id = l3.id - 1 AND l2.num = l3.num;
```

- [1164. Product Price at a Given Date](https://leetcode.com/problems/product-price-at-a-given-date/description)
```sql
SELECT p.product_id, 10 AS price
FROM Products p
GROUP BY p.product_id
HAVING MIN(p.change_date) > '2019-08-16'
UNION
SELECT p.product_id, p.new_price AS price
FROM Products p
WHERE (p.product_id, p.change_date) IN (
    SELECT p2.product_id, MAX(p2.change_date)
    FROM Products p2
    WHERE p2.change_date <= '2019-08-16'
    GROUP BY p2.product_id
);
```

- Can Skip [1204. Last Person to Fit in the Bus](https://leetcode.com/problems/last-person-to-fit-in-the-bus/description)
```sql
SELECT t.person_name
FROM (
    SELECT 
        q.person_name,
        q.turn,
        SUM(q.weight) OVER (ORDER BY q.turn) AS cumulative_weight
    FROM Queue q
) t
WHERE t.cumulative_weight <= 1000
ORDER BY t.turn DESC
LIMIT 1;

--Alice	1	250
--Alex	2	600
--John Cena	3	1000
--Marie	4	1200
--Bob	5	1375
--Winston	6	1875
```

- [1907. Count Salary Categories](https://leetcode.com/problems/count-salary-categories/description)
```sql
SELECT 'Low Salary' AS category, COUNT(*) AS accounts_count
FROM Accounts a
WHERE a.income < 20000
UNION 
SELECT 'Average Salary' AS category, COUNT(*) AS accounts_count
FROM Accounts a
WHERE a.income BETWEEN 20000 AND 50000
UNION
SELECT 'High Salary' AS category, COUNT(*) AS accounts_count
FROM Accounts a
WHERE a.income > 50000;

-- This solution won't include category with 0 count
SELECT CASE 
        WHEN a.income < 20000 THEN 'Low Salary' 
        WHEN a.income BETWEEN 20000 AND 50000 THEN 'Average Salary'
        WHEN a.income > 50000 THEN 'High Salary'
    END AS category, 
    COUNT(a.account_id) AS accounts_count
FROM Accounts a
GROUP BY category;
```

## Subqueries

- [1978. Employees Whose Manager Left the Company](https://leetcode.com/problems/employees-whose-manager-left-the-company/description)
```sql
SELECT e.employee_id
FROM Employees e
LEFT JOIN Employees m ON e.manager_id = m.employee_id
WHERE m.employee_id IS NULL AND e.salary < 30000 AND e.manager_id IS NOT NULL
ORDER BY e.employee_id;
```

- [626. Exchange Seats](https://leetcode.com/problems/exchange-seats/description/)
```sql
-- odd id to event id + 1
-- event id to odd id - 1
-- max id remain the same
SELECT CASE
    WHEN s.id = (SELECT MAX(id) FROM Seat) AND id%2 = 1 THEN id
    WHEN id%2 = 1 THEN id + 1
    ELSE id - 1
    END AS id,
    student
FROM Seat s
ORDER BY id;
```

- [1341. Movie Rating](https://leetcode.com/problems/movie-rating/description)
```sql
(SELECT u.name AS results
FROM Movies m
INNER JOIN MovieRating mr ON m.movie_id = mr.movie_id
INNER JOIN Users u ON u.user_id = mr.user_id
GROUP BY mr.user_id
ORDER BY COUNT(mr.rating) DESC, u.name
LIMIT 1)
UNION ALL
(SELECT m.title AS results
FROM Movies m
INNER JOIN MovieRating mr ON m.movie_id = mr.movie_id
INNER JOIN Users u ON u.user_id = mr.user_id
WHERE mr.created_at BETWEEN '2020-02-01' AND '2020-02-29'
GROUP BY mr.movie_id
ORDER BY AVG(mr.rating) DESC, m.title
LIMIT 1);
```

- can skip [1321. Restaurant Growth](https://leetcode.com/problems/restaurant-growth/description)
```sql
SELECT c.visited_on,
    SUM(c.amount) OVER (ORDER BY c.visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS amount,
    ROUND(SUM(c.amount) OVER (ORDER BY c.visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW)/7,2) AS average_amount 
FROM (
    SELECT c.visited_on, SUM(c.amount) AS amount
    FROM Customer c
    GROUP BY c.visited_ON
) c
LIMIT 6,20000;
```

- [602. Friend Requests II: Who Has the Most Friends](https://leetcode.com/problems/friend-requests-ii-who-has-the-most-friends/description)
```sql
SELECT t.id, SUM(t.num) AS num
FROM (
    SELECT ra.requester_id AS id, COUNT(ra.accepter_id) AS num
    FROM RequestAccepted ra
    GROUP BY ra.requester_id
    UNION ALL
    SELECT ra.accepter_id AS id, COUNT(ra.requester_id) AS num
    FROM RequestAccepted ra
    GROUP BY ra.accepter_id
) t
GROUP BY t.id
ORDER BY num DESC
LIMIT 1;
```

- [585. Investments in 2016](https://leetcode.com/problems/investments-in-2016/description)
```sql
SELECT ROUND(SUM(i1.tiv_2016),2) AS tiv_2016
FROM Insurance i1
WHERE i1.pid IN(
    SELECT i1.pid 
    FROM Insurance i1
    INNER JOIN Insurance i2 ON i1.tiv_2015 = i2.tiv_2015 AND i1.pid != i2.pid
)
AND i1.pid NOT IN (
    SELECT i1.pid
    FROM Insurance i1
    INNER JOIN Insurance i2 ON i1.lat = i2.lat AND i1.lon = i2.lon
    WHERE i1.pid != i2.pid
);
```

- [185. Department Top Three Salaries](https://leetcode.com/problems/department-top-three-salaries/description)
```sql
SELECT d.name AS 'Department', e1.name AS 'Employee',  e1.salary AS 'Salary' 
FROM Employee e1
INNER JOIN Department d ON e1.departmentId = d.id 
WHERE (
    SELECT COUNT(DISTINCT e2.salary)
    FROM Employee e2
    WHERE e2.salary > e1.salary AND e1.departmentId = e2.departmentId
) < 3;  
```

## Advanced String Functions / Regex / Clause

- [1667. Fix Names in a Table](https://leetcode.com/problems/fix-names-in-a-table/description)
```sql
SELECT u.user_id, CONCAT(UPPER(SUBSTRING(u.name, 1, 1)), LOWER(SUBSTRING(u.name, 2))) AS name
FROM Users u
ORDER BY u.user_id;
```

- [1527. Patients With a Condition](https://leetcode.com/problems/patients-with-a-condition)
```sql
SELECT p.*
FROM Patients p
WHERE p.conditions LIKE '% DIAB1%' OR p.conditions LIKE 'DIAB1%';
```

- [196. Delete Duplicate Emails](https://leetcode.com/problems/delete-duplicate-emails/description)
```sql
DELETE p FROM Person p INNER JOIN Person p2 ON p.email = p2.email AND p.id > p2.id;
```

- [176. Second Highest Salary](https://leetcode.com/problems/second-highest-salary/description)
```sql
SELECT COALESCE(
(
    SELECT DISTINCT e.salary AS SecondHighestSalary
    FROM Employee e
    ORDER BY e.salary DESC
    LIMIT 1 OFFSET 1
),NULL)
AS SecondHighestSalary;
```

- [1484. Group Sold Products By The Date](https://leetcode.com/problems/group-sold-products-by-the-date/description)
```sql
SELECT a.sell_date, COUNT(DISTINCT a.product) AS num_sold,
    GROUP_CONCAT(DISTINCT a.product ORDER BY a.product) AS products
FROM Activities a
GROUP BY a.sell_date
ORDER BY a.sell_date;
```

- [1327. List the Products Ordered in a Period](https://leetcode.com/problems/list-the-products-ordered-in-a-period/description)
```sql
SELECT p.product_name, SUM(o.unit) AS unit
FROM Products p
INNER JOIN Orders o ON p.product_id = o.product_id
WHERE order_date BETWEEN '2020-02-01' AND '2020-02-29'
GROUP BY p.product_id
HAVING SUM(o.unit) >= 100;
```

- [1517. Find Users With Valid E-Mails](https://leetcode.com/problems/find-users-with-valid-e-mails/description)
```sql
SELECT *
FROM Users u
WHERE u.mail REGEXP '^[A-Za-z][A-Za-z0-9_\.\-]*@leetcode(\\?com)?\\.com$';
```