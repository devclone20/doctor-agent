# System Design Roadmap

## Ambassador

# Ambassador

Create helper services that send network requests on behalf of a consumer service or application. An ambassador service can be thought of as an out-of-process proxy that is co-located with the client.

This pattern can be useful for offloading common client connectivity tasks such as monitoring, logging, routing, security (such as TLS), and resiliency patterns in a language agnostic way. It is often used with legacy applications, or other applications that are difficult to modify, in order to extend their networking capabilities. It can also enable a specialized team to implement those features.

Visit the following resources to learn more:

- [@article@Ambassador pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/ambassador)

## Anti Corruption Layer

# Anti-corruption Layer

Implement a facade or adapter layer between different subsystems that don't share the same semantics. This layer translates requests that one subsystem makes to the other subsystem. Use this pattern to ensure that an application's design is not limited by dependencies on outside subsystems. This pattern was first described by Eric Evans in Domain-Driven Design.

Visit the following resources to learn more:

- [@article@Anti-corruption Layer pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/anti-corruption-layer)

## Application Caching

# Application Caching

In-memory caches such as Memcached and Redis are key-value stores between your application and your data storage. Since the data is held in RAM, it is much faster than typical databases where data is stored on disk. RAM is more limited than disk, so [cache invalidation](https://en.wikipedia.org/wiki/Cache_algorithms) algorithms such as [least recently used (LRU)](https://en.wikipedia.org/wiki/Cache_replacement_policies#Least_recently_used_\(LRU\)) can help invalidate 'cold' entries and keep 'hot' data in RAM.

Redis has the following additional features:

*   Persistence option
*   Built-in data structures such as sorted sets and lists

Generally, you should try to avoid file-based caching, as it makes cloning and auto-scaling more difficult.

Visit the following resources to learn more:

- [@opensource@Intro to Application Caching](https://github.com/donnemartin/system-design-primer#application-caching)

## Application Layer

# Application Layer

Separating out the web layer from the application layer (also known as platform layer) allows you to scale and configure both layers independently. Adding a new API results in adding application servers without necessarily adding additional web servers. The single responsibility principle advocates for small and autonomous services that work together. Small teams with small services can plan more aggressively for rapid growth.

![](https://i.imgur.com/F0cjurv.png)

Disadvantages
-------------

*   Adding an application layer with loosely coupled services requires a different approach from an architectural, operations, and process viewpoint (vs a monolithic system).
*   Microservices can add complexity in terms of deployments and operations.

Visit the following resources to learn more:

- [@article@Intro to architecting systems for scale](http://lethain.com/introduction-to-architecting-systems-for-scale/#platform_layer)

## Async Request Reply

# Asynchronous Request-Reply

Decouple backend processing from a frontend host, where backend processing needs to be asynchronous, but the frontend still needs a clear response.

Visit the following resources to learn more:

- [@article@Asynchronous Request-Reply pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/async-request-reply)

## Asynchronism

# Asynchronism

Asynchronous workflows help reduce request times for expensive operations that would otherwise be performed in-line. They can also help by doing time-consuming work in advance, such as periodic aggregation of data.

Visit the following resources to learn more:

- [@article@Patterns for microservices - Sync vs Async](https://medium.com/inspiredbrilliance/patterns-for-microservices-e57a2d71ff9e)
- [@article@Applying back pressure when overloaded](http://mechanical-sympathy.blogspot.com/2012/05/apply-back-pressure-when-overloaded.html)
- [@article@Little's law](https://en.wikipedia.org/wiki/Little%27s_law)
- [@article@What is the difference between a message queue and a task queue?](https://www.quora.com/What-is-the-difference-between-a-message-queue-and-a-task-queue-Why-would-a-task-queue-require-a-message-broker-like-RabbitMQ-Redis-Celery-or-IronMQ-to-function)
- [@video@It's all a numbers game](https://www.youtube.com/watch?v=1KRYH75wgy4)

## Availability In Numbers

# Availability in Numbers

Availability is often quantified by uptime (or downtime) as a percentage of time the service is available. Availability is generally measured in number of 9s--a service with 99.99% availability is described as having four 9s.

99.9% Availability - Three 9s:
------------------------------

    Duration           | Acceptable downtime
    -------------      | -------------
    Downtime per year  | 8h 41min 38s
    Downtime per month | 43m 28s
    Downtime per week  | 10m 4.8s
    Downtime per day   | 1m 26s
    

99.99% Availability - Four 9s
-----------------------------

    Duration           | Acceptable downtime
    -------------      | -------------
    Downtime per year  | 52min 9.8s
    Downtime per month | 4m 21s
    Downtime per week  | 1m 0.5s
    Downtime per day   | 8.6s
    

Availability in parallel vs in sequence
---------------------------------------

If a service consists of multiple components prone to failure, the service's overall availability depends on whether the components are in sequence or in parallel.

### In sequence

Overall availability decreases when two components with availability < 100% are in sequence:

    Availability (Total) = Availability (Foo) * Availability (Bar)
    

If both `Foo` and `Bar` each had 99.9% availability, their total availability in sequence would be 99.8%.

### In parallel

Overall availability increases when two components with availability < 100% are in parallel:

    Availability (Total) = 1 - (1 - Availability (Foo)) * (1 - Availability (Bar))
    

If both `Foo` and `Bar` each had 99.9% availability, their total availability in parallel would be 99.9999%.

Visit the following resources to learn more:

- [@article@Availability in System Design](https://www.enjoyalgorithms.com/blog/availability-system-design-concept/)
- [@article@Uptime calculator: How much downtime corresponds to 99.9 % uptime](https://uptime.is/)

## Availability Monitoring

# Availability Monitoring

A truly healthy system requires that the components and subsystems that compose the system are available. Availability monitoring is closely related to health monitoring. But whereas health monitoring provides an immediate view of the current health of the system, availability monitoring is concerned with tracking the availability of the system and its components to generate statistics about the uptime of the system.

Visit the following resources to learn more:

- [@article@Availability Monitoring](https://learn.microsoft.com/en-us/azure/architecture/best-practices/monitoring#availability-monitoring)
- [@feed@Explore top posts about Monitoring](https://app.daily.dev/tags/monitoring?ref=roadmapsh)

## Availability Patterns

# Availability Patterns

Availability patterns are established architectural approaches used to ensure a system remains operational and accessible to users, even in the face of failures or unexpected events. These patterns focus on minimizing downtime and maintaining a consistent level of service by incorporating redundancy, fault tolerance, and recovery mechanisms into the system's design. They provide a structured way to address potential points of failure and ensure business continuity.

Visit the following resources to learn more:

- [@article@High Availability in System Design – 15 Strategies for Always-On Systems](https://www.designgurus.io/blog/high-availability-system-design-basics)
- [@article@System Design: Availability Patterns](https://dev.to/decoders_lord/system-design-availability-patterns-104i)
- [@video@Design Patterns for High Availability: What gets you 99.999% uptime?](https://www.youtube.com/watch?v=LdvduBxZRLs)

## Availability Vs Consistency

# Availability vs Consistency

Availability refers to the ability of a system to provide its services to clients even in the presence of failures. This is often measured in terms of the percentage of time that the system is up and running, also known as its uptime.

Consistency, on the other hand, refers to the property that all clients see the same data at the same time. This is important for maintaining the integrity of the data stored in the system.

In distributed systems, it is often a trade-off between availability and consistency. Systems that prioritize high availability may sacrifice consistency, while systems that prioritize consistency may sacrifice availability. Different distributed systems use different approaches to balance the trade-off between availability and consistency, such as using replication or consensus algorithms.

Visit the following resources to learn more:

- [@opensource@CAP FAQ](https://github.com/henryr/cap-faq)
- [@article@CAP Theorem Revisited](https://robertgreiner.com/cap-theorem-revisited/)
- [@article@A plain english introduction to CAP Theorem](http://ksat.me/a-plain-english-introduction-to-cap-theorem)
- [@video@CAP Theorem](https://www.youtube.com/watch?v=_RbsFXWRZ10&t=1s)

## Availability

# Availability

Availability is measured as a percentage of uptime, and defines the proportion of time that a system is functional and working. Availability is affected by system errors, infrastructure problems, malicious attacks, and system load. Cloud applications typically provide users with a service level agreement (SLA), which means that applications must be designed and implemented to maximize availability.

Visit the following resources to learn more:

- [@article@Availability Patterns](https://learn.microsoft.com/en-us/azure/architecture/framework/resiliency/reliability-patterns#availability)

## Back Pressure

# Back Pressure

If queues start to grow significantly, the queue size can become larger than memory, resulting in cache misses, disk reads, and even slower performance. [Back pressure](http://mechanical-sympathy.blogspot.com/2012/05/apply-back-pressure-when-overloaded.html) can help by limiting the queue size, thereby maintaining a high throughput rate and good response times for jobs already in the queue. Once the queue fills up, clients get a server busy or HTTP 503 status code to try again later. Clients can retry the request at a later time, perhaps with [exponential backoff](https://en.wikipedia.org/wiki/Exponential_backoff).

## Backends For Frontend

# Backends for Frontend

Create separate backend services to be consumed by specific frontend applications or interfaces. This pattern is useful when you want to avoid customizing a single backend for multiple interfaces. This pattern was first described by Sam Newman.

Visit the following resources to learn more:

- [@article@Backends for Frontends pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/backends-for-frontends)
- [@feed@Explore top posts about Frontend Development](https://app.daily.dev/tags/frontend?ref=roadmapsh)

## Background Jobs

# Background Jobs

Background jobs in system design refer to tasks that are executed in the background, independently of the main execution flow of the system. These tasks are typically initiated by the system itself, rather than by a user or another external agent.

Background jobs can be used for a variety of purposes, such as:

*   Performing maintenance tasks: such as cleaning up old data, generating reports, or backing up the database.
*   Processing large volumes of data: such as data import, data export, or data transformation.
*   Sending notifications or messages: such as sending email notifications or push notifications to users.
*   Performing long-running computations: such as machine learning or data analysis.

Visit the following resources to learn more:

- [@article@Background Jobs - Best Practices](https://learn.microsoft.com/en-us/azure/architecture/best-practices/background-jobs)

## Bulkhead

# Bulkhead

The Bulkhead pattern is a type of application design that is tolerant of failure. In a bulkhead architecture, elements of an application are isolated into pools so that if one fails, the others will continue to function. It's named after the sectioned partitions (bulkheads) of a ship's hull. If the hull of a ship is compromised, only the damaged section fills with water, which prevents the ship from sinking.

Visit the following resources to learn more:

- [@article@Bulkhead pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/bulkhead)
- [@article@Get started with Bulkhead](https://dzone.com/articles/resilient-microservices-pattern-bulkhead-pattern)

## Bulkhead

# Bulkhead

The Bulkhead pattern is a type of application design that is tolerant of failure. In a bulkhead architecture, elements of an application are isolated into pools so that if one fails, the others will continue to function. It's named after the sectioned partitions (bulkheads) of a ship's hull. If the hull of a ship is compromised, only the damaged section fills with water, which prevents the ship from sinking.

Visit the following resources to learn more:

- [@article@Bulkhead pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/bulkhead)
- [@article@Get started with Bulkhead](https://dzone.com/articles/resilient-microservices-pattern-bulkhead-pattern)

## Busy Database

# Busy Database

A busy database in system design refers to a database that is handling a high volume of requests or transactions, this can occur when a system is experiencing high traffic or when a database is not properly optimized for the workload it is handling. This can lead to Performance degradation, Increased resource utilization, Deadlocks and contention, Data inconsistencies. To address a busy database, a number of approaches can be taken such as Scaling out, Optimizing the schema, Caching, and Indexing.

Visit the following resources to learn more:

- [@article@Busy Database antipattern](https://learn.microsoft.com/en-us/azure/architecture/antipatterns/busy-database/)
- [@feed@Explore top posts about Database](https://app.daily.dev/tags/database?ref=roadmapsh)

## Busy Frontend

# Busy Frontend

A busy frontend happens when the user-facing part of the system — such as the web servers, CDN, or browser — is handling more work than it can efficiently manage. This can lead to slow page loads, delayed responses, or timeouts. Common causes include too many concurrent users, large static assets, heavy client-side rendering, or missing caching layers.

To improve responsiveness, you can use CDNs to cache static files, optimize and lazy-load scripts, balance requests across multiple servers, and reduce unnecessary API calls. The goal is to make sure the frontend remains fast and responsive even under heavy traffic.

Visit the following resources to learn more:

- [@article@Busy Front End antipattern](https://learn.microsoft.com/en-us/azure/architecture/antipatterns/busy-front-end/)
- [@feed@Explore top posts about Frontend Development](https://app.daily.dev/tags/frontend?ref=roadmapsh)

## Cache Aside

# Cache Aside

Load data on demand into a cache from a data store. This can improve performance and also helps to maintain consistency between data held in the cache and data in the underlying data store.

Visit the following resources to learn more:

- [@article@Cache-Aside pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/cache-aside)

## Cache Aside

# Cache-aside

The application is responsible for reading and writing from storage. The cache does not interact with storage directly. The application does the following:

*   Look for entry in cache, resulting in a cache miss
    
*   Load entry from the database
    
*   Add entry to cache
    
*   Return entry
    
      def get_user(self, user_id):
        user = cache.get("user.{0}", user_id)
        if user is None:
            user = db.query("SELECT * FROM users WHERE user_id = {0}", user_id)
        if user is not None:
            key = "user.{0}".format(user_id)
            cache.set(key, json.dumps(user))
        return user
    
[Memcached](https://memcached.org/) is generally used in this manner. Subsequent reads of data added to cache are fast. Cache-aside is also referred to as lazy loading. Only the requested data is cached, which avoids filling up the cache with data that isn't requested.

![Cache Aside](https://i.imgur.com/Ujf0awN.png)

Visit the following resources to learn more:

- [@article@From cache to in-memory data grid](https://www.slideshare.net/tmatyashovsky/from-cache-to-in-memory-data-grid-introduction-to-hazelcast)

## Caching

# Caching

Caching is the process of storing frequently accessed data in a temporary storage location, called a cache, in order to quickly retrieve it without the need to query the original data source. This can improve the performance of an application by reducing the number of times a data source must be accessed.

There are several caching strategies:

*   Refresh Ahead
*   Write-Behind
*   Write-through
*   Cache Aside

Also, you can have the cache in several places, examples include:

*   Client Caching
*   CDN Caching
*   Web Server Caching
*   Database Caching
*   Application Caching

Visit the following resources to learn more:

- [@article@Caching Strategies](https://medium.com/@mmoshikoo/cache-strategies-996e91c80303)

## Cap Theorem

# CAP Theorem

According to CAP theorem, in a distributed system, you can only support two of the following guarantees:

*   **Consistency** - Every read receives the most recent write or an error
*   **Availability** - Every request receives a response, without guarantee that it contains the most recent version of the information
*   **Partition Tolerance** - The system continues to operate despite arbitrary partitioning due to network failures

Networks aren't reliable, so you'll need to support partition tolerance. You'll need to make a software tradeoff between consistency and availability.

CP - consistency and partition tolerance
----------------------------------------

Waiting for a response from the partitioned node might result in a timeout error. CP is a good choice if your business needs require atomic reads and writes.

AP - availability and partition tolerance
-----------------------------------------

Responses return the most readily available version of the data available on any node, which might not be the latest. Writes might take some time to propagate when the partition is resolved.

AP is a good choice if the business needs to allow for [eventual consistency](https://github.com/donnemartin/system-design-primer#eventual-consistency) or when the system needs to continue working despite external errors.

Visit the following resources to learn more:

- [@opensource@CAP FAQ](https://github.com/henryr/cap-faq)
- [@article@CAP theorem revisited](http://robertgreiner.com/2014/08/cap-theorem-revisited/)
- [@article@A plain english introduction to CAP theorem](http://ksat.me/a-plain-english-introduction-to-cap-theorem)
- [@video@The CAP theorem](https://www.youtube.com/watch?v=k-Yaq8AHlFA)

## Cdn Caching

# CDN Caching

A Content Delivery Network (CDN) is a distributed network of servers that are strategically placed in various locations around the world. The main purpose of a CDN is to serve content to end-users with high availability and high performance by caching frequently accessed content on servers that are closer to the end-users.

When a user requests content from a website that is using a CDN, the CDN will first check if the requested content is available in the cache of a nearby server. If the content is found in the cache, it is served to the user from the nearby server. If the content is not found in the cache, it is requested from the origin server (the original source of the content) and then cached on the nearby server for future requests.

CDN caching can significantly improve the performance and availability of a website by reducing the distance that data needs to travel, reducing the load on the origin server, and allowing for faster delivery of content to end-users.

## Chatty Io

# Chatty I/O

The cumulative effect of a large number of I/O requests can have a significant impact on performance and responsiveness.

Network calls and other I/O operations are inherently slow compared to compute tasks. Each I/O request typically has significant overhead, and the cumulative effect of numerous I/O operations can slow down the system. Here are some common causes of chatty I/O.

*   Reading and writing individual records to a database as distinct requests
*   Implementing a single logical operation as a series of HTTP requests
*   Reading and writing to a file on disk

Visit the following resources to learn more:

- [@article@Chatty I/O antipattern](https://learn.microsoft.com/en-us/azure/architecture/antipatterns/chatty-io/)

## Choreography

# Choreography

Have each component of the system participate in the decision-making process about the workflow of a business transaction, instead of relying on a central point of control.

Visit the following resources to learn more:

- [@article@Choreography pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/choreography)

## Circuit Breaker

# Circuit Breaker

Handle faults that might take a variable amount of time to recover from, when connecting to a remote service or resource. This can improve the stability and resiliency of an application.

Visit the following resources to learn more:

- [@article@Circuit breaker design pattern](https://en.wikipedia.org/wiki/Circuit_breaker_design_pattern)
- [@article@Overview of Circuit Breaker](https://medium.com/geekculture/design-patterns-for-microservices-circuit-breaker-pattern-276249ffab33)

## Circuit Breaker

# Circuit Breaker

Handle faults that might take a variable amount of time to recover from, when connecting to a remote service or resource. This can improve the stability and resiliency of an application.

Visit the following resources to learn more:

- [@article@Circuit breaker design pattern](https://en.wikipedia.org/wiki/Circuit_breaker_design_pattern)
- [@article@Overview of Circuit Breaker](https://medium.com/geekculture/design-patterns-for-microservices-circuit-breaker-pattern-276249ffab33)

## Claim Check

# Claim Check

Split a large message into a claim check and a payload. Send the claim check to the messaging platform and store the payload to an external service. This pattern allows large messages to be processed, while protecting the message bus and the client from being overwhelmed or slowed down. This pattern also helps to reduce costs, as storage is usually cheaper than resource units used by the messaging platform.

Visit the following resources to learn more:

- [@article@Claim Check - Cloud Design patterns](https://learn.microsoft.com/en-us/azure/architecture/patterns/claim-check)

## Client Caching

# Client Caching

Client-side caching refers to the practice of storing frequently accessed data on the client's device rather than the server. This type of caching can help improve the performance of an application by reducing the number of times the client needs to request data from the server.

One common example of client-side caching is web browsers caching frequently accessed web pages and resources. When a user visits a web page, the browser stores a copy of the page and its resources (such as images, stylesheets, and scripts) in the browser's cache. If the user visits the same page again, the browser can retrieve the cached version of the page and its resources instead of requesting them from the server, which can reduce the load time of the page.

Another example of client-side caching is application-level caching. Some applications, such as mobile apps, can cache data on the client's device to improve performance and reduce the amount of data that needs to be transferred over the network.

Client side caching has some advantages like reducing server load, faster page load times, and reducing network traffic. However, it also has some drawbacks like the potential for stale data if the client-side cache is not properly managed, or consuming memory or disk space on the client's device.

Visit the following resources to learn more:

- [@article@HTTP Caching](https://developer.mozilla.org/en-US/docs/Web/HTTP/Caching)

## Cloud Design Patterns

# Cloud Design Patterns

Cloud design patterns are solutions to common problems that arise when building systems that run on a cloud platform. These patterns provide a way to design and implement systems that can take advantage of the unique characteristics of the cloud, such as scalability, elasticity, and pay-per-use pricing. Some common cloud design patterns include Scalability, Elasticity, Fault Tolerance, Microservices, Serverless, Data Management, Front-end and Back-end separation and Hybrid.

Visit the following resources to learn more:

- [@article@Cloud Design Patterns](https://learn.microsoft.com/en-us/azure/architecture/patterns/)
- [@feed@Explore top posts about Cloud](https://app.daily.dev/tags/cloud?ref=roadmapsh)

## Communication

# Communication

Network protocols are a key part of systems today, as no system can exist in isolation - they all need to communicate with each other. You should learn about the networking protocols such as HTTP, TCP, UDP. Also, learn about the architectural styles such as RPC, REST, GraphQL and gRPC.

## Compensating Transaction

# Compensating Transaction

Undo the work performed by a series of steps, which together define an eventually consistent operation, if one or more of the steps fail. Operations that follow the eventual consistency model are commonly found in cloud-hosted applications that implement complex business processes and workflows.

Visit the following resources to learn more:

- [@article@Compensating Transaction pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/compensating-transaction)
- [@article@Intro to Compensation Transaction](https://en.wikipedia.org/wiki/Compensating_transaction)

## Competing Consumers

# Competing Consumers

Enable multiple concurrent consumers to process messages received on the same messaging channel. With multiple concurrent consumers, a system can process multiple messages concurrently to optimize throughput, to improve scalability and availability, and to balance the workload.

Visit the following resources to learn more:

- [@article@Competing Consumers pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/competing-consumers)

## Compute Resource Consolidation

# Compute Resource Consolidation

Consolidate multiple tasks or operations into a single computational unit. This can increase compute resource utilization, and reduce the costs and management overhead associated with performing compute processing in cloud-hosted applications.

Visit the following resources to learn more:

- [@article@Compute Resource Consolidation pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/compute-resource-consolidation)

## Consistency Patterns

# Consistency Patterns

Consistency patterns refer to the ways in which data is stored and managed in a distributed system, and how that data is made available to users and applications. There are three main types of consistency patterns:

*   Strong consistency
*   Weak consistency
*   Eventual Consistency

Each of these patterns has its own advantages and disadvantages, and the choice of which pattern to use will depend on the specific requirements of the application or system.

Visit the following resources to learn more:

- [@article@Consistency Patterns in Distributed Systems](https://cs.fyi/guide/consistency-patterns-week-strong-eventual/)

## Content Delivery Networks

# Content Delivery Networks

A content delivery network (CDN) is a globally distributed network of proxy servers, serving content from locations closer to the user. Generally, static files such as HTML/CSS/JS, photos, and videos are served from CDN, although some CDNs such as Amazon's CloudFront support dynamic content. The site's DNS resolution will tell clients which server to contact.

Serving content from CDNs can significantly improve performance in two ways:

*   Users receive content from data centers close to them
*   Your servers do not have to serve requests that the CDN fulfills

Visit the following resources to learn more:

- [@opensource@Introduction to CDNs](https://github.com/donnemartin/system-design-primer#content-delivery-network)
- [@article@The Differences Between Push And Pull CDNs](http://www.travelblogadvice.com/technical/the-differences-between-push-and-pull-cdns/)
- [@article@Brief about Content delivery network](https://en.wikipedia.org/wiki/Content_delivery_network)

## Cqrs

# CQRS

CQRS stands for Command and Query Responsibility Segregation, a pattern that separates read and update operations for a data store. Implementing CQRS in your application can maximize its performance, scalability, and security. The flexibility created by migrating to CQRS allows a system to better evolve over time and prevents update commands from causing merge conflicts at the domain level.

Visit the following resources to learn more:

- [@article@CQRS pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/cqrs)

## Cqrs

# CQRS

CQRS stands for Command and Query Responsibility Segregation, a pattern that separates read and update operations for a data store. Implementing CQRS in your application can maximize its performance, scalability, and security. The flexibility created by migrating to CQRS allows a system to better evolve over time and prevents update commands from causing merge conflicts at the domain level.

Visit the following resources to learn more:

- [@article@CQRS pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/cqrs)

## Data Management

# Data Management

Data management is the key element of cloud applications, and influences most of the quality attributes. Data is typically hosted in different locations and across multiple servers for reasons such as performance, scalability or availability, and this can present a range of challenges. For example, data consistency must be maintained, and data will typically need to be synchronized across different locations.

Visit the following resources to learn more:

- [@article@Data management patterns](https://learn.microsoft.com/en-us/azure/architecture/patterns/category/data-management)
- [@feed@Explore top posts about Data Management](https://app.daily.dev/tags/data-management?ref=roadmapsh)

## Database Caching

# Database Caching

Database caching involves storing frequently accessed data from a database in a temporary storage location (the cache) to reduce the load on the database and improve application performance. Instead of repeatedly querying the database for the same data, the application first checks the cache. If the data is present (a cache hit), it's retrieved from the cache, which is much faster than a database query. If the data is not in the cache (a cache miss), the application queries the database, retrieves the data, stores it in the cache for future use, and then returns it to the application.

Visit the following resources to learn more:

- [@article@Database Caching](https://aws.amazon.com/caching/database-caching/)
- [@article@Introduction to database caching](https://www.prisma.io/dataguide/managing-databases/introduction-database-caching)
- [@article@Database Caching Strategies](https://medium.com/@sesmiat/database-caching-strategies-f5e40c3c9b74)

## Databases

# Databases

Picking the right database for a system is an important decision, as it can have a significant impact on the performance, scalability, and overall success of the system. Some of the key reasons why it's important to pick the right database include:

*   Performance: Different databases have different performance characteristics, and choosing the wrong one can lead to poor performance and slow response times.
*   Scalability: As the system grows and the volume of data increases, the database needs to be able to scale accordingly. Some databases are better suited for handling large amounts of data than others.
*   Data Modeling: Different databases have different data modeling capabilities and choosing the right one can help to keep the data consistent and organized.
*   Data Integrity: Different databases have different capabilities for maintaining data integrity, such as enforcing constraints, and can have different levels of data security.
*   Support and maintenance: Some databases have more active communities and better documentation, making it easier to find help and resources.

Visit the following resources to learn more:

- [@video@Scaling up to your first 10 million users](https://www.youtube.com/watch?v=kKjm4ehYiMs)
- [@feed@Explore top posts about Backend Development](https://app.daily.dev/tags/backend?ref=roadmapsh)

## Denormalization

# Denormalization

Denormalization attempts to improve read performance at the expense of some write performance. Redundant copies of the data are written in multiple tables to avoid expensive joins. Some RDBMS such as PostgreSQL and Oracle support materialized views which handle the work of storing redundant information and keeping redundant copies consistent.

Once data becomes distributed with techniques such as federation and sharding, managing joins across data centers further increases complexity. Denormalization might circumvent the need for such complex joins.

Visit the following resources to learn more:

- [@article@Denormalization](https://en.wikipedia.org/wiki/Denormalization)

## Deployment Stamps

# Deployment Stamps

The deployment stamp pattern involves provisioning, managing, and monitoring a heterogeneous group of resources to host and operate multiple workloads or tenants. Each individual copy is called a stamp, or sometimes a service unit, scale unit, or cell. In a multi-tenant environment, every stamp or scale unit can serve a predefined number of tenants. Multiple stamps can be deployed to scale the solution almost linearly and serve an increasing number of tenants. This approach can improve the scalability of your solution, allow you to deploy instances across multiple regions, and separate your customer data.

Visit the following resources to learn more:

- [@article@Deployment Stamps pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/deployment-stamp)
- [@article@Deployment Stamps 101](https://blog.devgenius.io/deployment-stamps-101-7c04a6f704a2)
- [@feed@Explore top posts about CI/CD](https://app.daily.dev/tags/cicd?ref=roadmapsh)

## Deployment Stamps

# Deployment Stamps

The deployment stamp pattern involves provisioning, managing, and monitoring a heterogeneous group of resources to host and operate multiple workloads or tenants. Each individual copy is called a stamp, or sometimes a service unit, scale unit, or cell. In a multi-tenant environment, every stamp or scale unit can serve a predefined number of tenants. Multiple stamps can be deployed to scale the solution almost linearly and serve an increasing number of tenants. This approach can improve the scalability of your solution, allow you to deploy instances across multiple regions, and separate your customer data.

Visit the following resources to learn more:

- [@article@Deployment Stamps pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/deployment-stamp)
- [@article@Deployment Stamps 101](https://blog.devgenius.io/deployment-stamps-101-7c04a6f704a2)
- [@feed@Explore top posts about CI/CD](https://app.daily.dev/tags/cicd?ref=roadmapsh)

## Design  Implementation

# Design and Implementation

Good design encompasses factors such as consistency and coherence in component design and deployment, maintainability to simplify administration and development, and reusability to allow components and subsystems to be used in other applications and in other scenarios. Decisions made during the design and implementation phase have a huge impact on the quality and the total cost of ownership of cloud hosted applications and services.

Visit the following resources to learn more:

- [@article@Design and implementation patterns](https://learn.microsoft.com/en-us/azure/architecture/patterns/category/design-implementation)

## Document Store

# Document Store

A document store is centered around documents (XML, JSON, binary, etc), where a document stores all information for a given object. Document stores provide APIs or a query language to query based on the internal structure of the document itself. Note, many key-value stores include features for working with a value's metadata, blurring the lines between these two storage types.

Based on the underlying implementation, documents are organized by collections, tags, metadata, or directories. Although documents can be organized or grouped together, documents may have fields that are completely different from each other.

Visit the following resources to learn more:

- [@article@Document-oriented database](https://en.wikipedia.org/wiki/Document-oriented_database)

## Domain Name System

# Domain Name System

A Domain Name System (DNS) translates a domain name such as [www.example.com](http://www.example.com) to an IP address.

DNS is hierarchical, with a few authoritative servers at the top level. Your router or ISP provides information about which DNS server(s) to contact when doing a lookup. Lower level DNS servers cache mappings, which could become stale due to DNS propagation delays. DNS results can also be cached by your browser or OS for a certain period of time, determined by the time to live (TTL).

*   NS record (name server) - Specifies the DNS servers for your domain/subdomain.
*   MX record (mail exchange) - Specifies the mail servers for accepting messages.
*   A record (address) - Points a name to an IP address.
*   CNAME (canonical) - Points a name to another name or CNAME ([example.com](http://example.com) to [www.example.com](http://www.example.com)) or to an A record.

Services such as [CloudFlare](https://www.cloudflare.com/dns/) and [Route53](https://aws.amazon.com/route53/) provide managed DNS services. Some DNS services can route traffic through various methods:

    *   Prevent traffic from going to servers under maintenance
    *   Balance between varying cluster sizes
    *   A/B testing

Visit the following resources to learn more:

- [@opensource@Getting started with Domain Name System](https://github.com/donnemartin/system-design-primer#domain-name-system)
- [@article@What is DNS?](https://www.cloudflare.com/learning/dns/what-is-dns/)
- [@article@Latency Based](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html#routing-policy-latency)
- [@article@Geolocation Based](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html#routing-policy-geo)
- [@article@Weighted Round Robin](https://www.jscape.com/blog/load-balancing-algorithms)

## Event Driven

# Event Driven

Event-driven invocation uses a trigger to start the background task. Examples of using event-driven triggers include:

*   The UI or another job places a message in a queue. The message contains data about an action that has taken place, such as the user placing an order. The background task listens on this queue and detects the arrival of a new message. It reads the message and uses the data in it as the input to the background job. This pattern is known as asynchronous message-based communication.
*   The UI or another job saves or updates a value in storage. The background task monitors the storage and detects changes. It reads the data and uses it as the input to the background job.
*   The UI or another job makes a request to an endpoint, such as an HTTPS URI, or an API that is exposed as a web service. It passes the data that is required to complete the background task as part of the request. The endpoint or web service invokes the background task, which uses the data as its input.

Visit the following resources to learn more:

- [@article@Background Jobs - Event Driven Triggers](https://learn.microsoft.com/en-us/azure/architecture/best-practices/background-jobs#event-driven-triggers)

## Event Sourcing

# Event Sourcing

Instead of storing just the current state of the data in a domain, use an append-only store to record the full series of actions taken on that data. The store acts as the system of record and can be used to materialize the domain objects. This can simplify tasks in complex domains, by avoiding the need to synchronize the data model and the business domain, while improving performance, scalability, and responsiveness. It can also provide consistency for transactional data, and maintain full audit trails and history that can enable compensating actions.

Visit the following resources to learn more:

- [@article@Event Sourcing pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/event-sourcing)
- [@feed@Explore top posts about Architecture](https://app.daily.dev/tags/architecture?ref=roadmapsh)

## Eventual Consistency

# Eventual Consistency

Eventual consistency is a form of Weak Consistency. After an update is made to the data, it will be eventually visible to any subsequent read operations. The data is replicated in an asynchronous manner, ensuring that all copies of the data are eventually updated.

Visit the following resources to learn more:

- [@article@Consistency Patterns in Distributed Systems](https://cs.fyi/guide/consistency-patterns-week-strong-eventual/)

## External Config Store

# External Configuration Store

Move configuration information out of the application deployment package to a centralized location. This can provide opportunities for easier management and control of configuration data, and for sharing configuration data across applications and application instances.

Visit the following resources to learn more:

- [@article@External Configuration Store pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/external-configuration-store)

## Extraneous Fetching

# Extraneous Fetching

Extraneous fetching in system design refers to the practice of retrieving more data than is needed for a specific task or operation. This can occur when a system is not optimized for the specific workload or when the system is not properly designed to handle the data requirements.

Extraneous fetching can lead to a number of issues, such as:

*   Performance degradation
*   Increased resource utilization
*   Increased network traffic
*   Poor user experience

Visit the following resources to learn more:

- [@article@Extraneous Fetching antipattern](https://learn.microsoft.com/en-us/azure/architecture/antipatterns/extraneous-fetching/)

## Fail Over

# Fail-Over

Failover is an availability pattern that is used to ensure that a system can continue to function in the event of a failure. It involves having a backup component or system that can take over in the event of a failure.

In a failover system, there is a primary component that is responsible for handling requests, and a secondary (or backup) component that is on standby. The primary component is monitored for failures, and if it fails, the secondary component is activated to take over its duties. This allows the system to continue functioning with minimal disruption.

Failover can be implemented in various ways, such as active-passive, active-active, and hot-standby.

Active-passive
--------------

With active-passive fail-over, heartbeats are sent between the active and the passive server on standby. If the heartbeat is interrupted, the passive server takes over the active's IP address and resumes service.

The length of downtime is determined by whether the passive server is already running in 'hot' standby or whether it needs to start up from 'cold' standby. Only the active server handles traffic.

Active-passive failover can also be referred to as master-slave failover.

Active-active
-------------

In active-active, both servers are managing traffic, spreading the load between them.

If the servers are public-facing, the DNS would need to know about the public IPs of both servers. If the servers are internal-facing, application logic would need to know about both servers.

Active-active failover can also be referred to as master-master failover.

Disadvantages of Failover
-------------------------

*   Fail-over adds more hardware and additional complexity.
*   There is a potential for loss of data if the active system fails before any newly written data can be replicated to the passive.

Visit the following resources to learn more:

- [@opensource@Fail Over](https://github.com/donnemartin/system-design-primer?tab=readme-ov-file#fail-over)
- [@article@Active-Passive vs. Active-Active Failover](https://www.serverion.com/uncategorized/active-passive-vs-active-active-failover/)

## Federated Identity

# Federated Identity pattern

Delegate authentication to an external identity provider. This can simplify development, minimize the requirement for user administration, and improve the user experience of the application.

Visit the following resources to learn more:

- [@article@Federated Identity pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/federated-identity)

## Federation

# Federation

Federation (or functional partitioning) splits up databases by function. For example, instead of a single, monolithic database, you could have three databases: forums, users, and products, resulting in less read and write traffic to each database and therefore less replication lag. Smaller databases result in more data that can fit in memory, which in turn results in more cache hits due to improved cache locality. With no single central master serializing writes you can write in parallel, increasing throughput.

## Gatekeeper

# Gatekeeper

Protect applications and services using a dedicated host instance that acts as a broker between clients and the application or service, validates and sanitizes requests, and passes requests and data between them. This can provide an additional layer of security and limit the system's attack surface.

Visit the following resources to learn more:

- [@article@Gatekeeper pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/gatekeeper)

## Gateway Aggregation

# Gateway Aggregation

Use a gateway to aggregate multiple individual requests into a single request. This pattern is useful when a client must make multiple calls to different backend systems to perform an operation.

Visit the following resources to learn more:

- [@article@Gateway Aggregation pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/gateway-aggregation)

## Gateway Offloading

# Gateway Offloading

Offload shared or specialized service functionality to a gateway proxy. This pattern can simplify application development by moving shared service functionality, such as the use of SSL certificates, from other parts of the application into the gateway.

Visit the following resources to learn more:

- [@article@Gateway Offloading pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/gateway-offloading)

## Gateway Routing

# Gateway Routing

Route requests to multiple services or multiple service instances using a single endpoint. The pattern is useful when you want to:

*   Expose multiple services on a single endpoint and route to the appropriate service based on the request
*   Expose multiple instances of the same service on a single endpoint for load balancing or availability purposes
*   Expose differing versions of the same service on a single endpoint and route traffic across the different versions

Visit the following resources to learn more:

- [@article@Gateway Routing pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/gateway-routing)

## Geodes

# Geodes

The Geode pattern involves deploying a collection of backend services into a set of geographical nodes, each of which can service any request for any client in any region. This pattern allows serving requests in an active-active style, improving latency and increasing availability by distributing request processing around the globe.

Visit the following resources to learn more:

- [@article@Geode pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/geodes)

## Geodes

# Geodes

The Geode pattern involves deploying a collection of backend services into a set of geographical nodes, each of which can service any request for any client in any region. This pattern allows serving requests in an active-active style, improving latency and increasing availability by distributing request processing around the globe.

Visit the following resources to learn more:

- [@article@Geode pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/geodes)
- [@article@Geode Formation, Types & Appearance | What is a Geode?](https://study.com/academy/lesson/geode-formation-types-appearance.html)

## Graph Databases

# Graph Databases

In a graph database, each node is a record and each arc is a relationship between two nodes. Graph databases are optimized to represent complex relationships with many foreign keys or many-to-many relationships.

Graphs databases offer high performance for data models with complex relationships, such as a social network. They are relatively new and are not yet widely-used; it might be more difficult to find development tools and resources. Many graphs can only be accessed with REST APIs.

Visit the following resources to learn more:

- [@article@Graph database](https://en.wikipedia.org/wiki/Graph_database)
- [@video@Introduction to NoSQL](https://www.youtube.com/watch?v=qI_g07C_Q5I)
- [@feed@Explore top posts about Backend Development](https://app.daily.dev/tags/backend?ref=roadmapsh)

## Graphql

# GraphQL

GraphQL is a query language and runtime for building APIs. It allows clients to define the structure of the data they need and the server will return exactly that. This is in contrast to traditional REST APIs, where the server exposes a fixed set of endpoints and the client must work with the data as it is returned.

Visit the following resources to learn more:

- [@article@GraphQL Server](https://www.howtographql.com/basics/3-big-picture/)
- [@article@What is GraphQL?](https://www.redhat.com/en/topics/api/what-is-graphql)
- [@feed@Explore top posts about GraphQL](https://app.daily.dev/tags/graphql?ref=roadmapsh)

## Grpc

# gRPC

gRPC is a high-performance, open-source framework for building remote procedure call (RPC) APIs. It is based on the Protocol Buffers data serialization format and supports a variety of programming languages, including C#, Java, and Python.

Visit the following resources to learn more:

- [@article@What Is gRPC?](https://www.wallarm.com/what/the-concept-of-grpc)
- [@feed@Explore top posts about gRPC](https://app.daily.dev/tags/grpc?ref=roadmapsh)

## Health Endpoint Monitoring

# Health Endpoint Monitoring

Implement functional checks in an application that external tools can access through exposed endpoints at regular intervals. This can help to verify that applications and services are performing correctly.

Visit the following resources to learn more:

- [@article@Health Endpoint Monitoring pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/health-endpoint-monitoring)
- [@article@Explaining the health endpoint monitoring pattern](https://www.oreilly.com/library/view/java-ee-8/9781788830621/5012c01e-90ca-4809-a210-d3736574f5b3.xhtml)
- [@feed@Explore top posts about Monitoring](https://app.daily.dev/tags/monitoring?ref=roadmapsh)

## Health Endpoint Monitoring

# Health Endpoint Monitoring

Implement functional checks in an application that external tools can access through exposed endpoints at regular intervals. This can help to verify that applications and services are performing correctly.

Visit the following resources to learn more:

- [@article@Health Endpoint Monitoring pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/health-endpoint-monitoring)
- [@article@Explaining the health endpoint monitoring pattern](https://www.oreilly.com/library/view/java-ee-8/9781788830621/5012c01e-90ca-4809-a210-d3736574f5b3.xhtml)
- [@feed@Explore top posts about Monitoring](https://app.daily.dev/tags/monitoring?ref=roadmapsh)

## Health Endpoint Monitoring

# Health Endpoint Monitoring

Implement functional checks in an application that external tools can access through exposed endpoints at regular intervals. This can help to verify that applications and services are performing correctly.

Visit the following resources to learn more:

- [@article@Health Endpoint Monitoring pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/health-endpoint-monitoring)
- [@article@Explaining the health endpoint monitoring pattern](https://www.oreilly.com/library/view/java-ee-8/9781788830621/5012c01e-90ca-4809-a210-d3736574f5b3.xhtml)
- [@feed@Explore top posts about Monitoring](https://app.daily.dev/tags/monitoring?ref=roadmapsh)

## Health Monitoring

# Health Monitoring

A system is healthy if it is running and capable of processing requests. The purpose of health monitoring is to generate a snapshot of the current health of the system so that you can verify that all components of the system are functioning as expected.

Visit the following resources to learn more:

- [@article@Health Monitoring of a System](https://learn.microsoft.com/en-us/azure/architecture/best-practices/monitoring#health-monitoring)
- [@feed@Explore top posts about Monitoring](https://app.daily.dev/tags/monitoring?ref=roadmapsh)

## High Availability

# High availability

Azure infrastructure is composed of geographies, regions, and Availability Zones, which limit the blast radius of a failure and therefore limit potential impact to customer applications and data. The Azure Availability Zones construct was developed to provide a software and networking solution to protect against datacenter failures and to provide increased high availability (HA) to our customers. With HA architecture there is a balance between high resilience, low latency, and cost.

Visit the following resources to learn more:

- [@article@High availability Patterns](https://learn.microsoft.com/en-us/azure/architecture/framework/resiliency/reliability-patterns#high-availability)

## Horizontal Scaling

# Horizontal Scaling

Load balancers can also help with horizontal scaling, improving performance and availability. Scaling out using commodity machines is more cost efficient and results in higher availability than scaling up a single server on more expensive hardware, called Vertical Scaling. It is also easier to hire for talent working on commodity hardware than it is for specialized enterprise systems.

Disadvantages of horizontal scaling
-----------------------------------

*   Scaling horizontally introduces complexity and involves cloning servers
    *   Servers should be stateless: they should not contain any user-related data like sessions or profile pictures
    *   Sessions can be stored in a centralized data store such as a database (SQL, NoSQL) or a persistent cache (Redis, Memcached)
*   Downstream servers such as caches and databases need to handle more simultaneous connections as upstream servers scale out.

## How To Approach System Design

# How To: System Design?

There are several steps that can be taken when approaching a system design:

*   **Understand the problem**: Gather information about the problem you are trying to solve and the requirements of the system. Identify the users and their needs, as well as any constraints or limitations of the system.
*   **Identify the scope of the system:** Define the boundaries of the system, including what the system will do and what it will not do.
*   **Research and analyze existing systems:** Look at similar systems that have been built in the past and identify what worked well and what didn't. Use this information to inform your design decisions.
*   **Create a high-level design:** Outline the main components of the system and how they will interact with each other. This can include a rough diagram of the system's architecture, or a flowchart outlining the process the system will follow.
*   **Refine the design:** As you work on the details of the design, iterate and refine it until you have a complete and detailed design that meets all the requirements.
*   **Document the design:** Create detailed documentation of your design for future reference and maintenance.
*   **Continuously monitor and improve the system:** The system design is not a one-time process, it needs to be continuously monitored and improved to meet the changing requirements.

Visit the following resources to learn more:

- [@opensource@How to approach System Design?](https://github.com/donnemartin/system-design-primer#how-to-approach-a-system-design-interview-question)
- [@article@What are system design questions?](https://www.hiredintech.com/system-design)
- [@article@My System Design Template](https://leetcode.com/discuss/career/229177/My-System-Design-Template)
- [@video@Intro to Architecture and Systems Design Interviews](https://www.youtube.com/watch?v=ZgdS0EUmn70)

## Http

# HTTP

HTTP is a method for encoding and transporting data between a client and a server. It is a request/response protocol: clients issue requests and servers issue responses with relevant content and completion status info about the request. HTTP is self-contained, allowing requests and responses to flow through many intermediate routers and servers that perform load balancing, caching, encryption, and compression.

A basic HTTP request consists of a verb (method) and a resource (endpoint). Below are common HTTP verbs:

    Verb   | Description                   | Idempotent* | Safe | Cacheable                               |
    -------|-------------------------------|-------------|------|-----------------------------------------|
    GET    | Reads a resource              | Yes         | Yes  | Yes                                     |
    POST   | Creates a resource or trigger | No          | No   | Yes if response contains freshness info |
    PUT    | Creates or replace a resource | Yes         | No   | No                                      |
    PATCH  | Partially updates a resource  | No          | No   | Yes if response contains freshness info |
    DELETE | Deletes a resource            | Yes         | No   | No                                      |

Visit the following resources to learn more:

- [@article@Everything you need to know about HTTP](https://cs.fyi/guide/http-in-depth)
- [@article@What Is HTTP?](https://www.nginx.com/resources/glossary/http/)
- [@article@What is the difference between HTTP protocol and TCP protocol?](https://www.quora.com/What-is-the-difference-between-HTTP-protocol-and-TCP-protocol)

## Idempotent Operations

# Idempotent Operations

Idempotent operations are operations that can be applied multiple times without changing the result beyond the initial application. In other words, if an operation is idempotent, it will have the same effect whether it is executed once or multiple times.

It is also important to understand the benefits of [idempotent](https://en.wikipedia.org/wiki/Idempotence#Computer_science_meaning) operations, especially when using message or task queues that do not guarantee _exactly once_ processing. Many queueing systems guarantee _at least once_ message delivery or processing. These systems are not completely synchronized, for instance, across geographic regions, which simplifies some aspects of their implementation or design. Designing the operations that a task queue executes to be idempotent allows one to use a queueing system that has accepted this design trade-off.

Visit the following resources to learn more:

- [@article@What is an idempotent operation?](https://stackoverflow.com/questions/1077412/what-is-an-idempotent-operation)
- [@article@Overview of Idempotent Operation](https://www.baeldung.com/cs/idempotent-operations)

## Improper Instantiation

# Improper Instantiation

Improper instantiation in system design refers to the practice of creating unnecessary instances of an object, class or service, which can lead to performance and scalability issues. This can happen when the system is not properly designed, when the code is not written in an efficient way, or when the code is not optimized for the specific use case.

Visit the following resources to learn more:

- [@article@Improper Instantiation antipattern](https://learn.microsoft.com/en-us/azure/architecture/antipatterns/improper-instantiation/)

## Index Table

# Index Table

Create indexes over the fields in data stores that are frequently referenced by queries. This pattern can improve query performance by allowing applications to more quickly locate the data to retrieve from a data store.

Visit the following resources to learn more:

- [@article@Index Table pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/index-table)

## Instrumentation

# Instrumentation

Instrumentation is a critical part of the monitoring process. You can make meaningful decisions about the performance and health of a system only if you first capture the data that enables you to make these decisions. The information that you gather by using instrumentation should be sufficient to enable you to assess performance, diagnose problems, and make decisions without requiring you to sign in to a remote production server to perform tracing (and debugging) manually. Instrumentation data typically comprises metrics and information that's written to trace logs.

Visit the following resources to learn more:

- [@article@Instrumenting an application](https://learn.microsoft.com/en-us/azure/architecture/best-practices/monitoring#instrumenting-an-application)
- [@article@Instrumenting using Open Telemetry](https://opentelemetry.io/docs/concepts/what-is-opentelemetry)

## Introduction

# Introduction

System design is the process of defining the elements of a system, as well as their interactions and relationships, in order to satisfy a set of specified requirements.

It involves taking a problem statement, breaking it down into smaller components and designing each component to work together effectively to achieve the overall goal of the system. This process typically includes analyzing the current system (if any) and determining any deficiencies, creating a detailed plan for the new system, and testing the design to ensure that it meets the requirements. It is an iterative process that may involve multiple rounds of design, testing, and refinement.

In software engineering, system design is a phase in the software development process that focuses on the high-level design of a software system, including the architecture and components.

It is also one of the important aspects of the interview process for software engineers. Most of the companies have a dedicated system design interview round, where they ask the candidates to design a system for a given problem statement. The candidates are expected to come up with a detailed design of the system, including the architecture, components, and their interactions. They are also expected to discuss the trade-offs involved in their design and the alternatives that they considered.

## Key Value Store

# Key Value Store

A key-value store generally allows for `O(1)` reads and writes and is often backed by memory or SSD. Data stores can maintain keys in lexicographic order, allowing efficient retrieval of key ranges. Key-value stores can allow for storing of metadata with a value.

Key-value stores provide high performance and are often used for simple data models or for rapidly-changing data, such as an in-memory cache layer. Since they offer only a limited set of operations, complexity is shifted to the application layer if additional operations are needed.

Visit the following resources to learn more:

- [@article@Key–value database](https://en.wikipedia.org/wiki/Key%E2%80%93value_database)
- [@article@What are the disadvantages of using a key/value table?](https://stackoverflow.com/questions/4056093/what-are-the-disadvantages-of-using-a-key-value-table-over-nullable-columns-or)

## Latency Vs Throughput

# Latency vs Throughput

Latency and throughput are two important measures of a system's performance. **Latency** refers to the amount of time it takes for a system to respond to a request. **Throughput** refers to the number of requests that a system can handle at the same time.

Generally, you should aim for maximal throughput with acceptable latency.

Visit the following resources to learn more:

- [@article@System Design: Latency vs Throughput](https://cs.fyi/guide/latency-vs-throughput/)
- [@article@Understanding Latency versus Throughput](https://community.cadence.com/cadence_blogs_8/b/fv/posts/understanding-latency-vs-throughput)
- [@video@Latency and Throughput - MIT](https://www.youtube.com/watch?v=3HIV4MnLGCw)

## Layer 4 Load Balancing

# Layer 4 Load Balancing

Layer 4 load balancers look at info at the transport layer to decide how to distribute requests. Generally, this involves the source, destination IP addresses, and ports in the header, but not the contents of the packet. Layer 4 load balancers forward network packets to and from the upstream server, performing Network Address Translation (NAT).

Visit the following resources to learn more:

- [@article@Layer 4 Load Balancing](https://www.f5.com/glossary/layer-4-load-balancing)

## Layer 7 Load Balancing

# Layer 7 Load Balancing

Layer 7 load balancers look at the application layer to decide how to distribute requests. This can involve contents of the header, message, and cookies. Layer 7 load balancers terminate network traffic, reads the message, makes a load-balancing decision, then opens a connection to the selected server. For example, a layer 7 load balancer can direct video traffic to servers that host videos while directing more sensitive user billing traffic to security-hardened servers.

At the cost of flexibility, layer 4 load balancing requires less time and computing resources than Layer 7, although the performance impact can be minimal on modern commodity hardware.

## Lb Vs Reverse Proxy

# Load Balancer vs Reverse Proxy

*   Deploying a load balancer is useful when you have multiple servers. Often, load balancers route traffic to a set of servers serving the same function.
*   Reverse proxies can be useful even with just one web server or application server, opening up the benefits described in the previous section.
*   Solutions such as NGINX and HAProxy can support both layer 7 reverse proxying and load balancing.

Disadvantages of Reverse Proxy:
-------------------------------

*   Introducing a reverse proxy results in increased complexity.
*   A single reverse proxy is a single point of failure, configuring multiple reverse proxies (ie a failover) further increases complexity.

Visit the following resources to learn more:

- [@article@Reverse Proxy vs Load Balancer](https://www.nginx.com/resources/glossary/reverse-proxy-vs-load-balancer/)
- [@article@NGINX Architecture](https://www.nginx.com/blog/inside-nginx-how-we-designed-for-performance-scale/)
- [@article@HAProxy Architecture Guide](http://www.haproxy.org/download/1.2/doc/architecture.txt)
- [@article@Reverse Proxy](https://en.wikipedia.org/wiki/Reverse_proxy)

## Leader Election

# Leader Election

Coordinate the actions performed by a collection of collaborating instances in a distributed application by electing one instance as the leader that assumes responsibility for managing the others. This can help to ensure that instances don't conflict with each other, cause contention for shared resources, or inadvertently interfere with the work that other instances are performing.

Visit the following resources to learn more:

- [@article@Leader Election Pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/leader-election)

## Leader Election

# Leader Election

Coordinate the actions performed by a collection of collaborating instances in a distributed application by electing one instance as the leader that assumes responsibility for managing the others. This can help to ensure that instances don't conflict with each other, cause contention for shared resources, or inadvertently interfere with the work that other instances are performing.

Visit the following resources to learn more:

- [@article@Leader Election Pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/leader-election)

## Load Balancers

# Load Balancers

Load balancers distribute incoming client requests to computing resources such as application servers and databases. In each case, the load balancer returns the response from the computing resource to the appropriate client. Load balancers are effective at:

*   Preventing requests from going to unhealthy servers
*   Preventing overloading resources
*   Helping to eliminate a single point of failure

Load balancers can be implemented with hardware (expensive) or with software such as HAProxy. Additional benefits include:

*   **SSL termination** - Decrypt incoming requests and encrypt server responses so backend servers do not have to perform these potentially expensive operations
    *   Removes the need to install X.509 certificates on each server
*   **Session persistence** - Issue cookies and route a specific client's requests to same instance if the web apps do not keep track of sessions

Disadvantages of load balancer
------------------------------

*   The load balancer can become a performance bottleneck if it does not have enough resources or if it is not configured properly.
*   Introducing a load balancer to help eliminate a single point of failure results in increased complexity.
*   A single load balancer is a single point of failure, configuring multiple load balancers further increases complexity.

Visit the following resources to learn more:

- [@article@Scalability](https://cs.fyi/guide/scalability-for-dummies)
- [@article@NGINX Architecture](https://www.nginx.com/blog/inside-nginx-how-we-designed-for-performance-scale/)
- [@article@HAProxy Architecture Guide](http://www.haproxy.org/download/1.2/doc/architecture.txt)

## Load Balancing Algorithms

# Load Balancing Algorithms

A load balancer is a software or hardware device that keeps any one server from becoming overloaded. A load balancing algorithm is the logic that a load balancer uses to distribute network traffic between servers (an algorithm is a set of predefined rules).

There are two primary approaches to load balancing. Dynamic load balancing uses algorithms that take into account the current state of each server and distribute traffic accordingly. Static load balancing distributes traffic without making these adjustments. Some static algorithms send an equal amount of traffic to each server in a group, either in a specified order or at random.

Visit the following resources to learn more:

- [@article@Types of Load Balancing Algorithms](https://www.cloudflare.com/learning/performance/types-of-load-balancing-algorithms/)
- [@feed@Explore top posts about Algorithms](https://app.daily.dev/tags/algorithms?ref=roadmapsh)

## Materialized View

# Materialized View

Generate prepopulated views over the data in one or more data stores when the data isn't ideally formatted for required query operations. This can help support efficient querying and data extraction, and improve application performance.

Visit the following resources to learn more:

- [@article@Materialized View pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/materialized-view)

## Message Queues

# Message Queues

Message queues receive, hold, and deliver messages. If an operation is too slow to perform inline, you can use a message queue with the following workflow:

*   An application publishes a job to the queue, then notifies the user of job status
*   A worker picks up the job from the queue, processes it, then signals the job is complete

The user is not blocked and the job is processed in the background. During this time, the client might optionally do a small amount of processing to make it seem like the task has completed. For example, if posting a tweet, the tweet could be instantly posted to your timeline, but it could take some time before your tweet is actually delivered to all of your followers.

Visit the following resources to learn more:

- [@article@What is Redis?](https://redis.io/)
- [@article@RabbitMQ in Message Queues](https://www.rabbitmq.com/)
- [@article@Overview of Amazon SQS](https://aws.amazon.com/sqs/)
- [@article@Apache Kafka](https://kafka.apache.org/)
- [@article@RabbitMQ for beginners](https://www.cloudamqp.com/blog/part1-rabbitmq-for-beginners-what-is-rabbitmq.html)

## Messaging

# Messaging

Messaging is a pattern that allows for the communication and coordination between different components or systems, using messaging technologies such as message queues, message brokers, and event buses. This pattern allows for decoupling of the sender and receiver, and can be used to build scalable and flexible systems.

Visit the following resources to learn more:

- [@article@Messaging Cloud Patterns](https://learn.microsoft.com/en-us/azure/architecture/patterns/category/messaging)

## Microservices

# Microservices

Related to the "Application Layer" discussion are microservices, which can be described as a suite of independently deployable, small, modular services. Each service runs a unique process and communicates through a well-defined, lightweight mechanism to serve a business goal. 1

Pinterest, for example, could have the following microservices: user profile, follower, feed, search, photo upload, etc.

Visit the following resources to learn more:

- [@article@Introduction to Microservices](https://aws.amazon.com/microservices/)
- [@article@Microservices - Wikipedia](https://en.wikipedia.org/wiki/Microservices)
- [@article@Microservices](https://martinfowler.com/articles/microservices.html)
- [@feed@Explore top posts about Microservices](https://app.daily.dev/tags/microservices?ref=roadmapsh)

## Monitoring

# Monitoring

Distributed applications and services running in the cloud are, by their nature, complex pieces of software that comprise many moving parts. In a production environment, it's important to be able to track the way in which users use your system, trace resource utilization, and generally monitor the health and performance of your system. You can use this information as a diagnostic aid to detect and correct issues, and also to help spot potential problems and prevent them from occurring.

Visit the following resources to learn more:

- [@article@Monitoring and Diagnostics Guidance](https://learn.microsoft.com/en-us/azure/architecture/best-practices/monitoring)
- [@feed@Explore top posts about Monitoring](https://app.daily.dev/tags/monitoring?ref=roadmapsh)

## Monolithic Persistence

# Monolithic Persistence

Monolithic Persistence refers to the use of a single, monolithic database to store all of the data for an application or system. This approach can be used for simple, small-scale systems but as the system grows and evolves it can become a bottleneck, resulting in poor scalability, limited flexibility, and increased complexity. To address these limitations, a number of approaches can be taken such as Microservices, Sharding, and NoSQL databases.

Visit the following resources to learn more:

- [@article@Monolithic Persistence antipattern](https://learn.microsoft.com/en-us/azure/architecture/antipatterns/monolithic-persistence/)

## No Caching

# No Caching

No caching antipattern occurs when a cloud application that handles many concurrent requests, repeatedly fetches the same data. This can reduce performance and scalability.

When data is not cached, it can cause a number of undesirable behaviors, including:

*   Repeatedly fetching the same information from a resource that is expensive to access, in terms of I/O overhead or latency.
*   Repeatedly constructing the same objects or data structures for multiple requests.
*   Making excessive calls to a remote service that has a service quota and throttles clients past a certain limit.

Visit the following resources to learn more:

- [@article@No Caching antipattern](https://learn.microsoft.com/en-us/azure/architecture/antipatterns/no-caching/)

## Noisy Neighbor

# Noisy Neighbor

Noisy neighbor refers to a situation in which one or more components of a system are utilizing a disproportionate amount of shared resources, leading to resource contention and reduced performance for other components. This can occur when a system is not properly designed or configured to handle the workload, or when a component is behaving unexpectedly.

Examples of noisy neighbor scenarios include:

*   One user on a shared server utilizing a large amount of CPU or memory, leading to reduced performance for other users on the same server.
*   One process on a shared server utilizing a large amount of I/O, causing other processes to experience slow I/O and increased latency.
*   One application consuming a large amount of network bandwidth, causing other applications to experience reduced throughput.

Visit the following resources to learn more:

- [@article@Noisy Neighbor antipattern](https://learn.microsoft.com/en-us/azure/architecture/antipatterns/noisy-neighbor/noisy-neighbor)

## Performance Antipatterns

# Performance Antipatterns

Performance antipatterns in system design refer to common mistakes or suboptimal practices that can lead to poor performance in a system. These patterns can occur at different levels of the system and can be caused by a variety of factors such as poor design, lack of optimization, or lack of understanding of the workload.

Some of the examples of performance antipatterns include:

*   **N+1 queries:** This occurs when a system makes multiple queries to a database to retrieve related data, instead of using a single query to retrieve all the necessary data.
*   **Chatty interfaces:** This occurs when a system makes too many small and frequent requests to an external service or API, instead of making fewer, larger requests.
*   **Unbounded data:** This occurs when a system retrieves or processes more data than is necessary for the task at hand, leading to increased resource usage and reduced performance.
*   **Inefficient algorithms:** This occurs when a system uses an algorithm that is not well suited to the task at hand, leading to increased resource usage and reduced performance.

Visit the following resources to learn more:

- [@article@Performance antipatterns for cloud applications](https://learn.microsoft.com/en-us/azure/architecture/antipatterns/)
- [@feed@Explore top posts about Performance](https://app.daily.dev/tags/performance?ref=roadmapsh)

## Performance Monitoring

# Performance Monitoring

As the system is placed under more and more stress (by increasing the volume of users), the size of the datasets that these users access grows and the possibility of failure of one or more components becomes more likely. Frequently, component failure is preceded by a decrease in performance. If you're able detect such a decrease, you can take proactive steps to remedy the situation.

Visit the following resources to learn more:

- [@article@Performance Monitoring](https://learn.microsoft.com/en-us/azure/architecture/best-practices/monitoring#performance-monitoring)
- [@feed@Explore top posts about Monitoring](https://app.daily.dev/tags/monitoring?ref=roadmapsh)

## Performance Vs Scalability

# Performance vs Scalability

A service is **scalable** if it results in increased **performance** in a manner proportional to resources added. Generally, increasing performance means serving more units of work, but it can also be to handle larger units of work, such as when datasets grow.

Another way to look at performance vs scalability:

*   If you have a **performance** problem, your system is slow for a single user.
*   If you have a **scalability** problem, your system is fast for a single user but slow under heavy load.

Visit the following resources to learn more:

- [@article@Scalability, Availability & Stability Patterns](https://www.slideshare.net/jboner/scalability-availability-stability-patterns/)
- [@article@A Word on Scalability](https://www.allthingsdistributed.com/2006/03/a_word_on_scalability.html)
- [@article@Performance vs Scalability](https://blog.professorbeekums.com/performance-vs-scalability/)
- [@feed@Explore top posts about Performance](https://app.daily.dev/tags/performance?ref=roadmapsh)

## Pipes  Filters

# Pipes and Filters

Decompose a task that performs complex processing into a series of separate elements that can be reused. This can improve performance, scalability, and reusability by allowing task elements that perform the processing to be deployed and scaled independently.

Visit the following resources to learn more:

- [@article@Pipe and Filter Architectural Style](https://learn.microsoft.com/en-us/azure/architecture/patterns/pipes-and-filters)

## Pipes And Filters

# Pipes and Filters

Decompose a task that performs complex processing into a series of separate elements that can be reused. This can improve performance, scalability, and reusability by allowing task elements that perform the processing to be deployed and scaled independently.

Visit the following resources to learn more:

- [@article@Pipes and Filters pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/pipes-and-filters)

## Priority Queue

# Priority Queue

Prioritize requests sent to services so that requests with a higher priority are received and processed more quickly than those with a lower priority. This pattern is useful in applications that offer different service level guarantees to individual clients.

Visit the following resources to learn more:

- [@article@Priority Queue pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/priority-queue)

## Publishersubscriber

# Publisher Subscriber

Enable an application to announce events to multiple interested consumers asynchronously, without coupling the senders to the receivers.

Visit the following resources to learn more:

- [@article@Publisher-Subscriber pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/publisher-subscriber)

## Pull Cdns

# Pull CDNs

Pull CDNs grab new content from your server when the first user requests the content. You leave the content on your server and rewrite URLs to point to the CDN. This results in a slower request until the content is cached on the CDN.

A time-to-live (TTL) determines how long content is cached. Pull CDNs minimize storage space on the CDN, but can create redundant traffic if files expire and are pulled before they have actually changed. Sites with heavy traffic work well with pull CDNs, as traffic is spread out more evenly with only recently-requested content remaining on the CDN.

Visit the following resources to learn more:

- [@opensource@Introduction to CDNs](https://github.com/donnemartin/system-design-primer#content-delivery-network)
- [@article@The Differences Between Push And Pull CDNs](http://www.travelblogadvice.com/technical/the-differences-between-push-and-pull-cdns/)

## Push Cdns

# Push CDNs

Push CDNs receive new content whenever changes occur on your server. You take full responsibility for providing content, uploading directly to the CDN and rewriting URLs to point to the CDN. You can configure when content expires and when it is updated. Content is uploaded only when it is new or changed, minimizing traffic, but maximizing storage.

Sites with a small amount of traffic or sites with content that isn't often updated work well with push CDNs. Content is placed on the CDNs once, instead of being re-pulled at regular intervals.

Visit the following resources to learn more:

- [@opensource@Introduction to CDNs](https://github.com/donnemartin/system-design-primer#content-delivery-network)

## Queue Based Load Leveling

# Queue-Based load leveling

Use a queue that acts as a buffer between a task and a service it invokes in order to smooth intermittent heavy loads that can cause the service to fail or the task to time out. This can help to minimize the impact of peaks in demand on availability and responsiveness for both the task and the service.

Visit the following resources to learn more:

- [@article@Queue-Based Load Leveling pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/queue-based-load-leveling)

## Queue Based Load Leveling

# Queue-Based Load Leveling

Use a queue that acts as a buffer between a task and a service it invokes in order to smooth intermittent heavy loads that can cause the service to fail or the task to time out. This can help to minimize the impact of peaks in demand on availability and responsiveness for both the task and the service.

Visit the following resources to learn more:

- [@article@Queue-Based Load Leveling pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/queue-based-load-leveling)

## Queue Based Load Leveling

# Queue-Based load leveling

Use a queue that acts as a buffer between a task and a service it invokes in order to smooth intermittent heavy loads that can cause the service to fail or the task to time out. This can help to minimize the impact of peaks in demand on availability and responsiveness for both the task and the service.

Visit the following resources to learn more:

- [@article@Queue-Based Load Leveling pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/queue-based-load-leveling)

## Refresh Ahead

# Refresh-ahead

You can configure the cache to automatically refresh any recently accessed cache entry prior to its expiration.

Refresh-ahead can result in reduced latency vs read-through if the cache can accurately predict which items are likely to be needed in the future.

Disadvantage of refresh-ahead:
------------------------------

*   Not accurately predicting which items are likely to be needed in the future can result in reduced performance than without refresh-ahead.

![](https://i.imgur.com/sBXb7lb.png)

Visit the following resources to learn more:

- [@article@From cache to in-memory data grid](http://www.slideshare.net/tmatyashovsky/from-cache-to-in-memory-data-grid-introduction-to-hazelcast)
- [@article@Caching Strategy: Refresh Ahead Pattern](https://www.enjoyalgorithms.com/blog/refresh-ahead-caching-pattern)

## Reliability Patterns

# Reliability Patterns

These patterns provide a way to design and implement systems that can withstand failures, maintain high levels of performance, and recover quickly from disruptions. Some common reliability patterns include Failover, Circuit Breaker, Retry, Bulkhead, Backpressure, Cache-Aside, Idempotent Operations and Health Endpoint Monitoring.

Visit the following resources to learn more:

- [@article@Reliability Patterns](https://learn.microsoft.com/en-us/azure/architecture/framework/resiliency/reliability-patterns)

## Replication

# Replication

Replication is an availability pattern that involves having multiple copies of the same data stored in different locations. In the event of a failure, the data can be retrieved from a different location. There are two main types of replication: Master-Master replication and Master-Slave replication.

*   **Master-Master replication:** In this type of replication, multiple servers are configured as "masters," and each one can accept read and write operations. This allows for high availability and allows any of the servers to take over if one of them fails. However, this type of replication can lead to conflicts if multiple servers update the same data at the same time, so some conflict resolution mechanism is needed to handle this.
    
*   **Master-Slave replication:** In this type of replication, one server is designated as the "master" and handles all write operations, while multiple "slave" servers handle read operations. If the master fails, one of the slaves can be promoted to take its place. This type of replication is simpler to set up and maintain compared to Master-Master replication.

Visit the following resources to learn more:

- [@opensource@Replication: Availability Pattern](https://github.com/donnemartin/system-design-primer#replication)
- [@article@Database Replication Introduction: Types and Advantages](https://www.enjoyalgorithms.com/blog/introduction-to-database-replication-system-design)

## Replication

# Replication

Replication is the process of copying data from one database to another. Replication is used to increase availability and scalability of databases. There are two types of replication: master-slave and master-master.

Master-slave Replication:
-------------------------

The master serves reads and writes, replicating writes to one or more slaves, which serve only reads. Slaves can also replicate to additional slaves in a tree-like fashion. If the master goes offline, the system can continue to operate in read-only mode until a slave is promoted to a master or a new master is provisioned.

Master-master Replication:
--------------------------

Both masters serve reads and writes and coordinate with each other on writes. If either master goes down, the system can continue to operate with both reads and writes.

## Resiliency

# Resilience

Resiliency is the ability of a system to gracefully handle and recover from failures, both inadvertent and malicious.

The nature of cloud hosting, where applications are often multi-tenant, use shared platform services, compete for resources and bandwidth, communicate over the Internet, and run on commodity hardware means there is an increased likelihood that both transient and more permanent faults will arise. The connected nature of the internet and the rise in sophistication and volume of attacks increase the likelihood of a security disruption.

Detecting failures and recovering quickly and efficiently, is necessary to maintain resiliency.

Visit the following resources to learn more:

- [@article@Resiliency Patterns](https://learn.microsoft.com/en-us/azure/architecture/framework/resiliency/reliability-patterns#resiliency)

## Rest

# REST

REST is an architectural style enforcing a client/server model where the client acts on a set of resources managed by the server. The server provides a representation of resources and actions that can either manipulate or get a new representation of resources. All communication must be stateless and cacheable.

There are four qualities of a RESTful interface:

*   Identify resources (URI in HTTP) - use the same URI regardless of any operation.
*   Change with representations (Verbs in HTTP) - use verbs, headers, and body.
*   Self-descriptive error message (status response in HTTP) - Use status codes, don't reinvent the wheel.
*   HATEOAS (HTML interface for HTTP) - your web service should be fully accessible in a browser.

REST is focused on exposing data. It minimizes the coupling between client/server and is often used for public HTTP APIs. REST uses a more generic and uniform method of exposing resources through URIs, representation through headers, and actions through verbs such as GET, POST, PUT, DELETE, and PATCH. Being stateless, REST is great for horizontal scaling and partitioning.

Visit the following resources to learn more:

- [@opensource@What Is REST?](https://github.com/donnemartin/system-design-primer#representational-state-transfer-rest)
- [@article@What are the drawbacks of using RESTful APIs?](https://www.quora.com/What-are-the-drawbacks-of-using-RESTful-APIs)
- [@feed@Explore top posts about REST API](https://app.daily.dev/tags/rest-api?ref=roadmapsh)

## Retry Storm

# Retry Storm

Retry Storm refers to a situation in which a large number of retries are triggered in a short period of time, leading to a significant increase in traffic and resource usage. This can occur when a system is not properly designed to handle failures or when a component is behaving unexpectedly. This can lead to Performance degradation, Increased resource utilization, Increased network traffic, and Poor user experience. To address retry storms, a number of approaches can be taken such as Exponential backoff, Circuit breaking, and Monitoring and alerting.

Visit the following resources to learn more:

- [@article@Retry Storm antipattern](https://learn.microsoft.com/en-us/azure/architecture/antipatterns/retry-storm/)
- [@article@How To Avoid Retry Storms In Distributed Systems](https://faun.pub/how-to-avoid-retry-storms-in-distributed-systems-91bf34f43c7f)

## Retry

# Retry

Enable an application to handle transient failures when it tries to connect to a service or network resource, by transparently retrying a failed operation. This can improve the stability of the application.

Visit the following resources to learn more:

- [@article@Retry pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/retry)

## Returning Results

# Returning Results

Background jobs execute asynchronously in a separate process, or even in a separate location, from the UI or the process that invoked the background task. Ideally, background tasks are "fire and forget" operations, and their execution progress has no impact on the UI or the calling process. This means that the calling process does not wait for completion of the tasks. Therefore, it cannot automatically detect when the task ends.

Visit the following resources to learn more:

- [@article@Returning Results - Background Jobs](https://learn.microsoft.com/en-us/azure/architecture/best-practices/background-jobs#returning-results)

## Rpc

# RPC

In an RPC, a client causes a procedure to execute on a different address space, usually a remote server. The procedure is coded as if it were a local procedure call, abstracting away the details of how to communicate with the server from the client program. Remote calls are usually slower and less reliable than local calls so it is helpful to distinguish RPC calls from local calls. Popular RPC frameworks include [Protobuf](https://developers.google.com/protocol-buffers/), [Thrift](https://thrift.apache.org/), and [Avro](https://avro.apache.org/docs/current/).

RPC is a request-response protocol:

*   Client program - Calls the client stub procedure. The parameters are pushed onto the stack like a local procedure call.
*   Client stub procedure - Marshals (packs) procedure id and arguments into a request message.
*   Client communication module - OS sends the message from the client to the server.
*   Server communication module - OS passes the incoming packets to the server stub procedure.
*   Server stub procedure - Unmarshalls the results, calls the server procedure matching the procedure id and passes the given arguments.
*   The server response repeats the steps above in reverse order.

Sample RPC calls:

    GET /someoperation?data=anId
    
    POST /anotheroperation
    {
      "data":"anId";
      "anotherdata": "another value"
    }
    

RPC is focused on exposing behaviors. RPCs are often used for performance reasons with internal communications, as you can hand-craft native calls to better fit your use cases.

Disadvantage of RPC
-------------------

*   RPC clients become tightly coupled to the service implementation.
*   A new API must be defined for every new operation or use case.
*   It can be difficult to debug RPC.
*   You might not be able to leverage existing technologies out of the box. For example, it might require additional effort to ensure [RPC calls are properly cached](http://etherealbits.com/2012/12/debunking-the-myths-of-rpc-rest/) on caching servers such as [Squid](http://www.squid-cache.org/).

Visit the following resources to learn more:

- [@opensource@What Is RPC?](https://github.com/donnemartin/system-design-primer#remote-procedure-call-rpc)
- [@feed@Explore top posts about Backend Development](https://app.daily.dev/tags/backend?ref=roadmapsh)

## Schedule Driven

# Schedule Driven

Schedule-driven invocation uses a timer to start the background task. Examples of using schedule-driven triggers include:

*   A timer that is running locally within the application or as part of the application's operating system invokes a background task on a regular basis.
*   A timer that is running in a different application, such as Azure Logic Apps, sends a request to an API or web service on a regular basis. The API or web service invokes the background task.
*   A separate process or application starts a timer that causes the background task to be invoked once after a specified time delay, or at a specific time.

Typical examples of tasks that are suited to schedule-driven invocation include batch-processing routines (such as updating related-products lists for users based on their recent behavior), routine data processing tasks (such as updating indexes or generating accumulated results), data analysis for daily reports, data retention cleanup, and data consistency checks.

Visit the following resources to learn more:

- [@article@Schedule Driven - Background Jobs](https://learn.microsoft.com/en-us/azure/architecture/best-practices/background-jobs#schedule-driven-triggers)

## Scheduler Agent Supervisor

# Scheduling Agent Supervisor

Coordinate a set of distributed actions as a single operation. If any of the actions fail, try to handle the failures transparently, or else undo the work that was performed, so the entire operation succeeds or fails as a whole. This can add resiliency to a distributed system, by enabling it to recover and retry actions that fail due to transient exceptions, long-lasting faults, and process failures.

Visit the following resources to learn more:

- [@article@Scheduler Agent Supervisor pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/scheduler-agent-supervisor)

## Scheduling Agent Supervisor

# Scheduling Agent Supervisor

Coordinate a set of distributed actions as a single operation. If any of the actions fail, try to handle the failures transparently, or else undo the work that was performed, so the entire operation succeeds or fails as a whole. This can add resiliency to a distributed system, by enabling it to recover and retry actions that fail due to transient exceptions, long-lasting faults, and process failures.

Visit the following resources to learn more:

- [@article@Scheduler Agent Supervisor pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/scheduler-agent-supervisor)

## Security Monitoring

# Security Monitoring

All commercial systems that include sensitive data must implement a security structure. The complexity of the security mechanism is usually a function of the sensitivity of the data. In a system that requires users to be authenticated, you should record:

*   All sign-in attempts, whether they fail or succeed.
*   All operations performed by—and the details of all resources accessed by—an authenticated user.
*   When a user ends a session and signs out.

Monitoring might be able to help detect attacks on the system. For example, a large number of failed sign-in attempts might indicate a brute-force attack. An unexpected surge in requests might be the result of a distributed denial-of-service (DDoS) attack. You must be prepared to monitor all requests to all resources regardless of the source of these requests. A system that has a sign-in vulnerability might accidentally expose resources to the outside world without requiring a user to actually sign in.

Visit the following resources to learn more:

- [@article@Security Monitoring](https://learn.microsoft.com/en-us/azure/architecture/best-practices/monitoring#security-monitoring)
- [@feed@Explore top posts about Monitoring](https://app.daily.dev/tags/monitoring?ref=roadmapsh)

## Security

# Security

Security provides confidentiality, integrity, and availability assurances against malicious attacks on information systems (and safety assurances for attacks on operational technology systems). Losing these assurances can negatively impact your business operations and revenue, as well as your organization's reputation in the marketplace. Maintaining security requires following well-established practices (security hygiene) and being vigilant to detect and rapidly remediate vulnerabilities and active attacks.

Visit the following resources to learn more:

- [@article@Security patterns](https://learn.microsoft.com/en-us/azure/architecture/framework/security/security-patterns)
- [@feed@Explore top posts about Security](https://app.daily.dev/tags/security?ref=roadmapsh)

## Sequential Convoy

# Sequential Convoy

Sequential Convoy is a pattern that allows for the execution of a series of tasks, or convoy, in a specific order. This pattern can be used to ensure that a set of dependent tasks are executed in the correct order and to handle errors or failures during the execution of the tasks. It can be used in scenarios like workflow and transaction. It can be implemented using a variety of technologies such as state machines, workflows, and transactions.

Visit the following resources to learn more:

- [@article@What is Sequential Convoy?](https://learn.microsoft.com/en-us/biztalk/core/sequential-convoys)
- [@article@Overview - Sequential Convoy pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/sequential-convoy)

## Service Discovery

# Service Discovery

Systems such as [Consul](https://www.consul.io/docs/index.html), [Etcd](https://coreos.com/etcd/docs/latest), and [Zookeeper](http://www.slideshare.net/sauravhaloi/introduction-to-apache-zookeeper) can help services find each other by keeping track of registered names, addresses, and ports. [Health checks](https://www.consul.io/intro/getting-started/checks.html) help verify service integrity and are often done using an HTTP endpoint. Both Consul and Etcd have a built in key-value store that can be useful for storing config values and other shared data.

Visit the following resources to learn more:

- [@opensource@Intro to Service Discovery](https://github.com/donnemartin/system-design-primer#Service-Discovery)
- [@article@What is Service-oriented architecture?](https://en.wikipedia.org/wiki/Service-oriented_architecture)
- [@feed@Explore top posts about Architecture](https://app.daily.dev/tags/architecture?ref=roadmapsh)

## Sharding

# Sharding

Sharding distributes data across different databases such that each database can only manage a subset of the data. Taking a users database as an example, as the number of users increases, more shards are added to the cluster.

Similar to the advantages of federation, sharding results in less read and write traffic, less replication, and more cache hits. Index size is also reduced, which generally improves performance with faster queries. If one shard goes down, the other shards are still operational, although you'll want to add some form of replication to avoid data loss. Like federation, there is no single central master serializing writes, allowing you to write in parallel with increased throughput.

Visit the following resources to learn more:

- [@article@The coming of the Shard](http://highscalability.com/blog/2009/8/6/an-unorthodox-approach-to-database-design-the-coming-of-the.html)
- [@article@Shard (database architecture)](https://en.wikipedia.org/wiki/Shard_(database_architecture))
- [@feed@Explore top posts about Backend Development](https://app.daily.dev/tags/backend?ref=roadmapsh)

## Sharding

# Sharding

Sharding is a technique used to horizontally partition a large data set across multiple servers, in order to improve the performance, scalability, and availability of a system. This is done by breaking the data set into smaller chunks, called shards, and distributing the shards across multiple servers. Each shard is self-contained and can be managed and scaled independently of the other shards. Sharding can be used in scenarios like scalability, availability, and geo-distribution. Sharding can be implemented using several different algorithms such as range-based sharding, hash-based sharding, and directory-based sharding.

Visit the following resources to learn more:

- [@article@Sharding pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/sharding)
- [@feed@Explore top posts about Backend Development](https://app.daily.dev/tags/backend?ref=roadmapsh)

## Sidecar

# Sidecar

Deploy components of an application into a separate process or container to provide isolation and encapsulation. This pattern can also enable applications to be composed of heterogeneous components and technologies.

This pattern is named Sidecar because it resembles a sidecar attached to a motorcycle. In the pattern, the sidecar is attached to a parent application and provides supporting features for the application. The sidecar also shares the same lifecycle as the parent application, being created and retired alongside the parent. The sidecar pattern is sometimes referred to as the sidekick pattern and is a decomposition pattern.

Visit the following resources to learn more:

- [@article@Sidecar pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/sidecar)
- [@feed@Explore top posts about Infrastructure](https://app.daily.dev/tags/infrastructure?ref=roadmapsh)

## Sql Tuning

# SQL Tuning

SQL tuning is the attempt to diagnose and repair SQL statements that fail to meet a performance standard. It is a broad topic and many books have been written as reference. It's important to benchmark and profile to simulate and uncover bottlenecks.

*   Benchmark - Simulate high-load situations with tools such as ab.
*   Profile - Enable tools such as the slow query log to help track performance issues.

Benchmarking and profiling might point you to the following optimizations.

Visit the following resources to learn more:

- [@official@Introduction to SQL Tuning - Oracle](https://docs.oracle.com/en/database/oracle/oracle-database/23/tgsql/introduction-to-sql-tuning.html#GUID-B653E5F3-F078-4BBC-9516-B892960046A2)
- [@article@Query Optimization for Mere Humans in PostgreSQL](https://towardsdatascience.com/query-optimization-for-mere-humans-in-postgresql-875ab864390a/)
- [@feed@Explore top posts about SQL](https://app.daily.dev/tags/sql?ref=roadmapsh)

## Sql Vs Nosql

# SQL vs noSQL

SQL databases, such as MySQL and PostgreSQL, are best suited for structured, relational data and use a fixed schema. They provide robust ACID (Atomicity, Consistency, Isolation, Durability) transactions and support complex queries and joins.

NoSQL databases, such as MongoDB and Cassandra, are best suited for unstructured, non-relational data and use a flexible schema. They provide high scalability and performance for large amounts of data and are often used in big data and real-time web applications.

The choice between SQL and NoSQL depends on the specific use case and requirements of the project. If you need to store and query structured data with complex relationships, an SQL database is likely a better choice. If you need to store and query large amounts of unstructured data with high scalability and performance, a NoSQL database may be a better choice.

Visit the following resources to learn more:

- [@article@SQL vs NoSQL: The Differences](https://www.sitepoint.com/sql-vs-nosql-differences/)
- [@article@SQL vs. NoSQL Databases: What’s the Difference?](https://www.ibm.com/blog/sql-vs-nosql/)
- [@article@NoSQL vs. SQL Databases](https://www.mongodb.com/nosql-explained/nosql-vs-sql)
- [@feed@Explore top posts about NoSQL](https://app.daily.dev/tags/nosql?ref=roadmapsh)

## Static Content Hosting

# Static Content Hosting

Deploy static content to a cloud-based storage service that can deliver them directly to the client. This can reduce the need for potentially expensive compute instances.

Visit the following resources to learn more:

- [@article@Static Content Hosting pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/static-content-hosting)

## Static Content Hosting

# Static Content Hosting

Deploy static content to a cloud-based storage service that can deliver them directly to the client. This can reduce the need for potentially expensive compute instances.

Visit the following resources to learn more:

- [@article@Static Content Hosting pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/static-content-hosting)

## Strangler Fig

# Strangler fig

Incrementally migrate a legacy system by gradually replacing specific pieces of functionality with new applications and services. As features from the legacy system are replaced, the new system eventually replaces all of the old system's features, strangling the old system and allowing you to decommission it.

Visit the following resources to learn more:

- [@article@What is Strangler fig?](https://learn.microsoft.com/en-us/azure/architecture/patterns/strangler-fig)

## Strong Consistency

# Strong Consistency

After an update is made to the data, it will be immediately visible to any subsequent read operations. The data is replicated in a synchronous manner, ensuring that all copies of the data are updated at the same time.

Visit the following resources to learn more:

- [@article@Consistency Patterns in Distributed Systems](https://cs.fyi/guide/consistency-patterns-week-strong-eventual/)

## Synchronous Io

# Synchronous I/O

Blocking the calling thread while I/O completes can reduce performance and affect vertical scalability.

A synchronous I/O operation blocks the calling thread while the I/O completes. The calling thread enters a wait state and is unable to perform useful work during this interval, wasting processing resources.

Common examples of I/O include:

*   Retrieving or persisting data to a database or any type of persistent storage.
*   Sending a request to a web service.
*   Posting a message or retrieving a message from a queue.
*   Writing to or reading from a local file.

This antipattern typically occurs because:

*   It appears to be the most intuitive way to perform an operation.
*   The application requires a response from a request.
*   The application uses a library that only provides synchronous methods for I/O.
*   An external library performs synchronous I/O operations internally. A single synchronous I/O call can block an entire call chain.

Visit the following resources to learn more:

- [@article@What is Synchronous I/O antipattern?](https://learn.microsoft.com/en-us/azure/architecture/antipatterns/synchronous-io/)

## Task Queues

# Task Queues

Tasks queues receive tasks and their related data, runs them, then delivers their results. They can support scheduling and can be used to run computationally-intensive jobs in the background.

[Celery](https://docs.celeryproject.org/en/stable/) has support for scheduling and primarily has python support.

Visit the following resources to learn more:

- [@article@Celery - Distributed Task Queue](https://docs.celeryq.dev/en/stable/)

## Tcp

# TCP

TCP (Transmission Control Protocol) is a connection-oriented, reliable, and ordered protocol used for transmitting data over an IP network. It establishes a connection between a sender and receiver before data transfer begins, ensures that data packets arrive in the correct sequence without errors, and provides mechanisms for retransmission of lost packets and flow control to manage network congestion.

Visit the following resources to learn more:

- [@opensource@What Is TCP?](https://github.com/donnemartin/system-design-primer#transmission-control-protocol-tcp)
- [@article@What is the difference between HTTP protocol and TCP protocol?](https://www.quora.com/What-is-the-difference-between-HTTP-protocol-and-TCP-protocol)
- [@article@Networking for game programming](http://gafferongames.com/networking-for-game-programmers/udp-vs-tcp/)
- [@article@Key differences between TCP and UDP protocols](http://www.cyberciti.biz/faq/key-differences-between-tcp-and-udp-protocols/)
- [@article@Difference between TCP and UDP](http://stackoverflow.com/questions/5970383/difference-between-tcp-and-udp)
- [@article@Transmission control protocol](https://en.wikipedia.org/wiki/Transmission_Control_Protocol)
- [@article@User datagram protocol](https://en.wikipedia.org/wiki/User_Datagram_Protocol)
- [@article@Scaling memcache at Facebook](http://www.cs.bu.edu/~jappavoo/jappavoo.github.com/451/papers/memcache-fb.pdf)

## Throttling

# Throttling

Control the consumption of resources used by an instance of an application, an individual tenant, or an entire service. This can allow the system to continue to function and meet service level agreements, even when an increase in demand places an extreme load on resources.

Visit the following resources to learn more:

- [@article@Throttling pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/throttling)

## Udp

# UDP

UDP is connectionless. Datagrams (analogous to packets) are guaranteed only at the datagram level. Datagrams might reach their destination out of order or not at all. UDP does not support congestion control. Without the guarantees that TCP support, UDP is generally more efficient.

UDP can broadcast, sending datagrams to all devices on the subnet. This is useful with DHCP because the client has not yet received an IP address, thus preventing a way for TCP to stream without the IP address.

UDP is less reliable but works well in real time use cases such as VoIP, video chat, streaming, and realtime multiplayer games.

Use UDP over TCP when:

*   You need the lowest latency
*   Late data is worse than loss of data
*   You want to implement your own error correction

Visit the following resources to learn more:

- [@article@Networking for game programming](http://gafferongames.com/networking-for-game-programmers/udp-vs-tcp/)
- [@article@Key differences between TCP and UDP protocols](http://www.cyberciti.biz/faq/key-differences-between-tcp-and-udp-protocols/)
- [@article@Difference between TCP and UDP](http://stackoverflow.com/questions/5970383/difference-between-tcp-and-udp)
- [@article@Transmission control protocol](https://en.wikipedia.org/wiki/Transmission_Control_Protocol)
- [@article@User datagram protocol](https://en.wikipedia.org/wiki/User_Datagram_Protocol)
- [@article@Scaling memcache at Facebook](http://www.cs.bu.edu/~jappavoo/jappavoo.github.com/451/papers/memcache-fb.pdf)

## Usage Monitoring

# Usage Monitoring

Usage monitoring tracks how the features and components of an application are used. An operator can use the gathered data to:

*   Determine which features are heavily used and determine any potential hotspots in the system. High-traffic elements might benefit from functional partitioning or even replication to spread the load more evenly. An operator can also use this information to ascertain which features are infrequently used and are possible candidates for retirement or replacement in a future version of the system.
*   Obtain information about the operational events of the system under normal use. For example, in an e-commerce site, you can record the statistical information about the number of transactions and the volume of customers that are responsible for them. This information can be used for capacity planning as the number of customers grows.
*   Detect (possibly indirectly) user satisfaction with the performance or functionality of the system. For example, if a large number of customers in an e-commerce system regularly abandon their shopping carts, this might be due to a problem with the checkout functionality.
*   Generate billing information. A commercial application or multitenant service might charge customers for the resources that they use.
*   Enforce quotas. If a user in a multitenant system exceeds their paid quota of processing time or resource usage during a specified period, their access can be limited or processing can be throttled.

Visit the following resources to learn more:

- [@article@Usage Monitoring](https://learn.microsoft.com/en-us/azure/architecture/best-practices/monitoring#usage-monitoring)
- [@feed@Explore top posts about Monitoring](https://app.daily.dev/tags/monitoring?ref=roadmapsh)

## Valet Key

# Valet Key

Use a token that provides clients with restricted direct access to a specific resource, in order to offload data transfer from the application. This is particularly useful in applications that use cloud-hosted storage systems or queues, and can minimize cost and maximize scalability and performance.

Visit the following resources to learn more:

- [@article@Valet Key pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/valet-key)

## Valet Key

# Valet Key

Use a token that provides clients with restricted direct access to a specific resource, in order to offload data transfer from the application. This is particularly useful in applications that use cloud-hosted storage systems or queues, and can minimize cost and maximize scalability and performance.

Visit the following resources to learn more:

- [@article@Valet Key pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/valet-key)

## Visualization  Alerts

# Visualization and Alerts

An important aspect of any monitoring system is the ability to present the data in such a way that an operator can quickly spot any trends or problems. Also important is the ability to quickly inform an operator if a significant event has occurred that might require attention.

Visit the following resources to learn more:

- [@article@Visualize Data and Raise Alerts](https://learn.microsoft.com/en-us/azure/architecture/best-practices/monitoring#visualizing-data-and-raising-alerts)

## Weak Consistency

# Weak Consistency

After an update is made to the data, it is not guaranteed that any subsequent read operation will immediately reflect the changes made. The read may or may not see the recent write.

Visit the following resources to learn more:

- [@article@Consistency Patterns in Distributed Systems](https://cs.fyi/guide/consistency-patterns-week-strong-eventual/)

## Web Server Caching

# Web Server Caching

[Reverse proxies](https://github.com/donnemartin/system-design-primer#reverse-proxy-web-server) and caches such as [Varnish](https://www.varnish-cache.org/) can serve static and dynamic content directly. Web servers can also cache requests, returning responses without having to contact application servers.

## What Is System Design

# What is System Design?

System design is the process of defining the elements of a system, as well as their interactions and relationships, in order to satisfy a set of specified requirements.

It involves taking a problem statement, breaking it down into smaller components and designing each component to work together effectively to achieve the overall goal of the system. This process typically includes analyzing the current system (if any) and determining any deficiencies, creating a detailed plan for the new system, and testing the design to ensure that it meets the requirements. It is an iterative process that may involve multiple rounds of design, testing, and refinement.

In software engineering, system design is a phase in the software development process that focuses on the high-level design of a software system, including the architecture and components.

Visit the following resources to learn more:

- [@article@System Design: Complete Guide with Patterns, Examples, and Techniques](https://swimm.io/learn/system-design/system-design-complete-guide-with-patterns-examples-and-techniques)
- [@article@A comprehensive guide to system design](https://www.crio.do/blog/a-comprehensive-guide-to-system-design/)

## Wide Column Store

# Wide Column Store

A wide column store's basic unit of data is a column (name/value pair). A column can be grouped in column families (analogous to a SQL table). Super column families further group column families. You can access each column independently with a row key, and columns with the same row key form a row. Each value contains a timestamp for versioning and for conflict resolution.

Google introduced Bigtable as the first wide column store, which influenced the open-source HBase often-used in the Hadoop ecosystem, and Cassandra from Facebook. Stores such as BigTable, HBase, and Cassandra maintain keys in lexicographic order, allowing efficient retrieval of selective key ranges.

Visit the following resources to learn more:

- [@article@Bigtable architecture](https://www.read.seas.harvard.edu/~kohler/class/cs239-w08/chang06bigtable.pdf)

## Write Behind

# Write-behind

In write-behind, the application does the following:

*   Add/update entry in cache
*   Asynchronously write entry to the data store, improving write performance

Disadvantages of write-behind:
------------------------------

*   There could be data loss if the cache goes down prior to its contents hitting the data store.
*   It is more complex to implement write-behind than it is to implement cache-aside or write-through.

![Scalability, availability, stability, patterns](https://i.imgur.com/XDsb7RS.png)

Visit the following resources to learn more:

- [@article@Scalability, availability, stability, patterns](http://www.slideshare.net/jboner/scalability-availability-stability-patterns/)

## Write Through

# Write-through

The application uses the cache as the main data store, reading and writing data to it, while the cache is responsible for reading and writing to the database:

*   Application adds/updates entry in cache
*   Cache synchronously writes entry to data store
*   Return

Application code:

    set_user(12345, {"foo": "bar"})
    

Cache code:

    def set_user(user_id, values):
        user = db.query("UPDATE Users WHERE id = {0}", user_id, values)
        cache.set(user_id, user)
    

Write-through is a slow overall operation due to the write operation, but subsequent reads of just written data are fast. Users are generally more tolerant of latency when updating data than reading data. Data in the cache is not stale.

Disadvantages
-------------

*   When a new node is created due to failure or scaling, the new node will not cache entries until the entry is updated in the database. Cache-aside in conjunction with write through can mitigate this issue.
*   Most data written might never be read, which can be minimized with a TTL.

![Write through](https://i.imgur.com/Ujf0awN.png)

Visit the following resources to learn more:

- [@article@Scalability, availability, stability, patterns](http://www.slideshare.net/jboner/scalability-availability-stability-patterns/)
