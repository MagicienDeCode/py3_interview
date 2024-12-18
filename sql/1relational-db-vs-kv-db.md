# Relational Database
A relational database is a type of database that stores and organizes data in **tables**, which are structured as rows and columns.

- example, users

|  id  |  name | email | sex | phone | age |
|:---:|:---:|:---:|:---:|:---:|:---:|
|1|xiang|magiciendecode@gmail.com|M|0123456789|32|
|2|kate|kate@gmail.com|F|9876543210|18|
|3|kiki|kiki@keoi.com|F|1598746320|21|
|4|lx|lx@gmail.com|F|3652987410|23|

- Primary Key: unique identifier for each row, every table must have one (techinial a table can exist without PK), better in int (could be a composite of two columns).
    1. **unique**
    2. **non NULL**
    3. **immutable**
- Foreign Key: a column in one table that establishes a link to a primary key in another table, creating relationships between tables.
    1. The foreign key value must match a primary key value in the referenced table, or it can be **NULL**

- example, jobs

|  id | company |  job_title | length_of_year | salary | user_id |
|:---:|:---:|:---:|:---:|:---:|:---:|
|1|mb|sde|0.5|1500| 1 |
|2|sp|sde|6.2|3100| 1 |
|3|bb|stage|0.2|0| 3 |

- Why relational database ?
    1. Efficiency: Easy to retrieve and manipulate data with SQL.
    2. Scalability: Handle large datasets effectively. (pandas?)
    3. Flexibility: Allows for changes in the database structure without major disruptions.
    4. Data Integrity: Maintains relationships and prevents invalid data entries.

- When ?
Relational databases are commonly used in applications requiring **structured data**, such as e-commerce systems, customer relationship management (CRM), financial systems, and enterprise resource planning (ERP).

# NoSQL, Not Only SQL