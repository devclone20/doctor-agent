# Software Design Architecture Roadmap

## Abstract Classes

# Abstract Classes

An abstract class is a class in object-oriented programming (OOP) that cannot be instantiated. Instead, it serves as a template or blueprint for other classes to inherit from. An abstract class can contain both abstract and non-abstract methods (abstract methods are methods that do not have any implementation, they just have a signature).

Abstract classes are used to provide a common interface and implementation for a group of related classes. They are also used to define common behavior that must be implemented by all subclasses. A subclass that inherits from an abstract class is called a concrete class, and it must provide an implementation for all the abstract methods declared in the parent class.

Visit the following resources to learn more:

- [@article@What is an Abstract Class in Object Oriented Programming](https://www.theserverside.com/definition/abstract-class)

## Abstraction

# Abstraction

Abstraction is a concept in object-oriented programming (OOP) that refers to the process of hiding the implementation details of an object and exposing only its essential features. It enables the use of objects without the need to understand the underlying complexity of their internal structure and behavior.

There are two types of abstraction:

*   Data abstraction: refers to hiding the internal representation of data and providing a simplified view of the data through a set of well-defined interfaces.
*   Behavioral abstraction: refers to hiding the internal behavior of an object and providing a simplified view of its capabilities through a set of well-defined interfaces.

Visit the following resources to learn more:

- [@video@Tutorial - Abstraction](https://www.youtube.com/watch?v=OF55HZPE7lQ)

## Anemic Models

# Anemic Models

An Anemic model, also known as an anemic domain model, is a type of domain model in which the domain objects only contain data (attributes) and lack behavior. An anemic model often results in the use of data-transfer objects (DTOs) and service layer to handle the behavior.

An anemic model is considered an anti-pattern in object-oriented programming (OOP) because it violates the principles of encapsulation and separation of concerns. In an anemic model, the behavior is separated from the data, and is typically implemented in a separate service layer, which can lead to a complex, tightly coupled, and hard-to-maintain codebase.

Visit the following resources to learn more:

- [@article@Overview of Anemic Domain Model](https://en.wikipedia.org/wiki/Anemic_domain_model)

## Architectural Patterns

# Architectural Patterns

## Architectural Patterns

# Architectural Patterns

Architectural patterns are a set of solutions that have been proven to work well for specific types of software systems. They provide a common vocabulary and set of best practices for designing and building software systems, and can help developers make better design decisions. Some common architectural patterns include:

*   Model-View-Controller (MVC): A pattern for separating the user interface, business logic, and data storage components of a system.
*   Microservices: A pattern for building systems as a collection of small, independently deployable services that communicate over a network.
*   Event-Driven: A pattern for building systems that respond to events and perform actions in response.
*   Layered: A pattern for organizing a system into layers, with each layer providing a specific set of services to the layer above it.
*   Pipe-and-Filter: A pattern for building systems as a series of independent, reusable processing elements that are connected together in a pipeline.
*   Command-Query Responsibility Segregation (CQRS): A pattern for separating the handling of commands (which change the state of the system) from the handling of queries (which retrieve information from the system)
*   Blackboard: A pattern for creating a centralized repository of information that can be accessed and modified by multiple independent modules or subsystems.
*   Microkernel: A pattern that aims to minimize the amount of code running in kernel mode and move as much functionality as possible into user-mode processes.
*   Serverless: A design pattern that allows developers to build and run applications and services without having to provision and manage servers.
*   Message Queues and Streams: A pattern that decouples different components of a system and enables asynchronous communication between them.
*   Event Sourcing: A pattern that stores all changes to the system's state as a sequence of events, rather than just the current state.

Visit the following resources to learn more:

- [@article@Overview - Architectural Pattern](https://en.wikipedia.org/wiki/Architectural_pattern)
- [@video@Architecture Patterns Used In Enterprise Software Development](https://www.youtube.com/watch?v=BrT3AO8bVQY)

## Architectural Principles

# Architectural Principles

Architectural principles refer to a set of guidelines or rules that are used to guide the design and development of a software architecture. These principles are intended to ensure that the resulting architecture is maintainable, scalable, and easy to understand and modify. Some common architectural principles include the separation of concerns, modularity, loose coupling, and high cohesion. Additionally, architectural principles are often used in conjunction with design patterns, which are reusable solutions to common software design problems.

Visit the following resources to learn more:

- [@article@Intro to Architectural Principles](https://learn.microsoft.com/en-us/dotnet/architecture/modern-web-apps-azure/architectural-principles)
- [@video@Principles of Software Design](https://www.youtube.com/watch?v=TO9igqkPtfc)

## Architectural Principles

# Architectural Principles

## Architectural Styles

# Architectural Styles

Architectural styles are sets of principles and constraints that define the characteristics of a software system. They provide a vocabulary and a framework for describing common system properties such as structure, behavior, and interaction. These styles act as blueprints, offering reusable solutions to recurring design problems and guiding the organization of components and their relationships within a software architecture. Examples of architectural styles include layered architecture, microservices, and event-driven architecture, each with its own strengths and weaknesses that make it suitable for specific scenarios.

Visit the following resources to learn more:

- [@video@Types of Architectural Styles in Software Engineering](https://www.youtube.com/watch?v=2Pp0BcXN9YY)
- [@video@10 Architecture Patterns Used In Enterprise Software Development Today](https://www.youtube.com/watch?v=brt3ao8bvqy)

## Architectural Styles

# Architectural Styles

Architectural styles in software refer to the overall design and organization of a software system, and the principles and patterns that are used to guide the design. These styles provide a general framework for the design of a system, and can be used to ensure that the system is well-structured, maintainable, and scalable.

Some common architectural styles in software include:

*   Microservices: where the system is built as a collection of small, independent, and loosely-coupled services.
*   Event-Driven: where the system reacts to specific events that occur, rather than being continuously polled for changes.
*   Layered: where the system is divided into a set of layers, each of which has a specific responsibility and communicates with the other layers through well-defined interfaces.
*   Service-Oriented: where the system is built as a collection of services that can be accessed over a network.
*   Data-Centric: where the system is focused on the storage, retrieval and manipulation of data, rather than the processing of data.
*   Component-Based: where the system is composed of reusable and independent software components.
*   Domain-Driven: where the system is organized around the core business domain and business entities.

Visit the following resources to learn more:

- [@article@What is Software Architecture & Styles?](https://study.com/academy/lesson/software-architecture-styles-patterns-components.html)
- [@video@Types of Architectural Styles in Software Engineering](https://www.youtube.com/watch?v=2Pp0BcXN9YY)
- [@video@10 Architecture Patterns Used In Enterprise Software Development Today](https://www.youtube.com/watch?v=brt3ao8bvqy)

## Avoid Passing Nulls Booleans

# Avoid Passing Nulls Booleans

Passing nulls or Booleans can lead to unexpected behavior and difficult-to-debug errors in a program. Here are some ways to avoid passing nulls or Booleans in system architecture:

*   Use Optionals or Maybe types instead of nulls to indicate the absence of a value. This makes it clear when a value is missing and prevents null reference exceptions.
*   Use a default value for function arguments instead of allowing them to be null or Boolean. This eliminates the need to check for null or Boolean values and reduces the potential for errors.
*   Use the Null Object pattern to replace null values with a special object that has a defined behavior. This eliminates the need to check for null values and makes the code more readable.
*   Use the Ternary operator (?:) instead of if-else statements when working with Booleans. This can make the code more concise and easier to read.
*   Use the assert function to check the validity of function arguments and throw an exception if they are invalid.

By following these best practices, the system architecture will be more robust and less error-prone.

## Be Consistent

# Be Consistent

Being consistent refers to maintaining a consistent pattern. This can include using consistent naming conventions, data structures, and interfaces throughout the system, as well as adhering to established design principles and best practices. Consistency can help to make the system more maintainable, understandable, and extendable.

Visit the following resources to learn more:

- [@article@10 Tips for Writing Clean Code](https://www.pluralsight.com/blog/software-development/10-steps-to-clean-code)

## Blackboard Pattern

# Blackboard Pattern

The Blackboard architectural pattern is a software design pattern that allows for the creation of a centralized repository of information that can be accessed and modified by multiple independent modules or subsystems. The blackboard serves as a communication and coordination mechanism between these modules, allowing them to share information and collaborate to achieve a common goal. This pattern is often used in artificial intelligence and decision-making systems, where multiple processes or agents need to share and reason over complex data.

Visit the following resources to learn more:

- [@article@Overview of Blackboard (design pattern)](https://en.wikipedia.org/wiki/Blackboard_(design_pattern))
- [@article@Architectural Patterns: Blackboard](http://www.openloop.com/softwareEngineering/patterns/architecturePattern/arch_Blackboard.htm)

## Boundaries

# Boundaries

In software architecture, boundaries refer to the interfaces or the points of separation between different components or systems. These boundaries can be physical, such as between different microservices in a distributed system, or logical, such as between different layers in an application.

Boundaries are important because they define the points of interaction between different components or systems, and they dictate how those components or systems will communicate with each other. By defining clear boundaries, it makes it easier to understand, test, and maintain the system, as the interactions between components or systems are well-defined and easy to reason about.

Visit the following resources to learn more:

- [@article@Boundaries in Software Architecture](https://www.open.edu/openlearn/science-maths-technology/approaches-software-development/content-section-1.1.4)

## Class Variants

# Class Invariants

A class invariant is a set of conditions that must be true for any object of a class, at any point in time. In object-oriented programming (OOP), class invariants are used to define the valid states of an object and to ensure that the object always remains in a valid state.

Class invariants are typically defined in the constructor of a class and are enforced through the use of private methods and data members that are used to validate the state of the object. They are also checked in the class's methods before and after any operation that can change the state of the object.

Visit the following resources to learn more:

- [@article@Overview of Class invariant](https://en.wikipedia.org/wiki/Class_invariant)
- [@article@The concept of class invariant in object-oriented programming](https://arxiv.org/abs/2109.06557)

## Clean Code Principles

# Clean Code Principles

Clean code principles are guidelines for writing code that is easy to understand, maintain, and modify. These principles emphasize readability, simplicity, and reducing complexity to improve collaboration and reduce the likelihood of errors. Ultimately, the goal is to create source code that is as easy to read and understand as well-written prose.

Visit the following resources to learn more:

- [@article@Introduction to Clean Code & Software Design Principles](https://workat.tech/machine-coding/tutorial/introduction-clean-code-software-design-principles-nwu4qqc63e09)
- [@feed@Explore top posts about General Programming](https://app.daily.dev/tags/general-programming?ref=roadmapsh)

## Clean Code

# Clean Code Principles

Clean code is code that is easy to read, understand, and maintain. It follows a set of principles that are designed to make the code more readable, testable, and less error-prone. Some of the key principles of clean code include:

*   Clarity: The code should be easy to read and understand.
*   Simplicity: The code should be as simple as possible, avoiding unnecessary complexity.
*   Comments: Comments should be used sparingly and only when necessary to explain complex or non-obvious code.
*   Naming: Variables, functions, and classes should have meaningful and descriptive names.
*   Formatting: The code should be consistently formatted to improve readability.
*   Functionality: The code should be organized into small, single-purpose functions and classes.
*   Error handling: The code should handle errors in a consistent and predictable way.
*   Testing: The code should be testable and have a high test coverage.
*   Reusability: The code should be designed to be reusable and modular.
*   Performance: The code should be designed to be efficient and performant.

Visit the following resources to learn more:

- [@article@Introduction to Clean Code & Software Design Principles](https://workat.tech/machine-coding/tutorial/introduction-clean-code-software-design-principles-nwu4qqc63e09)
- [@feed@Explore top posts about General Programming](https://app.daily.dev/tags/general-programming?ref=roadmapsh)

## Client Server

# Client Server

The client-server architecture is a common architecture pattern used in distributed systems, where a client (or multiple clients) send requests to a server, and the server responds to those requests. The client and server are separate entities that communicate over a network, such as the Internet or a local network.

The client is responsible for presenting the user interface and handling user input, while the server is responsible for processing the requests and returning the appropriate response. The server can also handle tasks such as data storage, security, and business logic.

Visit the following resources to learn more:

- [@article@Intro to Client-server Architecture](https://cs.uwaterloo.ca/~m2nagapp/courses/CS446/1195/Arch_Design_Activity/ClientServer.pdf)

## Command Query Separation

# Command Query Separation

Command-Query Separation (CQS) is a software design principle that separates the responsibilities of a method or function into two categories: commands and queries. Commands are methods that change the state of the system, while queries are methods that return information but do not change the state of the system.

Visit the following resources to learn more:

- [@article@CQS Pattern](https://martinfowler.com/bliki/CommandQuerySeparation.html)

## Commands  Queries

# Commands Queries

The Command and Query Responsibility Segregation (CQRS) pattern is a technique used in enterprise application development to separate the responsibilities of handling command (write) operations and query (read) operations for performing actions that change the state of the system, such as creating, updating, or deleting data. These operations are handled by Command Handlers, which are responsible for validating the data and executing the appropriate business logic.

Queries are used for retrieving data from the system, such as reading data from a database or a cache. These operations are handled by Query Handlers, which are responsible for executing the appropriate query and returning the data to the caller.

Visit the following resources to learn more:

- [@article@Get Started with CQRS Pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/cqrs)

## Component Based

# Component Based

In software architecture, component-based design (CBD) is an approach to designing software systems by composing them from a set of reusable and independent software components. These components encapsulate specific functionality and can be easily integrated into different parts of the system, allowing for a more modular and flexible design.

In CBD, a software system is divided into a set of components, each of which has a well-defined interface and a specific responsibility. These components can be developed, tested, and deployed independently, making it easier to add new features, modify existing ones, and maintain the system.

Visit the following resources to learn more:

- [@article@Component Based Software architecture](https://www.tutorialspoint.com/software_architecture_design/component_based_architecture.htm)

## Component Principles

# Component Principles

Component principles in software architecture refer to guidelines for designing and implementing software components that are modular, reusable, and easy to understand, test, and maintain. Some of the key component principles in software architecture include:

*   High cohesion
*   Low coupling
*   Separation of concerns
*   Interface-based design
*   Reusability
*   Testability
*   Modularity
*   Interoperability

By following these component principles, software can be developed in a way that is easy to understand, maintain, and extend, and that is less prone to bugs. It also enables better code reuse, and makes it easier to test and change the code, and also enables better code reuse, as components can be reused in different contexts.

Visit the following resources to learn more:

- [@article@Component-Based Architecture](https://www.tutorialspoint.com/software_architecture_design/component_based_architecture.htm)

## Composition Over Inheritance

# Composition over Inheritance

Composition over inheritance is a programming principle that suggests that it is better to use composition, a mechanism for assembling objects, to create complex objects, rather than using inheritance, which is a mechanism for creating new classes based on existing ones.

Inheritance is a powerful mechanism for creating reusable code, but it can also lead to tightly coupled, hard-to-maintain code. This is because inherited classes are tightly bound to their parent classes and any changes made to the parent class will affect all of its child classes. This makes it hard to change or extend the code without affecting the entire class hierarchy.

Visit the following resources to learn more:

- [@article@Overview of Composition over Inheritance](https://en.wikipedia.org/wiki/Composition_over_inheritance)
- [@video@Tutorial - Composition over Inheritance](https://www.youtube.com/watch?v=wfMtDGfHWpA)
- [@video@Composition over Inheritance Explained by Games](https://www.youtube.com/watch?v=HNzP1aLAffM&list=PLCl5BUbK0jXt5l18S5UNAoUc4eQ2PJDye)

## Concrete Classes

# Concrete Classes

A concrete class is a class in object-oriented programming (OOP) that can be instantiated, meaning objects can be created from it. A concrete class is a class that provides an implementation for all of the abstract methods declared in its parent class, if it inherits from an abstract class. A concrete class can also be a class that does not inherit from an abstract class, in that case it can have implementation for all of its methods.

Concrete classes are used to provide specific implementation details for a group of related classes that inherit from a common abstract class. They are also used to define unique behavior for a specific class. A concrete class can have its own methods and variables, and can also override the methods of its parent class.

## Coupling And Cohesion

# Coupling and Cohesion

Coupling and cohesion are two principles in software architecture that are used to measure the degree of interdependence between components in a system.

Coupling refers to the degree to which one component depends on another component. High coupling means that a change in one component will likely affect other components, making the system more difficult to understand, test, and maintain. Low coupling, on the other hand, means that changes to one component have minimal impact on other components, making the system more modular and easier to understand, test, and maintain.

Cohesion, on the other hand, refers to the degree to which the responsibilities of a component are related to each other. High cohesion means that a component has a single, well-defined purpose and that all its functionality and data is related to that purpose. Low cohesion, on the other hand, means that a component has multiple, unrelated responsibilities, making it more difficult to understand, test, and maintain.

Visit the following resources to learn more:

- [@video@Cohesion and Coupling in Software Engineering](https://www.youtube.com/watch?v=NweTzHYBgYU)

## Cqrs

# CQRS

CQRS (Command Query Responsibility Segregation) is an architectural pattern that is used to separate the responsibilities of reading and writing data in a software system. In a CQRS architecture, the system is divided into two separate parts: the command side and the query side.

The command side is responsible for processing commands and updating the system's state, while the query side is responsible for reading the current state of the system and returning the results to the client. The command and query sides can use different data models, storage mechanisms, and even different technologies.

Visit the following resources to learn more:

- [@article@Get Started with CQRS Pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/cqrs)
- [@article@CQRS Software Architecture Pattern: The Good, Bad, and the Ugly](https://betterprogramming.pub/cqrs-software-architecture-pattern-the-good-the-bad-and-the-ugly-e9d6e7a34daf)

## Design Patterns

# Design Patterns

Design patterns are general solutions to common problems that arise in software development. They provide a way to describe and communicate proven solutions to common design problems and they provide a common vocabulary for design. They are not specific to any particular programming language or technology, but rather describe the problem and the solution in a way that can be applied to many different contexts.

There are several different types of design patterns, including:

*   Creational patterns
*   Structural patterns
*   Behavioral patterns
*   Architectural patterns

Visit the following resources to learn more:

- [@article@Overview - Software Design Pattern](https://en.wikipedia.org/wiki/Software_design_pattern)
- [@article@Explaining, imaging and simplifying design patterns](https://refactoring.guru/design-patterns/what-is-pattern)
- [@video@What Are Design Patterns?](https://www.youtube.com/watch?v=BWprw8UHIzA)
- [@feed@Explore top posts about Design Patterns](https://app.daily.dev/tags/design-patterns?ref=roadmapsh)

## Design Patterns

# Design Patterns

Design patterns are general solutions to common problems that arise in software development. They provide a way to describe and communicate proven solutions to common design problems and they provide a common vocabulary for design. They are not specific to any particular programming language or technology, but rather describe the problem and the solution in a way that can be applied to many different contexts.

There are several different types of design patterns, including:

*   Creational patterns
*   Structural patterns
*   Behavioral patterns
*   Architectural patterns

Visit the following resources to learn more:

- [@article@Overview - Software Design Pattern](https://en.wikipedia.org/wiki/Software_design_pattern)
- [@article@Explaining, imaging and simplifying design patterns](https://refactoring.guru/design-patterns/what-is-pattern)
- [@video@What Are Design Patterns?](https://www.youtube.com/watch?v=BWprw8UHIzA)
- [@feed@Explore top posts about Design Patterns](https://app.daily.dev/tags/design-patterns?ref=roadmapsh)

## Design Principles

# Design Principles

## Design Principles

# Design Principles

Design principles are fundamental guidelines that help software engineers create systems that are maintainable, scalable, robust, and easy to understand. They represent best practices derived from decades of software engineering experience and are widely used to guide the structure and behavior of code. Applying these principles can lead to better software architecture, easier debugging, and improved collaboration.

## Distributed

# Distributed

Distributed systems refer to the design and organization of software components that are distributed across multiple devices or locations, connected via a network, and work together to achieve a common goal. The main challenge in designing distributed systems is dealing with the inherent complexity that arises from the distribution of components and the communication between them, and it requires techniques such as load balancing, replication, and partitioning to improve scalability, fault-tolerance, and performance. Additionally, security and coordination are also important aspects of distributed systems.

Visit the following resources to learn more:

- [@article@Overview of Distributed Architecture](https://www.tutorialspoint.com/software_architecture_design/distributed_architecture.htm)

## Domain Driven Design

# Domain Driven Design

Domain-Driven Design (DDD) is an architectural pattern that is used to design software systems based on the core business domain and business entities, it's focused on creating a clear and accurate representation of the business domain within the software system, and on aligning the software system with the business goals and objectives. DDD provides several advantages over other architectural patterns, such as alignment with business goals and objectives, improved communication between domain experts and developers, a clear and expressive model of the business domain and improved scalability and maintainability. It's implemented using a set of principles and patterns such as strategic design, subdomains, bounded context, entities, value objects, aggregate, and repository.

Visit the following resources to learn more:

- [@article@Modern Software Architecture (#1): Domain Driven Design](https://medium.com/modern-software-architecture/modern-software-architecture-1-domain-driven-design-f06fad8695f9)
- [@article@The Concept of Domain-Driven Design Explained](https://medium.com/microtica/the-concept-of-domain-driven-design-explained-3184c0fd7c3f)
- [@video@What is DDD (Domain-Driven Design) ?](https://www.youtube.com/watch?v=Tnecs_7OT74)
- [@video@Domain-Driven Design patterns for a distributed system](https://www.youtube.com/watch?v=i3d_jzpf0gE)
- [@feed@Explore top posts about Domain-Driven Design](https://app.daily.dev/tags/domain-driven-design?ref=roadmapsh)

## Domain Language

# Domain Language

A domain language is a specific vocabulary and set of concepts used to describe and communicate about a specific area of knowledge or business. In software development, a domain language is used to model the objects and concepts within a specific domain, and to capture the relationships and constraints between them.

A domain language is used to provide a common understanding of the problem domain among all stakeholders, including developers, business analysts, and domain experts. It is also used to ensure that the software system accurately reflects the real-world problem it is intended to solve.

Visit the following resources to learn more:

- [@article@Overview of Domain-specific language](https://en.wikipedia.org/wiki/Domain-specific_language)
- [@article@What are Domain Languages (DSLs)?](https://www.jetbrains.com/mps/concepts/domain-specific-languages/)

## Domain Models

# Domain Models

A domain model is a representation of a specific area of knowledge or business that is used to model the objects and concepts within that domain, and to capture the relationships and constraints between them. In object-oriented programming (OOP), a domain model is typically represented by a set of classes and interfaces, with each class or interface representing a specific concept or object within the domain.

A domain model is used to provide a clear and consistent representation of the problem domain, and to capture the business requirements and constraints of the system. It is also used to guide the design of the system and to ensure that the system accurately reflects the real-world problem it is intended to solve.

Visit the following resources to learn more:

- [@article@Overview of Domain model](https://en.wikipedia.org/wiki/Domain_model)
- [@article@Domain Driven Design](https://khalilstemmler.com/articles/categories/domain-driven-design/)

## Domain Models

# Domain Models

Domain Models are a pattern used in enterprise application development to represent the business concepts and rules of a specific domain. They are typically used to model the problem domain, or the area of expertise of a specific business.

A Domain Model is a collection of objects that represent the real-world concepts and entities of the domain. These objects are typically modeled as classes or types, and they encapsulate the data and behavior that is specific to the domain. They are responsible for representing the state and behavior of the business concepts they model, and for enforcing the rules and constraints of the domain.

Visit the following resources to learn more:

- [@article@Overview - Domain Models](https://sparxsystems.com/enterprise_architect_user_guide/14.0/model_domains/specialized_models.html)
- [@video@Tutorial - Domain Model Pattern](https://www.youtube.com/watch?v=75EGANiqADw)

## Dry

# DRY

DRY (Don't Repeat Yourself) is a software development principle that suggests that code should not have duplicate functionality. The idea is to keep the codebase as simple as possible by eliminating redundancy and duplication. The goal is to reduce complexity and improve maintainability by ensuring that each piece of knowledge is expressed in a single, unambiguous way within the system.

The DRY principle is closely related to the Single Responsibility Principle (SRP) and the Open-Closed Principle (OCP), which are part of the SOLID principles. The DRY principle aims to reduce the amount of duplicate code by creating abstractions that can be reused across the system.

Visit the following resources to learn more:

- [@article@Overview of Don't repeat yourself (DRY)](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself)
- [@video@What is DRY in programming?](https://www.youtube.com/watch?v=Rv3RIc_ziOY)

## Dtos

# DTOs

The Data Transfer Object Design Pattern is one of the enterprise application architecture patterns that calls for the use of objects that aggregate and encapsulate data for transfer. A Data Transfer Object is, essentially, like a data structure. It should not contain any business logic but should contain serialization and deserialization mechanisms.

Visit the following resources to learn more:

- [@article@Data Transfer Object pattern and Mappers](https://medium.com/@abdalrhmanalkraien/data-transfer-object-pattern-and-mapper-116508bc9df0)

## Encapsulate What Varies

# Encapsulate What Varies

Encapsulate what varies is a programming principle that suggests that code should be organized in such a way that the parts that are likely to change in the future are isolated from the parts that are unlikely to change. This is accomplished by creating interfaces and classes that separate the varying parts of the code from the stable parts.

Encapsulating what varies allows for more flexibility in the code. When changes are needed, they can be made to the encapsulated parts without affecting the rest of the code. This makes it easier to understand, test, and maintain the code.

Visit the following resources to learn more:

- [@article@What does it mean when one says “Encapsulate what varies”?](https://softwareengineering.stackexchange.com/questions/337413/what-does-it-mean-when-one-says-encapsulate-what-varies)
- [@article@Overview of Encapsulate What Varies](https://bootcamp.uxdesign.cc/software-design-principles-every-developers-should-know-23d24735518e)

## Encapsulation

# Encapsulation

Encapsulation is a concept in object-oriented programming (OOP) that refers to the practice of wrapping an object's internal data and behavior within a defined interface, and hiding the implementation details from the outside world. It is one of the fundamental concepts of OOP and is closely related to the concepts of data hiding and information hiding.

Encapsulation is achieved by using access modifiers (such as "public," "private," and "protected") to control the visibility and accessibility of an object's data and methods. For example, data members of a class can be declared as private, which means they can only be accessed by methods within the class, while methods can be declared as public, which means they can be called by any code that has a reference to the object.

Visit the following resources to learn more:

- [@article@Overview of Encapsulation](https://en.wikipedia.org/wiki/Encapsulation_(computer_programming))
- [@video@Tutorial - What is encapsulation in programming?](https://www.youtube.com/watch?v=sNKKxc4QHqA)
- [@feed@Explore top posts about General Programming](https://app.daily.dev/tags/general-programming?ref=roadmapsh)

## Enterprise Patterns

# Enterprise Patterns

Enterprise Patterns are well-documented, reusable solutions to commonly occurring problems in enterprise software development. These patterns provide a vocabulary and a set of best practices for designing robust, scalable, and maintainable enterprise applications, addressing recurring challenges like data access, concurrency, distribution, and integration with legacy systems. They serve as blueprints for solving complex architectural and design issues, promoting consistency and reducing development time.

Visit the following resources to learn more:

- [@article@Enterprise Software Architecture Patterns: An Ultimate Guide](https://www.rishabhsoft.com/blog/enterprise-software-architecture-patterns)
- [@video@What are Enterprise Integration Patterns?](https://www.youtube.com/watch?v=WNm3QmJadNs)
- [@feed@Explore top posts about Enterprise](https://app.daily.dev/tags/enterprise?ref=roadmapsh)

## Enterprise Patterns

# Enterprise Patterns

Enterprise patterns are a set of design patterns that are commonly used in the development of enterprise software applications. These patterns provide a common vocabulary and a set of best practices for solving common problems that arise in the development of large, complex software systems. Some examples of enterprise patterns include:

*   Domain-Driven Design (DDD)
*   Model-View-Controller (MVC)
*   Service Oriented Architecture (SOA)
*   Command and Query Responsibility Segregation (CQRS)
*   Event Sourcing
*   Microservices
*   Event-Driven Architecture (EDA)

These patterns can help to improve the maintainability and scalability of the software, by providing a clear separation of concerns and allowing for a more modular and flexible architecture.

Visit the following resources to learn more:

- [@article@Software Architecture Patterns in Enterprise Software](https://blog.devgenius.io/10-software-architecture-patterns-in-enterprise-software-development-fabacb5ed0c8)
- [@video@What are Enterprise Integration Patterns?](https://www.youtube.com/watch?v=WNm3QmJadNs)
- [@feed@Explore top posts about Enterprise](https://app.daily.dev/tags/enterprise?ref=roadmapsh)

## Entities

# Entities

Entities are a pattern used in enterprise application development to represent the business concepts that have a unique identity and a lifetime. They are typically used to model real-world objects or concepts that have a distinct identity and a lifecycle, such as a customer, an order, or an account.

An Entity is defined by its identity, meaning that two entities with the same identity are considered to be the same, regardless of their state. Entities usually have a unique identifier, such as a primary key, that is used to identify them. They also have an associated set of properties or attributes that describe their state.

## Event Driven

# Event Driven

Event-driven architecture (EDA) is a software design pattern in which the system reacts to specific events that occur, rather than being continuously polled for changes. In EDA, events are messages that are sent asynchronously between components, and the components react to the events they are interested in.

The main advantage of using EDA is that it allows for a clear separation of concerns between the components, and it can improve the scalability and fault-tolerance of the system. Additionally, it allows for loose coupling between components, meaning that the components are not aware of each other's existence, and can be developed, deployed, and scaled independently.

Visit the following resources to learn more:

- [@article@Overview of Event-driven programming](https://en.wikipedia.org/wiki/Event-driven_programming)
- [@article@What is event-driven architecture?](https://www.redhat.com/en/topics/integration/what-is-event-driven-architecture)

## Event Sourcing

# Event Sourcing

Event sourcing is an architectural pattern that is used to build systems that need to maintain a history of all the changes that have occurred over time. This pattern stores all changes to the system's state as a sequence of events, rather than just the current state.

In Event sourcing, all changes to the state of the system are treated as events, and these events are stored in an append-only log, also known as an event store. The current state of the system can be reconstructed from the event log at any given point in time by replaying the events from the log.

Visit the following resources to learn more:

- [@article@Event Sourcing Pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/event-sourcing)
- [@video@Event Sourcing Example & Explained](https://www.youtube.com/watch?v=AUj4M-st3ic&list=PLThyvG1mlMzkRKJnhzvxtSAbY8oxENLUQ&ab_channel=CodeOpinion)
- [@feed@Explore top posts about Architecture](https://app.daily.dev/tags/architecture?ref=roadmapsh)

## Functional Programming

# Functional Programming

Functional programming is a programming paradigm that treats computation as the evaluation of mathematical functions and avoids changing-state and mutable data. It emphasizes the use of functions to solve problems, often using higher-order functions, immutability, and recursion. Instead of modifying data, functional programming creates new data structures.

Visit the following resources to learn more:

- [@article@What is Functional Programming?](https://medium.com/javascript-scene/master-the-javascript-interview-what-is-functional-programming-7f218c68b3a0)
- [@feed@Explore top posts about Functional Programming](https://app.daily.dev/tags/functional-programming?ref=roadmapsh)

## Gof Design Patterns

# GoF Design Patterns

The Gang of Four (GoF) design patterns are a set of design patterns for object-oriented software development that were first described in the book "Design Patterns: Elements of Reusable Object-Oriented Software" by Erich Gamma, Richard Helm, Ralph Johnson, and John Vlissides (also known as the Gang of Four).

The GoF design patterns are divided into three categories: Creational, Structural and Behavioral.

*   Creational Patterns
*   Structural Patterns
*   Behavioral Patterns

Visit the following resources to learn more:

- [@article@Gangs of Four (GoF) Design Patterns](https://www.digitalocean.com/community/tutorials/gangs-of-four-gof-design-patterns)
- [@video@Tutorial - Builder Pattern (Gang of Four Design Patterns Series)](https://www.youtube.com/watch?v=_sa2WlAFWQos)

## Hollywood Principle

# Hollywood Principle

The Hollywood Principle is a software development principle that states: "Don't call us, we'll call you." It suggests that high-level components should dictate the flow of control in an application, rather than low-level components.

This principle is often used in the context of inversion of control (IoC) and dependency injection. In traditional software development, low-level components are responsible for creating and managing the high-level components that they depend on. With IoC, the high-level components dictate the flow of control, and the low-level components are created and managed by a separate mechanism.

Visit the following resources to learn more:

- [@video@Tutorial - Hollywood Principle](https://www.youtube.com/watch?v=lRuygpsXE5s)

## Identity Maps

# Identity Maps

Identity Maps is a pattern used in enterprise application development to maintain a map of objects that have been loaded from the database, keyed by their unique identifier. It is used to ensure that multiple copies of the same object are not created in memory when the same data is accessed multiple times.

The identity map pattern is typically used in conjunction with an ORM (Object-Relational Mapping) tool. When an object is loaded from the database, it is first checked against the identity map to see if it has already been loaded. If it has, the existing object is returned, instead of creating a new copy.

Visit the following resources to learn more:

- [@article@Overview of Identity map pattern](https://en.wikipedia.org/wiki/Identity_map_pattern)
- [@video@Tutorial - Identity Map Design Pattern](https://youtube.com/watch?v=erDxkIyNudY)

## Indentation And Code Style

# Indentation and Code Style

Indentation and code style refer to the consistent formatting of source code to improve readability and maintainability. This involves using whitespace, line breaks, and naming conventions in a standardized manner across a project. The goal is to create code that is visually appealing and easy for developers to understand, regardless of who wrote it. Consistent indentation highlights the code's structure, making it easier to follow control flow and identify logical blocks. Adhering to a specific code style, which dictates rules for naming, commenting, and other formatting aspects, further enhances the clarity and consistency of the codebase.

Visit the following resources to learn more:

- [@article@Clean Code – Formatting](https://www.baeldung.com/cs/clean-code-formatting)
- [@feed@Explore top posts about General Programming](https://app.daily.dev/tags/general-programming?ref=roadmapsh)

## Inheritance

# Inheritance

Inheritance is a fundamental concept in object-oriented programming (OOP) that allows a new class to inherit the properties and methods of an existing class. The class that is inherited from is called the parent or super class, while the class that inherits is called the child or sub class. Inheritance enables code reuse and allows for a hierarchical organization of classes, where a child class can inherit the properties and methods of its parent class and potentially add or override them. The main advantage of inheritance is that it allows for a clean and organized way to reuse code and share functionality among classes.

Visit the following resources to learn more:

- [@article@Overview of Inheritance (object-oriented programming)](https://en.wikipedia.org/wiki/Inheritance_(object-oriented_programming))
- [@video@What is inheritance in programming?](https://www.youtube.com/watch?v=ajOYOxCanhE)

## Interfaces

# Interfaces

In object-oriented programming (OOP), an interface is a contract or a set of methods that a class must implement. It defines a common set of methods that a class must provide, but it does not provide any implementation details. An interface can include both method signatures and constants.

Interfaces are used to define a common behavior for a group of related classes, and to provide a way for objects of different classes to be treated polymorphically. A class that implements an interface must provide an implementation for all of the methods declared in the interface. A class can implement multiple interfaces, but can only inherit from one base class.

Visit the following resources to learn more:

- [@video@Fundamental concepts: What's an Interface?](https://www.youtube.com/watch?v=o1jBgdhQsGo)

## Keep Framework Code Distant

# Keep Framework Code Distant

Keeping framework code distant refers to separating the application's code from the framework's code. By doing so, it makes it easier to maintain, test, and upgrade the application's codebase and the framework independently.

Here are some ways to keep framework code distant in system architecture:

1.  Use an abstraction layer to separate the application code from the framework code. This allows the application code to be written without the need to know the specifics of the framework.
2.  Use dependency injection to decouple the application code from the framework code. This allows the application code to use the framework's functionality without having to instantiate the framework objects directly.
3.  Avoid using framework-specific libraries or classes in the application code. This makes it easier to switch to a different framework in the future if needed.
4.  Use a standard interface for the application code to interact with the framework. This allows the application code to be written without the need to know the specifics of the framework.
5.  Keep the application and the framework code in separate projects and/or repositories.

By following these best practices, the system architecture will be more maintainable, testable, and less error-prone, and it will be easier to upgrade or switch the framework if needed.

Visit the following resources to learn more:

- [@article@Clean architecture](https://pusher.com/tutorials/clean-architecture-introduction/)
- [@feed@Explore top posts about General Programming](https://app.daily.dev/tags/general-programming?ref=roadmapsh)

## Keep It Simple And Refactor Often

# Avoid Hasty Abstractions

Creating abstractions is an important part of software development, but creating too many abstractions or creating them too early can lead to unnecessary complexity and make the code harder to understand and maintain.

Here are some ways to avoid hasty abstractions in system architecture:

*   Understand the problem that needs to be solved before creating an abstraction.
*   Start with a simple solution and only create an abstraction when it becomes clear that the solution is becoming too complex.
*   Use code refactoring techniques to simplify the code before creating an abstraction.
*   Avoid creating abstractions for the sake of creating abstractions.
*   Use established design patterns and practices when creating abstractions, but do not force them into the code.
*   Use automated testing to ensure that the abstraction does not introduce new bugs or break existing functionality.
*   Create abstraction in a way that it's easy to test, debug, and reason about.

Visit the following resources to learn more:

- [@article@AHA Programming](https://kentcdodds.com/blog/aha-programming)

## Keep Methods  Classes  Files Small

# Keep it Small

You should design and implement small, focused components that serve a specific purpose, rather than large, monolithic components that try to do everything. This can help to improve the maintainability and scalability of the system by making it easier to understand, test, and modify individual components.

## Law Of Demeter

# Law of Demeter

Also called “Principle of Least Knowledge”, it states:

In Practice
-----------

*   Avoid chaining calls deep into the internals of other objects.
*   Restrict communication to objects you directly manage.

### 🔹 ❌ Bad Example (Violation)

    // Controller
    total = order.customer.address.getRegionTaxRate() * order.amount
    

### 🔹 ✅ Good Example

    // Controller
    total = order.calculateTotal()
    

🔹 Why It Matters
-----------------

*   **Reduces coupling** → fewer dependencies between classes.
*   **Increases maintainability** → changes in one class don’t affect distant classes.
*   **Improves readability** → clear boundaries of responsibility.

🔹 Resources
------------

Visit the following resources to learn more:

- [@article@@Article: Law of Demeter Explained](https://en.wikipedia.org/wiki/Law_of_Demeter)

## Layered Architectures

# Layered Architectures

A layered architecture is a software design pattern in which the functionality of a system is divided into a set of layers, with each layer having a specific responsibility and interacting with the layers above and below it. The main idea behind a layered architecture is to separate the concerns of the system into distinct and independent layers, making the code more modular, easier to understand, test, and modify.

There are several types of layered architectures, but a common one is the three-layer architecture which consists of:

*   Presentation Layer
*   Business Layer
*   Data Access Layer

Visit the following resources to learn more:

- [@article@Software Architecture Patterns — Layered Architecture](https://priyalwalpita.medium.com/software-architecture-patterns-layered-architecture-a3b89b71a057)
- [@article@5 Primary Layers in Software Architecture?](https://www.indeed.com/career-advice/career-development/what-are-the-layers-in-software-architecture)
- [@feed@Explore top posts about Architecture](https://app.daily.dev/tags/architecture?ref=roadmapsh)

## Layered

# Layered

In software architecture, layered architecture is a design approach in which a software system is divided into a set of layers, each of which has a specific responsibility and communicates with the other layers through well-defined interfaces. This approach allows for a more modular and flexible design, where each layer can be developed, tested, and deployed independently, making it easier to add new features, modify existing ones, and maintain the system.

A layered architecture is often used for large and complex systems, where the need for scalability and flexibility is high. Each layer in a layered architecture is responsible for a specific functionality and can be thought of as a "black box" with a well-defined interface. The layers communicate with each other through these interfaces, allowing for a clear separation of concerns.

Visit the following resources to learn more:

- [@article@Get started with Layered Architecture](https://cs.uwaterloo.ca/~m2nagapp/courses/CS446/1195/Arch_Design_Activity/Layered.pdf)
- [@video@Layered Architectures](https://www.youtube.com/watch?v=0kpTKLTx8f4)

## Mappers

# Mappers

Mappers are a pattern used in enterprise application development to provide a consistent and abstracted way to map between different data models. They act as an abstraction layer between the application and the data storage, providing a consistent and simple API for data transformation.

A mapper is a component that can be used to convert data from one format or model to another. For example, a mapper can be used to convert data from a database model to a domain model, or from a domain model to a data transfer object (DTO).

Visit the following resources to learn more:

- [@article@Overview of Data Mapper Pattern](https://en.wikipedia.org/wiki/Data_mapper_pattern)
- [@video@Tutorial - Mappers](https://www.youtube.com/watch?v=7noMLStHcTE)

## Meaningful Names Over Comments

# Meaningful Names

You should follow the practice of giving clear and descriptive names to different components of a system, such as variables, functions, and classes. This can help to make the system more understandable and maintainable by clearly communicating the purpose of each component and its intended usage.

Visit the following resources to learn more:

- [@article@A Guide for Naming Things in Programming](https://levelup.gitconnected.com/a-guide-for-naming-things-in-programming-2dc2d74879f8)

## Message Queues  Streams

# Message Queues Streams

Message queues and streams are architectural patterns that are used to decouple different components of a system and enable asynchronous communication between them.

Message Queues: A message queue is a software component that allows multiple systems or applications to communicate with each other by passing messages between them. Messages are stored in a queue, and each message is processed by a single consumer. This pattern is useful for systems where there is a high degree of variability in the rate of message production and consumption, and where the sender and receiver do not need to be active at the same time. Examples of message queue systems are Apache Kafka, RabbitMQ, and Amazon SQS.

Visit the following resources to learn more:

- [@article@System Design — Message Queues](https://medium.com/must-know-computer-science/system-design-message-queues-245612428a22)
- [@article@Overview of Message Queue pattern](https://badia-kharroubi.gitbooks.io/microservices-architecture/content/patterns/communication-patterns/message-queue-pattern.html)

## Messaging

# Messaging

Messaging is a key concept in several architectural styles, including event-driven architecture (EDA), microservices, and message-driven architecture (MDA).

*   Event-driven architecture (EDA)
*   Microservices
*   Message-driven architecture (MDA)

In general, messaging is a powerful concept that allows for the decoupling and scalability of systems and it's used in different architectural styles to improve the flexibility and scalability of the system by allowing for loose coupling between components and making it easier to add new features or modify existing ones.

Visit the following resources to learn more:

- [@article@Architectural Styles in Software Engineering](https://shapingsoftware.com/2009/02/09/architectural-styles/)
- [@article@Architectural Messaging Patterns](https://www.redhat.com/architect/architectural-messaging-patterns)

## Microkernel

# Microkernel

A microkernel is an architectural pattern in operating system design that aims to minimize the amount of code running in kernel mode (i.e., privileged mode with direct access to hardware resources) and instead move as much functionality as possible into user mode. This is done by providing a small, minimalistic core kernel that only handles basic tasks such as memory management, process scheduling, and inter-process communication (IPC), and leaving all other functionality to be implemented in user-mode processes.

Visit the following resources to learn more:

- [@article@Overview of Microkernel Architecture](https://www.oreilly.com/library/view/software-architecture-patterns/9781491971437/ch03.html)
- [@video@Microkernel Architectural Pattern | Software Architecture](https://www.youtube.com/watch?v=h3icQDMRLd8)

## Microservices

# Microservices

Microservices is an architectural pattern that is used to design software systems as a collection of small, independent, and loosely-coupled services. Each service is responsible for a specific functionality and can be developed, deployed, and scaled independently. The main advantage of a microservices architecture is that it allows for a more flexible and scalable system, it also improves fault isolation and enables faster deployment. It's often used in combination with other architectural patterns and styles such as event-driven architecture, CQRS, and service-oriented architecture.

Visit the following resources to learn more:

- [@official@Brief of Microservices](https://microservices.io/patterns/microservices.html)
- [@video@Tutorial - Microservices Architectural Pattern](https://www.youtube.com/watch?v=8BPDv038oMI)
- [@video@Get started with Microservices Design Patterns](https://www.youtube.com/watch?v=xuH81XGWeGQ)
- [@feed@Explore top posts about Microservices](https://app.daily.dev/tags/microservices?ref=roadmapsh)

## Minimize Cyclomatic Complexity

# Minimize Cyclomatic Complexity

Cyclomatic complexity measures the number of linearly independent paths through a program's source code.  It's calculated based on the number of decision points (like `if`, `for`, `while`, `case`) within a function or code block. High cyclomatic complexity indicates code that is harder to understand, test, and maintain due to its increased number of possible execution paths. Reducing this complexity aims to simplify the control flow and logic within code, leading to more readable and reliable software.

Visit the following resources to learn more:

- [@article@How to reduce cyclomatic complexity?](https://kasp9023.medium.com/how-to-make-your-code-more-readable-focus-on-the-happy-path-and-reduce-cyclomatic-complexity-66802b8897b5)

## Model Driven Design

# Model Driven Design

Model-driven design (MDD) is a software development methodology in which the design of a system is represented by a set of models, and the models are used to drive the development of the system. MDD is based on the idea that the design of a system can be represented by a set of models, and that these models can be used to generate the code for the system.

The main advantage of using MDD is that it allows for a clear separation of concerns between the design and implementation of a system. The models represent the design of the system, and the code is generated from the models, which makes it easier to maintain and evolve the system. Additionally, MDD can also improve the quality of the code, as the models can be used to check for design errors and inconsistencies before the code is generated.

Visit the following resources to learn more:

- [@article@Model Driven Design – theory to practice](https://www.todaysoftmag.com/article/1529/model-driven-design-theory-to-practice)

## Model View Controller

# Model View Controller

Model-View-Controller (MVC) is an architectural pattern that separates the concerns of a software system into three distinct components: the model, the view, and the controller, where the model represents the data and the business logic of the system, the view represents the user interface of the system and the controller acts as an intermediary between the model and the view. The main goal of MVC is to separate the concerns of the system, making it easier to understand, maintain and evolve, it's widely used in web development.

Visit the following resources to learn more:

- [@article@MVC Framework - Introduction](https://www.tutorialspoint.com/mvc_framework/mvc_framework_introduction.htm)
- [@video@Tutorial - MVC Architectural Pattern](https://www.youtube.com/watch?v=e9S90R-Y24Q)

## Monolithic

# Monolithic

In software architecture, monolithic architecture is a design approach in which a software system is built as a single, integrated, and self-contained unit. In a monolithic architecture, all the components of the system are tightly coupled and depend on each other. This means that changes in one part of the system may affect other parts of the system.

A monolithic architecture is often used for small to medium-sized systems, where the complexity of the system is manageable and the need for scalability and flexibility is not as high. In a monolithic architecture, the entire system is typically built, deployed, and executed as a single unit, which can make it easier to understand and manage the system.

Visit the following resources to learn more:

- [@article@Overview of Monolithic Architecture](https://www.atlassian.com/microservices/microservices-architecture/microservices-vs-monolith)
- [@article@What is Monolithic architecture?](https://www.techtarget.com/whatis/definition/monolithic-architecture)
- [@video@What is Software Architecture? (Monolithic vs. Layered vs. Microservice)s](https://www.youtube.com/watch?v=_07NtoK-Kns)

## Object Oriented Programming

# Object Oriented Programming

Object-oriented programming (OOP) is a programming paradigm that is based on the concept of "objects," which are instances of a class. In OOP, a class is a blueprint for creating objects, which have both data (attributes) and behavior (methods). The main idea behind OOP is to model real-world objects and their interactions, making it well-suited for creating complex and large-scale software systems.

Visit the following resources to learn more:

- [@article@Discover Object Oriented Programming](https://opendsa.cs.vt.edu/ODSA/Books/Everything/html/IntroOO.html)
- [@video@Software Development Tutorial - What is object-oriented language?s](https://www.youtube.com/watch?app=desktop&v=SS-9y0H3Si8)
- [@feed@Explore top posts about General Programming](https://app.daily.dev/tags/general-programming?ref=roadmapsh)

## Object Oriented Programming

# Object Oriented Programming

Object-oriented programming (OOP) is a programming paradigm that uses objects and classes to structure and organize code. In OOP, an object is an instance of a class, which is a template that defines the properties and behaviors of the object. OOP is based on the principles of encapsulation, inheritance, and polymorphism.

Visit the following resources to learn more:

- [@article@What is Object Oriented Programming?](https://www.freecodecamp.org/news/what-is-object-oriented-programming/)
- [@article@OOP introduction](https://www.geeksforgeeks.org/introduction-of-object-oriented-programming/)
- [@feed@Explore top posts about OOP](https://app.daily.dev/tags/oop?ref=roadmapsh)

## Object Oriented Programming

# Object Oriented Programming

Object-oriented programming (OOP) is a programming paradigm that is based on the concept of "objects," which are instances of a class. In OOP, a class is a blueprint for creating objects, which have both data (attributes) and behavior (methods). The main idea behind OOP is to model real-world objects and their interactions, making it well-suited for creating complex and large-scale software systems.

Visit the following resources to learn more:

- [@article@Discover Object Oriented Programming](https://opendsa.cs.vt.edu/ODSA/Books/Everything/html/IntroOO.html)
- [@video@Software Development Tutorial - What is object-oriented language?s](https://www.youtube.com/watch?app=desktop&v=SS-9y0H3Si8)
- [@feed@Explore top posts about General Programming](https://app.daily.dev/tags/general-programming?ref=roadmapsh)

## Organize Code By Actor It Belongs To

# Organize Code by Actor It Belongs To

Organizing code by the actor it belongs to means structuring your codebase around the primary users, roles, or systems that interact with it. Instead of grouping code purely by technical layers (controllers, services, repositories), you group it by _who_ or _what_ uses the functionality. This improves cohesion, discoverability, and long-term maintainability.

Some key ideas behind this approach include:

*   Actor-focused structure: Group related functionality by user roles, domains, or external systems (e.g., `admin`, `customer`, `payment-gateway`).
*   High cohesion: Keep logic that changes for the same reason in the same place.
*   Reduced coupling: Minimize dependencies between unrelated actors or domains.
*   Clear ownership: Each module clearly represents a responsibility or business capability.
*   Easier navigation: Developers can quickly find relevant code based on the actor they are working on.
*   Scalability: The codebase grows more naturally as new actors or features are added.
*   Improved testing: Actor-based modules are easier to test in isolation.
*   Alignment with business logic: The structure mirrors real-world use cases and workflows.
*   Better collaboration: Teams can own specific actors or domains.
*   Cleaner boundaries: Encourages well-defined APIs between parts of the system.

Visit the following resources to learn more:

- [@article@Package by Feature vs Package by Layer](https://www.baeldung.com/java-packaging-structures)
- [@article@Screaming Architecture](https://blog.cleancoder.com/uncle-bob/2011/09/30/Screaming-Architecture.html)
- [@feed@Explore top posts about Software Architecture](https://app.daily.dev/tags/software-architecture?ref=roadmapsh)

## Orms

# ORMs

ORM stands for Object-Relational Mapping, it is a technique used in enterprise application development to map between the object-oriented programming model and the relational database model. It allows developers to work with objects in their code, while the ORM tool takes care of translating those objects into the appropriate database operations.

ORMs are designed to abstract away the complexity of working with a relational database and allow developers to interact with the database using a higher-level, object-oriented API. They provide a set of libraries and tools that map the objects in the code to the tables and rows in the database, and vice versa. This allows developers to work with the data using a familiar object-oriented paradigm, rather than having to write complex SQL queries.

Visit the following resources to learn more:

- [@article@Why do you need an ORM?](https://enterprisecraftsmanship.com/posts/do-you-need-an-orm/)
- [@feed@Explore top posts about Backend Development](https://app.daily.dev/tags/backend?ref=roadmapsh)

## Peer To Peer

# Peer to Peer

Peer-to-peer (P2P) architecture is a distributed computing architecture in which each node (peer) in the network acts as both a client and a server. In P2P architecture, there is no central authority or server that manages the network, and each node communicates directly with other nodes to exchange information, share resources, and perform computations.

The main advantage of using P2P architecture is that it allows for a more decentralized and fault-tolerant system. As there is no central authority, there is no single point of failure, and the network can continue to function even if some nodes fail. Additionally, P2P architecture can also improve scalability as the number of nodes in the network increases.

Visit the following resources to learn more:

- [@article@Peer to Peer Architecture](https://student.cs.uwaterloo.ca/~cs446/1171/Arch_Design_Activity/Peer2Peer.pdf)
- [@feed@Explore top posts about Peer-to-Peer](https://app.daily.dev/tags/peer-to-peer?ref=roadmapsh)

## Policy Vs Detail

# Policy vs Detail

In software architecture, the distinction between **policy** and **detail** refers to the separation of high-level decisions and low-level implementation details.

Policy refers to the high-level decisions that define the overall behavior and structure of the system. These decisions include things like the overall architecture, the system's interface, and the major components and their interactions. Policy decisions are often made by architects and designers, and they set the overall direction for the system.

Detail refers to the low-level implementation details that are required to implement the policy decisions. These include things like the specific algorithms, data structures, and code that make up the system's components. Details are often implemented by developers and are responsible for the actual functioning of the system.

## Polymorphism

# Polymorphism

Polymorphism is a concept in object-oriented programming (OOP) that allows objects of different classes to be treated as objects of a common parent class. This is achieved by defining a common interface for all classes that need to be treated polymorphically. The word polymorphism is derived from Greek, "poly" means many and "morph" means form.

There are two types of polymorphism:

*   Compile-time polymorphism (also called static polymorphism or early binding) occurs when the type of the object that is going to be acted upon is determined at compile-time. This is achieved through method overloading, which allows multiple methods to have the same name but different parameters within the same class.
*   Run-time polymorphism (also called dynamic polymorphism or late binding) occurs when the type of the object is determined at run-time. This is achieved through method overriding, which allows a child class to provide a specific implementation of a method that is already defined in its parent class.

Visit the following resources to learn more:

- [@article@Overview of Polymorphism in programming](https://www.bmc.com/blogs/polymorphism-programming/)
- [@video@What is polymorphism in programming?](https://www.youtube.com/watch?v=tIWm3I_Zu7I)

## Posa Patterns

# POSA Patterns

POSA (Pattern-Oriented Software Architecture) is a set of design patterns for developing software systems that can scale and adapt to changing requirements. These patterns were first described in the book "Patterns of Scalable, Reliable Services" by Kevin Hoffman.

POSA patterns are divided into four categories:

*   Partitioning Patterns
*   Placement Patterns
*   Routing Patterns
*   Federation Patterns

Visit the following resources to learn more:

- [@article@Overview of Pattern-Oriented Software Architecture](https://en.wikipedia.org/wiki/Pattern-Oriented_Software_Architecture)
- [@video@POSA Pattern Examples](https://www.youtube.com/watch?v=iYNa_KcWxCU)

## Program Against Abstractions

# Program Against Abstractions

Programming against abstractions is a programming principle that suggests that code should be written in such a way that it is not tied to specific implementations, but rather to abstractions. This is accomplished by defining interfaces or abstract classes that define the behavior of a group of related classes without specifying their implementation.

Programming against abstractions allows for more flexibility in the code. When changes are needed, they can be made to the implementation of the abstractions without affecting the code that uses them. This makes it easier to understand, test, and maintain the code.

Visit the following resources to learn more:

- [@article@Overview of Abstraction principle](https://en.wikipedia.org/wiki/Abstraction_principle_(computer_programming))

## Programming Paradigms

# Programming Paradigms

A programming paradigm is a fundamental style or approach to solving problems using a programming language. Different programming paradigms provide different ways of organizing and structuring code, and have different strengths and weaknesses. Some of the most common programming paradigms include:

*   Imperative programming
*   Functional programming
*   Object-oriented programming
*   Logic programming
*   Declarative programming

Visit the following resources to learn more:

- [@article@Overview of Programming paradigm](https://en.wikipedia.org/wiki/Programming_paradigm)

## Programming Paradigms

# Programming Paradigms

A programming paradigm is a fundamental style or approach to solving problems using a programming language. Different programming paradigms provide different ways of organizing and structuring code, and have different strengths and weaknesses. Some of the most common programming paradigms include:

*   Imperative programming
*   Functional programming
*   Object-oriented programming
*   Logic programming
*   Declarative programming

Visit the following resources to learn more:

- [@article@Overview of Programming paradigm](https://en.wikipedia.org/wiki/Programming_paradigm)

## Publish Subscribe

# Publish Subscribe

The publish-subscribe pattern is a messaging pattern in which a publisher sends a message to a topic, and any number of subscribers can subscribe to that topic to receive the message. The publish-subscribe pattern is also known as the "observer pattern" and is a way of implementing communication between different parts of an application in a decoupled way.

The main advantage of using the publish-subscribe pattern is that it allows for a clear separation of concerns between the publisher and the subscribers, and it can improve the flexibility and scalability of the system. Additionally, it allows for loose coupling between components, meaning that the publisher and subscribers are not aware of each other's existence, and can be developed, deployed, and scaled independently.

Visit the following resources to learn more:

- [@article@Tutorial - Publish–subscribe pattern](https://en.wikipedia.org/wiki/Publish%E2%80%93subscribe_pattern)
- [@video@Publish-Subscribe Architecture (Explained by Example)](https://www.youtube.com/watch?v=O1PgqUqZKTA)

## Pure Functions

# Pure Functions

Pure functions are a type of function in programming where the output is solely determined by its input values, without any side effects. This means that for the same input, a pure function will always return the same output, and it does not modify any state outside of its own scope. They are deterministic, predictable, and make code easier to test and reason about.

Visit the following resources to learn more:

- [@video@What are Pure Functions? | Javascript Functions Tutorial](https://www.youtube.com/watch?v=ZXxahQS1PN8)

## Repositories

# Repositories

Repositories are a pattern used in enterprise application development to provide a consistent and abstracted way to access data storage. Repositories act as an abstraction layer between the application and the data storage, providing a consistent and simple API for data access and manipulation.

A repository is a pattern that can be used to organize the data access code and encapsulate the logic of retrieving and storing objects. Repositories provide a way to separate the concerns of the data access from the rest of the application, allowing the application code to be written against an interface and not a specific data storage technology.

Visit the following resources to learn more:

- [@article@Introduction to Repository Design Patterns](https://cubettech.com/resources/blog/introduction-to-repository-design-pattern/)
- [@video@Tutorial - Repository Design Pattern](https://www.youtube.com/watch?v=mb6bwnEaZ3U)

## Scope  Visibility

# Scope Visibility

Scope visibility refers to the accessibility or visibility of variables, functions, and other elements in a program, depending on the context in which they are defined. In object-oriented programming (OOP), scope visibility is controlled through the use of access modifiers, such as "public," "private," and "protected."

*   Public: A public element can be accessed from anywhere in the program, both within the class and outside of it.
*   Private: A private element can only be accessed within the class in which it is defined. It is not accessible to other classes, even if they inherit from the class.
*   Protected: A protected element can only be accessed within the class and its subclasses.

There are variations of scope visibility based on the programming language, but these are the most common.

## Serverless Architecture

# Serverless Architecture

Serverless architecture is a design pattern that allows developers to build and run applications and services without having to provision and manage servers. Instead, these applications and services are executed in a fully managed environment, such as AWS Lambda, Azure Functions, or Google Cloud Functions, where the infrastructure and scaling are handled automatically by the cloud provider.

This architecture pattern mainly focuses on the business logic and event-driven execution, rather than on server management. It allows developers to write and deploy code in small, single-purpose functions that are triggered by specific events, such as changes in a database or the arrival of new data in a stream.

Visit the following resources to learn more:

- [@article@Serverless Architecture Patterns in AWS](https://waswani.medium.com/serverless-architecture-patterns-in-aws-edeab0e46a32)
- [@feed@Explore top posts about Architecture](https://app.daily.dev/tags/architecture?ref=roadmapsh)

## Soa

# SOA

SOA (Service-Oriented Architecture) is an architectural pattern that is used to design and organize software systems as a collection of services that can be accessed over a network, these services are autonomous, self-contained units of functionality that can be reused and combined to create new functionality. SOA services are designed to be loosely coupled, meaning that they do not depend on the implementation details of other services, they communicate with each other through well-defined interfaces, usually using a protocol such as HTTP or SOAP. SOA provides several advantages over other architectural patterns, such as reusability, modularity, interoperability, and scalability. It can be implemented using a variety of technologies, such as Web Services, REST, and microservices.

Visit the following resources to learn more:

- [@article@Overview of Service-Oriented Architecture](https://medium.com/design-microservices-architecture-with-patterns/service-oriented-architecture-1e4716fbca17)
- [@video@Tutorial - Service-Oriented Architecture -SOA](https://www.youtube.com/watch?v=jNiEMmoTDoE)
- [@video@What is Service-Oriented Architecture](https://www.youtube.com/watch?v=_dFJOSR-aFs)
- [@feed@Explore top posts about Architecture](https://app.daily.dev/tags/architecture?ref=roadmapsh)

## Solid

# SOLID

SOLID is an acronym that stands for five principles of object-oriented software development, which were first introduced by Robert C. Martin in the early 2000s. These principles are:

*   Single Responsibility Principle (SRP)
*   Open/Closed Principle (OCP)
*   Liskov Substitution Principle (LSP)
*   Interface Segregation Principle (ISP)
*   Dependency Inversion Principle (DIP)

Visit the following resources to learn more:

- [@article@Get Started with SOLID](https://www.bmc.com/blogs/solid-design-principles/)
- [@article@SOLID Principles](https://khalilstemmler.com/articles/tags/solid/)
- [@video@Tutorial - What are SOLID principle?](https://www.youtube.com/watch?v=aUCo5cy32kE)

## Structural

# Structural

Structural architecture in software refers to the organization and design of the components of a software system, and how they interact with each other. It deals with the physical organization of the system, and the relationships between the different components.

There are several different structural architecture patterns and styles that can be used to design software systems, including:

*   Monolithic: where the system is built as a single, integrated, and self-contained unit.
*   Layered: where the system is divided into a set of layers, each of which has a specific responsibility and communicates with the other layers through well-defined interfaces.
*   Microservices: where the system is built as a collection of small, independent, and loosely-coupled services.
*   Event-driven: where the system reacts to specific events that occur, rather than being continuously polled for changes.
*   Client-Server: where a client sends requests to a server, and the server responds to those requests
*   Peer-to-Peer: where each node in the network acts as both a client and a server
*   Component-based: where the system is composed of reusable and independent software components
*   Domain-Driven: where the system is organized around the core business domain and business entities.

## Structured Programming

# Structured Programming

Structured programming is a programming paradigm that emphasizes the use of well-structured control flow constructs such as loops, conditionals, and subroutines. It was developed in the 1960s and 1970s as a reaction to the "spaghetti code" produced by the widespread use of goto statements.

Visit the following resources to learn more:

- [@article@Structured Programming Wikipedia](https://en.wikipedia.org/wiki/Structured_programming)
- [@feed@Explore top posts about General Programming](https://app.daily.dev/tags/general-programming?ref=roadmapsh)

## Tell Dont Ask

# Tell, Don’t Ask

The Tell, Don’t Ask principle emphasizes that objects should be told what to do rather than being queried for their state and having decisions made externally. This promotes encapsulation and reduces coupling by keeping logic within the objects that own the data.

Key Concepts
------------

*   Instead of pulling data out of objects to make decisions, push the behavior into the object itself.
*   Objects should be responsible for their own logic and state management.

Asking style (bad):

    if (user.profile.isComplete()) {
        // allow checkout
    }
    

Telling style (good):

    if (user.canCheckout()) {
        // allow checkout
    }

Visit the following resources to learn more:

- [@article@Tell, Don't Ask](https://martinfowler.com/bliki/TellDontAsk.html)

## Tests Should Be Fast And Independent

# Tests Should Be Fast and Independent

Fast and independent tests are a cornerstone of reliable and maintainable software. They enable developers to run tests frequently, get quick feedback, and trust the results. When tests are slow or tightly coupled to each other or external systems, they become a bottleneck and reduce confidence in the codebase.

Well-designed tests focus on validating behavior in isolation and execute quickly enough to be run as part of everyday development.

Some of the key principles of fast and independent tests include:

*   Speed: Tests should execute quickly so they can be run frequently during development.
*   Independence: Each test should run in isolation and not depend on the outcome or state of other tests.
*   Determinism: Tests should produce the same result every time they are run.
*   Isolation: External dependencies (databases, APIs, file systems, time) should be mocked or stubbed.
*   Single Responsibility: Each test should verify one behavior or scenario.
*   Easy Setup and Teardown: Tests should have minimal and clear setup logic.
*   Reliability: Tests should fail only when the code under test is broken, not due to environment issues.
*   Automation Friendly: Tests should be easy to run in CI/CD pipelines without special configuration.
*   Maintainability: Tests should be easy to read, understand, and update as the code evolves.
*   Feedback-Oriented: Test failures should provide clear and actionable feedback.

Fast and independent tests improve developer productivity, encourage refactoring, and act as living documentation for the system’s behavior.

Visit the following resources to learn more:

- [@article@Unit Testing Best Practices](https://martinfowler.com/articles/practical-test-pyramid.html)
- [@article@Test Pyramid Explained](https://martinfowler.com/bliki/TestPyramid.html)
- [@article@Writing Reliable Tests](https://testing.googleblog.com/2014/05/testing-on-toilet-how-much.html)
- [@feed@Explore top posts about Testing](https://app.daily.dev/tags/testing?ref=roadmapsh)

## Transaction Script

# Transaction Script

Transaction Script is a pattern used in enterprise application development that organizes business logic into a single procedural script. It is often used for simple CRUD (create, read, update, delete) operations, where all of the logic for a specific transaction is contained in a single script or function. This pattern is simple to implement and easy to understand, but can become unwieldy as the complexity of the application increases. Alternative patterns such as Domain-Driven Design (DDD) and the Active Record pattern may be more appropriate for more complex applications.

Visit the following resources to learn more:

- [@article@Transaction Script Pattern](https://gunnarpeipman.com/transaction-script-pattern/)
- [@video@Tutorial - Transaction Script Design Pattern](https://www.youtube.com/watch?v=fnsU9cqcY3I)

## Use Correct Constructs

# Use Correct Constructs

In the context of clean code principles, "using correct constructs" refers to using appropriate programming constructs, such as loops, conditionals, and functions, in a way that makes the code easy to understand, maintain, and modify.

When using correct constructs, the code should be organized in a logical and intuitive way, making use of appropriate control flow statements and data structures to accomplish the task at hand. This also means that the code should avoid using unnecessary or overly complex constructs that make the code harder to understand or reason about.

Additionally, correct constructs also means to use the right constructs for the right problem, for example, if you want to iterate over an array, use a for loop instead of recursion and also, you should avoid using global variables and instead use function arguments and return values to pass data between different parts of the code.

By using correct constructs, the code will be more readable, more maintainable, and less prone to bugs, making it easier for other developers to understand, debug and extend the code.

## Usecases

# Use Cases

Use Cases are a pattern used in enterprise application development to represent the functional requirements of a system. They describe the interactions between the system and its users, and the steps that are required to accomplish a specific goal. Use cases are a way to capture the requirements of the system in a way that is easily understood by both the development team and the stakeholders.

A use case is a description of a sequence of actions that a system performs in response to a request from a user, in order to achieve a specific goal. A use case typically includes:

*   The actor (user) who initiates the action
*   The goal that the actor wants to achieve
*   The steps required to achieve the goal, including any alternative paths or error conditions
*   The expected outcome of the interaction

Use cases are often used to drive the design and development of the system, as they provide a clear and detailed understanding of the requirements.

Visit the following resources to learn more:

- [@article@Use Case Patterns](https://caminao.blog/how-to-implement-symbolic-representations/patterns/functional-patterns/use-case-patterns/)

## Value Objects

# Value Objects

Value Objects are a pattern used in enterprise application development to represent simple, immutable values that are used to model domain concepts. They are typically used to encapsulate data that is not an entity, but is important to the domain.

A Value Object is defined by its value rather than its identity, meaning that two Value Objects with the same value are considered to be equal, regardless of their identity.

Visit the following resources to learn more:

- [@article@Overview - Implement Value Objects](https://learn.microsoft.com/en-us/dotnet/architecture/microservices/microservice-ddd-cqrs-patterns/implement-value-objects)
- [@article@Intro to Value object](https://en.wikipedia.org/wiki/Value_object)

## Yagni

# YAGNI

YAGNI (You Ain't Gonna Need It) is a software development principle that suggests that developers should not add functionality to a codebase unless it is immediately necessary. The idea is to avoid creating unnecessary complexity in the codebase by only adding features that are actually needed.

The YAGNI principle is closely related to the Single Responsibility Principle (SRP) and the Open-Closed Principle (OCP), which are part of the SOLID principles. YAGNI aims to keep the codebase as simple as possible by avoiding the creation of unnecessary abstractions and functionality.

Visit the following resources to learn more:

- [@article@YAGNI (You Aren't Gonna Need It) Principle Helps in Efficiency](https://builtin.com/software-engineering-perspectives/yagni)
- [@video@What is YAGNI coding rule, and Why it helps?](https://www.youtube.com/watch?v=2vys1q1dKc4)
