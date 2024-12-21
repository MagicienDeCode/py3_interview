# Before Start
- Make sure zoom or goole meet works.
- Create a leetcode account or login with google account.
- Just have fun.
- 恩返しです。

# SQL (Structed Query Language)
- SQL is a standardized programming language used to manage and manipulate relational databases.

# Relational database vs NoSQL
- [README](https://github.com/MagicienDeCode/py3_interview/blob/master/sql/1.0.relational-db-vs-kv-db.md)

# SELECT 
- [template and basice functions](https://github.com/MagicienDeCode/py3_interview/blob/master/sql/2.0.select.md)

- table users

|  id  |  name | email | sex | phone | age |
|:---:|:---:|:---:|:---:|:---:|:---:|
|1|xiang|magiciendecode@gmail.com|M|0123456789|32|
|2|kate|kate@gmail.com|F|9876543210|NULL|
|3|kiki|kiki@keoi.com|F|1598746320|21|
|4|lx|lx@gmail.com|F|3652987410|23|

- table jobs

|  id | company |  job_title | length_of_year | salary | user_id |
|:---:|:---:|:---:|:---:|:---:|:---:|
|1|mb|sde|0.5|1500| 1 |
|2|sp|sde|6.2|3100| 1 |
|3|bb|stage|0.2|0| 3 |

```sql
-- 1. SELECT all users name which length of email greater or equal than 14, return upper case name, example: KIKI
-- 2. SELECT all users name which has age and sex is F, return small case name: example: kiki
-- 3. calculate average age of women, if age is NULL, take default value 18
```
- homework todo, [answer](https://github.com/MagicienDeCode/py3_interview/blob/master/sql/2.1.todo.md)

# Basic Joins
- [README](https://github.com/MagicienDeCode/py3_interview/blob/master/sql/3.0.basic-joins.md)

# Basic Aggregate Functions
- COUNT SUM AVG MIN MAX