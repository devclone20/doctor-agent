# Graphql Roadmap

## Aliases

# Aliases

Aliases in GraphQL rename fields in query responses, useful when requesting the same field multiple times with different arguments or when field names aren't suitable for client usage. They distinguish fields in responses and improve query readability and usability.

Visit the following resources to learn more:

- [@official@What are GraphQL Aliases?](https://graphql.org/learn/queries/#aliases)

## Apollo Client

# Apollo Client

Apollo Client is a popular GraphQL client library for JavaScript that provides data fetching, caching, and state management. It offers declarative data fetching with React hooks, intelligent caching, optimistic UI updates, and error handling for building efficient GraphQL-powered applications.

Visit the following resources to learn more:

- [@article@Why Apollo Client - Frontend?](https://www.howtographql.com/react-apollo/0-introduction/)
- [@feed@Explore top posts about Apollo](https://app.daily.dev/tags/apollo?ref=roadmapsh)

## Apollo Server

# Apollo Server

Apollo Server is a popular open-source library for building GraphQL servers in JavaScript. It provides tools for parsing, validating, executing resolvers, and formatting responses with built-in features for authentication, authorization, data validation, and real-time subscriptions.

Visit the following resources to learn more:

- [@article@Apollo Tutorial - Introduction](https://www.howtographql.com/react-apollo/0-introduction/)
- [@feed@Explore top posts about Apollo](https://app.daily.dev/tags/apollo?ref=roadmapsh)

## Arguments

# Arguments

Arguments in GraphQL are values passed to fields in queries and mutations to filter or modify returned data. They're defined in the schema with a name, type, and optional default value, enabling dynamic data retrieval.

Visit the following resources to learn more:

- [@official@Get started with Arguments in GraphQL](https://graphql.org/learn/schema/#arguments)

## Arguments

# Arguments

Arguments in GraphQL are values passed to fields or directives to specify execution details like filtering, sorting, pagination, or configuration options. They're passed as key-value pairs, can be defined as variables, and may be optional or required depending on the field definition.

Visit the following resources to learn more:

- [@official@GraphQL - Arguments](https://graphql.org/learn/queries/#arguments)

## Asynchronous

# Asynchronous

Asynchronous resolvers in GraphQL are functions that return promises instead of immediate values. They allow resolvers to wait for external operations like database queries or API calls to complete before returning results, enabling non-blocking execution.

Visit the following resources to learn more:

- [@official@Get Started with Asynchronous](https://graphql.org/learn/execution/#asynchronous-resolvers)

## Authorization

# Authorization

Authorization in GraphQL controls access to data and operations based on user permissions and roles. It can be implemented at the schema level, field level, or within resolvers, ensuring users only access data they're permitted to see through various authentication and permission strategies.

There are several ways to implement authorization in GraphQL:

*   Using middleware
*   Using schema directives
*   Using a data source layer

Visit the following resources to learn more:

- [@official@Get Started with Authorization](https://graphql.org/learn/authorization/)
- [@feed@Explore top posts about Authorization](https://app.daily.dev/tags/authorization?ref=roadmapsh)

## Authorization

# Authorization

Authorization in GraphQL refers to the process of controlling access to specific fields, types, or operations in a GraphQL schema based on user roles or permissions. It allows you to restrict access to certain data or functionality in your application based on the user's role or permissions.

There are several ways to implement authorization in GraphQL:

*   Using middleware
*   Using schema directives
*   Using a data source layer

Visit the following resources to learn more:

- [@official@Get Started with Authorization](https://graphql.org/learn/authorization/)
- [@feed@Explore top posts about Authorization](https://app.daily.dev/tags/authorization?ref=roadmapsh)

## Authorization

# Authorization

Authorization in GraphQL refers to the process of controlling access to specific fields, types, or operations in a GraphQL schema based on user roles or permissions. It allows you to restrict access to certain data or functionality in your application based on the user's role or permissions.

There are several ways to implement authorization in GraphQL:

*   Using middleware
*   Using schema directives
*   Using a data source layer

Visit the following resources to learn more:

- [@official@Get Started with Authorization](https://graphql.org/learn/authorization/)
- [@feed@Explore top posts about Authorization](https://app.daily.dev/tags/authorization?ref=roadmapsh)

## Batching

# Batching

Batching in GraphQL combines multiple queries into a single request to reduce network overhead and improve performance. DataLoader is a common pattern that batches and caches database requests, preventing N+1 query problems and optimizing data fetching efficiency.

Visit the following resources to learn more:

- [@opensource@DataLoader](https://github.com/graphql/dataloader)
- [@article@Solving the N+1 Problem](https://shopify.engineering/solving-the-n-1-problem-for-graphql-through-batching)

## Caching

# Caching

Caching in GraphQL improves performance by storing query results for reuse. Strategies include HTTP caching, response caching, dataloader for batching requests, and normalized caching at the client level to reduce redundant API calls and improve user experience.

There are several types of caching that can be used in GraphQL:

*   Client-side caching
*   Server-side caching
*   CDN caching

Visit the following resources to learn more:

- [@official@Get started with Caching](https://graphql.org/learn/caching/)

## Defer  Stream Directives

# Defer & Stream Directives

Defer and Stream directives are experimental GraphQL features for incremental data delivery. @defer postpones non-critical fields to improve initial response times, while @stream sends list items progressively, enabling better user experiences with large datasets and slow-loading fields.

Visit the following resources to learn more:

- [@article@Defer and Stream in GraphQL](https://the-guild.dev/graphql/yoga-server/docs/features/defer-stream)

## Directives

# Directives

Directives in GraphQL modify query execution by adding behavior or validation to fields, operations, and fragments. They can take arguments to configure behavior and include built-in directives like @include and @skip, or custom ones defined by developers for specific functionality.

Visit the following resources to learn more:

- [@official@Directives in GraphQL](https://graphql.org/learn/queries/#directives)

## Enums

# Enums

Enums (enumeration types) are special scalars restricted to a particular set of allowed values. They validate arguments against allowed values and communicate through the type system that fields will always be one of a finite set of predefined options.

Visit the following resources to learn more:

- [@official@What are Enums?](https://graphql.org/learn/schema/#enumeration-types)

## Event Based Subscriptions

# Event-Based Subscriptions

Event-based subscriptions in GraphQL provide real-time updates by subscribing to specific events or data changes. Clients maintain persistent connections through WebSockets to receive live updates when subscribed events occur, enabling reactive applications with real-time functionality.

Visit the following resources to learn more:

- [@official@GraphQL Subscriptions Documentation](https://graphql.org/blog/subscriptions-in-graphql-and-relay/)
- [@article@GraphQL Subscriptions](https://the-guild.dev/blog/subscriptions-and-live-queries-real-time-with-graphql)

## Execution

# Execution

Execution in GraphQL is the process of running queries or mutations and returning results to clients. The GraphQL engine performs parsing, validation, and data retrieval steps to produce the final response, coordinating resolver functions to fetch data from various sources.

Visit the following resources to learn more:

- [@official@Get Started with Execution in GraphQL](https://graphql.org/learn/execution/)
- [@official@Intro to Execution](https://graphql.org/graphql-js/execution/)

## Fields

# Fields

Fields in GraphQL are units of data that can be queried or manipulated. Each field has a name, type, and optional description, and can return scalar values or objects, enabling complex nested data structures and taking arguments for filtering.

Visit the following resources to learn more:

- [@official@GraphQL: Types and Fields](https://graphql.org/learn/queries/#fields)

## Fields

# Fields

Fields in GraphQL are individual pieces of data that can be queried or modified, representing properties of the requested data. They're defined in the GraphQL schema and serve as building blocks for queries and mutations, specifying what data is available for each type.

Visit the following resources to learn more:

- [@official@GraphQL: Types and Fields](https://graphql.org/learn/queries/#fields)

## Fragments

# Fragments

Fragments in GraphQL are reusable pieces of queries that retrieve specific fields from one or more types. Defined with the "fragment" keyword, they promote code reuse, reduce duplication, and make complex queries more maintainable by separating common field selections.

Visit the following resources to learn more:

- [@official@Intro to Fragments in GraphQL](https://graphql.org/learn/queries/#fragments)

## Graphql Go

# GraphQL Go

GraphQL Go refers to implementing GraphQL servers and clients using the Go programming language. Popular libraries include graphql-go/graphql for schema-first development and 99designs/gqlgen for code-first generation. Go's strong typing and performance make it excellent for building scalable GraphQL APIs.

Visit the following resources to learn more:

- [@opensource@graphql-go/graphql](https://github.com/graphql-go/graphql)
- [@opensource@99designs/gqlgen](https://github.com/99designs/gqlgen)

## Graphql Http

# graphql-http

GraphQL over HTTP is a specification that defines how GraphQL queries and mutations should be transported over HTTP. It standardizes request/response formats, HTTP methods, status codes, and headers, ensuring consistent GraphQL API communication across different implementations.

Visit the following resources to learn more:

- [@official@GraphQL over HTTP Specification](https://graphql.github.io/graphql-over-http/)
- [@opensource@graphql-http Library](https://github.com/graphql/graphql-http)

## Graphql Http

# GraphQL HTTP

GraphQL HTTP is a specification for serving GraphQL over HTTP protocol. It defines standard methods for sending queries and mutations, primarily using POST requests with JSON payloads in the request body, and receiving results in the response body.

Visit the following resources to learn more:

- [@official@Overview of GraphQL HTTP](https://graphql.org/graphql-js/express-graphql/#graphqlhttp)
- [@official@Get Started with GraphQL HTTP](https://graphql.org/learn/serving-over-http/)
- [@feed@Explore top posts about GraphQL](https://app.daily.dev/tags/graphql?ref=roadmapsh)

## Graphql Java

# GraphQL Java

GraphQL Java is a popular library for implementing GraphQL APIs in Java applications. It provides schema-first development capabilities, runtime query execution, and integrates well with Spring Boot and other Java frameworks, making it a solid choice for enterprise GraphQL implementations.

Visit the following resources to learn more:

- [@official@GraphQL Java Repository](https://github.com/graphql-java/graphql-java)
- [@article@GraphQL Java Documentation](https://www.graphql-java.com/)

## Graphql On Backend

# GraphQL on the Backend

GraphQL on the backend involves implementing servers that execute GraphQL queries, mutations, and subscriptions. It includes defining schemas, writing resolvers, handling data sources, implementing authentication/authorization, and optimizing performance through caching and batching strategies.

Visit the following resources to learn more:

- [@article@How to use GraphQL in Backend?](https://www.howtographql.com/)
- [@feed@Explore top posts about Backend Development](https://app.daily.dev/tags/backend?ref=roadmapsh)

## Graphql On Frontend

# GraphQL on the Frontend

GraphQL on the frontend enables efficient data fetching with clients like Apollo, URQL, or Relay. It provides declarative data requirements, intelligent caching, real-time subscriptions, and type safety, allowing frontend applications to request exactly the data they need in a single query.

Visit the following resources to learn more:

- [@article@Get started with GraphQL on the frontend](https://www.howtographql.com/react-apollo/0-introduction/)
- [@feed@Explore top posts about Frontend Development](https://app.daily.dev/tags/frontend?ref=roadmapsh)

## Graphql Over Http Spec

# GraphQL Over HTTP Spec

The GraphQL over HTTP specification defines standard practices for serving GraphQL over HTTP, including request/response formats, status codes, and content types. It ensures interoperability between different GraphQL implementations and provides guidance for consistent API behavior across platforms.

## Graphql Queries

# GraphQL Queries

GraphQL queries are client requests to retrieve specific data from a server. They specify exactly which fields should be returned, using a hierarchical structure that matches the data requirements. Queries are written in GraphQL syntax and executed by the server to fetch the requested data.

Visit the following resources to learn more:

- [@official@What are GraphQL Queries?](https://graphql.org/learn/queries/)
- [@feed@Explore top posts about GraphQL](https://app.daily.dev/tags/graphql?ref=roadmapsh)

## Graphql Yoga

# GraphQL Yoga

GraphQL Yoga is an open-source GraphQL server library for Node.js built on Express.js. It provides minimal boilerplate setup with built-in authentication, authorization, data validation, and subscription support for real-time updates, making GraphQL server development streamlined.

Visit the following resources to learn more:

- [@article@GraphQL Armor - for Yoga Server 2](https://the-guild.dev/blog/improved-security-with-graphql-armor-support-for-yoga-server-2)
- [@feed@Explore top posts about GraphQL](https://app.daily.dev/tags/graphql?ref=roadmapsh)

## Graphqljs

# GraphQL.js

GraphQL.js is the reference implementation of GraphQL for JavaScript and Node.js. It provides the core functionality for parsing, validating, and executing GraphQL queries, serving as the foundation for many other GraphQL tools and libraries in the JavaScript ecosystem.

Visit the following resources to learn more:

- [@official@GraphQL.js Repository](https://github.com/graphql/graphql-js)
- [@official@GraphQL.js Documentation](https://graphql.org/graphql-js/)

## Interfaces

# Interfaces

Interfaces in GraphQL define a set of fields that implementing types must include. They enable polymorphism by allowing common field querying across different types that implement the same interface, promoting code reuse and consistent API design.

Visit the following resources to learn more:

- [@official@Get started with Interfaces](https://graphql.org/learn/schema/#interfaces)

## Introduction

# GraphQL Introduction

GraphQL is a query language and runtime for APIs that enables clients to request exactly the data they need in a single call. It provides a predictable format, reducing multiple API calls and eliminating over-fetching, making data retrieval more efficient than traditional REST APIs.

Visit the following resources to learn more:

- [@official@Introduction to GraphQL](https://graphql.org/learn/)
- [@official@Getting started with GraphQL](https://graphql.org/)
- [@feed@Explore top posts about GraphQL](https://app.daily.dev/tags/graphql?ref=roadmapsh)

## Lists

# Lists

Lists in GraphQL represent ordered collections of items, defined using square brackets around the item type. They can contain scalars, objects, or other lists, enabling complex nested data structures and array-based field returns in schemas.

Visit the following resources to learn more:

- [@official@Get started with Lists](https://graphql.org/learn/schema/#lists-and-non-null)

## Lists

# Lists

Lists in GraphQL represent ordered collections of items and can be used as return types for fields. They can contain any type of items including scalars and objects, with resolver functions typically returning data as arrays from databases or APIs.

Visit the following resources to learn more:

- [@official@Get started with Lists and Non-Null](https://graphql.org/learn/schema/#lists-and-non-null)

## Live Queries

# Live Queries

Live Queries automatically update query results when underlying data changes, providing real-time synchronization without manual subscription management. This advanced feature simplifies building reactive applications by maintaining fresh data automatically, though it requires specialized GraphQL implementations.

Visit the following resources to learn more:

- [@article@GraphQL Live Queries](https://the-guild.dev/blog/collecting-graphql-live-query-resource-identifier-with-graphql-tools)

## Mercurius

# Mercurius

Mercurius is a high-performance GraphQL server library for Fastify, offering excellent performance and minimal memory usage. It provides schema-first development, built-in caching, subscriptions support, and integration with Fastify's ecosystem for building fast, scalable GraphQL APIs.

Visit the following resources to learn more:

- [@opensource@Mercurius Repository](https://github.com/mercurius-js/mercurius)
- [@article@Mercurius Documentation](https://mercurius.dev/)

## Multiple Fields In Mutation

# Multiple Mutation Fields

GraphQL allows multiple mutations in a single query by including multiple mutation fields, a practice often called batching mutations. This approach improves network efficiency by reducing the number of round-trips between the client and server.

Visit the following resources to learn more:

- [@official@Guide to Multiple fields in mutations](https://graphql.org/learn/mutations/#multiple-fields-in-mutations)

## Mutations

# Mutations

Mutations in GraphQL are used to modify data on the server, including creating, updating, or deleting records. They're structured like queries but use the "mutation" field at the top level and include fields specifying the data to be changed and the operation type.

Visit the following resources to learn more:

- [@official@Getting started with Mutations](https://graphql.org/learn/queries/#mutations)

## Objects

# Objects

Objects in GraphQL are types that represent groups of fields, defining the structure of queries and mutations. Each field can return scalar values or other objects, enabling complex nested data structures. Objects are defined using the "type" keyword followed by the name and field definitions.

Visit the following resources to learn more:

- [@official@Object Types and Fields](https://graphql.org/learn/schema/#object-types-and-fields)
- [@official@Object Types](https://graphql.org/graphql-js/object-types/)

## Operation Name

# Operation Name

Operation names are optional identifiers for GraphQL queries and mutations that help uniquely identify operations in documents with multiple operations. They provide meaningful names for operations, improve debugging, and make error identification easier in complex applications.

Visit the following resources to learn more:

- [@official@Intro to Operation Name](https://graphql.org/learn/queries/#operation-name)

## Pagination

# Pagination

Pagination in GraphQL handles large datasets by breaking them into smaller chunks. Common approaches include cursor-based pagination (using cursors for stable pagination) and offset-based pagination (using skip/take), with cursor-based being preferred for performance and consistency.

Visit the following resources to learn more:

- [@official@Get Started with Pagination](https://graphql.org/learn/pagination/)

## Problems Graphql Solves

# Problems GraphQL Solves

GraphQL solves major API problems including over-fetching (getting unnecessary data), under-fetching (multiple requests needed), inefficient versioning, and lack of flexibility. It enables precise data requests, single queries for multiple resources, seamless versioning through schema evolution, and microservice communication through federation.

## Producing The Result

# Producing The Result

Producing the result in GraphQL involves generating the final response to queries and mutations. This process includes parsing the request, validating against the schema, executing resolvers to fetch data, and formatting the response according to the query requirements.

Visit the following resources to learn more:

- [@official@Get Started with GraphQL](https://graphql.org/learn/)

## Realtime

# Realtime

Realtime GraphQL enables live data updates through subscriptions, allowing clients to receive instant notifications when data changes. Implemented using WebSockets, Server-Sent Events, or polling, it's essential for chat applications, live feeds, and collaborative tools requiring immediate data synchronization.

Visit the following resources to learn more:

- [@article@Get Started with Real Time with GraphQL](https://the-guild.dev/blog/subscriptions-and-live-queries-real-time-with-graphql)

## Relay

# Relay

Relay is Facebook's GraphQL client designed for React applications, emphasizing performance and data consistency. It uses a declarative approach with fragments, automatic query optimization, pagination handling, and strict conventions for building scalable, efficient GraphQL applications.

Visit the following resources to learn more:

- [@article@GraphQL Code Generator & Relay Compiler](https://the-guild.dev/blog/graphql-codegen-relay-compiler)

## Resolvers

# Resolvers

Resolvers are functions responsible for fetching data for each field in GraphQL queries and mutations. Defined in the schema and executed by the GraphQL server, they retrieve data from databases, APIs, or other sources and return it to clients.

Visit the following resources to learn more:

- [@article@Guide to Resolver](https://the-guild.dev/blog/better-type-safety-for-resolvers-with-graphql-codegen)

## Root Fields

# Root Fields

Root fields are the top-level fields available to clients in GraphQL queries and mutations. They serve as entry points for client requests, with Query fields for retrieving data and Mutation fields for modifying data on the server.

Visit the following resources to learn more:

- [@official@Get Started with Root Fields](https://graphql.org/learn/execution/#root-fields-resolvers)

## Scalar Coercion

# Scalar Coercion

Scalar coercion in GraphQL converts input values from one type to another when they don't match the expected type but can be successfully converted. This process is implemented using custom scalar types with coerce functions that handle the type conversion.

Visit the following resources to learn more:

- [@official@Get started with Scalar coercion](https://graphql.org/learn/execution/#scalar-coercion)

## Scalars

# Scalars

Scalars are "leaf" values in GraphQL representing primitive data types. Built-in scalars include String, Int, Float, Boolean, and ID for unique identifiers. Custom scalars can be defined for specific needs like dates, JSON, or large integers, extending the type system beyond basic primitives.

Visit the following resources to learn more:

- [@official@Get started with Scalars in GraphQL](https://graphql.org/learn/schema/#scalar-types)

## Schema

# Schema

A GraphQL schema defines the structure and capabilities of a GraphQL API using Schema Definition Language (SDL). It specifies types, fields, arguments, relationships, and root operations (Query, Mutation, Subscription) that serve as entry points, acting as a contract between client and server.

Visit the following resources to learn more:

- [@official@What is Schema?](https://graphql.org/learn/schema/)

## Serving Over Internet

# Serving over Internet

Serving GraphQL over the internet involves making a GraphQL server accessible to clients through a public IP address or domain name. This can be done using reverse proxies, cloud services, or serverless functions to expose the GraphQL endpoint publicly.

Visit the following resources to learn more:

- [@official@Introduction to Serving over HTTPs](https://graphql.org/learn/serving-over-http/)

## Specification

# Specification

The GraphQL specification is the official standard that defines the GraphQL query language, type system, execution algorithm, and validation rules. It ensures consistency across different GraphQL implementations and serves as the authoritative reference for developers building GraphQL services and tools.

Visit the following resources to learn more:

- [@official@GraphQL Specification](https://spec.graphql.org/)
- [@official@GraphQL Foundation](https://foundation.graphql.org/)

## Specification

# Specification

The GraphQL specification defines the core language, type system, execution model, and validation rules for GraphQL. Maintained by the GraphQL Foundation, it provides the technical foundation that all GraphQL implementations must follow to ensure interoperability and consistency across platforms.

Visit the following resources to learn more:

- [@official@GraphQL Specification](https://spec.graphql.org/)
- [@official@GraphQL Foundation](https://foundation.graphql.org/)

## Subscriptions

# Subscriptions

Subscriptions in GraphQL enable real-time updates by allowing clients to subscribe to specific events or data changes on the server. The server maintains an open connection and pushes updates to subscribed clients as soon as events occur or data changes.

Visit the following resources to learn more:

- [@article@Subscriptions and Live Queries - Real Time with GraphQL](https://the-guild.dev/blog/subscriptions-and-live-queries-real-time-with-graphql)

## Synchronous

# Synchronous

Synchronous resolvers in GraphQL execute immediately and return their results directly without waiting for external operations. They complete their execution before returning any value, making them simpler but potentially blocking if they perform complex computations.

Visit the following resources to learn more:

- [@official@GraphQL Execution](https://graphql.org/learn/execution/)
- [@article@Understanding Resolvers](https://www.apollographql.com/docs/apollo-server/data/resolvers/)

## Thinking In Graphs

# Thinking in Graphs

"Thinking in Graphs" is a GraphQL mindset where data is organized as a graph with nodes (objects) and edges (relationships). This approach allows flexible and intuitive querying by following relationships between connected data points, making complex data retrieval more natural and efficient.

Visit the following resources to learn more:

- [@official@GraphQL - Thinking in Graphs](https://graphql.org/learn/thinking-in-graphs/)

## Type System

# Type System

GraphQL is strongly typed with a type system that defines data types available in applications. It includes Scalar, Object, Query, Mutation, and Enum types. The type system defines the schema, acting as a contract between client and server for predictable API interactions.

Visit the following resources to learn more:

- [@official@Get started with Type system](https://graphql.org/learn/schema/#type-system)

## Unions

# Unions

Unions allow fields to return multiple types, enabling different handling for various types in clients. They provide schema flexibility by grouping types together, though they don't allow common field querying across types like interfaces do.

Visit the following resources to learn more:

- [@official@Get started with Union in GraphQL](https://graphql.org/learn/schema/#union-types)

## Urql

# URQL

URQL is a lightweight, highly customizable GraphQL client for React, Vue, and Svelte. It provides caching, real-time subscriptions, offline support, and a modular architecture with exchanges for extending functionality, offering an alternative to Apollo Client with better performance.

Visit the following resources to learn more:

- [@article@urql - Formidable Labs](https://formidable.com/open-source/urql/)

## Validation

# Validation

Validation in GraphQL ensures queries and mutations adhere to schema rules by verifying field access, type correctness, and input constraints. GraphQL servers validate all incoming operations before execution, returning errors for invalid queries with specific details about violations.

Visit the following resources to learn more:

- [@official@Get Started with Validation in GraphQL](https://graphql.org/learn/validation/)

## Validation

# Validation

Validation in GraphQL ensures queries and mutations conform to schema rules and constraints. It checks for required fields, correct argument types, and value ranges before execution, preventing invalid operations and improving API reliability.

Visit the following resources to learn more:

- [@official@Get Started with Validation in GraphQL](https://graphql.org/learn/validation/)

## Variables

# Variables

Variables in GraphQL pass dynamic values to queries and mutations, making them flexible and reusable. Defined with the $ symbol and a type, their values are passed in a separate JSON object. Variables are type-safe, ensuring values match the defined types.

Visit the following resources to learn more:

- [@official@Intro to Variables in GraphQL](https://graphql.org/learn/queries/#variables)
- [@article@GraphQL Variables](https://dgraph.io/docs/graphql/api/variables/)

## What Are Mutations

# What are Mutations

Mutations in GraphQL are operations used to modify data on the server - creating, updating, or deleting records. They're structured like queries but use the "mutation" field at the top level and include fields specifying the data to be changed and the operation type.

Visit the following resources to learn more:

- [@official@Get started with Mutations](https://graphql.org/learn/mutations/)

## What Are Queries

# What are Queries

In GraphQL, queries are client requests to retrieve data from the server. They're structured as hierarchical trees of fields that correspond to the properties of the requested data, allowing clients to specify exactly what data they need in a predictable format.

Visit the following resources to learn more:

- [@official@Introduction of GraphQL - Query](https://graphql.org/learn/queries/)

## What Are Subscriptions

# What are Subscriptions

Subscriptions in GraphQL enable real-time updates by allowing clients to subscribe to specific events or data changes on the server. They're structured like queries with a "subscription" field at the top level and push updates to clients as soon as events occur.

Visit the following resources to learn more:

- [@article@How GraphQL Subscriptions Work?](https://the-guild.dev/blog/subscriptions-and-live-queries-real-time-with-graphql)

## What Is Graphql

# What is GraphQL

GraphQL is a query language for APIs and server-side runtime that lets clients request exactly the data they need. Unlike REST, it uses a type system to define data structure and allows fetching multiple resources in a single request, reducing over-fetching and under-fetching problems.

Visit the following resources to learn more:

- [@official@Introduction to graphQL](https://graphql.org/learn/)
- [@article@Tutorial - What is graphQL?](https://www.howtographql.com/basics/0-introduction/)
- [@feed@Explore top posts about GraphQL](https://app.daily.dev/tags/graphql?ref=roadmapsh)
