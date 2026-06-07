# Spring Boot Roadmap

## Actuators

# Actuators

Spring Boot Actuators are a set of production-ready features in Spring Boot that allow you to monitor and manage your application in various ways. They provide a variety of endpoints that expose information about the health and performance of your application, and allow you to perform various management tasks such as shutting down the application or refreshing its configuration.

Spring Boot Actuators are typically used in production environments to monitor the health and performance of an application and identify any issues that may arise. They can also be used in development and testing environments to gain insight into the internal workings of the application.

Visit the following resources to learn more:

- [@official@Building a RESTful Web Service with Spring Boot Actuator](https://spring.io/guides/gs/actuator-service/)
- [@article@What is Spring Boot Actuator](https://www.baeldung.com/spring-boot-actuators)
- [@feed@Explore top posts about Spring Framework](https://app.daily.dev/tags/spring?ref=roadmapsh)

## Annotations

# Annotations

One of the key features of Spring Boot is its use of annotations, which are used to configure various aspects of the application and to enable certain features.

Some of the most commonly used annotations in Spring Boot include:

*   `@SpringBootApplication`
*   `@RestController`
*   `@Autowired`
*   `@Value`
*   `@Enable`
*   `@Configuration`
*   `@Bean`

These are just a few examples of the many annotations that are available in Spring Boot. There are many other annotations that you can use to configure various aspects of your application, such as security, caching, and data access.

Visit the following resources to learn more:

- [@article@Spring Annotations](https://www.digitalocean.com/community/tutorials/spring-annotations)
- [@article@Annotations in Spring](https://www.techferry.com/articles/spring-annotations.html)

## Architecture

# Architecture

The Spring MVC (Model-View-Controller) is a web application framework that is part of the Spring Framework. It is designed to make it easy to build web applications using the MVC design pattern.

Visit the following resources to learn more:

- [@article@Overview of Spring MVC Architecture](https://terasolunaorg.github.io/guideline/1.0.1.RELEASE/en/Overview/SpringMVCOverview.html)
- [@feed@Explore top posts about Architecture](https://app.daily.dev/tags/architecture?ref=roadmapsh)

## Architecture

# Architecture

Spring Boot follows a layered architecture in which each layer communicates with the layer directly below or above (hierarchical structure) it. The four layers in Spring Boot are as follows:

*   **Presentation Layer**: handles the HTTP requests, translates the JSON parameter to object, and authenticates the request and transfer it to the business layer.
*   **Business Layer**: The business layer handles all the business logic. It consists of service classes and uses services provided by data access layers. It also performs authorization and validation.
*   **Persistence Layer**: The persistence layer contains all the storage logic and translates business objects from and to database rows.
*   **Database Layer**: In the database layer, CRUD (create, retrieve, update, delete) operations are performed.

Visit the following resources to learn more:

- [@article@Spring Boot Architecture – Detailed Explanation](https://www.interviewbit.com/blog/spring-boot-architecture)
- [@feed@Explore top posts about Architecture](https://app.daily.dev/tags/architecture?ref=roadmapsh)

## Authentication

# Authentication

Spring Security is a framework for securing Java-based applications. One of its core features is authentication, which is the process of verifying that a user is who they claim to be. Spring Security provides a wide range of options for implementing authentication, including support for traditional username/password-based authentication as well as more modern alternatives such as OAuth and JSON Web Tokens (JWT).

Visit the following resources to learn more:

- [@official@Spring Authentication](https://docs.spring.io/spring-security/reference/features/authentication/index.html)
- [@official@Spring Security Authentication](https://spring.io/projects/spring-security)
- [@article@Spring Security Basic Authentication](https://www.baeldung.com/spring-security-basic-authentication)
- [@feed@Explore top posts about Authentication](https://app.daily.dev/tags/authentication?ref=roadmapsh)

## Authorization

# Authorization

Spring Security supports a variety of authentication mechanisms, such as username and password authentication, OAuth2, and more. Once a user is authenticated, Spring Security can then be used to authorize that user's access to specific resources or functionality. There are several annotations that can be used to control access to specific methods or classes.

Visit the following resources to learn more:

- [@official@Spring Authorization](https://docs.spring.io/spring-security/reference/servlet/authorization/index.html)
- [@article@Advanced authorization in Spring](https://docs.spring.io/spring-security/site/docs/5.2.11.RELEASE/reference/html/authorization.html)
- [@article@Spring Security: Authentication and Authorization In-Depth](https://www.marcobehler.com/guides/spring-security)
- [@feed@Explore top posts about Authorization](https://app.daily.dev/tags/authorization?ref=roadmapsh)

## Autoconfiguration

# Autoconfiguration

Spring Boot's Autoconfiguration is a powerful and convenient feature that makes it easy to configure beans and other components in your application based on the presence of certain dependencies and properties. It saves developer's time by reducing the need for boilerplate configuration code, and can be fine-tuned through properties and annotations, to provide a fine-grained control over the auto-configurations.

Visit the following resources to learn more:

- [@official@Auto-configuration using Spring Boot](https://docs.spring.io/spring-boot/docs/2.0.x/reference/html/using-boot-auto-configuration.html)

## Cloud Config

# Cloud Config

Spring Cloud Config is a library for managing configuration properties for distributed applications. It allows developers to externalize configuration properties for an application, so that they can be easily changed without modifying the application's code. It also provides a centralized server for storing and managing configuration properties for multiple applications, making it easy to update and rollback configurations across different environments.

Visit the following resources to learn more:

- [@official@Spring Cloud Config](https://spring.io/projects/spring-cloud-config)
- [@article@Quick Intro to Spring Cloud Configuration](https://www.baeldung.com/spring-cloud-configuration)
- [@article@Spring Boot - Cloud Configuration Server](https://www.tutorialspoint.com/spring_boot/spring_boot_cloud_configuration_server.htm)
- [@feed@Explore top posts about Cloud](https://app.daily.dev/tags/cloud?ref=roadmapsh)

## Components

# Components

The Spring MVC (Model-View-Controller) framework has several key components that work together to handle the requests and generate the appropriate responses in a web application.

There are other supporting components that are used to manage the lifecycle of the application's objects, such as the Spring IoC container and different interceptors that provides additional functionality, such as caching and security.

Visit the following resources to learn more:

- [@official@Web MVC Framework](https://docs.spring.io/spring-framework/docs/3.2.x/spring-framework-reference/html/mvc.html)

## Configuration

# Configuration

Spring Core Configuration is the process of configuring the Spring Framework, which involves specifying the various configuration details required for an application to function properly. This can include setting up beans, specifying bean dependencies, configuring aspect-oriented programming (AOP) aspects, and more. Configuration can be done through Java code, XML files, or using annotations in the code.

Visit the following resources to learn more:

- [@official@Spring Framework Documentation](https://docs.spring.io/spring/docs/current/spring-framework-reference/)
- [@article@"Spring Configuration" tutorial](https://www.baeldung.com/project-configuration-with-spring)
- [@article@"Spring Framework" tutorial](https://www.tutorialspoint.com/spring/index.htm)
- [@video@Spring Configuration | Spring Tutorial For Beginners](https://www.youtube.com/watch?v=fLs_yULL10g)

## Dependency Injection

# Dependency Injection

Spring Boot uses the Spring Framework's Inversion of Control (IoC) container to manage objects and their dependencies. The IoC container is responsible for creating objects, wiring them together, and managing their lifecycle. When an object is created, its dependencies are also created and injected into the object.

Visit the following resources to learn more:

- [@article@Spring Dependency Injection](https://www.baeldung.com/spring-dependency-injection)
- [@article@Dependency Injection Using Spring Boot](https://medium.com/edureka/what-is-dependency-injection-5006b53af782)
- [@video@Understanding Dependency Injection](https://www.youtube.com/watch?v=GB8k2-Egfv0)
- [@feed@Explore top posts about Dependency Injection](https://app.daily.dev/tags/dependency-injection?ref=roadmapsh)

## Embedded Server

# Embedded Server

Spring Boot's Embedded Server feature is a convenient and powerful feature that allows you to run a web server directly within your application, without the need to deploy it to a separate standalone web server. This makes it easy to develop, test, and deploy web applications, and it's also lightweight, easy to start and stop, and easy to configure.

Visit the following resources to learn more:

- [@official@Embedded Web Servers ‘How-to’ guides](https://docs.spring.io/spring-boot/docs/2.1.9.RELEASE/reference/html/howto-embedded-web-servers.html)
- [@article@Embedded Servers in Spring](https://subscription.packtpub.com/book/application-development/9781789132588/3/ch03lvl1sec24/embedded-servers)
- [@article@What is an Embedded Server? (Spring Boot)](https://www.springboottutorial.com/java-programmer-essentials-what-is-an-embedded-server)
- [@feed@Explore top posts about Embedded Systems](https://app.daily.dev/tags/embedded?ref=roadmapsh)

## Entity Lifecycle

# Entity lifecycle

In Hibernate, we can either create a new object of an entity and store it into the database, or we can fetch the existing data of an entity from the database. These entity is connected with the lifecycle and each object of entity passes through the various stages of the lifecycle.

There are mainly four states of the Hibernate Lifecycle :

*   Transient State
*   Persistent State
*   Detached State
*   Removed State

Visit the following resources to learn more:

- [@article@Hibernate Entity Lifecycle & and its state](https://www.baeldung.com/hibernate-entity-lifecycle)

## Eureka

# Eureka

Spring Cloud Eureka is a library for service discovery in a microservices-based architecture. Service discovery is a technique that allows services to find and communicate with each other, without having to hardcode their addresses.

Eureka is a service registry that allows service instances to register themselves and to discover other services by name. It provides a simple, consistent way for services to find and communicate with each other, and it integrates with other Spring Cloud libraries such as Ribbon and Feign to provide load balancing and declarative REST clients.

Visit the following resources to learn more:

- [@article@Introduction to Spring Cloud Netflix – Eureka](https://www.baeldung.com/spring-cloud-netflix-eureka)
- [@article@Spring Boot - Eureka Server](https://www.tutorialspoint.com/spring_boot/spring_boot_eureka_server.htm)
- [@video@Introducing Spring Cloud EUREKA](https://www.youtube.com/watch?v=1uNo1NrqsX4)
- [@feed@Explore top posts about Backend Development](https://app.daily.dev/tags/backend?ref=roadmapsh)

## Hibernate

# Hibernate

Hibernate is a Java framework that provides an object-relational mapping to an object-oriented model to the relational database. It means hibernate provides from Java classes to database tables and also provides data querying and retrieval facility.

Visit the following resources to learn more:

- [@article@Difference Between Spring vs Hibernate](https://www.educba.com/spring-vs-hibernate/)
- [@article@Spring Hibernate Integration Example](https://www.digitalocean.com/community/tutorials/spring-hibernate-integration-example-tutorial)

## Introduction

# Introduction

Spring Boot is a framework for building applications based on the Spring Framework, a widely-used, open-source framework for building Java-based enterprise applications. Spring Boot aims to make it easy to create stand-alone, production-grade Spring-based applications that you can "just run".

Visit the following resources to learn more:

- [@course@Spring Boot Course](https://spring.academy/courses/spring-boot)
- [@official@Spring Boot](https://spring.io/projects/spring-boot)
- [@article@Spring Boot - Introduction](https://www.tutorialspoint.com/spring_boot/spring_boot_introduction.htm)
- [@article@Introduction to Spring Boot](https://medium.com/adessoturkey/introduction-to-spring-boot-458cb814ec14)
- [@article@What-is-Spring-Boot?](https://www.ibm.com/topics/java-spring-boot)

## Jpa Test

# JPA Test

Spring JPA (Java Persistence API) is a library that makes it easy to work with databases and other data stores in a Spring application. Spring JPA uses the Java Persistence API (JPA) to interact with databases and provides an abstraction layer to work with different data stores.

Visit the following resources to learn more:

- [@article@Testing JPA Queries with Spring Boot and @DataJpaTest](https://reflectoring.io/spring-boot-data-jpa-test/)
- [@article@@DataJpaTest example for Spring Data Repository Unit Test](https://www.bezkoder.com/spring-boot-unit-test-jpa-repo-datajpatest/)
- [@article@Testing in Spring Boot](https://www.baeldung.com/spring-boot-testing)
- [@feed@Explore top posts about Java](https://app.daily.dev/tags/java?ref=roadmapsh)

## Jsp Files

# JSP Files

JSP (JavaServer Pages) is a technology for building dynamic web pages using Java.

In a Spring MVC application that uses JSPs, the view component of the MVC pattern is implemented using JSP files. The JSP files contain the presentation logic for the application and are responsible for generating the HTML that is sent to the client's web browser. When a user makes a request to a Spring MVC application, the DispatcherServlet, which acts as the front controller, handles the request and delegates responsibility for generating the response to the appropriate JSP file.

Visit the following resources to learn more:

- [@official@Spring MVC: from JSP and Tiles to Thymeleaf](https://spring.io/blog/2012/10/30/spring-mvc-from-jsp-and-tiles-to-thymeleaf/)
- [@article@Spring Boot With JavaServer Pages (JSP)](https://www.baeldung.com/spring-boot-jsp)

## Jwt Authentication

# JWT Authentication

Spring Security can be used to implement JWT Authentication and Authorization to your APIs. The library provides a JWT-based authentication filter that you can add to your API endpoints. The filter will check the JWT that is included in the request header, and if it is valid, it will set the authentication information in the security context. You can then use the security context to perform authorization checks on the API endpoints.

Visit the following resources to learn more:

- [@article@JWT Token Authentication in Spring](https://springframework.guru/jwt-authentication-in-spring-microservices-jwt-token/)
- [@article@Spring Security with JWT for REST API](https://www.toptal.com/spring/spring-security-tutorial)
- [@article@Spring Security - JWT](https://www.tutorialspoint.com/spring_security/spring_security_with_jwt.htm)
- [@feed@Explore top posts about Authentication](https://app.daily.dev/tags/authentication?ref=roadmapsh)

## Micrometer

# Micrometer

## Microservices

# Microservices

Spring Microservices is a framework that makes it easier to build and manage microservices-based applications using the Spring Framework. Microservices is an architectural style in which a large application is built as a collection of small, independently deployable services. Each service has a narrowly defined responsibility and communicates with other services through APIs.

Visit the following resources to learn more:

- [@official@Microservices with Spring](https://spring.io/microservices)
- [@article@Microservices with Spring Boot ](https://medium.com/omarelgabrys-blog/microservices-with-spring-boot-intro-to-microservices-part-1-c0d24cd422c3)
- [@feed@Explore top posts about Microservices](https://app.daily.dev/tags/microservices?ref=roadmapsh)

## Mock Mvc

# Mock MVC

Spring's MockMvc is a class that allows you to test Spring MVC controllers without the need for an actual web server. It is part of the Spring Test module, which provides a set of testing utilities for Spring applications.

Visit the following resources to learn more:

- [@article@Spring MockMVC tutorial](https://zetcode.com/spring/mockmvc/)
- [@article@Spring Boot MockMVC Example](https://howtodoinjava.com/spring-boot2/testing/spring-boot-mockmvc-example/)
- [@article@Integration Testing in Spring](https://baeldung.com/integration-testing-in-spring)

## Mockbean Annotation

# @MockBean Annotation

`MockBean` is a Spring annotation that can be used to create a mock implementation of a bean in the Spring application context. When a test is annotated with MockBean, Spring creates a mock implementation of the specified bean and adds it to the application context. The mock bean can then be used to replace the real bean during testing.

Visit the following resources to learn more:

- [@official@Annotation Interface MockBean](https://docs.spring.io/spring-boot/docs/current/api/org/springframework/boot/test/mock/mockito/MockBean.html)
- [@article@Mockito.mock() vs @Mock vs @MockBean](https://www.baeldung.com/java-spring-mockito-mock-mockbean)
- [@article@Spring Boot @MockBean Example](https://howtodoinjava.com/spring-boot2/testing/spring-mockbean-annotation/)

## Oauth2

# OAuth2

Spring Security OAuth2 library provides support for both the authorization code grant type (for web apps) and the implicit grant type (for single-page apps). You can also use Spring Security to protect your resources and to configure your application as an OAuth2 resource server. The OAuth2 authentication process can be complex and time-consuming, but the Spring Security OAuth2 library makes it easy to get started by providing a set of convenient configuration classes and annotations.

Visit the following resources to learn more:

- [@course@Securing a REST API with OAuth 2.0](https://spring.academy/courses/spring-academy-secure-rest-api-oauth2)
- [@article@OAuth 2 using Spring Boot](https://medium.com/@bubu.tripathy/oauth-2-using-spring-boot-99c17292f228)
- [@article@Spring Boot - OAuth2 with JWT](https://www.tutorialspoint.com/spring_boot/spring_boot_oauth2_with_jwt.htm)
- [@article@Spring Security](https://www.tutorialspoint.com/spring_security/spring_security_with_oauth2.htm)
- [@video@OAuth2 Login Made Easy in Java: A Spring Boot & Spring Security Walkthrough](https://www.youtube.com/watch?v=us0VjFiHogo)

## Relationships

# Relationships

Using hibernate, if we want to have relationship between two entities, there must exist a foreign key relationship between the tables, we call it as Referential integrity. The main advantage of having relationship between objects is, we can do operation on one object, and the same operation can transfer onto the other object in the database.

Visit the following resources to learn more:

- [@article@Hibernate Relationships In Depth](https://www.java4s.com/hibernate/hibernate-relationships-in-depth/)
- [@article@Guide to JPA with Hibernate - Relationship Mapping](https://stackabuse.com/a-guide-to-jpa-with-hibernate-relationship-mapping/)
- [@article@Hibernate Mapping](https://dzone.com/articles/hibernate-mapping)

## Servlet

# Servlet

A Spring servlet is a Java class that serves as the central point for handling requests and managing the lifecycle of the Spring IoC container. The Spring Framework provides a class called DispatcherServlet, which acts as the front controller in a Spring-based web application. When a user makes a request to a Spring web application, the DispatcherServlet is responsible for handling the request, delegating responsibility to other components, and ultimately returning a response to the user. The DispatcherServlet also manages the lifecycle of the Spring IoC container, including creating and initializing the container and making its beans available for use by other components in the application.

Visit the following resources to learn more:

- [@official@The DispatcherServlet](https://docs.spring.io/spring-framework/reference/web/webmvc/mvc-servlet.html)
- [@article@DispatcherServlet and web.xml in Spring Boot](https://www.baeldung.com/spring-boot-dispatcherservlet-web-xml)

## Spring Aop

# Spring AOP

Spring AOP (Aspect-Oriented Programming) is a feature of the Spring Framework that allows developers to define certain behaviors (i.e., "aspects") that cut across multiple classes, such as logging or transaction management. These behaviors, which are called "advices," can be applied to specific "join points" (i.e., points in the execution of a program) in the application, using "pointcuts" to determine where the advices should be applied.

Spring AOP allows developers to separate the implementation of these cross-cutting concerns from the business logic of the application, making the code more modular and easier to understand. This can also make the application more flexible, since the same advices can be applied to different parts of the code without having to duplicate the code for the advices themselves.

Visit the following resources to learn more:

- [@article@Spring AOP Tutorial](https://www.simplilearn.com/tutorials/spring-tutorial/spring-aop-aspect-oriented-programming)
- [@article@AOP with Spring Framework](https://www.tutorialspoint.com/spring/aop_with_spring.htm)
- [@article@Spring AOP Tutorial](https://howtodoinjava.com/spring-aop-tutorial/)
- [@feed@Explore top posts about Spring Framework](https://app.daily.dev/tags/spring?ref=roadmapsh)

## Spring Bean Scope

# Spring Bean Scope

In the Spring Framework, a bean is an object that is instantiated, assembled, and managed by the Spring IoC container. One of the key features of the Spring container is its ability to manage the lifecycle of beans, which includes creating, configuring, and destroying beans as necessary. One way the container can control the lifecycle of a bean is by specifying its scope.

Visit the following resources to learn more:

- [@article@Spring - Bean Scopes](https://www.tutorialspoint.com/spring/spring_bean_scopes.htm)
- [@article@Quick Guide to Spring Bean Scopes](https://www.baeldung.com/spring-bean-scopes)
- [@article@Spring Bean Scopes](https://www.digitalocean.com/community/tutorials/spring-bean-scopes)
- [@feed@Explore top posts about Spring Framework](https://app.daily.dev/tags/spring?ref=roadmapsh)

## Spring Boot Starters

# Spring Boot Starters

Spring Boot starters are a set of convenient dependency descriptors that you can include in your application. They provide a variety of functionality, such as security, data access, and web services, and help to minimize the amount of boilerplate code and configuration you need to write.

Visit the following resources to learn more:

- [@article@Intro to Spring Boot Starters](https://www.baeldung.com/spring-boot-starters)
- [@feed@Explore top posts about Spring Framework](https://app.daily.dev/tags/spring?ref=roadmapsh)

## Spring Cloud Circuit Breaker

# Circuit Breaker

Spring Cloud Circuit Breaker is a library for managing the fault tolerance of microservices-based applications using the Circuit Breaker pattern. The Circuit Breaker pattern is a design pattern that helps to prevent cascading failures and improve the resilience of distributed systems. It does this by introducing a "circuit breaker" proxy in front of a service that can detect when the service is unresponsive or has failed, and stop routing traffic to it temporarily, in order to allow the service to recover.

Visit the following resources to learn more:

- [@official@Spring Cloud Circuit Breaker](https://spring.io/projects/spring-cloud-circuitbreaker)
- [@article@Quick Guide to Spring Cloud Circuit Breaker](https://www.baeldung.com/spring-cloud-circuit-breaker)
- [@article@Spring Cloud - Circuit Breaker using Hystrix](https://www.tutorialspoint.com/spring_cloud/spring_cloud_circuit_breaker_using_hystrix.htm)
- [@feed@Explore top posts about Cloud](https://app.daily.dev/tags/cloud?ref=roadmapsh)

## Spring Cloud Gateway

# Spring Cloud Gateway

Spring Cloud Gateway is a Spring Framework library for building API gateways. An API gateway is a service that acts as an intermediary between an application and a set of microservices. The API gateway is responsible for request routing, composition, and protocol translation, among other things. It can also perform tasks such as authentication, rate limiting, and caching.

Visit the following resources to learn more:

- [@official@Spring Cloud Gateway](https://spring.io/projects/spring-cloud-gateway)
- [@article@What is Spring Cloud Gateway?](https://tanzu.vmware.com/developer/guides/scg-what-is/)
- [@article@Exploring the New Spring Cloud Gateway](https://www.baeldung.com/spring-cloud-gateway)
- [@feed@Explore top posts about Cloud](https://app.daily.dev/tags/cloud?ref=roadmapsh)

## Spring Cloud Open Feign

# Spring Cloud OpenFeign

Spring Cloud OpenFeign is a library for creating declarative REST clients in Spring applications. It allows developers to easily make HTTP requests to other microservices or remote services, without having to manually write the low-level code to handle the requests and responses. OpenFeign is built on top of the OpenFeign declarative HTTP client, which is a simple, lightweight library for creating HTTP clients in Java.

Visit the following resources to learn more:

- [@official@Spring Cloud OpenFeign](https://spring.io/projects/spring-cloud-openfeign)
- [@article@Introduction to Spring Cloud OpenFeign](https://www.baeldung.com/spring-cloud-openfeign)
- [@article@Simple Implementation of Spring Cloud OpenFeign](https://medium.com/javarevisited/simple-implementation-of-spring-cloud-openfeign-7f022630d01d)
- [@feed@Explore top posts about Cloud](https://app.daily.dev/tags/cloud?ref=roadmapsh)

## Spring Cloud

# Spring Cloud

Spring Cloud is a collection of libraries and tools for building cloud-native applications using the Spring Framework. It provides a set of abstractions and implementations for common patterns and best practices used in cloud-based applications, such as service discovery, configuration management, and circuit breaker patterns, among others.

Visit the following resources to learn more:

- [@official@Spring Cloud](https://spring.io/projects/spring-cloud)
- [@article@Spring Cloud – Bootstrapping](https://www.baeldung.com/spring-cloud-bootstrapping)
- [@feed@Explore top posts about Cloud](https://app.daily.dev/tags/cloud?ref=roadmapsh)

## Spring Data Jdbc

# Spring Data JDBC

Spring Data JDBC is a part of the Spring Data project that provides support for using JDBC (Java Database Connectivity) to interact with relational databases. It is designed to provide a simple and consistent programming model for interacting with databases using JDBC, while still allowing for the full power of JDBC to be used if needed. Spring Data JDBC provides a set of abstraction and utility classes that simplify the task of working with databases, such as a simple template class for executing SQL queries, a repository abstraction for implementing data access objects (DAOs), and support for pagination and sorting of query results. It works with both Java and Kotlin.

Visit the following resources to learn more:

- [@official@Spring Data JDBC](https://spring.io/projects/spring-data-jdbc)
- [@article@Spring Data JDBC - Reference Documentation](https://docs.spring.io/spring-data/jdbc/docs/current/reference/html/)
- [@article@Introduction to Spring Data JDBC](https://www.baeldung.com/spring-data-jdbc-intro)
- [@feed@Explore top posts about Spring Framework](https://app.daily.dev/tags/spring?ref=roadmapsh)

## Spring Data Jpa

# Spring Data JPA

Spring Data JPA is a library that makes it easy to implement Java Persistence API (JPA) based repositories (a fancy word for "DAO") for Spring applications. It's an abstraction on top of JPA that allows you to use a simpler and more convenient API for performing CRUD (Create, Read, Update, Delete) operations on databases. Spring Data JPA also provides additional functionality such as pagination, dynamic query generation, and more.

Visit the following resources to learn more:

- [@official@Spring Data JPA](https://spring.io/projects/spring-data-jpa)
- [@article@Introduction to Spring Data JPA](https://www.baeldung.com/the-persistence-layer-with-spring-data-jpa)
- [@feed@Explore top posts about Spring Framework](https://app.daily.dev/tags/spring?ref=roadmapsh)

## Spring Data Mongodb

# Spring Data Mongodb

Spring Data for MongoDB is part of the umbrella Spring Data project which aims to provide a familiar and consistent Spring-based programming model for new datastores while retaining store-specific features and capabilities

The Spring Data MongoDB project provides integration with the MongoDB document database. Key functional areas of Spring Data MongoDB are a POJO centric model for interacting with a MongoDB DBCollection and easily writing a Repository style data access layer.

Visit the following resources to learn more:

- [@official@Spring Data MongoDB](https://spring.io/projects/spring-data-mongodb)
- [@official@Spring Boot Integration with MongoDB Tutorial](https://www.mongodb.com/compatibility/spring-boot)
- [@article@Introduction to Spring Data MongoDB](https://www.baeldung.com/spring-data-mongodb-tutorial)
- [@feed@Explore top posts about MongoDB](https://app.daily.dev/tags/mongodb?ref=roadmapsh)

## Spring Data

# Spring Data

Spring Data is a collection of projects for data access in Spring-based applications. It provides a common interface for working with various types of data stores, including relational databases, NoSQL data stores, and cloud-based data services. The goal of Spring Data is to simplify data access in Spring applications by providing a consistent, high-level repository programming model across different data stores and data access technologies. This can help developers write less boilerplate code and focus on business logic, while still being able to take advantage of the full power of the underlying data store.

Visit the following resources to learn more:

- [@official@Spring Data](https://spring.io/projects/spring-data)
- [@article@Spring Data – One API To Rule Them All?](https://www.infoq.com/articles/spring-data-intro/)
- [@article@What is JPA, Spring Data and Spring Data JPA](https://www.amitph.com/jpa-and-spring-data-jpa/)
- [@feed@Explore top posts about Spring Framework](https://app.daily.dev/tags/spring?ref=roadmapsh)

## Spring Ioc

# Spring IOC

Inversion of Control (IoC) is a design pattern that is often used in conjunction with the Dependency Injection (DI) pattern. The basic idea behind IoC is to invert the flow of control in a program, so that instead of the program controlling the flow of logic and the creation of objects, the objects themselves control the flow of logic and the creation of other objects.

Spring is a popular Java framework that uses IoC and DI to provide a more flexible, modular approach to software development. The Spring IoC container is responsible for managing the creation and configuration of objects in a Spring-based application.

Visit the following resources to learn more:

- [@article@Spring IoC, Spring Bean Example Tutorial](https://www.digitalocean.com/community/tutorials/spring-ioc-bean-example-tutorial)
- [@article@Intro to Inversion of Control with Spring](https://www.baeldung.com/inversion-control-and-dependency-injection-in-spring)
- [@feed@Explore top posts about Spring Framework](https://app.daily.dev/tags/spring?ref=roadmapsh)

## Spring Mvc

# Spring MVC

Spring MVC is a framework for building web applications in Java. It is part of the Spring Framework, which is a larger ecosystem of tools for building Java applications. Spring MVC is built on the Model-View-Controller (MVC) design pattern, which helps to separate the concerns of the application into three distinct components: the Model, the View, and the Controller.

Spring MVC provides a powerful and flexible way to build web applications, and it integrates well with other parts of the Spring ecosystem, such as Spring Security for authentication and authorization, and Spring Data for data access.

Visit the following resources to learn more:

- [@official@Web MVC framework](https://docs.spring.io/spring-framework/docs/3.2.x/spring-framework-reference/html/mvc.html)
- [@article@Spring - MVC Framework](https://www.tutorialspoint.com/spring/spring_web_mvc_framework.htm)
- [@feed@Explore top posts about Spring Framework](https://app.daily.dev/tags/spring?ref=roadmapsh)

## Spring Mvc

# Spring MVC

Spring MVC is a web application framework that is part of the Spring Framework. It is designed to make it easy to build web applications using the Model-View-Controller (MVC) design pattern.

In Spring MVC, the application is divided into three main components: the Model, the View, and the Controller. The Model represents the data and the business logic of the application, the View is responsible for generating the HTML that is sent to the client's web browser, and the Controller acts as an intermediary between the Model and the View, handling incoming HTTP requests and generating the appropriate response.

Visit the following resources to learn more:

- [@article@Spring - MVC Framework](https://www.tutorialspoint.com/spring/spring_web_mvc_framework.htm)
- [@article@Spring MVC Tutorial – Everything You Need To Know](https://www.edureka.co/blog/spring-mvc-tutorial/)
- [@feed@Explore top posts about Spring Framework](https://app.daily.dev/tags/spring?ref=roadmapsh)

## Spring Security

# Spring security

Spring Security is a framework for securing Java-based applications. It is a powerful and highly customizable authentication and access-control framework that can be easily integrated with a wide variety of applications, including web applications and RESTful web services. Spring Security provides a comprehensive security solution for both authentication and authorization, and it can be used to secure applications at both the web and method level.

Visit the following resources to learn more:

- [@official@Spring Security](https://spring.io/projects/spring-security)
- [@article@What is Spring security](https://www.javadevjournal.com/spring/what-is-spring-security/)
- [@article@Spring Security: Authentication and Authorization In-Depth](https://www.marcobehler.com/guides/spring-security)
- [@feed@Explore top posts about Security](https://app.daily.dev/tags/security?ref=roadmapsh)

## Springboottest Annotation

# @SpringBootTest annotation

`@SpringBootTest` This annotation is used to create a fully-configured instance of the Spring ApplicationContext for testing. It can be used to test the application's components, including controllers, services, and repositories, in a real application environment.

Visit the following resources to learn more:

- [@official@Annotation Interface SpringBootTest](https://docs.spring.io/spring-boot/docs/current/api/org/springframework/boot/test/context/SpringBootTest.html)
- [@article@Testing with Spring Boot and @SpringBootTest](https://reflectoring.io/spring-boot-test/)
- [@article@Testing in Spring Boot](https://www.baeldung.com/spring-boot-testing)
- [@feed@Explore top posts about Spring Framework](https://app.daily.dev/tags/spring?ref=roadmapsh)

## Terminology

# Terminology

Spring Core, the base of the Spring Framework, provides a model for configuring Java applications. Key concepts include **Beans** (Java objects managed by Spring), **Inversion of Control (IoC)** (Spring managing bean lifecycles and dependencies), and **Dependency Injection (DI)** (Spring providing bean dependencies). The **Spring container** (specifically an **ApplicationContext**) creates and manages these beans. Spring also offers **Aspect-Oriented Programming (AOP)** for handling cross-cutting concerns, an **event model** for decoupled communication using **ApplicationEvent** and **listeners**, abstractions for **Data Access** and **Transactions**, and utilities for **Task Execution and Scheduling**.

Visit the following resources to learn more:

- [@official@Spring Boot](https://spring.io/projects/spring-boot)
- [@official@Spring Boot - Starter Guide](https://spring.io/quickstart)

## Testing

# Testing

Spring provides a set of testing utilities that make it easy to test the various components of a Spring application, including controllers, services, repositories, and other components. It has a rich set of testing annotations, utility classes and other features to aid in unit testing, integration testing and more.

Visit the following resources to learn more:

- [@article@What Is Spring Testing?](https://www.developer.com/design/what-is-spring-testing/)
- [@article@Complete Guide To Spring Testing](https://www.lambdatest.com/blog/spring-testing/)
- [@feed@Explore top posts about Testing](https://app.daily.dev/tags/testing?ref=roadmapsh)

## Transactions

# Transactions

A transaction simply represents a unit of work. In such case, if one step fails, the whole transaction fails (which is termed as atomicity). A transaction can be described by ACID properties (Atomicity, Consistency, Isolation and Durability).

In hibernate framework, we have Transaction interface that defines the unit of work. It maintains abstraction from the transaction implementation (JTA,JDBC).

Visit the following resources to learn more:

- [@official@Hibernate Transactions](https://docs.hibernate.org/orm/current/userguide/html_single/#transactions)
- [@article@Hibernate Transaction Management](https://www.javaguides.net/2018/12/hibernate-transaction-management-tutorial.html)

## Why Use Spring

# Why Spring

Spring Boot provides a number of features that make it easier to create a Spring-based application, including:

*   Embedded Application Server
*   Automatic Configuration
*   Pre-configured Starters
*   Ease of Packaging and Distribution
*   Ease of monitoring through built-in health check endpoint and the ability to customize the management endpoint.

Additionally, it's come with a lot of best practices and conventions baked in, which reduces the amount of work and boiler plate code developers need to write.

Visit the following resources to learn more:

- [@official@Why Spring?](https://spring.io/why-spring)
- [@article@Spring vs Spring Boot: Know The Difference](https://www.interviewbit.com/blog/spring-vs-spring-boot)
- [@article@A Comparison Between Spring and Spring Boot](https://www.baeldung.com/spring-vs-spring-boot)
- [@article@Advantages of Spring Boot](https://www.adservio.fr/post/advantages-of-spring-boot)
- [@feed@Explore top posts about Spring Framework](https://app.daily.dev/tags/spring?ref=roadmapsh)
