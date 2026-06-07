# Postgresql Dba Roadmap

## Acid

# ACID

ACID are the four properties of relational database systems that help in making sure that we are able to perform the transactions in a reliable manner. It's an acronym which refers to the presence of four properties: atomicity, consistency, isolation and durability

Visit the following resources to learn more:

- [@article@What is ACID Compliant Database?](https://retool.com/blog/whats-an-acid-compliant-database/)
- [@article@What is ACID Compliance?: Atomicity, Consistency, Isolation](https://fauna.com/blog/what-is-acid-compliance-atomicity-consistency-isolation)
- [@video@ACID Explained: Atomic, Consistent, Isolated & Durable](https://www.youtube.com/watch?v=yaQ5YMWkxq4)

## Adding Extra Extensions

# Adding Extensions

PostgreSQL provides various extensions to enhance its features and functionalities. Extensions are optional packages that can be loaded into your PostgreSQL database to provide additional functionality like new data types or functions. Using extensions can be a powerful way to add new features to your PostgreSQL database and customize your database's functionality according to your needs.

Learn more from the following resources:

- [@official@PostgreSQL Extensions](https://www.postgresql.org/download/products/6-postgresql-extensions/)
- [@official@Create Extension](https://www.postgresql.org/docs/current/sql-createextension.html)

## Advanced Topics

# Advanced Topics in PostgreSQL Security

In addition to basic PostgreSQL security concepts, such as user authentication, privilege management, and encryption, there are several advanced topics that you should be aware of to enhance the security of your PostgreSQL databases.

Visit the following resources to learn more:

- [@article@Best Practices for Postgres Security](https://www.timescale.com/learn/postgres-security-best-practices)
- [@article@PostgreSQL - Encryption and Monitoring](https://www.enterprisedb.com/postgresql-best-practices-encryption-monitoring)

## Aggregate And Window Functions

# Aggregate and Window Functions

Aggregate functions in PostgreSQL perform calculations on a set of rows and return a single value, such as `SUM()`, `AVG()`, `COUNT()`, `MAX()`, and `MIN()`. Window functions, on the other hand, calculate values across a set of table rows related to the current row while preserving the row structure. Common window functions include `ROW_NUMBER()`, `RANK()`, `DENSE_RANK()`, `NTILE()`, `LAG()`, and `LEAD()`. These functions are crucial for data analysis, enabling complex queries and insights by summarizing and comparing data effectively.

Learn more from the following resources:

- [@article@Data Processing With PostgreSQL Window Functions](https://www.timescale.com/learn/postgresql-window-functions)
- [@article@Why & How to Use Window Functions to Aggregate Data in Postgres](https://coderpad.io/blog/development/window-functions-aggregate-data-postgres/)

## Ansible

# Ansible for PostgreSQL Configuration Management

Ansible is a widely used open-source configuration management and provisioning tool that helps automate many tasks for managing servers, databases, and applications. It uses a simple, human-readable language called YAML to define automation scripts, known as “playbooks”. By using Ansible playbooks and PostgreSQL modules, you can automate repetitive tasks, ensure consistent configurations, and reduce human error.

Learn more from the following resources:

- [@official@Ansible](https://www.ansible.com/)
- [@opensource@ansible/ansible](https://github.com/ansible/ansible)
- [@article@Ansible Tutorial for Beginners: Ultimate Playbook & Examples](https://spacelift.io/blog/ansible-tutorial)

## Any Programming Language

# Programming Languages and PostgreSQL Automation

PostgreSQL supports various languages for providing server-side scripting and developing custom functions, triggers, and stored procedures. When choosing a language, consider factors such as the complexity of the task, the need for a database connection, and the trade-off between learning a new language and leveraging existing skills.

Learn more from the following resources:

- [@official@Procedural Languages](https://www.postgresql.org/docs/current/external-pl.html)

## Attributes

# Attributes in the Relational Model

Attributes in the relational model are the columns of a table, representing the properties or characteristics of the entity described by the table. Each attribute has a domain, defining the possible values it can take, such as integer, text, or date. Attributes play a crucial role in defining the schema of a relation (table) and are used to store and manipulate data. They are fundamental in maintaining data integrity, enforcing constraints, and enabling the relational operations that form the basis of SQL queries.

Learn more from the following resources:

- [@article@What is a Relational Model?](https://www.guru99.com/relational-data-model-dbms.html)
- [@article@Relational Model in DBMS](https://www.scaler.com/topics/dbms/relational-model-in-dbms/)

## Authentication Models

# Authentication Models

PostgreSQL supports various authentication models to control access, including trust (no password, for secure environments), password-based (md5 and scram-sha-256 for hashed passwords), GSSAPI and SSPI (Kerberos for secure single sign-on), LDAP (centralized user management), certificate-based (SSL certificates for strong authentication), PAM (leveraging OS-managed authentication), Ident (verifying OS user names), and RADIUS (centralized authentication via RADIUS servers). These methods are configured in the `pg_hba.conf` file, specifying the appropriate authentication method for different combinations of databases, users, and client addresses, ensuring flexible and secure access control.

Learn more from the following resources:

- [@official@Authentication Methods](https://www.postgresql.org/docs/current/auth-methods.html)
- [@article@An Introduction to Authorization and Authentication in PostgreSQL](https://www.prisma.io/dataguide/postgresql/authentication-and-authorization/intro-to-authn-and-authz)

## Awk

# Awk

Awk is a versatile text processing tool that is widely used for various data manipulation, log analysis, and text reporting tasks. It is especially suitable for working with structured text data, such as data in columns. Awk can easily extract specific fields or perform calculations on them, making it an ideal choice for log analysis.

Learn more from the following resources:

- [@article@Awk](https://www.grymoire.com/Unix/Awk.html)
- [@article@Awk Command in Linux/Unix](https://www.digitalocean.com/community/tutorials/awk-command-linux-unix)
- [@video@Tutorial - AWK in 300 Seconds](https://www.youtube.com/watch?v=15DvGiWVNj0)

## B Tree

# B-Tree Indexes

B-Tree (short for Balanced Tree) is the default index type in PostgreSQL, and it's designed to work efficiently with a broad range of queries. A B-Tree is a data structure that enables fast search, insertion, and deletion of elements in a sorted order. B-Tree indexes are the most commonly used index type in PostgreSQL – versatile, efficient, and well-suited for various query types.

Learn more from the following resources:

- [@official@B-Tree](https://www.postgresql.org/docs/current/indexes-types.html#INDEXES-TYPES-BTREE)
- [@video@B-Tree Indexes](https://www.youtube.com/watch?v=NI9wYuVIYcA&t=109s)

## Backup Validation Procedures

# Backup Validation Procedures

It's not enough to just take backups; you must also ensure that your backups are valid and restorable. A corrupt or incomplete backup can lead to data loss or downtime during a crisis. Therefore, it's essential to follow best practices and validate your PostgreSQL backups periodically.

## Key Validation Procedures

Here are the critical backup validation procedures you should follow:

- **Restore Test**: Regularly perform a restore test using your backups to ensure that the backup files can be used for a successful restoration of your PostgreSQL database. This process can be automated using scripts and scheduled tasks.

- **Checksum Verification**: Use checksums during the backup process to validate the backed-up data. Checksums can help detect errors caused by corruption or data tampering. PostgreSQL provides built-in checksum support, which can be enabled at the database level.

- **File-Level Validation**: Compare the files in your backup with the source files in your PostgreSQL database. This will ensure that your backup contains all the necessary files and that their content matches the original data.

- **Backup Logs Monitoring**: Monitor and analyze the logs generated during your PostgreSQL backup process. Pay close attention to any warnings, errors, or unusual messages. Investigate and resolve any issues to maintain the integrity of your backups.

- **Automated Testing**: Set up automated tests to simulate a disaster recovery scenario and see if your backup can restore the database fully. This will not only validate your backups but also test the overall reliability of your recovery plan.

## Post-validation Actions

After validating your backups, it's essential to document the results and address any issues encountered during the validation process. This may involve refining your backup and recovery strategies, fixing any errors or updating your scripts and tools.

Learn more from the following resources:

- [@official@pg_verifybackup](https://www.postgresql.org/docs/current/app-pgverifybackup.html)
- [@article@PostgreSQL Backup and Restore Validation](https://portal.nutanix.com/page/documents/solutions/details?targetId=NVD-2155-Nutanix-Databases:postgresql-backup-and-restore-validation.html)

## Barman

# Barman (Backup and Recovery Manager)

Barman (Backup and Recovery Manager) is a robust tool designed for managing PostgreSQL backups and disaster recovery. It supports various backup types, including full and incremental backups, and provides features for remote backups, backup retention policies, and compression to optimize storage. Barman also offers point-in-time recovery (PITR) capabilities and integrates with PostgreSQL's WAL archiving to ensure data integrity. With its extensive monitoring and reporting capabilities, Barman helps database administrators automate and streamline backup processes, ensuring reliable and efficient recovery options in case of data loss or corruption.

Learn more from the following resources:

- [@official@pgBarman Website](https://www.pgbarman.org/)
- [@opensource@EnterpriseDB/barman](https://github.com/EnterpriseDB/barman)

## Basic Rdbms Concepts

# RDBMS Concepts

Relational Database Management Systems (RDBMS) are a type of database management system which stores and organizes data in tables, making it easy to manipulate, query, and manage the information. They follow the relational model defined by E.F. Codd in 1970, which means that data is represented as tables with rows and columns.

Visit the following resources to learn more:

- [@article@Understanding Relational Database Management Systems](https://www.essentialsql.com/understanding-relational-databases-a-beginners-guide/)

## Brin

# BRIN (Block Range INdex)

BRIN is an abbreviation for Block Range INdex which is an indexing technique introduced in PostgreSQL 9.5. This indexing strategy is best suited for large tables containing sorted data. It works by storing metadata regarding ranges of pages in the table. This enables quick filtering of data when searching for rows that match specific criteria. While not suitable for all tables and queries, they can significantly improve performance when used appropriately. Consider using a BRIN index when working with large tables with sorted or naturally ordered data.

Learn more from the following resources:

- [@official@BRIN Indexes](https://www.postgresql.org/docs/17/brin.html)
- [@article@Block Range INdexes](https://en.wikipedia.org/wiki/Block_Range_Index)

## Buffer Management

# Buffer Management

PostgreSQL uses a buffer pool to efficiently cache frequently accessed data pages in memory. The buffer pool is a fixed-size, shared memory area where database blocks are stored while they are being used, modified or read by the server. Buffer management is the process of efficiently handling these data pages to optimize performance.

Learn more from the following resources:

- [@article@Buffer Manager](https://dev.to/vkt1271/summary-of-chapter-8-buffer-manager-from-the-book-the-internals-of-postgresql-part-2-4f6o)
- [@official@pg_buffercache](https://www.postgresql.org/docs/current/pgbuffercache.html)
- [@official@Write Ahead Logging](https://www.postgresql.org/docs/current/wal-intro.html)

## Bulk Loading  Processing Data

# Bulk Load Process Data

Bulk load process data involves transferring large volumes of data from external files into the PostgreSQL database. This is an efficient way to insert massive amounts of data into your tables quickly, and it's ideal for initial data population or data migration tasks. Leveraging the `COPY` command or `pg_bulkload` utility in combination with best practices should help you load large datasets swiftly and securely.

Learn more from the following resources:

- [@official@Populating a Database](https://www.postgresql.org/docs/current/populate.html)
- [@article@7 Best Practice Tips for PostgreSQL Bulk Data Loading](https://www.enterprisedb.com/blog/7-best-practice-tips-postgresql-bulk-data-loading)

## Check Pgactivity

# check_pgactivity

`check_pgactivity` is a PostgreSQL monitoring tool that provides detailed health and performance statistics for PostgreSQL databases. Designed to be used with the Nagios monitoring framework, it checks various aspects of PostgreSQL activity, including connection status, replication status, lock activity, and query performance. By collecting and presenting key metrics, `check_pgactivity` helps database administrators detect and troubleshoot performance issues, ensuring the database operates efficiently and reliably. The tool supports custom thresholds and alerting, making it a flexible solution for proactive database monitoring.

- [@opensource@OPMDG/check_pgactivity](https://github.com/OPMDG/check_pgactivity)

## Check Pgbackrest

# check_pgbackrest

Monitoring `pgBackRest` helps ensure that your PostgreSQL backups are consistent, up-to-date, and free from any potential issues. By regularly checking your backups, you'll be able to maintain a reliable and efficient backup-restore process for your PostgreSQL database.

`pgBackRest` provides a built-in command called `check` which performs various checks to validate your repository and configuration settings. The command is executed as follows:

```sh
pgbackrest --stanza=<stanza_name> check
```

`<stanza_name>` should be replaced with the name of the stanza for which you want to verify the repository and configuration settings.

Learn more from the following resources:

- [@official@pgBackRest Website](https://pgbackrest.org/)

## Checkpoints  Background Writer

# Checkpoints and Background Writer

In PostgreSQL, checkpoints and the background writer are essential for maintaining data integrity and optimizing performance. Checkpoints periodically write all modified data (dirty pages) from the shared buffers to the disk, ensuring that the database can recover to a consistent state after a crash. This process is controlled by settings such as `checkpoint_timeout`, `checkpoint_completion_target`, and `max_wal_size`, balancing between write performance and recovery time. The background writer continuously flushes dirty pages to disk in the background, smoothing out the I/O workload and reducing the amount of work needed during checkpoints. This helps to maintain steady performance and avoid spikes in disk activity. Proper configuration of these mechanisms is crucial for ensuring efficient disk I/O management and overall database stability.

Learn more from the following resources:

- [@official@Checkpoints](https://www.postgresql.org/docs/current/sql-checkpoint.html)
- [@article@What is a checkpoint?](https://www.cybertec-postgresql.com/en/postgresql-what-is-a-checkpoint/)
- [@article@What are the difference between background writer and checkpoint in postgresql?](https://stackoverflow.com/questions/71534378/what-are-the-difference-between-background-writer-and-checkpoint-in-postgresql)

## Chef

# Chef for PostgreSQL Configuration Management

Chef is a powerful and widely-used configuration management tool that provides a simple yet customizable way to manage your infrastructure, including PostgreSQL installations. Chef is an open-source automation platform written in Ruby that helps users manage their infrastructure by creating reusable and programmable code, called "cookbooks" and "recipes", to define the desired state of your systems. It uses a client-server model and employs these cookbooks to ensure that your infrastructure is always in the desired state.

Learn more from the following resources:

- [@official@Chef Website](https://www.chef.io/products/chef-infra)
- [@opensource@chef/chef](https://github.com/chef/chef)

## Columns

# Columns in PostgreSQL

Columns are a fundamental component of PostgreSQL's object model. They are used to store the actual data within a table and define their attributes such as data type, constraints, and other properties. 

Learn more from the following resources:

- [@official@Columns](https://www.postgresql.org/docs/current/ddl-alter.html)
- [@article@PostgreSQL ADD COLUMN](https://www.w3schools.com/postgresql/postgresql_add_column.php)

## Configuring

# Configuring PostgreSQL

Configuring PostgreSQL involves modifying several key configuration files to optimize performance, security, and functionality. The primary configuration files are postgresql.conf, pg_hba.conf, and pg_ident.conf, typically located in the PostgreSQL data directory. By properly configuring these files, you can tailor PostgreSQL to better fit your specific needs and environment.

Visit the following resources to learn more:

- [@official@Configuring PostgreSQL](https://www.postgresql.org/docs/current/runtime-config.html)
- [@article@Install and Configure PostgreSQL](https://ubuntu.com/server/docs/install-and-configure-postgresql)

## Connect Using Psql

# Connect Using `psql`

`psql` is an interactive command-line utility that enables you to interact with a PostgreSQL database server. Using `psql`, you can perform various SQL operations on your database.

Learn more from the following resources:

- [@official@psql](https://www.postgresql.org/docs/current/app-psql.html#:~:text=psql%20is%20a%20terminal%2Dbased,and%20see%20the%20query%20results.)
- [@article@psql guide](https://www.postgresguide.com/utilities/psql/)

## Constraints

# Constraints in PostgreSQL

Constraints are an essential part of the relational model, as they define rules that the data within the database must follow. They ensure that the data is consistent, accurate, and reliable.

**Primary Key** - A primary key constraint is a column or a set of columns that uniquely identifies each row in a table. There can only be one primary key per table, and its value must be unique and non-null for each row.

**Foreign Key** - A foreign key constraint ensures that a column or columns in a table refer to an existing row in another table. It helps maintain referential integrity between tables.

**Unique** - A unique constraint ensures that the values in a column or set of columns are unique across all rows in a table. In other words, it prevents duplicate entries in the specified column(s).

**Check** - A check constraint verifies that the values entered into a column meet a specific condition. It helps to maintain data integrity by restricting the values that can be inserted into a column.

**Not Null** - A NOT NULL constraint enforces that a column cannot contain a NULL value. This ensures that a value must be provided for the specified column when inserting or updating data in the table.

**Exclusion** - An exclusion constraint is a more advanced form of constraint that allows you to specify conditions that should not exist when comparing multiple rows in a table. It helps maintain data integrity by preventing conflicts in data.

Learn more from the following resources:

- [@official@Constraints](https://www.postgresql.org/docs/current/ddl-constraints.html)
- [@article@PostgreSQL - Constraints](https://www.tutorialspoint.com/postgresql/postgresql_constraints.htm)

## Consul

# Consul - an introduction in the context of load balancing

Consul is a distributed, highly-available, and multi-datacenter aware service discovery and configuration tool developed by HashiCorp. It can be used to implement load balancing in a PostgreSQL cluster to distribute client connections and queries evenly across multiple backend nodes.

Consul uses a consensus protocol for leader election and ensures that only one server acts as a leader at any given time. This leader automatically takes over upon leader failure or shutdown, making the system resilient to outages. It provides a range of services like service discovery, health checking, key-value storage, and DNS services.

Learn more from the following resources:

- [@official@Consul by Hashicorp](https://www.consul.io/)
- [@opensource@hashicorp/consul](https://github.com/hashicorp/consul)
- [@article@What is Consul?](https://developer.hashicorp.com/consul/docs/intro)

## Core Dumps

# Core Dumps

A core dump is a file that contains the memory image of a running process and its process status. It's typically generated when a program crashes or encounters an unrecoverable error, allowing developers to analyze the state of the program at the time of the crash. In the context of PostgreSQL, core dumps can help diagnose and fix issues with the database system.

Learn more from the following resources:

- [@article@Core Dump](https://wiki.archlinux.org/title/Core_dump)
- [@article@Enabling Core Dumps](https://wiki.postgresql.org/wiki/Getting_a_stack_trace_of_a_running_PostgreSQL_backend_on_Linux/BSD#Enabling_core_dumps)

## Cte

# Common Table Expressions (CTEs)

A Common Table Expression, also known as CTE, is a named temporary result set that can be referenced within a `SELECT`, `INSERT`, `UPDATE`, or `DELETE` statement. CTEs are particularly helpful when dealing with complex queries, as they enable you to break down the query into smaller, more readable chunks. Recursive CTEs are helpful when working with hierarchical or tree-structured data.

Learn more from the following resources:

- [@official@Common Table Expressions](https://www.postgresql.org/docs/current/queries-with.html)
- [@article@PostgreSQL CTEs](https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-cte/)

## Data Partitioning

# Data Partitioning

Data partitioning is a technique that divides a large table into smaller, more manageable pieces called partitions. Each partition is a smaller table that stores a subset of the data, usually based on specific criteria such as ranges, lists, or hashes. Partitioning can improve query performance, simplifies data maintenance tasks, and optimizes resource utilization.

Learn more from the following resources:

- [@official@Table Partitioning](https://www.postgresql.org/docs/current/ddl-partitioning.html)
- [@article@How to use Table Partitioning to Scale PostgreSQL](https://www.enterprisedb.com/postgres-tutorials/how-use-table-partitioning-scale-postgresql)

## Data Types

# Data Types in PostgreSQL

PostgreSQL offers a rich and diverse set of data types, catering to a wide range of applications and ensuring data integrity and performance. These include standard numeric types such as integers, floating-point numbers, and serial types for auto-incrementing fields. Character types like `VARCHAR` and `TEXT` handle varying lengths of text, while DATE, TIME, and TIMESTAMP support a variety of temporal data requirements. PostgreSQL also supports a comprehensive set of Boolean, enumerated (ENUM), and composite types, enabling more complex data structures. Additionally, it excels with its support for JSON and JSONB data types, allowing for efficient storage and querying of semi-structured data. The inclusion of array types, geometric data types, and the PostGIS extension for geographic data further extends PostgreSQL's versatility, making it a powerful tool for a broad spectrum of data management needs.

Learn more from the following resources:

- [@official@Data Types](https://www.postgresql.org/docs/current/datatype.html)
- [@article@Introduction to PostgreSQL DataTypes](https://www.prisma.io/dataguide/postgresql/introduction-to-data-types)
- [@article@PostgreSQL® Data Types: Mappings to SQL, JDBC, and Java Data Types](https://www.instaclustr.com/blog/postgresql-data-types-mappings-to-sql-jdbc-and-java-data-types/)

## Data Types

# Data Types in PostgreSQL

PostgreSQL offers a comprehensive set of data types to cater to diverse data needs, including numeric types like `INTEGER`, `FLOAT`, and `SERIAL` for auto-incrementing fields; character types such as `VARCHAR` and `TEXT` for variable-length text; and temporal types like `DATE`, `TIME`, and `TIMESTAMP` for handling date and time data. Additionally, PostgreSQL supports `BOOLEAN` for true/false values, `ENUM` for enumerated lists, and composite types for complex structures. It also excels with `JSON` and `JSONB` for storing and querying semi-structured data, arrays for storing multiple values in a single field, and geometric types for spatial data. These data types ensure flexibility and robust data management for various applications.

Learn more from the following resources:

- [@article@PostgreSQL® Data Types: Mappings to SQL, JDBC, and Java Data Types](https://www.instaclustr.com/blog/postgresql-data-types-mappings-to-sql-jdbc-and-java-data-types/)
- [@official@Data Types](https://www.postgresql.org/docs/current/datatype.html)

## Databases

# Databases in PostgreSQL

In PostgreSQL, a database is a named collection of tables, indexes, views, stored procedures, and other database objects. Each PostgreSQL server can manage multiple databases, enabling the separation and organization of data sets for various applications, projects, or users.

Learn more from the following resources:

- [@official@Managing Databases](https://www.postgresql.org/docs/current/managing-databases.html)

## Default Privileges

# Default Privileges in PostgreSQL

PostgreSQL allows you to define object privileges for various types of database objects. These privileges determine if a user can access and manipulate objects like tables, views, sequences, or functions. In this section, we will focus on understanding default privileges in PostgreSQL.

Learn more from the following resources:

- [@official@ALTER DEFAULT PRIVILEGES](https://www.postgresql.org/docs/current/sql-alterdefaultprivileges.html)
- [@official@Privileges](https://www.postgresql.org/docs/current/ddl-priv.html)

## Depesz

# Depesz: A Tool for Query Analysis

"Depesz" is a popular, online query analysis tool for PostgreSQL, named after Hubert "depesz" Lubaczewski, the creator of the tool. It helps you understand and analyze the output of `EXPLAIN ANALYZE`, a powerful command in PostgreSQL for examining and optimizing your queries. Depesz is often used to simplify the query analysis process, as it offers valuable insights into the performance of your SQL queries and aids in tuning them for better efficiency.

Learn more from the following resources:

- [@official@Depesz Website](https://www.depesz.com/)

## Deployment In Cloud

# Deployment in Cloud

In this section, we will discuss deploying PostgreSQL in the cloud. Deploying your PostgreSQL database in the cloud offers significant advantages such as scalability, flexibility, high availability, and cost reduction. There are several cloud providers that offer PostgreSQL as a service, which means you can quickly set up and manage your databases without having to worry about underlying infrastructure, backups, and security measures.

Learn more from the following resources:

- [@article@5 Ways to Host PostgreSQL Databases](https://www.prisma.io/dataguide/postgresql/5-ways-to-host-postgresql)
- [@article@Postgres On Kubernetes](https://cloudnative-pg.io/)
- [@feed@Explore top posts about Cloud](https://app.daily.dev/tags/cloud?ref=roadmapsh)

## Domains

# Domains in PostgreSQL

Domains in PostgreSQL are essentially user-defined data types that can be created using the `CREATE DOMAIN` command. These custom data types allow you to apply constraints and validation rules to columns in your tables by defining a set of values that are valid for a particular attribute or field. This ensures consistency and data integrity within your relational database.

To create a custom domain, you need to define a name for your domain, specify its underlying data type, and set any constraints or default values you want to apply. Domains in PostgreSQL are a great way to enforce data integrity and consistency in your relational database. They allow you to create custom data types based on existing data types with added constraints, default values, and validation rules. By using domains, you can streamline your database schema and ensure that your data complies with your business rules or requirements.

Learn more from the following resources:

- [@official@CREATE DOMAIN](https://www.postgresql.org/docs/current/sql-createdomain.html)
- [@official@Domain Types](https://www.postgresql.org/docs/current/domains.html)

## Ebpf

# eBPF (Extended Berkeley Packet Filter)

eBPF is a powerful Linux kernel technology used for tracing and profiling various system components such as processes, filesystems, network connections, and more. It has gained enormous popularity among developers and administrators because of its ability to offer deep insights into the system's behavior, performance, and resource usage at runtime. In the context of profiling PostgreSQL, eBPF can provide valuable information about query execution, system calls, and resource consumption patterns.

Learn more from the following resources:

- [@article@What is eBPF? (Extended Berkeley Packet Filter)](https://www.kentik.com/kentipedia/what-is-ebpf-extended-berkeley-packet-filter/)
- [@article@What is Extended Berkeley Packet Filter (eBPF)](https://www.sentinelone.com/cybersecurity-101/what-is-extended-berkeley-packet-filter-ebpf/)
- [@video@Introduction to eBPF](https://www.youtube.com/watch?v=qXFi-G_7IuU)

## Etcd

# Etcd

Etcd is a distributed key-value store that provides an efficient and reliable means for storing crucial data across clustered environments. It has become popular as a fundamental component for storing configuration data and service discovery in distributed systems.

Etcd can be utilized in conjunction with _connection poolers_ such as PgBouncer or HAProxy to improve PostgreSQL load balancing. By maintaining a list of active PostgreSQL servers' IP addresses and ports as keys in the store, connection poolers can fetch this information periodically to route client connections to the right servers. Additionally, transactional operations on the store can simplify the process of adding or removing nodes from the load balancer configuration while maintaining consistency.

Learn more from the following resources:

- [@opensource@PostgreSQL High Availability with Etcd](https://github.com/patroni/patroni)
- [@video@PostgreSQL High Availability](https://www.youtube.com/watch?v=J0ErkLo2b1E)
- [@articles@etcd vs PostgreSQL](https://api7.ai/blog/etcd-vs-postgresql)

## Explain

# Query Analysis: EXPLAIN in PostgreSQL

Understanding the performance and efficiency of your queries is crucial when working with databases. In PostgreSQL, the `EXPLAIN` command helps to analyze and optimize your queries by providing insights into the query execution plan. This command allows you to discover bottlenecks, inefficient table scans, improper indexing, and other issues that may impact your query performance.

`EXPLAIN` generates a query execution plan without actually executing the query. It shows the nodes in the plan tree, the order in which they will be executed, and the estimated cost of each operation.

Learn more from the following resources:

- [@official@Using EXPLAIN](https://www.postgresql.org/docs/current/using-explain.html)
- [@article@PostgreSQL EXPLAIN](https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-explain/)

## Explaindalibocom

# explain.dalibo.com

explain.dalibo.com is a free service that allows you to analyze the execution plan of your queries. It is based on the explain.depesz.com service.

Learn more from the following resources:

- [@official@explain.dalibo.com](https://explain.dalibo.com/)

## Filtering Data

# Filtering Data in PostgreSQL

Filtering data is an essential feature in any database management system, and PostgreSQL is no exception. When we refer to filtering data, we're talking about selecting a particular subset of data that fulfills specific criteria or conditions. In PostgreSQL, we use the **WHERE** clause to filter data in a query based on specific conditions.

Learn more from the following resources:

- [@article@How to Filter Query Results in PostgreSQL](https://www.prisma.io/dataguide/postgresql/reading-and-querying-data/filtering-data)
- [@article@Using PostgreSQL FILTER](https://www.crunchydata.com/blog/using-postgres-filter)
- [@article@PostgreSQL - WHERE](https://www.w3schools.com/postgresql/postgresql_where.php)

## For Schemas

# Schemas in PostgreSQL

A schema is a logical collection of database objects within a PostgreSQL database. It behaves like a namespace that allows you to group and isolate your database objects separately from other schemas. The primary goal of a schema is to organize your database structure, making it easier to manage and maintain. By default, every PostgreSQL database has a `public` schema, which is the default search path for any unqualified table or other database object.

Learn more from the following resources:

- [@official@Schemas](https://www.postgresql.org/docs/current/ddl-schemas.html)
- [@article@PostgreSQL Schema](https://hasura.io/learn/database/postgresql/core-concepts/1-postgresql-schema/)

## Fortables

# For Tables in PostgreSQL

The primary DDL statements for creating and managing tables in PostgreSQL include `CREATE TABLE`, `ALTER TABLE`, and `DROP TABLE`, these DDL commands allow you to create, modify, and delete tables and their structures, providing a robust framework for database schema management in PostgreSQL.

Learn more from the following resources:

- [@official@CREATE TABLE](https://www.postgresql.org/docs/current/sql-createtable.html)
- [@official@DROP TABLE](https://www.postgresql.org/docs/current/sql-droptable.html)
- [@official@ALTER TABLE](https://www.postgresql.org/docs/current/sql-altertable.html)

## Gdb

# GDB (GNU Debugger)

GDB, the GNU Debugger, is a powerful debugging tool that provides inspection and modification features for applications written in various programming languages, including C, C++, and Fortran. GDB can be used alongside PostgreSQL for investigating backend processes and identifying potential issues that might not be apparent at the application level.

Learn more from the following resources:

- [@official@GDB](https://sourceware.org/gdb/)
- [@article@Learn how to use GDB](https://opensource.com/article/21/3/debug-code-gdb)

## Get Involved In Development

# Get Involved in Development

PostgreSQL is an open-source database system developed by a large and active community. By getting involved in the development process, you can help contribute to its growth, learn new skills, and collaborate with other developers around the world. In this section, we'll discuss some ways for you to participate in the PostgreSQL development community.

## Join Mailing Lists and Online Forums

Join various PostgreSQL mailing lists, such as the general discussion list (_pgsql-general_), the development list (_pgsql-hackers_), or other specialized lists to stay up-to-date on discussions related to the project. You can also participate in PostgreSQL-related forums, like Stack Overflow or Reddit, to engage with fellow developers, ask questions, and provide assistance to others.

## Bug Reporting and Testing

Reporting bugs and testing new features are invaluable contributions to improving the quality and stability of PostgreSQL. Before submitting a bug report, make sure to search the official bug tracking system to see if the issue has already been addressed. Additionally, consider testing patches submitted by other developers or contributing tests for new features or functionalities.

## Contribute Code

Contributing code can range from fixing small bugs or optimizing existing features, to adding entirely new functionalities. To start contributing to the PostgreSQL source code, you'll need to familiarize yourself with the [PostgreSQL coding standards](https://www.postgresql.org/docs/current/source.html) and submit your changes as patches through the PostgreSQL mailing list. Make sure to follow the [patch submission guidelines](https://wiki.postgresql.org/wiki/Submitting_a_Patch) to ensure that your contributions are properly reviewed and considered.

## Documentation and Translations

Improving and expanding the official PostgreSQL documentation is crucial for providing accurate and up-to-date information to users. If you have expertise in a particular area, you can help by updating the documentation. Additionally, translating the documentation or interface messages into other languages can help expand the PostgreSQL community by providing resources for non-English speakers.

## Offer Support and Help Others

By helping others in the community, you not only contribute to the overall growth and development of PostgreSQL but also develop your own knowledge and expertise. Participate in online discussions, answer questions, conduct workshops or webinars, and share your experiences and knowledge to help others overcome challenges they may be facing.

## Advocate for PostgreSQL

Promoting and advocating for PostgreSQL in your organization and network can help increase its adoption and visibility. Share your success stories, give talks at conferences, write blog posts, or create tutorials to help encourage more people to explore PostgreSQL as a go-to solution for their database needs.

Remember, the PostgreSQL community thrives on the input and dedication of its members, so don't hesitate to get involved and contribute. Every contribution, no matter how small, can have a positive impact on the project and create a more robust and powerful database system for everyone.

## Gin

# GIN (Generalized Inverted Index)

Generalized Inverted Index (GIN) is a powerful indexing method in PostgreSQL that can be used for complex data types such as arrays, text search, and more. GIN provides better search capabilities for non-traditional data types, while also offering efficient and flexible querying.

Learn more from the following resources:

- [@official@GIN Introduction](https://www.postgresql.org/docs/current/gin-intro.html)
- [@article@Generalized Inverted Indexes](https://www.cockroachlabs.com/docs/stable/inverted-indexes)

## Gist

# GIST Indexes

The Generalized Search Tree (GiST) is a powerful and flexible index type in PostgreSQL that serves as a framework to implement different indexing strategies. GiST provides a generic infrastructure for building custom indexes, extending the core capabilities of PostgreSQL. This powerful indexing framework allows you to extend PostgreSQL's built-in capabilities, creating custom indexing strategies aligned with your specific requirements.

Learn more from the following resources:

- [@official@GIST Indexes](https://www.postgresql.org/docs/8.1/gist.html)
- [@article@Generalized Search Trees for Database Systems](https://www.vldb.org/conf/1995/P562.PDF)

## Golden Signals

# Golden Signals

Golden Signals are a set of metrics that help monitor application performance and health, particularly in distributed systems. These metrics are derived from Google's Site Reliability Engineering (SRE) practices and can be easily applied to PostgreSQL troubleshooting methods. By monitoring these four key signals – latency, traffic, errors, and saturation – you can gain a better understanding of your PostgreSQL database's overall performance and health, as well as quickly identify potential issues.

Learn more from the following resources:

- [@article@The Four Golden Signals](https://sre.google/sre-book/monitoring-distributed-systems/#xref_monitoring_golden-signals)
- [@article@4 SRE Golden Signals (What they are and why they matter)](https://www.blameless.com/blog/4-sre-golden-signals-what-they-are-and-why-they-matter)

## Grant  Revoke

# Grant and Revoke Privileges in PostgreSQL

One of the most important aspects of database management is providing appropriate access permissions to users. In PostgreSQL, this can be achieved with the `GRANT` and `REVOKE` commands, which allow you to manage the privileges of database objects such as tables, sequences, functions, and schemas. 

Learn more from the following resources:

- [@official@GRANT](https://www.postgresql.org/docs/current/sql-grant.html)
- [@official@REVOKE](https://www.postgresql.org/docs/current/sql-revoke.html)
- [@article@PostgreSQL GRANT statement](https://www.postgresqltutorial.com/postgresql-administration/postgresql-grant/)
- [@article@PostgreSQL REVOKE statement](https://www.postgresqltutorial.com/postgresql-administration/postgresql-revoke/)

## Grep

# Grep Command in Log Analysis

Grep is a powerful command-line tool used for searching plain-text data sets against specific patterns. It was originally developed for the Unix operating system and has since become available on almost every platform. When analyzing PostgreSQL logs, you may find the `grep` command an incredibly useful resource for quickly finding specific entries or messages.

Learn more from the following resources:

- [@article@grep command in Linux/Unix](https://www.digitalocean.com/community/tutorials/grep-command-in-linux-unix)
- [@article@Use the Grep Command](https://docs.rackspace.com/docs/use-the-linux-grep-command)
- [@video@Tutorial - grep: A Practical Guide](https://www.youtube.com/watch?v=crFZOrqlqao)

## Grouping

# Grouping

Grouping is a powerful technique in SQL that allows you to organize and aggregate data based on common values in one or more columns. The `GROUP BY` clause is used to create groups, and the `HAVING` clause is used to filter the group based on certain conditions.

Learn more from the following resources:

- [@official@PostgreSQL GROUP BY CLAUSE](https://www.postgresql.org/docs/current/sql-select.html#SQL-GROUPBY)
- [@article@PostgreSQL GROUP BY](https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-group-by/)
- [@article@PostgreSQL - GROUP BY](https://www.tutorialspoint.com/postgresql/postgresql_group_by.htm)
- [@article@PostgreSQL - HAVING](https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-having/)
- [@video@PostgreSQL Group BY](https://www.youtube.com/watch?v=SI-bPx4jaGc)

## Haproxy

# HAProxy

HAProxy, short for High Availability Proxy, is a popular open-source software used to provide high availability, load balancing, and proxying features for TCP and HTTP-based applications. It is commonly used to improve the performance, security, and reliability of web applications, databases, and other services. When it comes to load balancing in PostgreSQL, HAProxy is a popular choice due to its flexibility and efficient performance. By distributing incoming database connections across multiple instances of your PostgreSQL cluster, HAProxy can help you achieve better performance, high availability, and fault tolerance.

Learn more from the following resources:

- [@official@HAProxy Website](https://www.haproxy.org/)
- [@article@An Introduction to HAProxy and Load Balancing Concepts](https://www.digitalocean.com/community/tutorials/an-introduction-to-haproxy-and-load-balancing-concepts)

## Hash

# Hash Indexes

Hash Indexes are a type of database index that uses a hash function to map each row's key value into a fixed-length hashed key. The purpose of using a hash index is to enable quicker search operations by converting the key values into a more compact and easily searchable format.

Learn more from the following resources:

- [@official@Hash](https://www.postgresql.org/docs/current/indexes-types.html#INDEXES-TYPES-HASH)
- [@article@Re-Introducing Hash Indexes in PostgreSQL](https://hakibenita.com/postgresql-hash-index)

## Helm

# Helm - Package Manager for Kubernetes

Helm is a popular package manager for Kubernetes that allows you to easily deploy, manage, and upgrade applications on your Kubernetes cluster. In the Kubernetes world, Helm plays a similar role as "apt" or "yum" in the Linux ecosystem.

Helm streamlines the installation process by providing ready-to-use packages called "charts". A Helm chart is a collection of YAML files, templates, and manifests, that describe an application's required resources and configurations.

Learn more from the following resources:

- [@official@Helm Website](https://helm.sh/)
- [@opensource@helm/helm](https://github.com/helm/helm)

## High Level Database Concepts

# High Level Database Concepts

High-level database concepts encompass fundamental principles that underpin the design, implementation, and management of database systems. These concepts form the foundation of effective database management, enabling the design of robust, efficient, and scalable systems.

Visit the following resources to learn more:

- [@article@Demystifying PostgreSQL: 10 Crucial Concepts and Files](https://medium.com/@RohitAjaygupta/demystifying-postgresql-10-crucial-concepts-and-files-explained-with-practical-examples-a5a70cd2b848)

## Htap

# HTAP

Hybrid Transactional/Analytical Processing (HTAP) in PostgreSQL refers to a database system's ability to efficiently handle both Online Transaction Processing (OLTP) and Online Analytical Processing (OLAP) workloads simultaneously. PostgreSQL achieves this through its robust architecture, which supports ACID transactions for OLTP and advanced analytical capabilities for OLAP. Key features include Multi-Version Concurrency Control (MVCC) for high concurrency, partitioning and parallel query execution for performance optimization, and extensions like PL/pgSQL for complex analytics. PostgreSQL's ability to manage transactional and analytical tasks in a unified system reduces data latency and improves real-time decision-making, making it an effective platform for HTAP applications.

Learn more from the following resources:

- [@article@HTAP: Hybrid Transactional and Analytical Processing](https://www.snowflake.com/guides/htap-hybrid-transactional-and-analytical-processing/)
- [@article@What is HTAP?](https://planetscale.com/blog/what-is-htap)

## Import  Export Using Copy

# Import and Export using COPY

In PostgreSQL, one of the fastest and most efficient ways to import and export data is by using the `COPY` command. The `COPY` command allows you to import data from a file, or to export data to a file from a table or a query result.

If you can't use the `COPY` command due to lack of privileges, consider using the `\copy` command in the `psql` client instead, which works similarly, but runs as the current user rather than the PostgreSQL server.

Learn more from the following resources:

- [@official@COPY](https://www.postgresql.org/docs/current/sql-copy.html)
- [@article@Copying Data Between Tables in PostgreSQL](https://www.atlassian.com/data/sql/copying-data-between-tables)

## Indexes And Their Usecases

# Indexes Use Cases

Indexes in PostgreSQL improve query performance by allowing faster data retrieval. Common use cases include:

- Primary and Unique Keys: Ensure fast access to rows based on unique identifiers.
- Foreign Keys: Speed up joins between related tables.
- Search Queries: Optimize searches on large text fields with full-text search indexes.
- Range Queries: Improve performance for range-based queries on date, time, or numerical fields.
- Partial Indexes: Create indexes on a subset of data, useful for frequently queried columns with specific conditions.
-	Expression Indexes: Index expressions or functions, enhancing performance for queries involving complex calculations.
- Composite Indexes: Optimize multi-column searches by indexing multiple fields together.
- GIN and GiST Indexes: Enhance performance for array, JSONB, and geometric data types.

## Infrastructure Skills

# PostgreSQL Infrastructure Skills

PostgreSQL is an advanced, enterprise-class open-source relational database system that offers excellent performance and reliability. As a database administrator (DBA) or a developer working with PostgreSQL, it is essential to have a strong understanding of the various infrastructure skills required to manage and maintain a PostgreSQL environment effectively.

Having a solid grasp of these PostgreSQL infrastructure skills will significantly benefit you in your professional endeavors and empower you to manage PostgreSQL environments effectively, be it as a developer or a DBA.

## Installation And Setup

# Installation and Setup of PostgreSQL

To install and set up PostgreSQL, begin by downloading the installer from the official PostgreSQL website for your operating system (Windows, macOS, or Linux). For Windows, run the installer and follow the prompts to configure components, set a password for the superuser (postgres), and choose the installation directory and port (default is 5432). On macOS, using Homebrew is the recommended method; simply run brew install postgresql in the terminal, then initialize the database with brew services start postgresql. For Linux, use the package manager (APT for Debian/Ubuntu or YUM for CentOS/RHEL) to install PostgreSQL, followed by initializing the database and starting the service. After installation, you can access PostgreSQL using the psql command-line tool to create databases and manage your data effectively.

Visit the following resources to learn more:

- [@official@Installing PostgreSQL](https://www.postgresql.org/download/)
- [@article@PostgreSQL - Installation](https://www.postgresql.org/docs/current/tutorial-install.html)

## Introduction

# Introduction to PostgreSQL

PostgreSQL is a powerful, open-source Object-Relational Database Management System (ORDBMS) that is known for its robustness, extensibility, and SQL compliance. It was initially developed at the University of California, Berkeley, in the 1980s and has since become one of the most popular open-source databases in the world.

Visit the following resources to learn more:

- [@official@PostgreSQL](https://www.postgresql.org/)
- [@official@PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [@article@History of POSTGRES to PostgreSQL](https://www.postgresql.org/docs/current/history.html)

## Iotop

# iotop

`iotop` is an essential command-line utility that provides real-time insights into the input/output (I/O) activities of processes running on your system. This tool is particularly useful when monitoring and managing your PostgreSQL database's performance, as it helps system administrators or database developers to identify processes with high I/O, leading to potential bottlenecks or server optimization opportunities.

Learn more from the following resources:

- [@article@Linux iotop Check What’s Stressing & Increasing Load On Hard Disks](https://www.cyberciti.biz/hardware/linux-iotop-simple-top-like-io-monitor/)
- [@article@iotop man page](https://linux.die.net/man/1/iotop)

## Joining Tables

# Joining Tables

Joining tables is a fundamental operation in the world of databases. It allows you to combine information from multiple tables based on common columns. PostgreSQL provides various types of joins, such as Inner Join, Left Join, Right Join, and Full Outer Join. 

Learn more from the following resources:

- [@official@Joins Between Tables](https://www.postgresql.org/docs/current/tutorial-join.html)

## Keepalived

# Keepalived

Keepalived is a robust and widely-used open-source solution for load balancing and high availability. It helps to maintain a stable and perfect working environment even in the presence of failures such as server crashes or connectivity issues.

Keepalived achieves this by utilizing the Linux Virtual Server (LVS) module and the Virtual Router Redundancy Protocol (VRRP). For PostgreSQL database systems, Keepalived can be an advantageous addition to your infrastructure by offering fault tolerance and load balancing. With minimal configuration, it distributes read-only queries among multiple replicated PostgreSQL servers or divides transaction processing across various nodes – ensuring an efficient and resilient system.

Learn more from the following resources:

- [@official@Keepalived](https://www.keepalived.org/)
- [@opensource@acassen/keepalived](https://github.com/acassen/keepalived)
- [@article@Keepalived: High Availability for Self-hosted Services](https://www.virtualizationhowto.com/2023/09/keepalived-high-availability-for-self-hosted-services/)

## Lateral Join

# Lateral Join in PostgreSQL

Lateral join allows you to reference columns from preceding tables in a query, making it possible to perform complex operations that involve correlated subqueries and the application of functions on tables in a cleaner and more effective way. The `LATERAL` keyword in PostgreSQL is used in conjunction with a subquery in the `FROM` clause of a query. It helps you to write more concise and powerful queries, as it allows the subquery to reference columns from preceding tables in the query.

Learn more from the following resources:

- [@official@LATERAL Subqueries](https://www.postgresql.org/docs/current/queries-table-expressions.html#QUERIES-LATERAL)
- [@article@How to use lateral join in PostgreSQL](https://popsql.com/learn-sql/postgresql/how-to-use-lateral-joins-in-postgresql)

## Learn Sql

# Learn SQL Concepts

SQL stands for Structured Query Language. It is a standardized programming language designed to manage and interact with relational database management systems (RDBMS). SQL allows you to create, read, edit, and delete data stored in database tables by writing specific queries.

Visit the following resources to learn more:

- [@roadmap@Visit Dedicated SQL Roadmap](https://roadmap.sh/sql)
- [@article@SQL Tutorial - Essential SQL For The Beginners](https://www.sqltutorial.org/)

## Learn To Automate

# Learn Automation in PostgreSQL

When working with PostgreSQL, automating repetitive and time-consuming tasks is crucial for increasing efficiency and reliability in your database operations.

Visit the following resources to learn more:

- [@article@PostgreSQL - Automation](https://www.postgresql.org/docs/current/maintenance.html)
- [@article@Autoscaling Azure PostgreSQL Server with Automation Tasks](https://techcommunity.microsoft.com/blog/adforpostgresql/autoscaling-azure-postgresql-server-with-automation-tasks/3911718)

## Lock Management

# Lock Management

Lock management in PostgreSQL is implemented using a lightweight mechanism that allows database objects, such as tables, rows, and transactions, to be locked in certain modes. The primary purpose of locking is to prevent conflicts that could result from concurrent access to the same data or resources.

There are various types of lock modes available, such as `AccessShareLock`, `RowExclusiveLock`, `ShareUpdateExclusiveLock`, etc. Each lock mode determines the level of compatibility with other lock modes, allowing or preventing specific operations on the locked object.

Learn more from the following resources:

- [@official@Lock Management](https://www.postgresql.org/docs/current/runtime-config-locks.html)
- [@article@Understanding Postgres Locks and Managing Concurrent Transactions](https://medium.com/@sonishubham65/understanding-postgres-locks-and-managing-concurrent-transactions-1ededce53d59)

## Logical Replication

# Logical Replication

Logical replication in PostgreSQL allows the selective replication of data between databases, providing flexibility in synchronizing data across different systems. Unlike physical replication, which copies entire databases or clusters, logical replication operates at a finer granularity, allowing the replication of individual tables or specific subsets of data. This is achieved through the use of replication slots and publications/subscriptions. A publication defines a set of changes (INSERT, UPDATE, DELETE) to be replicated, and a subscription subscribes to these changes from a publisher database to a subscriber database. Logical replication supports diverse use cases such as real-time data warehousing, database migration, and multi-master replication, where different nodes can handle both reads and writes. Configuration involves creating publications on the source database and corresponding subscriptions on the target database, ensuring continuous, asynchronous data flow with minimal impact on performance.

Learn more from the following resources:

- [@official@Logical Replication](https://www.postgresql.org/docs/current/logical-replication.html)
- [@article@Logical Replication in PostgreSQL Explained](https://www.enterprisedb.com/postgres-tutorials/logical-replication-postgresql-explained)
- [@article@How to start Logical Replication for PostgreSQL](https://www.percona.com/blog/how-to-start-logical-replication-in-postgresql-for-specific-tables-based-on-a-pg_dump/)

## Mailing Lists

# Mailing Lists

Mailing lists are an essential part of PostgreSQL's development community. They provide a platform for collaboration, discussion, and problem-solving. By participating in these lists, you can contribute to the development of PostgreSQL, share your knowledge with others, and stay informed about the latest updates, improvements, and conferences.

PostgreSQL's development community offers a variety of mailing lists for discussions, announcements, and contributions. Key lists include **pgsql-hackers** for core development and feature discussions, **pgsql-announce** for official announcements, **pgsql-general** for general usage and administration queries, **pgsql-novice** for beginners seeking advice, and **pgsql-docs** for documentation-related contributions. Regional and language-specific lists are also available. To engage, subscribe to a mailing list that matches your interests, introduce yourself, read the archives for context, and participate in discussions. For guidelines, follow the Mailing List Etiquette.

Visit the following resources to learn more:

- [@official@Mailing List Etiquette](https://www.postgresql.org/community/lists/etiquette/)
- [@official@pgsql-hackers Subscription](https://www.postgresql.org/list/pgsql-hackers/)  
- [@official@pgsql-announce Subscription](https://www.postgresql.org/list/pgsql-announce/)  
- [@official@pgsql-general Subscription](https://www.postgresql.org/list/pgsql-general/)  
- [@official@pgsql-novice Subscription](https://www.postgresql.org/list/pgsql-novice/)  
- [@official@pgsql-docs Subscription](https://www.postgresql.org/list/pgsql-docs/)  
- [@official@PostgreSQL Mailing Lists page](https://www.postgresql.org/list/)

## Migration Related Tools

# liquibase, sqitch, Bytebase, ora2pg etc

Migrations are crucial in the lifecycle of database applications. As the application evolves, changes to the database schema and sometimes data itself become necessary. 

Learn more from the following resources:

- [@official@Liquibase Website](https://www.liquibase.com/)
- [@official@Sqitch Website](https://sqitch.org/)
- [@official@Bytebase Website](https://www.bytebase.com/)

## Modifying Data

# Modifying Data in PostgreSQL

Modifying data in PostgreSQL is an essential skill when working with databases. The primary DML queries used to modify data are `INSERT`, `UPDATE`, and `DELETE`.

Learn more from the following resources:

- [@official@INSERT](https://www.postgresql.org/docs/current/sql-insert.html)
- [@official@UPDATE](https://www.postgresql.org/docs/current/sql-update.html)
- [@official@DELETE](https://www.postgresql.org/docs/current/sql-delete.html)

## Mvcc

# Multi-Version Concurrency Control (MVCC)

Multi-Version Concurrency Control (MVCC) is a technique used by PostgreSQL to allow multiple transactions to access the same data concurrently without conflicts or delays. It ensures that each transaction has a consistent snapshot of the database and can operate on its own version of the data.

Visit the following resources to learn more:

- [@official@Intro to MVCC](https://www.postgresql.org/docs/current/mvcc-intro.html)
- [@article@Multi-Version Concurrency Control - Wikipedia](https://en.wikipedia.org/wiki/Multiversion_concurrency_control)
- [@article@What is MVVC?](https://www.theserverside.com/blog/Coffee-Talk-Java-News-Stories-and-Opinions/What-is-MVCC-How-does-Multiversion-Concurrencty-Control-work)

## Normalization  Normal Forms

# Data Normalization: Normal Forms

Data normalization in PostgreSQL involves organizing tables to minimize redundancy and ensure data integrity through a series of normal forms: First Normal Form (1NF) ensures each column contains atomic values and records are unique; Second Normal Form (2NF) requires that all non-key attributes are fully dependent on the primary key; Third Normal Form (3NF) eliminates transitive dependencies so non-key attributes depend only on the primary key; Boyce-Codd Normal Form (BCNF) further ensures that every determinant is a candidate key; Fourth Normal Form (4NF) removes multi-valued dependencies; and Fifth Normal Form (5NF) addresses join dependencies, ensuring tables are decomposed without loss of data integrity. These forms create a robust framework for efficient, consistent, and reliable database schema design.

Learn more from the following resources:

- [@article@A Guide to Data Normalization in PostgreSQL ](https://www.cybertec-postgresql.com/en/data-normalization-in-postgresql/)
- [@video@First normal form](https://www.youtube.com/watch?v=PCdZGzaxwXk)
- [@video@Second normal form](https://www.youtube.com/watch?v=_NHkY6Yvh64)
- [@video@Third normal form](https://www.youtube.com/watch?v=IN2m7VtYbEU)

## Null

# The Relational Model: Null Values

In the relational model used by PostgreSQL, null values represent missing or unknown information within a database. Unlike zero, empty strings, or other default values, null signifies the absence of a value and is treated uniquely in operations and queries. For example, any arithmetic operation involving a null results in a null, and comparisons with null using standard operators return unknown rather than true or false. To handle null values, PostgreSQL provides specific functions and constructs such as `IS NULL`, `IS NOT NULL`, and the `COALESCE` function, which returns the first non-null value in its arguments. Understanding and correctly handling null values is crucial for accurate data retrieval and integrity in relational databases.

Visit the following resources to learn more:

- [@official@PostgreSQL - NULL](https://www.postgresql.org/docs/current/datatype-numeric.html#DATATYPE-NULL)
- [@article@PostgreSQL - NULL Values](https://www.relationaldbdesign.com/database-analysis/module2/relational-database-null-values.php)

## Object Model

# Object Model in PostgreSQL

PostgreSQL is an object-relational database management system (ORDBMS). That means it combines features of both relational (RDBMS) and object-oriented databases (OODBMS). The object model in PostgreSQL provides features like user-defined data types, inheritance, and polymorphism, which enhances its capabilities beyond a typical SQL-based RDBMS.

Visit the following resources to learn more:

- [@official@Object Model](https://www.postgresql.org/docs/current/tutorial-concepts.html)
- [@article@Understanding PostgreSQL: The Power of an Object-Relational](https://medium.com/@asadbukhari886/understanding-of-postgresql-the-power-of-an-object-relational-database-b6ae349c3f40)
- [@article@PostgreSQL Server and Database Objects](https://neon.com/postgresql/postgresql-tutorial/postgresql-server-and-database-objects)

## Object Privileges

# Object Privileges

Object privileges in PostgreSQL are the permissions given to different user roles to access or modify database objects like tables, views, sequences, and functions. Ensuring proper object privileges is crucial for maintaining a secure and well-functioning database.

Learn more from the following resources:

- [@article@PostgreSQL Roles and Privileges Explained](https://www.aviator.co/blog/postgresql-roles-and-privileges-explained/)
- [@article@What are Object Privileges?](https://www.prisma.io/dataguide/postgresql/authentication-and-authorization/managing-privileges#what-are-postgresql-object-privileges)

## Olap

# OLAP

Online Analytical Processing (OLAP) in PostgreSQL refers to a class of systems designed for query-intensive tasks, typically used for data analysis and business intelligence. OLAP systems handle complex queries that aggregate large volumes of data, often from multiple sources, to support decision-making processes. PostgreSQL supports OLAP workloads through features such as advanced indexing, table partitioning, and the ability to create materialized views for faster query performance. Additionally, PostgreSQL's support for parallel query execution and extensions like Foreign Data Wrappers (FDW) and PostGIS enhance its capability to handle large datasets and spatial data, making it a robust platform for analytical applications.

Learn more from the following resources:

- [@article@Transforming Postgres into a Fast OLAP Database](https://blog.paradedb.com/pages/introducing_analytics)
- [@video@Online Analytical Processing](https://www.youtube.com/watch?v=NuVAgAgemGI)

## Oltp

# Workload Dependant Tuning

Online Transaction Processing (OLTP) in PostgreSQL refers to a class of systems designed to manage transaction-oriented applications, typically for data entry and retrieval transactions in database systems. OLTP systems are characterized by a large number of short online transactions (INSERT, UPDATE, DELETE), where the emphasis is on speed, efficiency, and maintaining data integrity in multi-access environments. PostgreSQL supports OLTP workloads through features like ACID compliance (Atomicity, Consistency, Isolation, Durability), MVCC (Multi-Version Concurrency Control) for high concurrency, efficient indexing, and robust transaction management. These features ensure reliable, fast, and consistent processing of high-volume, high-frequency transactions critical to OLTP applications.

Learn more from the following resources:

- [@video@OLTP vs OLAP](https://www.youtube.com/watch?v=iw-5kFzIdgY)
- [@article@What is OLTP?](https://www.oracle.com/uk/database/what-is-oltp/)

## Operators

# Operators in Kubernetes Deployment

Operators in Kubernetes are software extensions that use custom resources to manage applications and their components. They encapsulate operational knowledge and automate complex tasks such as deployments, backups, and scaling. Using Custom Resource Definitions (CRDs) and custom controllers, Operators continuously monitor the state of the application and reconcile it with the desired state, ensuring the system is self-healing and resilient. Popular frameworks for building Operators include the Operator SDK, Kubebuilder, and Metacontroller, which simplify the process and enhance Kubernetes' capability to manage stateful and complex applications efficiently.

- [@roadmap@Visit Dedicated Kubernetes Roadmap](https://roadmap.sh/kubernetes)
- [@official@Kubernetes](https://kubernetes.io/)
- [@article@Kubernetes Operators](https://kubernetes.io/docs/concepts/extend-kubernetes/operator/)

## Package Managers

# Package Managers

Package managers are essential tools that help you install, update, and manage software packages on your system. They keep track of dependencies, handle configuration files and ensure that the installation process is seamless for the end-user.

Visit the following resources to learn more:

- [@official@Install PostgreSQL with APT](https://www.postgresql.org/download/linux/ubuntu/)
- [@official@Install PostgreSQL with YUM & DNF](https://www.postgresql.org/download/linux/redhat/)
- [@official@Install PostgreSQL with Homebrew](https://wiki.postgresql.org/wiki/Homebrew)

## Patroni Alternatives

# Alternatives to Patroni for PostgreSQL Cluster Management

While Patroni is a popular choice for managing PostgreSQL clusters, there are several other tools and frameworks available that you might consider as alternatives to Patroni. Each of these has its unique set of features and benefits, and some may be better suited to your specific requirements or use-cases.

Several alternatives to Patroni exist for PostgreSQL cluster management, each with unique features catering to specific needs. **Stolon**, a cloud-native manager by Sorint.lab, ensures high availability and seamless scaling. **Pgpool-II**, by the Pgpool Global Development Group, offers load balancing, connection pooling, and high availability. **Repmgr**, developed by 2ndQuadrant, simplifies replication and cluster administration. **PAF (PostgreSQL Automatic Failover)**, created by Dalibo, provides lightweight failover management using Pacemaker and Corosync. These tools present diverse options for managing PostgreSQL clusters effectively.  

Visit the following resources to learn more:

- [@opensources@sorintlab/stolen](https://github.com/sorintlab/stolon)
- [@official@RepMgr](https://repmgr.org/)
- [@official@pgPool](https://www.pgpool.net/mediawiki/index.php/Main_Page)
- [@opensource@dalibo/PAF](https://github.com/dalibo/PAF)

## Patroni

# Patroni

Patroni is an open-source tool that automates the setup, management, and failover of PostgreSQL clusters, ensuring high availability. It leverages distributed configuration stores like Etcd, Consul, or ZooKeeper to maintain cluster state and manage leader election. Patroni continuously monitors the health of PostgreSQL instances, automatically promoting a replica to primary if the primary fails, minimizing downtime. It simplifies the complexity of managing PostgreSQL high availability by providing built-in mechanisms for replication, failover, and recovery, making it a robust solution for maintaining PostgreSQL clusters in production environments.

Learn more from the following resources:

- [@opensource@zalando/patroni](https://github.com/zalando/patroni)

## Patterns  Antipatterns

# Practical Patterns and Antipatterns for Queues in PostgreSQL

Practical patterns for implementing queues in PostgreSQL include using a dedicated table to store queue items, leveraging the `FOR` `UPDATE` `SKIP` `LOCKED` clause to safely dequeue items without conflicts, and partitioning tables to manage large volumes of data efficiently. Employing batch processing can also enhance performance by processing multiple queue items in a single transaction. Antipatterns to avoid include using high-frequency polling, which can lead to excessive database load, and not handling concurrency properly, which can result in data races and deadlocks. Additionally, storing large payloads directly in the queue table can degrade performance; instead, store references to the payloads. By following these patterns and avoiding antipatterns, you can build efficient and reliable queuing systems in PostgreSQL.

Learn more from the following resources:

- [@article@Postgres as Queue](https://leontrolski.github.io/postgres-as-queue.html)
- [@video@Can PostgreSQL Replace Your Messaging Queue?](https://www.youtube.com/watch?v=IDb2rKhzzt8)

## Per User Per Database Setting

# Per-User Per-Database Settings in PostgreSQL

In PostgreSQL, per-user and per-database settings allow administrators to customize configurations for specific users or databases, enhancing performance and management. These settings are managed using the ALTER ROLE and ALTER DATABASE commands.

These commands store the settings in the system catalog and apply them whenever the user connects to the database or the database is accessed. Commonly customized parameters include search_path, work_mem, and maintenance_work_mem, allowing fine-tuned control over query performance and resource usage tailored to specific needs.

Learn more from the following resources:

- [@official@ALTER ROLE](https://www.postgresql.org/docs/current/sql-alterrole.html)
- [@official@ALTER DATABASE](https://www.postgresql.org/docs/current/sql-alterdatabase.html)

## Perf Tools

# Profiling with Perf Tools

Perf tools is a suite of performance analysis tools that comes as part of the Linux kernel. It enables you to monitor various performance-related events happening in your system, such as CPU cycles, instructions executed, cache misses, and other hardware-related metrics. These tools can be helpful in understanding the bottlenecks and performance issues in your PostgreSQL instance and can be used to discover areas of improvement.

Learn more from the following resources:

- [@article@Profiling with Linux perf tool](https://mariadb.com/kb/en/profiling-with-linux-perf-tool/)
- [@official@perf: Linux profiling with performance counters ](https://perf.wiki.kernel.org/index.php/Main_Page)

## Pev2

# PEV2

`pev2`, or *Postgres Explain Visualizer v2*, is an open-source tool designed to make query analysis with PostgreSQL easier and more understandable. By providing a visual representation of the `EXPLAIN ANALYZE` output, `pev2` simplifies query optimization by displaying the query plan and execution metrics in a readable structure.

Learn more from the following resources:

- [@opensource@dalibo/pev2](https://github.com/dalibo/pev2)

## Pg Basebackup

# Backup Recovery Tools: pg_basebackup

`pg_basebackup` is a utility for creating a physical backup of a PostgreSQL database cluster. It generates a consistent backup of the entire database cluster by copying data files while ensuring write operations do not interfere. Typically used for setting up streaming replication or disaster recovery, `pg_basebackup` can be run in parallel mode to speed up the process and can output backups in tar format or as a plain directory. It ensures minimal disruption to database operations during the backup process.

Learn more from the following resources:

- [@official@pg_basebackup](https://www.postgresql.org/docs/current/app-pgbasebackup.html)
- [@article@Understanding the new pg_basebackup options](https://www.postgresql.fastware.com/blog/understanding-the-new-pg_basebackup-options)

## Pg Dump

# pg_dump: A PostgreSQL Backup Tool

`pg_dump` is a utility for backing up a PostgreSQL database by exporting its data and schema. Unlike `pg_basebackup`, which takes a physical backup of the entire cluster, `pg_dump` produces a logical backup of a single database. It can output data in various formats, including plain SQL, custom, directory, and tar, allowing for flexible restore options. `pg_dump` can be used to selectively backup specific tables, schemas, or data, making it suitable for tasks like migrating databases or creating development copies. The utility ensures the backup is consistent by using the database's built-in mechanisms to capture a snapshot of the data at the time of the dump.

Learn more from the following resources:

- [@official@pg_dump](https://www.postgresql.org/docs/current/app-pgdump.html)
- [@article@pg_dump - VMWare](https://docs.vmware.com/en/VMware-Greenplum/5/greenplum-database/utility_guide-client_utilities-pg_dump.html)

## Pg Dumpall

# pg_dumpall: Backing Up Entire PostgreSQL Clusters

`pg_dumpall` is a utility for backing up all databases in a PostgreSQL cluster, including cluster-wide data such as roles and tablespaces. It creates a plain text SQL script file that contains the commands to recreate the cluster's databases and their contents, as well as the global objects. This utility is useful for comprehensive backups where both database data and cluster-wide settings need to be preserved. Unlike `pg_dump`, which targets individual databases, `pg_dumpall` ensures that the entire PostgreSQL cluster can be restored from the backup, making it essential for complete disaster recovery scenarios.

Learn more from the following resources:

- [@official@pg_dumpall](https://www.postgresql.org/docs/current/app-pg-dumpall.html)
- [@article@pg_dump & pg_dumpall](https://www.postgresqltutorial.com/postgresql-administration/postgresql-backup-database/)

## Pg Hbaconf

# PostgreSQL Security: pg_hba.conf

When securing your PostgreSQL database, one of the most important components to configure is the `pg_hba.conf` (short for PostgreSQL Host-Based Authentication Configuration) file. This file is a part of PostgreSQL's Host-Based Authentication (HBA) system and is responsible for controlling how clients authenticate and connect to your database. 

Learn more from the following resources:

- [@official@The pg_hba.conf file](https://www.postgresql.org/docs/current/auth-pg-hba-conf.html)

## Pg Probackup

# Pg_probackup

`pg_probackup` is a backup and recovery manager for PostgreSQL, designed to handle periodic backups of PostgreSQL clusters. It supports incremental backups, merge strategies to avoid frequent full backups, validation, and parallelization for efficiency. It also offers features like backup from standby servers, remote operations, and compression. With support for PostgreSQL versions 11 through 16, it enables comprehensive management of backups and WAL archives, ensuring data integrity and efficient recovery processes.

Learn more from the following resources:

- [@opensource@postgrespro/pg_probackup](https://github.com/postgrespro/pg_probackup)
- [@official@PostgresPro Website](https://postgrespro.com/products/extensions/pg_probackup)

## Pg Restore

# pg_restore

`pg_restore` is a utility for restoring PostgreSQL database backups created by `pg_dump` in non-plain-text formats (custom, directory, or tar). It allows for selective restoration of database objects such as tables, schemas, or indexes, providing flexibility to restore specific parts of the database. `pg_restore` can also be used to reorder data load operations, create indexes and constraints after data load, and parallelize the restore process to speed up recovery. This utility ensures efficient and customizable restoration from logical backups.

- [@official@pg_restore](https://www.postgresql.org/docs/current/app-pgrestore.html)
- [@article@A guide to pg_restore](https://www.timescale.com/learn/a-guide-to-pg_restore-and-pg_restore-example)

## Pg Stat Activity

# Pg Stat Activity

`pg_stat_activity` is a crucial system view in PostgreSQL that provides real-time information on current database connections and queries being executed. This view is immensely helpful when troubleshooting performance issues, identifying long-running or idle transactions, and managing the overall health of the database. `pg_stat_activity` provides you with valuable insights into database connections and queries, allowing you to monitor, diagnose, and act accordingly to maintain a robust and optimally performing system.

Learn more from the following resources:

- [@official@pg_state_activity](https://www.postgresql.org/docs/current/monitoring-stats.html#MONITORING-PG-STAT-ACTIVITY-VIEW)
- [@article@Understanding pg_stat_activity](https://www.depesz.com/2022/07/05/understanding-pg_stat_activity/)

## Pg Stat Statements

# Pg Stat Statements

**Pg Stat Statements** is a system view in PostgreSQL that provides detailed statistics on the execution of SQL queries. It is particularly useful for developers and database administrators to identify performance bottlenecks, optimize query performance, and troubleshoot issues. This view can be queried directly or accessed through various administration tools. To use Pg Stat Statements, you need to enable the `pg_stat_statements` extension by adding the following line to the `postgresql.conf` configuration file.

Learn more from the following resources:

- [@official@pg_stat_statements](https://www.postgresql.org/docs/current/pgstatstatements.html)
- [@article@Using pg_stat_statements to Optimize Queries](https://www.timescale.com/blog/using-pg-stat-statements-to-optimize-queries/)

## Pgbackrest

# pgBackRest: A Comprehensive Backup and Recovery Solution

pgBackRest is a robust backup and restore solution for PostgreSQL, designed for high performance and reliability. It supports full, differential, and incremental backups, and provides features like parallel processing, backup validation, and compression to optimize storage and speed. pgBackRest also includes support for point-in-time recovery (PITR), encryption, and remote operations. Its configuration flexibility and extensive documentation make it suitable for various PostgreSQL deployment scenarios, ensuring efficient data protection and disaster recovery.

- [@official@pgBackRest documentation](https://pgbackrest.org)
- [@opensource@pgbackrest/pgbackrest](https://github.com/pgbackrest/pgbackrest)

## Pgbadger

# PgBadger

PgBadger is a fast, efficient PostgreSQL log analyzer and report generator. It parses PostgreSQL log files to generate detailed reports on database performance, query statistics, connection information, and more. PgBadger supports various log formats and provides insights into slow queries, index usage, and overall database activity. Its reports, typically in HTML format, include visual charts and graphs for easy interpretation. PgBadger is valuable for database administrators looking to optimize performance and troubleshoot issues based on log data.

Learn more from the following resources:

- [@opensource@darold/pgbadger](https://github.com/darold/pgbadger)
- [@article@PGBadger - Postgresql log analysis made easy](https://dev.to/full_stack_adi/pgbadger-postgresql-log-analysis-made-easy-54ki)

## Pgbouncer Alternatives

# Connection Pooling: Alternatives to PgBouncer

Pgpool-II, HAProxy, and Odyssey are prominent tools for enhancing PostgreSQL performance and availability. **Pgpool-II** is a versatile connection pooler offering load balancing, replication, and connection limits to optimize performance. **HAProxy** excels as a load balancer for distributing connections across PostgreSQL servers, featuring health checks and SSL/TLS support for secure, high-availability setups. **Odyssey**, developed by Yandex, is a multithreaded connection pooler designed for high-performance deployments, providing advanced routing, transparent SSL, and load balancing capabilities tailored for large-scale systems.

Learn more from the following resources:

- [@opensource@yandex/odyssey](https://github.com/yandex/odyssey)
- [@official@HAProxy Website](http://www.haproxy.org/)
- [@official@PGPool Website](https://www.pgpool.net/mediawiki/index.php/Main_Page)

## Pgbouncer

# PgBouncer

PgBouncer is a lightweight connection pooler for PostgreSQL, designed to reduce the overhead associated with establishing new database connections. It sits between the client and the PostgreSQL server, maintaining a pool of active connections that clients can reuse, thus improving performance and resource utilization. PgBouncer supports multiple pooling modes, including session pooling, transaction pooling, and statement pooling, catering to different use cases and workloads. It is highly configurable, allowing for fine-tuning of connection limits, authentication methods, and other parameters to optimize database access and performance.

- [@official@PgBouncer Website](https://www.pgbouncer.org/)
- [@opensource@pgbouncer/pgbouncer](https://github.com/pgbouncer/pgbouncer)

## Pgcenter

# pgcenter

`pgcenter` is a command-line tool that provides real-time monitoring and management for PostgreSQL databases. It offers a convenient interface for tracking various aspects of database performance, allowing users to quickly identify bottlenecks, slow queries, and other potential issues. With its numerous features and easy-to-use interface, `pgcenter` is an essential tool in the toolbox of anyone working with PostgreSQL databases.

Learn more from the following resources:

- [@opensource@lesovsky/pgcenter](https://github.com/lesovsky/pgcenter)

## Pgcluu

# pgCluu

PgCluu is a powerful and easy-to-use PostgreSQL performance monitoring and tuning tool. This open-source program collects statistics and provides various metrics in order to analyze PostgreSQL databases, helping you discover performance bottlenecks and optimize your cluster's performance. Apart from PostgreSQL-specific settings, you can also tweak other options, such as the RRDtool's data file format (JPG or SVG), time range for graphs, and more.

Learn more from the following resources:

- [@official@pgCluu Website](https://pgcluu.darold.net/)
- [@opensource@darold/pgcluu](https://github.com/darold/pgcluu)

## Pgq

# Skytools PGQ

Skytools is a set of tools developed by Skype to assist with using PostgreSQL databases. One of the key components of Skytools is PGQ, a queuing system built on top of PostgreSQL that provides efficient and reliable data processing.

Learn more from the following resources:

- [@opensource@PgQ — Generic Queue for PostgreSQL](https://github.com/pgq)

## Physical Storage And File Layout

# Physical Storage and File Layout

PostgreSQL's physical storage and file layout optimize data management and performance through a structured organization within the data directory, which includes subdirectories like `base` for individual databases, `global` for cluster-wide tables, `pg_wal` for Write-Ahead Logs ensuring durability, and `pg_tblspc` for tablespaces allowing flexible storage management. Key configuration files like `postgresql.conf`, `pg_hba.conf`, and `pg_ident.conf` are also located here. This layout facilitates efficient data handling, recovery, and maintenance, ensuring robust database operations.

Learn more from the following resources:

- [@article@What is $PGDATA in PostgreSQL?](https://stackoverflow.com/questions/26851709/what-is-pgdata-in-postgresql)
- [@official@TOAST](https://www.postgresql.org/docs/current/storage-toast.html)

## Plpgsql

# PL/pgSQL - Procedural Language for PostgreSQL

`PL/pgSQL` is a procedural language for the PostgreSQL database system that enables you to create stored procedures and functions using conditionals, loops, and other control structures, similar to a traditional programming language. Using PL/pgSQL, you can perform complex operations on the server-side, reducing the need to transfer data between the server and client. This can significantly improve performance, and it enables you to encapsulate and modularize your logic within the database.

Learn more from the following resources:

- [@official@PL/pgSQL — SQL Procedural Language](https://www.postgresql.org/docs/current/plpgsql.html)
- [@article@PostgreSQL PL/pgSQL](https://www.postgresqltutorial.com/postgresql-plpgsql/)

## Postgresql Anonymizer

# PostgreSQL Anonymizer

PostgreSQL Anonymizer is an extension designed to mask or anonymize sensitive data within PostgreSQL databases. It provides various anonymization techniques, including randomization, generalization, and pseudonymization, to protect personal and sensitive information in compliance with data privacy regulations like GDPR. This extension can be configured to apply these techniques to specific columns or datasets, ensuring that the anonymized data remains useful for development, testing, or analysis without exposing actual sensitive information.

- [@opensource@dalibo/postgresql_anonymizer](https://github.com/dalibo/postgresql_anonymizer)
- [@official@PostgreSQL Anonymizer Website](https://postgresql-anonymizer.readthedocs.io/en/stable/)

## Postgresql Vs Nosql Databases

# PostgreSQL vs NoSQL

PostgreSQL, a powerful open-source relational database system, excels in handling complex queries, ensuring data integrity, and supporting ACID transactions, making it ideal for applications requiring intricate data relationships and strong consistency. It offers advanced features like JSON support for semi-structured data, full-text search, and extensive indexing capabilities. In contrast, NoSQL databases, such as MongoDB or Cassandra, prioritize scalability and flexibility, often supporting schema-less designs that make them suitable for handling unstructured or semi-structured data and high-velocity workloads. These databases are typically used in scenarios requiring rapid development, horizontal scaling, and high availability, often at the cost of reduced consistency guarantees compared to PostgreSQL.

Learn more from the following resources:

- [@article@What’s the Difference Between MongoDB and PostgreSQL?](https://aws.amazon.com/compare/the-difference-between-mongodb-and-postgresql/)
- [@article@MongoDB vs PostgreSQL: 15 Critical Differences](https://kinsta.com/blog/mongodb-vs-postgresql/)

## Postgresql Vs Other Rdbms

# PostgreSQL vs. Other Databases

PostgreSQL stands out among other RDBMS options due to its open-source nature, advanced features, and robust performance. Unlike proprietary systems like Oracle or Microsoft SQL Server, PostgreSQL is free to use and highly extensible, allowing users to add custom functions, data types, and operators. It supports a wide range of indexing techniques and provides advanced features such as full-text search, JSON support, and geographic information system (GIS) capabilities through PostGIS. Additionally, PostgreSQL's strong adherence to SQL standards ensures compatibility and ease of migration. While systems like MySQL are also popular and known for their speed in read-heavy environments, PostgreSQL often surpasses them in terms of functionality and compliance with ACID properties, making it a versatile choice for complex, transactional applications.

Learn more from the following resources:

- [@article@PostgreSQL vs MySQL: The Critical Differences](https://www.integrate.io/blog/postgresql-vs-mysql-which-one-is-better-for-your-use-case/)
- [@article@Whats the difference between PostgreSQL and MySQL?](https://aws.amazon.com/compare/the-difference-between-mysql-vs-postgresql/)

## Practical Patterns  Antipatterns

# Practical Patterns for Migrations

Practical patterns for PostgreSQL migrations include using version control tools like Liquibase or Flyway to manage schema changes, applying incremental updates to minimize risk, maintaining backward compatibility during transitions, and employing zero-downtime techniques like rolling updates. Data migration scripts should be thoroughly tested in staging environments to ensure accuracy. Employing transactional DDL statements helps ensure atomic changes, while monitoring and having rollback plans in place can quickly address any issues. These strategies ensure smooth, reliable migrations with minimal application disruption.

Learn more from the following resources:

- [@official@Liquibase Website](https://www.liquibase.com/)
- [@official@Flyway Website](https://flywaydb.org/)

## Procedures And Functions

# Procedures and Functions in PostgreSQL

In PostgreSQL, functions and procedures encapsulate reusable logic within the database to enhance performance and maintain organization. Functions return a value or a table, take input parameters, and are used in SQL queries, defined with `CREATE FUNCTION`. Procedures, introduced in PostgreSQL 11, do not return values but can perform actions and include transaction control commands like `COMMIT` and `ROLLBACK`, defined with `CREATE PROCEDURE` and called using the `CALL` statement. Key differences include functions' mandatory return value and integration in SQL queries, while procedures focus on performing operations and managing transactions.

Learn more from the following resources:

- [@official@CREATE PROCEDURE](https://www.postgresql.org/docs/current/sql-createprocedure.html)
- [@official@CREATE FUNCTION](https://www.postgresql.org/docs/current/sql-createfunction.html)
- [@article@PostgreSQL CREATE PROCEDURE](https://www.postgresqltutorial.com/postgresql-plpgsql/postgresql-create-procedure/)

## Processes  Memory Architecture

# Process Memory Architecture in PostgreSQL

PostgreSQL’s process memory architecture is designed to efficiently manage resources and ensure performance. It consists of several key components:

- Shared Memory: This is used for data that needs to be accessed by all server processes, such as the shared buffer pool (shared_buffers), which caches frequently accessed data pages, and the Write-Ahead Log (WAL) buffers (wal_buffers), which store transaction log data before it is written to disk.
- Local Memory: Each PostgreSQL backend process (one per connection) has its own local memory for handling query execution. Key components include the work memory (work_mem) for sorting operations and hash tables, and the maintenance work memory (maintenance_work_mem) for maintenance tasks like vacuuming and index creation.
- Process-specific Memory: Each process allocates memory dynamically as needed for tasks like query parsing, planning, and execution. Memory contexts within each process ensure efficient memory usage and cleanup.
- Temporary Files: For operations that exceed available memory, such as large sorts or hash joins, PostgreSQL spills data to temporary files on disk.

Learn more from the following resources:

- [@article@Understanding PostgreSQL Shared Memory](https://stackoverflow.com/questions/32930787/understanding-postgresql-shared-memory)
- [@article@Understanding The Process and Memory Architecture of PostgreSQL](https://dev.to/titoausten/understanding-the-process-and-memory-architecture-of-postgresql-5hhp)

## Prometheus

# Prometheus: An Effective Monitoring Tool

Prometheus is an open-source systems monitoring and alerting toolkit designed for reliability and scalability. Originally developed at SoundCloud, it is now a part of the Cloud Native Computing Foundation. Prometheus collects metrics from configured targets at specified intervals, evaluates rule expressions, displays results, and can trigger alerts if certain conditions are met. It features a powerful query language called PromQL, a multi-dimensional data model based on time-series data identified by metric names and key/value pairs, and an efficient storage system. Prometheus is highly adaptable, supporting service discovery mechanisms and static configurations, making it a robust choice for monitoring dynamic cloud environments and microservices architectures.

Learn more from the following resources:

- [@official@Prometheus Website](https://prometheus.io/)
- [@article@Prometheus Monitoring](https://www.tigera.io/learn/guides/prometheus-monitoring/)

## Puppet

# Puppet: Configuration Management for PostgreSQL

Puppet is an open-source software configuration management tool that enables system administrators to automate the provisioning, configuration, and management of a server infrastructure. It helps minimize human errors, ensures consistency across multiple systems, and simplifies the process of managing PostgreSQL installations.

Learn more from the following resources:

- [@official@Puppet Documentation](https://puppet.com/docs/puppet/latest/index.html)
- [@official@Puppet PostgreSQL Module Documentation](https://forge.puppet.com/modules/puppetlabs/postgresql/)

## Queries

# Queries in PostgreSQL

Queries are the primary way to interact with a PostgreSQL database and retrieve or manipulate data stored within its tables. In this section, we will cover the fundamentals of querying in PostgreSQL - from basic `SELECT` statements to more advanced techniques like joins, subqueries, and aggregate functions.

Learn more from the following resources:

- [@official@Querying a Table](https://www.postgresql.org/docs/current/tutorial-select.html)

## Query Planner

# Query Planner in PostgreSQL

The PostgreSQL query planner is an essential component of the system that's responsible for optimizing the execution of SQL queries. It finds the most efficient way to join tables, establish subquery relationships, and determine the order of operations based on available data, query structure, and the current PostgreSQL configuration settings.

Learn more from the following resources:

- [@official@Planner/Optimizer](https://www.postgresql.org/docs/current/planner-optimizer.html)
- [@official@Query Planning](https://www.postgresql.org/docs/current/runtime-config-query.html)

## Query Processing

# Query Processing in PostgreSQL

Query processing is an important aspect of a database system, as it is responsible for managing data retrieval and modification using Structured Query Language (SQL) queries. Efficient query processing is crucial for ensuring optimal database performance.

Learn more from the following resources:

- [@article@Query Processing in PostgreSQL](https://www.interdb.jp/pg/pgsql03.html)
- [@course@Understand PostgreSQL Query Processing - Microsoft](https://learn.microsoft.com/en-us/training/modules/understand-postgresql-query-process/)

## Querying Data

# Querying Data

Querying data with Data Manipulation Language (DML) in PostgreSQL involves using SQL statements to retrieve and manipulate data within the database. The primary DML statements for querying and modifying data are `SELECT`, `INSERT`, `UPDATE`, and `DELETE`.

Learn more from the following resources:

- [@official@SELECT](https://www.postgresql.org/docs/current/sql-select.html)
- [@official@INSERT](https://www.postgresql.org/docs/current/sql-insert.html)
- [@official@UPDATE](https://www.postgresql.org/docs/current/sql-update.html)
- [@official@DELETE](https://www.postgresql.org/docs/current/sql-delete.html)

## Rdbms Benefits And Limitations

# RDBMS Benefits and Limitations

Relational Database Management Systems (RDBMS) offer several benefits, including robust data integrity through ACID (Atomicity, Consistency, Isolation, Durability) compliance, powerful querying capabilities with SQL, and strong support for data relationships via foreign keys and joins. They are highly scalable vertically and can handle complex transactions reliably. However, RDBMS also have limitations such as difficulties in horizontal scaling, which can limit performance in highly distributed systems. They can be less flexible with schema changes, often requiring significant effort to modify existing structures, and may not be the best fit for unstructured data or large-scale, high-velocity data environments typical of some NoSQL solutions.

Learn more from the following resources:

- [@article@15 Advantages and Disadvantages of RDBMS](https://trainings.internshala.com/blog/advantages-and-disadvantages-of-rdbms/)
- [@article@Top 11 Advantages and Disadvantages of RDBMS You Should Know](https://webandcrafts.com/blog/advantages-disadvantages-rdbms)
- [@video@Limitations of Relational Databases](https://www.youtube.com/watch?v=t62DXEfIFy4)

## Recursive Cte

# Recursive CTE (Common Table Expressions)

Recursive CTEs are a powerful feature in SQL that allow you to build complex hierarchical queries, retrieve data stored in hierarchical structures or even perform graph traversal. In simple terms, a recursive CTE is a CTE that refers to itself in its own definition, creating a loop that iterates through the data until a termination condition is met.

Note that recursive CTEs can be complex, and it's important to ensure a proper termination condition to avoid infinite recursion. Also, be careful with the use of `UNION ALL` or `UNION`, as it may impact the results and the performance of your query.

Learn more from the following resources:

- [@article@PostgreSQL - Recursive Query](https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-recursive-query/)
- [@article@PostgreSQL Recursive Query Explained](https://elvisciotti.medium.com/postgresql-recursive-query-the-simplest-example-explained-f9b85e0a371b)

## Red

# Troubleshooting Methods: Analyzing 'red' Situations

The acronym stands for Rate, Errors, and Duration. These are request-scoped, not resource-scoped as the USE method is. Duration is explicitly taken to mean distributions, not averages.

The Rate is the number of requests per second. The Errors is the number of requests that failed. The Duration is the distribution of request durations.

The Red Method is a methodology for analyzing the performance of any system. It directs the construction of a checklist, which for server analysis can be used for quickly identifying resource bottlenecks or errors. It begins by posing questions, and then seeks answers, instead of beginning with given metrics (partial answers) and trying to work backwards.

Learn more from the following resources:

- [@article@The RED Method: A New Approach to Monitoring Microservices](https://thenewstack.io/monitoring-microservices-red-method)
- [@article@PostgreSQL, RED, Golden Signals](https://dataegret.com/2020/10/postgresql-red-golden-signals-getting-started/)

## Relational Model

# Relational Model

The relational model is an approach to organizing and structuring data using tables, also referred to as "relations". It was first introduced by Edgar F. Codd in 1970 and has since become the foundation for most database management systems (DBMS), including PostgreSQL. This model organizes data into tables with rows and columns, where each row represents a single record and each column represents an attribute or field of the record. 

Learn more from the following resources:

- [@article@What is the Relational Model?](https://www.postgresql.org/docs/7.1/relmodel-oper.html)

## Relations

# Relations in the Relational Model

In the relational model, a relation is essentially a table composed of rows and columns, where each row represents a unique record (or tuple) and each column represents an attribute of the data. The structure of a relation is defined by its schema, which specifies the relation's name and the names and data types of its attributes. Relations are governed by integrity constraints, such as domain constraints, key constraints, and referential integrity constraints, to ensure data accuracy and consistency. Operations like selection, projection, join, and others can be performed on relations to retrieve and manipulate data efficiently.

Learn more from the following resources:

- [@official@Domain Constraints](https://www.postgresql.org/docs/current/infoschema-domain-constraints.html)
- [@article@Relationships](https://hasura.io/learn/database/postgresql/core-concepts/6-postgresql-relationships/)

## Replication

# Replication in PostgreSQL

Replication, in simple terms, is the process of copying data from one database server to another. It helps in maintaining a level of redundancy and improving the performance of databases. Replication ensures that your database remains highly available, fault-tolerant, and scalable.

Learn more from the following resources:

- [@official@Replication](https://www.postgresql.org/docs/current/runtime-config-replication.html)
- [@article@PostgreSQL Replication](https://kinsta.com/blog/postgresql-replication/)

## Reporting Logging  Statistics

# Reporting Logging Statistics

When working with PostgreSQL, it is often useful to analyze the performance of your queries and system as a whole. This can help you optimize your database and spot potential bottlenecks. One way to achieve this is by reporting logging statistics. PostgreSQL provides configuration settings for generating essential logging statistics on query and system performance.

Learn more from the following resources:

- [@official@Error Reporting and Logging](https://www.postgresql.org/docs/current/runtime-config-logging.html)
- [@article@PostgreSQL Logging: Everything You Need to Know](https://betterstack.com/community/guides/logging/how-to-start-logging-with-postgresql/)

## Resource Usage  Provisioning  Capacity Planning

# Resource Usage, Provisioning, and Capacity Planning

Capacity planning and resource management are essential skills for professionals working with PostgreSQL. A well-designed infrastructure balances resource usage among the server, I/O, and storage systems to maintain smooth database operations. In this context, resource usage refers to the consumption of computational resources like CPU, memory, storage, and network resources. Planning for provisioning and capacity can help administrators run an efficient and scalable PostgreSQL infrastructure.

## Resource Usage

When monitoring your PostgreSQL database's performance, some factors to look out for include CPU, memory, disk I/O, and network usage.

- **CPU**: High CPU usage may indicate that queries are taking longer than expected, causing increased resource consumption by the system. It is crucial to monitor the CPU usage and optimize queries and indexes to avoid performance bottlenecks.
- **Memory**: A well-managed memory system can significantly speed up database operations. Monitor memory usage, as low memory utilization rates can lead to slow query responses and reduced performance.
- **Disk I/O**: Monitor disk read and write performance to avoid bottlenecks and maintain efficient database operations. Excessive write activities, heavy workload, or slow storage can affect the PostgreSQL's transaction processing.
- **Network**: Network problems might lead to slow response times or connectivity issues. Monitoring the network traffic can help identify any problems with the database, client connections, or replication.

## Provisioning

Proper resource provisioning is critical to ensure the system can handle the workload, while also being cost-effective. When dealing with PostgreSQL, there are three main aspects to consider:

- **Instance Size**: Resource allocation includes determining the appropriate instance size for your PostgreSQL server. Consider the expected workload for your database application and choose the right balance of CPU power, memory, and storage for your requirements.
- **Scaling**: Plan for the ability to scale your PostgreSQL database horizontally (by adding more nodes) or vertically (by increasing resources) to maintain system performance as your needs grow. This will help you accommodate fluctuating workloads, new applications, or changes in usage patterns.
- **High Availability**: Provision multiple PostgreSQL instances to form a high-availability (HA) setup, protecting against hardware failures and providing minimal downtime. In addition, PostgreSQL supports replication to ensure data durability and consistency across multiple nodes.

## Capacity Planning

Capacity planning is a dynamic process that includes forecasting the infrastructure requirements based on business assumptions and actual usage patterns. System requirements might change as new applications or users are added, or as the database grows in size. Consider the following factors when planning your PostgreSQL infrastructure:

- **Workload**: Understand the expected workload for your PostgreSQL database to determine database size, indexing, and caching requirements.
- **Data Storage**: Anticipate the growth of your data volume through regular database maintenance, monitoring, and by having storage expansion plans in place.
- **Performance Metrics**: Establish key performance indicators (KPIs) to measure performance, detect possible issues, and act accordingly to minimize service degradation.
- **Testing**: Simulate test scenarios and perform stress tests to identify bottlenecks and inconsistencies to adjust your infrastructure as needed.

Learn more from the following resources:

- [@official@Resource Consumption](https://www.postgresql.org/docs/current/runtime-config-resource.html)
- [@article@5 ways to host PostgreSQL databases](https://www.prisma.io/dataguide/postgresql/5-ways-to-host-postgresql)

## Resource Usage

# Resources Usage

Configuring PostgreSQL for optimal resource usage involves adjusting settings in the `postgresql.conf` file to balance memory, CPU, and disk usage. 

Key parameters include `shared_buffers`, typically set to 25-40% of total RAM, to optimize caching; `work_mem`, which should be adjusted based on the complexity and number of concurrent queries, often starting at 1-2MB per connection; `maintenance_work_mem`, set higher (e.g., 64MB) to speed up maintenance tasks; `effective_cache_size`, usually set to about 50-75% of total RAM to inform the planner about available cache; and `max_connections`, which should be carefully set based on available resources to avoid overcommitting memory. Additionally, `autovacuum` settings should be fine-tuned to ensure regular cleanup without overloading the system. Adjusting these parameters helps PostgreSQL efficiently utilize available hardware, improving performance and stability.

Learn more from the following resources:

- [@official@Resource Consumption Documentation](https://www.postgresql.org/docs/current/runtime-config-resource.html#RUNTIME-CONFIG-RESOURCE-MEMORY)
- [@article@effective_cache_size](https://docs.aws.amazon.com/prescriptive-guidance/latest/tuning-postgresql-parameters/effective-cache-size.html)

## Reviewing Patches

# Reviewing Patches

Reviewing patches is a vital contribution to PostgreSQL, ensuring quality control, maintaining project standards, and helping new contributors understand the system's internals. By identifying bugs, improving performance, and ensuring proper documentation and test coverage, reviewers uphold PostgreSQL's reliability and stability. To participate, subscribe to the *pgsql-hackers mailing list*, explore patches in the *commitfest schedule*, and provide constructive feedback on correctness, performance, and code quality. Engaging in this collaborative process is an impactful way to support the PostgreSQL community.  

Visit the following resources to learn more:

- [@official@pgsql-hackers Mailing List](https://www.postgresql.org/list/pgsql-hackers/)  
- [@official@Commitfest Schedule](https://commitfest.postgresql.org/)

## Roles

# PostgreSQL Roles

In PostgreSQL, roles are entities that manage database access permissions, combining user and group functionalities. Roles can own database objects and have privileges, such as the ability to create databases or tables. A role can be configured with login capabilities (login role), or it can be used purely for privilege management (group role). Roles can inherit permissions from other roles, simplifying the management of complex permission hierarchies. Key role attributes include `SUPERUSER` (full access), `CREATEDB` (ability to create databases), `CREATEROLE` (ability to create and manage other roles), and `REPLICATION` (replication-related privileges). Roles are created and managed using SQL commands such as `CREATE ROLE`, `ALTER ROLE`, and `DROP ROLE`.

Learn more from the following resources:

- [@video@For Your Eyes Only: Roles, Privileges, and Security in PostgreSQL](https://www.youtube.com/watch?v=mtPM3iZFE04)
- [@official@Database Roles](https://www.postgresql.org/docs/current/user-manag.html)
- [@official@Predefined Roles](https://www.postgresql.org/docs/current/predefined-roles.html)

## Row Level Security

# Row Level Security (RLS)

Row Level Security (RLS) is a feature introduced in PostgreSQL 9.5 that allows you to control access to rows in a table based on a user or role's permissions. This level of granularity in data access provides an extra layer of security for protecting sensitive information from unauthorized access.

Learn more from the following resources:

- [@official@Row Security Policies](https://www.postgresql.org/docs/current/ddl-rowsecurity.html)
- [@video@How to Setup Row Level Security (RLS) in PostgreSQL](https://www.youtube.com/watch?v=j53NoW9cPtY)

## Rows

# Rows in PostgreSQL

A row in PostgreSQL represents a single, uniquely identifiable record with a specific set of fields in a table. Each row in a table is made up of one or more columns, where each column can store a specific type of data (e.g., integer, character, date, etc.). The structure of a table determines the schema of its rows, and each row in a table must adhere to this schema.

Learn more from the following resources:

- [@official@PostgreSQL - Rows](https://www.postgresql.org/docs/current/functions-comparisons.html)

## Salt

# Salt - Configuration Management for PostgreSQL

Salt (SaltStack) is an open-source configuration management, remote execution, and automation tool that helps you manage, automate, and orchestrate your PostgreSQL infrastructure. Salt is an excellent choice for managing your PostgreSQL infrastructure, providing a powerful, flexible, and extensible solution to help you maintain consistency and automate common tasks seamlessly.

Learn more from the following resources:

- [@official@Saltstack Website](https://saltproject.io/index.html)
- [@opensource@saltstack/salt](https://github.com/saltstack/salt)

## Schema Design Patterns  Anti Patterns

# Schema Design Patterns in PostgreSQL

Schema design patterns in PostgreSQL ensure efficient and scalable databases by using normalization to reduce redundancy and maintain data integrity, while denormalization improves read performance for read-heavy applications. Employing star and snowflake schemas optimizes query performance in data warehousing, with the former having a central fact table and the latter normalizing dimension tables. Partitioning tables based on specific criteria enhances query performance and maintenance, while strategic use of indexes speeds up data retrieval. Foreign keys and constraints maintain data integrity, and materialized views precompute complex queries for faster access to summary data, collectively ensuring an optimized and robust database design.

Learn more from the following resources:

- [@article@How to Design Your PostgreSQL Database: Two Schema Examples](https://www.timescale.com/learn/how-to-design-postgresql-database-two-schema-examples)
- [@video@What is STAR schema | Star vs Snowflake Schema](https://www.youtube.com/watch?v=hQvCOBv_-LE)

## Schemas

# Schemas

Schemas are an essential part of PostgreSQL's object model, and they help provide structure, organization, and namespacing for your database objects. A schema is a collection of database objects, such as tables, views, indexes, and functions, that are organized within a specific namespace. 

Learn more from the following resources:

- [@official@Schemas](https://www.postgresql.org/docs/current/ddl-schemas.html)
- [@article@Schema in PostgreSQL](https://hasura.io/learn/database/postgresql/core-concepts/1-postgresql-schema/)

## Security

# PostgreSQL Security Concepts

Securing PostgreSQL involves multiple layers of considerations to protect data and ensure only authorized access.

Learn more from the following resources:

- [@article@PostgreSQL Database Security Best Practices](https://www.percona.com/blog/postgresql-database-security-best-practices/)
- [@article@Security - Azure Database for PostgreSQL](https://learn.microsoft.com/en-us/azure/postgresql/flexible-server/concepts-security)

## Sed

# Sed: The Stream Editor

Sed is a powerful command-line utility for text processing and manipulation in Unix-based systems, including Linux operating systems. It operates on a text stream – reading from a file, standard input, or a pipe from another command – and applies a series of editing instructions known as "scripts" to transform the input text into a desired output format.

Learn more from the following resources:

- [@article@sed, a stream editor](https://www.gnu.org/software/sed/manual/sed.html)
- [@article@How to use the sed command on Linux](https://www.howtogeek.com/666395/how-to-use-the-sed-command-on-linux/)

## Selinux

# SELinux

SELinux, or Security-Enhanced Linux, is a Linux kernel security module that brings heightened access control and security policies to your system. It is specifically designed to protect your system from unauthorized access and data leaks by enforcing a strict security policy, preventing processes from accessing resources they shouldn't, which is a significant tool for database administrators to help secure PostgreSQL instances.

Learn more from the following resources:

- [@article@What is SELinux?](https://www.redhat.com/en/topics/linux/what-is-selinux)
- [@article@Introduction to SELinux](https://github.blog/developer-skills/programming-languages-and-frameworks/introduction-to-selinux/)

## Set Operations

# Set Operations in PostgreSQL

Set operations are useful when you need to perform actions on whole sets of data, such as merging or comparing them. Set operations include UNION, INTERSECT, and EXCEPT, and they can be vital tools in querying complex datasets.

Learn more from the following resources:

- [@official@Combining Queries](https://www.postgresql.org/docs/current/queries-union.html)
- [@article@PostgreSQL UNION Operator](https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-union/)
- [@article@PostgreSQL INTERSECT Operator](https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-intersect/)
- [@article@PostgreSQL EXCEPT Operator](https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-except/)

## Sharding Patterns

# Sharding Patterns

Sharding is a technique that splits a large dataset across multiple database instances or servers, called shards. Each shard is an independent and self-contained unit that holds a portion of the overall data, and shards can be distributed across different geographical locations or infrastructures.

Learn more from the following resources:

- [@article@Exploring Effective Sharding Strategies with PostgreSQL](https://medium.com/@gustavo.vallerp26/exploring-effective-sharding-strategies-with-postgresql-for-scalable-data-management-2c9ae7ef1759)
- [@article@Mastering PostgreSQL Scaling: A Tale of Sharding and Partitioning](https://doronsegal.medium.com/scaling-postgres-dfd9c5e175e6)

## Shell Scripts

# Shell Scripts

Shell scripts are a powerful tool used to automate repetitive tasks and perform complex operations. They are essentially text files containing a sequence of commands to be executed by the shell (such as Bash or Zsh). By leveraging shell scripts with tools such as `cron`, you can efficiently automate tasks related to PostgreSQL and streamline your database administration processes.

Learn more from the following resources:

- [@article@Shell Script Cheatsheet](https://cheatsheets.zip/bash)
- [@article@Shell Scripting Tutorial](https://www.tutorialspoint.com/unix/shell_scripting.htm)
- [@video@Shell Scripting for Beginners](https://www.youtube.com/watch?v=cQepf9fY6cE&list=PLS1QulWo1RIYmaxcEqw5JhK3b-6rgdWO_)

## Simple Stateful Setup

# Simple Stateful Setup

Here are the key components and steps involved in setting up a simple stateful `PostgreSQL` deployment on `Kubernetes`:

- **Create a Storage Class**: Define a `StorageClass` resource in `Kubernetes`, specifying the type of storage to be used and the access mode (read-write, read-only, etc.).

- **Create a Persistent Volume Claim**: Define a `PersistentVolumeClaim` (PVC) to request a specific amount of storage from the storage class for your `PostgreSQL` database.

- **Create a ConfigMap**: Define a `ConfigMap` to store your database configuration settings (e.g., usernames, passwords, etc.), separate from your application code.

- **Create a Secret**: Store sensitive data (e.g., database passwords) securely in a `Secret` object. The `Secret` will be mounted as a volume in the pod and the environment variables will be set.

- **Create a StatefulSet**: Define a `StatefulSet` that manages the deployment of your `PostgreSQL` pods. Specify the container image, port, volumes (PVC and ConfigMap), and a startup script. It ensures the unique identifier for each pod and guarantees the order of pod creation/deletion.

Learn more from the following resources:

- [@article@How to Deploy Postgres to Kubernetes Cluster](https://www.digitalocean.com/community/tutorials/how-to-deploy-postgres-to-kubernetes-cluster)
- [@article@Deploy PostgreSQL on K8's](https://refine.dev/blog/postgres-on-kubernetes/)

## Sp Gist

# Using SP-GiST Indexes in PostgreSQL

The Spatial Generalized Search Tree (SP-GiST) is an advanced indexing structure in PostgreSQL designed to efficiently manage spatial and multidimensional data. Unlike traditional balanced trees like GiST, SP-GiST supports space-partitioning trees such as quad-trees and kd-trees, which are particularly useful for spatial data where the data space can be partitioned into non-overlapping regions.

SP-GiST is ideal for applications that involve complex spatial queries and need efficient indexing mechanisms for large datasets. It works by dividing the data space into smaller, manageable partitions, which helps in optimizing search operations and improving query performance. This structure is particularly beneficial in geographic information systems (GIS), spatial databases, and applications dealing with high-dimensional data.

Learn more from the following resources:

- [@article@PostgreSQL SP-GiST](https://www.slingacademy.com/article/postgresql-sp-gist-space-partitioned-generalized-search-tree/)
- [@article@(The Many) Spatial Indexes of PostGIS](https://www.crunchydata.com/blog/the-many-spatial-indexes-of-postgis)

## Sql Query Patterns  Anti Patterns

# SQL Query Patterns in PostgreSQL

Schema query patterns in PostgreSQL optimize data retrieval and manipulation by using indexes on frequently queried columns to speed up SELECT queries, optimizing joins with indexed foreign keys and appropriate join types, and leveraging table partitioning to limit data scans. Common Table Expressions (CTEs) break down complex queries for better readability and maintainability, while window functions allow advanced analytics within queries. Query caching and prepared statements reduce access times and execution overhead, respectively, and materialized views precompute and store complex query results for faster access. These patterns collectively enhance the efficiency, performance, and reliability of PostgreSQL queries.

Visit the following resources to learn more:

- [@official@PostgreSQL - Query Patterns](https://www.postgresql.org/docs/current/functions-matching.html)

## Ssl Settings

# SSL Settings in PostgreSQL

Securing the communication channels is a crucial aspect of protecting your PostgreSQL database from different types of attacks. One way to achieve this security is by using SSL (Secure Socket Layer) connections. By enabling and configuring SSL, you add an extra layer of security to your PostgreSQL database, ensuring the data transferred between the client and server is encrypted and protected.

Learn more from the following resources:

- [@official@SSL Support](https://www.postgresql.org/docs/current/libpq-ssl.html)
- [@article@How to Configure SSL on PostgreSQL](https://www.cherryservers.com/blog/how-to-configure-ssl-on-postgresql)
- [@video@How to use SSL in PostgreSQL The Right Way](https://www.youtube.com/watch?v=Y1lsbF9NWW0)

## Storage Parameters

# Storage Parameters in PostgreSQL

Storage parameters help optimize the database's performance by allowing you to configure settings related to memory usage, storage behavior, and buffer management for specific tables and indexes. PostgreSQL provides several configuration options to tailor the behavior of storage and I/O on a per-table or per-index basis. These options are set using the `ALTER TABLE` or `ALTER INDEX` commands, and they affect the overall performance of your database.

Learn more from the following resources:

- [@official@ALTER INDEX](https://www.postgresql.org/docs/current/sql-alterindex.html)
- [@article@PostgreSQL Storage Parameters](https://pgpedia.info/s/storage-parameters.html)
- [@article@SQL ALTER TABLE Statement](https://www.w3schools.com/sql/sql_alter.asp)

## Strace

# Strace

`strace` is a powerful command-line tool used to diagnose and debug programs on Linux systems. It allows you to trace the system calls made by the process you're analyzing, allowing you to observe its interaction with the operating system.

Learn more from the following resources:

- [@article@strace man page](https://man7.org/linux/man-pages/man1/strace.1.html)
- [@article@Understand system calls with strace](https://opensource.com/article/19/10/strace)

## Streaming Replication

# Streaming Replication in PostgreSQL

Streaming Replication is a powerful feature in PostgreSQL that allows efficient real-time replication of data across multiple servers. It is a type of asynchronous replication, meaning that the replication process occurs continuously in the background without waiting for transactions to be committed. The primary purpose of streaming replication is to ensure high availability and fault tolerance, as well as to facilitate load balancing for read-heavy workloads. In the context of PostgreSQL, streaming replication involves a *primary* server and one or more *standby* servers. The primary server processes write operations and then streams the changes (or write-ahead logs, also known as WAL) to the standby servers, which apply the changes to their local copies of the database. The replication is unidirectional – data flows only from the primary server to the standby servers.

Learn more from the following resources:

- [@article@Streaming Replication](https://wiki.postgresql.org/wiki/Streaming_Replication)
- [@video@Postgres Streaming Replication on Centos](https://www.youtube.com/watch?v=nnnAmq34STc)

## Subqueries

# Subqueries

A subquery is a query nested inside another query, often referred to as the outer query. Subqueries are invaluable tools for retrieving information from multiple tables, performing complex calculations, or applying filter criteria based on the results of other queries. They can be found in various parts of SQL statements, such as `SELECT`, `FROM`, `WHERE`, and `HAVING` clauses.

Learn more from the following resources:

- [@official@PostgreSQL Subquery](https://www.postgresql.org/docs/current/functions-subquery.html)
- [@article@PostgreSQL Subquery](https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-subquery/)
- [@article@PostgreSQL Subqueries](https://www.w3resource.com/PostgreSQL/postgresql-subqueries.php)

## Sysstat

# Sysstat

Sysstat is a collection of performance monitoring tools for Linux. It collects various system statistics, such as CPU usage, memory usage, disk activity, network traffic, and more. System administrators can use these tools to monitor the performance of their servers and identify potential bottlenecks and areas for improvement.

Learn more from the following resources:

- [@opensource@sysstat/sysstat](https://github.com/sysstat/sysstat)
- [@article@Sysstat – All-in-One System Performance and Usage Activity Monitoring Tool For Linux](https://www.tecmint.com/install-sysstat-in-linux/)

## System Catalog

# System Catalog

The PostgreSQL system catalog is a set of tables and views that store metadata about the database objects, providing critical information for database management and querying. Key system catalog tables include `pg_database` (information about databases), `pg_tables` (details of tables), `pg_indexes` (index information), `pg_class` (general information about tables, indexes, and sequences), `pg_attribute` (column details for each table), and `pg_roles` (user and role information). These catalogs enable the database engine and users to efficiently manage schema, security, and query optimization, ensuring effective database operations and maintenance.

Learn more from the following resources:

- [@official@System Catalogs](https://www.postgresql.org/docs/current/catalogs.html)
- [@article@Exploring the PostgreSQL System Catalogs](https://www.openlogic.com/blog/postgresql-system-catalog-overview)

## Tables

# Tables in PostgreSQL

A table is one of the primary data storage objects in PostgreSQL. In simple terms, a table is a collection of rows or records, organized into columns. Each column has a unique name and contains data of a specific data type.

Learn more from the following resources:

- [@official@Table Basics](https://www.postgresql.org/docs/current/ddl-basics.html)

## Temboard

# temBoard

temBoard is an open-source monitoring and management tool for PostgreSQL databases developed by Dalibo. It provides a web-based interface that helps database administrators (DBAs) manage and monitor multiple PostgreSQL instances efficiently. Key features of temBoard include:

1.	Real-Time Monitoring: Offers real-time insights into database performance metrics such as CPU usage, memory usage, disk I/O, and query performance. This helps DBAs quickly identify and address potential issues.
2.	Agent-Based Architecture: Uses a lightweight agent installed on each PostgreSQL instance to collect metrics and perform management tasks. This architecture ensures minimal performance impact on the monitored databases.
3.	Alerting and Notifications: Configurable alerts and notifications allow DBAs to receive timely updates on critical database events and performance issues, enabling proactive management and quicker response times.
4.	Performance Analysis: Provides detailed performance analysis tools, including query statistics and historical performance data. This allows DBAs to analyze trends, identify bottlenecks, and optimize database performance.
5.	User Management and Security: Supports user authentication and role-based access control, ensuring secure management of PostgreSQL instances. It also provides an audit log for tracking user activities.
6.	Plugin System: Extensible through plugins, allowing customization and addition of new features as needed.

Learn more from the following resources:

- [@official@temBoard Documentation](https://temboard.readthedocs.io/en/v8/)
- [@opensource@dalibo/temboard](https://github.com/dalibo/temboard)

## Tensor

# Tensor Query Language

Tensor Query Language (TQL) is a specialized SQL-like language designed for querying and managing datasets stored as tensors, primarily used within the Deep Lake platform. TQL extends traditional SQL capabilities to support multidimensional array operations, making it particularly useful for data science and machine learning workflows. Key features include array arithmetic, user-defined functions, and integration with deep learning frameworks like PyTorch and TensorFlow, allowing for efficient data manipulation and analysis directly within these environments.

TQL enables users to perform complex queries on datasets, including operations like embedding search, array slicing, and custom numeric computations. This flexibility supports a wide range of applications, from simple data retrieval to sophisticated data preprocessing steps needed for training machine learning models. The language also integrates with version control, allowing users to manage and query different versions of their datasets seamlessly.

Learn more from the following resources:

- [@official@Tensor Query Language Documentation](https://docs.activeloop.ai/examples/tql)

## Top

# Top Command in PostgreSQL

`top` is a command-line utility that comes pre-installed on most Unix-based operating systems such as Linux, macOS, and BSD. It provides a dynamic, real-time view of the processes running on a system, displaying valuable information like process ID, user, CPU usage, memory usage, and more.

Learn more from the following resources:

- [@article@How to Use the top Command in Linux](https://phoenixnap.com/kb/top-command-in-linux)
- [@article@top man page](https://man7.org/linux/man-pages/man1/top.1.html)
- [@video@Demystifying the Top Command in Linux](https://www.youtube.com/watch?v=WsR11EGF9PA)

## Transactions

# Transactions

Transactions are a fundamental concept in database management systems, allowing multiple statements to be executed within a single transaction context. In PostgreSQL, transactions provide ACID (Atomicity, Consistency, Isolation, and Durability) properties, which ensure that your data remains in a consistent state even during concurrent access or system crashes. By leveraging transaction control, savepoints, concurrency control, and locking, you can build robust and reliable applications that work seamlessly with PostgreSQL.

Learn more from the following resources:

- [@official@Transactions](https://www.postgresql.org/docs/current/tutorial-transactions.html)
- [@video@How to implement transactions](https://www.youtube.com/watch?v=DvJq4L41ru0)

## Transactions

# Transactions

Transactions are a fundamental concept in database management systems, allowing multiple statements to be executed within a single transaction context. In PostgreSQL, transactions provide ACID (Atomicity, Consistency, Isolation, and Durability) properties, which ensure that your data remains in a consistent state even during concurrent access or system crashes. By leveraging transaction control, savepoints, concurrency control, and locking, you can build robust and reliable applications that work seamlessly with PostgreSQL.

Learn more from the following resources:

- [@official@Transactions](https://www.postgresql.org/docs/current/tutorial-transactions.html)
- [@video@How to implement transactions](https://www.youtube.com/watch?v=DvJq4L41ru0)

## Triggers

# Advanced SQL: Triggers

Triggers are special user-defined functions that get invoked automatically when an event (like `INSERT`, `UPDATE`, `DELETE`, or `TRUNCATE`) occurs on a specified table or view. They allow you to perform additional actions when data is modified in the database, helping to maintain the integrity and consistency of your data.

Learn more from the following resources:

- [@official@Triggers](https://www.postgresql.org/docs/8.1/triggers.html)
- [@article@PostgreSQL Triggers](https://www.postgresqltutorial.com/postgresql-triggers/)
- [@article@Understanding PostgreSQL Triggers](https://hevodata.com/learn/postgresql-triggers/)
- [@video@Using PostgreSQL triggers to automate processes with Supabase](https://www.youtube.com/watch?v=0N6M5BBe9AE)

## Tuples

# Tuples

In the relational model, a **tuple** is a fundamental concept that represents a single record or row in a table. In PostgreSQL, a tuple is composed of a set of attribute values, each corresponding to a specific column or field in the table. A tuple is defined as an ordered set of attribute values, meaning that each value in a tuple corresponds to a specific attribute or column in the table. The values can be of different data types, such as integers, strings, or dates, depending on the schema of the table.

For example, consider a `users` table with columns `id`, `name`, and `email`. A sample tuple in this table could be `(1, 'John Smith', 'john.smith@example.com')`, where each value corresponds to its respective column. PostgreSQL provides a variety of operations that can be performed on tuples.

Learn more from the following resources:

- [@article@How PostgreSQL Freezes Tuples](https://medium.com/@hnasr/how-postgres-freezes-tuples-4a9931261fc)
- [@article@Whats the difference between and tuple and a row?](https://stackoverflow.com/questions/19799282/whats-the-difference-between-a-tuple-and-a-row-in-postgres)

## Use

# Troubleshooting Methods - Use

The Utilization Saturation and Errors (USE) Method is a methodology for analyzing the performance of any system. It directs the construction of a checklist, which for server analysis can be used for quickly identifying resource bottlenecks or errors. It begins by posing questions, and then seeks answers, instead of beginning with given metrics (partial answers) and trying to work backwards.

Learn more from the following resources:

- [@article@The USE Method](https://www.brendangregg.com/usemethod.html)
- [@article@Making the USE method of monitoring useful](https://www.infoworld.com/article/2270621/making-the-use-method-of-monitoring-useful.html)
- [@article@Adopting monitoring frameworks - RED and USE ](https://lantern.splunk.com/Observability/Product_Tips/Observability_Cloud/Adopting_monitoring_frameworks_-_RED_and_USE)

## Using Docker

# Using Docker for PostgreSQL Installation and Setup

Docker is an excellent tool for simplifying the installation and management of applications, including PostgreSQL. By using Docker, you can effectively isolate PostgreSQL from your system and avoid potential conflicts with other installations or configurations.

Learn more from the following resources:

- [@official@Official PostgresSQL Docker Image](https://hub.docker.com/_/postgres)
- [@video@How to Set Up a PostgreSQL Database with Docker](https://www.youtube.com/watch?v=RdPYA-wDhTA)
- [@article@How to Use the Postgres Docker Official Image](https://www.docker.com/blog/how-to-use-the-postgres-docker-official-image/)

## Using Logical Replication

# 4.2 Using Logical Replication

Logical replication is an asynchronous feature that allows data modification to be transferred from a source (publisher) to a target system (subscriber) across different PostgreSQL database versions. It provides more granular control over the data copied and is useful during an upgrade.

**Advantages of Logical Replication**

- It allows you to replicate only specific tables, rather than the entire database.
- You can create replicas with different database schemas by using a transformation layer between publisher and subscriber.
- It allows you to perform a live upgrade, avoiding the downtime of your database.

Learn more from the following resources:

- [@official@Logical Replication](https://www.postgresql.org/docs/current/logical-replication.html)
- [@youtube@PostgreSQL Logical Replication Guide](https://www.youtube.com/watch?v=OvSzLjkMmQo)

## Using Pg Ctl

# Using `pg_ctl`

`pg_ctl` is a command-line utility that enables you to manage a PostgreSQL database server. With `pg_ctl`, you can start, stop, and restart the PostgreSQL service, among other tasks.

Learn more from the following resources:

- [@official@pg_ctl](https://www.postgresql.org/docs/current/app-pg-ctl.html)
- [@article@pg_ctl Tips and Tricks](https://pgdash.io/blog/pgctl-tips-tricks.html)

## Using Pg Ctlcluster

# Using pg_ctlcluster

`pg_ctlcluster` is a command-line utility provided by PostgreSQL to manage database clusters. It is especially helpful for users who have multiple PostgreSQL clusters running on the same system.

Learn more from the following resources:

- [@article@pg_ctlcluster](https://manpages.ubuntu.com/manpages/focal/man1/pg_ctlcluster.1.html)

## Using Pg Upgrade

# Using pg_upgrade

`pg_upgrade` is a PostgreSQL utility that facilitates the in-place upgrade of a PostgreSQL database cluster to a new major version. It allows users to upgrade their database without needing to dump and restore the database, significantly reducing downtime. Here are the key steps involved in using `pg_upgrade`:

1. **Preparation**: Before starting the upgrade, ensure both the old and new versions of PostgreSQL are installed. Backup the existing database cluster and ensure no connections are active.

2. **Initialize the New Cluster**: Initialize a new PostgreSQL cluster with the target version using `initdb`.

3. **Run `pg_upgrade`**: Execute the `pg_upgrade` command, specifying the data directories of the old and new clusters, and the paths to the old and new `pg_ctl` binaries.

4. **Analyze and Optimize**: After the upgrade, run the `analyze_new_cluster.sh` script generated by `pg_upgrade` to update optimizer statistics. This step is crucial for performance.

5. **Finalize**: If everything works correctly, you can start the new cluster and remove the old cluster to free up space.

Learn more from the following resources:

- [@official@pg_upgrade](https://www.postgresql.org/docs/current/pgupgrade.html)
- [@video@Upgrade PostgreSQL with pg_upgrade](https://www.youtube.com/watch?v=DXHEk4fohcI)
- [@article@Examining Postgres Upgrades with pg_upgrade](https://www.crunchydata.com/blog/examining-postgres-upgrades-with-pg_upgrade)

## Using Systemd

# Using systemd

Using systemd to manage PostgreSQL involves utilizing the system and service manager to control the PostgreSQL service. This allows you to start, stop, and manage PostgreSQL automatically with the boot process.

Learn more from the following resources:

- [@article@What is systemd?](https://www.digitalocean.com/community/tutorials/what-is-systemd)
- [@article@Systemd postgresql start script](https://unix.stackexchange.com/questions/220362/systemd-postgresql-start-script)
- [@youtube@systemd on Linux](https://www.youtube.com/watch?v=N1vgvhiyq0E)

## Vacuum Processing

# Vacuum Processing

Vacuum processing is an essential aspect of maintaining the performance and stability of a PostgreSQL database. PostgreSQL uses a storage technique called Multi-Version Concurrency Control (MVCC), which allows multiple transactions to access different versions of a database object simultaneously. This results in the creation of multiple "dead" rows whenever a row is updated or deleted. Vacuum processing helps in cleaning up these dead rows and reclaiming storage space, preventing the database from becoming bloated and inefficient.

Learn more from the following resources:

- [@article@PostgreSQL VACUUM Guide and Best Practices](https://www.enterprisedb.com/blog/postgresql-vacuum-and-analyze-best-practice-tips)
- [@article@How to run VACUUM ANALYZE explicitly?](https://medium.com/@dmitry.romanoff/postgresql-how-to-run-vacuum-analyze-explicitly-5879ec39da47)

## Vacuums

# Vacuuming in PostgreSQL

Vacuuming is an essential component in PostgreSQL maintenance tasks. By reclaiming storage, optimizing performance, and keeping the database lean, vacuuming helps maintain the health of your PostgreSQL system. During the normal operation of PostgreSQL, database tuples (rows) are updated, deleted and added. This can lead to fragmentation, wasted space, and decreased efficiency. Vacuuming is used to:

- Reclaim storage space used by dead rows.
- Update statistics for the query planner.
- Make unused space available for return to the operating system.
- Maintain the visibility map in indexed relations.

Learn more from the following resources:

- [@official@VACUUM](https://www.postgresql.org/docs/current/sql-vacuum.html)
- [@official@Routine Vacuuming](https://www.postgresql.org/docs/current/routine-vacuuming.html)
- [@article@PostgreSQL Vacuuming Command to Optimize Database Performance](https://www.percona.com/blog/postgresql-vacuuming-to-optimize-database-performance-and-reclaim-space/)

## Wal G

# WAL-G - An Advanced Backup Recovery Tool for PostgreSQL

WAL-G is an open-source archival and restoration tool for PostgreSQL and MySQL/MariaDB, designed for managing Write-Ahead Logs (WAL) and performing continuous archiving. It extends the capabilities of the traditional `pg_basebackup` by supporting features like delta backups, compression, and encryption. WAL-G is optimized for cloud storage, integrating seamlessly with services like Amazon S3, Google Cloud Storage, and Azure Blob Storage. It ensures efficient backup storage by deduplicating data and providing incremental backup capabilities. Additionally, WAL-G supports point-in-time recovery, allowing databases to be restored to any specific time, enhancing disaster recovery processes.

Learn more from the following resources:

- [@opensource@wal-g/wal-g](https://github.com/wal-g/wal-g)
- [@article@Continuous PostgreSQL Backups using WAL-G](https://supabase.com/blog/continuous-postgresql-backup-walg)

## What Are Relational Databases

# What are Relational Databases?

Relational databases are a type of database management system (DBMS) that stores and organizes data in a structured format called tables. These tables are made up of rows, also known as records or tuples, and columns, which are also called attributes or fields. The term "relational" comes from the fact that these tables can be related to one another through keys and relationships.

Learn more from the following resources:

- [@article@Relational Databases](https://www.ibm.com/cloud/learn/relational-databases)
- [@article@Intro To Relational Databases](https://www.udacity.com/course/intro-to-relational-databases--ud197)
- [@article@Relational Databases: Concept and History](https://www.ibm.com/topics/relational-databases)
- [@course@Databases and SQL](https://www.edx.org/course/databases-5-sql)
- [@feed@Explore top posts about Relational Databases](https://app.daily.dev/tags/relational-databases?ref=roadmapsh)

## Write Ahead Log

# Write Ahead Log (WAL)

The Write Ahead Log, also known as the WAL, is a crucial part of PostgreSQL's data consistency strategy. The WAL records all changes made to the database in a sequential log before they are written to the actual data files. In case of a crash, PostgreSQL can use the WAL to bring the database back to a consistent state without losing any crucial data. This provides durability and crash recovery capabilities for your database.

Learn more from the following resources:

- [@official@Write Ahead Logging](https://www.postgresql.org/docs/current/wal-intro.html)
- [@article@Working With Postgres WAL Made Easy 101](https://hevodata.com/learn/working-with-postgres-wal/)
- [@video@Write Ahead Logging](https://www.youtube.com/watch?v=yV_Zp0Mi3xs)

## Write Ahead Log

# Write Ahead Log (WAL)

The Write Ahead Log, also known as the WAL, is a crucial part of PostgreSQL's data consistency strategy. The WAL records all changes made to the database in a sequential log before they are written to the actual data files. In case of a crash, PostgreSQL can use the WAL to bring the database back to a consistent state without losing any crucial data. This provides durability and crash recovery capabilities for your database.

Learn more from the following resources:

- [@official@Write Ahead Logging](https://www.postgresql.org/docs/current/wal-intro.html)
- [@article@Working With Postgres WAL Made Easy 101](https://hevodata.com/learn/working-with-postgres-wal/)
- [@video@Write Ahead Logging](https://www.youtube.com/watch?v=yV_Zp0Mi3xs)

## Writing Patches

# Writing Patches

If you are an experienced developer or willing to learn, you can contribute to PostgreSQL by writing patches. Patches are important to fix bugs, optimize performance, and implement new features. Here are some guidelines on how to write patches for PostgreSQL:

### Step 1: Find an Issue or Feature

Before writing a patch, you should identify an issue in PostgreSQL that needs fixing or a feature that requires implementation. You can find existing issues or propose new ones in the [PostgreSQL Bug Tracker](https://www.postgresql.org/support/submitbug/) and [PostgreSQL mailing lists](https://www.postgresql.org/list/).

### Step 2: Familiarize Yourself with the Codebase

To write a patch, you must have a good understanding of the PostgreSQL source code. The code is available on the [official website](https://www.postgresql.org/developer/sourcecode/) and is organized into different modules. Familiarize yourself with the coding conventions, coding style, and the appropriate module where your patch will be applied.

### Step 3: Set up the Development Environment

To create a patch, you need a development environment with the required tools, such as Git, GCC, and Bison. Follow the instructions in the [PostgreSQL Developer Setup Guide](https://wiki.postgresql.org/wiki/Developer_Setup) to set up your environment.

### Step 4: Write the Patch

Ensure that your patch adheres to the [PostgreSQL Coding Conventions](https://www.postgresql.org/docs/current/source-format.html). This includes following proper indentation, formatting, and organizing your code. Write clear and concise comments to help others understand the purpose of your patch.

### Step 5: Test the Patch

Before submitting your patch, thoroughly test it to ensure it works correctly and does not introduce new issues. Run the patch through the PostgreSQL regression test suite, as well as any additional tests specific to your patch.

### Step 6: Create a Commit and Generate a Patch

After completing your patch and testing it, create a Git commit with a clear and concise commit message. Use `git-format-patch` to generate a patch file that can be submitted to the PostgreSQL project.

### Step 7: Submit the Patch

Once your patch is ready, submit it through the appropriate [PostgreSQL mailing list](https://www.postgresql.org/list/) for review. Be prepared to receive feedback, make revisions, and resubmit your patch if necessary. Remember, contributing to an open-source project like PostgreSQL is a collaborative process!

By following these steps, you will be well on your way to contributing to the PostgreSQL project by writing patches. Happy coding!

## Zabbix

# Zabbix: An Introduction

Zabbix is an open-source monitoring software for networks, servers, virtual machines, and cloud services. It provides real-time monitoring, alerting, and visualization of metrics collected from various IT infrastructure components. Zabbix supports multiple data collection methods, including SNMP, IPMI, JMX, and custom scripts, making it versatile for different environments. It features a web-based interface for configuration and monitoring, allowing users to set thresholds, generate alerts, and create detailed performance reports and dashboards. Zabbix also supports distributed monitoring, auto-discovery, and scaling capabilities, making it suitable for both small and large-scale deployments. It is widely used for its robustness, flexibility, and comprehensive monitoring capabilities.

Learn more from the following resources:

- [@official@Zabbix](https://www.zabbix.com/)
- [@opensource@zabbix/zabbix](https://github.com/zabbix/zabbix)
- [@article@Using Zabbix to Monitor your Home Network](https://jswheeler.medium.com/using-zabbix-to-monitor-your-home-network-71ed2b1181ae)
