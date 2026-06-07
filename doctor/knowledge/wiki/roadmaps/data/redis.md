# Redis Roadmap

## Active Active Geo Distribution

# Active-Active geo Distribution

An Active-Active architecture is a data resiliency architecture that distributes the database information over multiple data centers via independent and geographically distributed clusters and nodes. It is a network of separate processing nodes, each having access to a common replicated database such that all nodes can participate in a common application ensuring local low latency with each region being able to run in isolation.

Learn more from the following resources:

- [@official@Active-Active geo-distribution](https://redis.io/active-active/)
- [@video@What is active active geo-distribution](https://youtu.be/x5iHPPZIlQg?si=ZZCwU-tDCIVDboXc)

## Aof Rewrite  Compaction

# AOF rewrite & compaction

Persistence refers to the writing of data to durable storage, such as a solid-state disk (SSD). Redis provides a range of persistence options of which AOF (Append Only File) is one of the options. AOF persistence logs every write operation received by the server. These operations can then be replayed again at server startup, reconstructing the original dataset.The rewrite will create a small optimized version of the current Append Only File. 

Learn more from the following resources:

- [@official@Persistence in Redis](https://redis.io/docs/latest/operate/oss_and_stack/management/persistence/)
- [@video@Enabling Redis persistence](https://youtu.be/qBKnUeR0p10?si=TPvcFtpFMcTZB-Be)

## Append

# APPEND

Redis APPEND command is used to add some value in a key. If the key already exists and is a string, this command appends the value at the end of the string. If key does not exist it is created and set as an empty string,

Learn more from the following resources:

- [@official@APPEND](https://redis.io/docs/latest/commands/append/)
- [@article@Redis - String Append Command](https://www.tutorialspoint.com/redis/strings_append.htm)

## Atomicity In Redis

# Atomicity in Redis

Atomicity in Redis refers to the property that ensures a set of operations is executed as a single, indivisible unit. This means that either all the operations are executed successfully or none of them are. Atomicity is crucial in Redis to maintain consistency, especially when multiple operations need to be performed together.

Learn more from the following resources:

- [@official@Atomicity with Lua](https://redis.io/learn/develop/java/spring/rate-limiting/fixed-window/reactive-lua)
- [@article@Atomicity in Redis operations](https://lucaspin.medium.com/atomicity-in-redis-operations-a1d7bc9f4a90)

## Authentication

# Authentication

Authentication in Redis is a security feature used to restrict access to the server by requiring clients to authenticate themselves with a password before performing any commands. This helps prevent unauthorized users from connecting to your Redis instance and performing operations.

Learn more from the following resources:

- [@official@AUTH](https://redis.io/docs/latest/commands/auth/)

## Backup And Recovery

# Backup and Recovery

Backing up and recovering Redis data is crucial for ensuring data persistence and reliability. Redis, by default, stores its data in memory for fast access, but it provides mechanisms to persist data to disk to allow for recovery in case of failure or system restarts. The primary methods for backup and recovery in Redis are RDB snapshots and AOF (Append-Only File). These methods can be used individually or in combination, depending on the specific use case.

Learn more from the following resources:

- [@official@Backup and Recovery](https://redis.io/redis-enterprise/technology/backup-disaster-recovery/)
- [@video@Backup & Restore Redis Cluster with Stash](https://youtu.be/Py_Ivv-2dcQ?si=z8gAAmhlpUBce4jY)

## Basic Commands  Set Get

# Basic Commands / SET, GET

In Redis, the SET and GET commands are fundamental operations used to store and retrieve key-value pairs. Redis is an in-memory key-value store, and these commands form the basis for working with data in Redis.

Learn more from the following resources:

- [@official@SET Docs](https://redis.io/docs/latest/commands/set/)
- [@official@GET Docs](https://redis.io/docs/latest/commands/get/)
- [@official@Redis Cheat Sheet](https://redis.io/learn/howtos/quick-start/cheat-sheet)

## Batch Operations

# Batch Operations

Batch operations in Redis allow you to execute multiple commands efficiently in a single network round-trip. While Redis does not have true batching like some databases (where a set of operations are sent together and processed atomically), it provides ways to send multiple commands together to reduce the overhead of individual network requests. These include Pipelining, Transactions (MULTI/EXEC), and Lua Scripting.

Learn more from the following resources:

- [@article@Batch Operations in Redis](https://www.compilenrun.com/docs/middleware/redis/redis-operations/redis-batch-operations/)
- [@article@Using Pipelining to Batch Issue Commands](https://www.alibabacloud.com/help/en/redis/use-cases/use-pipelining-to-batch-issue-commands#:~:text=You%20can%20use%20the%20Redis,network%20latency%20and%20improving%20performance.)

## Bitcount

# BITCOUNT

The BITCOUNT command in Redis is used to count the number of bits set to 1 (i.e., the number of binary 1s) in the value stored at a specific key. Since Redis allows string values to be stored as binary data, the BITCOUNT command becomes useful for operations involving bits, like efficiently tracking and counting bits in binary-encoded data.

Learn more from the following resources:

- [@official@BITCOUNT](https://redis.io/docs/latest/commands/bitcount/)
- [@article@BITCOUNT](https://upstash.com/docs/redis/sdks/ts/commands/bitmap/bitcount)

## Bitmaps

# Bitmaps

In Redis, Bitmaps are a data structure that allows you to manipulate individual bits within a string value. While Redis doesn't have a native "bitmap" data type, it uses strings to represent bitmaps. The power of bitmaps comes from their ability to perform operations on binary data at the bit level, making them extremely memory-efficient for certain types of applications, like tracking the presence/absence of elements (such as daily active users, features, etc.).

Learn more from the following resources:

- [@official@Bitmap](https://redis.io/docs/latest/develop/data-types/bitmaps/)
- [@video@Redis Bitmap Explained](https://youtu.be/oj8LdJQjhJo?si=jem54LfPbZtrpnEP)

## Bitop

# BITOP

The `BITOP` command in Redis performs bitwise operations (AND, OR, XOR, and NOT) across one or more string keys, treating the strings as binary data. The result is stored in a destination key. This command is useful for manipulating and analyzing binary data directly in Redis, such as when aggregating flags or working with bitmap data structures.

Learn more from the following resources:

- [@official@BITOP](https://redis.io/docs/latest/commands/bitop/)
- [@article@BITOP Explained](https://www.dragonflydb.io/docs/command-reference/strings/bitop)

## Bitpos

# BITPOS

The `BITPOS` command in Redis is used to find the position of the first bit set to 1 or 0 in a string key. You can specify a starting and ending byte range for the search. It’s commonly used in scenarios where you need to quickly locate specific bits within a bitmap, such as finding the first occurrence of a flag or status in large datasets.

Learn more from the following resources:

- [@official@BITPOS](https://redis.io/docs/latest/commands/bitpos/)
- [@article@BITPOS Documentation](https://upstash.com/docs/redis/sdks/py/commands/bitmap/bitpos)

## Cache

# Cache

Redis cache is an in-memory key-value store used to cache frequently accessed data to improve application performance. By storing data in memory rather than on disk, Redis significantly reduces data access latency, making it ideal for use cases such as session management, caching database query results, and storing temporary data. Its ability to handle high throughput and support data persistence options allows it to be used as both a short-term cache and a durable data store.

Learn more from the following resources:

- [@official@Redis Caching](https://redis.io/solutions/caching/)
- [@official@How to use Redis for Query Caching](https://redis.io/learn/howtos/solutions/microservices/caching)
- [@article@Understanding Redis Caching](https://medium.com/@devlexus/understanding-redis-caching-how-it-works-and-why-its-efficient-99afdbf1b8e0)
- [@video@How to use Redis Caching for incredible performance](https://www.youtube.com/watch?v=-5RTyEim384)

## Caching

# Caching

Redis cache is an in-memory key-value store used to cache frequently accessed data to improve application performance. By storing data in memory rather than on disk, Redis significantly reduces data access latency, making it ideal for use cases such as session management, caching database query results, and storing temporary data. Its ability to handle high throughput and support data persistence options allows it to be used as both a short-term cache and a durable data store.

Learn more from the following resources:

- [@official@Redis Caching](https://redis.io/solutions/caching/)
- [@official@How to use Redis for Query Caching](https://redis.io/learn/howtos/solutions/microservices/caching)
- [@article@Understanding Redis Caching](https://medium.com/@devlexus/understanding-redis-caching-how-it-works-and-why-its-efficient-99afdbf1b8e0)
- [@video@How to use Redis Caching for incredible performance](https://www.youtube.com/watch?v=-5RTyEim384)

## Clustering

# Clustering

Redis Cluster is a distributed implementation of Redis that provides automatic data partitioning across multiple nodes and ensures high availability through data replication. It uses a sharding mechanism to split data across nodes using a hash slot system, where each key is mapped to one of 16,384 slots distributed among the cluster's nodes. Redis Cluster offers fault tolerance by replicating data across master and replica nodes, enabling the cluster to continue operating even if some nodes fail. This setup is ideal for large-scale applications requiring scalability and resilience.

Learn more from the following resources:

- [@official@Scale with Redis Cluster](https://redis.io/docs/latest/operate/oss_and_stack/management/scaling/)
- [@video@How to Create a Cluster in Redis](https://www.youtube.com/watch?v=N8BkmdZzxDg)

## Configuring Save Interval

# Configuring Save Interval

Configuring the save interval in Redis controls how often data is saved from memory to disk (RDB snapshots). This is done using the `save` directive in the `redis.conf` file. You can specify multiple save intervals with different thresholds, for example: `save 900 1` saves the dataset if at least one key is changed within 900 seconds. Redis allows configuring multiple save intervals, offering flexibility between performance and data durability based on your use case.

Learn more from the following resources:

- [@official@Redis Persistence](https://redis.io/docs/latest/operate/oss_and_stack/management/persistence/)
- [@video@Understanding Redis Persistence](https://www.youtube.com/watch?v=1pfvz24BAUs)

## Connecting Using Redis Cli

# Connecting using Redis CLI

The Redis CLI (`redis-cli`) is a command-line interface used to interact with a Redis server. It allows users to run Redis commands, monitor the server, manage data, and perform administrative tasks. Common operations include setting and getting keys, managing key expiration, and checking server status. The CLI supports running commands in both interactive mode and non-interactive mode for scripting and automation. It’s a powerful tool for developers and administrators to troubleshoot and manage Redis instances directly.

Learn more from the following resources:

- [@official@Redis CLI Documentation](https://redis.io/docs/latest/develop/connect/cli/)
- [@video@The Command Line Tool: redis-cli](https://www.youtube.com/watch?v=VenGyryG4OE)

## Data Persistence Options

# Data Persistence Options

Redis offers two main data persistence options: **RDB (Redis Database)** snapshots and **AOF (Append-Only File)**. RDB creates point-in-time snapshots of the dataset at specified intervals, making it suitable for infrequent backups but with potential data loss between snapshots. AOF logs every write operation and replays them on restart, providing more durable persistence with finer control over data recovery. You can also configure Redis to use both methods for a balance between fast recovery and minimal data loss. Additionally, Redis supports running in memory-only mode without persistence.

## Decr

# DECR

The `DECR` command in Redis decreases the integer value of a key by 1. If the key does not exist, it is initialized to 0 before performing the decrement. If the key contains a value that is not an integer, Redis returns an error. This command is useful in counters and for tracking state changes in a simple, atomic way.

Learn more from the following resources:

- [@official@DECR Documentation](https://redis.io/docs/latest/commands/decr/)
- [@article@Redis String DECR](https://www.w3resource.com/redis/redis-decr-key.php)

## Del

# DEL

The `DEL` command in Redis is used to delete one or more keys from the database. If the specified key(s) exist, they are removed, and the command returns the number of keys that were deleted. If a key does not exist, it is simply ignored, and no error is returned. This command is useful for managing memory by removing unnecessary or obsolete data and is an atomic operation, ensuring that keys are deleted without interference from other operations.

Learn more from the following resources:

- [@official@DEL](https://redis.io/docs/latest/commands/del/)
- [@article@Redis DEL Command](https://www.tutorialspoint.com/redis/keys_del.htm)

## Disaster Recovery

# Disaster Recovery

Disaster recovery in Redis involves strategies and practices to ensure data availability and integrity in the event of failures, such as server crashes, data corruption, or network issues. Key approaches include leveraging Redis's built-in replication, where data is copied from master to replica nodes for redundancy. Snapshots (RDB) and append-only file (AOF) persistence methods can be configured for data recovery, allowing the restoration of data to a recent state. Additionally, implementing a Redis Cluster can provide automated failover capabilities, distributing data across multiple nodes to minimize downtime and ensure business continuity. Regular backups and monitoring are also essential components of a robust disaster recovery plan.

Learn more from the following resources:

- [@official@Backup Disaster Recovery](https://redis.io/redis-enterprise/technology/backup-disaster-recovery/)
- [@article@Disaster Recovery for Redis in the Cloud](https://www.alibabacloud.com/tech-news/a/redis/gtu8u2afbc-disaster-recovery-for-redis-in-the-cloud-strategies-and-best-practices)

## Eval

# EVAL

The `EVAL` command in Redis allows the execution of Lua scripts directly on the server, enabling complex operations that can be atomically executed. This command takes a Lua script as an argument, along with a list of keys and arguments for the script. By executing scripts server-side, `EVAL` reduces the number of round trips between the client and server, enhances performance, and allows for operations that require multiple commands to be executed in a single atomic operation. It is particularly useful for implementing advanced data manipulations, custom logic, or conditional operations within Redis.

Learn more from the following resources:

- [@official@EVAL](https://redis.io/docs/latest/commands/eval/)
- [@article@Redis EVAL Command](https://www.tutorialspoint.com/redis/scripting_eval.htm)

## Evalsha

# EVALSHA

The `EVALSHA` command in Redis is used to execute a Lua script that has already been loaded into the server with the `SCRIPT LOAD` command. Instead of sending the entire script each time, you provide the SHA1 hash of the script, which allows for more efficient execution and reduced network overhead. Like `EVAL`, `EVALSHA` can accept keys and arguments, enabling complex, atomic operations to be performed directly on the server. This approach is particularly beneficial in scenarios where the same script is executed multiple times, as it avoids the need to re-transmit the script’s source code.

Learn more from the following resources:

- [@official@EVALSHA](https://redis.io/docs/latest/commands/evalsha/)
- [@article@Redis EVALSHA Command](https://www.tutorialspoint.com/redis/scripting_evalsha.htm)

## Exec

# EXEC

The `EXEC` command in Redis is used to execute a transaction that has been initiated with the `MULTI` command. When a transaction is started with `MULTI`, subsequent commands are queued but not executed immediately. Calling `EXEC` will execute all the commands in the transaction atomically, ensuring that either all commands succeed or none are applied. If any command in the transaction fails, the entire transaction is aborted. This command is essential for maintaining data integrity when performing a series of operations that should be treated as a single unit of work.

Learn more from the following resources:

- [@official@EXEC](https://redis.io/docs/latest/commands/exec/)
- [@article@Redis Transactions: EXEC](https://www.w3resource.com/redis/redis-exec.php)

## Expiration

# Expiration

Redis key expiration allows you to set a time-to-live (TTL) for keys, automatically deleting them after a specified duration. This can be achieved using commands like `EXPIRE`, which sets the expiration time in seconds, or `PEXPIRE`, which uses milliseconds for finer granularity. You can also use `SET` with the EX argument to set a key with a value and expiration in a single command. Expired keys are removed during normal operations, such as when accessed or during periodic cleanup. This feature is useful for managing memory efficiently and for scenarios like session management or caching where temporary data storage is needed.

Learn more from the following resources:

- [@official@PEXPIRE](https://redis.io/docs/latest/commands/pexpire/)
- [@official@EXPIRE](https://redis.io/docs/latest/commands/expire/)

## Expire

# EXPIRE

The EXPIRE command is used to set a time-to-live (TTL) for a key in seconds, after which the key will be automatically deleted. If you need to specify the expiration time in milliseconds, you can use the PEXPIRE command. Both commands help manage memory by allowing you to automatically remove keys that are no longer needed, which is especially useful in caching and session management scenarios.

Learn more from the following resources:

- [@official@Expiring Keys](https://redis.io/ebook/part-2-core-concepts/chapter-3-commands-in-redis/3-7-other-commands/3-7-3-expiring-keys/)
- [@official@EXPIRE](https://redis.io/docs/latest/commands/expire/)

## Geoadd

# GEOADD

The `GEOADD` command in Redis is used to add geospatial data to a sorted set, where each entry consists of a member (a unique identifier) and its corresponding longitude and latitude coordinates. This command allows you to store location-based data efficiently, enabling geospatial queries such as finding members within a specified radius or calculating distances between points. The coordinates are stored in a format that allows for quick retrieval and analysis, making `GEOADD` a powerful tool for applications involving mapping, location tracking, and proximity searches.

Learn more from the following resources:

- [@official@GEOADD](https://redis.io/docs/latest/commands/geoadd/)

## Geosearch

# GEOSEARCH

The `GEOSEARCH` command in Redis is used to query geospatial data by finding members within a specified geographic area. It allows you to search for entries based on a central point (latitude and longitude) and a defined radius, or by bounding box coordinates. The command returns a sorted set of members that fall within the specified geographical range, making it ideal for applications that require proximity searches, such as locating nearby businesses or services. `GEOSEARCH` can also be combined with various options, such as sorting results by distance or limiting the number of results returned.

Learn more from the following resources:

- [@official@GEOADD](https://redis.io/docs/latest/commands/geoadd/)
- [@article@Getting Started with Geospatial Search in Redis](https://redis.io/learn/howtos/solutions/geo/getting-started)

## Geospatial Indexes

# Geospatial Indexes

Geospatial indexes in Redis are used to efficiently store and query location-based data, enabling fast geospatial operations. Redis uses a sorted set data structure to maintain these indexes, where each member represents a geographic location identified by longitude and latitude coordinates. The coordinates are encoded into a single value, allowing Redis to perform operations like adding locations (`GEOADD`), searching for nearby locations (`GEOSEARCH`), and calculating distances (`GEODIST`). This indexing mechanism allows for rapid retrieval of geospatial data, making it suitable for applications such as mapping services, location tracking, and proximity-based searches.

Learn more from the following resources:

- [@official@Geospatial Indexing](https://redis.io/docs/latest/develop/interact/search-and-query/indexing/geoindex/)
- [@article@Geospatial Indexes in Redis](https://codesignal.com/learn/courses/redis-data-structures-beyond-basics/lessons/introduction-to-geospatial-indexes-in-redis-using-java)

## Get

# GET

The `GET` command in Redis is used to retrieve the value associated with a specified key. If the key exists, it returns the value as a string; if the key does not exist, it returns a nil response. This command is fundamental for accessing stored data in Redis and is often used in conjunction with other commands to manipulate and manage data within the database. The `GET` command is atomic, meaning it provides a consistent view of the data at the time the command is executed.

Learn more from the following resources:

- [@official@GET](https://redis.io/docs/latest/commands/get/)
- [@article@How to get all keys in Redis](https://www.atlassian.com/data/admin/how-to-get-all-keys-in-redis)

## Getbit

# GETBIT

The `GETBIT` command in Redis retrieves the value of a specific bit at a given offset in a string key. It returns either 0 or 1, depending on the state of the bit at that position. If the key does not exist, the command returns 0, as it treats non-existing keys as empty strings. This command is particularly useful for working with bitmap data structures, allowing you to check the status of individual bits in a more efficient manner compared to retrieving the entire string.

Learn more from the following resources:

- [@official@GETBIT](https://redis.io/docs/latest/commands/getbit/)

## Hashes

# Hashes

Hashes in Redis are a data type that allows you to store a collection of key-value pairs under a single key, similar to a dictionary or a map. Each hash can hold multiple fields, and each field has its own value, making hashes ideal for representing objects or entities with various attributes. You can perform operations like adding fields (`HSET`), retrieving field values (`HGET`), deleting fields (`HDEL`), and iterating over fields (`HSCAN`). Hashes are memory-efficient and provide a way to group related data together, making them suitable for use cases like user profiles, configuration settings, or any structured data storage.

Learn more from the following resources:

- [@official@Redis Hashes](https://redis.io/docs/latest/develop/data-types/hashes/)

## Hdel

# HDEL

`HDEL` is a Redis command used to delete one or more specified fields from a hash. If the fields exist in the hash, they are removed, and the command returns the number of fields that were deleted. If a specified field does not exist, it is ignored. `HDEL` is useful for efficiently managing memory and cleaning up data within a Redis hash without removing the entire hash structure.

Learn more from the following resources:

- [@official@HDEL](https://redis.io/docs/latest/commands/hdel/)

## Hexists

# HEXISTS

`HEXISTS` is a Redis command used to check if a specified field exists within a hash. It returns `1` if the field is present and `0` if it is not. This command is useful for verifying the presence of specific fields in a hash before performing operations like updates or deletions. It helps ensure data consistency and avoid unnecessary operations in Redis.

Learn more from the following resources:

- [@official@HEXISTS](https://redis.io/docs/latest/commands/hexists/)

## Hget

# HGET

`HGET` is a Redis command used to retrieve the value of a specified field within a hash. If the field exists, it returns the value; if not, it returns `nil`. This command is efficient for accessing specific fields within a hash without retrieving the entire hash structure, making it ideal for scenarios where only selective data needs to be read from a Redis hash.

Learn more from the following resources:

- [@official@HGET](https://redis.io/docs/latest/commands/hget/)

## Hgetall

# HGETALL

`HGETALL` is a Redis command that retrieves all the fields and their values from a specified hash. It returns the data as an array of field-value pairs, making it useful for obtaining a complete view of the hash's contents. However, it can be memory-intensive for large hashes, so it’s recommended to use it cautiously when dealing with high data volumes.

Learn more from the following resources:

- [@official@HGETALL](https://redis.io/docs/latest/commands/hgetall/)

## High Performance And Scalability

# High Performance and Scalability

High performance and scalability in Redis are achieved through its in-memory data storage model, which allows for extremely fast read and write operations with minimal latency. Redis supports data partitioning, replication, and clustering, enabling it to scale horizontally across multiple nodes and handle large volumes of requests simultaneously. With asynchronous replication and automatic failover, Redis ensures high availability, making it well-suited for real-time applications that require low latency and high throughput, such as caching, messaging, and session management.

Learn more from the following resources:

- [@article@Optimizing Redis for High Performance](https://loadforge.com/guides/optimizing-redis-for-high-performance-essential-configuration-tweaks)
- [@article@High-Performance and Scalable Architecture with Redis](https://medium.com/@emreemenekse/high-performance-and-scalable-architecture-with-redis-and-net-core-abde36074d26)

## How Aof Works

# How AOF Works?

The Append-Only File (AOF) in Redis is a persistence mechanism that logs every write operation to a file in sequential order, ensuring data durability. Each command is appended to the end of the AOF file, which Redis can replay to rebuild the dataset in case of a restart. The AOF file can grow over time, so Redis provides an automatic background process called *AOF rewrite* to create a compact version by eliminating redundant commands. AOF is generally safer than the default RDB snapshotting, as it provides finer granularity for data recovery and minimizes the potential for data loss.

Learn more from the following resources:

- [@article@About AOF Persistence - Google](https://cloud.google.com/memorystore/docs/cluster/about-aof-persistence)

## How Rdb Works

# How RDB Works?

The RDB (Redis Database Backup) mechanism in Redis creates snapshots of the dataset at specified intervals and saves them to disk as a compact binary file. This process is triggered manually, via the `SAVE` or `BGSAVE` commands, or automatically based on predefined conditions. During a snapshot, Redis forks a child process to write the in-memory data to the RDB file, ensuring that the main process is not blocked. While RDB offers a lightweight and fast backup option, it may lead to potential data loss if Redis crashes between snapshots, making it ideal for periodic backups rather than real-time persistence.

Learn more from the following resources:

- [@official@Backup Data](https://redis.io/docs/latest/operate/rc/databases/back-up-data/)
- [@article@About RDB Snapshots](https://cloud.google.com/memorystore/docs/redis/about-rdb-snapshots)

## Hset

# HSET

`HSET` is a Redis command used to set the value of a specified field within a hash. If the field already exists, it updates the value; if not, it adds the field to the hash. This command is useful for creating and managing key-value pairs within a hash structure without modifying other fields. It returns `1` if a new field is created and `0` if an existing field is updated, making it efficient for atomic updates in a Redis hash.

Learn more from the following resources:

- [@official@HSET](https://redis.io/docs/latest/commands/hset/)

## Hybrid Persistence

# Hybrid Persistence

Hybrid persistence in Redis combines both RDB (Redis Database Backup) and AOF (Append-Only File) mechanisms to leverage the benefits of each. RDB provides efficient snapshot-based backups at defined intervals, while AOF logs every write operation to ensure minimal data loss. Using both, Redis achieves a balance between fast recovery times (thanks to compact RDB snapshots) and high durability (from the detailed logging of AOF). This approach minimizes the drawbacks of using either persistence type alone and offers a robust solution for scenarios requiring both performance and data safety.

Learn more from the following resources:

- [@official@Redis Persistence](https://redis.io/docs/latest/operate/oss_and_stack/management/persistence/)

## Hyperloglog

# HyperLogLog

HyperLogLog is a probabilistic data structure in Redis used for efficiently estimating the cardinality (i.e., the number of unique elements) of large datasets with minimal memory usage. Instead of storing the actual elements, it maintains a compressed representation, allowing it to estimate cardinality with a typical error rate of only 0.81%. Commands like `PFADD`, `PFCOUNT`, and `PFMERGE` are used to add elements, get the count, and merge HyperLogLogs, respectively. This structure is ideal for applications like unique visitor tracking or counting events where exact counts are not required but low memory consumption is critical.

Learn more from the following resources:

- [@official@HyperLogLog Documentation](https://redis.io/docs/latest/develop/data-types/probabilistic/hyperloglogs/)
- [@video@Redis HyperLogLog Explained](https://www.youtube.com/watch?v=MunL8nnwscQ)

## In Memory Data Structure Store

# In-memory Data Structure Store

An in-memory database is a purpose-built database that relies primarily on internal memory for data storage. It enables minimal response times by eliminating the need to access standard disk drives (SSDs). In-memory databases are ideal for applications that require microsecond response times or have large spikes in traffic, such as gaming leaderboards, session stores, and real-time data analytics. The terms main memory database (MMDB), in-memory database system (IMDS), and real-time database system (RTDB) also refer to in-memory databases.

Learn more from the following resources:

- [@official@Get Started with In-Memory Data Store](https://redis.io/docs/latest/develop/get-started/data-store/)
- [@article@Amazon MemoryDB](https://aws.amazon.com/memorydb/)

## Incr

# INCR

`INCR` command used to increment the value of a string key by 1. If the key does not exist, it initializes the key with a value of 0 before performing the increment operation, resulting in a value of 1. If the key contains a non-integer value, the command will return an error. `INCR` is atomic, meaning it is safe to use in concurrent environments without race conditions, making it ideal for use cases like counters or tracking metrics.

Learn more from the following resources:

- [@official@INCR](https://redis.io/docs/latest/commands/incr/)

## Info

# INFO

`INFO` command that provides detailed information and statistics about the server, including memory usage, CPU load, connected clients, replication status, and more. It can be called without arguments to get a full overview or with specific sections (e.g., `INFO memory`) to retrieve targeted data. This command is useful for monitoring and debugging Redis instances, helping administrators understand the server's current state and performance metrics.

Learn more from the following resources:

- [@official@INFO](https://redis.io/docs/latest/commands/info/)

## Key Value Database

# Key-value Database

Key-value Database is a non-relational (NoSQL) database that stores data as a collection of key-value pairs. In this model, each piece of data is associated with a unique identifier (key) that is used to retrieve the corresponding value. This simple structure allows for high performance and scalability, making key-value databases ideal for certain use cases. 

Visit the following resources to learn more:

- [@official@What is a Key-Value Database?](https://redis.io/nosql/key-value-databases/)
- [@video@Key Value Store - System Design Interview Basics](https://www.youtube.com/watch?v=ozJHmm05EXM)

## Leaderboards And Counters

# Leaderboards and Counters

Leaderboards and counters are common use cases for Redis, leveraging its sorted sets and atomic increment operations. For leaderboards, the `ZADD` command is used to add members with their scores to a sorted set, and `ZRANGE` or `ZREVRANGE` retrieves the top (or bottom) ranked members efficiently. This makes Redis ideal for ranking systems in gaming or tracking top-performing entities. Counters are managed using commands like `INCR` and `DECR`, which atomically increase or decrease integer values. These operations are lightweight and performant, making Redis a go-to solution for tracking metrics, analytics, or rate limiting.

Learn more from the following resources:

- [@official@ZADD](https://redis.io/docs/latest/commands/zadd/)
- [@official@ZRANGE](https://redis.io/docs/latest/commands/zrange/)

## Lindex

# LINDEX

`LINDEX` is a Redis command used to retrieve an element from a list by its index. The index can be positive (starting from 0 for the first element) or negative (e.g., -1 for the last element). If the index is out of range, the command returns `nil`. This command is useful for accessing specific elements in a list without needing to fetch the entire list, making it efficient for operations where only certain elements are needed.

Learn more from the following resources:

- [@official@LINDEX](https://redis.io/docs/latest/commands/lindex/)

## Lists

# Lists

Lists in Redis are ordered collections of string elements, allowing operations such as pushing, popping, and accessing elements by index. Lists support various commands, like `LPUSH` and `RPUSH` to add elements to the beginning or end, `LPOP` and `RPOP` to remove elements, and `LRANGE` to retrieve a range of elements. They are ideal for use cases like message queues, task management, or implementing stacks and queues, where maintaining order is crucial. Lists can grow dynamically and provide high performance for operations at the ends, making them highly flexible for managing ordered data sequences.

Learn more from the following resources:

- [@official@Redis Lists](https://redis.io/docs/latest/develop/data-types/lists/)

## Llen

# LLEN

`LLEN` is a Redis command used to return the length of a list stored at a specified key. If the list does not exist, it returns `0`. This command is efficient for quickly checking the number of elements in a list without retrieving its contents, making it useful for monitoring queue sizes, tracking list growth, or validating data presence in real-time applications.

Learn more from the following resources:

- [@official@LLEN](https://redis.io/docs/latest/commands/llen/)

## Lmove

# LMOVE

`LMOVE` is a Redis command used to atomically move an element from one list to another. It pops an element from the source list (either from the left or right end) and pushes it to the destination list (either to the left or right end), based on the specified parameters (`LEFT` or `RIGHT`). This command is useful for implementing queue-like patterns or managing work distribution between different lists without race conditions, as it ensures that the element is safely transferred in a single atomic operation.

Learn more from the following resources:

- [@official@LMOVE](https://redis.io/docs/latest/commands/lmove/)

## Lpop

# LPOP

`LPOP` is a Redis command that removes and returns the first element from the left side of a list. If the list is empty or does not exist, it returns `nil`. This command is commonly used in scenarios like implementing queues or consuming elements in FIFO (First-In-First-Out) order, making it ideal for task processing, message handling, and managing ordered data flows in real-time applications.

Learn more from the following resources:

- [@official@LPOP](https://redis.io/docs/latest/commands/lpop/)

## Lpush

# LPUSH

`LPUSH` is a Redis command that inserts one or more elements at the beginning (left side) of a list. If the list does not exist, it creates a new list before performing the insertion. This command returns the length of the list after the operation. `LPUSH` is useful for building stacks or adding items to queues where new elements need to be prioritized, enabling efficient manipulation of ordered data structures in Redis.

Learn more from the following resources:

- [@official@LPUSH](https://redis.io/docs/latest/commands/lpush/)

## Lrange

# LRANGE

`LRANGE` is a Redis command that retrieves a specified range of elements from a list, defined by a start and stop index. The indices can be positive (starting from 0) or negative (e.g., -1 for the last element). This command is commonly used to fetch subsets of a list without loading the entire list into memory, making it useful for paginating data, viewing portions of a queue, or analyzing a segment of ordered data in an efficient manner.

Learn more from the following resources:

- [@official@LRANGE](https://redis.io/docs/latest/commands/lrange/)

## Lua Scripting

# Lua Scripting

Lua scripting in Redis allows users to execute custom scripts atomically on the server side, enabling complex operations to be performed in a single step. Lua scripts are run using the `EVAL` or `EVALSHA` commands, and can manipulate multiple keys and values in a single execution. This reduces network overhead and ensures data consistency, as the script executes as a single transaction. Lua is commonly used for tasks like conditional updates, batch processing, and combining multiple commands into a single operation, enhancing Redis's flexibility and power for advanced use cases.

Learn more from the following resources:

- [@official@Lua Programming Language](https://www.lua.org/)
- [@video@Lua in 100 Seconds](https://www.youtube.com/watch?v=jUuqBZwwkQw)
- [@video@Full Lua Programming Crash Course](https://www.youtube.com/watch?v=1srFmjt1Ib0)

## Max Memory Policy

# Max Memory Policy

The Max Memory Policy in Redis determines how the server handles data when it reaches the configured maximum memory limit. Redis offers several eviction policies, such as `noeviction` (return an error on writes), `allkeys-lru` (evict the least recently used keys), `volatile-lru` (evict the least recently used keys with an expiration set), `allkeys-random` (evict random keys), and others. These policies allow Redis to optimize memory usage based on the use case, balancing between maintaining data availability and minimizing the risk of data loss when memory constraints are reached.

Learn more from the following resources:

- [@official@Database Memory Limits](https://redis.io/docs/latest/operate/rs/databases/memory-performance/memory-limit/)
- [@official@Eviction Policy](https://redis.io/docs/latest/operate/rs/databases/memory-performance/eviction-policy/)

## Memory Management

# Memory Management

Memory management in Redis involves efficiently handling data storage within its in-memory structure to maximize performance and prevent memory overflows. Redis uses various techniques such as memory-efficient data encoding (e.g., `ziplist` or `intset`), active and passive eviction strategies based on the configured max memory policy, and expiration of keys to automatically free up space. To persist data, Redis offers snapshotting (RDB) and logging (AOF) mechanisms. Additionally, commands like `MEMORY USAGE` and `MEMORY STATS` help monitor memory consumption, making it easier to tune and optimize the instance for specific use cases. Effective memory management ensures high availability, low latency, and predictable performance.

Learn more from the following resources:

- [@official@MEMORY USAGE Command](https://redis.io/docs/latest/commands/memory-usage/)
- [@official@MEMORY STATS Command](https://redis.io/docs/latest/commands/memory-stats/)
- [@article@Memory Management Best Practices](https://cloud.google.com/memorystore/docs/redis/memory-management-best-practices)

## Message Broker

# Message Broker

A message broker is a middleware system that enables communication between different services or applications by routing, storing, and delivering messages. Redis can serve as a lightweight message broker using its `PUBLISH` and `SUBSCRIBE` commands for a pub/sub messaging pattern, or through lists and sorted sets for more advanced messaging scenarios like task queues. Redis Streams provide additional features like message persistence, acknowledgment, and consumer groups, making it suitable for both real-time communication and more complex message processing pipelines. Its high throughput and low latency make Redis an efficient solution for building scalable messaging systems.

Learn more from the following resources:

- [@official@PUBLISH Command](https://redis.io/docs/latest/commands/publish/)
- [@official@SUBSCRIBE Command](https://redis.io/docs/latest/commands/subscribe/)
- [@article@Redis As a Message Broker](https://medium.com/shoutloudz/redis-as-a-message-broker-d1a1aeac23c3)

## Monitor

# MONITOR

`MONITOR` is a Redis command that provides a real-time feed of all commands executed on the server, displaying each command along with its arguments as they are processed. It is primarily used for debugging, monitoring, or analyzing the behavior of a Redis instance. Since `MONITOR` can impact performance by streaming every command in real-time, it should be used cautiously in production environments. It is a useful tool for understanding command patterns, tracking down issues, and gaining insights into how clients interact with the Redis server.

Learn more from the following resources:

- [@official@MONITOR](https://redis.io/docs/latest/commands/monitor/)
- [@official@SLOWLOG](https://redis.io/docs/latest/commands/slowlog/)

## Monitoring

# Monitoring

Monitoring in Redis involves tracking the health, performance, and resource usage of the server to ensure optimal operation and early detection of issues. Tools and commands like `INFO` (providing statistics on memory, CPU, and clients), `MONITOR` (real-time command tracking), and `SLOWLOG` (logging slow queries) offer insights into server activity. Additionally, external tools like Redis Sentinel, Prometheus, and Grafana are often integrated for more comprehensive monitoring, alerting, and visualization. Effective monitoring helps maintain stability, optimize performance, and troubleshoot potential bottlenecks, making it crucial for managing Redis deployments at scale.

Learn more from the following resources:

- [@official@Monitoring with Metrics and Alerts](https://redis.io/docs/latest/operate/rs/clusters/monitoring/)
- [@official@MONITOR](https://redis.io/docs/latest/commands/monitor/)

## More Commands

# More Commands - Strings

Redis strings include a variety of operations that go beyond basic SET and GET functionality. Examples include MSET and MGET for setting and getting multiple keys at once, GETSET to set a new value while returning the old one, and SETEX or PSETEX for setting a value with an expiration time. Other commands like INCRBY and DECRBY allow incrementing or decrementing by a specified amount, while BITCOUNT and BITOP provide bit-level manipulations.

Learn more from the following resources:

- [@official@All Redis String Commands](https://redis.io/docs/latest/commands/?group=string)

## More Commands

# More Commands - Streams

Streams include a variety of operations that enhance the core functionality provided by basic commands like XADD and XREAD. Examples include XDEL to remove specific entries from a stream, XTRIM to control the size of a stream by trimming old entries, and XGROUP for managing consumer groups, allowing multiple clients to read from the same stream in a coordinated manner. Commands like XPENDING and XCLAIM are useful for monitoring and handling pending messages, ensuring that no data is lost or left unprocessed.

Learn more from the following resources:

- [@official@All Redis Stream Commands](https://redis.io/docs/latest/commands/?group=stream)

## More Commands

# More Commands - Geospatial Indexes

Redis Geospatial indexes include operations like GEODIST to calculate the distance between two members of a geospatial set, GEOHASH to retrieve the Geohash representation of locations, and GEOPOS to get the longitude and latitude of specified members. Additionally, GEORADIUS and GEORADIUSBYMEMBER allow searching for members within a given radius based on coordinates or a reference member.

Learn more from the following resources:

- [@official@All Redis Geospatial Commands](https://redis.io/docs/latest/commands/?group=geo)

## More Commands

# More Commands - Hashes

Redis Hashes include operations like HMSET and HMGET to set or retrieve multiple fields and values at once, HINCRBY and HINCRBYFLOAT to increment the value of a field by a given integer or float, and HLEN to get the number of fields in a hash. Commands like HKEYS and HVALS are used to retrieve all field names or values, respectively, while HSCAN enables incremental iteration over large hashes. These commands extend the functionality of basic hash operations, making Redis Hashes ideal for storing and manipulating structured data, such as user profiles or configuration settings, with efficient access and updates.

Learn more from the following resources:

- [@official@All Redis Hash Commands](https://redis.io/docs/latest/commands/?group=hash)

## More Commands

# More Commands - Pub/Sub

Redis Pub/Sub include operations like PSUBSCRIBE and PUNSUBSCRIBE for subscribing and unsubscribing to channels using pattern matching, allowing for flexible topic-based subscriptions. Additionally, PUBSUB CHANNELS lists active channels, PUBSUB NUMSUB shows the number of subscribers per channel, and PUBSUB NUMPAT returns the count of active pattern subscriptions. These commands extend the basic publish and subscribe functionality, providing better insights and control over the messaging patterns, making Pub/Sub ideal for real-time event broadcasting, chat applications, and inter-service communication in distributed systems.

Learn more from the following resources:

- [@official@All Redis Pub/Sub Commands](https://redis.io/docs/latest/commands/?group=pubsub)

## More Commands

# More Commands - Sets

Redis Sets include advanced operations like SRANDMEMBER to retrieve random members from a set, SPOP to remove and return random elements, and SMOVE to atomically move elements between sets. Commands like SSCAN allow for incremental iteration over large sets, avoiding performance issues with massive data structures. For complex set operations, SINTERSTORE, SUNIONSTORE, and SDIFFSTORE enable storing the results of set intersections, unions, or differences into new sets. These commands extend the functionality of basic set operations, enabling efficient membership tests, set manipulations, and mathematical set calculations, making Redis Sets highly versatile for diverse data management needs.

Learn more from the following resources:

- [@official@All Redis Set Commands](https://redis.io/docs/latest/commands/?group=set)

## More Commands

# More Commands - Lists

Redis Lists include operations like LTRIM to trim the list to a specified range, RPOPLPUSH to remove an element from one list and append it to another, and BLPOP or BRPOP for blocking pop operations that wait until an element is available. Commands like LPOS allow finding the position of elements, and LSET is used to update a list element at a specified index. These additional commands provide robust functionality for manipulating lists, implementing queue-based patterns, and ensuring efficient handling of ordered data, making lists highly suitable for real-time data pipelines and task queues.

Learn more from the following resources:

- [@official@All Redis List Commands](https://redis.io/docs/latest/commands/?group=list)

## More Commands

# More Commands - Sorted Sets

Redis Sorted Sets include operations like ZREVRANGE to get elements in reverse order, ZRANGEBYLEX to retrieve elements within a specific lexicographical range, and ZINTERSTORE or ZUNIONSTORE to perform intersection and union operations on multiple sorted sets and store the results. Commands like ZREMrangeBYRANK and ZREMRANGEBYSCORE allow for removing elements based on their rank or score ranges.

Learn more from the following resources:

- [@official@All Redis Sorted Set Commands](https://redis.io/docs/latest/commands/?group=sorted-set)

## Multi

# MULTI

`MULTI` is a Redis command used to start a transaction, allowing a group of commands to be executed sequentially and atomically. After initiating a `MULTI` block, commands are queued instead of being executed immediately. Once all desired commands are added, the `EXEC` command is called to run them as a single atomic operation. If an error occurs in any command during queuing, it can be discarded using `DISCARD`. `MULTI` ensures that no other clients can interfere with the transaction, making it ideal for complex operations that require consistent state updates.

Learn more from the following resources:

- [@official@MULTI](https://redis.io/docs/latest/commands/multi/)

## Naming Conventions

# Naming Conventions

Naming conventions in Redis are crucial for maintaining organized and understandable data structures, especially in large applications. Common practices include using colons (`:`) as separators for hierarchical keys (e.g., `user:1001:settings`), employing prefixes to group related keys (e.g., `session:`, `cache:`), and using concise, descriptive names to indicate the purpose and type of the key.

## Network Security

# Network Security

Network security in Redis involves implementing measures to protect the server from unauthorized access and data breaches. Best practices include binding Redis to trusted interfaces, using firewalls to restrict access, and configuring `requirepass` for password protection. Redis should run in a secure network environment, ideally with TLS/SSL enabled for encrypted communication. Additionally, the use of `ACL` (Access Control Lists) provides granular permissions for different users. By disabling dangerous commands and using proper authentication and authorization mechanisms, Redis instances can be secured against common threats such as unauthorized data access and denial-of-service attacks.

Learn more from the following resources:

- [@official@Redis Authentication](https://redis.io/docs/latest/operate/oss_and_stack/management/security/#authentication)
- [@official@Redis Network Security](https://redis.io/docs/latest/operate/rc/security/database-security/network-security/)

## No Persistence Option

# No Persistence Option

The **No Persistence** option in Redis disables all data persistence mechanisms, meaning that no data will be saved to disk. This can be configured by turning off both RDB snapshots and AOF (Append-Only File) logging. Running Redis without persistence is ideal for use cases where high-speed caching is prioritized over data durability, such as storing ephemeral data or managing sessions that don’t need to survive a server restart. While this option reduces disk I/O and maximizes performance, it also means that all data will be lost if the server is shut down or crashes, making it suitable only for scenarios where data loss is acceptable.

Learn more from the following resources:

- [@official@Redis Persistence](https://redis.io/docs/latest/operate/oss_and_stack/management/persistence/)

## Optimistic Locking

# Optimistic Locking

Optimistic locking in Redis is implemented using the `WATCH` command in combination with transactions (`MULTI` and `EXEC`). `WATCH` monitors specified keys for changes before starting a transaction. If any of the watched keys are modified by another client before `EXEC` is called, the transaction is aborted, and `EXEC` returns `nil` instead of executing the queued commands. This allows Redis to handle concurrent updates without requiring traditional locks, making it ideal for scenarios where multiple clients might modify the same keys. Optimistic locking helps maintain data integrity while minimizing the performance overhead typically associated with locking mechanisms.

Learn more from the following resources:

- [@official@Optimistic Locking using CHECK & SET](https://redis.io/docs/latest/develop/interact/transactions/#optimistic-locking-using-check-and-set)
- [@official@WATCH Command](https://redis.io/docs/latest/commands/watch/)
- [@official@MULTI Command](https://redis.io/docs/latest/commands/multi/)

## Overview Of Data Types

# Overview of Data Types

Redis is a data structure server and at its core, REdis provides a collection of native data types that allow you to solve a wide variety of problems, from caching to event processing.

Learn more from the following resources:

- [@official@Understand Redis Data Types](https://redis.io/docs/latest/develop/data-types/)
- [@article@Redis Data Types](https://www.tutorialspoint.com/redis/redis_data_types.htm)

## Persistence Options

# Persistence Options

Redis provides two main persistence options: **RDB (Redis Database Backup)** and **AOF (Append-Only File)**. RDB creates point-in-time snapshots of the dataset at specified intervals, offering efficient storage with minimal performance impact, making it suitable for periodic backups but with potential data loss between snapshots. AOF logs every write operation to disk, providing higher data durability by allowing finer-grained recovery, though it can be more resource-intensive. Redis also supports a **hybrid persistence** mode that combines both RDB and AOF for faster restarts and stronger durability. Additionally, a **No Persistence** option is available for scenarios where data retention is unnecessary, prioritizing speed and memory efficiency.

Learn more from the following resources:

- [@official@Data Persistence](https://redis.io/docs/latest/operate/rc/databases/configuration/data-persistence/)
- [@official@Redis Persistence](https://redis.io/docs/latest/operate/oss_and_stack/management/persistence/)

## Pfadd

# PFADD

`PFADD` command used to add elements to a HyperLogLog data structure, which is designed for estimating the cardinality (number of unique elements) of a dataset. When elements are added using `PFADD`, Redis updates the internal structure without storing the actual elements, ensuring low memory consumption. This command returns `1` if the HyperLogLog was modified (i.e., a new unique element was added) and `0` otherwise. `PFADD` is ideal for use cases like counting unique visits or tracking unique events in a highly memory-efficient manner.

Learn more from the following resources:

- [@official@PFADD](https://redis.io/docs/latest/commands/pfadd/)

## Pfcount

# PFCOUNT

`PFCOUNT` is a Redis command used to retrieve the estimated number of unique elements in one or more HyperLogLog structures. It provides an approximate cardinality count with a typical error rate of 0.81%, making it highly efficient for large datasets while using minimal memory. When called with multiple HyperLogLog keys, `PFCOUNT` merges the data and returns the approximate count of the union, allowing for quick aggregation of unique elements across multiple sets.

Learn more from the following resources:

- [@official@PFCOUNT](https://redis.io/docs/latest/commands/pfcount/)

## Pfmerge

# PFMERGE

`PFMERGE` is a Redis command used to combine multiple HyperLogLog data structures into a single HyperLogLog key, creating a new structure that represents the union of all unique elements. This command is useful when you want to aggregate and estimate the cardinality of distinct elements across multiple datasets. The resulting HyperLogLog can then be queried using `PFCOUNT` to get the approximate count of the merged unique elements.

Learn more from the following resources:

- [@official@PFMERGE](https://redis.io/docs/latest/commands/pfmerge/)

## Pipelining

# Pipelining

Pipelining in Redis is a technique that allows clients to send multiple commands to the server without waiting for individual responses after each command. Instead, the commands are sent in a batch, and responses are read together at the end. This reduces the network overhead and latency associated with multiple round trips, significantly improving throughput, especially in high-volume operations.

Learn more from the following resources:

- [@official@Redis Pipelining](https://redis.io/docs/latest/develop/use/pipelining/)

## Pre Compiled Binaries

# Pre-compiled Binaries

Redis can be compiled and installed on a variety of platofrm and operating systems including Linux and macOS, the Redis binaries have no dependencies other than a C compiler and libc

Learn more from the following resources:

- [@official@Installing Redis from Source](https://redis.io/docs/latest/operate/oss_and_stack/install/install-redis/install-redis-from-source/)
- [@article@How to install Redis from source on Ubuntu and CentOS](https://docs.vultr.com/how-to-install-redis-from-source-on-ubuntu-and-centos)

## Publish

# PUBLISH

`PUBLISH` is a Redis command used to send messages to a specified channel in the pub/sub messaging system. When a message is published, all clients that are subscribed to that channel receive the message immediately. This command is useful for implementing real-time communication features, such as chat applications, notifications, or event broadcasting. The `PUBLISH` command does not return any acknowledgment to the sender, as it operates on a fire-and-forget basis, allowing for efficient message distribution without requiring the sender to wait for subscribers to process the message.

Learn more from the following resources:

- [@official@PUBLISH](https://redis.io/docs/latest/commands/publish/)

## Pubsub Messaging

# Pub/Sub Messaging

Pub/Sub messaging in Redis is a messaging pattern that allows clients to communicate with each other through channels without needing direct connections. In this model, clients can subscribe to one or more channels to receive messages and can publish messages to these channels. When a message is published, all subscribed clients receive it in real-time, making it ideal for applications requiring instant notifications, such as chat systems, live updates, or event broadcasting. Redis's implementation of Pub/Sub is simple and efficient, supporting commands like `PUBLISH`, `SUBSCRIBE`, and `UNSUBSCRIBE`, although it does not provide message persistence or acknowledgment, which means that messages are not stored for clients that are not actively subscribed at the time of publishing.

Learn more from the following resources:

- [@official@Redis Pub/Sub](https://redis.io/docs/latest/develop/interact/pubsub/)
- [@official@PUBLISH Command](https://redis.io/docs/latest/commands/publish/)
- [@official@SUBSCRIBE Command](https://redis.io/docs/latest/commands/subscribe/)
- [@official@UNSUBSCRIBE Command](https://redis.io/docs/latest/commands/unsubscribe/)

## Pubsub

# Pub/Sub

Pub/Sub in Redis is a powerful messaging paradigm that allows for real-time communication between clients through a publish/subscribe model. In this system, publishers send messages to specific channels without knowing who, if anyone, will receive them. Subscribers, on the other hand, express interest in particular channels and receive messages published to those channels instantly. This decouples the message producers from the consumers, facilitating flexible and scalable communication. Key commands in this model include `PUBLISH` for sending messages, `SUBSCRIBE` for listening to channels, and `UNSUBSCRIBE` for stopping the reception of messages.

Visit the following resources to learn more:

- [@official@Pub/Sub in Redis](https://redis.io/docs/latest/develop/interact/pubsub/)

## Rdb Vs Aof Tradeoffs

# RDB vs AOF Tradeoffs

When comparing RDB (Redis Database Backup) and AOF (Append-Only File) for data persistence in Redis, several trade-offs must be considered.

**RDB** is optimized for performance and efficient storage, creating point-in-time snapshots of the dataset at specified intervals. It is faster for startup since it loads a single file and consumes less disk I/O during normal operations. However, it may lead to data loss between snapshots if the server crashes, as changes made during that interval are not saved.

**AOF**, on the other hand, logs every write operation in real-time, allowing for more granular recovery with minimal data loss, as you can replay commands to reconstruct the dataset. This comes at the cost of increased disk I/O and potential performance overhead, especially with frequent write operations. The AOF file can also grow significantly, requiring periodic rewriting to optimize size.

Learn more from the following resources:

- [@official@RDB Advantages](https://redis.io/docs/latest/operate/oss_and_stack/management/persistence/#rdb-advantages)
- [@official@AOF Advantages](https://redis.io/docs/latest/operate/oss_and_stack/management/persistence/#aof-advantages)
- [@article@AOF vs RDB, Which One to Choose?](https://codedamn.com/news/backend/redis-data-persistence-aof-vs-rdb)

## Real Time Analytics

# Real-time Analytics

Real-time analytics in Redis involves the immediate processing and analysis of data as it is generated or received, enabling businesses and applications to gain insights and make decisions on-the-fly. Redis's in-memory data storage architecture allows for extremely low-latency access to data, making it ideal for scenarios such as monitoring user behavior, tracking metrics, and processing events in real-time. With support for various data structures like sorted sets for leaderboards, streams for event logging, and pub/sub for live notifications, Redis facilitates efficient aggregation, querying, and visualization of data.

Learn more from the following resources:

- [@official@Real-time Analytics with Redis](https://redis.io/resources/real-time-analytics-redis/)

## Redis Benchmark

# redis-benchmark

`redis-benchmark` is a utility provided with Redis that measures the performance of the Redis server by simulating various types of workloads. It allows users to test the speed and responsiveness of Redis commands under different conditions, providing metrics such as requests per second and latency. The tool can simulate multiple clients and different command types, such as `GET`, `SET`, and `INCR`, enabling users to evaluate the performance of their Redis configuration and hardware. By adjusting parameters like the number of parallel connections and the number of requests to be sent, `redis-benchmark` helps identify performance bottlenecks, optimize configurations, and assess the impact of changes to the Redis environment, making it a valuable tool for capacity planning and performance tuning.

Learn more from the following resources:

- [@official@Redis Benchmark](https://redis.io/docs/latest/operate/oss_and_stack/management/optimization/benchmarks/)
- [@article@How to benchmark the performance of a Redis server](https://www.digitalocean.com/community/tutorials/how-to-perform-redis-benchmark-tests)

## Redis Enterprise

# Redis Enterprise

Redis Enterprise is a commercial offering that extends the capabilities of open-source Redis with advanced features designed for high availability, scalability, and performance in enterprise environments. It provides automatic sharding and replication, allowing for seamless horizontal scaling across multiple nodes and data centers. Redis Enterprise supports various deployment options, including on-premises, cloud, and hybrid environments, and offers enhanced data persistence options like active-active geo-distribution for global applications. Additionally, it includes advanced security features, such as role-based access control (RBAC), encryption, and audit logging, along with built-in monitoring and management tools. Redis Enterprise is particularly suited for mission-critical applications that require low-latency access to data and robust data management capabilities, making it ideal for use cases like real-time analytics, session management, and caching.

Learn more from the following resources:

- [@official@Redis Enterprise](https://redis.io/about/redis-enterprise/)
- [@official@Redis Enterprise Software](https://redis.io/docs/latest/operate/rs/)
- [@article@Redis Open Source vs. Enterprise](https://www.metricfire.com/blog/redis-open-source-vs-enterprise/)

## Redis Modules

# Redis Modules

Redis Modules are extensions that enhance the core functionality of Redis by adding new data types, commands, and capabilities. These modules allow developers to customize and extend Redis to better fit specific application needs without modifying the core Redis source code. Examples of popular Redis Modules include:

1. **RediSearch**: Provides full-text search capabilities, allowing for indexing and querying data with complex search queries.
2. **RedisGraph**: Adds graph database capabilities, enabling the storage and querying of graph data using the Cypher query language.
3. **RedisJSON**: Facilitates the handling of JSON data structures, allowing for storage, retrieval, and manipulation of JSON documents within Redis.
4. **RedisTimeSeries**: Optimized for time-series data, offering features for storing, querying, and aggregating time-stamped data efficiently.
5. **RedisAI**: Integrates artificial intelligence capabilities, allowing for the execution of machine learning models directly within Redis.

These modules enable users to leverage Redis for a wide variety of use cases, from real-time analytics and search functionalities to complex data relationships and machine learning, while maintaining the performance and simplicity of Redis as an in-memory database.

## Redis On Flash

# Redis on Flash

Redis on Flash is a feature of Redis Enterprise that allows users to extend the memory capacity of their Redis instances by utilizing SSDs (Solid State Drives) alongside traditional RAM. This enables organizations to store larger datasets at a lower cost while maintaining the high performance that Redis is known for.  In this configuration, frequently accessed data remains in RAM for fast access, while less frequently used data can be stored on Flash storage. Redis on Flash intelligently manages the data placement between memory and Flash, ensuring that performance is optimized by leveraging the speed of in-memory operations while still allowing for the efficient storage of larger datasets. This capability is particularly beneficial for use cases involving large-scale applications, such as caching, real-time analytics, and high-throughput data processing, as it allows organizations to handle big data workloads without the need for extensive investments in additional RAM.

Learn more from the following resources:

- [@official@Redis on Flash](https://redis.io/blog/redis-on-flash-now-3-7x-faster/)
- [@official@Redis on Flash Data Sheet](https://media.trustradius.com/product-downloadables/1V/DT/TCXS6PSOA64L.pdf)

## Redis Sentinel

# Redis Sentinel

Redis Sentinel serves as a robust high-availability solution for Redis deployments, offering a comprehensive suite of monitoring, notification, and automatic failover capabilities. By continuously overseeing master and replica Redis servers, Sentinel ensures system integrity and swift response to failures. In the event of a master instance failure, it seamlessly promotes a replica to master status, reconfiguring the system to maintain service continuity with minimal downtime.

Learn more from the following resources:

- [@official@High Availability with Redis Sentinel](https://redis.io/docs/latest/operate/oss_and_stack/management/sentinel/)

## Redis Vs Sqlnosql Dbs

# Redis vs SQL/NoSQL DBs

Redis differs significantly from traditional SQL and NoSQL databases in terms of data model, performance, and use cases. Redis is an in-memory key-value store that supports various data structures like strings, hashes, lists, and sets, allowing for flexible data handling and low-latency access. This makes it ideal for high-speed operations such as caching, real-time analytics, and session management. In contrast, SQL databases use a structured schema with tables and relationships, excelling in complex queries and transactions, while other NoSQL databases may utilize document, graph, or wide-column models to accommodate unstructured or semi-structured data.

Learn more from the following resources:

- [@article@Redis vs MongoDB](https://aws.amazon.com/compare/the-difference-between-redis-and-mongodb/)
- [@video@Understanding NoSQL vs SQL](https://www.youtube.com/watch?v=9JHrL0UWrWs)

## Redisbloom

# RedisBloom

RedisBloom is a Redis module that extends the capabilities of Redis by introducing probabilistic data structures, allowing for efficient membership testing and counting while minimizing memory usage. It provides tools such as Bloom Filters, Cuckoo Filters, Count-Min Sketches, and HyperLogLogs, enabling developers to manage large datasets with high performance and low memory overhead. With Bloom Filters, for instance, users can quickly determine if an element is possibly in a set or definitely not, making it useful for applications like web caching, spam filtering, and network security. Cuckoo Filters offer similar functionality but allow for the deletion of items. Count-Min Sketches enable approximate counting of elements in a dataset, while HyperLogLogs provide efficient cardinality estimation. RedisBloom is particularly beneficial for use cases involving big data analytics, real-time monitoring, and applications requiring high throughput with limited memory resources.

Learn more from the following resources:

- [@official@RedisBloom](https://redis.io/probabilistic/)
- [@opensource@RedisBloom/RedisBloom - GitHub](https://github.com/RedisBloom/RedisBloom)

## Rediscommander

# RedisCommander

RedisCommander is a web-based GUI management tool for Redis that simplifies the interaction with Redis databases through a user-friendly interface. It allows users to browse, edit, and manage Redis keys and data structures easily, providing visual representations of data types such as strings, hashes, lists, sets, and sorted sets. With RedisCommander, users can perform common operations like adding, modifying, and deleting keys, as well as executing commands directly from the interface. The tool also supports features like searching for keys, viewing key details, and monitoring server performance metrics. RedisCommander is particularly useful for developers and administrators who prefer a graphical interface over command-line interaction, making it easier to manage Redis instances, troubleshoot issues, and explore data in real-time. Overall, it enhances productivity and streamlines Redis database management tasks.

Learn more from the following resources:

- [@opensource@joeferner/redis-commander - GitHub](https://github.com/joeferner/redis-commander)

## Redisconf

# redis.conf

`redis.conf` is the configuration file used by Redis to set up server parameters and customize its behavior. This file allows administrators to specify various settings, including memory limits, persistence options (like RDB and AOF), network configurations (such as port and binding addresses), and security features (like password protection and access control). Key parameters within `redis.conf` include `maxmemory`, which sets the maximum amount of memory Redis can use, `save`, which defines RDB snapshot intervals, and `requirepass`, which enables password authentication for client connections.

Learn more from the following resources:

- [@official@Redis Configuration Documentation](https://redis.io/docs/latest/operate/oss_and_stack/management/config/)
- [@official@Redis Configuration File Example](https://redis.io/docs/latest/operate/oss_and_stack/management/config-file/)

## Redisinsight

# RedisInsight

RedisInsight is an advanced graphical user interface (GUI) tool developed by Redis Labs that provides comprehensive management and monitoring capabilities for Redis databases. It offers users an intuitive interface to visualize and interact with their Redis data, making it easier to manage data structures such as strings, hashes, lists, sets, and sorted sets. With RedisInsight, users can perform tasks like querying and modifying data, running commands, and analyzing performance metrics in real-time. It includes features such as a query builder, visual data exploration, and memory analysis tools to help identify key usage patterns and potential optimization opportunities. Additionally, RedisInsight supports monitoring of multiple Redis instances, allowing administrators to keep track of performance and health across their deployments. Overall, RedisInsight enhances the user experience by simplifying complex Redis operations and providing valuable insights into database performance and data management.

Learn more from the following resources:

- [@official@RedisInsight](https://redis.io/insight/)
- [@opensource@RedisInsight/RedisInsight - RedisInsight Module on GitHub](https://github.com/RedisInsight/RedisInsight)

## Redisjson

# RedisJSON

RedisJSON is a Redis module that enables the storage, retrieval, and manipulation of JSON documents directly within Redis. It provides a rich set of commands for working with JSON data structures, allowing users to perform operations such as adding, updating, and querying JSON documents efficiently. With RedisJSON, users can store complex nested data and perform queries on specific fields, making it ideal for applications that require handling structured data without the need for additional data transformation or processing layers. Key features include support for JSONPath querying, atomic updates, and the ability to index JSON fields for faster retrieval. This module enhances Redis's capabilities, making it a suitable choice for use cases like real-time analytics, configuration management, and any application that benefits from the flexibility and performance of JSON data structures. Overall, RedisJSON allows developers to leverage the speed of Redis while working with JSON natively, streamlining data management in modern applications.

Learn more from the following resources:

- [@official@RedisJSON](https://redis.io/json/)
- [@opensource@RedisJSON/RedisJSON - GitHub](https://github.com/RedisJSON/RedisJSON)

## Redistimeseries

# RedisTimeSeries

RedisTimeSeries is a Redis module specifically designed for efficiently storing, querying, and managing time-series data, making it ideal for applications such as IoT monitoring, financial data analysis, and real-time analytics. It allows users to easily ingest time-stamped data, perform aggregations, and retrieve data across specified time intervals with minimal latency. The module supports features like automatic downsampling, retention policies, and powerful querying capabilities, enabling users to analyze trends and patterns over time while efficiently storing metadata alongside the time-series data.

Learn more from the following resources:

- [@official@RedisTimeSeries](https://redis.io/timeseries/)
- [@official@Time Series Documentation](https://redis.io/docs/latest/develop/data-types/timeseries/)

## Replication Basics

# Replication Basics

Replication in Redis is a process that allows data from one Redis instance (the master) to be copied to one or more Redis instances (the replicas). This mechanism enhances data availability, reliability, and scalability. When a master instance receives write operations, it propagates these changes to its replicas, ensuring they maintain an up-to-date copy of the data. Replication in Redis is asynchronous, meaning that replicas may lag behind the master, but this design improves performance by allowing the master to handle write operations without waiting for replicas to confirm the receipt of data. In addition to providing redundancy, Redis replication supports read scaling, as read operations can be distributed across replicas, reducing the load on the master. Configuring replication is straightforward, requiring minimal setup in the `redis.conf` file to designate a master and its replicas. Overall, replication is a fundamental feature in Redis that plays a crucial role in building resilient and scalable applications.

Learn more from the following resources:

- [@official@Redis Replication](https://redis.io/docs/latest/operate/oss_and_stack/management/replication/)

## Retrieval By Pattern

# Retrieval by Pattern

The SCAN command in Redis is a cursor-based iterator that does not guarantee to return all matching keys in one call, even if COUNT is specified. Instead, SCAN returns a small subset of keys that match the pattern, requiring subsequent calls to complete the iteration. Redis offers powerful pattern-based key retrieval, allowing users to query multiple keys using wildcard patterns. This functionality primarily relies on the KEYS command, which supports glob-style patterns such as *, ?, and [] for flexible matching.

Learn more from the following resources:

- [@official@SCAN](https://redis.io/docs/latest/commands/scan/)

## Rich Data Structures

# Rich Data Structures

Redis provides data structures such as strings, hashes, lists, sets, sorted sets with range queries, bitmaps, hyperloglogs, geospatial indexes, and streams.

Learn more from the following resources:

- [@official@Data Structures](https://redis.io/redis-enterprise/data-structures/)
- [@official@Understand Redis Data Types](https://redis.io/docs/latest/develop/data-types/)

## Rpop

# RPOP

The RPOP command removes and then returns the last elements of the list stored and the specified key, by default it will pop only a single element from the list.

Learn more from the following resources:

- [@official@RPOP](https://redis.io/docs/latest/commands/rpop/)

## Rpush

# RPUSH

The RPUSH command will insert all the specified values at the tail end o the list that is stored at the defined key, if the key does not exist then it will be created as an empty list before performing the push.

Learn more from the following resources:

- [@official@RPUSH](https://redis.io/docs/latest/commands/rpush/)

## Sadd

# SADD

The SADD command will add the specified members to the set which is stored and the defined key, any specified members that are already a member of the set will simply be ignored.

Learn more from the following resources:

- [@official@SADD](https://redis.io/docs/latest/commands/sadd/)

## Scard

# SCARD

`SCARD` is a Redis command used to get the number of members in a set, it returns the cardinality of the specified set, which is the total count of unique elements it contains. If the set does not exist, `SCARD` returns `0`. This command is useful for quickly determining the size of a set, allowing applications to make decisions based on the number of unique items, such as checking user participation in a campaign or the count of unique tags in a system.

Learn more from the following resources:

- [@official@SCARD](https://redis.io/docs/latest/commands/scard/)

## Sdiff

# SDIFF

The SDIFF coimmand returns the members of a set resulting from the difference between the first set and all the following sets.

Learn more from the following resources:

- [@official@SDIFF](https://redis.io/docs/latest/commands/sdiff/)

## Search

# Search

Redis Search enhances the Redis experience by offering a robust set of search and query features, including a rich query language, incremental indexing for JSON and hash documents, vector search, full-text search, geospatial queries, and aggregations. These capabilities allow Redis to function as a document database, vector database, secondary index, and search engine, making it suitable for a variety of applications.

Learn more from the following resources:

- [@official@Search and Query](https://redis.io/docs/latest/operate/oss_and_stack/stack-with-enterprise/search/)
- [@video@Querying, Indexing and Full-text Search in Redis](https://www.youtube.com/watch?v=infTV4ifNZY)

## Security And Compliance

# Security and Compliance

Security and compliance in Redis involve implementing various measures to protect data, ensure secure access, and adhere to relevant regulatory standards. Redis provides several built-in security features, such as password authentication using the `requirepass` directive, which restricts access to authorized users only. Additionally, Redis supports TLS/SSL encryption, allowing for secure communication between clients and the server, protecting data in transit from eavesdropping and tampering. Access control can be further enhanced through Redis's Access Control Lists (ACLs), which allow administrators to define user roles and permissions, controlling which commands users can execute and which keys they can access. It’s also important to configure Redis to bind to trusted network interfaces, limiting exposure to potential threats.

Learn more from the following resources:

- [@official@Redis Security Documentation](https://redis.io/docs/latest/operate/rs/security/)
- [@article@How to Secure Redis](https://goteleport.com/blog/secure-redis/)
- [@video@Rediscover Redis Security](https://www.youtube.com/watch?v=oD8k3ymbfkY)

## Session Management

# Session Management

Redis session management leverages the database's speed and versatility for efficient web application user session handling by using key-value storage with session IDs as keys, allowing quick access and updates.

Learn more from the following resources:

- [@official@Redis Distributed Session Management](https://redis.io/solutions/session-management/)
- [@article@Session Management Basics with Redis](https://dev.to/koshirok096/session-management-basics-with-redis-2o2e)

## Set

# SET

The SET command sets the defined key to hold a value, if the key already holds a value then it will be overwritten regardless of its type.

Learn more from the following resources:

- [@official@SET](https://redis.io/docs/latest/commands/set/)

## Setbit

# SETBIT

The SETBIT command sets or clearts the bit at the specified offset in the string value that is stored at the specified key. When the key does not exist, a new string value will be created and the string is grown to make sure it can hold a bit to the same value as the earlier defined offset.

Learn more from the following resources:

- [@official@SETBIT](https://redis.io/docs/latest/commands/setbit/)

## Sets

# Sets

A Redis set is an unordered collection of members which can be used to track unique items, represent relations and preform set operations.

Learn more from the following resources:

- [@official@Redis Sets](https://redis.io/docs/latest/develop/data-types/sets/)

## Setting And Getting Keys

# Setting and Getting Keys

In Redis, setting keys refers to the operation of storing keys by associating them with unique identifiers (keys), it's the process of writing or updating data in the systems. Getting keys refers to the process of retrieving data from the system using the associated key.

Learn more from the following resources:

- [@official@Keys](https://redis.io/docs/latest/commands/keys/)
- [@official@SET](https://redis.io/docs/latest/commands/set/)
- [@article@Set key values](https://www.w3resource.com/redis/redis-set-key-value.php)

## Sinter

# SINTER

The SINTER command will return members of the set which will result in the intersection of all the given sets, keys that do not exist are considered to be empty sets.

Learn more from the following resources:

- [@official@SINTER](https://redis.io/docs/latest/commands/sinter/)

## Sismember

# SISMEMBER

The SISMEMBER command will simply return a boolean value is the members is a part of the set stored at key.

Learn more from the following resources:

- [@official@SISMEMBER](https://redis.io/docs/latest/commands/sismember/)

## Slow Log Analysis

# Slow Log Analysis

The Redis Slow Log in a system to log any queries that take longer than a specified time. The execution time does not include any I/O operations such as talking with the client, just the time need to execute the specified command.

Learn more from the following resources:

- [@official@SLOWLOG](https://redis.io/docs/latest/commands/slowlog/)
- [@official@View Redis Slow Log](https://redis.io/docs/latest/operate/rs/clusters/logging/redis-slow-log/)

## Smembers

# SMEMBERS

The SMEMBERS command returns all the members of the set that is defined at key.

Learn more from the following resources:

- [@official@SMEMBERS](https://redis.io/docs/latest/commands/smembers/)

## Sorted Sets

# Sorted Sets

A sorted set in Redis is a collection of unique strings, or members, that are ordered by an associated score. When more than one string has the same score, the strings are ordered lexicographically.

Learn more from the following resources:

- [@official@Sorted Sets](https://redis.io/docs/latest/develop/data-types/sorted-sets/)

## Srem

# SREM

The SREM command will remove the specified members from the set stored at the defined key, specified members that are not a member of the set will be ignored.

Learn more from the following resources:

- [@official@SREM](https://redis.io/docs/latest/commands/srem/)

## Ssltls Encryption

# SSL/TLS Encryption

SSL/TLS is supported by Redis starting with version 6 as an optional feature that needs to be enabled at compile time. TLS will add a layer to the communication stack with overheads due to the read and writes from an SSL connection and integrity checks, this will lead to a decrease of achieveable throughput.

Learn more from the following resources:

- [@official@Redis TLS Support](https://redis.io/docs/latest/operate/oss_and_stack/management/security/encryption/#getting-started)
- [@official@Transport Layer Security Documentation](https://redis.io/docs/latest/operate/rc/security/database-security/tls-ssl/)

## Starting The Server

# Starting the Server

Starting a Redis server is platform dependant and is usually done via `systemctl` on Linux or `brew services` on MacOS.

Learn more from the following resources:

- [@official@Start and stop Redis on MacOS](https://redis.io/docs/latest/operate/oss_and_stack/install/install-redis/install-redis-on-mac-os/#starting-and-stopping-redis-in-the-foreground)
- [@official@Start and stop Redis on Ubuntu/Debian](https://redis.io/docs/latest/operate/oss_and_stack/install/install-redis/install-redis-on-linux/#starting-and-stopping-redis-in-the-background)
- [@official@Install and start Redis on WSL2](https://redis.io/docs/latest/operate/oss_and_stack/install/install-redis/install-redis-on-windows/#install-redis)

## Streams

# Streams

A Redis stream is a data structure that acts like an append-only log but can also implement multiple operations to overcome limits seen in typical append-only logs. These include random access in O(1) time and complex consumption strategies, such as consumer groups.

Learn more from the following resources:

- [@official@Redis Streams](https://redis.io/docs/latest/develop/data-types/streams/)
- [@official@Transport Layer Security Documentation](https://redis.io/docs/latest/operate/rc/security/database-security/tls-ssl/)

## Strings

# Strings

Strings in Redis are binary-safe, meaning they can contain any kind of data, including text, integers, floats, or even binary data like images and they can hold up to 512 MB of data per key. Redis strings support a wide range of operations, from basic CRUD (Create, Read, Update, Delete) to more complex manipulations like incrementing/decrementing numeric values, appending data, or extracting substrings.

Learn more from the following resources:

- [@official@Redis Strings](https://redis.io/docs/latest/develop/data-types/strings/)

## Strlen

# STRLEN

The STRLEN command returns the length of a string value that is stored at the defined key, if no string value is help at the key then an error will be returned.

Learn more from the following resources:

- [@official@STRLEN](https://redis.io/docs/latest/commands/strlen/)

## Subscribe

# SUBSCRIBE

The SUBSCRIBE command subscribes the client to the channels specified, once subscribed the client enters a state where it is not supposed to issue any other commands, except from those in the SUBSCRIBE subset i.e. SSUBSCRIBE, PSUBSCRIBE etc.

Learn more from the following resources:

- [@official@SUBSCRIBE](https://redis.io/docs/latest/commands/subscribe/)

## Sunion

# SUNION

The SUNION command returns the members of a set resulting in a union of all the given sets.

Learn more from the following resources:

- [@official@SUNION](https://redis.io/docs/latest/commands/sunion/)

## Transactions

# Transactions

Redis Transactions allow the execution of a group of commands in a single step, they are centered around the commands MULTI, EXEC, DISCARD and WATCH.

Learn more from the following resources:

- [@official@Transactions](https://redis.io/docs/latest/develop/interact/transactions/)
- [@official@MULTI](https://redis.io/docs/latest/commands/multi/)
- [@official@EXEC](https://redis.io/docs/latest/commands/exec/)
- [@official@DISCARD](https://redis.io/docs/latest/commands/discard/)
- [@official@WATCH](https://redis.io/docs/latest/commands/watch/)

## Truncation  Corruption

# Truncation / Corruption

Truncation and corruption typically refer to scenarios where data is unexpectedly cut off or altered, compromising its integrity. This can occur due to various reasons, such as sudden power failures, system crashes, or disk errors. Redis mitigates these risks through its persistence mechanisms like RDB snapshots and AOF (Append-Only File) logs.

Learn more from the following resources:

- [@official@AOF Advantages](https://redis.io/docs/latest/operate/oss_and_stack/management/persistence/#aof-advantages)
- [@official@What should I do if my AOF gets truncated?](https://redis.io/docs/latest/operate/oss_and_stack/management/persistence/#what-should-i-do-if-my-aof-gets-truncated)
- [@official@What should I do if my AOF gets corrupted?](https://redis.io/docs/latest/operate/oss_and_stack/management/persistence/#what-should-i-do-if-my-aof-gets-corrupted)

## Ttl

# TTL

The TTL command returns the remaining time left to live of a key that is specified, this capability allows a Redis client to check how many seconds a given key will continue to be a part of a dataset.

Learn more from the following resources:

- [@official@TTL](https://redis.io/docs/latest/commands/ttl/)

## Unsubscribe

# UNSUBSCRIBE

The UNSUBSCRIBE command unsubscribes the client for the given channels, or all channels if none are specifically stated.

Learn more from the following resources:

- [@official@UNSUBSCRIBE](https://redis.io/docs/latest/commands/unsubscribe/)

## Upgrading Redis

# Upgrading Redis

Upgrading Redis typically involves careful planning and execution to ensure minimal downtime and data integrity. The process generally includes backing up your data, installing the new Redis version, updating configuration files to accommodate any new settings or deprecated options, and restarting the Redis server.

Learn more from the following resources:

- [@official@Redis Administration](https://redis.io/docs/latest/operate/oss_and_stack/management/admin/)
- [@official@Upgrading or Restarting a Redis instance without downtime](https://redis.io/docs/latest/operate/oss_and_stack/management/admin/#upgrading-or-restarting-a-redis-instance-without-downtime)

## Usecases  Best Practices

# Usecases / Best Practices

## Usecases

# Usecases

## Usecases

# Usecases

## Usecases

# Usecases

## Usecases

# Usecases

## Usecases

# Usecases

## Usecases

# Usecases

## Usecases

# Usecases

## Usecases

# Usecases

## Usecases

# Usecases

## Usecases

# Usecases

## Usecases

# Usecases

## Usecases

# Usecases

## Using Docker

# Using Docker

Redis Community Edition can be installed on Docker but it is recommended to complete the installation of Redis Stack in order to gain access to the modeling capabilities, be able to seach and query data, as well as using Redis as a vector database.

Learn more from the following resources:

- [@official@How can I install Redis on Docker?](https://redis.io/kb/doc/1hcec8xg9w/how-can-i-install-redis-on-docker)
- [@official@redis/redis-stack-server](https://hub.docker.com/r/redis/redis-stack-server)

## Using Package Managers

# Using Package Managers

Redis can be installed on Linux, MacOS and WSL2 via the platform specific package managers such as yum, apt and brew.

Learn more from the following resources:

- [@official@Install via apt](https://redis.io/docs/latest/operate/oss_and_stack/install/install-stack/linux/)
- [@official@Install via brew](https://redis.io/docs/latest/operate/oss_and_stack/install/install-redis/install-redis-on-mac-os/)
- [@official@Install on WSL2](https://redis.io/docs/latest/operate/oss_and_stack/install/install-redis/install-redis-on-windows/)

## Watch

# WATCH

The WATCH command marks the given keys to be watched for conditional execution of a transaction. It's a critical component of Redis's approach to handling race conditions in multi-key transactions.

Learn more from the following resources:

- [@official@WATCH](https://redis.io/docs/latest/commands/watch/)

## What Is Redis

# What is Redis?

Redis is an open-source, in-memory data structure store, primarily used as a database, cache, and message broker. It supports various data structures like strings, hashes, lists, sets, and sorted sets, making it highly versatile. Redis operates with extremely low latency due to its in-memory nature, enabling fast access to data. It is often used in real-time applications such as session management, leaderboards, or caching mechanisms, where quick data retrieval is critical. Additionally, Redis supports data persistence by periodically writing the dataset to disk, balancing memory speed with data reliability.

Visit the following resources to learn more:

- [@official@What is Redis?](https://redis.io/docs/latest/get-started/)
- [@official@Introduction to Redis](https://redis.io/about/)
- [@article@Redis - Wikipedia](https://en.wikipedia.org/wiki/Redis)
- [@article@What is Redis Explained? - IBM](https://www.ibm.com/think/topics/redis)

## When To Choose Redis

# When to choose Redis?

Redis is ideal when you need a fast, in-memory data store with low latency and high throughput. It's particularly well-suited for caching, session management, real-time analytics, leaderboards, and message queues. 

Learn more from the following resources:

- [@official@Introduction to Redis](https://redis.io/about/)
- [@video@Why Use Redis For All Your Applications](https://www.youtube.com/watch?v=ZL4cHe3oL84)

## When To Consider Enterprise

# When to consider enterprise?

Redis Enterprise is typically considered when an organization requires enhanced scalability, high availability, and advanced features beyond what open-source Redis provides. It's particularly valuable for large-scale applications with demanding performance requirements, complex architectures, or mission-critical deployments.

Learn more from the following resources:

- [@official@About Redis Enterprise](https://redis.io/about/redis-enterprise/)
- [@official@Redis Enterprise](https://redis.io/enterprise/)

## Xadd

# XADD

The XADD command used to append new entries to a stream data structure. It allows you to add one or more field-value pairs as a single entry, automatically assigning a unique ID to each new entry.

Learn more from the following resources:

- [@official@XADD](https://redis.io/docs/latest/commands/xadd/)

## Xlen

# XLEN

The XLEN command used to get the length of a stream, returning the number of entries it contains. This simple yet powerful command provides a quick way to assess the size of a stream without retrieving its contents. Unlike other Redis types, zero-length streams are possible so XLEN should be used in tandem with TYPE or EXISTS.

Learn more from the following resources:

- [@official@XLEN](https://redis.io/docs/latest/commands/xlen/)

## Xrange

# XRANGE

The XRANGE command used for retrieving messages from a stream. It allows you to query a range of messages based on their IDs, returning them in chronological order. This command is particularly useful for reading a portion of a stream's history, enabling efficient data retrieval and processing.

Learn more from the following resources:

- [@official@XRANGE](https://redis.io/docs/latest/commands/xrange/)

## Xread

# XREAD

The XREAD command reads data from one or more streams, only returning entries with an ID greater than the last received ID.

Learn more from the following resources:

- [@official@XREAD](https://redis.io/docs/latest/commands/xread/)

## Zadd

# ZADD

The ZADD command adds all of the specified members with the specified scores to the sorted set defined at `key`.

Learn more from the following resources:

- [@official@ZADD](https://redis.io/docs/latest/commands/zadd/)

## Zcount

# ZCOUNT

ZCOUNT returns the number of elements in the sorted set at the targetted `key`, with a score between `min` and `max`.

Learn more from the following resources:

- [@official@ZCOUNT](https://redis.io/docs/latest/commands/zcount/)

## Zincrby

# ZINCRBY

ZINCRBY increments the score of a member in a sorted set by the defined increment. If the member targeted does not exists in the sorted set then it will be added and will be assigned the value of the increment. If the key does not exists that ZINCRBY will created the set with the targeted member as it's only member.

Learn more from the following resources:

- [@official@ZINCRBY](https://redis.io/docs/latest/commands/zincrby/)

## Zrange

# ZRANGE

The ZRANGE command can perform multiple range queries including by rank, by score or by lexiographical order. The order of elements returned are always from lowest to highest and any score ties are resolved using reverse lexiographical ordering.

Learn more from the following resources:

- [@official@ZRANGE](https://redis.io/docs/latest/commands/zrange/)

## Zrangebyscore

# ZRANGEBYSCORE

This command retrieves elements from a sorted set stored at the specified key. It returns all elements with scores falling within the given min and max range, inclusive of both boundaries. Elements are ordered from lowest to highest score. For elements sharing the same score, the command returns them in lexicographical order. This ordering is an inherent property of Redis sorted sets and requires no additional computation.

Learn more from the following resources:

- [@official@ZRANGEBYSCORE](https://redis.io/docs/latest/commands/zrangebyscore/)

## Zrank

# ZRANK

ZRANK returns the rank of member in the sorted set stored at key, with the scores ordered from low to high. The rank is 0-based, which means that the member with the lowest score has rank 0. The optional WITHSCORE argument supplements the command's reply with the score of the element returned.

Learn more from the following resources:

- [@official@ZRANK](https://redis.io/docs/latest/commands/zrank/)

## Zrem

# ZREM

Removes the specified members from the sorted set stored at key. Non existing members are ignored. An error is returned when key exists and does not hold a sorted set.

Learn more from the following resources:

- [@official@ZREM](https://redis.io/docs/latest/commands/zrem/)
