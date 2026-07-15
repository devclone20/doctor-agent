# Aspnet Core Roadmap

## Activemq

# ActiveMQ

ActiveMQ is an open-source message broker written in Java that implements the Java Message Service (JMS) API. It can be used to send and receive messages between different applications in a loosely coupled, asynchronous manner. ActiveMQ supports a variety of messaging protocols, including JMS, AMQP, STOMP, MQTT, and OpenWire.

In the context of an [ASP.NET](http://ASP.NET) application, ActiveMQ can be used to send and receive messages to and from other systems. For example, it can be used to send messages from a web application to a background service, or to send messages between different microservices.

Visit the following resources to learn more:

- [@article@What Is ActiveMQ And How Can You Use It?](https://www.c-sharpcorner.com/article/what-is-activemq-and-how-can-you-use-it/)
- [@article@Messaging with .NET and ActiveMQ](https://remark.wordpress.com/articles/messaging-with-net-and-activemq/)
- [@article@Messaging with ActiveMQ and ASP.NET](https://havret.io/activemq-artemis-net-core)

## Api Clients And Communication

# API Clients

API clients in [ASP.NET](http://ASP.NET) are software libraries that allow applications to interact with external APIs. They provide a set of methods and classes that make it easy to send requests to an API and process the responses.

API clients can be used to access a wide variety of services, such as web services, cloud services, and social media platforms. They can be used to perform tasks such as fetching data, posting updates, and deleting resources.

API clients in [ASP.NET](http://ASP.NET) are typically built using the HttpClient class, which is part of the System.Net.Http namespace. This class provides a set of methods for sending HTTP requests and receiving HTTP responses.

Visit the following resources to learn more:

- [@article@How to Call a Web API From a .NET Client](https://learn.microsoft.com/en-us/aspnet/web-api/overview/advanced/calling-a-web-api-from-a-net-client)
- [@article@Overview of Web API REST Service in ASP.NET](https://www.c-sharpcorner.com/article/consuming-asp-net-web-api-rest-service-in-asp-net-mvc-using-http-client/)
- [@article@Building an ASP.NET Web API With ASP.NET](https://www.toptal.com/asp-dot-net/asp-net-web-api-tutorial)

## App Settings And Configs

# App Settings and Configurations

In the [ASP.NET](http://ASP.NET) Core framework, app settings and configurations refer to the process of storing and managing application-specific settings and configuration data.

*   **App Settings** refers to the key-value pairs of data that an application uses to configure its behavior, such as database connection strings, api keys, or other settings. These settings are typically stored in configuration files, such as `appsettings.json`, `appsettings.development.json`, or `appsettings.production.json`, and can be accessed using the IConfiguration interface.
    
*   **Configurations** refer to the process of loading and managing the app settings, including specifying the source of the settings and the format of the configuration files. In [ASP.NET](http://ASP.NET) Core, the `Startup` class is responsible for configuring the application's settings, and typically loads configuration data from various sources, such as JSON files, environment variables, or command-line arguments.

Visit the following resources to learn more:

- [@article@What is Azure App Configuration?](https://learn.microsoft.com/en-us/azure/azure-app-configuration/overview)
- [@article@What are App Configurations and how do I work with them?](https://support.procore.com/faq/what-are-app-configurations)
- [@article@Configuration & AppSettings](https://docs.servicestack.net/appsettings)

## Aspnet Core Basics

# Basics of ASP.NET Core

[ASP.NET](http://ASP.NET) Core is a open-source, cross-platform web framework for building modern web applications using .NET. Some of the basics of [ASP.NET](http://ASP.NET) Core are Cross-platform, Open-source, Modular, High performance, MVC pattern, Dependency Injection, Middleware, Razor Pages and Razor Components, EF Core.

Visit the following resources to learn more:

- [@article@ASP.NET documentation](https://learn.microsoft.com/en-us/aspnet/core/?view=aspnetcore-7.0)
- [@article@ASP.NET Core Tutorial](https://www.tutorialspoint.com/asp.net_core/index.htm)
- [@article@Learn ASP.NET Core from Scratch](https://www.tutorialsteacher.com/core)
- [@feed@Explore top posts about ASP.NET](https://app.daily.dev/tags/aspnet?ref=roadmapsh)

## Autofac

# Autofac

Autofac is an open-source dependency injection framework for .NET. It is designed to make it easier to manage the dependencies of an application by automatically resolving and managing the lifetime of objects and their dependencies.

Autofac uses a technique called "component registration" to define the objects and dependencies of an application. This is done by creating instances of the `ContainerBuilder` class and using its methods to register types, instances and factories. Then, the `Build()` method is called to create an instance of the `IContainer` interface, which can be used to resolve dependencies throughout the application.

Visit the following resources to learn more:

- [@official@Getting started with Autofac](https://autofac.org/)
- [@article@Autofac’s Documentation](https://autofac.readthedocs.io/en/latest/)
- [@article@Dependency Injection with Autofac](https://www.codeproject.com/Articles/25380/Dependency-Injection-with-Autofac)

## Autofixture

# AutoFixture

AutoFixture is an open-source .NET library designed to minimize the 'Arrange' phase of your unit tests by creating object instances automatically with dummy data. It helps reduce boilerplate code and makes tests easier to maintain.

Visit the following resources to learn more:

- [@official@Quick start to AutoFixture](https://autofixture.github.io/docs/quick-start/)

## Automapper

# AutoMapper

AutoMapper is a library for .NET that allows you to easily map between objects of different types. It is particularly useful when working with domain models and data transfer objects (DTOs) in a layered architecture. It can also be used to map between different versions of an object, or to map between objects in different formats, such as JSON and XML.

AutoMapper uses a convention-based approach to mapping, which means that it automatically maps properties with the same name and type from one object to another. It also provides a fluent API for configuring more complex mappings, such as ignoring certain properties, using custom logic to map properties, or mapping properties based on a value in another property.

Visit the following resources to learn more:

- [@article@What is Automapper in ASP.NET?](https://www.simplilearn.com/tutorials/asp-dot-net-tutorial/automapper-in-c-sharp)
- [@article@Getting Started with AutoMapper in ASP.NET](https://code-maze.com/automapper-net-core/)
- [@article@Examples of AutoMapper in ASP.NET](https://dotnettutorials.net/lesson/automapper-in-c-sharp/)

## Azure Pipelines

# Azure Pipelines

Azure Pipelines is a continuous integration and continuous delivery (CI/CD) platform that allows developers to automate the process of building, testing, and deploying code. It is a part of the Azure DevOps suite of tools and can be used to automate the software development process for various languages and platforms, including [ASP.NET](http://ASP.NET).

In [ASP.NET](http://ASP.NET), Azure Pipelines can be used to automate various tasks related to the development, testing, and deployment of [ASP.NET](http://ASP.NET) applications. For example, you can use Azure Pipelines to automatically build, test, and deploy an [ASP.NET](http://ASP.NET) application to a hosting provider, such as Azure or AWS, every time you push code to your source control repository.

Visit the following resources to learn more:

- [@article@Deploy ASP.NET Apps with Azure Pipelines](https://learn.microsoft.com/en-us/training/modules/deploy-aspnet-apps-azure-app-service-pipelines/)
- [@article@Build ASP.NET apps with .NET Framework](https://learn.microsoft.com/en-us/azure/devops/pipelines/apps/aspnet/build-aspnet-4?view=azure-devops)
- [@article@How to Build, test & deploy .NET Apps](https://learn.microsoft.com/en-us/azure/devops/pipelines/ecosystems/dotnet-core?view=azure-devops&tabs=dotnetfive)
- [@feed@Explore top posts about Azure](https://app.daily.dev/tags/azure?ref=roadmapsh)

## Azure Service Bus

# Azure Service Bus

Azure Service Bus is a scalable and reliable messaging platform that can handle a high volume of messages, it's also easy to use, has a lot of features like subscription, Topics, Dead Letter, and easy to integrate with other Azure services, and it's a managed service which means Microsoft takes care of the infrastructure and scaling. However, it's worth noting that Azure Service Bus is a paid service and the cost will depend on the number of messages and the size of the data that you are sending and receiving.

Visit the following resources to learn more:

- [@article@Getting Started With Azure Service Bus and ASP.NET Core](https://www.c-sharpcorner.com/article/get-started-with-azure-service-bus-queues-asp-net-core-part-1/)
- [@article@How to Send & receive messages from Azure Service Bus queue (.NET)?](https://learn.microsoft.com/en-us/azure/service-bus-messaging/service-bus-dotnet-get-started-with-queues?tabs=passwordless)
- [@article@What is Azure Service Bus?](https://learn.microsoft.com/en-us/azure/service-bus-messaging/service-bus-messaging-overview)
- [@feed@Explore top posts about Azure](https://app.daily.dev/tags/azure?ref=roadmapsh)

## Benchmarknet

# BenchmarkDotNet

BenchmarkDotNet is an open-source library for .NET that provides a simple and easy-to-use API for benchmarking the performance of code. It allows you to measure the performance of methods, classes, and entire assemblies, and provides a rich set of features for analyzing and comparing the results. It provides a wide range of performance metrics, such as CPU cycles, memory allocation, and garbage collection, and can generate detailed reports that include charts, tables, and source code highlighting. It has support for multithreading and a built-in support for .NET Core.

Visit the following resources to learn more:

- [@article@Benchmarking .NET Using BenchmarkDotNet](https://www.codemag.com/Article/2209061/Benchmarking-.NET-6-Applications-Using-BenchmarkDotNet-A-Deep-Dive)
- [@video@Benchmarking ASP.NET Applications with .NET Crank](https://www.youtube.com/watch?v=2IgfrnG-128)
- [@video@Intro to BenchmarkDotNet](https://www.youtube.com/watch?v=mmza9x3QxYE)

## Blazor

# Blazor

Blazor is a framework for building web applications using C# and .NET that runs in the browser via WebAssembly. It allows developers to write C# code that runs directly in the browser, eliminating the need for JavaScript.

Blazor comes in two flavors:

*   Blazor WebAssembly, a client-side solution that allows you to run C# code directly in the browser using WebAssembly. The app is executed on the client-side and can work offline, it can also interact with JavaScript and access the browser's DOM.
*   Blazor Server, a server-side solution that allows you to run C# code on the server and update the UI in real-time. The app is executed on the server-side and requires an active connection to the server to function.

Visit the following resources to learn more:

- [@article@Guide to ASP.NET Core Blazor](https://learn.microsoft.com/en-us/aspnet/core/blazor/?view=aspnetcore-7.0)
- [@article@What Is Blazor And How It Works?](https://www.c-sharpcorner.com/article/what-is-blazor-and-how-does-it-works/)
- [@video@Tutorial of ASP.NET Core Blazor](https://www.youtube.com/watch?v=LyO4zj6NRuc)
- [@feed@Explore top posts about Blazor](https://app.daily.dev/tags/blazor?ref=roadmapsh)

## Bogus

# Bogus

## C

# C#

C# is a modern coding language that was developed by Microsoft that focuses on applying the coding style to C++ and making it so that way it's more condensed and simple. It's similar to Java by both being static, strong, and manifestive languages. Both use the System's prebuilt class to do certain features like printing output to the screen, etc.C#, like Java, also contains a garbage collection, which removes lower-level maintenance code from the programmer.

Visit the following resources to learn more:

- [@article@C# official website?](https://learn.microsoft.com/en-us/dotnet/csharp/)
- [@video@C# Full Course - Learn C# 10 and .NET 6 in 7 hours](https://www.youtube.com/watch?v=q_F4PyW8GTg)
- [@feed@Explore top posts about C#](https://app.daily.dev/tags/csharp?ref=roadmapsh)

## Caching

# Caching

Caching is a technique of storing frequently used data or information in a local memory, for a certain time period. So, next time, when the client requests the same information, instead of retrieving the information from the database, it will give the information from the local memory. The main advantage of caching is that it improves the performance by reducing the processing burden.

Visit the following resources to learn more:

- [@article@Caching in ASP.Net](https://www.c-sharpcorner.com/UploadFile/2072a9/caching-in-Asp-Net/)
- [@article@Overview of caching in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/performance/caching/overview?view=aspnetcore-7.0)
- [@article@Intro to Data Caching in ASP.NET](https://www.tutorialspoint.com/asp.net/asp.net_data_caching.htm)

## Cassandra

# Cassandra

Apache Cassandra is a free and open-source, NoSQL, distributed, wide-column store, and high-performance database management system designed to handle large amounts of data across many commodity servers, providing high availability with no single point of failure. It is designed to handle large amounts of data across many commodity servers, providing high availability with no single point of failure.

Cassandra is a column-family store and it stores data in a structured format, using tables and columns. It is based on a data model that is similar to that of Google's Bigtable, and it provides a query language that is similar to SQL.

Visit the following resources to learn more:

- [@article@Introduction to Cassandra](https://www.tutorialspoint.com/cassandra/cassandra_introduction.htm)
- [@article@Overview of Cassandra in ASP.NET](https://www.spiceworks.com/tech/big-data/articles/what-is-cassandra/)
- [@feed@Explore top posts about Apache Cassandra](https://app.daily.dev/tags/apache-cassandra?ref=roadmapsh)

## Change Tracker Api

# Change Tracker API

The Change Tracker API is a feature of ORM (Object-Relational Mapping) frameworks, such as Entity Framework Core, that allows developers to track changes to entities and automatically persist them to the database.

The Change Tracker API is typically exposed through the context class, which is the main class that manages the connection to the database and provides access to the entities.

Visit the following resources to learn more:

- [@article@Change Tracking in EF Core](https://learn.microsoft.com/en-us/ef/core/change-tracking/)
- [@article@Intro to Change Tracking](https://www.oreilly.com/library/view/programming-entity-framework/9781449331825/ch05.html)
- [@article@ChangeTracker in Entity Framework Core](https://www.entityframeworktutorial.net/efcore/changetracker-in-ef-core.aspx)

## Ci  Cd

# CI CD

CI/CD (Continuous Integration/Continuous Deployment) is a software development practice that involves automating the process of building, testing, and deploying code changes. It is a popular practice among software development teams, as it helps to ensure that code changes are integrated, tested, and deployed quickly and reliably.

In the context of [ASP.NET](http://ASP.NET), CI/CD can be used to automate various tasks related to the development, testing, and deployment of [ASP.NET](http://ASP.NET) applications. For example, you can use CI/CD to automatically build, test, and deploy an [ASP.NET](http://ASP.NET) application to a hosting provider, such as Azure or AWS, every time you push code to your source control repository.

Visit the following resources to learn more:

- [@article@How to reate a CI/CD pipeline for ASP.NET?](https://www.azuredevopslabs.com/labs/vstsextend/azuredevopsprojectdotnet/)
- [@video@Building a CI/CD Pipeline in Azure DevOps for ASP.NET Core](https://youtube.com/watch?v=eOQL0nXQlLs)
- [@feed@Explore top posts about CI/CD](https://app.daily.dev/tags/cicd?ref=roadmapsh)

## Circle Ci

# CircleCI

CircleCI is a cloud-based continuous integration and continuous delivery (CI/CD) platform that allows developers to automate the process of building, testing, and deploying code. It is a popular platform that supports a wide range of languages and frameworks, including [ASP.NET](http://ASP.NET).

In [ASP.NET](http://ASP.NET), CircleCI can be used to automate various tasks related to the development, testing, and deployment of [ASP.NET](http://ASP.NET) applications. For example, you can use CircleCI to automatically build, test, and deploy an [ASP.NET](http://ASP.NET) application to a hosting provider, such as Azure or AWS, every time you push code to your source control repository.

Visit the following resources to learn more:

- [@official@Building and testing an ASP.NET apps with CircleCI](https://circleci.com/blog/building-and-testing-an-asp-net-core-application/)
- [@article@How to Setup CircleCI for ASP.NET project](https://discuss.circleci.com/t/setup-circleci-for-asp-net-project/33796s)
- [@feed@Explore top posts about CI/CD](https://app.daily.dev/tags/cicd?ref=roadmapsh)

## Cloud

# Cloud

Cloud in the context of [ASP.NET](http://ASP.NET) refers to the use of cloud computing services to host and run [ASP.NET](http://ASP.NET) web applications. Cloud computing is a model of delivering computing resources (such as servers, storage, and applications) over the internet on a pay-per-use basis.

In the case of [ASP.NET](http://ASP.NET), cloud providers such as Microsoft Azure, Amazon Web Services (AWS), and Google Cloud Platform (GCP) offer services specifically tailored to host and run [ASP.NET](http://ASP.NET) web applications. These services include virtual machines, web roles, and serverless computing, which can be used to deploy and run [ASP.NET](http://ASP.NET) web applications in the cloud.

Visit the following resources to learn more:

- [@article@Building a .NET Cloud Application](https://www.c-sharpcorner.com/article/building-the-net-cloud-application/)
- [@article@How to make a .NET Cloud Application?](https://dotnet.microsoft.com/en-us/apps/cloud)
- [@article@Getting started with Cloud](https://aws.amazon.com/free/)
- [@feed@Explore top posts about Cloud](https://app.daily.dev/tags/cloud?ref=roadmapsh)

## Code First  Migrations

# Code First Migrations

Code First Migrations is a feature of Entity Framework that enables you to change the model classes in your application and then propagate those changes to the database. When you use Code First Migrations, Entity Framework generates the necessary SQL commands to update the database schema to match the model classes.

To use Code First Migrations, you need to enable it in your Entity Framework application. This can be done by adding a reference to the Entity Framework Migrations NuGet package, and then enabling Migrations in your application.

Visit the following resources to learn more:

- [@article@What is a Code First Migration?](https://www.entityframeworktutorial.net/code-first/what-is-code-first.aspx)
- [@article@Example for Code First Migrations](https://learn.microsoft.com/en-us/ef/ef6/modeling/code-first/migrations/)
- [@article@Code First Migrations in Entity Framework](https://www.c-sharpcorner.com/UploadFile/26b237/code-first-migrations-in-entity-framework/)

## Constraints

# Constraints

Database constraints are rules that are used to limit the data that can be stored in a database table. These constraints can be used to ensure the integrity and accuracy of the data in the table, and they can be used to enforce business rules or other requirements. For example, a constraint might be used to ensure that a column only contains positive numbers, or to ensure that a column always has a unique value. Constraints can be specified at the time a table is created, or they can be added to an existing table. Some common types of constraints include primary keys, foreign keys, and NOT NULL constraints.

Visit the following resources to learn more:

- [@article@Constraints of SQL](https://www.educative.io/courses/database-design-fundamentals/m7JnY9Xm6Qp)
- [@article@Constraints in DBMS](https://beginnersbook.com/2015/04/constraints-in-dbms/)

## Coravel

# Coravel

Coravel is an open-source, lightweight library for .NET that allows you to easily perform background processing and scheduling in your [ASP.NET](http://ASP.NET) Core application. It provides a simple and elegant way to schedule tasks, run background jobs, and manage queues in your application.

Coravel is inspired by Laravel's task scheduler and it's built on top of the .NET Core built-in Dependency Injection. It uses a fluent API to schedule tasks, allowing you to easily specify the frequency, start time, and end time of the task. It also provides a simple way to queue and process background jobs, allowing you to easily process large amounts of data or perform long-running tasks.

Visit the following resources to learn more:

- [@article@Documentation of Coravel](https://docs.coravel.net/)
- [@video@ASP.NET Task Scheduling with Coravel](https://www.youtube.com/watch?v=vu0fxlWl0wo)
- [@video@How to Run a .Net Console App with Coravel](https://www.youtube.com/watch?v=KQpw_OYkKq8)

## Cosmos Db

# CosmosDB

Visit the following resources to learn more:

- [@article@What is Azure Cosmos DB?](https://intellipaat.com/blog/what-is-azure-cosmos-db/)
- [@article@Cosmos DB, Its Features, Benefits, Pricing etc](https://stackify.com/what-is-azure-cosmos-db/)
- [@article@Getting started with Cosmos DB](https://acloudguru.com/blog/engineering/azure-cosmos-db-lets-you-focus-on-the-good-stuff)

## Couchdb

# CouchDB

CouchDB is an open-source, NoSQL document database designed for the web. It uses a document-oriented data model, which means that it stores data in semi-structured JSON format, and it is designed to be simple and easy to use. CouchDB provides a built-in web interface, called Futon, which can be used to interact with the database, and it also provides an HTTP API that can be used to interact with the database from an [ASP.NET](http://ASP.NET) application.

In an [ASP.NET](http://ASP.NET) application, CouchDB can be used as a data store to persist and retrieve application data. There are several libraries available for integrating CouchDB with an [ASP.NET](http://ASP.NET) application, such as Couchbase, which provides a .NET client for CouchDB that can be used to interact with the CouchDB server from within an [ASP.NET](http://ASP.NET) application.

Visit the following resources to learn more:

- [@article@CouchDB in ASP.NET Core Application](https://www.c-sharpcorner.com/article/crud-operation-to-couchdb-via-rest-api-in-asp-net-core-application/)
- [@article@Use CouchDB with .NET](https://stackoverflow.com/questions/1050152/use-couchdb-with-net)

## Cypress

# Cypress

Cypress is an open-source end-to-end testing framework for web applications, it's built on top of JavaScript and provides a set of APIs that allows developers to automate browser interactions. It's commonly used for testing web applications, as it can be used to automate browser-based tests and assert that the application behaves as expected. Cypress for .NET is not built on top of the .NET Core runtime and it does not provide bindings for C# or any other .NET languages, it's built on top of JavaScript and can be run in the browser.

Visit the following resources to learn more:

- [@official@Overview of Cypress](https://www.cypress.io/)
- [@article@Cypress - End To End Testing Tool](https://www.c-sharpcorner.com/article/getting-started-with-cypress-io/)
- [@feed@Explore top posts about Cypress](https://app.daily.dev/tags/cypress?ref=roadmapsh)

## Dapper

# Dapper

Dapper is a lightweight object-relational mapper (ORM) for the .NET framework. It is designed to provide fast and simple access to data stored in a database, by mapping the data to objects in the application.

Dapper helps you to write efficient and concise code for interacting with databases, without the need for a full-featured ORM like Entity Framework. It provides a set of extension methods for the IDbConnection interface, which you can use to execute SQL queries and map the results to strongly-typed objects.

Visit the following resources to learn more:

- [@opensource@The official Dapper website](https://github.com/StackExchange/Dapper)
- [@article@The Dapper Documentation](https://dappertutorial.net/)

## Dapr

# Dapr

Dapr (Distributed Application Runtime) is an open-source, portable runtime that makes it easy to build microservices-based applications that run on the cloud and edge. It provides a set of building blocks for building microservices, including service discovery, state management, pub-sub messaging, and more. It is designed to be language-agnostic, so it can be used with any programming language, including .NET.

Visit the following resources to learn more:

- [@article@Get started with Dapr](https://learn.microsoft.com/en-us/dotnet/architecture/dapr-for-net-developers/getting-started)
- [@article@Building an event-driven .NET Core app with Dapr](https://medium.com/polarsquad/building-an-event-driven-net-core-app-with-dapr-58cc83ab120b)

## Data Structures And Algorithms

# Data Structures

As the name indicates, a **Data Structure** is a way of organizing the data in the **memory** so it can be used efficiently. Some common data structures are array, linked list, stack, hashtable, queue, tree, heap, and graph.

Visit the following resources to learn more:

- [@article@C# resources](https://dev.to/adavidoaiei/fundamental-data-structures-and-algorithms-in-c-4ocf)
- [@article@Interview Questions about Data Structures](https://www.csharpstar.com/csharp-algorithms/)
- [@video@Data Structures Illustrated](https://www.youtube.com/watch?v=9rhT3P1MDHk&list=PLkZYeFmDuaN2-KUIv-mvbjfKszIGJ4FaY)
- [@feed@Explore top posts about Algorithms](https://app.daily.dev/tags/algorithms?ref=roadmapsh)

## Database Design Basics

# Database design basics

Database Design is a collection of processes that facilitate the designing, development, implementation and maintenance of enterprise data management systems. Properly designed database are easy to maintain, improves data consistency and are cost effective in terms of disk storage space. The main objectives of database design in DBMS are to produce logical and physical designs models of the proposed database system.

Visit the following resources to learn more:

- [@article@Database design basics](https://support.microsoft.com/en-us/office/database-design-basics-eb2159cf-1e30-401a-8084-bd4f9c9ca1f5)
- [@video@Database Design Course](https://www.youtube.com/watch?v=ztHopE5Wnpc)
- [@feed@Explore top posts about Database](https://app.daily.dev/tags/database?ref=roadmapsh)

## Database Fundamentals

# Database fundamentals

A database is a collection of useful data of one or more related organizations structured in a way to make data an asset to the organization. A database management system is a software designed to assist in maintaining and extracting large collections of data in a timely fashion.

A **Relational database** is a type of database that stores and provides access to data points that are related to one another. Relational databases store data in a series of tables.

**NoSQL databases** offer data storage and retrieval that is modelled differently to "traditional" relational databases. NoSQL databases typically focus more on horizontal scaling, eventual consistency, speed and flexibility and is used commonly for big data and real-time streaming applications.

Visit the following resources to learn more:

- [@article@Oracle: What is a Database?](https://www.oracle.com/database/what-is-database/)
- [@article@Prisma.io: What are Databases?](https://www.prisma.io/dataguide/intro/what-are-databases)
- [@article@Intro To Relational Databases](https://www.udacity.com/course/intro-to-relational-databases--ud197)
- [@article@NoSQL Explained](https://www.mongodb.com/nosql-explained)
- [@video@What is Relational Database](https://youtu.be/OqjJjpjDRLc)
- [@video@How do NoSQL Databases work](https://www.youtube.com/watch?v=0buKQHokLK8)
- [@feed@Explore top posts about Database](https://app.daily.dev/tags/database?ref=roadmapsh)

## Databases

# Databases

In an [ASP.NET](http://ASP.NET) application, there are several types of databases that can be used to store and retrieve data. Some of the most commonly used databases include:

*   Relational databases
*   NoSQL databases
*   In-memory databases
*   Embedded databases
*   Cloud-based databases

Each database type has its own set of features and use cases, and the choice of which database to use will depend on the specific requirements of the application.

Visit the following resources to learn more:

- [@article@ASP.NET Database Tutorial](https://www.guru99.com/insert-update-delete-asp-net.html)
- [@article@Introduction to Working with a Database in ASP.NET](https://learn.microsoft.com/en-us/aspnet/web-pages/overview/data/5-working-with-data)
- [@feed@Explore top posts about Backend Development](https://app.daily.dev/tags/backend?ref=roadmapsh)

## Dependency Injection

# Dependency Injection

Dependency injection (DI) is a software design pattern that is used to manage the dependencies of an application. It is a technique that allows developers to write loosely-coupled code, by separating the responsibility of creating and managing objects from the objects themselves.

In a typical implementation, a DI container is used to manage the dependencies of the application. The container is responsible for creating and managing instances of objects and their dependencies, and providing them to other objects as needed.

Visit the following resources to learn more:

- [@article@What is Dependency Injection?](https://stackoverflow.com/questions/130794/what-is-dependency-injection)
- [@article@Dependency Injection, It's Definition & principles](https://www.growin.com/blog/what-is-dependency-injection/)
- [@feed@Explore top posts about Dependency Injection](https://app.daily.dev/tags/dependency-injection?ref=roadmapsh)

## Di Containers

# DI Containers

A dependency injection (DI) container is a software component that is responsible for managing the dependencies of an application. It is used to create and manage instances of objects and their dependencies, and is particularly useful for implementing the Dependency Inversion Principle in software development.

A DI container typically consists of two main parts: a configuration API, which is used to register the types and their dependencies, and a resolution API, which is used to retrieve instances of the registered types. The DI container automatically resolves the dependencies of the objects it creates, and manages the lifetime of the objects and their dependencies.

Visit the following resources to learn more:

- [@article@What is DI Container?](https://www.dotnettricks.com/learn/dependencyinjection/what-is-ioc-container-or-di-container)
- [@article@Getting Started with DI Container](https://stackoverflow.com/questions/50718586/what-is-a-di-container)
- [@article@How to Use DI Container?](https://learn.userfrosting.com/services/the-di-container)
- [@feed@Explore top posts about Containers](https://app.daily.dev/tags/containers?ref=roadmapsh)

## Distributed Cache

# Distributed Cache

A distributed cache is a cache shared by multiple app servers, typically maintained as an external service to the app servers that access it. A distributed cache can improve the performance and scalability of an [ASP.NET](http://ASP.NET) Core app, especially when the app is hosted by a cloud service or a server farm.

Visit the following resources to learn more:

- [@article@Distributed caching in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/performance/caching/distributed?view=aspnetcore-7.0)
- [@article@What is a Distributed Cached?](https://hazelcast.com/glossary/distributed-cache/)
- [@video@Distributed Caching In ASP.NET Core With Redis](https://www.youtube.com/watch?v=Tt5zIKVMMbs)

## Distributed Lock

# Distributed Lock

## Docker

# Docker

Docker is a platform for developing, shipping, and running applications in containers. A container is a lightweight, standalone, and executable package of software that includes everything needed to run a piece of software, including the code, a runtime, system tools, libraries, and settings.

Docker allows developers to package their applications and dependencies into a container, which can then be easily deployed and run on any host machine with Docker installed. This makes it easy to run the same software on different environments, such as development, staging, and production, without worrying about compatibility issues.s

Visit the following resources to learn more:

- [@article@ASP.NET and Docker](https://www.tatvasoft.com/blog/asp-net-core-and-docker/)
- [@article@Introduction to .NET and Docker](https://learn.microsoft.com/en-us/dotnet/core/docker/introduction)
- [@video@What is Docker, Why use it?](https://www.youtube.com/watch?v=vmnvOITMoIg)
- [@feed@Explore top posts about Docker](https://app.daily.dev/tags/docker?ref=roadmapsh)

## Dynamo Db

# DynamoDB

Amazon DynamoDB is a fully-managed, NoSQL database service provided by Amazon Web Services (AWS) that can be used to store and retrieve large amounts of data. It is a highly-scalable, fast, and flexible NoSQL database service that supports both document and key-value data models.

DynamoDB is designed to handle extremely high levels of read and write throughput, and it automatically scales to accommodate the traffic of an application. It also provides built-in support for data replication, allowing data to be automatically spread across multiple availability zones for increased durability and availability.

Visit the following resources to learn more:

- [@article@Getting started with DynamoDB](https://aws.amazon.com/dynamodb/)
- [@article@Introduction to DynamoDB](https://cloudacademy.com/lab/introduction-dynamodb/)
- [@feed@Explore top posts about AWS DynamoDB](https://app.daily.dev/tags/aws-dynamodb?ref=roadmapsh)

## Easynetq

# EasyNetQ

EasyNetQ is a simple and easy-to-use .NET client for RabbitMQ, a popular open-source message broker. It provides a simple and fluent API for connecting to RabbitMQ, publishing and consuming messages, and managing message queues.

EasyNetQ supports a wide range of messaging patterns, such as publish-subscribe, request-response, and message-based sagas, and makes it easy to work with RabbitMQ's advanced features, such as message routing, message persistence, and message acknowledgements.

Visit the following resources to learn more:

- [@official@Overview of EasyNetQ](https://easynetq.com/)
- [@video@RabbitMQ with EasyNetQ Tutorials](https://www.youtube.com/watch?v=CqxV_Xn4PlI)

## Elastic Search

# Elasticsearch

Elasticsearch is a distributed, open-source search and analytics engine that can be used to index, search, and analyze large volumes of data quickly and in near real-time. It is built on top of the Apache Lucene library and can be used to perform full-text search, faceted search, and geospatial search, among other things.

Visit the following resources to learn more:

- [@article@Elasticsearch in ASP.NET Core](https://code-maze.com/elasticsearch-aspnet-core/)
- [@article@An Elasticsearch Tutorial for .NET Developers](https://www.toptal.com/dot-net/elasticsearch-dot-net-developers)
- [@article@How to integrate ElasticSearch in ASP.NET?](https://blexin.com/en/blog-en/how-to-integrate-elasticsearch-in-asp-net-core/)
- [@feed@Explore top posts about ELK](https://app.daily.dev/tags/elk?ref=roadmapsh)

## Entity Framework 2Nd Level Cache

# Entity Framework Cache

Entity Framework Core(EF Core) is a cross-platform version of the popular Entity Framework data access technology that is lightweight, extendable, and open source. It can be used as an object-relational mapper (O/RM), which can Allow .NET developers to use .NET objects to interact with a database and Removes the requirement for most of the data-access code that is generally required.

However, during peak loads, high-transaction .NET Core apps using EF Core have performance and scalability problems in the database tier. This is because, although you can scale the application layer by adding more application servers, you can't scale the database tier by adding more database servers.

Visit the following resources to learn more:

- [@article@Entity Framework 2nd Level Cache](https://www.gridgain.com/docs/latest/developers-guide/net-specific/net-entity-framework-cache)
- [@article@Caching In Entity Framework](https://www.c-sharpcorner.com/article/caching-in-entity-framework-ef-core-using-ncache/)
- [@video@What is Entity Framework?](https://www.youtube.com/watch?v=Z7713GBhi4k)

## Entity Framework Core

# Entity Framework Core

Entity Framework Core (EF Core) is an open-source Object-Relational Mapping (ORM) framework for .NET. It is a lightweight, cross-platform version of Entity Framework, the ORM framework that was part of the .NET Framework. EF Core allows developers to work with relational data using domain-specific objects, eliminating the need to write raw SQL statements. Instead, EF Core provides a set of APIs that can be used to interact with a database, providing a simple and efficient way to perform common database operations such as querying, inserting, updating, and deleting data.

Visit the following resources to learn more:

- [@article@Example of Entity Framework Core](https://learn.microsoft.com/en-us/ef/core/)
- [@article@Entity Framework Core Documentation](https://learn.microsoft.com/en-us/ef/)
- [@article@What are the Basics of Entity Framework Core?](https://www.jetbrains.com/dotnet/guide/tutorials/basics/entity-framework-core/)
- [@feed@Explore top posts about .NET](https://app.daily.dev/tags/.net?ref=roadmapsh)

## Fakeiteasy

# FakeitEasy

FakeItEasy is an open-source library for .NET that allows developers to create fake objects for use in unit testing, it is a powerful and easy-to-use mocking framework that provides a simple and intuitive syntax for creating fake objects and setting up fake behavior. In the context of [ASP.NET](http://ASP.NET), FakeItEasy can be used to create fake objects for testing web applications built using the [ASP.NET](http://ASP.NET) framework, it provides a simple and expressive syntax for creating fake objects and setting up fake behavior. FakeItEasy supports a wide range of testing frameworks, including MSTest, NUnit, and xUnit. FakeItEasy is lightweight and easy to use, making it a good choice for developers who are new to mocking and unit testing, it also provides a rich set of features, such as support for setting up fake behavior, making assertions on calls made to the fake objects, and more. It also has a wide range of extension points for customizing the fakes to suit different needs.

Visit the following resources to learn more:

- [@article@Easy mocking in C# code with FakeItEasy library](https://devislandblog.wordpress.com/2018/05/09/easy-mocking-in-c-code-with-fakeiteasy-library/)
- [@article@FakeItEasy when testing ASP.NET Core controllers](https://stackoverflow.com/questions/56170818/how-to-fake-an-interface-method-dynamically-with-fakeiteasy-when-testing-asp-net)

## Filters And Attributes

# Filters and Attributes

In the [ASP.NET](http://ASP.NET) Core framework, filters and attributes are used to add additional functionality to controllers and action methods, such as authentication, authorization, caching, and exception handling.

## Fluentvalidation

# FluentValidation

FluentValidation is an open-source library for .NET that provides a fluent, easy-to-use API for validating domain models. It allows developers to define validation rules using a fluent, chainable syntax. It separates validation rules into separate classes called validators, it supports async validation, custom validation rules, and cascading validation. It makes it easy to read and understand the validation logic, and it returns a ValidationResult object, which contains information about any validation errors that were found.

Visit the following resources to learn more:

- [@article@Documentations of FluentValidation](https://docs.fluentvalidation.net/en/latest/)
- [@article@FluentValidation in ASP.NET Core](https://docs.fluentvalidation.net/en/latest/aspnet.html)
- [@article@Overview of FluentValidation in ASP.NET Core](https://code-maze.com/fluentvalidation-in-aspnet/)

## Fluid

# Fluid

Fluid is a template engine for .NET that is based on the Fluid template language, it is similar to Liquid, but it's written in C#. It provides a simple and easy-to-use API for parsing and rendering templates, and supports a wide range of features such as variables, loops, conditionals, and functions. It also provides a wide range of built-in functions for working with strings, numbers, dates, and other types of data. It also supports advanced features such as scripting and metaprogramming. It is often used in web applications to separate the logic of the application from the presentation of the data, making it easy to change the appearance of the application without having to change the underlying code.

Visit the following resources to learn more:

- [@opensource@Overview of Fluid](https://github.com/sebastienros/fluid)

## Framework Basics

# Framework Basics

An ORM (Object-Relational Mapping) framework is a tool that maps the objects in an application to the database tables, allowing developers to work with the database using familiar, object-oriented concepts.

ORM frameworks are tools that map the objects in an application to the database tables, allowing developers to work with the database using familiar, object-oriented concepts such as Entities, Mapping, Context, Queries, Lazy Loading, Change Tracking, and Caching.

Visit the following resources to learn more:

- [@article@ORM Framework](https://www.h2kinfosys.com/blog/orm-framework/)
- [@article@What are Frameworks in ORM](https://www.killerphp.com/articles/what-are-orm-frameworks/)
- [@article@Essentials of ORM Framework](https://medium.com/@mikependon/the-essentials-of-orm-framework-in-your-software-development-837131efd91b)
- [@article@ORM Frameworks – What is an Object-Relational Mapping Framework](https://onlinecode.org/what-are-orm-frameworks/)

## Frameworks

# Frameworks

## General Development Skills

# General development skills

There are several skills that are generally considered to be important for working with .NET and C#:

*   Object-oriented programming: Understanding the concepts of classes, objects, inheritance, and polymorphism is essential for working with C# and the .NET Framework.
    
*   C# language: A strong understanding of the C# language, including its syntax, keywords, and built-in classes and types, is necessary for writing efficient and maintainable code.
    
*   .NET Framework: Familiarity with the .NET Framework, including the Common Language Runtime (CLR) and the Base Class Library (BCL), is important for understanding how C# code is executed and for utilizing the framework's many built-in features.
    
*   Web & Software development: Knowledge of web development technologies such as HTML, CSS, JavaScript, and [ASP.NET](http://ASP.NET) is important for creating web applications using C# and the .NET Framework and knowledge of software development methodologies such as Agile, Scrum, or Waterfall is also useful.
    
*   Database: Familiarity with database concepts and technologies, such as SQL and [ADO.NET](http://ADO.NET), is important for working with data in C# applications.
    
*   Cloud computing: Familiarity with cloud computing concepts and technologies, such as Azure, is becoming increasingly important for deploying and scaling C# applications.
    
*   DevOps: Understanding of DevOps concepts and practices, such as continuous integration and continuous deployment, is necessary for automating and streamlining the software development process.

Visit the following resources to learn more:

- [@video@Asp.net - Complete Tutorial](https://www.youtube.com/watch?v=kdPtNMb8tPw)
- [@video@Learn Cloud Computing](https://www.youtube.com/watch?v=eWwK2FKWp0g)
- [@video@DevOps Course for Beginners](https://www.youtube.com/watch?v=hQcFE0RD0cQ)
- [@feed@Explore top posts about Career](https://app.daily.dev/tags/career?ref=roadmapsh)

## Git   Version Control

# Git

[Git](https://git-scm.com/) is a free and open source distributed version control system designed to handle everything from small to very large projects with speed and efficiency.

Visit the following resources to learn more:

- [@article@Learn Git with Tutorials, News and Tips - Atlassian](https://www.atlassian.com/git)
- [@article@Git Cheat Sheet](https://cs.fyi/guide/git-cheatsheet)
- [@video@Git & GitHub Crash Course For Beginners](https://www.youtube.com/watch?v=SWYqp7iY_Tc)
- [@feed@Explore top posts about Git](https://app.daily.dev/tags/git?ref=roadmapsh)

## Github Actions

# GitHub Actions

GitHub Actions is a powerful and flexible automation platform that enables developers to create custom workflows for their software development lifecycle (SDLC) directly in their GitHub repository. It allows developers to automate various tasks, such as building, testing, and deploying code, directly from their GitHub repository.

In [ASP.NET](http://ASP.NET), GitHub Actions can be used to automate various tasks related to the development, testing, and deployment of [ASP.NET](http://ASP.NET) applications. For example, you can use GitHub Actions to automatically build, test, and deploy an [ASP.NET](http://ASP.NET) application to a hosting provider, such as Azure or AWS, every time you push code to your GitHub repository.

Visit the following resources to learn more:

- [@article@Intro to GitHub Actions for .NET](https://devblogs.microsoft.com/dotnet/dotnet-loves-github-actions/)
- [@article@Tutorial: Create a GitHub Action with .NET](https://learn.microsoft.com/en-us/dotnet/devops/create-dotnet-github-action)
- [@article@Building and testing .NET](https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-net)
- [@feed@Explore top posts about GitHub](https://app.daily.dev/tags/github?ref=roadmapsh)

## Github Gitlab Bitbucket

# Repo Hosting Services

There are different repository hosting services with the most famous one being GitHub, GitLab and BitBucket. I would recommend creating an account on GitHub because that is where most of the OpenSource work is done and most of the developers are.

Visit the following resources to learn more:

- [@opensource@GitHub: Where the world builds software](https://github.com)
- [@opensource@GitLab: Iterate faster, innovate together](https://gitlab.com)
- [@article@BitBucket: The Git solution for professional teams](https://bitbucket.com)

## Gitlab Cicd

# GitLab CI/CD

## Graphql Net

# GraphQL .NET

GraphQL is a query language for your API, it allows clients to define the structure of the data they need, and the server will return only the requested data. It is an alternative to RESTful web services, and it is gaining popularity because of its flexibility and efficiency.

Visit the following resources to learn more:

- [@article@Introduction to GraphQL .NET in ASP.NET](https://graphql-dotnet.github.io/docs/getting-started/introduction/)
- [@article@How to use GraphQL in .NET?](https://softchris.github.io/pages/dotnet-graphql.html)
- [@article@Building and consuming GraphQL API in ASP.NET](https://www.red-gate.com/simple-talk/development/dotnet-development/building-and-consuming-graphql-api-in-asp-net-core-5/)
- [@feed@Explore top posts about GraphQL](https://app.daily.dev/tags/graphql?ref=roadmapsh)

## Graphql

# GraphQL

GraphQL is a query language for your API that allows clients to define the structure of the data they need, and the server will return only the requested data. It is an alternative to RESTful web services, and it is gaining popularity because of its flexibility and efficiency.

In [ASP.NET](http://ASP.NET), GraphQL can be used to create web services that expose data in a more flexible and efficient way. There are several libraries available to implement GraphQL in an [ASP.NET](http://ASP.NET) application, such as [GraphQL.NET](http://GraphQL.NET), Hot Chocolate, and others. These libraries provide a set of classes and methods that make it easy to create a GraphQL schema, handle requests, and generate responses.

Visit the following resources to learn more:

- [@article@How to implement GraphQL in ASP.Net](https://blog.christian-schou.dk/how-to-implement-graphql-in-asp-net-core/)
- [@article@Intro to GraphQL](https://graphql-dotnet.github.io/docs/getting-started/introduction/)
- [@article@Developing API In .NET Core With GraphQL](https://www.c-sharpcorner.com/article/building-api-in-net-core-with-graphql2/)
- [@feed@Explore top posts about GraphQL](https://app.daily.dev/tags/graphql?ref=roadmapsh)

## Gridlify

# Gridify

Gridify offers a powerful string-based dynamic LINQ query language that is both simple and easy to use. Gridify is a dynamic LINQ library that simplifies the process of converting strings to LINQ queries. Gridify makes it effortless to apply filtering, sorting, and pagination using text-based data. It also has a Javascript/Typescript client to integrate the Gridify with the frontend tables.

Visit the following resources to learn more:

- [@opensource@Gridify Library](https://github.com/alirezanet/Gridify)
- [@article@Working with Dynamic Filters Using Gridify in .NET](https://levelup.gitconnected.com/working-with-dynamic-filters-using-gridify-in-net-6bba618dd9f8)

## Grpc

# gRPC

gRPC is a high-performance, open-source framework for building remote procedure call (RPC) APIs. It uses the Protocol Buffers data serialization format and the HTTP/2 protocol to create highly efficient and scalable APIs. gRPC supports a variety of programming languages, including C# and [ASP.NET](http://ASP.NET).

In [ASP.NET](http://ASP.NET), gRPC can be used to create high-performance, low-latency APIs for a variety of use cases. gRPC allows for bi-directional streaming of data, which can be useful for real-time applications such as gaming, financial trading, and more.

Visit the following resources to learn more:

- [@article@Overview for gRPC on .NET](https://learn.microsoft.com/en-us/aspnet/core/grpc/?view=aspnetcore-7.0)
- [@article@Getting Started with ASP.NET Core and gRPC](https://blog.jetbrains.com/dotnet/2021/07/19/getting-started-with-asp-net-core-and-grpc/)
- [@article@Create a gRPC client & server in ASP.NET](https://learn.microsoft.com/en-us/aspnet/core/tutorials/grpc/grpc-start?view=aspnetcore-7.0&tabs=visual-studio)
- [@feed@Explore top posts about gRPC](https://app.daily.dev/tags/grpc?ref=roadmapsh)

## Hangfire

# Hangfire

Hangfire is an open-source, lightweight library for .NET that allows you to easily perform background processing in your [ASP.NET](http://ASP.NET) application. It provides a simple and elegant way to run background jobs, schedule future tasks, and monitor the progress of your background jobs.

Hangfire uses a storage backend, such as SQL Server or Redis, to persist the state of your background jobs. This allows you to easily scale your background processing and to monitor and manage your background jobs, even if your application restarts or crashes.

Visit the following resources to learn more:

- [@article@Hangfire with ASP.NET Core](https://code-maze.com/hangfire-with-asp-net-core/)
- [@article@Intro to Hangfire](https://www.partech.nl/nl/publicaties/2021/05/a-beginners-guide-to-hangfire)
- [@article@How to use Hangfire with ASP.NET](https://blog.christian-schou.dk/how-to-use-hangfire-with-asp-net-core-5-0-api/)

## Hotchocolate

# Hot Chocolate

Hot Chocolate is a GraphQL server implementation for .NET and .NET Core. It is an open-source library that provides a simple and flexible way to build GraphQL APIs in [ASP.NET](http://ASP.NET).

Hot Chocolate provides a set of classes and methods that make it easy to create a GraphQL schema, handle requests, and generate responses. It also provides a number of features to help with things such as validation, authorization, caching, and more.

Visit the following resources to learn more:

- [@article@Getting started with HotChocolate](https://learn.microsoft.com/en-us/shows/on-net/getting-started-with-hotchocolate)
- [@article@ASP.NET Core and HotChocolate](https://chillicream.com/docs/hotchocolate/v12/api-reference/aspnetcore)
- [@article@Intro to HotChocolate](https://chillicream.com/docs/hotchocolate)

## Http  Https Protocol

# HTTP

HTTP is the `TCP/IP` based application layer communication protocol which standardizes how the client and server communicate with each other. It defines how the content is requested and transmitted across the internet.

HTTPS
=====

HTTPS (**H**ypertext **T**ransfer **P**rotocol **S**ecure) is the secure version of HTTP, which is the primary protocol used to send data between a web browser and a website.

`HTTPS = HTTP + SSL/TLS`

Visit the following resources to learn more:

- [@article@Everything you need to know about HTTP](https://cs.fyi/guide/http-in-depth)
- [@article@What is HTTP?](https://www.cloudflare.com/en-gb/learning/ddos/glossary/hypertext-transfer-protocol-http/)
- [@article@An overview of HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview)
- [@article@HTTP/3 From A To Z: Core Concepts](https://www.smashingmagazine.com/2021/08/http3-core-concepts-part1/)
- [@article@What is HTTPS?](https://www.cloudflare.com/en-gb/learning/ssl/what-is-https/)
- [@article@Why HTTPS Matters](https://developers.google.com/web/fundamentals/security/encrypt-in-transit/why-https)
- [@article@Enabling HTTPS on Your Servers](https://web.dev/enable-https/)
- [@article@How HTTPS works (comic)](https://howhttps.works/)
- [@video@HTTP Crash Course & Exploration](https://www.youtube.com/watch?v=iYM2zFP3Zn0)

## Kafka

# Apache Kafka

Apache Kafka is an open-source, distributed event streaming platform that is used for building real-time data pipelines and streaming applications. It is designed to handle high volumes of data and to support real-time data processing.

Kafka is based on a publish-subscribe model, where producers write data to topics, and consumers read data from those topics. Data is stored in topics in a log-based format, which allows for efficient storage and retrieval of data.

Visit the following resources to learn more:

- [@article@Working with Apache Kafka in ASP.NET](https://www.codemag.com/Article/2201061/Working-with-Apache-Kafka-in-ASP.NET-6-Core)
- [@article@Kafka and .NET](https://docs.confluent.io/kafka-clients/dotnet/current/overview.html)
- [@feed@Explore top posts about Apache](https://app.daily.dev/tags/apache?ref=roadmapsh)

## Kubernetes

# Kubernetes

Kubernetes is an [open source](https://github.com/kubernetes/kubernetes) container management platform, and the dominant product in this space. Using Kubernetes, teams can deploy images across multiple underlying hosts, defining their desired availability, deployment logic, and scaling logic in YAML. Kubernetes evolved from Borg, an internal Google platform used to provision and allocate compute resources (similar to the Autopilot and Aquaman systems of Microsoft Azure).

The popularity of Kubernetes has made it an increasingly important skill for the DevOps Engineer and has triggered the creation of Platform teams across the industry. These Platform engineering teams often exist with the sole purpose of making Kubernetes approachable and usable for their product development colleagues.

Visit the following resources to learn more:

- [@official@Kubernetes Website](https://kubernetes.io/)
- [@official@Kubernetes Documentation](https://kubernetes.io/docs/home/)
- [@article@Primer: How Kubernetes Came to Be, What It Is, and Why You Should Care](https://thenewstack.io/primer-how-kubernetes-came-to-be-what-it-is-and-why-you-should-care/)
- [@article@Kubernetes: An Overview](https://thenewstack.io/kubernetes-an-overview/)
- [@video@Kubernetes Crash Course for Absolute Beginners](https://www.youtube.com/watch?v=s_o8dwzRlu4)
- [@feed@Explore top posts about Kubernetes](https://app.daily.dev/tags/kubernetes?ref=roadmapsh)

## Lazy Eager Explicit Loading

# Lazy Eager Explicit Loading

Eager Loading
-------------

Eager Loading helps you to load all your needed entities at once; i.e., all your child entities will be loaded at single database call. This can be achieved, using the Include method, which returns the related entities as a part of the query and a large amount of data is loaded at once.

Lazy Loading
------------

It is the default behavior of an Entity Framework, where a child entity is loaded only when it is accessed for the first time. It simply delays the loading of the related data, until you ask for it.

Visit the following resources to learn more:

- [@article@Eager Loading & Lazy Loading](https://www.c-sharpcorner.com/article/eager-loading-lazy-loading-and-explicit-loading-in-entity-framework/)
- [@article@Difference between Eager and Lazy Loading](https://stackoverflow.com/questions/31366236/lazy-loading-vs-eager-loading)
- [@article@Working With Lazy & Eager Loading in Entity Framework](https://dzone.com/articles/working-with-lazy-loading-and-eager-loading-in-ent)

## Learn The Basics Of C

# C#

C# (pronounced "C-sharp") is a general-purpose, object-oriented programming language developed by Microsoft. It is part of the .NET family of languages and is used to build a wide range of applications, from web and mobile applications to games and cloud services.

C# is a statically-typed language, which means that the type of a variable must be specified when it is declared, and that the type of a value cannot be changed after it has been assigned. C# also supports object-oriented programming, which means that it provides features such as encapsulation, inheritance, and polymorphism.

C# is a popular language for building .NET applications, and it is used by many large companies and organizations, including Microsoft, Dell, and IBM. It is a versatile language that can be used for a wide range of purposes, and it is well-suited for building scalable and maintainable software systems.

Visit the following resources to learn more:

- [@article@Introduction to C#](https://learn.microsoft.com/en-us/dotnet/csharp/tour-of-csharp/tutorials/)
- [@article@Basics Of C#](https://www.c-sharpcorner.com/UploadFile/e9fdcd/basics-of-C-Sharp/)
- [@article@C# Tutorials](https://dotnettutorials.net/course/csharp-dot-net-tutorials/)
- [@feed@Explore top posts about C#](https://app.daily.dev/tags/csharp?ref=roadmapsh)

## Life Cycles

# Life Cycles

In [ASP.NET](http://ASP.NET), dependency injection (DI) lifecycles determine the lifetime of objects that are resolved through the DI container. There are several predefined lifecycle options in the `Microsoft.Extensions.DependencyInjection` library, including:

*   **Transient:** A new instance of the object is created every time it is requested.
*   **Scoped:** A new instance of the object is created for each request within the same scope.
*   **Singleton:** A single instance of the object is created and shared across the entire application.

Additionally, you can also create a custom lifecycle by implementing the `Microsoft.Extensions.DependencyInjection.IServiceScopeFactory` interface

Visit the following resources to learn more:

- [@article@What are Service Life Cyles in ASP.NET Core?](https://endjin.com/blog/2022/09/service-lifetimes-in-aspnet-core)
- [@article@Learn Service Lifetimes in .NET Core](https://henriquesd.medium.com/dependency-injection-and-service-lifetimes-in-net-core-ab9189349420)
- [@video@Complete Guide to Dependency Injection Lifecycles](https://www.youtube.com/watch?v=wA5bPsv2CLA)

## Light Bdd

# LightBDD

LightBDD is an open-source, lightweight, and easy-to-use BDD (Behavior-Driven Development) framework for .NET, which allows developers to write automated acceptance tests in a simple and readable format. LightBDD is commonly used in the context of [ASP.NET](http://ASP.NET) and other .NET technologies, to write acceptance tests for web applications. LightBDD is designed to provide a simple, yet powerful, way to write BDD tests. It allows developers to write tests using a fluent API, which allows them to describe the behavior of their application in a natural language format. The framework also provides a set of extension methods, which can be used to add additional functionality, such as validating the output of a test, logging test results, or integrating with other testing tools. LightBDD also comes with a built-in test runner, which makes it easy to execute tests and view the results. The framework supports a variety of test runners, such as NUnit, xUnit, and MSTest, and can be integrated with other BDD frameworks, such as SpecFlow and Cucumber.

Visit the following resources to learn more:

- [@opensource@The Lightweight Behavior Driven Development test framework](https://github.com/LightBDD/LightBDD)
- [@video@Getting started with Behavior Driven Development (BDD) in .NET](https://www.youtube.com/watch?v=EEeVU0z26u0)
- [@video@Introduction To BDD using SpecFlow in ASP.NET](https://www.youtube.com/watch?v=8KPrhBqZ-kk)
- [@feed@Explore top posts about Testing](https://app.daily.dev/tags/testing?ref=roadmapsh)

## Litedb

# LiteDB

LiteDB is a lightweight, open-source, NoSQL embedded document-oriented database engine for .NET and .NET Core. It uses a file-based storage system, meaning that the entire database is stored in a single file on disk. It uses a similar syntax to MongoDB, but it is designed to be simple and easy to use, and it does not require a separate server or installation.

LiteDB supports data types like string, int, decimal, DateTime, and also supports binary data and serialized objects. It also supports LINQ, transactions, indexes and collections.

Visit the following resources to learn more:

- [@official@Getting started with LiteDB](https://www.litedb.org/)
- [@official@Overview of LiteDB in ASP.NET](https://www.litedb.org/docs/)

## Log Frameworks

# Log Frameworks

In [ASP.NET](http://ASP.NET), log frameworks are libraries that provide a way to log and analyze data in an application. Some popular log frameworks for [ASP.NET](http://ASP.NET) include:

*   Serilog
*   NLog
*   Log4Net
*   ELMAH
*   Microsoft.Extensions.Logging

These are some of the most popular log frameworks in [ASP.NET](http://ASP.NET), each of them has its own set of features and use cases, and the choice of which log framework to use will depend on the specific requirements of the application.

Visit the following resources to learn more:

- [@article@Implement logging in ASP.NET](https://learn.microsoft.com/en-us/training/modules/aspnet-logging/)
- [@article@ASP.NET Core: Logging with log4net](https://www.linkedin.com/learning/asp-dot-net-core-logging-with-log4net)
- [@feed@Explore top posts about Logging](https://app.daily.dev/tags/logging?ref=roadmapsh)

## Manual Mapping

# Manual Mapping

Manual object mapping in [ASP.NET](http://ASP.NET) Core means explicitly assigning values from one object to another without using third-party libraries like AutoMapper. This approach gives you full control over how properties are mapped and allows for custom transformations if needed.

For instance, if an **Employee** entity has properties such as Id, Name, Email, and Department, and we need to convert it into an **EmployeeDTO** without exposing sensitive data like Id, a manual mapping method can selectively map only the necessary fields. However, it comes with trade-offs, such as increased boilerplate code and the need for manual updates whenever the data model changes. In a real-world [ASP.NET](http://ASP.NET) Core application, manual mapping can be implemented using static helper methods or extension methods that take an entity as input and return a DTO, ensuring that the mapping logic remains centralized and reusable across different parts of the application.

Visit the following resources to learn more:

- [@article@Manual vs Automapping in ASP.NET?](https://medium.com/@anderson.buenogod/manual-vs-automated-mapping-in-c-which-approach-is-best-for-your-project-50de1fd73bfa)

## Mapperly

# Mapperly

## Mariadb

# MariaDB

MariaDB is an open-source relational database management system (RDBMS) that is a fork of the MySQL database. It is fully compatible with MySQL, but it also includes additional features and improvements. MariaDB is developed and maintained by the MariaDB Corporation and the MariaDB community, and it is widely used as a replacement for MySQL in many web and enterprise applications.

In an [ASP.NET](http://ASP.NET) application, MariaDB can be used as the underlying database for storing and retrieving data. There are several libraries available for integrating MariaDB with an [ASP.NET](http://ASP.NET) application, such as MariaDB.Data, MySql.Data, and Dapper. These libraries provide a .NET client for MariaDB, which can be used to interact with the MariaDB database from within an [ASP.NET](http://ASP.NET) application.

Visit the following resources to learn more:

- [@official@Working with MariaDB and .Net](https://mariadb.com/kb/en/mariadb-and-net/)
- [@article@How to use MariaDB in ASP.NET?](https://blog.georgekosmidis.net/using-mariadb-in-an-aspnet-core-api-with-entity-framework-core.html)
- [@article@Building an application with ASP.NET & MariaDB](https://medium.com/@BMatt92656920/building-a-web-application-with-asp-net-core-mvc-entity-framework-core-mariadb-bootstrap-a2bf0927d20e)
- [@feed@Explore top posts about Infrastructure](https://app.daily.dev/tags/infrastructure?ref=roadmapsh)

## Marten

# Marten

## Mass Transit

# MassTransit

MassTransit is an open-source, highly configurable service bus framework for building distributed systems using the .NET framework. It allows developers to easily create message-based, loosely-coupled applications by providing a simple and fluent API for defining message contracts, handling messages, and managing message routing.

It supports multiple messaging transports such as RabbitMQ, Azure Service Bus, Amazon SQS and others, automatic serialization and deserialization of messages, automatic retries and exception handling for failed message deliveries, and support for advanced messaging patterns like publish-subscribe, request-response, and event-driven architectures.

Visit the following resources to learn more:

- [@opensource@Complete guide to MassTransit](https://github.com/MassTransit/MassTransit)
- [@article@Using MassTransit with RabbitMQ in ASP.NET Core](https://code-maze.com/masstransit-rabbitmq-aspnetcore/)

## Mediatr

# MediatR

MediatR is an open-source library for .NET that is designed to simplify the process of handling messages and commands in a clean, decoupled manner. It's particularly useful in applications that use the Command-Query Responsibility Segregation (CQRS) pattern and event-driven architecture. It provides a simple and easy-to-use API for handling messages, and supports the concept of pipelines, which allow you to add additional behavior to message handling, such as logging, validation, and exception handling.

Visit the following resources to learn more:

- [@article@Use MediatR in ASP.NET or ASP.NET Core](https://medium.com/dotnet-hub/use-mediatr-in-asp-net-or-asp-net-core-cqrs-and-mediator-in-dotnet-how-to-use-mediatr-cqrs-aspnetcore-5076e2f2880c)
- [@article@How to implement CQRS using MediatR in an ASP.NET?](https://christian-schou.dk/blog/how-to-implement-cqrs-with-mediatr-in-asp-net/)

## Memcached

# Memcached

Memcached is an open-source, high-performance, distributed memory object caching system which helps in reducing database load. It maintains data as an in-memory key-value store for small chunks of arbitrary data (strings, objects) which can be result of API calls, database reads and so on.

Visit the following resources to learn more:

- [@official@Intro to Memcached](https://memcached.org/)
- [@article@Using Memcached as Distributed Cache in .NET Core](https://dotnetcorecentral.com/blog/using-memcached-as-distributed-cache-in-net-core/)
- [@video@Memcached as Distributed Cache in .Net Core Application](https://www.youtube.com/watch?v=yQ8Kwx9M_Hg)

## Memory Cache

# Memory Cache

Memory caching (often simply referred to as caching) is a technique in which computer applications temporarily store data in a computer’s main memory (i.e., random access memory, or RAM) to enable fast retrievals of that data. The RAM that is used for the temporary storage is known as the cache.

Visit the following resources to learn more:

- [@article@Cache in-memory in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/performance/caching/memory?view=aspnetcore-7.0)
- [@article@What is Memory Caching?](https://hazelcast.com/glossary/memory-caching/)
- [@video@Intro to In-Memory Caching in C#](https://www.youtube.com/watch?v=2jj2wH60QuE)

## Microservices

# Microservices

Microservices are a software architectural style in which a large application is built as a set of small, independent services that communicate with each other through APIs. These services are typically built using different technologies and run in their own processes, and can be deployed, scaled, and updated independently.

In [ASP.NET](http://ASP.NET), microservices can be built using the .NET Core framework, which is a cross-platform, open-source version of the .NET framework that can run on Windows, Linux, and macOS. Each microservice can be built as a self-contained, small web application that handles a specific set of functionality, such as user management, product catalog, or order processing.

Visit the following resources to learn more:

- [@article@Intro to Microservices Using ASP.NET Core](https://www.c-sharpcorner.com/article/microservice-using-asp-net-core/)
- [@article@Advantages and Disadvantages of Microservices Architecture](https://www.dotnettricks.com/learn/microservices/architecture-example-advantages)
- [@feed@Explore top posts about Microservices](https://app.daily.dev/tags/microservices?ref=roadmapsh)

## Microsoftextensions

# Microsoft Extensions Dependency Injection

Microsoft.Extensions.DependencyInjection is a dependency injection framework that is part of the Microsoft.Extensions.DependencyInjection NuGet package. It is used to create and manage instances of objects and their dependencies, and is particularly useful for implementing the Dependency Inversion Principle in .NET applications.

The package provides a simple and consistent API for registering services and resolving dependencies, which can be used to configure and manage the lifetime of objects in an application. It also provides built-in support for various types of service lifetime, such as transient, singleton and scoped.

Visit the following resources to learn more:

- [@article@Guide to Microsoft Extensions Dependency Injection](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.dependencyinjection?view=dotnet-plat-ext-7.0)
- [@article@Exploring the Microsoft.Extensions.DependencyInjection](https://www.codeproject.com/Articles/5339241/Exploring-the-Microsoft-Extensions-DependencyInjec)
- [@article@How to use Microsoft.Extensions.DependencyInjection](https://stackoverflow.com/questions/53825155/how-can-i-use-microsoft-extensions-dependencyinjection-in-an-net-core-console-a)
- [@feed@Explore top posts about Microsoft](https://app.daily.dev/tags/microsoft?ref=roadmapsh)

## Middlewares

# Middlewares

Middleware is software that sits between an operating system and application software, and facilitates communication and data exchange between them. In the context of web development, middleware refers to software components that handle requests and responses in a web application. These components are typically executed in a pipeline, with each component performing a specific task, such as authentication, logging, or routing.

In the [ASP.NET](http://ASP.NET) Core framework, middleware is a key concept that is used to build web applications. Middleware components are added to the application pipeline using the `IApplicationBuilder` interface, and are executed in the order in which they are added. For example, an application might have middleware components for handling authentication, logging, and routing, in that order.

Visit the following resources to learn more:

- [@article@What is Middleware?](https://www.redhat.com/en/topics/middleware/what-is-middleware)
- [@article@Introduction to Middleware](https://www.techtarget.com/searchapparchitecture/definition/middleware)
- [@article@What is Middleware in .NET?](https://www.talend.com/resources/what-is-middleware/)

## Minimal Apis

# Minimal APIs

Minimal APIs is a lightweight approach to building HTTP APIs in .NET with minimal ceremony. It is designed for simplicity and performance, making it ideal for microservices, serverless applications, and small web services. Minimal APIs provide a streamlined way to define routes, handle requests, and return responses without requiring controllers or extensive configuration. They leverage top-level statements, reducing boilerplate code while maintaining flexibility and scalability.

Minimal APIs support dependency injection, middleware, model binding, and validation. They also integrate seamlessly with OpenAPI (Swagger) for API documentation. Their simplicity makes them an excellent choice for building fast and efficient web applications with .NET.

Visit the following resources to learn more:

- [@article@Minimal APIs in .NET 8: A Simplified Approach to Build Services](https://medium.com/codenx/minimal-apis-in-net-8-a-simplified-approach-to-build-services-eb50df56819f)
- [@article@Introduction to ASP.NET Core Minimal APIs](https://blog.jetbrains.com/dotnet/2023/04/25/introduction-to-asp-net-core-minimal-apis/)

## Mongodb

# MongoDB

MongoDB is a cross-platform, open-source, NoSQL document-oriented database that can be used to store and retrieve large amounts of data. It uses a flexible, JSON-like data structure called BSON (binary JSON) and it is designed to handle large amounts of unstructured data.

In an [ASP.NET](http://ASP.NET) application, MongoDB can be used as a data store to persist and retrieve application data. There are several libraries available for integrating MongoDB with an [ASP.NET](http://ASP.NET) application, such as MongoDB.Driver and C# MongoDB Driver. These libraries provide a .NET client for MongoDB, which can be used to interact with the MongoDB server from within an [ASP.NET](http://ASP.NET) application.

Visit the following resources to learn more:

- [@article@Use MongoDB in Your C# ASP.NET Apps](https://developer.okta.com/blog/2020/01/02/mongodb-csharp-aspnet-datastore)
- [@article@MongoDB With ASP.NET Core Web API](https://www.c-sharpcorner.com/article/using-mongodb-with-asp-net-core-web-api/)
- [@feed@Explore top posts about MongoDB](https://app.daily.dev/tags/mongodb?ref=roadmapsh)

## Moq

# Moq

Moq is an open-source library for .NET that allows developers to create mock objects for use in unit testing, it is a popular mocking framework that provides a simple and intuitive syntax for creating mock objects and setting up mock behavior. In the context of [ASP.NET](http://ASP.NET), Moq can be used to create mock objects for testing web applications built using the [ASP.NET](http://ASP.NET) framework, it provides a simple and expressive syntax for creating mock objects and setting up mock behavior. Moq supports a wide range of testing frameworks, including MSTest, NUnit, and xUnit and it also supports various platforms including .NET Framework, .NET Core and Xamarin. Moq is lightweight and easy to use, making it a good choice for developers who are new to mocking and unit testing, it also provides a rich set of features, such as support for setting up mock behavior, making assertions on calls made to the mock objects, and more.

Visit the following resources to learn more:

- [@article@What is use of Moq?](https://stackoverflow.com/questions/678878/what-is-use-of-moq)
- [@article@Moq - Unit Test In .NET Core App](https://www.c-sharpcorner.com/article/moq-unit-test-net-core-app-using-mock-object/)
- [@video@Getting started with Mocking using Moq in .NET](https://www.youtube.com/watch?v=9ZvDBSQa_so)

## Mstest

# MSTest

MSTest is a unit testing framework for the .NET framework, it's one of the built-in test frameworks in Visual Studio and it's widely used for unit testing in the .NET ecosystem. In the context of [ASP.NET](http://ASP.NET), MSTest can be used to write unit tests for web applications built using the [ASP.NET](http://ASP.NET) framework. MSTest provides features such as data-driven testing, parallel test execution, and test discovery and execution, it also provides the ability to run tests on multiple frameworks.

Visit the following resources to learn more:

- [@article@.NET Core testing with MSTest](https://www.oreilly.com/library/view/c-and-net/9781788292481/aa08c601-f374-4e31-be8e-8eb69d63bd19.xhtml)
- [@article@Unit testing with MSTest and .NET](https://learn.microsoft.com/en-us/dotnet/core/testing/unit-testing-with-mstest)
- [@article@Complete Guide of MSTest for Unit Testing in ASP.NET](https://sweetcode.io/a-complete-guide-of-mstest-for-unit-testing-in-asp-net/)

## Mvc

# MVC

MVC is an architectural design pattern used for developing applications, specifically web applications. This pattern separates an application into three main logical components **Model View Controller**. Each architectural component is built to handle specific development aspects of an application.

*   **Model** - Handles all data-related logic. Interacts with Database.
*   **View** - Handles UI part of the applications (data presentation).
*   **Controller** - Handles request flow, and acts as an intermediary between view and model.

Visit the following resources to learn more:

- [@article@MVC Official Documentation](https://learn.microsoft.com/en-us/aspnet/core/mvc/overview?WT.mc_id=dotnet-35129-website&view=aspnetcore-7.0)
- [@article@ASP.NET MVC Architecture](https://www.tutorialsteacher.com/mvc/mvc-architecture)
- [@article@MVC Framework - Introduction](https://www.tutorialspoint.com/mvc_framework/mvc_framework_introduction.htm)

## Mysql

# MySQL

MySQL is an open-source relational database management system (RDBMS) that is widely used in web and enterprise applications. It is developed, distributed, and supported by Oracle Corporation. MySQL provides a rich set of features to handle high-performance, high-availability, and high-scalability requirements of modern web applications.

In an [ASP.NET](http://ASP.NET) application, MySQL can be used as the underlying database for storing and retrieving data. There are several libraries available for integrating MySQL with an [ASP.NET](http://ASP.NET) application, such as MySql.Data, Dapper and EF Core. These libraries provide a .NET client for MySQL, which can be used to interact with the MySQL database from within an [ASP.NET](http://ASP.NET) application.

Visit the following resources to learn more:

- [@article@Getting started with ASP.NET Core and MySQL](https://dev.mysql.com/blog-archive/getting-started-with-asp-net-core-and-mysql-connectornet/)
- [@article@MySql database connectivity with ASP.Net](https://www.c-sharpcorner.com/UploadFile/brij_mcn/mysql-database-connectivity-with-Asp-Net/)
- [@video@How To Connect MySQL With ASP.NET](https://www.youtube.com/watch?v=g5rVd1JGbIg)
- [@feed@Explore top posts about MySQL](https://app.daily.dev/tags/mysql?ref=roadmapsh)

## Native Background Service

# Native Background Service

A Native Background Service in [ASP.NET](http://ASP.NET) is a type of service that can run in the background on a device, without the need for an active user session. These services are typically used for tasks that need to run continuously, such as sending notifications, polling for updates, or processing data.

In [ASP.NET](http://ASP.NET), a Native Background Service can be implemented using the IHostedService interface, which is part of the Microsoft.Extensions.Hosting namespace. This interface allows you to create a background service that can run continuously, even when the main application is not running.

Visit the following resources to learn more:

- [@article@Background tasks with hosted services in ASP.NET](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/host/hosted-services?view=aspnetcore-7.0&tabs=visual-studio)
- [@article@BackgroundService in ASP.NET Core](https://medium.com/@daniel.sagita/backgroundservice-for-a-long-running-work-3debe8f8d25b)
- [@video@Tutorial on Background Tasks in ASP.NET](https://youtube.com/watch?v=rugxQIH_p3A)

## Net Aspire

# .NET Aspire

## Net Aspire

# .NET Aspire

## Net Cli

# .NET CLI

.NET CLI is the command-line interface (CLI) for the .NET platform. It is a tool that provides a common interface for running .NET Core command-line tools and utilities. .NET Core is a cross-platform, open-source, and modular version of the .NET framework, and the .NET CLI provides a way to interact with it from the command line.

Visit the following resources to learn more:

- [@article@Microsoft - .NET CLI overview](https://learn.microsoft.com/en-us/dotnet/core/tools/)
- [@video@Intro To The .NET CLI](https://youtu.be/RQLzp2Z8-BE)
- [@feed@Explore top posts about CLI](https://app.daily.dev/tags/cli?ref=roadmapsh)

## Net Maui

# .NET MAUI

## Net

# .NET Framework

.NET (pronounced "dot net") is a software framework developed by Microsoft that can be used to create a wide range of applications, including Windows desktop and web applications, mobile apps, and gaming. The .NET Framework provides a large library of pre-built functionality, including collections, file input/output, and networking, that can be used by .NET applications. It also includes a Common Language Runtime (CLR) which manages the execution of code, providing features such as memory management, security, and exception handling.

Visit the following resources to learn more:

- [@article@What is .NET?](https://dotnet.microsoft.com/en-us/learn/dotnet/what-is-dotnet)
- [@article@An Overview of .NET](https://auth0.com/blog/what-is-dotnet-platform-overview/)
- [@feed@Explore top posts about .NET](https://app.daily.dev/tags/.net?ref=roadmapsh)

## Netmq

# NetMQ

NetMQ is a lightweight, open-source messaging library for building distributed systems and real-time applications in .NET. It provides an API for sending and receiving messages using a variety of messaging patterns and protocols, including request-response, publish-subscribe, and push-pull.

NetMQ is built on top of ZeroMQ, a high-performance, asynchronous messaging library that provides a minimalistic socket-based API for building distributed systems. NetMQ is designed to be easy to use and to abstract away the complexities of ZeroMQ, making it a good choice for developers who want to add messaging capabilities to their [ASP.NET](http://ASP.NET) applications without having to learn a complex API.

Visit the following resources to learn more:

- [@article@Documentation of NetMQ](https://netmq.readthedocs.io/en/latest/introduction/)
- [@article@NetMQ and creating a Dynamic Worker in .NET](https://mikaelkoskinen.net/post/netmq-and-creating-a-dynamic-worker-per-task)

## Nhibernate

# NHibernate

NHibernate is an open-source Object-Relational Mapping (ORM) framework for .NET. It is a powerful and flexible framework that can greatly simplify working with relational data in .NET. NHibernate is similar to other ORM frameworks such as Entity Framework and RepoDb in that it provides a higher-level abstraction on top of the underlying data access technology ([ADO.NET](http://ADO.NET) in this case) and allows developers to work with data using domain-specific objects, eliminating the need to write raw SQL statements.

NHibernate uses the concept of "mapping files" which are XML files that define how the classes in the application map to the tables and columns in the database. These mapping files are used to create a conceptual model of the data in the form of classes, and then NHibernate uses this model to generate the SQL statements necessary to interact with the database.

Visit the following resources to learn more:

- [@official@Get Started with NHibernate](https://nhibernate.info/)
- [@article@What is Nhibernate?](https://www.partech.nl/en/publications/2021/08/what-is-nhibernate-and-how-is-it-different-from-entity-framework)
- [@article@NHibernate - ORM](https://www.tutorialspoint.com/nhibernate/nhibernate_orm.htm)

## Nlog

# NLog

NLog is an open-source logging library for .NET applications, including [ASP.NET](http://ASP.NET). It is designed to be easy to use, highly configurable, and extensible, and it provides a number of features that help developers to log and analyze data in their applications.

NLog is a powerful, flexible, and easy-to-use logging library that can be used in [ASP.NET](http://ASP.NET) applications to provide detailed log data. It allows developers to easily configure their logging pipeline, and to write log data to a variety of destinations, making it easier to analyze and troubleshoot issues in the application.

Visit the following resources to learn more:

- [@article@Logging with NLog in ASP.NET](https://codewithmukesh.com/blog/logging-with-nlog-in-aspnet-core/)
- [@article@Introduction To NLog With ASP.NET Core](https://www.c-sharpcorner.com/article/introduction-to-nlog-with-asp-net-core2/)
- [@video@Tutorial of Nlog with ASP.NET](https://www.youtube.com/watch?v=PnlxRmHg0lU)

## Nosql

# Nosql

NoSQL (Not Only SQL) is a type of database that does not use the traditional table-based relational model. It is designed to handle large amounts of unstructured or semi-structured data, and it is often used in big data and real-time web applications. NoSQL databases are highly scalable and can handle high-performance needs and large data sets.

There are several types of NoSQL databases, such as document databases, key-value databases, graph databases, and column-family databases, each with their own unique features and use cases. Some examples of NoSQL databases include MongoDB, Cassandra, RavenDB, CouchDB, and Redis.

Visit the following resources to learn more:

- [@article@NoSQL in .NET Applications](https://www.slideshare.net/shijucv/nosql-database-in-net-apps)
- [@article@Open Source NoSQL Database for .NET](https://www.alachisoft.com/nosdb/)
- [@article@Use NoSQL databases in ASP.NET](https://learn.microsoft.com/en-us/dotnet/architecture/microservices/microservice-ddd-cqrs-patterns/nosql-database-persistence-infrastructure)
- [@feed@Explore top posts about NoSQL](https://app.daily.dev/tags/nosql?ref=roadmapsh)

## Nservicebus

# NServiceBus

NServiceBus (NSB) is a service bus framework for building distributed systems using the .NET framework. It provides a set of features for building message-based, loosely-coupled applications, including support for message routing, message handling, and message persistence.

NSB supports multiple messaging transports, including MSMQ, RabbitMQ, and Azure Service Bus, and provides support for advanced messaging patterns such as publish-subscribe, request-response, and message-based sagas.

Visit the following resources to learn more:

- [@article@Using NServiceBus in an ASP.NET](https://docs.particular.net/samples/web/send-from-aspnetcore-webapi/)
- [@article@Learn NServiceBus from .NET Core](https://www.codeproject.com/Articles/1224839/Learn-NServiceBus-from-NET-Core-WebAPI)

## Nsubstitute

# NSubstitute

NSubstitute is a popular open-source .NET library that allows developers to create mock objects for use in unit testing, it is a powerful and flexible substitute for traditional mocking frameworks such as Moq and Rhino Mocks. In the context of [ASP.NET](http://ASP.NET), NSubstitute can be used to create mock objects for testing web applications built using the [ASP.NET](http://ASP.NET) framework, it provides a simple and intuitive syntax for creating mock objects, setting up mock behavior, and making assertions on calls made to the mock objects. NSubstitute supports a wide range of testing frameworks and test runners, including MSTest, NUnit, and xUnit and it also supports various platforms including .NET Framework, .NET Core, Xamarin and Unity.

Visit the following resources to learn more:

- [@opensource@Overview of NSubstitute](https://github.com/nsubstitute/NSubstitute)
- [@article@Getting started NSubstitute](https://nsubstitute.github.io/help/getting-started/)

## Nuke

# NUKE

NUKE (Build Automation for .NET) is an open-source build automation tool for .NET projects. It is designed to be simple, flexible, and extensible, making it easy to automate the build, test, and deployment process of your .NET projects.

NUKE allows you to define your build process using a simple, declarative syntax, making it easy to understand and maintain. It provides a set of built-in tasks for common build actions, such as compiling, testing, and publishing, as well as a powerful extensibility model that allows you to add custom tasks and scripts.

Visit the following resources to learn more:

- [@article@How to Build Automation with NUKE](https://learn.microsoft.com/en-us/shows/on-net/build-automation-with-nuke)
- [@article@Automate your .NET project builds with NUKE](https://laurentkempe.com/2022/02/02/automate-your-dotnet-project-builds-with-nuke-a-cross-platform-build-automation-solution/)

## Nunit

# NUnit

NUnit is a unit testing framework for the .NET framework, it's an open-source testing framework that provides a set of attributes and classes that can be used to create unit tests. In the context of [ASP.NET](http://ASP.NET), NUnit can be used to write unit tests for web applications built using the [ASP.NET](http://ASP.NET) framework. NUnit provides features such as support for data-driven tests, support for parallel test execution, and support for test discovery and execution, it also provides support for test isolation which allows developers to run tests in isolation from each other. NUnit is a popular alternative to other testing frameworks like MSTest and xUnit and it has a similar syntax as JUnit and it's considered as one of the oldest testing frameworks for .NET.

Visit the following resources to learn more:

- [@article@NUnit With C#](https://www.c-sharpcorner.com/UploadFile/84c85b/nunit-with-C-Sharp/)
- [@article@Unit testing C# with NUnit and .NET Core](https://learn.microsoft.com/en-us/dotnet/core/testing/unit-testing-with-nunit)

## Object Mapping

# Object Mapping

Object mapping in [ASP.NET](http://ASP.NET) refers to the process of converting an object of one type to an object of another type. This can be useful in a number of scenarios, such as when working with domain models and data transfer objects (DTOs) in a layered architecture, or when mapping between different versions of an object or different formats such as JSON and XML.

There are several libraries available for object mapping in [ASP.NET](http://ASP.NET), such as AutoMapper, ExpressMapper, AgileMapper, AgileMapster and Mapster. These libraries provide a convenient and flexible way to map between objects, using a convention-based approach or a fluent API to configure more complex mappings. They also support for a wide range of mapping scenarios, including nested and circular object graphs, collections, and different types of inheritance.

Visit the following resources to learn more:

- [@article@Building a Fast Object-to-Object Mapper in .NET](https://www.twilio.com/blog/building-blazing-fast-object-mapper-c-sharp-net-core)
- [@article@Overview of Object Mapping in ASP.NET](https://docs.abp.io/en/abp/latest/Object-To-Object-Mapping)
- [@article@Comparison of Object Mapper Libraries](https://www.simplilearn.com/tutorials/asp-dot-net-tutorial/automapper-in-c-sharp)

## Object Relational Mapping

# ORM

ORM stands for Object-Relational Mapping, and it is a technique that allows a developer to work with a database using objects. It is a way of abstracting the database so that the developer can think in terms of objects, rather than tables and SQL queries. This can make it easier to write and maintain code, as well as improve the performance of the application.

Visit the following resources to learn more:

- [@article@ORM (Object Relational Mapping)](https://www.telerik.com/blogs/dotnet-basics-orm-object-relational-mapping)
- [@article@Understanding Object-Relational Mapping: Pros, Cons](https://www.altexsoft.com/blog/object-relational-mapping/)

## Ocelot

# Ocelot

Ocelot is an open-source API gateway for [ASP.NET](http://ASP.NET) Core. It is designed to work as a reverse proxy, routing incoming requests to the appropriate service and aggregating the responses to return to the client. Ocelot allows you to define routing rules, handle requests and responses, and perform other common API gateway tasks such as rate limiting, caching, and authentication.

One of the key features of Ocelot is its flexibility, it can route incoming requests to multiple services, aggregate the responses, and return them as a single response to the client. It also allows you to define dynamic routes, based on the request's content, perform request and response transformations, and handle errors.

Visit the following resources to learn more:

- [@article@Implement API Gateways with Ocelot](https://learn.microsoft.com/en-us/dotnet/architecture/microservices/multi-container-microservice-net-applications/implement-api-gateways-with-ocelot)
- [@article@Getting Started with Ocelot](https://ocelot.readthedocs.io/en/latest/introduction/gettingstarted.html)
- [@video@Building an API Gateway in ASP.NET using Ocelotss](https://www.youtube.com/watch?v=hlUGZ6Hmv6s)

## Odata

# OData

OData (Open Data Protocol) is a web protocol for querying and updating data. It is an open standard for creating and consuming RESTful web services. OData is built on top of the HTTP protocol, and it uses the conventions of REST to expose data through a standard interface.

In [ASP.NET](http://ASP.NET), OData can be used to create RESTful web services that expose data in a standardized way. OData provides a set of conventions for defining the structure of the data, and it also provides a set of conventions for querying and updating the data.

Visit the following resources to learn more:

- [@article@Create an OData v4 Endpoint Using ASP.NET](https://learn.microsoft.com/en-us/aspnet/web-api/overview/odata-support-in-aspnet-web-api/odata-v4/create-an-odata-v4-endpoint)
- [@video@Example of OData Protocol With ASP.NET Core](https://www.youtube.com/watch?v=L9HdnNCi0R0)

## Orleans

# Orleans

Orleans is an open-source virtual actor model framework for building distributed, high-scale, and low-latency applications in .NET. It is designed to make it easy to build and operate large-scale, distributed systems, such as cloud services, IoT applications, and gaming servers.

One of the key features of Orleans is its use of the virtual actor model, which is a programming model that allows developers to write concurrent and parallel code in a way that is similar to writing single-threaded code. Orleans provides a set of abstractions for building stateful actors, which are similar to objects in object-oriented programming, that can be distributed across multiple machines. These actors can communicate with each other using message passing, and can be accessed remotely using a transparent proxy

Visit the following resources to learn more:

- [@article@Microsoft Orleans](https://learn.microsoft.com/en-us/dotnet/orleans/overview)
- [@article@Introduction to Orleans](https://dev.to/willvelida/introduction-to-microsoft-orleans-796)
- [@video@Building real applications with Orleans](https://www.youtube.com/watch?v=8duFuggnj8o)

## Playwright

# Playwright

Playwright is an open-source library for automating web browsers built by Microsoft, similar to Selenium, it's commonly used for testing web applications. It's built on top of the .NET Core runtime and it provides bindings for C#, it allows developers to write tests for web applications in C# or other .NET languages. Playwright is designed to be fast and reliable and allows developers to run tests in multiple browsers.

Visit the following resources to learn more:

- [@opensource@Playwright for .NET](https://github.com/microsoft/playwright-dotnet)
- [@article@How to test Apps with Playwright and .NETs](https://www.twilio.com/blog/test-web-apps-with-playwright-and-csharp-dotnet)
- [@article@End-to-End Tests With ASP.NET and Playwright](https://khalidabuhakmeh.com/end-to-end-test-with-aspnet-core-xunit-and-playwright)

## Polly

# Polly

Polly is an open-source library for .NET that provides a simple and flexible API for handling transient faults and other types of errors that occur during the execution of a service. It allows developers to define a set of policies, such as retry, circuit breaker, and timeout, that can be used to handle specific types of errors and improve the resiliency of the service. It provides a fluent API that makes it easy to define and configure policies, supports advanced features such as async and sync execution, fallback policies, and policy wrapping. Additionally, it allows to specify the exception type that is thrown and it would trigger the policy.

Visit the following resources to learn more:

- [@article@Using Polly for .NET Resilience](https://www.telerik.com/blogs/using-polly-for-net-resilience-and-transient-fault-handling-with-net-core)
- [@article@Build Resilient Microservices Using Polly In ASP.NET](https://procodeguide.com/programming/polly-in-aspnet-core/)

## Postgresql

# PostgreSQL

PostgreSQL, often simply "Postgres", is an open-source relational database management system (RDBMS) emphasizing extensibility and SQL compliance. It was originally developed at the University of California, Berkeley in the 1980s and is now maintained by the PostgreSQL Global Development Group.

Postgres is known for its robustness and reliability, as well as its support for advanced features such as concurrency control, full-text search, and geospatial data. It is also highly extensible, allowing developers to create custom functions and operators in a variety of programming languages, including C, Python, and JavaScript.

Visit the following resources to learn more:

- [@official@Postgresql - Open Source Relational Database](https://www.postgresql.org/)
- [@article@What is Postgresql?](https://postgresqltutorial.com/postgresql-getting-started/what-is-postgresql/)
- [@article@Introduction, Advantages & Disadvantages of PostgreSQL](https://www.guru99.com/introduction-postgresql.html)
- [@feed@Explore top posts about PostgreSQL](https://app.daily.dev/tags/postgresql?ref=roadmapsh)

## Puppeteer

# Puppeteer

Puppeteer is an open-source library for automating web browsers, similar to Selenium and Playwright. It's built on top of the Chrome DevTools protocol and it provides a set of APIs that allows developers to interact with web browsers and simulate user interactions, such as clicking buttons, filling out forms, and navigating between pages. It's commonly used for testing web applications, web scraping, and generating screenshots and PDFs of web pages. Puppeteer for .NET is built on top of the .NET Core runtime and it provides bindings for C# and allows developers to write tests for web applications in C# or other .NET languages.

Visit the following resources to learn more:

- [@article@Why use Puppeteer?](https://www.kiltandcode.com/puppeteer-sharp-crawl-the-web-using-csharp-and-headless-chrome/)
- [@article@Documentations of Puppeteer](https://www.puppeteersharp.com/)
- [@feed@Explore top posts about Crawling](https://app.daily.dev/tags/crawling?ref=roadmapsh)

## Quartz

# Quartz

Quartz is an open-source, job scheduling library for .NET that can be used in [ASP.NET](http://ASP.NET) applications. It is based on the popular Quartz scheduler for Java, and provides a similar feature set for scheduling and executing background jobs in .NET applications.

With Quartz, you can schedule jobs to run at specific times or intervals, and you can also set up triggers to start a job based on certain events. Quartz also provides a rich set of options for configuring and managing your jobs, such as pausing, resuming, and canceling jobs, as well as job chaining and priorities.

Visit the following resources to learn more:

- [@article@Intro to Quartz in ASP.NET](https://aspnetboilerplate.com/Pages/Documents/Quartz-Integration)
- [@article@How to work with Quartz.Net in ASP.NET](https://www.infoworld.com/article/3078781/how-to-work-with-quartz-net-in-c.html)

## Rabbitmq

# RabbitMQ

RabbitMQ is an open-source message broker software that implements the Advanced Message Queuing Protocol (AMQP). It is written in Erlang and can be used to send and receive messages between different applications in a loosely coupled, asynchronous manner. RabbitMQ supports a variety of messaging patterns, including point-to-point, publish-subscribe, and request-response.

In the context of an [ASP.NET](http://ASP.NET) application, RabbitMQ can be used to send and receive messages to and from other systems. For example, it can be used to send messages from a web application to a background service, or to send messages between different microservices.

Visit the following resources to learn more:

- [@official@Introduction of RabbitMQ](https://www.rabbitmq.com/tutorials/tutorial-one-dotnet.html)
- [@article@How to Use RabbitMQ in ASP NET?](https://www.freecodespot.com/blog/use-rabbitmq-in-asp-net-core/)
- [@article@ASP.NET and RabbitMQ](https://referbruv.com/blog/integrating-rabbitmq-with-aspnet-core-quickstart-with-an-example/)

## Razor Components

# Razor Components

Razor Components is a feature of [ASP.NET](http://ASP.NET) Core that allows developers to build reusable, self-contained components that can be used across multiple pages or even multiple applications. Razor Components is built on top of the Razor view engine, which allows developers to define components using a combination of Razor markup and C# code.

Razor Components are useful for building complex, dynamic, and reusable UI elements, such as forms, tables, or dialogs, and can be used to build both small and large-scale web applications.

Visit the following resources to learn more:

- [@article@ASP.NET Core Razor components](https://learn.microsoft.com/en-us/aspnet/core/blazor/components/?view=aspnetcore-7.0)
- [@article@Core Razor Componets in .NET](https://www.c-sharpcorner.com/blogs/asp-net-core-razor-componets)
- [@video@What is Core razor components?](https://www.youtube.com/watch?v=KseDLejhYi0)

## Razor Pages

# Razor Pages

Razor Pages is a feature of the [ASP.NET](http://ASP.NET) Core framework that allows developers to build web applications using a combination of Razor markup (a markup syntax for defining dynamic HTML) and C# code. Razor Pages is built on top of the [ASP.NET](http://ASP.NET) Core MVC (Model-View-Controller) framework, and provides a simpler, more intuitive way to build web pages and handle user input.

Razor Pages are useful for building simple, self-contained web pages that do not require a complex navigation or layout structure, and are often used for building small to medium-size web applications.

Visit the following resources to learn more:

- [@article@Basics of Razor Pages](https://www.jetbrains.com/dotnet/guide/tutorials/basics/razor-pages/)
- [@article@Get started with Razor Pages in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/tutorials/razor-pages/?view=aspnetcore-7.0)
- [@article@What Is Razor Pages?](https://www.learnrazorpages.com/)

## Razor

# Razor

Razor is a markup syntax for embedding server-side code in web pages. It was introduced with [ASP.NET](http://ASP.NET) MVC 3 and later became a part of [ASP.NET](http://ASP.NET) Web Pages. It allows developers to write server-side code using C# or Visual Basic and embed it in HTML markup. Its syntax is designed to be compact and easy to read. It provides a rich set of features for building web applications, such as a component model for building reusable UI, a routing system for navigation, and support for dependency injection, it also allows you to use the same libraries, frameworks, and tools that you're already familiar with from building traditional [ASP.NET](http://ASP.NET) web applications.

Visit the following resources to learn more:

- [@article@Introduction to ASP.NET Web Programming Using Razor](https://learn.microsoft.com/en-us/aspnet/web-pages/overview/getting-started/introducing-razor-syntax-c)
- [@article@An Introduction To Razor](https://khalidabuhakmeh.com/what-is-razor-aspnet)

## Real Time Communication

# Real Time Communication

Real-time communication in [ASP.NET](http://ASP.NET) refers to the ability to send and receive data between a client and a server in real-time, typically with low latency. It allows the server to push updates to the client as they happen, instead of the client having to continuously poll the server for updates.

There are several technologies and libraries available for implementing real-time communication in [ASP.NET](http://ASP.NET), such as WebSockets, SignalR, gRPC, and more.

Visit the following resources to learn more:

- [@article@Overview of ASP.NET Core SignalR](https://learn.microsoft.com/en-us/aspnet/core/signalr/introduction?view=aspnetcore-7.0)
- [@article@Real-time ASP.NET with SignalR](https://dotnet.microsoft.com/en-us/apps/aspnet/signalr)

## Redis

# Redis

Redis is an open source (BSD licensed) which is an in-memory data structure store used as a database, cache, message broker, and streaming engine. Redis provides data structures such as strings, hashes, lists, sets, sorted sets with range queries, bitmaps, hyperloglogs, geospatial indexes, and streams. Redis has built-in replication, Lua scripting, LRU eviction, transactions, and various levels of on-disk persistence, and provides high availability via Redis Sentinel and automatic partitioning with Redis Cluster.

You can use Redis in many programming languages. It is such a popular and widely used cache that Microsoft Azure also provides its cloud-based version with the name Azure Cache for Redis.

Visit the following resources to learn more:

- [@official@Learn how to build with Redis Stack and .NET](https://redis.io/docs/stack/get-started/tutorials/stack-dotnet/)
- [@article@Redis Cache In ASP.NET 6.0 Web API](https://www.c-sharpcorner.com/article/easily-use-redis-cache-in-asp-net-6-0-web-api/)
- [@video@ASP.Net Core Distributed Caching - Redis Caching](https://www.youtube.com/watch?v=4Br-QnBo6Yw)
- [@feed@Explore top posts about Redis](https://app.daily.dev/tags/redis?ref=roadmapsh)

## Relational

# Relational

A relational database is a type of database that stores data in a structured format, using tables and relationships between them. It is based on the relational model, which organizes data into one or more tables, with each table consisting of a set of rows and columns.

The main feature of a relational database is the ability to establish relationships between tables, using a feature called a foreign key. A foreign key is a column or set of columns in one table that is used to link to the primary key of another table. This allows data to be spread across multiple tables, but still be connected and easily accessed through these relationships.

Visit the following resources to learn more:

- [@article@Introduction to Working with Database in ASP.NET](https://learn.microsoft.com/en-us/aspnet/web-pages/overview/data/5-working-with-data)
- [@article@Implement a Relational Database with ASP.NET](https://openclassrooms.com/en/courses/5671811-implement-a-relational-database-with-asp-net-core)

## Repodb

# RepoDB

RepoDB is an open-source ORM (Object-Relational Mapping) library for .NET that simplifies the process of working with databases. It is a lightweight, fast, and easy-to-use library that provides a simple and consistent API for performing common database operations such as querying, inserting, updating, and deleting data.

RepoDb is built on top of [ADO.NET](http://ADO.NET), which is the native data access technology in .NET, and provides a higher-level abstraction on top of it. This allows RepoDb to take advantage of the performance and scalability of [ADO.NET](http://ADO.NET) while providing a simpler and more convenient API for developers.

Visit the following resources to learn more:

- [@official@Get Started with RepoDB](https://repodb.net/)
- [@article@Complete Guide to RepoDB](https://medium.com/nerd-for-tech/everything-you-need-to-know-about-repodb-23cd4b9939c1)
- [@article@Why Choose RepoDB?](https://blog.devgenius.io/why-choose-repodb-orm-over-dapper-da87432c7830)

## Respawn

# Respawn

## Rest

# REST

REST (Representational State Transfer) is an architectural style for building web services. It is based on the principles of the HTTP protocol, and it uses the conventions of HTTP to create a standard interface for interacting with web services.

In [ASP.NET](http://ASP.NET), REST can be used to create web services that expose data in a standardized way. RESTful web services in [ASP.NET](http://ASP.NET) are typically built using the Web API framework, which provides a set of libraries and tools for building RESTful web services.

Visit the following resources to learn more:

- [@article@What is REST Services in ASP.NET?](http://www.codedigest.com/quick-start/16/what-is-rest-services-how-to-create-rest-services-in-aspnet)
- [@article@What are RESTful APIs?](https://www.pragimtech.com/blog/blazor/what-are-restful-apis/)
- [@video@Tutorial of Rest and Restful API](https://www.youtube.com/watch?v=4r1CIUs5s2I)
- [@feed@Explore top posts about REST API](https://app.daily.dev/tags/rest-api?ref=roadmapsh)

## Rest

# REST

REST (Representational State Transfer) is an architectural style for building web services. In the context of .NET, RESTful web services can be created using the [ASP.NET](http://ASP.NET) Web API framework, which allows developers to create HTTP-based services that can be consumed by a wide range of clients, including web browsers and mobile devices. The Web API framework provides a set of tools and libraries for creating RESTful services, including routing, request/response handling, and support for a variety of data formats, such as JSON and XML.

Visit the following resources to learn more:

- [@article@What is REST Services?](http://www.codedigest.com/quick-start/16/what-is-rest-services-how-to-create-rest-services-in-aspnet)
- [@article@Restful API In ASP.NET: Introduction of REST & Web API](https://www.c-sharpcorner.com/UploadFile/4b0136/restful-api-in-Asp-Net-introduction-of-rest-web-api/)
- [@article@What are RESTful APIs](https://www.pragimtech.com/blog/blazor/what-are-restful-apis/)
- [@feed@Explore top posts about REST API](https://app.daily.dev/tags/rest-api?ref=roadmapsh)

## Scalar

# Scalar

## Scoped

# Scoped

Scoped lifetime is a type of dependency injection that creates a new instance of an object for each unique request, but reuses the same instance for the same request. This means that if multiple components within the same request depend on the same service, they will all receive the same instance. However, if another request is made, a new instance of the service will be created for that request.

Scoped lifetime is useful when you have services that are specific to a given request, such as a request-scoped database context. This allows you to have a separate and isolated instance of a service for each unique request, which can help to prevent cross-request contamination of data and improve performance.

Visit the following resources to learn more:

- [@article@Dependency Injection - What is Scope?](https://javaranch.com/journal/2008/10/dependency-injection-what-is-scope.html)
- [@article@Effective Dependency Injection Scoping](https://medium.com/android-news/effective-dependency-injection-scoping-4bac813d4491)

## Scriban

# Scriban

Scriban is an open-source, lightweight template engine for .NET that is based on the Lua programming language. It is designed to be simple and easy to use, while still providing a powerful set of features for creating and manipulating templates. It provides a simple and easy-to-use API for parsing and rendering templates, and supports a wide range of features such as variables, loops, conditionals, and functions. It also provides a wide range of built-in functions for working with strings, numbers, dates, and other types of data, and also supports advanced features such as scripting and metaprogramming.

Visit the following resources to learn more:

- [@opensource@Guide to Scriban in ASP.NET](https://github.com/scriban/scriban)
- [@article@Introduction to Scriban](https://www.markvanaalst.com/blog/sxa/sxa-9-3-introducing-scriban/)

## Scrutor

# Scrutor

Scrutor is an open-source library for .NET that extends the functionality of the built-in dependency injection framework in .NET Core. It provides a set of extension methods for the `IServiceCollection` interface, which can be used to register and configure services in a more convenient and flexible way.

One of the main features of Scrutor is its ability to automatically scan assemblies for services and register them with the dependency injection container, allowing you to avoid having to manually register each service one by one. It also provides a fluent API that makes it easy to configure services, such as specifying the lifetime of a service, adding decorators, and more.

Visit the following resources to learn more:

- [@article@How to use Scrutor in ASP.Net Core?](https://www.infoworld.com/article/3321356/how-to-use-scrutor-in-aspnet-core.html)
- [@article@Complete Guide to Scrutor](https://andrewlock.net/using-scrutor-to-automatically-register-your-services-with-the-asp-net-core-di-container/)

## Search Engines

# Search Engines

A search engine in an [ASP.NET](http://ASP.NET) application is a tool or module that allows users to search for and retrieve specific information from the application's database or other data sources. Search engines can be used to perform full-text search, faceted search, and geospatial search, among other things.

Search engines can be integrated into an [ASP.NET](http://ASP.NET) application by using libraries or frameworks that provide a .NET client for interacting with the search engine. Some popular search engines that can be integrated with an [ASP.NET](http://ASP.NET) application include Elasticsearch, Apache Solr, Sphinx, and Microsoft Azure Search.

Visit the following resources to learn more:

- [@article@Search Engine Optimization with ASP.NET](https://learn.microsoft.com/en-us/archive/msdn-magazine/2009/september/search-engine-optimization-with-asp-net-4-0-visual-studio-2010-and-iis7)
- [@article@Creating an ASP.NET Search Engine](https://www.developerfusion.com/article/4389/create-a-site-search-engine-in-aspnet/)
- [@video@Simple Search Engine in ASP.NET](https://www.youtube.com/watch?v=KTkubhS-u50)

## Serilog

# Serilog

Serilog is a third-party logging library for [ASP.NET](http://ASP.NET) Core that allows developers to easily create structured and searchable log data. It is built on top of the `Microsoft.Extensions.Logging` framework, which is included in [ASP.NET](http://ASP.NET) Core. Serilog provides features such as automatic logging of request and response data, and the ability to write logs to a variety of destinations, including the console, files, and various logging services. It also supports for filtering and formatting log messages.

Visit the following resources to learn more:

- [@opensource@Complete guide to Serilog in ASP.NET](https://github.com/serilog/serilog-aspnetcore)
- [@article@How to Work with Serilog in ASP.NET?](https://www.codeguru.com/dotnet/serilog-c-sharp/)
- [@article@Advanced Serilog features in ASP.NET](https://www.infoworld.com/article/3624022/how-to-use-advanced-serilog-features-in-aspnet-core-mvc.html)

## Shouldly

# Shouldly

Shouldly is a .NET library that provides a set of extension methods for writing expressive and readable assertions in unit tests, it's designed to be an alternative to traditional assertion libraries. In the context of [ASP.NET](http://ASP.NET), Shouldly can be used in conjunction with test frameworks such as MSTest, xUnit, and NUnit to write more expressive and readable unit tests for the application. It provides advanced features such as support for collection-specific assertions, support for asynchronous code, and support for custom types, also includes options to customize the error message.

Visit the following resources to learn more:

- [@article@How to Use Shouldly to Improve Unit Tests in .NET?](https://code-maze.com/improve-unit-tests-shouldly-dotnet/)
- [@article@Improve Test Asserts with Shouldly](https://visualstudiomagazine.com/articles/2015/08/01/improve-test-asserts-with-shouldly.aspx?admgarea=ALM)

## Signalr Core

# SignalR Core

SignalR is a real-time communication library for .NET that allows for the creation of real-time web applications. SignalR Core is the latest version of SignalR, which has been rebuilt from the ground up to be cross-platform and lightweight. It allows for bidirectional communication between a client (such as a web page) and a server, enabling real-time updates, notifications, and other interactions. SignalR Core can be used in a variety of scenarios such as chat applications, gaming, and real-time dashboards. It supports multiple transports like WebSockets, Server-Sent Events and Long polling. It also supports for authentication and authorization.

Visit the following resources to learn more:

- [@article@Overview of ASP.NET Core SignalR](https://learn.microsoft.com/en-us/aspnet/core/signalr/introduction?view=aspnetcore-8.0)

## Singleton

# Singleton

Singleton lifetime is a type of dependency injection that creates a single instance of an object and reuses it throughout the lifetime of the application. This means that if multiple components within the same request or across different requests depend on the same service, they will all receive the same instance of the service.

Singleton lifetime is useful when you have services that need to maintain state or shared data across requests, such as a service that caches data or maintains a connection to a resource.

Visit the following resources to learn more:

- [@article@What are Singleton Dependencies?](https://blazor-university.com/dependency-injection/dependency-lifetimes-and-scopes/transient-dependencies/)
- [@article@Dependency Injection Lifetime](https://www.tektutorialshub.com/asp-net-core/asp-net-core-dependency-injection-lifetime/)
- [@video@Dependency Injection Explained with Singleton](https://www.youtube.com/watch?v=NkTF_6IQPiY)

## Solr

# Solr

Apache Solr is a search engine platform based on the Apache Lucene library. It is a standalone enterprise search server that provides a REST-like API for indexing, searching, and updating documents. Solr can be used to perform full-text search, faceted search, and geospatial search, among other things.

Solr can be useful in [ASP.NET](http://ASP.NET) application to provide advanced search capabilities, such as full-text search, faceted search and geospatial search, which can be useful in e-commerce, content management systems, and logging and monitoring applications. It is known for its scalability, performance and its ability to handle large volumes of data with complex queries.

Visit the following resources to learn more:

- [@article@Guide to Solr in ASP.NET](https://www.codeproject.com/Tips/480091/Using-Solr-for-Search-with-NET-Csharp)
- [@article@How to get Started with Solr.NET?](https://stackoverflow.com/questions/5646615/how-to-get-started-with-solr-net)
- [@article@Integrate Solr Instance With .NET Core](https://stacksecrets.com/dot-net-core/integrate-solr-instance-with-net-core)

## Specflow

# SpecFlow

SpecFlow is an open-source tool that allows developers to create automated acceptance tests in a natural language format, such as Gherkin. SpecFlow is commonly used in the context of [ASP.NET](http://ASP.NET) and other .NET technologies, to write acceptance tests for web applications. With SpecFlow, developers can write test scenarios using plain text in the Gherkin syntax, which uses a Given-When-Then format to describe the steps of a test. These scenarios can be written by non-technical stakeholders, such as business analysts or product owners, and can be easily understood by anyone who reads them. SpecFlow then converts these Gherkin scenarios into executable tests, which can be run using a variety of test runners, such as NUnit, xUnit, or MSTest. The tool also provides a set of bindings that allow developers to map the steps in the Gherkin scenarios to code in their application, making it easy to test specific functionality. Additionally, SpecFlow provides a set of advanced features, such as support for parameterized tests, background steps, and hooks, which allows developers to create more complex and powerful tests.

Visit the following resources to learn more:

- [@official@What is SpecFlow?](https://specflow.org/tools/specflow/)
- [@article@SpecFlow’s documentation](https://docs.specflow.org/_/downloads/specflow/en/latest/pdf/)
- [@article@Getting Started with SpecFlow](https://docs.specflow.org/projects/getting-started/en/latest/index.html)

## Sphinx

# Sphinx

Sphinx is an open-source full-text search engine that can be used to index, search and analyze large volumes of data quickly and in near real-time. It is designed to handle high-traffic websites and large data sets and can be used for full-text search, faceted search, and geospatial search.

In an [ASP.NET](http://ASP.NET) application, Sphinx can be integrated as a search engine to provide advanced search functionality to the application. There are several libraries available for integrating Sphinx with an [ASP.NET](http://ASP.NET) application, such as [SphinxQL.NET](http://SphinxQL.NET) and SphinxClient. These libraries provide a .NET client for Sphinx, which can be used to interact with the Sphinx engine from within an [ASP.NET](http://ASP.NET) application.

Visit the following resources to learn more:

- [@article@Overview of Sphinx in ASP.NET](https://www.sphinxconnector.net/)
- [@article@Intro to Sphinx](http://sphinxsearch.com/forum/view.html?id=3609)
- [@article@Documentation of Sphinx in ASP.NET](https://www.ericholscher.com/blog/2016/jul/1/sphinx-and-rtd-for-writers/)

## Sql Basics

# Sql basics

SQL stands for Structured Query Language. SQL lets you access and manipulate databases SQL became a standard of the American National Standards Institute (ANSI) in 1986, and of the International Organization for Standardization (ISO) in 1987.

Although SQL is an ANSI/ISO standard, there are different versions of the SQL language.

However, to be compliant with the ANSI standard, they all support at least the major commands (such as SELECT, UPDATE, DELETE, INSERT, WHERE) in a similar manner.

Visit the following resources to learn more:

- [@video@SQL Tutorial - Full Database Course for Beginners](https://www.youtube.com/watch?v=HXV3zeQKqGY)
- [@feed@Explore top posts about SQL](https://app.daily.dev/tags/sql?ref=roadmapsh)

## Sql Server

# SQL Server

MS SQL (or Microsoft SQL Server) is the Microsoft developed relational database management system (RDBMS). MS SQL uses the T-SQL (Transact-SQL) query language to interact with the relational databases. There are many different versions and editions available of MS SQL

Visit the following resources to learn more:

- [@article@MS SQL website](https://www.microsoft.com/en-ca/sql-server/)
- [@article@Tutorials for SQL Server](https://docs.microsoft.com/en-us/sql/sql-server/tutorials-for-sql-server-2016?view=sql-server-ver15)
- [@video@SQL Server tutorial for beginners](https://www.youtube.com/watch?v=-EPMOaV7h_Q)
- [@feed@Explore top posts about SQL](https://app.daily.dev/tags/sql?ref=roadmapsh)

## Steeltoe

# Steeltoe

Steeltoe is an open-source project that provides a set of libraries for building cloud-native applications on the .NET platform. The libraries are designed to work with the .NET Core runtime and provide a set of abstractions for common cloud-native patterns, such as service discovery, configuration management, and circuit breaking. The goal of Steeltoe is to make it easy for developers to take advantage of the cloud-native capabilities of the .NET platform and build resilient and scalable applications.

Visit the following resources to learn more:

- [@article@.NET Microservices with Steeltoe](https://learn.microsoft.com/en-us/shows/on-net/net-microservices-with-steeltoe)
- [@article@Steeltoe Documentation](https://docs.steeltoe.io/api/v3/welcome/index.html)
- [@video@.NET Microservices with Steeltoe](https://www.youtube.com/watch?v=QLRi6iPapVg)

## Stored Procedures

# Stored Procedures

A stored procedure is a pre-compiled collection of SQL statements that can be executed on a database server. Stored procedures are typically used to perform specific tasks, such as retrieving data from a database, inserting or updating data, or performing complex calculations. They are stored on the database server and can be called or executed from a client application or other stored procedures. Stored procedures can improve database performance by reducing the amount of SQL code needed to be executed and allowing developers to reuse common pieces of code. They can also provide security by allowing database administrators to control which users have access to specific stored procedures.

Visit the following resources to learn more:

- [@article@Stored Procedure in SQL: Benefits And How to Create It](https://www.simplilearn.com/tutorials/sql-tutorial/stored-procedure-in-sql)
- [@article@SQL Server stored procedures for beginners](https://www.sqlshack.com/sql-server-stored-procedures-for-beginners/)

## Stylecop Rules

# StyleCop Rules

StyleCop is a tool used for developers to standardize their code and ensure they all follow the same syntax principles. With StyleCop, one standard can be defined in a `stylecop.json` file and shared across your team so that each member has the same guidelines when formatting your code. Beyond a single project, StyleCop can also be added as an extension, so all of the projects on your IDE follow the same formatting rules, this is especially useful if your organization follows the same rule standards for all projects.

Visit the following resources to learn more:

- [@opensource@StyleCop GitHub official page](https://github.com/StyleCop/StyleCop)
- [@opensource@StyeleCop Analyzers, a more modern version of StyleCop](https://github.com/DotNetAnalyzers/StyleCopAnalyzers)
- [@article@StyleCop: A Detailed Guide to Starting and Using It](https://blog.submain.com/stylecop-detailed-guide/)
- [@video@The StyleCop setup and Advantages](https://www.youtube.com/watch?v=dmpOKmz3lPw)

## Task Scheduling

# Task Scheduling

Task scheduling in [ASP.NET](http://ASP.NET) refers to the process of scheduling and executing background tasks in an application. This can include tasks such as sending emails, processing data, generating reports, or performing maintenance tasks.

In [ASP.NET](http://ASP.NET), task scheduling can be implemented using a variety of libraries and frameworks such as [Quartz.NET](http://Quartz.NET), Hangfire, Coravel and Microsoft's built-in IHostedService interface. These libraries and frameworks provide a way to schedule tasks to run at specific times or intervals, and also provide APIs for managing and monitoring the progress of scheduled tasks.

Visit the following resources to learn more:

- [@article@How schedule Tasks in ASP.NET?](https://beansoftware.com/ASP.NET-Tutorials/Scheduled-Tasks.aspx)
- [@video@Task Scheduling in ASP.NET](https://www.youtube.com/watch?v=Vg4AOpb7OqA)

## Template Engines

# Template Engines

Template engines in [ASP.NET](http://ASP.NET) are libraries that allow developers to embed dynamic data in HTML templates. These engines are used to separate the logic of the application from the presentation of the data, making it easy to change the appearance of the application without having to change the underlying code.

Visit the following resources to learn more:

- [@article@Template Engine in ASP.NET](https://ej2.syncfusion.com/aspnetmvc/documentation/common/template-engine)
- [@article@How to Create Custom Templates using the .Net Template Engine ](https://www.infoq.com/articles/dotnet-core-template-engine/)

## Test Containers

# Test Containers

## Testing

# Testing

Testing in [ASP.NET](http://ASP.NET) is the process of evaluating the performance, functionality, and overall correctness of an application developed using the [ASP.NET](http://ASP.NET) framework. There are several types of testing that can be performed on an [ASP.NET](http://ASP.NET) application, including unit testing, integration testing, acceptance testing and E2E testing. Each type of testing has a different focus and is used at a different stage of the development process. Common testing frameworks for [ASP.NET](http://ASP.NET) include MSTest, XUnit, NUnit, Selenium, Playwright, Puppeteer, Cypress, Specflow, Cucumber, and LightBDD.

Visit the following resources to learn more:

- [@article@A Complete Tutorial on ASP.NET Testing](https://www.lambdatest.com/blog/aspnet-testing/)
- [@article@Unit test controller logic in ASP.NET](https://learn.microsoft.com/en-us/aspnet/core/mvc/controllers/testing?view=aspnetcore-7.0)
- [@article@Integration tests in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/test/integration-tests?view=aspnetcore-7.0)
- [@feed@Explore top posts about Testing](https://app.daily.dev/tags/testing?ref=roadmapsh)

## Transient

# Transient

Transient lifetime is a type of dependency injection that creates a new instance of an object each time it is requested. This means that if multiple components within the same request or across different requests depend on the same service, they will each receive a new instance of the service.

Transient lifetime is useful when you have services that are stateless and do not need to maintain any data between requests, such as a service that performs a simple calculation or returns data from a database.

Visit the following resources to learn more:

- [@article@What are Transient Dependencies?](https://blazor-university.com/dependency-injection/dependency-lifetimes-and-scopes/transient-dependencies/)
- [@article@Dependency Injection Lifetime](https://www.tektutorialshub.com/asp-net-core/asp-net-core-dependency-injection-lifetime/)
- [@video@Dependency Injection Explained with Transient](https://www.youtube.com/watch?v=NkTF_6IQPiY)

## Triggers

# Triggers

Triggers are special type of stored procedures that are automatically executed in response to specific events that occur within a database. These events can include:

*   Data modification events (INSERT, UPDATE, DELETE) on a specific table or view.
*   Data definition events (CREATE, ALTER, DROP) on specific database objects such as tables or views.
*   Logon events (CONNECT, DISCONNECT) that occur when a user connects to or disconnects from the database.

Visit the following resources to learn more:

- [@article@Database Triggers](https://docs.oracle.com/cd/A57673_01/DOC/server/doc/SCN73/ch15.htm)
- [@article@Database Triggers: Examples & Overview](https://study.com/academy/lesson/database-triggers-examples-overview.html)
- [@article@What are Triggers in SQL?](https://www.edureka.co/blog/triggers-in-sql/)
- [@article@What is a SQL Trigger?](https://www.essentialsql.com/sql-trigger/)

## Web Sockets

# Web Sockets

WebSockets is a protocol that allows for real-time, bidirectional communication between a client and a server. It is based on the same principle as HTTP, but it uses a different protocol to establish and maintain a connection between the client and the server. Once a connection is established, WebSockets enables the client and server to send messages to each other in real-time.

In [ASP.NET](http://ASP.NET), WebSockets can be used to create real-time, highly interactive web applications. The [ASP.NET](http://ASP.NET) Core framework provides built-in support for WebSockets through the Microsoft.AspNetCore.WebSockets package. This package provides a set of classes and methods that make it easy to create and manage WebSockets connections.

Visit the following resources to learn more:

- [@article@WebSockets support in ASP.NET](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/websockets?view=aspnetcore-7.0)
- [@article@Understanding WebSockets with ASP.NET](https://sahansera.dev/understanding-websockets-with-aspnetcore-5/)
- [@article@Writing a WebSocket server in ASP.NET](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API/Writing_WebSocket_server)

## Webapplicationfactory

# WebApplicationFactory

Web Application Factory (WAF) is a built-in feature of the [ASP.NET](http://ASP.NET) Core framework that allows developers to create and configure a web application in a programmatic way. It provides a simple and flexible way to set up a web application for testing, without the need for a web server or a browser. The WAF can be used to create a test server that can be used to run integration tests or end-to-end tests for an [ASP.NET](http://ASP.NET) Core web application, this allows developers to test the web application in a realistic environment, without the need for a physical web server or a browser. The WAF can be configured to use different services, middleware, and settings, depending on the needs of the application, this allows developers to easily set up a web application that is configured specifically for testing. The WAF also allows developers to test the web application against different configurations, such as different databases, different authentication providers, and different hosting environments.

Visit the following resources to learn more:

- [@article@Integration tests in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/test/integration-tests?view=aspnetcore-7.0)
- [@article@How to use WebApplicationFactory in .NET](https://stackoverflow.com/questions/69058176/how-to-use-webapplicationfactory-in-net6-without-speakable-entry-point)
- [@video@Integration Testing ASP.NET Core WebAPI Applications](https://www.youtube.com/watch?v=xs8gNQjCXw0)

## Xunit

# xUnit

xUnit is a unit testing framework for the .NET framework, it's an open-source testing framework that provides a set of attributes and classes that can be used to create unit tests. In the context of [ASP.NET](http://ASP.NET), xUnit can be used to write unit tests for web applications built using the [ASP.NET](http://ASP.NET) framework. xUnit provides features such as support for data-driven tests, support for parallel test execution, and support for test discovery and execution, it also provides support for test isolation which allows developers to run tests in isolation from each other. xUnit is a popular alternative to other testing frameworks like MSTest and it does not rely on a test runner, instead relies on a console runner that can be run from the command line.

Visit the following resources to learn more:

- [@article@Unit Testing with xUnit in ASP.NET Core](https://code-maze.com/aspnetcore-unit-testing-xunit/)
- [@article@Unit testing in .NET Core using and xUnit](https://learn.microsoft.com/en-us/dotnet/core/testing/unit-testing-with-dotnet-test)
- [@article@Getting Started With Unit Testing Using ASP.NET And xUnit](https://www.c-sharpcorner.com/article/getting-started-with-unit-testing-using-c-sharp-and-xunit/)

## Yarp

# YARP

YARP is a library to help create reverse proxy servers that are high-performance, production-ready, and highly customizable. YARP is built on .NET using the infrastructure from [ASP.NET](http://ASP.NET) and .NET (.NET 6 and newer). The key differentiator for YARP is that it's been designed to be easily customized and tweaked via .NET code to match the specific needs of each deployment scenario. YARP is designed with customizability as a primary scenario rather than requiring you to break out to script or rebuild the library from source.

Visit the following resources to learn more:

- [@article@Getting Started with YARP](https://microsoft.github.io/reverse-proxy/articles/getting-started.html)
- [@video@YARP: The .NET Reverse proxy](https://www.youtube.com/watch?v=1IqQkNcsqWE)
