# Sql Roadmap

## Abs

# ABS

The `ABS()` function in SQL returns the absolute value of a given numeric expression, meaning it converts any negative number to its positive equivalent while leaving positive numbers unchanged. This function is useful when you need to ensure that the result of a calculation or a value stored in a database column is non-negative, such as when calculating distances, differences, or other metrics where only positive values make sense. For example, `SELECT ABS(-5)` would return `5`.

Visit the following resources to learn more:

- [@article@How to compute an absolute value in SQL](https://www.airops.com/sql-guide/how-to-compute-an-absolute-value-in-sql)
- [@article@ABS](https://www.w3schools.com/sql/func_sqlserver_abs.asp)

## Acid

# ACID

ACID are the four properties of relational database systems that help in making sure that we are able to perform the transactions in a reliable manner. It's an acronym which refers to the presence of four properties: atomicity, consistency, isolation and durability

Visit the following resources to learn more:

- [@article@What is ACID Compliant Database?](https://retool.com/blog/whats-an-acid-compliant-database/)
- [@article@What is ACID Compliance?: Atomicity, Consistency, Isolation](https://fauna.com/blog/what-is-acid-compliance-atomicity-consistency-isolation)
- [@video@ACID Explained: Atomic, Consistent, Isolated & Durable](https://www.youtube.com/watch?v=yaQ5YMWkxq4)

## Advanced Functions

# Advanced Functions

Advanced functions in SQL go beyond the basic operations like selecting and filtering data. These functions allow you to perform complex calculations, manipulate strings, work with dates, and analyze data in more sophisticated ways. They help you derive insights, transform data, and create more meaningful reports from your database.

## Advanced Sql

# Advanced SQL Concepts

Advanced SQL concepts encompass a wide range of sophisticated techniques and features that go beyond basic querying and data manipulation. These include complex joins, subqueries, window functions, stored procedures, triggers, and advanced indexing strategies. By mastering these concepts, database professionals can optimize query performance, implement complex business logic, ensure data integrity, and perform advanced data analysis, enabling them to tackle more challenging database management and data processing tasks in large-scale, enterprise-level applications.

## Aggregate Queries

# Aggregate Queries

Aggregate queries in SQL are used to calculate summary values from multiple rows of a table, reducing the data to a single row based on a specific calculation. These calculations provide insights like totals, averages, and counts. Commonly used aggregate functions include `COUNT()` to count rows, `SUM()` to add values, `AVG()` to calculate the average, `MIN()` to find the minimum value, and `MAX()` to find the maximum value within a group of rows.

## Alter Table

# Alter Table

The `ALTER TABLE` statement in SQL is used to modify the structure of an existing table. This includes adding, dropping, or modifying columns, changing the data type of a column, setting default values, and adding or dropping primary or foreign keys.

Visit the following resources to learn more:

- [@article@ALTER TABLE Statement](https://www.techonthenet.com/sql/tables/alter_table.php)
- [@article@ALTER TABLE - PostgreSQL](https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-alter-table/)

## Avg

# AVG

The `AVG()` function in SQL is an aggregate function that calculates the average value of a numeric column. It returns the sum of all the values in the column, divided by the count of those values.

Visit the following resources to learn more:

- [@article@AVG](https://www.sqlshack.com/sql-avg-function-introduction-and-examples/)
- [@article@SQL AVG() Function](https://www.w3schools.com/sql/sql_avg.asp)

## Basic Sql Syntax

# Basic SQL Syntax

Basic SQL syntax consists of straightforward commands that allow users to interact with a relational database. The core commands include `SELECT` for querying data, `INSERT INTO` for adding new records, `UPDATE` for modifying existing data, and `DELETE` for removing records. Queries can be filtered using `WHERE`, sorted with `ORDER BY`, and data from multiple tables can be combined using `JOIN`. These commands form the foundation of SQL, enabling efficient data manipulation and retrieval within a database.

Visit the following resources to learn more:

- [@article@SQL Tutorial - Mode](https://mode.com/sql-tutorial/)
- [@article@SQL Tutorial](https://www.sqltutorial.org/)

## Begin

# BEGIN

`BEGIN` is used in SQL to start a transaction, which is a sequence of one or more SQL operations that are executed as a single unit. A transaction ensures that all operations within it are completed successfully before any changes are committed to the database. If any part of the transaction fails, the `ROLLBACK` command can be used to undo all changes made during the transaction, maintaining the integrity of the database. Once all operations are successfully completed, the `COMMIT` command is used to save the changes. Transactions are crucial for maintaining data consistency and handling errors effectively.

Visit the following resources to learn more:

- [@article@BEGIN...END Statement](https://infocenter.sybase.com/help/index.jsp?topic=/com.sybase.infocenter.dc00801.1510/html/iqrefso/BABFBJAB.htm)
- [@article@SQL 'BEGIN' & 'END' Statements](https://reintech.io/blog/understanding-sql-begin-end-statements-guide)

## Case

# CASE

The CASE statement in SQL is used to create conditional logic within a query, allowing you to perform different actions based on specific conditions. It operates like an if-else statement, returning different values depending on the outcome of each condition. The syntax typically involves specifying one or more WHEN conditions, followed by the result for each condition, and an optional ELSE clause for a default outcome if none of the conditions are met.

Visit the following resources to learn more:

- [@article@SQL CASE - Intermediate SQL](https://mode.com/sql-tutorial/sql-case)

## Ceiling

# CEILING

The `CEILING()` function in SQL returns the smallest integer greater than or equal to a given numeric value. It's useful when you need to round up a number to the nearest whole number, regardless of whether the number is already an integer or a decimal. For example, `CEILING(4.2)` would return `5`, and `CEILING(-4.7)` would return `-4`. This function is commonly used in scenarios where rounding up is necessary, such as calculating the number of pages needed to display a certain number of items when each page has a fixed capacity.

Visit the following resources to learn more:

- [@article@SQL CEILING](https://www.w3schools.com/sql/func_sqlserver_ceiling.asp)

## Check

# CHECK

A `CHECK` constraint in SQL is used to enforce data integrity by specifying a condition that must be true for each row in a table. It allows you to define custom rules or restrictions on the values that can be inserted or updated in one or more columns. `CHECK` constraints help maintain data quality by preventing invalid or inconsistent data from being added to the database, ensuring that only data meeting specified criteria is accepted.

Visit the following resources to learn more:

- [@video@CHECK Constraint](https://www.youtube.com/watch?v=EeG2boJCXbc)

## Coalesce

# COALESCE

`COALESCE` is an SQL function that returns the first non-null value in a list of expressions. It's commonly used to handle null values or provide default values in queries. `COALESCE` evaluates its arguments in order and returns the first non-null result, making it useful for data cleaning, report generation, and simplifying complex conditional logic in SQL statements.

Visit the following resources to learn more:

- [@article@How to use the COALESCE function in SQL](https://learnsql.com/blog/coalesce-function-sql/)
- [@article@COALESCE - PostgreSQL](https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-coalesce/)

## Column

# Column

In SQL, columns are used to categorize the data in a table. A column serves as a structure that stores a specific type of data (ints, str, bool, etc.) in a table. Each column in a table is designed with a type, which configures the data that it can hold. Using the right column types and size can help to maintain data integrity and optimize performance.

Visit the following resources to learn more:

- [@article@Column Types - PostgreSQL](https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-data-types/)

## Commit

# COMMIT

COMMIT is an SQL command that saves all changes made during a transaction to the database. Until a COMMIT command is issued, all modifications within a transaction are only temporary and visible to the current session. Once COMMIT is executed, the changes become permanent and visible to other users and sessions. This ensures data consistency and durability.

Visit the following resources to learn more:

- [@article@SQL COMMIT and ROLLBACK](https://www.digitalocean.com/community/tutorials/sql-commit-sql-rollback)

## Common Table Expressions

# CTEs (Common Table Expressions)

Common Table Expressions (CTEs) in SQL are named temporary result sets that exist within the scope of a single `SELECT`, `INSERT`, `UPDATE`, `DELETE`, or `MERGE` statement. Defined using the `WITH` clause, CTEs act like virtual tables that can be referenced multiple times within a query. They improve query readability, simplify complex queries by breaking them into manageable parts, and allow for recursive queries. CTEs are particularly useful for hierarchical or graph-like data structures and can enhance query performance in some database systems.

Visit the following resources to learn more:

- [@article@Common Table Expressions (CTEs)](https://hightouch.com/sql-dictionary/sql-common-table-expression-cte)
- [@article@What is a Common Table Expression?](https://learnsql.com/blog/what-is-common-table-expression/)

## Concat

# CONCAT

`CONCAT` is an SQL function used to combine two or more strings into a single string. It takes multiple input strings as arguments and returns a new string that is the concatenation of all the input strings in the order they were provided. `CONCAT` is commonly used in `SELECT` statements to merge data from multiple columns, create custom output formats, or generate dynamic SQL statements.

Visit the following resources to learn more:

- [@article@An overview of the CONCAT function in SQL](https://www.sqlshack.com/an-overview-of-the-concat-function-in-sql-with-examples/)

## Correlated Subqueries

# Correlated Subqueries

In SQL, a correlated subquery is a subquery that uses values from the outer query in its `WHERE` clause. The correlated subquery is evaluated once for each row processed by the outer query. It exists because it depends on the outer query and it cannot execute independently of the outer query because the subquery is correlated with the outer query as it uses its column in its `WHERE` clause.

Visit the following resources to learn more:

- [@official@Correlated Subqueries](https://dev.mysql.com/doc/refman/8.4/en/correlated-subqueries.html)
- [@video@Intro To Subqueries](https://www.youtube.com/watch?v=TUxadt94L0M)

## Count

# COUNT

`COUNT` is an SQL aggregate function that returns the number of rows that match the specified criteria. It can be used to count all rows in a table, non-null values in a specific column, or rows that meet certain conditions when combined with a `WHERE` clause. `COUNT` is often used in data analysis, reporting, and performance optimization queries to determine the size of datasets or the frequency of particular values.

Visit the following resources to learn more:

- [@article@COUNT SQL Function](https://www.datacamp.com/tutorial/count-sql-function)

## Create Table

# Create Table

`CREATE TABLE` is an SQL statement used to define and create a new table in a database. It specifies the table name, column names, data types, and optional constraints such as primary keys, foreign keys, and default values. This statement establishes the structure of the table, defining how data will be stored and organized within it. `CREATE TABLE` is a fundamental command in database management, essential for setting up the schema of a database and preparing it to store data.

Visit the following resources to learn more:

- [@article@CREATE TABLE](https://www.tutorialspoint.com/sql/sql-create-table.htm)
- [@article@SQL CREATE TABLE](https://www.programiz.com/sql/create-table)

## Creating Views

# Creating Views

Creating views in SQL involves using the `CREATE VIEW` statement to define a virtual table based on the result of a `SELECT` query. Views don't store data themselves but provide a way to present data from one or more tables in a specific format. They can simplify complex queries, enhance data security by restricting access to underlying tables, and provide a consistent interface for querying frequently used data combinations. Views can be queried like regular tables and are often used to encapsulate business logic or present data in a more user-friendly manner.

Visit the following resources to learn more:

- [@article@How to create a view in SQL](https://www.sqlshack.com/how-to-create-a-view-in-sql-server/)
- [@video@SQL Views in 4 minutes](https://www.youtube.com/watch?v=vLLkNI-vkV8)

## Cross Join

# Cross Join

A Cross Join produces a result set that is the number of rows in the first table multiplied by the number of rows in the second table. If a WHERE clause is used in conjunction with a CROSS JOIN, it functions like an INNER JOIN. However, using an INNER JOIN is generally preferred to using a CROSS JOIN with a WHERE clause for readability and performance reasons. It essentially creates all possible combinations of rows from the tables involved.

Visit the following resources to learn more:

- [@article@SQL CROSS JOIN With Examples](https://www.sqlshack.com/sql-cross-join-with-examples/)

## Data Constraints

# Data Constraints

Data constraints in SQL are rules applied to columns or tables to enforce data integrity and consistency. They include primary key, foreign key, unique, check, and not null constraints. These constraints define limitations on the data that can be inserted, updated, or deleted in a database, ensuring that the data meets specific criteria and maintains relationships between tables. By implementing data constraints, database designers can prevent invalid data entry, maintain referential integrity, and enforce business rules directly at the database level.

Visit the following resources to learn more:

- [@article@SQL Constraints](https://www.programiz.com/sql/constraints)

## Data Definition Language Ddl

# Data Definition Language (DDL)

Data Definition Language (DDL) is a subset of SQL used to define and manage the structure of database objects. DDL commands include `CREATE`, `ALTER`, `DROP`, and `TRUNCATE`, which are used to create, modify, delete, and empty database structures such as tables, indexes, views, and schemas. These commands allow database administrators and developers to define the database schema, set up relationships between tables, and manage the overall structure of the database. DDL statements typically result in immediate changes to the database structure and can affect existing data.

Visit the following resources to learn more:

- [@article@Data Definition Language (DDL)](https://docs.getdbt.com/terms/ddl)
- [@article@The Definitive Guide on Data Definition Language](https://www.dbvis.com/thetable/sql-ddl-the-definitive-guide-on-data-definition-language/)

## Data Integrity  Security

# Data Integrity & Security

Data integrity ensures that the information stored in a database is accurate, consistent, and reliable over its entire lifecycle. Data security involves protecting the database from unauthorized access, modification, or deletion. These two concepts are essential for maintaining the trust and value of any database system, safeguarding against corruption, breaches, and ensuring data is used appropriately.

## Data Integrity Constraints

# Data Integrity Constraints

Data integrity constraints are rules you set up in a database to make sure the data is accurate and reliable. These rules prevent bad data from being entered into tables. Think of them as checks and balances that maintain the quality of your information by enforcing specific criteria like uniqueness, valid ranges, or required values.

Visit the following resources to learn more:

- [@article@Integrity Constraints in SQL: A Guide With Examples](https://www.datacamp.com/tutorial/integrity-constraints-sql)
- [@article@Integrity Constraints](https://dataheadhunters.com/academy/integrity-constraints-ensuring-accuracy-and-consistency-in-your-data/)

## Data Manipulation Language Dml

# Data Manipulation Language (DML)

Data Manipulation Language (DML) is a subset of SQL used to manage data within database objects. It includes commands like `SELECT`, `INSERT`, `UPDATE`, and `DELETE`, which allow users to retrieve, add, modify, and remove data from tables. DML statements operate on the data itself rather than the database structure, enabling users to interact with the stored information. These commands are essential for day-to-day database operations, data analysis, and maintaining the accuracy and relevance of the data within a database system.

Visit the following resources to learn more:

- [@article@What is DML?](https://satoricyber.com/glossary/dml-data-manipulation-language)
- [@article@What is DML?(Wiki)](https://en.wikipedia.org/wiki/Data_manipulation_language)
- [@article@Difference Between DDL & DML](https://appmaster.io/blog/difference-between-ddl-and-dml)

## Data Types

# Data Types

SQL data types define the kind of values that can be stored in a column and determine how the data is stored, processed, and retrieved. Common data types include numeric types (`INTEGER`, `DECIMAL`), character types (`CHAR`, `VARCHAR`), date and time types (`DATE`, `TIMESTAMP`), binary types (`BLOB`), and boolean types. Each database management system may have its own specific set of data types with slight variations. Choosing the appropriate data type for each column is crucial for optimizing storage, ensuring data integrity, and improving query performance.

Visit the following resources to learn more:

- [@article@SQL Data Types](https://www.digitalocean.com/community/tutorials/sql-data-types)
- [@video@MySQL 101 - Data Types](https://www.youtube.com/watch?v=vAiBa69YCnk)

## Date

# DATE

The DATE data type in SQL is used to store calendar dates (typically in the format YYYY-MM-DD). It represents a specific day without any time information. DATE columns are commonly used for storing birthdates, event dates, or any other data that requires only day-level precision. SQL provides various functions to manipulate and format DATE values, allowing for date arithmetic, extraction of date components, and comparison between dates. The exact range of valid dates may vary depending on the specific database management system being used.

Visit the following resources to learn more:

- [@video@Working with Dates](https://www.youtube.com/watch?v=XyZ9HwXoR7o)

## Dateadd

# DATEADD

`DATEADD` is an SQL function used to add or subtract a specified time interval to a date or datetime value. It typically takes three arguments: the interval type (e.g., day, month, year), the number of intervals to add or subtract, and the date to modify. This function is useful for date calculations, such as finding future or past dates, calculating durations, or generating date ranges. The exact syntax and name of this function may vary slightly between different database management systems (e.g., `DATEADD` in SQL Server, `DATE_ADD` in MySQL).

Visit the following resources to learn more:

- [@article@DATEADD](https://www.mssqltips.com/sqlservertutorial/9380/sql-dateadd-function/)
- [@video@DATEADD Function](https://www.youtube.com/watch?v=DYCWOzzOycU)

## Datepart

# DATEPART

`DATEPART` is a useful function in SQL that allows you to extract a specific part of a date or time field. You can use it to get the year, quarter, month, day of the year, day, week, weekday, hour, minute, second, or millisecond from any date or time expression.

Visit the following resources to learn more:

- [@article@SQL DATEPART](https://hightouch.com/sql-dictionary/sql-datepart)

## Db Security Best Practices

# DB Security Best Practices

Database security best practices are a collection of methods used to protect sensitive data from unauthorized access, modification, or deletion. They involve implementing access controls based on the least privilege principle, routinely updating systems, using strong passwords, limiting remote access, avoiding the admin account for everyday tasks, encrypting communication, performing regular backups, monitoring and auditing database operations, performing vulnerability scanning, and guarding against SQL injection attacks by using parameterized queries or prepared statements.

Visit the following resources to learn more:

- [@article@What is database security?](https://azure.microsoft.com/en-us/resources/cloud-computing-dictionary/what-is-database-security)

## Delete

# DELETE Statement

The DELETE statement removes rows from a table. You specify which table to remove data from and can use a WHERE clause to filter which rows should be deleted based on specific conditions. If no WHERE clause is provided, all rows in the table will be deleted.

Visit the following resources to learn more:

- [@article@DELETE](https://www.w3schools.com/sql/sql_delete.asp)

## Delete

# DELETE Statement in SQL

The `DELETE` statement in SQL removes existing records from a table. You specify which table to affect and can optionally include a `WHERE` clause to specify conditions for which rows should be deleted. If no `WHERE` clause is provided, all rows in the table will be deleted. It modifies the data within the database by removing entire rows based on the given criteria.

Visit the following resources to learn more:

- [@article@DELETE](https://www.w3schools.com/sql/sql_delete.asp)

## Dense Rank

# dense_rank

`dense_rank` is a window function that assigns a rank to each row within a partition of a result set, based on the order of rows. Unlike the `rank` function, `dense_rank` assigns consecutive ranks without gaps, even when there are ties in the ordering criteria. This means that if two or more rows have the same value for the ordering column(s), they will receive the same rank, and the next rank assigned will be the next consecutive integer, without skipping any numbers.

Visit the following resources to learn more:

- [@article@SQL DENSE_RANK](https://www.sqltutorial.org/sql-window-functions/sql-dense_rank/)
- [@article@Breaking Down DENSE_RANK](https://www.kdnuggets.com/breaking-down-denserank-a-step-by-step-guide-for-sql-enthusiasts)

## Drop Table

# Drop Table

The `DROP TABLE` statement removes a table and its data entirely from a database. It's a permanent operation; once a table is dropped, its structure and all the data it contained are lost unless you have a backup. This command should be used with caution, as it can have significant consequences for your database.

Visit the following resources to learn more:

- [@article@Drop a Table](https://www.coginiti.co/tutorials/beginner/drop-a-table/)

## Dropping Views

# Dropping Views

Dropping views in SQL involves using the `DROP VIEW` statement to remove an existing view from the database. This operation permanently deletes the view definition, but it doesn't affect the underlying tables from which the view was created. Dropping a view is typically done when the view is no longer needed, needs to be replaced with a different definition, or as part of database maintenance. It's important to note that dropping a view can impact other database objects or applications that depend on it, so caution should be exercised when performing this operation.

Visit the following resources to learn more:

- [@article@DROP VIEW](https://study.com/academy/lesson/sql-drop-view-tutorial-overview.html)
- [@article@DROP or DELETE a View](https://www.tutorialspoint.com/sql/sql-drop-view.htm)

## Dynamic Sql

# Dynamic SQL

Dynamic SQL refers to the ability to construct and execute SQL statements programmatically during runtime. Instead of writing static SQL queries directly into your code, you can build SQL strings based on varying conditions, user inputs, or other dynamic factors. This allows for more flexible and adaptable database interactions, enabling you to generate queries tailored to specific situations that cannot be known in advance.

Visit the following resources to learn more:

- [@article@Dynamic SQL in SQL Server](https://www.sqlshack.com/dynamic-sql-in-sql-server/)
- [@video@Dynamic SQL](https://www.youtube.com/watch?v=01LZMCotcpY)

## Floor

# FLOOR

FLOOR is a numeric function that returns the largest integer value that is less than or equal to a given number. Effectively, it rounds a number *down* to the nearest whole number. For instance, FLOOR(7.9) would return 7, and FLOOR(-7.1) would return -8.

Visit the following resources to learn more:

- [@video@How to Round in SQL](https://www.youtube.com/watch?v=AUXw2JRwCFY)

## Foreign Key

# Foreign Key

A foreign key in SQL is a column or group of columns in one table that refers to the primary key of another table. It establishes a link between two tables, enforcing referential integrity and maintaining relationships between related data. Foreign keys ensure that values in the referencing table correspond to valid values in the referenced table, preventing orphaned records and maintaining data consistency across tables. They are crucial for implementing relational database designs and supporting complex queries that join multiple tables.

Visit the following resources to learn more:

- [@article@What is a foreign key?](https://www.cockroachlabs.com/blog/what-is-a-foreign-key/)
- [@video@Foreign Keys are easy (kind of)](https://www.youtube.com/watch?v=rFssfx37UJw)

## From

# FROM Clause in SELECT Statements

The `FROM` clause in SQL specifies the table or tables from which you're retrieving data. It tells the database which dataset to look at when executing your query. Without a `FROM` clause, the database doesn't know where the data is coming from, and the `SELECT` statement wouldn't be able to produce any results. Essentially, it's the foundation upon which you build your data retrieval process.

Visit the following resources to learn more:

- [@video@How to write basic SQL](https://www.youtube.com/watch?v=YfTDBA45PHk)

## Full Outer Join

# FULL OUTER JOIN

A `FULL OUTER JOIN` in SQL combines the results of both `LEFT` and `RIGHT OUTER JOIN`s. It returns all rows from both tables, matching records where the join condition is met and including unmatched rows from both tables with `NULL` values in place of missing data. This join type is useful when you need to see all data from both tables, regardless of whether there are matching rows, and is particularly valuable for identifying missing relationships or performing data reconciliation between two tables.

Visit the following resources to learn more:

- [@video@SQL FULL OUTER JOIN](https://www.youtube.com/watch?v=XpBkXo3DCEg)

## Grant And Revoke

# GRANT and REVOKE

`GRANT` and `REVOKE` are SQL commands used to manage user permissions in a database. `GRANT` is used to give specific privileges (such as `SELECT`, `INSERT`, `UPDATE`, `DELETE`) on database objects to users or roles, while `REVOKE` is used to remove these privileges. These commands are essential for implementing database security, controlling access to sensitive data, and ensuring that users have appropriate permissions for their roles. By using `GRANT` and `REVOKE`, database administrators can fine-tune access control, adhering to the principle of least privilege in database management.

Visit the following resources to learn more:

- [@article@GRANT](https://www.ibm.com/docs/en/qmf/12.2.0?topic=privileges-sql-grant-statement)
- [@article@REVOKE](https://www.ibm.com/docs/en/qmf/12.2.0?topic=privileges-sql-revoke-statement)

## Group By

# GROUP BY

`GROUP BY` is an SQL clause used in `SELECT` statements to arrange identical data into groups. It's typically used with aggregate functions (like `COUNT`, `SUM`, `AVG`) to perform calculations on each group of rows. `GROUP BY` collects data across multiple records and groups the results by one or more columns, allowing for analysis of data at a higher level of granularity. This clause is fundamental for generating summary reports, performing data analysis, and creating meaningful aggregations of data in relational databases.

Visit the following resources to learn more:

- [@article@SQL GROUP BY](https://www.programiz.com/sql/group-by)
- [@video@Advanced Aggregate Functions in SQL](https://www.youtube.com/watch?v=nNrgRVIzeHg)

## Group By

# GROUP BY

`GROUP BY` is an SQL clause used in `SELECT` statements to arrange identical data into groups. It's typically used with aggregate functions (like `COUNT`, `SUM`, `AVG`) to perform calculations on each group of rows. `GROUP BY` collects data across multiple records and groups the results by one or more columns, allowing for analysis of data at a higher level of granularity. This clause is fundamental for generating summary reports, performing data analysis, and creating meaningful aggregations of data in relational databases.

Visit the following resources to learn more:

- [@article@SQL GROUP BY](https://www.programiz.com/sql/group-by)
- [@video@Advanced Aggregate Functions in SQL](https://www.youtube.com/watch?v=nNrgRVIzeHg)

## Having

# HAVING

The `HAVING` clause in SQL is used to filter the results of aggregate functions. It's similar to the `WHERE` clause, but operates on grouped rows produced by the `GROUP BY` clause. Essentially, `HAVING` allows you to specify conditions that groups must meet to be included in the final result set after aggregation has taken place.

Visit the following resources to learn more:

- [@article@SQL HAVING Clause](https://www.programiz.com/sql/having)
- [@video@HAVING Clause](https://www.youtube.com/watch?v=tYBOMw7Ob8E)

## Having

# HAVING

HAVING is a clause in SQL that filters the results of a `GROUP BY` query. It's like a `WHERE` clause, but it operates on groups rather than individual rows. You use `HAVING` to specify conditions that the group must meet to be included in the final result set.

Visit the following resources to learn more:

- [@article@SQL HAVING Clause](https://www.programiz.com/sql/having)
- [@video@HAVING Clause](https://www.youtube.com/watch?v=tYBOMw7Ob8E)

## Indexes

# Indexes

Indexes in SQL are database objects that improve the speed of data retrieval operations on database tables. They work similarly to book indexes, providing a quick lookup mechanism for finding rows with specific column values. Indexes create a separate data structure that allows the database engine to locate data without scanning the entire table. While they speed up `SELECT` queries, indexes can slow down `INSERT`, `UPDATE`, and `DELETE` operations because the index structure must be updated. Proper index design is crucial for optimizing database performance, especially for large tables or frequently queried columns.

Visit the following resources to learn more:

- [@video@SQL Indexing Best Practices](https://www.youtube.com/watch?v=BIlFTFrEFOI)

## Inner Join

# INNER JOIN

INNER JOINs combine rows from two or more tables based on a related column.  They return only the rows where there is a match in the specified columns of all tables involved in the join. If there's no matching value in the joined columns, that row is excluded from the result set.

Visit the following resources to learn more:

- [@article@SQL INNER JOIN Clause](https://www.programiz.com/sql/inner-join)

## Insert

# INSERT

INSERT is a SQL command used to add new rows of data into a table. It specifies which table to add the data to and provides the values for each column in the new row. You can insert a single row at a time or multiple rows with a single statement.

Visit the following resources to learn more:

- [@video@SQL INSERT Statement](https://www.youtube.com/watch?v=Yp1MKeIG-M4)

## Insert

# INSERT Statement

The INSERT statement in SQL is used to add new rows of data into a table. It specifies the table to which you want to add data, and the values you want to insert into each column of that table. You can insert a single row at a time or multiple rows in a single statement. It's a fundamental command for populating your database tables with information.

Visit the following resources to learn more:

- [@video@SQL INSERT Statement](https://www.youtube.com/watch?v=Yp1MKeIG-M4)

## Join Queries

# JOIN Queries

JOIN queries are used to combine rows from two or more tables based on a related column between them. This allows you to retrieve data from multiple tables in a single query, forming a more comprehensive dataset than you could get from a single table alone. Different types of joins, like INNER, LEFT, RIGHT, and FULL OUTER, determine how rows are included in the result based on whether matching values exist in the related columns.

Visit the following resources to learn more:

- [@article@7 SQL JOIN Examples With Detailed Explanations](https://learnsql.com/blog/sql-join-examples-with-explanations/)
- [@video@Joins are easy](https://www.youtube.com/watch?v=G3lJAxg1cy8)

## Joins

# JOINs

SQL JOINs let you combine data from two or more tables based on a related column between them.  Think of it as linking information together to get a more complete view. The four most commonly used are: `INNER JOIN`, which returns rows only when there is a match in both tables; `LEFT JOIN`, which returns all rows from the left table and the matched rows from the right table (or NULL if there's no match); `RIGHT JOIN`, which returns all rows from the right table and the matched rows from the left table (or NULL if there's no match); and `FULL OUTER JOIN`, which returns all rows when there is a match in one of the tables.

Visit the following resources to learn more:

- [@article@SQL JOINs Cheat Sheet](https://www.datacamp.com/cheat-sheet/sql-joins-cheat-sheet)
- [@video@SQL JOINs Tutorial for beginners](https://www.youtube.com/watch?v=0OQJDd3QqQM)

## Lag

# lag

`LAG` is a window function in SQL that provides access to a row at a specified offset prior to the current row within a partition. It allows you to compare the current row's values with previous rows' values without using self-joins. LAG is particularly useful for calculating running differences, identifying trends, or comparing sequential data points in time-series analysis. The function takes the column to offset, the number of rows to offset (default is 1), and an optional default value to return when the offset goes beyond the partition's boundary.

Visit the following resources to learn more:

- [@article@Understanding the LAG function in SQL](https://www.datacamp.com/tutorial/sql-lag)
- [@video@LAG and LEAD functions](https://www.youtube.com/watch?v=j2u52RQ0qlw)

## Lead

# lead

`LEAD` is a window function in SQL that provides access to a row at a specified offset after the current row within a partition. It's the counterpart to the `LAG` function, allowing you to look ahead in your dataset rather than behind. `LEAD` is useful for comparing current values with future values, calculating forward-looking metrics, or analyzing trends in sequential data. Like `LAG`, it takes arguments for the column to offset, the number of rows to look ahead (default is 1), and an optional default value when the offset exceeds the partition's boundary.

Visit the following resources to learn more:

- [@article@SQL LEAD](https://www.codecademy.com/resources/docs/sql/window-functions/lead)
- [@video@LAG and LEAD Window Functions in SQL](https://www.youtube.com/watch?v=nHEEyX_yDvo)

## Learn The Basics

# Learn the Basics

SQL (Structured Query Language) is a programming language used to manage and manipulate data stored in relational database management systems (RDBMS). It allows you to retrieve, insert, update, and delete data, as well as define database schemas and control access to data. The basic understanding of SQL is foundational to interact with almost any database.

Visit the following resources to learn more:

- [@article@SQL Tutorial - Mode](https://mode.com/sql-tutorial/)
- [@article@SQL Tutorial](https://www.sqltutorial.org/)

## Left Join

# LEFT JOIN

A LEFT JOIN returns all rows from the left table (the table listed before the `LEFT JOIN` keyword) and the matching rows from the right table (the table listed after the `LEFT JOIN` keyword). If there is no match in the right table for a row in the left table, the result will contain `NULL` values for the columns from the right table. Effectively, it ensures all rows from the left table are included in the result set, regardless of whether there's a corresponding row in the right table.

Visit the following resources to learn more:

- [@video@SQL LEFT JOIN - SQL Tutorial](https://www.youtube.com/watch?v=giKwmtsz1U8)

## Length

# LENGTH

The `LENGTH` function in SQL returns the number of characters in a string. It's used to measure the size of text data, which can be helpful for data validation, formatting, or analysis. In some database systems, `LENGTH` may count characters differently for multi-byte character sets. Most SQL dialects support `LENGTH`, but some may use alternative names like LEN (in SQL Server) or `CHAR_LENGTH`. This function is particularly useful for enforcing character limits, splitting strings, or identifying anomalies in string data.

Visit the following resources to learn more:

- [@article@How to Check the Length of a String in SQL](https://learnsql.com/cookbook/how-to-check-the-length-of-a-string-in-sql/)
- [@article@MySQL Length Function](https://www.w3schools.com/sql/func_mysql_length.asp)

## Lower

# LOWER

The `LOWER` function in SQL converts all characters in a specified string to lowercase. It's a string manipulation function that takes a single argument (the input string) and returns the same string with all alphabetic characters converted to their lowercase equivalents. `LOWER` is useful for standardizing data, making case-insensitive comparisons, or formatting output. It doesn't affect non-alphabetic characters or numbers in the string. `LOWER` is commonly used in data cleaning, search operations, and ensuring consistent data representation across different systems.

Visit the following resources to learn more:

- [@article@How to change text to lowercase in SQL](https://learnsql.com/cookbook/how-to-change-text-to-lowercase-in-sql/)
- [@article@LOWER Function](https://www.w3schools.com/sql/func_sqlserver_lower.asp)

## Managing Indexes

# Managing Indexes

Managing indexes in SQL involves creating, modifying, and dropping indexes to optimize database performance. This process includes identifying columns that benefit from indexing (frequently queried or used in JOIN conditions), creating appropriate index types (e.g., single-column, composite, unique), and regularly analyzing index usage and effectiveness. Database administrators must balance the improved query performance that indexes provide against the overhead they introduce for data modification operations. Proper index management also includes periodic maintenance tasks like rebuilding or reorganizing indexes to maintain their efficiency as data changes over time.

Visit the following resources to learn more:

- [@article@SQL Server Indexes](https://www.sqlservercentral.com/articles/introduction-to-indexes)
- [@article@Optimize index maintenance](https://learn.microsoft.com/en-us/sql/relational-databases/indexes/reorganize-and-rebuild-indexes?view=sql-server-ver16)

## Max

# MAX

`MAX` is an aggregate function in SQL that returns the highest value in a set of values. It can be used with numeric, date, or string data types, selecting the maximum value from a specified column. `MAX` is often used in combination with `GROUP BY` to find the highest value within each group. This function is useful for various data analysis tasks, such as finding the highest salary, the most recent date, or the alphabetically last name in a dataset.

Visit the following resources to learn more:

- [@article@MAX](https://www.techonthenet.com/sql/max.php)
- [@video@Basic Aggregate Functions](https://www.youtube.com/watch?v=jcoJuc5e3RE)

## Min

# MIN

`MIN` is an aggregate function in SQL that returns the lowest value in a set of values. It works with numeric, date, or string data types, selecting the minimum value from a specified column. Often used in conjunction with `GROUP BY`, `MIN` can find the smallest value within each group. This function is useful for various data analysis tasks, such as identifying the lowest price, earliest date, or alphabetically first name in a dataset.

Visit the following resources to learn more:

- [@article@SQL MAX & MIN](https://www.programiz.com/sql/min-and-max)
- [@video@COUNT, SUM, AVG, MIN, MAX (SQL) - Aggregating Data](https://www.youtube.com/watch?v=muwEdPsx534)

## Mod

# MOD

The `MOD` function in SQL calculates the remainder when one number is divided by another. It takes two arguments: the dividend and the divisor. `MOD` returns the remainder of the division operation, which is useful for various mathematical operations, including checking for odd/even numbers, implementing cyclic behaviors, or distributing data evenly. The syntax and exact behavior may vary slightly between different database systems, with some using the % operator instead of the `MOD` keyword.

Visit the following resources to learn more:

- [@video@MOD Function in SQL](https://www.youtube.com/watch?v=f1Rqf7CwjE0)

## Modifying Views

# Modifying Views

Modifying views in SQL allows you to alter the structure or definition of an existing view without having to drop and recreate it. This can involve changing the columns included in the view, updating the underlying tables or conditions used in the view's query, or renaming the view. Using `ALTER VIEW` simplifies maintenance and allows for adjustments to views as database requirements evolve.

Visit the following resources to learn more:

- [@article@Modify Views in SQL Server](https://www.sqlshack.com/create-view-sql-modifying-views-in-sql-server/)
- [@video@SQL VIEWs in 4 Minutes](https://www.youtube.com/watch?v=vLLkNI-vkV8)

## Nested Subqueries

# Nested Subqueries

Nested subqueries are queries embedded within another SQL query. Think of it as a query inside a query, where the inner query's result is used by the outer query. This allows you to perform more complex data retrieval and filtering operations by breaking down a larger problem into smaller, more manageable steps. Essentially, the outer query depends on the result returned by the inner query to complete its own operation.

Visit the following resources to learn more:

- [@article@Nested Subqueries](https://www.studysmarter.co.uk/explanations/computer-science/databases/nested-subqueries-in-sql/)
- [@video@MySQL Subqueries](https://www.youtube.com/watch?v=i5acg3Hvu6g)

## Not Null

# NOT NULL Constraint

The NOT NULL constraint in SQL ensures that a column does not accept null values. When a column is defined with this constraint, every row in the table must have a value for that specific column. Attempting to insert or update a row with a null value in a NOT NULL column will result in an error, maintaining data integrity by preventing missing or undefined entries.

Visit the following resources to learn more:

- [@article@SQL IS NULL and IS NOT NULL](https://www.programiz.com/sql/is-null-not-null)
- [@video@NOT NULL Constraint](https://www.youtube.com/watch?v=unzHhq82mKU)

## Nullif

# NULLIF

`NULLIF` is an SQL function that compares two expressions and returns NULL if they are equal, otherwise it returns the first expression. It's particularly useful for avoiding division by zero errors or for treating specific values as `NULL` in calculations or comparisons. `NULLIF` takes two arguments and is often used in combination with aggregate functions or in `CASE` statements to handle special cases in data processing or reporting.

Visit the following resources to learn more:

- [@video@What is NULLIF in SQL?](https://www.youtube.com/watch?v=Jaw53T__RRY)

## Operators

# Operators

SQL operators are symbols or keywords used to perform operations on data within a database. They are essential for constructing queries that filter, compare, and manipulate data. Common types of operators include arithmetic operators (e.g., `+`, `-`, `*`, `/`), which perform mathematical calculations; comparison operators (e.g., `=`, `!=`, `<`, `>`), used to compare values; logical operators (e.g., `AND`, `OR`, `NOT`), which combine multiple conditions in a query; and set operators (e.g., `UNION`, `INTERSECT`, `EXCEPT`), which combine results from multiple queries. These operators enable precise control over data retrieval and modification.

Visit the following resources to learn more:

- [@article@SQL Operators: 6 Different Types](https://dataengineeracademy.com/blog/sql-operators-6-different-types-code-examples/)

## Optimizing Joins

# Optimizing Joins

Optimizing joins in SQL involves techniques to improve the performance of queries that combine data from multiple tables. Key strategies include using appropriate join types (e.g., `INNER JOIN` for matching rows only, `LEFT JOIN` for all rows from one table), indexing the columns used in join conditions to speed up lookups, and minimizing the data processed by filtering results with `WHERE` clauses before the join. Additionally, reducing the number of joins, avoiding unnecessary columns in the `SELECT` statement, and ensuring that the join conditions are based on indexed and selective columns can significantly enhance query efficiency. Proper join order and using database-specific optimization hints are also important for performance tuning.

Visit the following resources to learn more:

- [@article@How to Optimize a SQL Query with Multiple Joins](https://dezbor.com/blog/optimize-sql-query-with-multiple-joins)
- [@video@Secret to optimizing SQL queries](https://www.youtube.com/watch?v=BHwzDmr6d7s)

## Order By

# ORDER BY

The `ORDER BY` clause in SQL is used to sort the result set of a query by one or more columns. By default, the sorting is in ascending order, but you can specify descending order using the `DESC` keyword. The clause can sort by numeric, date, or text values, and multiple columns can be sorted by listing them in the `ORDER BY` clause, each with its own sorting direction. This clause is crucial for organizing data in a meaningful sequence, such as ordering by a timestamp to show the most recent records first, or alphabetically by name.

Visit the following resources to learn more:

- [@video@SQL ORDER BY Sorting Clause](https://www.youtube.com/watch?v=h_HHTNjAgS8)

## Performance Optimization

# Performance Optimization

Performance optimization in SQL focuses on making your queries run faster and more efficiently. This involves techniques like using indexes to speed up data retrieval, rewriting queries for better performance, and understanding how the database engine executes your SQL code. It's about ensuring your database can handle large amounts of data and complex queries without slowing down.

Visit the following resources to learn more:

- [@article@Performance Tuning SQL Queries](https://mode.com/sql-tutorial/sql-performance-tuning)
- [@article@SQL performance tuning](https://stackify.com/performance-tuning-in-sql-server-find-slow-queries/)

## Pivot  Unpivot Operations

# Pivot / Unpivot Operations

Pivot and unpivot operations transform the structure of data within a table. Pivoting rotates rows into columns, aggregating data based on common values. Conversely, unpivoting transforms columns into rows, often expanding a table's length while reducing its width. These operations are useful for reshaping data for reporting or analysis.

Visit the following resources to learn more:

- [@article@SQL PIVOT](https://builtin.com/articles/sql-pivot)
- [@article@SQL UNPIVOT](https://duckdb.org/docs/sql/statements/unpivot.html)

## Primary Key

# Primary Key

A primary key in SQL is a unique identifier for each record in a database table. It ensures that each row in the table is uniquely identifiable, meaning no two rows can have the same primary key value. A primary key is composed of one or more columns, and it must contain unique values without any `NULL` entries. The primary key enforces entity integrity by preventing duplicate records and ensuring that each record can be precisely located and referenced, often through foreign key relationships in other tables. Using a primary key is fundamental for establishing relationships between tables and maintaining the integrity of the data model.

Visit the following resources to learn more:

- [@article@SQL Primary Key](https://www.tutorialspoint.com/sql/sql-primary-key.htm)

## Query Analysis Techniques

# Query Analysis Techniques

Understanding how SQL queries are executed is essential for performance tuning. Tools like `EXPLAIN` or `EXPLAIN PLAN` allow you to dissect the execution plan the database uses for a specific query. This plan reveals the order in which tables are accessed, the types of indexes used (or not used), and the estimated cost of each operation, enabling you to identify bottlenecks and optimize the query for faster execution.

Visit the following resources to learn more:

- [@article@EXPLAIN](https://docs.snowflake.com/en/sql-reference/sql/explain)
- [@article@EXPLAIN PLAN](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/EXPLAIN-PLAN.html)

## Query Optimization

# Query Optimization

Query optimization is the process of selecting the most efficient way to execute a SQL query. It involves the database management system (DBMS) analyzing different possible execution plans for a query and choosing the one that will return the results fastest, using the least amount of resources. This analysis considers factors like the data volume, index usage, and system resources to find the optimal path.

Visit the following resources to learn more:

- [@article@12 Ways to Optimize SQL Queries](https://www.developernation.net/blog/12-ways-to-optimize-sql-queries-in-database-management/)
- [@video@SQL Query Optimization](https://www.youtube.com/watch?v=GA8SaXDLdsY)

## Rank

# rank

The `RANK` function in SQL is a window function that assigns a rank to each row within a partition of a result set, based on the order specified by the `ORDER BY` clause. Unlike the `ROW_NUMBER` function, `RANK` allows for the possibility of ties—rows with equal values in the ordering column(s) receive the same rank, and the next rank is skipped accordingly. For example, if two rows share the same rank of 1, the next rank will be 3. This function is useful for scenarios where you need to identify relative positions within groups, such as ranking employees by salary within each department.

Visit the following resources to learn more:

- [@article@Overview of SQL RANK Functions](https://www.sqlshack.com/overview-of-sql-rank-functions/)
- [@video@RANK, DENSE_RANK, ROW_NUMBER SQL Analytical Functions Simplified](https://www.youtube.com/watch?v=xMWEVFC4FOk)

## Rdbms Benefits And Limitations

# RDBMS Benefits and Limitations

Relational Database Management Systems (RDBMS) organize data into tables with rows and columns, establishing relationships between these tables using keys. This structured approach offers benefits like data integrity through constraints and ACID properties (Atomicity, Consistency, Isolation, Durability), ensuring reliable transactions. However, RDBMS can face limitations regarding scalability, especially with massive datasets, and may not be the optimal choice for handling unstructured or semi-structured data due to their rigid schema.

Visit the following resources to learn more:

- [@article@Advantages and Disadvantages of DBMS](https://cloud.google.com/learn/what-is-a-relational-database)

## Recursive Queries

# Recursive Queries

Recursive queries are SQL queries that refer to themselves within their own definition. They're used to process hierarchical or tree-structured data, where relationships exist between rows in the same table, like organizational charts, bill of materials, or social networks. Using `WITH RECURSIVE` clause, these queries iterate through the data until a certain condition is met, allowing you to traverse the hierarchy and extract related information.

Visit the following resources to learn more:

- [@article@Recursive Queries in SQL](https://codedamn.com/news/sql/recursive-queries-in-sql)
- [@article@Recursive SQL Expression Visually Explained](https://builtin.com/data-science/recursive-sql)

## Reducing Subqueries

# Reducing Subqueries

Reducing subqueries is a common SQL optimization technique, especially when dealing with complex logic or large datasets. Correlated subqueries, which are evaluated once for each row in the outer query, can degrade the performance. Subqueries can often be replaced with JOIN operations. In cases where subqueries are reused, consider replacing them with Common Table Expressions (CTEs), which offer modularity and avoid repeated executions of the same logic. Limiting the result set returned by subqueries and storing the results of expensive subqueries in temporary tables for reuse can also improve performance.

Learn more from the following resources:

## Replace

# REPLACE

The `REPLACE` function in SQL is used to substitute all occurrences of a specified substring within a string with a new substring. It takes three arguments: the original string, the substring to be replaced, and the substring to replace it with. If the specified substring is found in the original string, `REPLACE` returns the modified string with all instances of the old substring replaced by the new one. If the substring is not found, the original string is returned unchanged. This function is particularly useful for data cleaning tasks, such as correcting typos, standardizing formats, or replacing obsolete data.

Visit the following resources to learn more:

- [@article@How to use the SQL REPLACE Function](https://www.datacamp.com/tutorial/sql-replace)

## Right Join

# RIGHT JOIN

A RIGHT JOIN combines rows from two tables based on a related column. It returns all rows from the right table (the table specified after the `RIGHT JOIN` keyword), and the matching rows from the left table. If there's no match in the left table for a row in the right table, `NULL` values are returned for the columns from the left table in the result set.

Visit the following resources to learn more:

- [@article@SQL RIGHT JOIN With Examples](https://www.programiz.com/sql/right-join)

## Rollback

# ROLLBACK

`ROLLBACK` is a SQL command used to undo transactions that have not yet been committed to the database. It reverses all changes made within the current transaction, restoring the database to its state before the transaction began. This command is crucial for maintaining data integrity, especially when errors occur during a transaction or when implementing conditional logic in database operations. `ROLLBACK` is an essential part of the ACID (Atomicity, Consistency, Isolation, Durability) properties of database transactions, ensuring that either all changes in a transaction are applied, or none are, thus preserving data consistency.

Visit the following resources to learn more:

- [@article@Difference between COMMIT and ROLLBACK in SQL](https://byjus.com/gate/difference-between-commit-and-rollback-in-sql/)
- [@video@How to undo a mistake a in SQL: Rollback and Commit](https://www.youtube.com/watch?v=jomsdMLiIZM)

## Round

# ROUND

The `ROUND` function in SQL is used to round a numeric value to a specified number of decimal places. It takes two arguments: the number to be rounded and the number of decimal places to round to. If the second argument is omitted, the function rounds the number to the nearest whole number. For positive values of the second argument, the number is rounded to the specified decimal places; for negative values, it rounds to the nearest ten, hundred, thousand, etc. The `ROUND` function is useful for formatting numerical data for reporting or ensuring consistent precision in calculations.

Visit the following resources to learn more:

- [@article@What is the SQL ROUND Function and how does it work?](https://www.datacamp.com/tutorial/mastering-sql-round)

## Row

# Row

In SQL, a row (also called a record or tuple) represents a single, implicitly structured data item in a table. Each row contains a set of related data elements corresponding to the table's columns. Rows are fundamental to the relational database model, allowing for the organized storage and retrieval of information. Operations like INSERT, UPDATE, and DELETE typically work at the row level.

Visit the following resources to learn more:

- [@article@Row - Database](https://en.wikipedia.org/wiki/Row_(database))
- [@article@Database Row: Definition, Examples](https://www.devx.com/terms/database-row/)

## Row Number

# Row_number

ROW\_NUMBER() is a SQL window function that assigns a unique, sequential integer to each row within a partition of a result set. It's useful for creating row identifiers, implementing pagination, or finding the nth highest/lowest value in a group. The numbering starts at 1 for each partition and continues sequentially, allowing for versatile data analysis and manipulation tasks.

Visit the following resources to learn more:

- [@article@SQL ROW_NUMBER](https://www.sqltutorial.org/sql-window-functions/sql-row_number/)
- [@article@How to Use ROW_NUMBER OVER() in SQL to Rank Data](https://learnsql.com/blog/row-number-over-in-sql/)

## Savepoint

# SAVEPOINT

A `SAVEPOINT` in SQL is a point within a transaction that can be referenced later. It allows for more granular control over transactions by creating intermediate points to which you can roll back without affecting the entire transaction. This is particularly useful in complex transactions where you might want to undo part of the work without discarding all changes. `SAVEPOINT` enhances transaction management flexibility.

Visit the following resources to learn more:

- [@article@SQL SAVEPOINT](https://www.ibm.com/docs/pl/informix-servers/12.10?topic=statements-savepoint-statement)
- [@video@DBMS - Save Point](https://www.youtube.com/watch?v=30ldSUkswGM)

## Scalar

# Scalar

A scalar value is a single data item, as opposed to a set or array of values. Scalar subqueries are queries that return exactly one column and one row, often used in `SELECT` statements, `WHERE` clauses, or as part of expressions. Scalar functions in SQL return a single value based on input parameters. Understanding scalar concepts is crucial for writing efficient and precise SQL queries.

Visit the following resources to learn more:

- [@article@Creating SQL Scalar Functions](https://www.ibm.com/docs/en/db2/11.5?topic=functions-creating-sql-scalar)
- [@video@Using Scalar SQL to boost performance](https://www.youtube.com/watch?v=v8X5FGzzc9A)

## Select

# Select Statement

The `SELECT` statement in SQL is used to retrieve data from one or more tables. It allows you to specify which columns you want to see and apply conditions to filter the rows returned. Think of it as a powerful tool to query a database and extract specific information based on your needs.

## Select

# SELECT statement

SELECT is one of the most fundamental SQL commands, used to retrieve data from one or more tables in a database. It allows you to specify which columns to fetch, apply filtering conditions, sort results, and perform various operations on the data. The SELECT statement is versatile, supporting joins, subqueries, aggregations, and more, making it essential for data querying and analysis in relational databases.

## Selective Projection

# Selective Projection

Selective projection in SQL refers to the practice of choosing only specific columns (attributes) from a table or query result, rather than selecting all available columns. This technique is crucial for optimizing query performance and reducing unnecessary data transfer. By using SELECT with explicitly named columns instead of `SELECT *`, developers can improve query efficiency and clarity, especially when dealing with large tables or complex joins.

## Self Join

# Self Join

A self join is a query in SQL that joins a table to itself. This is useful when you want to compare rows within the same table, often based on a hierarchical relationship or other connection between the data points within that table. Think of it as creating two copies of the same table and then joining them based on a shared column, allowing you to relate data from the same source in a new way.

Visit the following resources to learn more:

- [@article@Understanding the Self Joins in SQL](https://www.dbvis.com/thetable/understanding-self-joins-in-sql/)
- [@article@SQL self joins](https://www.w3schools.com/sql/sql_join_self.asp)

## Sql Keywords

# SQL keywords

SQL keywords are reserved words that have special meanings within SQL statements. These include commands (like `SELECT`, `INSERT`, `UPDATE`), clauses (such as `WHERE`, `GROUP BY`, `HAVING`), and other syntax elements that form the structure of SQL queries. Understanding SQL keywords is fundamental to writing correct and effective database queries. Keywords are typically case-insensitive but are often written in uppercase by convention for better readability.

Visit the following resources to learn more:

- [@article@SQL Keywords, Operators and Statements](https://blog.hubspot.com/website/sql-keywords-operators-statements)

## Sql Vs Nosql Databases

# SQL vs NoSQL

SQL (relational) and NoSQL (non-relational) databases represent two different approaches to data storage and retrieval. SQL databases use structured schemas and tables, emphasizing data integrity and complex queries through joins. NoSQL databases offer more flexibility in data structures, often sacrificing some consistency for scalability and performance. The choice between SQL and NoSQL depends on factors like data structure, scalability needs, consistency requirements, and the nature of the application.

Visit the following resources to learn more:

- [@article@Understanding SQL vs NoSQL Databases](https://www.mongodb.com/resources/basics/databases/nosql-explained/nosql-vs-sql)
- [@video@SQL vs NoSQL Databases in 4 mins](https://www.youtube.com/watch?v=_Ss42Vb1SU4)

## Stored Procedures  Functions

# Stored Procedures and Functions

Stored procedures and functions are precompiled database objects that encapsulate a set of SQL statements and logic. Stored procedures can perform complex operations and are typically used for data manipulation, while functions are designed to compute and return values. Both improve performance by reducing network traffic and allowing code reuse. They also enhance security by providing a layer of abstraction between the application and the database.

Visit the following resources to learn more:

- [@article@Stored Procedure vs Functions](https://www.shiksha.com/online-courses/articles/stored-procedure-vs-function-what-are-the-differences/)

## Subqueries

# Sub Queries

Subqueries, also known as nested queries or inner queries, are SQL queries embedded within another query. They can be used in various parts of SQL statements, such as SELECT, FROM, WHERE, and HAVING clauses. Subqueries allow for complex data retrieval and manipulation by breaking down complex queries into more manageable parts. They're particularly useful for creating dynamic criteria, performing calculations, or comparing sets of results.

Visit the following resources to learn more:

- [@article@SQL Sub Queries](https://www.tutorialspoint.com/sql/sql-sub-queries.htm)
- [@video@Advanced SQL Tutorial | Subqueries](https://www.youtube.com/watch?v=m1KcNV-Zhmc)

## Substring

# SUBSTRING

SUBSTRING is a SQL function used to extract a portion of a string. It allows you to specify the starting position and length of the substring you want to extract. This function is valuable for data manipulation, parsing, and formatting tasks. The exact syntax may vary slightly between database systems, but the core functionality remains consistent, making it a versatile tool for working with string data in databases.

Visit the following resources to learn more:

- [@article@SQL SUBSTRING](https://www.w3schools.com/sql/func_sqlserver_substring.asp)
- [@video@Advanced SQL Tutorial | String Functions + Use Cases](https://www.youtube.com/watch?v=GQj6_6V_jVA)

## Sum

# SUM

SUM is an aggregate function in SQL used to calculate the total of a set of values. It's commonly used with numeric columns in combination with GROUP BY clauses to compute totals for different categories or groups within the data. SUM is essential for financial calculations, statistical analysis, and generating summary reports from database tables. It ignores NULL values and can be used in conjunction with other aggregate functions for complex data analysis.

Visit the following resources to learn more:

- [@article@SQL SUM](https://www.studysmarter.co.uk/explanations/computer-science/databases/sql-sum/)

## Table

# Table

A table is a fundamental structure for organizing data in a relational database. It consists of rows (records) and columns (fields), representing a collection of related data entries. Tables define the schema of the data, including data types and constraints. They are the primary objects for storing and retrieving data in SQL databases, and understanding table structure is crucial for effective database design and querying.

Visit the following resources to learn more:

- [@article@Table (Database)](https://en.wikipedia.org/wiki/Table_(database))
- [@article@Introduction to Tables](https://support.microsoft.com/en-gb/office/introduction-to-tables-78ff21ea-2f76-4fb0-8af6-c318d1ee0ea7)

## Time

# TIME

The TIME data type in SQL is used to store time values, typically in the format of hours, minutes, and seconds. It's useful for recording specific times of day without date information. SQL provides various functions for manipulating and comparing TIME values, allowing for time-based calculations and queries. The exact range and precision of TIME can vary between different database management systems.

Learn more from the following resources:

## Timestamp

# TIMESTAMP

A TIMESTAMP is a data type used to store a specific point in time, typically including both date and time components. It often includes fractions of a second (milliseconds or microseconds) for greater precision. It is very common for databases to have a timestamp that automatically updates when a row is updated.

Visit the following resources to learn more:

- [@article@Different SQL TimeStamp functions in SQL Server](https://www.sqlshack.com/different-sql-timestamp-functions-in-sql-server/)

## Transaction Isolation Levels

# Transaction Isolation Levels

Transaction isolation levels in SQL define the degree to which the operations in one transaction are visible to other concurrent transactions. There are typically four standard levels: Read Uncommitted, Read Committed, Repeatable Read, and Serializable. Each level provides different trade-offs between data consistency and concurrency. Understanding and correctly setting isolation levels is crucial for maintaining data integrity and optimizing performance in multi-user database environments.

Visit the following resources to learn more:

- [@article@Everything you always wanted to know about SQL isolation levels](https://www.cockroachlabs.com/blog/sql-isolation-levels-explained/)
- [@article@Isolation Levels in SQL Server](https://www.sqlservercentral.com/articles/isolation-levels-in-sql-server)

## Transactions

# Transactions

Transactions in SQL are units of work that group one or more database operations into a single, atomic unit. They ensure data integrity by following the ACID properties: Atomicity (all or nothing), Consistency (database remains in a valid state), Isolation (transactions don't interfere with each other), and Durability (committed changes are permanent). Transactions are essential for maintaining data consistency in complex operations and handling concurrent access to the database.

Visit the following resources to learn more:

- [@article@Transactions](https://www.tutorialspoint.com/sql/sql-transactions.htm)
- [@article@A Guide to ACID Properties in Database Management Systems](https://www.mongodb.com/resources/basics/databases/acid-transactions)

## Truncate Table

# Truncate Table

Truncate Table is a command in SQL used to remove all rows from a table.  It's like resetting the table to its initial, empty state.  The table structure itself (columns, data types, constraints) remains intact. `TRUNCATE TABLE` is generally faster than `DELETE` because it deallocates the data pages used by the table, rather than individually logging each row deletion.

Visit the following resources to learn more:

- [@article@TRUNCATE TABLE](https://www.tutorialspoint.com/sql/sql-truncate-table.htm)
- [@video@SQL Tutorial - TRUNCATE TABLE](https://www.youtube.com/watch?v=zJidbjOQlJM)

## Unique

# Unique Constraint

A unique constraint ensures that all values in a column (or a group of columns) are different. It prevents duplicate entries, maintaining data integrity by enforcing uniqueness for the specified field(s). This is useful for fields like email addresses or usernames, where each record should have a distinct value.

Visit the following resources to learn more:

- [@article@SQL UNIQUE Constraint](https://www.w3schools.com/sql/sql_unique.asp)

## Update

# UPDATE Statement

The UPDATE statement modifies existing data within a table. It allows you to change the values of one or more columns in a table, based on specified conditions. You can update a single row or multiple rows, and it's essential for keeping your database information accurate and current.

Visit the following resources to learn more:

- [@article@Efficient column updates in SQL](https://www.atlassian.com/data/sql/how-to-update-a-column-based-on-a-filter-of-another-column)

## Update

# UPDATE Statement

The UPDATE statement modifies existing data within a table. It allows you to change the values of one or more columns for specific rows based on a specified condition. You use the `UPDATE` statement to correct errors, reflect changes in data, or apply new information to your database.

Visit the following resources to learn more:

- [@article@Efficient column updates in SQL](https://www.atlassian.com/data/sql/how-to-update-a-column-based-on-a-filter-of-another-column)

## Upper

# UPPER

UPPER is a string function that transforms all characters in a given string to uppercase. It accepts a single string or character-based column as an argument and returns a new string where every letter has been converted to its uppercase equivalent. Non-alphabetic characters and already uppercase characters remain unchanged.

Visit the following resources to learn more:

- [@article@How to Convert a String to Uppercase in SQL](https://learnsql.com/cookbook/how-to-convert-a-string-to-uppercase-in-sql/)

## Using Indexes

# Using Indexes

Indexes in SQL are database objects that improve the speed of data retrieval operations on database tables. They work similarly to an index in a book, allowing the database engine to quickly locate data without scanning the entire table. Proper use of indexes can significantly enhance query performance, especially for large tables. However, they come with trade-offs: while they speed up reads, they can slow down write operations (INSERT, UPDATE, DELETE) as the index also needs to be updated. Common types include B-tree indexes (default in most systems), bitmap indexes, and full-text indexes. Understanding when and how to create indexes is crucial for database optimization. This involves analyzing query patterns, understanding the data distribution, and balancing the needs of different types of operations on the database.

Visit the following resources to learn more:

- [@article@What is an index in SQL?](https://stackoverflow.com/questions/2955459/what-is-an-index-in-sql)
- [@video@SQL Indexes - Definition, Examples, and Tips](https://www.youtube.com/watch?v=NZgfYbAmge8)

## Views

# Views

Views are like virtual tables. Instead of physically storing data, a view's definition is based on a query against one or more tables. When you query a view, the database executes the underlying query defined in the view, and the results are presented as if they were from an actual table. This simplifies complex queries and provides a level of data abstraction and security.

Visit the following resources to learn more:

- [@article@Views in SQL](https://www.datacamp.com/tutorial/views-in-sql)
- [@video@SQL Views Tutorial](https://www.youtube.com/watch?v=cLSxasHg9WY)

## What Are Relational Databases

# Relational Databases

Relational databases organize data into tables, where each table represents a specific type of entity (like customers or products). These tables are linked together based on relationships between the data, often using shared columns called keys. This structure allows for efficient storage, retrieval, and management of large datasets while ensuring data integrity and consistency.

Visit the following resources to learn more:

- [@article@What is a relational database - AWS](https://aws.amazon.com/relational-database/)
- [@video@What is a relational database?](https://www.youtube.com/watch?v=OqjJjpjDRLc)

## Where

# WHERE Clause in SELECT Statements

The WHERE clause is a fundamental part of the SELECT statement in SQL. It filters the rows returned by a query based on a specified condition.  Essentially, it allows you to retrieve only the data that meets certain criteria, enabling you to focus on specific subsets of information within your database tables.

Visit the following resources to learn more:

- [@article@WHERE Clause](https://www.w3schools.com/sql/sql_where.asp)
- [@video@How to filter with the WHERE clause in SQL](https://www.youtube.com/watch?v=4Uv0o8IBqw0)

## Window Functions

# Window Functions

Window functions perform calculations across a set of rows that are related to the current row. Unlike standard aggregate functions that group rows into a single result row, window functions retain the individual rows and add a calculated value for each row based on the window frame. This allows you to perform analyses like calculating running totals, moving averages, or ranking within partitions of data without collapsing the rows.

Visit the following resources to learn more:

- [@article@SQL Window Functions](https://mode.com/sql-tutorial/sql-window-functions)
- [@video@SQL Window Functions in 10 Minutes](https://www.youtube.com/watch?v=y1KCM8vbYe4)
