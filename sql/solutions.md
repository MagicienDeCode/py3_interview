# Solutions

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



- []()
```sql

```

- []()
```sql

```

- []()
```sql

```