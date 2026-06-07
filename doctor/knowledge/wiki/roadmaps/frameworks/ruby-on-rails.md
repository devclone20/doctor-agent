# Ruby On Rails Roadmap

## Accessibility

# Accessibility

Accessibility, often shortened to A11y, focuses on designing and developing websites and applications that are usable by people with disabilities. This includes individuals with visual, auditory, motor, or cognitive impairments, ensuring they can perceive, understand, navigate, and interact with web content effectively. Implementing accessibility involves following established guidelines and best practices to create inclusive digital experiences.

## Action Views

# Action Views

Action View is the view component of the Ruby on Rails framework. It's responsible for rendering the user interface, typically in HTML, but also in other formats like XML or JSON. It handles tasks such as template rendering, layout management, and helper methods to simplify the creation of dynamic web pages.

Visit the following resources to learn more:

- [@official@Action View Overview](https://guides.rubyonrails.org/action_view_overview.html)
- [@article@Views](https://www.theodinproject.com/lessons/ruby-on-rails-views#introduction)
- [@article@Rails Views — The V in MVC](https://medium.com/@tafby88/rails-views-the-v-in-mvc-71e04d017791)
- [@video@Action View in Rails](https://www.youtube.com/watch?v=n2X_75Jja1A)

## Active Record

# Active Record

Active Record is the ORM (Object-Relational Mapping) layer within Ruby on Rails. It acts as an interface between your Ruby code and the database. Instead of writing raw SQL queries, you use Active Record's methods to interact with your database tables as if they were Ruby objects. This allows you to create, read, update, and delete data in a more intuitive and object-oriented way, simplifying database interactions within your Rails application.

Visit the following resources to learn more:

- [@official@Active Record Query Interface](https://guides.rubyonrails.org/active_record_querying.html#what-is-the-active-record-query-interface-questionmark)
- [@article@Active Record Queries](https://www.theodinproject.com/lessons/ruby-on-rails-active-record-queries)
- [@article@Advanced Queries in ActiveRecord for Ruby on Rails](https://blog.appsignal.com/2025/02/26/advanced-queries-in-activerecord-for-ruby-on-rails.html)
- [@video@Ep 4. Active Record explained | Rails New Tutorial with Typecraft](https://www.youtube.com/watch?v=n0TPEsKE9v0)

## Advanced Asset Management

# Advanced Asset Management

You can use advanced asset management techniques to optimize and organize your application's assets (images, stylesheets, JavaScript files) beyond the basic functionality provided by the asset pipeline. This includes strategies like using CDNs for faster delivery, implementing asset versioning for cache busting, precompiling assets for production environments, and employing tools for minification and compression to reduce file sizes and improve performance. It also covers techniques for organizing assets into logical groups and managing dependencies between them.

Visit the following resources to learn more:

- [@official@Advanced Asset Management](https://guides.rubyonrails.org/asset_pipeline.html#advanced-asset-management)

## Aggregations

# Aggregations

Aggregations in Active Record allow you to derive summary information from your database records. This involves performing calculations like finding the average, minimum, maximum, or sum of values across a set of records, or counting the number of records that meet certain criteria. These calculations are typically performed directly within the database for efficiency and can be easily accessed through your Rails models.

Visit the following resources to learn more:

- [@official@Grouping](https://guides.rubyonrails.org/active_record_querying.html#grouping)
- [@official@Calculations](https://guides.rubyonrails.org/active_record_querying.html#calculations)
- [@article@Grouping and Aggregating](https://backend.turing.edu/module2/lessons/grouping_and_aggregating)
- [@video@SQL Learning Path - Group By Statement](https://www.youtube.com/watch?v=KdI1IPVJlHg)

## App

# App Directory

The `app` directory in a Rails application is the heart of your project, containing the core logic and components that define its behavior. It's where you'll find the code responsible for handling user requests, interacting with the database, and rendering views. This directory is organized into subdirectories, each dedicated to a specific aspect of the application, such as models, views, and controllers.

## Assets Pipeline

# Assets Pipeline

The Assets Pipeline in Rails provides a structured way to manage and pre-process assets like stylesheets, JavaScript files, and images. It bundles, minifies, and compresses these assets to improve website performance by reducing the number of requests and the size of the files that need to be downloaded by the browser. It also allows you to use features like automatic CSS prefixing and CoffeeScript compilation.

Visit the following resources to learn more:

- [@official@The Asset Pipeline](https://guides.rubyonrails.org/asset_pipeline.html)
- [@article@The Asset Pipeline](https://www.theodinproject.com/lessons/ruby-on-rails-the-asset-pipeline)
- [@article@Rails Asset Pipeline](https://medium.com/@tali.scheer/rails-asset-pipeline-ab441688616a)
- [@article@Understanding the Asset Pipeline in Ruby on Rails](https://webcrunch.com/posts/understanding-asset-pipeline-ruby-on-rails)
- [@video@A Quick and Easy Guide to the Asset Pipeline in Rails 7](https://www.youtube.com/watch?v=cQQH9sEhnnY)
- [@video@Understanding The Rails Asset Pipeline](https://www.youtube.com/watch?v=maTYAac1ESI)

## Authentication

# Authentication

Authentication in Rails verifies the identity of users, ensuring they are who they claim to be before granting access to protected resources. It typically involves checking user credentials, like a username and password, against stored data to confirm their validity. Upon successful verification, a user session is created, allowing the application to remember the user across multiple requests without repeatedly asking for credentials. This process helps secure the application by restricting access to authorized users only.

Visit the following resources to learn more:

- [@official@Authentication](https://guides.rubyonrails.org/security.html#authentication)
- [@article@Rails Authentication: Gems vs. Recipes vs. Generators](https://masilotti.com/rails-authentication/)
- [@article@Authentication and Authorization in Ruby on Rails](https://medium.com/@zachlandis91/authentication-and-authorization-in-ruby-on-rails-c44c1ccea94d)
- [@video@Securing your app with the default Authentication Generator | Rails 8 Unpacked](https://www.youtube.com/watch?v=4q1RWZABhKE)
- [@video@How to Use Authentication in Ruby on Rails 8](https://www.youtube.com/watch?v=uGllXLfRx60)

## Authorization

# Authorization

Authorization determines what a user is allowed to do within an application. It focuses on verifying if a user has the necessary permissions to access specific resources or perform certain actions. This process happens after authentication, which confirms the user's identity and dictates the level of access granted based on their role or attributes.

Visit the following resources to learn more:

- [@article@Complete Guide To Managing User Permissions In Rails Apps](https://www.honeybadger.io/blog/complete-guide-to-managing-user-permissions-in-rails-apps/)
- [@article@Implementing Role-Based Access Control (RBAC) in Rails: A Comprehensive Guide](https://medium.com/@er.sumitsah/implementing-role-based-access-control-rbac-in-rails-a-comprehensive-guide-752194c8bffe)
- [@article@Authentication and Authorization in Ruby on Rails](https://www.shakacode.com/blog/mastering-authorization-in-rails-with-pundit/)

## Background Jobs

# Background Jobs in Rails

Background jobs allow you to perform time-consuming tasks outside of the main request-response cycle. This means your web application can remain responsive and quickly handle user requests, while the longer tasks are processed in the background. Rails achieves this using Active Job, a framework for declaring jobs and making them run on a variety of queuing backends like Sidekiq, Resque, or even a simple in-memory queue for development. This abstraction allows developers to write job logic once and easily switch between different background processing systems as needed.

Visit the following resources to learn more:

- [@official@Active Job Basics](https://guides.rubyonrails.org/active_job_basics.html)
- [@article@Rails Background Jobs — Reconstruct Your Application](https://medium.com/@hasnatraza.dev/rails-background-jobs-reconstruct-your-application-ccaef2860552)
- [@article@A Simple Guide to Background Jobs in Ruby on Rails](https://www.bluebash.co/blog/simple-guide-to-background-jobs-in-ruby-on-rails/)
- [@video@Manage asynchronous tasks with Solid Queue | Rails 8 Unpacked](https://www.youtube.com/watch?v=ReyKfb12EVU)
- [@video@Testing Active Job in Ruby on Rails](https://www.youtube.com/watch?v=7ieeu0r27ig)

## Basic Queries

# Basic Queries in Active Record

Active Record provides a powerful and intuitive interface for interacting with databases in Rails applications. Basic queries allow you to retrieve data from your database tables using simple and expressive methods. These methods enable you to find records based on various criteria, such as specific IDs, attribute values, or more complex conditions, forming the foundation for data retrieval operations within your Rails application.

Visit the following resources to learn more:

- [@official@Active Record Query Interface](https://guides.rubyonrails.org/active_record_querying.html)
- [@article@Active Record Queries](https://www.theodinproject.com/lessons/ruby-on-rails-active-record-queries)
- [@article@Advanced Queries in ActiveRecord for Ruby on Rails](https://blog.appsignal.com/2025/02/26/advanced-queries-in-activerecord-for-ruby-on-rails.html)
- [@article@Query Like a Pro: Active Record for Database Queries](https://dev.to/minchulan/exploring-rails-active-record-and-querying-with-relational-databases-3p2g)
- [@video@Ep 4. Active Record explained | Rails New Tutorial with Typecraft](https://www.youtube.com/watch?v=n0TPEsKE9v0)

## Better Errors

# Better Errors

Better Errors is a Ruby gem that enhances the standard Rails error page with more detailed and interactive debugging information. It provides a richer debugging experience by displaying source code snippets, allowing you to inspect variables, and even execute code directly within the error page. This makes it easier to understand the cause of errors and quickly identify solutions during development.

## Bin

# bin Directory

The `bin` directory in a Rails application contains executable scripts that are specific to your application. These scripts are typically used for tasks like starting the server, running tests, or performing other administrative operations. They provide a convenient way to interact with your Rails application from the command line.

## Byebug

# Byebug

Byebug is a powerful debugger for Ruby. It allows you to step through your code, set breakpoints, inspect variables, and evaluate expressions in real-time, helping you identify and fix errors in your Ruby applications. It's a gem that integrates directly into your Ruby environment, providing a command-line interface for debugging.

## Caching

# Caching

Caching is a technique used to store copies of frequently accessed data in a temporary storage location, like memory, to reduce the need to retrieve the data from its source, such as a database or external API, every time it's requested. This results in faster response times and reduced load on the original data source.

Visit the following resources to learn more:

- [@official@Caching with Rails: An Overview](https://guides.rubyonrails.org/caching_with_rails.html)
- [@article@An Introduction to HTTP Caching in Ruby On Rails](https://blog.appsignal.com/2024/08/14/an-introduction-to-http-caching-in-ruby-on-rails.html)
- [@article@Mastering Low Level Caching in Rails](https://www.honeybadger.io/blog/rails-low-level-caching/)
- [@article@Types of Caching in Rails](https://tadhao.medium.com/types-of-caching-in-rails-cba708aae679)
- [@video@Fragment and Collection Cache in Ruby on Rails 7](https://www.youtube.com/watch?v=t4bugdvKEag)
- [@video@Easy caching with Solid Cache | Rails 8 Unpacked](https://www.youtube.com/watch?v=mA6somzKYEg)

## Callbacks

# Callbacks

Callbacks are methods that get called at certain moments in the lifecycle of an Active Record object. These moments can include creation, updating, deletion, validation, or saving. By using callbacks, you can trigger logic before or after these actions, allowing you to perform tasks like data validation, auditing, or related object updates automatically

Visit the following resources to learn more:

- [@official@Active Record Callbacks](https://guides.rubyonrails.org/active_record_callbacks.html)
- [@article@Active Record Callbacks | The Odin Project](https://www.theodinproject.com/lessons/ruby-on-rails-active-record-callbacks)
- [@article@Rails ActiveRecord Callbacks — cheatsheet & best practices](https://medium.com/@jaysadiq/rails-activerecord-callbacks-cheatsheet-55fdb37f76ef)
- [@article@Ruby on Rails ActiveRecord Callbacks](https://dev.to/eapenzac/ruby-on-rails-activerecord-callbacks-597a)
- [@video@Understanding Active Record Callbacks](https://www.youtube.com/watch?v=1-31AlGv96Y)
- [@video@Callbacks](https://www.youtube.com/watch?v=GLBMfB8N1G8)

## Cancancan

# CanCanCan

CanCanCan is an authorization library for Ruby on Rails applications that restricts what resources a given user is allowed to access. It provides a simple and declarative way to define abilities, based on the user's role and the resource being accessed. This allows developers to easily manage permissions and ensure that users can only perform actions they are authorized to do.

## Cancancan

# CanCanCan

CanCanCan is an authorization library for Ruby on Rails applications that restricts what resources a given user is allowed to access. It provides a simple and flexible way to define abilities, which represent the permissions a user has on different resources, and then checks these abilities within your controllers and views to control access and display appropriate content. This gem helps in defining and managing user roles and permissions, ensuring that only authorized users can perform specific actions.

Visit the following resources to learn more:

- [@opensource@cancancan](https://github.com/CanCanCommunity/cancancan)
- [@article@Rails 7 Authorization with Cancancan Gem](https://medium.com/@learnwithalfred/rails-7-authorization-with-cancancan-gem-f3a29c01b3bd)
- [@article@Authorization Gems in Ruby: Pundit and CanCanCan](https://blog.appsignal.com/2023/03/22/authorization-gems-in-ruby-pundit-and-cancancan.html)
- [@video@Authorization on Rails (CanCanCan Demonstration)](https://www.youtube.com/watch?v=cTYu-OjUgDw)
- [@video@Ruby On Rails - Authorization Using CanCanCan](https://www.youtube.com/playlist?list=PL6HtmRWwDtYMuIDt4syZdGXWFPZrAWvm_)

## Capybara

# Capybara

Capybara is a Ruby gem that simplifies acceptance testing for web applications. It simulates how a user interacts with your application through a browser, allowing you to write tests that verify the behavior of your application from an end-user perspective. It provides a clean and easy-to-use API for interacting with elements on a web page, such as clicking links, filling in forms, and asserting the presence of specific content.

Visit the following resources to learn more:

- [@opensource@capybara](https://github.com/teamcapybara/capybara)
- [@article@Integration Testing Ruby on Rails with Minitest and Capybara](https://semaphore.io/community/tutorials/integration-testing-ruby-on-rails-with-minitest-and-capybara)
- [@article@A Rails testing “hello world” using RSpec and Capybara](https://www.codewithjason.com/rails-testing-hello-world-using-rspec-capybara/)
- [@video@End to end testing Rails with capybara](https://www.youtube.com/watch?v=ggnGOBe2A3o)
- [@video@System Tests With Capybara and Selenium | Ruby On Rails 7 Tutorial](https://www.youtube.com/watch?v=2TInLtG8dj4)

## Conditions

# Active Record Conditions

Active Record conditions are used to specify criteria for retrieving data from a database table. They allow you to filter records based on specific attributes and values, enabling you to retrieve only the data that meets your desired requirements. These conditions are typically expressed using SQL-like syntax or through a more Ruby-friendly syntax provided by Active Record.

Visit the following resources to learn more:

- [@official@Conditions](https://guides.rubyonrails.org/active_record_querying.html#conditions)
- [@official@Overriding Conditions](https://guides.rubyonrails.org/active_record_querying.html#overriding-conditions)

## Config

# Config Directory

The `config` directory in a Rails application houses configuration files that control various aspects of the application's behavior. These files define database connections, routing rules, environment-specific settings, and other application-wide configurations, allowing developers to customize the application without modifying the core code.

Visit the following resources to learn more:

- [@official@Configuring Rails Applications](https://guides.rubyonrails.org/configuring.html)
- [@article@Setting Up and Managing Databases in Ruby on Rails](https://bhartee-tech-ror.medium.com/setting-up-and-managing-databases-in-ruby-on-rails-72885f9f1164)
- [@article@The Rails database.yml File](https://dev.to/andreimaxim/the-rails-databaseyml-file-4dm9)

## Constraints

# Routing Constraints

Routing constraints allow you to restrict which routes are matched based on specific criteria. These criteria can include the request's subdomain, IP address, HTTP headers, or any other attribute of the request. By adding constraints, you can create more precise and targeted routes, ensuring that requests are handled by the correct controller action.

Visit the following resources to learn more:

- [@official@Constraints](https://guides.rubyonrails.org/routing.html#http-verb-constraints)
- [@official@Advanced Constrains](https://guides.rubyonrails.org/routing.html#advanced-constraints)
- [@article@How to Use Rails Routing Constraints: Two Use Cases with Code](https://8thlight.com/insights/how-to-use-rails-routing-constraints-2-use-cases-with-code)
- [@article@Rails advanced routing constraints](https://thoughtbot.com/blog/rails-advanced-routing-constraints)
- [@video@Advanced Rails Routing Constraints: Domain, Subdomain, Authentication, and more | Preview](https://www.youtube.com/watch?v=bauG5ibI9Xc)

## Controller Actions

# Controller Actions

Controller actions are methods within a Rails controller that handle specific requests from users or other parts of the application. Each action typically corresponds to a specific route and performs a task, such as displaying a form, creating a new record, updating an existing record, or deleting a record. These actions interact with models to retrieve or manipulate data and then render a view to display the results to the user.

Visit the following resources to learn more:

- [@official@Action Controller Overview](https://guides.rubyonrails.org/action_controller_overview.html)
- [@article@Introduction to Controllers in Rails](https://codesignal.com/learn/courses/ruby-on-rails-basics/lessons/controllers-in-rails)

## Controller Callbacks Filters

# Controller Callbacks

Controller callbacks, often referred to as filters, are methods that are executed at specific points in the lifecycle of a controller action. They allow you to run code before, after, or around a controller action, providing a way to encapsulate common logic, such as authentication, authorization, or data preparation, and keep your controller actions clean and focused.

Visit the following resources to learn more:

- [@official@Controller Callbacks](https://guides.rubyonrails.org/action_controller_overview.html#controller-callbacks)
- [@article@A Simple Guide to before_action Callbacks in Ruby on Rails](https://medium.com/@havanurkara55/a-simple-guide-to-before-action-callbacks-in-ruby-on-rails-fb068fb533d7)
- [@article@Rails "around_action" : a less used callback](https://dev.to/moltenhead/rails-aroundaction-a-less-used-callback-10cf)
- [@video@ActionController callbacks in Rails](https://www.youtube.com/watch?v=SnRq1_VXVVc)

## Controllers

# Controllers

Controllers are the intermediary between the user, the view, and the model. They receive requests from the user (often through routes), process the request by interacting with the model to retrieve or manipulate data, and then determine which view to render to display the results to the user. Essentially, they manage the application's workflow and logic.

Visit the following resources to learn more:

- [@official@Action Controller Overview](https://guides.rubyonrails.org/action_controller_overview.html)
- [@article@Controllers](https://www.theodinproject.com/lessons/ruby-on-rails-controllers)
- [@article@Ruby on Rails Controller Patterns and Anti-patterns](https://blog.appsignal.com/2021/04/14/ruby-on-rails-controller-patterns-and-anti-patterns.html)
- [@article@How I keep my Rails controllers organized](https://www.codewithjason.com/keep-rails-controllers-organized/)
- [@video@Controllers - Ruby on Rails - The Odin Project](https://www.youtube.com/watch?v=2isr-7DdoYE)
- [@video@Fun With The Controller - Ruby On Rails Friend List App #11](https://www.youtube.com/watch?v=SErZhMh2o30)

## Cookies

# Cookies in Rails Controllers

Cookies are small pieces of data that a server sends to a user's web browser. The browser may store it and send it back with later requests to the same server. Rails controllers provide a convenient way to set, read, and delete cookies, allowing you to maintain state between requests, such as remembering user preferences or tracking session information.

Visit the following resources to learn more:

- [@official@Cookies](https://guides.rubyonrails.org/action_controller_overview.html)
- [@article@The Complete Guide to Working With Cookies in Rails](https://www.writesoftwarewell.com/how-http-cookies-work-rails/)
- [@article@Mastering Sessions and Cookies in Rails: A Comprehensive Guide](https://medium.com/@carriekarft/mastering-sessions-and-cookies-in-rails-a-comprehensive-guide-0446422d7b22)
- [@article@Cookies & Sessions in Rails](https://dev.to/matthewkohn/cookies-sessions-in-rails-54b8)
- [@video@Rails 6 for Beginners Part 15: Login with Session Cookies](https://www.youtube.com/watch?v=IzbQAj_tcfI)
- [@video@Rails Cookies and Session](https://www.youtube.com/watch?v=iOR-9fMMmLM)

## Create An App

# Creating a New Rails Application

Creating a new Rails application is the initial step in starting any Rails project. It involves using the `rails new` command, which sets up the basic directory structure, configuration files, and dependencies needed for a functional Rails application. This process bootstraps your project with a default set of tools and conventions, allowing you to quickly begin building your web application.

## Creating Controllers

# Creating Controllers

Controllers are the logical center of your application, responsible for receiving specific requests from the user, interacting with the model to retrieve or save data, and then rendering a view to present that data back to the user. Creating a controller involves defining a Ruby class that inherits from `ApplicationController` and defining methods (called actions) within that class to handle specific routes and user interactions. These actions orchestrate the application's response to user input.

Visit the following resources to learn more:

- [@official@Creating a Controller](https://guides.rubyonrails.org/action_controller_overview.html#creating-a-controller)
- [@article@Introduction to Controllers in Rails](https://codesignal.com/learn/courses/ruby-on-rails-basics/lessons/controllers-in-rails)
- [@video@Controllers - Ruby on Rails - The Odin Project](https://www.youtube.com/watch?v=2isr-7DdoYE)

## Creating Models

# Creating Models

Models in Ruby on Rails represent the data and business logic of your application. They are Ruby classes that inherit from `ApplicationRecord` and typically correspond to tables in your database. Creating a model involves defining its attributes (columns in the database table) and any associated validations, callbacks, and relationships with other models. This process allows you to interact with your database in an object-oriented way, making data management more intuitive and efficient.

Visit the following resources to learn more:

- [@official@Creating Active Record Models](https://guides.rubyonrails.org/active_record_basics.html#creating-active-record-models)
- [@article@Rails Models](https://www.theodinproject.com/lessons/ruby-on-rails-active-record-basics#rails-models)
- [@article@Ruby on Rails - Models](https://www.tutorialspoint.com/ruby-on-rails/rails-models.htm)
- [@video@Ep 4. Active Record explained | Rails New Tutorial with Typecraft](https://www.youtube.com/watch?v=n0TPEsKE9v0)

## Csrf Protection

# CSRF Protection

Cross-Site Request Forgery (CSRF) is a web security vulnerability that allows an attacker to trick a user's browser into executing unwanted actions on a trusted site when the user is authenticated. CSRF protection involves adding a unique, unpredictable token to each form submitted by the user. This token is then verified on the server-side to ensure that the request originated from the legitimate application and not a malicious source.

## Customizing Routes

# Customizing Routes

Customizing routes allows developers to define specific URL patterns and map them to particular controller actions. This provides flexibility in designing user-friendly and SEO-optimized URLs, deviating from the default Rails conventions. By modifying the `routes.rb` file, you can create custom routes that cater to the unique needs of your application, including specifying HTTP methods, defining route parameters, and using regular expressions for pattern matching.

Visit the following resources to learn more:

- [@official@Customizing Resourceful Routes](https://guides.rubyonrails.org/routing.html#customizing-resourceful-routes)
- [@article@How to Write Custom Routes in Rails](https://levelup.gitconnected.com/how-to-write-custom-routes-in-rails-872df2ca4d39)
- [@article@Custom routes in rails](https://medium.com/@leviyitzchokdeutsch/custom-routes-in-rails-f790e5940e22)

## Data Types

# Data Types in Rails Models

Data types define the kind of information a database column can store. When creating Rails models, you specify data types for each attribute, which then translates into the corresponding column type in your database table. These types include integers, strings, booleans, dates, and more, ensuring data integrity and efficient storage.

Visit the following resources to learn more:

- [@official@ActiveRecord::Type](https://api.rubyonrails.org/classes/ActiveRecord/Type.html)
- [@article@Rails ActiveRecord Data Types](https://dev.to/asyraf/rails-activerecord-data-types-32ip)
- [@article@List of Rails data types for ActiveRecord migrations](https://www.jdeen.com/blog/list-of-rails-data-types-for-activerecord-migrations)

## Databases

# Database

Databases are structured collections of data, organized for efficient storage, retrieval, and management. Active Record is Rails' ORM (Object-Relational Mapping) layer, providing an interface between your Ruby code and the database. It allows you to interact with database tables as if they were Ruby objects, simplifying database operations like creating, reading, updating, and deleting records.

Visit the following resources to learn more:

- [@official@Configuring a Database](https://guides.rubyonrails.org/configuring.html#configuring-a-database)
- [@official@Multiple Databases with Active Record](https://guides.rubyonrails.org/active_record_multiple_databases.html)
- [@article@Setting Up and Managing Databases in Ruby on Rails](https://bhartee-tech-ror.medium.com/setting-up-and-managing-databases-in-ruby-on-rails-72885f9f1164)
- [@article@The Rails database.yml File](https://dev.to/andreimaxim/the-rails-databaseyml-file-4dm9)
- [@video@How to Configure Multiple Databases with Rails](https://www.youtube.com/watch?v=aOsffm22T8I)

## Db

# db

The `db` directory in a Rails application houses everything related to your database. It contains files for database schema definition, migrations, and seed data. This directory is essential for managing and evolving your application's data structure over time.

## Debug

# debug

The `debug` helper in Ruby on Rails provides a way to display the contents of a variable or object directly within your views. It's primarily used for debugging purposes, allowing you to quickly inspect data structures and identify issues in your code during development. When used, it outputs the object's information in a readable format within `<pre>` tags on the rendered HTML page, making it easy to examine its properties and values.

Visit the following resources to learn more:

- [@official@debug](https://guides.rubyonrails.org/debugging_rails_applications.html#debug)

## Debugging

# Debugging

Debugging is the process of identifying and removing errors (bugs) from software. It involves systematically finding the source of a problem, understanding why it's happening, and then implementing a solution to fix it. Effective debugging relies on using tools and techniques to inspect code, track down unexpected behavior, and verify that the fix resolves the issue without introducing new problems.

Visit the following resources to learn more:

- [@official@Debugging Rails Applications](https://guides.rubyonrails.org/debugging_rails_applications.html#view-helpers-for-debugging)

## Deployment

# Deployment

Deployment is the process of making your Ruby on Rails application accessible to users on a live server. It involves configuring the server environment, transferring your application code, setting up databases, and ensuring the application runs smoothly and reliably in a production setting. This includes handling aspects like web server configuration, application server setup, database connections, and ongoing maintenance.

Visit the following resources to learn more:

- [@official@Deploying to Production](https://guides.rubyonrails.org/getting_started.html)
- [@video@Deploying with Kamal 2.0 | Rails 8 Unpacked](https://www.youhttps://www.youtube.com/watch?v=sPUk9-1WVXItube.com/watch?v=sPUk9-1WVXI)

## Devise

# Devise

Devise is a flexible authentication solution for Rails applications. It provides a complete MVC solution based on Warden that handles user registration, login, password recovery, and other common authentication tasks. It uses a modular approach, allowing developers to choose and configure the specific features they need for their application.

Visit the following resources to learn more:

- [@opensource@devise](https://github.com/heartcombo/devise)
- [@article@An Introduction to Devise for Ruby on Rails](https://blog.appsignal.com/2023/07/12/an-introduction-to-devise-for-ruby-on-rails.html)
- [@article@How To Set Up User Authentication with Devise in a Rails 7 Application](https://www.digitalocean.com/community/tutorials/how-to-set-up-user-authentication-with-devise-in-a-rails-7-application)
- [@video@Build a Blog with Rails Part 10: Authentication with Devise](https://www.youtube.com/watch?v=dTpyInyvQ2Y)
- [@video@This New Devise API Gem Makes User Auth So Simple! | Ruby On Rails 7 Tutorial](https://www.youtube.com/watch?v=sLcLwVCBU0c)

## Dynamic Finders

# Dynamic Finders

Dynamic finders provide a convenient way to query your database based on specific attributes of your model. They allow you to create methods on the fly that search for records based on the values of those attributes, eliminating the need to write custom query methods for simple attribute-based searches. This feature simplifies data retrieval and makes your code more readable.

## Engines

# Engines

Engines are like mini-applications that can be plugged into a larger Rails application. They provide a way to encapsulate specific functionality, such as a blog, a forum, or an e-commerce platform, into a reusable component. This allows developers to create modular and maintainable applications by isolating concerns and promoting code reuse across different projects.

## Erb Templates

# ERB Templates

ERB (Embedded Ruby) templates are a core component of Rails views, allowing you to embed Ruby code directly within your HTML markup. This enables dynamic content generation, where data from your Rails application can be seamlessly integrated into the presentation layer. ERB templates use special tags to denote Ruby code, which is then executed when the view is rendered, producing the final HTML output sent to the user's browser.

Visit the following resources to learn more:

- [@official@ERB](https://guides.rubyonrails.org/action_view_overview.html#erb)
- [@official@Layouts and Rendering in Rails](https://guides.rubyonrails.org/layouts_and_rendering.html)
- [@article@Clean Code in ERB Templates: Ruby on Rails Basics](https://medium.com/nyc-ruby-on-rails/clean-code-in-erb-templates-ruby-on-rails-basics-374ad48dd95e)
- [@video@Rails Application Templates](https://www.youtube.com/watch?v=ucskVEiN8J8)

## Factory Bot

# Factory Bot

Factory Bot is a library for creating Ruby objects for testing purposes. It provides a simple and clean syntax for defining factories, which are blueprints for creating instances of your models with pre-defined attributes. This helps to avoid repetitive setup code in your tests and ensures consistent test data.

Visit the following resources to learn more:

- [@opensource@factory_bot_rails](https://github.com/thoughtbot/factory_bot_rails)
- [@article@FactoryBot for Rails testing](https://www.honeybadger.io/blog/factorybot-for-rails-testing-md/)
- [@article@How I set up Factory Bot on a fresh Rails project](http://codewithjason.com/set-factory-bot-fresh-rails-project/)
- [@article@My Introduction To Factory Bot](https://medium.com/@mariacristina.simoes/my-introduction-to-factory-bot-88949467a7e9)
- [@video@Install Factory Bot with Ruby on Rails](https://www.youtube.com/watch?v=vQQKIyAHPI4)
- [@video@Factory Bot Testing with Active Storage and Devise | Ruby on Rails 7 Tutorial](https://www.youtube.com/watch?v=7JdyQEcZ7F8)
- [@video@Factory Bot Tutorial for Beginners](https://www.youtube.com/watch?v=ef82mR9Mm8Q)

## Form Elements

# Form Elements

Form elements are the individual components within an HTML form that allow users to input data. These elements include text fields, text areas, checkboxes, radio buttons, select boxes, and buttons, each serving a specific purpose in collecting different types of user information. They are essential for creating interactive web applications where users can submit data to the server.

Visit the following resources to learn more:

- [@official@Helpers for Generating Form Elements](https://guides.rubyonrails.org/form_helpers.html#helpers-for-generating-form-elements)

## Form Validation

# Form Validation

Form validation is the process of ensuring that the data submitted through a form meets specific requirements before it's saved to the database. This helps prevent errors, maintain data integrity, and provide a better user experience. Rails provides built-in methods and helpers to easily define and enforce these validation rules directly within your models, such as checking for presence, format, uniqueness, or custom criteria.

Visit the following resources to learn more:

- [@official@Active Record Validations](https://guides.rubyonrails.org/active_record_validations.html#performing-custom-validations)
- [@article@Keeping it Clean — Data Validation with Ruby on Rails](https://medium.com/@jennyjean8675309/keeping-it-clean-data-validation-with-ruby-on-rails-a0c6190f1b8e)
- [@video@Rails Custom Validations](https://www.youtube.com/watch?v=nPS-dalL_hQ)
- [@video@Nested Attributes & Validation In Ruby On Rails 7](https://www.youtube.com/watch?v=Fpu0rc3stq4)
- [@video@Rails 6 for Beginners Part 12: Validations](https://www.youtube.com/watch?v=l-Jv5vMjB70&t=209s)

## Form For

# form_for

`form_for` is a helper method in Ruby on Rails that simplifies the creation of HTML forms. It automatically generates the necessary HTML tags and attributes for creating forms that are bound to a specific model object. This helper streamlines the process of building forms for creating, updating, and managing data within your Rails application.

Visit the following resources to learn more:

- [@official@Action View Form Helpers](https://guides.rubyonrails.org/form_helpers.html)
- [@official@form_for](https://api.rubyonrails.org/v8.1.2/classes/ActionView/Helpers/FormHelper.html#method-i-form_for)
- [@article@I Have a Form_For That! (Rails Forms)](https://medium.com/@thorntonbrenden/i-have-a-form-for-that-rails-forms-42345b69c31)
- [@article@Rails form_for Helpers Under the Hood](https://smitham50.medium.com/rails-form-for-helpers-under-the-hood-fdf98c7bd3d1)
- [@video@Rails 5.2 - Blog with Comments and Users Nested Resources, form_for and much more](https://www.youtube.com/watch?v=CBn_zu-2mtk)
- [@video@Understanding Rails Forms](https://www.youtube.com/watch?v=28wOvW5x7HY)

## Form With

# form_with

`form_with` is a helper method used to create HTML forms. It simplifies the process of generating the necessary HTML tags for form elements, handling attributes like the form's action URL, HTTP method (GET, POST, PUT, PATCH, DELETE), and CSRF protection. It's the recommended way to build forms in Rails 5.1 and later, offering a more streamlined and flexible approach compared to older form helpers.

Visit the following resources to learn more:

- [@official@Action View Form Helpers](https://guides.rubyonrails.org/form_helpers.html)
- [@official@form_with](https://api.rubyonrails.org/v8.1.2/classes/ActionView/Helpers/FormHelper.html#method-i-form_with)
- [@article@Form helpers: form_with](https://www.theodinproject.com/lessons/ruby-on-rails-form-basics#form-helpers-formwith)
- [@video@Improving form_with Errors in Rails | Preview](https://www.youtube.com/watch?v=mSSO_lT9MeA)
- [@video@Ruby on Rails Forms With Hotwire](https://www.youtube.com/watch?v=-n7IbUFKjoM)
- [@video@Understanding Rails Forms](https://www.youtube.com/watch?v=28wOvW5x7HY)

## Gemfile

# Gemfile

The Gemfile is a file in the root directory of a Ruby on Rails application that specifies the gem dependencies required for the project. It uses Ruby's syntax to list the gems and their versions, allowing Bundler to manage and install the correct versions of each gem. This ensures that the application has all the necessary libraries to run properly and consistently across different environments.

## Helpers

# Helpers

Helpers in Rails are methods that you can use in your views to encapsulate complex logic, format data, or generate HTML. They promote code reusability and keep your views clean and readable by moving presentation-related code out of the templates. Helpers can be defined in application-wide helpers or controller-specific helpers.

Visit the following resources to learn more:

- [@official@Action View Helpers](https://guides.rubyonrails.org/action_view_helpers.html)
- [@article@A Guide to Rails View Helpers](https://blog.appsignal.com/2023/02/01/a-guide-to-rails-view-helpers.html)
- [@article@How to Use Rails Helpers (Complete Guide)](https://www.rubyguides.com/2020/01/rails-helpers/)
- [@video@Rails helpers: How to use them right](https://www.youtube.com/watch?v=n0UhaSI54As)
- [@video@How to Use Rails Helper Methods](https://www.youtube.com/watch?v=jASswaHkCbk)

## Hotwire

# Hotwire

Hotwire is an alternative approach to building modern web applications by sending HTML over the wire, instead of complex JSON APIs. It allows you to build rich, dynamic user interfaces without writing large amounts of JavaScript. By leveraging server-rendered HTML and a lightweight JavaScript framework, Hotwire simplifies the development process and improves performance.

Visit the following resources to learn more:

- [@official@Hotwire](https://hotwired.dev/)
- [@article@Turbo Rails Tutorial](https://www.hotrails.dev/turbo-rails)
- [@article@From Zero to Hotwire — Rails 8](https://medium.com/jungletronics/from-zero-to-hotwire-rails-8-e6cd16216165)
- [@video@Hotwire for Rails](https://www.youtube.com/playlist?list=PLm8ctt9NhMNWy8fC-7g9OC1IJPkYQ_pI7)
- [@video@Introduction to Hotwire in Ruby on Rails](https://www.youtube.com/watch?v=m_4myBwU2cU)
- [@video@How to use Hotwire in Rails](https://www.youtube.com/watch?v=Qp6sxgjA-xY)

## How The Web Works

# How the Web Works

The web operates through a client-server model where a client (like a web browser) sends a request to a server, and the server processes that request and sends back a response. This interaction typically involves HTTP (Hypertext Transfer Protocol) for communication, URLs (Uniform Resource Locators) to identify resources, and HTML (Hypertext Markup Language) to structure the content displayed in the browser. The server hosts the website's files and logic, while the client interprets and renders the received information for the user.

## Inspecting Routes

# Inspecting Routes

Rails comes with functionalities that allow developers to view all defined routes, their corresponding HTTP methods (GET, POST, PUT, DELETE, etc.), the controller and action they map to, and any route parameters. This is crucial for understanding how URLs are handled within the application and for debugging routing issues. Rails provides tools to easily list and analyze these routes, offering insights into the application's URL structure.

Visit the following resources to learn more:

- [@official@Inspecting Routes](https://guides.rubyonrails.org/routing.html#inspecting-routes)
- [@article@How to Inspect Rails Routes from the Terminal](https://dpericich.medium.com/how-to-inspect-rails-routes-from-the-terminal-860b1aab1df4)

## Introduction

# Introduction to Ruby on Rails

Ruby on Rails, often shortened to Rails, is a server-side web application framework written in the Ruby programming language. It provides a structure for databases, web services, and web pages, emphasizing the use of convention over configuration (CoC) and the don't repeat yourself (DRY) principles. Rails aims to make web application development easier by providing tools and structures that developers can use to quickly build robust and maintainable web applications.

## Joins

# Joins in Active Record

Joins in Active Record allow you to combine data from multiple database tables based on related columns. This is essential for retrieving information that spans across different tables, such as fetching a user's posts or a product's categories. By specifying the relationships between your models, Active Record simplifies the process of writing complex SQL queries, enabling you to efficiently retrieve and manipulate related data.

Visit the following resources to learn more:

- [@official@Joining Tables](https://guides.rubyonrails.org/active_record_querying.html#joining-tables)
- [@article@Getting Really Good at Rails :joins](https://medium.com/swlh/getting-really-good-at-rails-joins-93fd5b33fa8e)
- [@article@Joins](https://medium.com/swlh/getting-really-good-at-rails-joins-93fd5b33fa8e)
- [@article@Understanding multiple joins in ActiveRecord](https://dev.to/anakbns/multiple-joins-with-activerecord-33j5)

## Kamal

# Kamal

Kamal is a deployment tool created by 37signals (the creators of Ruby on Rails) designed to simplify the process of deploying web applications to one or more servers. It focuses on using Docker containers and modern deployment strategies like zero-downtime deployments, making it easier to manage and scale your Rails applications in production environments. It aims to provide a streamlined alternative to more complex deployment solutions.

Visit the following resources to learn more:

- [@official@Kamal](https://kamal-deploy.org/)
- [@opensource@kamal](https://github.com/basecamp/kamal)
- [@article@Deploying a Rails 8 app with Kamal](https://community.hetzner.com/tutorials/deploy-rails-8-app-on-hetzner-with-kamal)
- [@video@https://www.youtube.com/watch?v=sPUk9-1WVXI](https://www.youhttps//www.youtube.com/watch?v=sPUk9-1WVXItube.com/watch?v=sPUk9-1WVXI)
- [@video@How to Deploy a Rails App With Kamal](https://www.youtube.com/watch?v=9nRY0p2br28)
- [@video@Absolute Beginners Guide to Deploying Rails 8 to Production (Kamal Tutorial)](https://www.youtube.com/watch?v=tGi3YGGhIGg)

## Kaminari

# Kaminari

Kaminari is a Ruby on Rails gem that simplifies the process of adding pagination to your application. It provides an easy-to-use interface for displaying large datasets in manageable chunks, improving performance and user experience by loading only the necessary data for each page. Kaminari integrates seamlessly with ActiveRecord and other ORMs, making it a straightforward solution for paginating data in your Rails applications.

Visit the following resources to learn more:

- [@opensource@kaminari](https://github.com/kaminari/kaminari)
- [@article@Ruby On Rails Pagination With Kaminari](https://www.dennisokeeffe.com/blog/2022-03-02-ruby-on-rails-pagination-with-kaminari)
- [@article@Implementing Pagination in Rails with Kaminari](https://devcamp.com/trails/2/campsites/37/guides/implementing-pagination-rails-kaminari)
- [@video@The Kaminari Gem in Ruby on Rails 7](https://www.youtube.com/watch?v=sHbI0jY8RUs)

## Layouts  Yield

# Layouts and Yield in Rails Views

Layouts provide a consistent structure for your application's views. They are templates that define the overall look and feel of a page, including elements like headers, footers, and navigation. The `yield` keyword acts as a placeholder within the layout, indicating where the content from individual views should be inserted. This allows you to reuse common elements across multiple pages while still displaying unique content for each.

Visit the following resources to learn more:

- [@article@Structuring Layouts](https://guides.rubyonrails.org/layouts_and_rendering.html#structuring-layouts)
- [@article@Ruby on Rails - Layouts](https://www.tutorialspoint.com/ruby-on-rails/rails-layouts.htm)
- [@article@How Layouts Work in Rails](https://railsdesigner.com/rails-layouts/)
- [@video@How to Use Rails Layouts & Display The Current Action Name](https://www.youtube.com/watch?v=KKg63bQocmw)

## Log Levels

# Log Levels

Log levels in Rails are categories that indicate the severity of a log message. They help you filter and prioritize information when debugging or monitoring your application. Common log levels, in increasing order of severity, are: `debug`, `info`, `warn`, `error`, and `fatal`. Each level allows you to control the amount of detail recorded, from verbose debugging information to critical errors that require immediate attention.

## Logging

# Logging

Logging involves recording events that occur within an application, such as user actions, errors, and system information. This recorded data is typically stored in log files, providing a valuable resource for monitoring application behavior, diagnosing issues, and understanding performance. Rails provides a built-in logging framework that simplifies the process of generating and managing these logs.

Visit the following resources to learn more:

- [@article@How to Start Logging With Ruby on Rails](https://betterstack.com/community/guides/logging/how-to-start-logging-with-ruby-on-rails/)
- [@article@Making the Most of Your Logs in Rails](https://blog.appsignal.com/2023/03/01/making-the-most-of-your-logs-in-rails.html)
- [@article@The Rails Logging Setup That Saved Me From Debugging Hell](https://bhavyansh001.medium.com/the-rails-logging-setup-that-saved-me-from-debugging-hell-97904592eceb)
- [@video@Debugging And Logging | Intro To Ruby On Rails 7 Part 24](https://www.youtube.com/watch?v=9rDK2rbm6DI)
- [@video@Logging Mastery: From Rails Default to Kibana 📈](https://www.youtube.com/watch?v=CoHMwJsLiLU)

## Mailbox  Mailer

# Mailbox and Mailer

The Rails Mailbox and Mailer provide a structured way to handle incoming and outgoing emails. Mailers are used to compose and send emails from your application, defining email content, recipients, and headers. Mailboxes, introduced more recently, route incoming emails to specific controllers or models within your application, allowing you to process and respond to emails programmatically.

Visit the following resources to learn more:

- [@official@Action Mailbox Basics](https://guides.rubyonrails.org/action_mailbox_basics.html)
- [@official@Action Mailer Basics](https://guides.rubyonrails.org/action_mailer_basics.html)
- [@article@In Depth Look At Action Mailbox](https://www.codynorman.com/ruby/action_mailbox/)
- [@article@Rails Mailer Tutorial](https://medium.com/@ericschwartz7/rails-mailer-tutorial-82700f6737d9)
- [@article@Writing better Action Mailers: Revisiting a core Rails concept](https://boringrails.com/articles/writing-better-action-mailers/)
- [@video@Receive and process inbound email with Ruby on Rails](https://www.youtube.com/watch?v=jOfAV2QWNOw&t=87s)
- [@video@Action Mailer for Beginners | Ruby on Rails 7](https://www.youtube.com/watch?v=-8Rs1DcMZ9I)
- [@video@Realtime Rails with Hotwire & ActionMailbox | Part 1](https://www.youtube.com/watch?v=WSuFaY7-q3g&t=66s)

## Mariadb

# MariaDB Support in Rails

MariaDB is an open-source relational database management system (RDBMS) that is a popular fork of MySQL. Rails applications can connect to and interact with MariaDB databases using the `mysql2` adapter. This allows developers to leverage MariaDB's features, such as enhanced performance and storage engines, within their Rails applications for data persistence and management.

Visit the following resources to learn more:

- [@official@Configuring a MySQL or MariaDB Database](https://guides.rubyonrails.org/configuring.html#configuring-a-mysql-or-mariadb-database)
- [@official@Connector/Ruby Guide](https://mariadb.com/docs/connectors/connectors-quickstart-guides/connector-ruby-guide)
- [@article@Howto Set Up MariaDB For Rails Development](https://myrtana.sk/articles/howto-set-up-mariadb-for-rails-development)

## Migrations

# Migrations

Migrations are a way to evolve your database schema over time in a consistent and manageable way. They are Ruby files that define changes to your database structure, such as creating tables, adding columns, or modifying indexes. These files allow you to track and apply changes to your database schema, making it easy to collaborate with other developers and deploy your application to different environments.

Visit the following resources to learn more:

- [@official@Active Record Migrations](https://guides.rubyonrails.org/active_record_migrations.html)
- [@article@Migrations](https://www.theodinproject.com/lessons/ruby-on-rails-migrations)
- [@article@How to create Active Record migrations in Ruby on Rails](https://learnetto.com/tutorials/how-to-create-active-record-migrations-in-ruby-on-rails)
- [@article@A quick guide on database migrations in Ruby on Rails](https://dev.to/dumebii/quick-guide-to-migrations-in-ruby-on-rails-for-beginners-4gmb)
- [@video@How to Use Migrations in Rails (Step-by-Step)](https://www.youtube.com/watch?v=1DaO6F8-Qdc)

## Minitest

# Minitest

Minitest is a complete testing suite for Ruby, providing support for test-driven development (TDD), behavior-driven development (BDD), mocking, and benchmarking. It's a lightweight and fast testing framework that comes bundled with Ruby, making it readily available for use in Rails applications. Minitest allows developers to write various types of tests, including unit tests, integration tests, and system tests, to ensure the quality and reliability of their code.

Visit the following resources to learn more:

- [@opensource@minirtest](https://github.com/minitest/minitest)
- [@article@Getting Started With Testing In Rails (Using Minitest and RSpec)](https://medium.com/@ethanryan/getting-started-with-testing-in-rails-using-minitest-and-rspec-113fe1f866a)
- [@article@Minitest vs. RSpec in Rails](https://www.honeybadger.io/blog/minitest-rspec-rails/)
- [@article@Getting Started With System Tests in Rails With Minitest](https://blog.appsignal.com/2020/02/12/getting-started-with-system-tests-in-ruby-with-minitest.html)
- [@article@Testing Rails with MiniTest](https://medium.com/@mario_chavez/testing-rails-with-minitest-7b4f99d4fcb8)

## Model Methods

# Model Methods

Model methods in Ruby on Rails are custom functions defined within a model class that encapsulate specific business logic related to that model. These methods allow you to perform operations on model instances or the model class itself, such as data validation, calculations, or interactions with other models, promoting code reusability and maintainability within your Rails application.

Visit the following resources to learn more:

- [@official@CRUD: Reading and Writing Data](https://guides.rubyonrails.org/active_record_basics.html#validations)
- [@article@💎 Ruby on Rails Cheat Sheet](https://pagertree.com/blog/ruby-on-rails-cheat-sheet#migration-data-types)

## Model Relationships

# Model Relationships

Model relationships in Rails define how different models in your application are connected to each other. These relationships allow you to easily access related data and maintain data integrity. Common types of relationships include one-to-one, one-to-many, and many-to-many, each representing a different way that data entities can be associated.

Visit the following resources to learn more:

- [@official@Active Record Associations](https://guides.rubyonrails.org/association_basics.html)
- [@article@Active Record Associations](https://www.theodinproject.com/lessons/ruby-on-rails-active-record-associations)
- [@article@Active Record Associations For Dummies](https://jontzavala.medium.com/active-record-associations-for-dummies-82af58050da4)
- [@article@Ruby on Rails - Active Record Associations](https://www.tutorialspoint.com/ruby-on-rails/rails-active-record-associations.htm)
- [@video@Learn Active Record associations with Starwars](https://www.youtube.com/watch?v=E2jk4h1gQ2I)
- [@video@Understanding Active Record Associations](https://www.youtube.com/watch?v=5mhuNSkV_vQ)

## Models

# Models

Models are Ruby classes that represent data and business logic. They interact with the database to perform CRUD (Create, Read, Update, Delete) operations on the data. Models provide a structured way to manage data, enforce validations, and define relationships between different data entities within an application. They are a core component of the Model-View-Controller (MVC) architectural pattern.

Visit the following resources to learn more:

- [@official@Active Record Basics](https://guides.rubyonrails.org/active_record_basics.html#creating-active-record-models)
- [@article@Rails models](https://www.theodinproject.com/lessons/ruby-on-rails-active-record-basics#rails-models)
- [@article@Ruby on Rails - Models](https://www.tutorialspoint.com/ruby-on-rails/rails-models.htm)
- [@article@The Rails Model Introduction I Wish I Had](https://www.maxwellantonucci.com/posts/2020/04/07/rails-model-intro-wish-i-had/)
- [@article@Rails models cheatsheet](https://devhints.io/rails-models)
- [@video@How to Use Active Record: An Introduction For Beginner Rails Developers](https://www.youtube.com/watch?v=-zQdVV7D4w8)

## Mvc Architecture

# MVC Architecture

MVC, or Model-View-Controller, is a software design pattern commonly used for developing user interfaces that divides an application into three interconnected parts. The Model manages the application's data and logic, the View displays the data to the user, and the Controller handles user input and updates the Model and View accordingly. This separation of concerns makes applications easier to develop, test, and maintain.

## Mysql

# MySQL in Rails

MySQL is a popular open-source relational database management system (RDBMS). In a Ruby on Rails application, MySQL serves as a persistent data store for your application's information, such as user accounts, product details, and blog posts. Rails leverages Active Record, an Object-Relational Mapping (ORM) framework, to interact with MySQL databases, allowing developers to work with data using Ruby objects instead of writing raw SQL queries.

Visit the following resources to learn more:

- [@official@Configuring a MySQL or MariaDB Database](https://guides.rubyonrails.org/configuring.html#configuring-a-mysql-or-mariadb-database)
- [@article@Ruby on Rails with MySQL](https://medium.com/@chandan-sharma/ruby-on-rails-create-mysql-database-and-add-table-5e62ac0e823c)
- [@article@How to use MySQL with your Ruby on Rails application](https://www.ionos.com/digitalguide/server/know-how/use-mysql-with-ruby-on-rails/)

## Named Routes

# Named Routes

Named routes provide a convenient way to refer to specific routes within your application's code. Instead of hardcoding URLs, you can use a symbolic name that represents the route, making your code more readable and maintainable. These names are automatically generated based on your `routes.rb` file and can be used in views, controllers, and models to generate URLs and paths.

Visit the following resources to learn more:

- [@official@Naming Routes](https://guides.rubyonrails.org/routing.html)
- [@article@Understanding Named Routes in Rails](https://www.writesoftwarewell.com/understanding-named-routes-in-rails/)

## Nested Forms

# Nested Forms

Nested forms allow you to manage associated models directly within a parent form. This means you can create, update, and delete records of related models on the same page as the parent model, providing a more streamlined user experience. For example, you might create a new blog post and its associated comments all at once.

Visit the following resources to learn more:

- [@official@Building Complex Forms](https://guides.rubyonrails.org/form_helpers.html#building-complex-forms)
- [@article@Rails — Nested Forms and Nested Resources](https://david-rafe.medium.com/rails-nested-forms-and-nested-resources-cb9f21bb1a1a)
- [@article@Nested Forms in Rails - FastRuby.io](https://www.fastruby.io/blog/learning/rails/nested-forms.html)
- [@article@Dynamic Nested Forms with Rails and Stimulus](https://jonathanyeong.com/writing/rails-stimulus-dynamic-nested-form/)
- [@video@Rails - Nested Forms in Rails | [Tutorial]](https://www.youtube.com/watch?v=niLRlaL-ss0)
- [@video@Stimulus Nested Forms | Ruby on Rails 7 Tutorial](https://www.youtube.com/watch?v=7JNRZLTRDCc)

## Nested Routes

# Nested Routes

Nested routes allow you to define hierarchical relationships between resources in your application's URLs. This means you can represent parent-child relationships, such as comments belonging to a specific post, directly in the URL structure. This approach helps to create more organized and intuitive URLs, reflecting the data's relationships and improving the user experience.

## Non Restful Routes

# Non-RESTful Routes

Non-RESTful routes are custom routes that deviate from the standard RESTful conventions (like `index`, `show`, `create`, `update`, `destroy`). They are used when an action doesn't naturally map to a typical CRUD operation or when you need a more descriptive or specific URL for a particular function in your application. These routes allow you to define custom paths and HTTP verbs to connect to specific controller actions.

## Omniauth

# OmniAuth

OmniAuth is a flexible authentication system that allows users to sign in to your application using third-party providers like Google, Facebook, Twitter, and more. It provides a standardized way to handle the authentication process, abstracting away the complexities of dealing with different authentication protocols and APIs. This simplifies the integration of social login and other external authentication methods into your Ruby on Rails application.

## Ordering

# Ordering

Ordering in Active Record allows you to specify the sequence in which records are retrieved from the database. This is achieved by using the `order` method, which accepts either a string representing the SQL order clause or a hash/symbol representing the attribute(s) to order by and their direction (ascending or descending). Ordering ensures that data is presented in a predictable and meaningful way, enhancing the user experience and facilitating data analysis.

Visit the following resources to learn more:

- [@article@Ordering](https://guides.rubyonrails.org/active_record_querying.html#ordering)
- [@article@Rails Quick Tips - ActiveRecord Ordering](https://hashrocket.com/blog/posts/rails-quick-tips-activerecord-ordering)
- [@article@Rails 7 adds ActiveRecord::QueryMethods#in_order_of to return query results in a particular sequence](https://blog.saeloun.com/2021/10/05/rails-7-activerecord-adds-in-order-of-method/)

## Pagination

# Pagination

Pagination is the process of dividing content into discrete pages, allowing users to navigate through large sets of data in a more manageable way. This technique enhances user experience by preventing overwhelming amounts of information from being displayed on a single page, leading to faster loading times and improved site usability.

Visit the following resources to learn more:

- [@article@Pagination in Rails from scratch (no gems)](https://dev.to/anakbns/pagination-in-rails-from-scratch-no-gems-206f)

## Pagination

# Pagination

Pagination is the process of dividing content into discrete pages, allowing users to navigate through large datasets in a manageable way. Instead of displaying all records at once, which can lead to performance issues and a poor user experience, pagination presents data in smaller, more digestible chunks, typically with navigation controls to move between pages. This improves loading times and makes it easier for users to find the information they need.

## Pagy

# Pagy

Pagy is a gem in Ruby on Rails that simplifies the implementation of pagination in your web applications. It provides a fast and flexible way to divide large datasets into smaller, more manageable pages, improving user experience and server performance. Pagy focuses on efficiency and minimal memory usage, offering customizable templates and a variety of features to suit different pagination needs.

Visit the following resources to learn more:

- [@official@Pagy](https://ddnexus.github.io/pagy/)
- [@opensource@pagy](https://github.com/ddnexus/pagy)
- [@article@A step-by-step guide to paginate your Rails app with Pagy gem](https://medium.com/@barrosgiovanni1/a-step-by-step-guide-to-paginate-your-rails-app-with-pagy-gem-d177c42a43a6)
- [@video@Pagy Gem with Turbo for Easy Infinite Scrolling | Ruby on Rails 7 Tutorial](https://www.youtube.com/watch?v=4nrmf5KfD8Y)

## Partials

# Partials

Partials are reusable snippets of view code that can be rendered within other views. They help to keep your views organized and DRY (Don't Repeat Yourself) by extracting common UI elements or logic into separate files. This allows you to easily update and maintain these elements across your application without duplicating code.

Visit the following resources to learn more:

- [@official@Partials](https://guides.rubyonrails.org/action_view_overview.html#partials)
- [@article@An Intro to Partials and Helpers in Ruby on Rails](https://staceymck.medium.com/an-intro-to-partials-and-helpers-in-ruby-on-rails-10d62d85da24)
- [@video@Rails Tutorial | Working with View Partials in Ruby on Rails](https://www.youtube.com/watch?v=YIJwb0rQS74)

## Phlex

# Phlex

Phlex is a Ruby library for building HTML views with a Ruby syntax. It offers a component-based approach, allowing developers to define reusable UI elements as Ruby classes. This approach aims to provide a more structured and maintainable way to create dynamic web pages compared to traditional ERB templates.

Visit the following resources to learn more:

- [@official@Phlex](https://www.phlex.fun/)
- [@opensource@phlex-rails](https://github.com/yippee-fun/phlex-rails)
- [@article@Ruby On rails Using phlex gem](https://medium.com/@ashwinborkar1997/ruby-on-rails-using-phlex-gem-5603ab87a4bf)
- [@video@Components with Phlex in Rails](https://www.youtube.com/watch?v=l4bQSfqZZfQ)

## Plugins  Engines

# Plugins & Engines

Plugins and engines in Rails are both ways to package and reuse code, but they serve slightly different purposes. Plugins are typically smaller and used to add specific functionalities or modify existing behavior within a Rails application. Engines, on the other hand, are more self-contained and can act as mini-applications within a larger Rails application, often providing their own models, controllers, views, and routes.

Visit the following resources to learn more:

- [@official@The Basics of Creating Rails Plugins](https://guides.rubyonrails.org/plugins.html)
- [@official@Getting Started with Engines](https://guides.rubyonrails.org/engines.html)
- [@article@Building Ruby on Rails engines](https://www.honeybadger.io/blog/rails-engines/)
- [@article@A Guide to Rails Engines in the Wild: Real World Examples of Rails Engines in Action](https://www.toptal.com/developers/ruby-on-rails/rails-engines-in-the-wild-real-world-examples-of-rails-engines-in-action)
- [@video@Creating A Private Ruby Gem for Ruby on Rails 7](https://www.youtube.com/watch?v=H4j2vUwZgEk)
- [@video@Your First Rails Engine | Ruby on Rails 7 Gem Tutorial](http://youtube.com/watch?v=7AVb4mJuIWA)

## Plugins

# Plugins

Plugins are self-contained packages of code that extend or modify the functionality of a Rails application. They provide a way to encapsulate reusable features, such as authentication, authorization, or payment processing, and easily integrate them into different Rails projects. Plugins can add models, controllers, views, helpers, and even modify the Rails framework itself.

## Postgresql

# PostgreSQL in Rails

PostgreSQL is an open-source, object-relational database system known for its reliability, feature robustness, and adherence to standards. It's a popular choice for Rails applications due to its advanced data types, support for complex queries, and strong community support. Rails seamlessly integrates with PostgreSQL through Active Record, providing an abstraction layer for database interactions.

Visit the following resources to learn more:

- [@roadmap@Visit the Dedicated PostgreSQL Roadmap](https://roadmap.sh/postgresql-dba)
- [@official@Configuring a PostgreSQL Database](https://guides.rubyonrails.org/configuring.html#configuring-a-postgresql-database)
- [@article@How To Set Up Ruby on Rails with Postgres](https://www.digitalocean.com/community/tutorials/how-to-set-up-ruby-on-rails-with-postgres)
- [@article@Getting started with Ruby on Rails and Postgres on Supabase](https://supabase.com/blog/ruby-on-rails-postgres)
- [@video@How To Use PostgreSQL with Your Ruby on Rails Application](https://www.youtube.com/watch?v=lLiEiBzEct8)

## Pry

# Pry

Pry is a powerful Ruby runtime developer console and alternative to `irb`. It allows you to pause your code's execution at any point, inspect variables, step through code line by line, and even modify your code on the fly. This makes it an invaluable tool for understanding and debugging Ruby and Rails applications.

Visit the following resources to learn more:

- [@opensource@pry](https://github.com/pry/pry)
- [@article@How to use Pry to debug Ruby apps](https://www.honeybadger.io/blog/debugging-ruby-with-pry/)
- [@article@Debugging Ruby Code with Pry](https://laflamablanc.medium.com/debugging-ruby-code-with-pry-a0bf1f5e97ca)
- [@video@Pry Open Your Rails 7 Code Debug Like a Pro](https://www.youtube.com/watch?v=yMdV0tpra7c)
- [@video@Ruby on Rails - Railscasts #280 Pry With Rails](https://www.youtube.com/watch?v=KfFf2-KJNTU)

## Public

# Public Directory

The `public` directory in a Ruby on Rails application serves as the root directory for all static assets that are directly accessible by web browsers. It holds files like HTML, CSS, JavaScript, images, and other media that don't require any processing or compilation by Rails before being served to the user. These files are served directly by the web server (like Nginx or Apache) without Rails intervention, making them efficient for delivering static content.

## Pundit

# Pundit

Pundit is a Ruby gem that provides a straightforward way to implement authorization in your Ruby on Rails applications. It focuses on defining authorization rules using plain Ruby objects (policies) that determine whether a given user is allowed to perform a specific action on a particular resource. This approach promotes clean, maintainable, and testable authorization logic within your application.

Visit the following resources to learn more:

- [@opensource@pundit](https://github.com/varvet/pundit)
- [@article@Mastering Authorization in Rails with Pundit](https://www.shakacode.com/blog/mastering-authorization-in-rails-with-pundit/)
- [@video@Pundit Gem For Authorization In Ruby On Rails 7](https://www.youtube.com/watch?v=SodfIjgcaW8)
- [@video@Ruby on Rails #49 gem Pundit for Authorization - Complete Guide](https://www.youtube.com/watch?v=xxkx57-vbQI)

## Query Optimization

# Query Optimization

Query optimization focuses on improving the efficiency of database queries to reduce execution time and resource consumption. This involves techniques like eager loading to minimize the number of queries, using indexes to speed up data retrieval, and writing efficient query conditions to filter data effectively. The goal is to retrieve the necessary data as quickly as possible, improving the overall performance of your Rails application.

Visit the following resources to learn more:

- [@official@Eager Loading Associations](https://guides.rubyonrails.org/active_record_querying.html#eager-loading-associations)
- [@article@Optimizing database queries in Rails with Active Record](https://medium.com/@arnaudetienne/optimizing-database-queries-in-rails-with-active-record-b84295866af0)
- [@article@Active Record Query Optimization Tips: Boost Your Ruby on Rails Application Performance](https://kinsta.com/blog/active-record-query-optimization/)

## Rails  Frontend

# Rails & Frontend

Rails, while primarily a backend framework, works seamlessly with various frontend technologies to build complete web applications. You can use Rails to handle the server-side logic, data management, and API endpoints, while employing frontend frameworks like React, Vue.js, or even Hotwire for the user interface and interactive elements. Hotwire, in particular, allows you to build modern, reactive UIs by sending HTML over the wire instead of complex JSON, simplifying the development process and leveraging Rails' server-side rendering capabilities. This combination allows developers to create full-stack applications with a clear separation of concerns, where Rails manages the backend and the chosen frontend framework handles the user experience.

## Rails Command Line

# Rails Command Line

The Rails command line interface (CLI), often accessed via the `rails` command, is a powerful tool for creating, managing, and interacting with Rails applications. It provides a suite of commands to generate code, run tests, manage databases, and perform various other development tasks, streamlining the development process and reducing boilerplate code.

## Rails Generators

# Rails Generators

Rails Generators are powerful tools built into the Rails framework that automate the creation of files and directories needed for various parts of your application. They streamline development by providing pre-built templates for models, controllers, views, migrations, and more, reducing boilerplate code and ensuring consistency across your project. Using generators helps you quickly scaffold out the basic structure of your application components, allowing you to focus on the specific logic and functionality you need to implement.

## Rails Internationalization

# Rails Internationalization

Internationalization (I18n) is the process of designing and developing applications that can be adapted to various languages and regions without engineering changes. It involves extracting text and other locale-specific data from the application's code and storing it in separate files, allowing the application to be translated and formatted for different locales. This enables users to interact with the application in their preferred language and cultural context.

Visit the following resources to learn more:

- [@official@Rails Internationalization (I18n) API](https://guides.rubyonrails.org/i18n.html)
- [@article@Rails internationalization (I18n): Tutorial on Rails locales & more](https://lokalise.com/blog/rails-i18n/)
- [@article@A Comprehensive Guide to Rails Internationalization (i18n)](https://www.honeybadger.io/blog/rails-i18n/)
- [@article@7 Key Best Practices for Rails Internationalization](https://phrase.com/blog/posts/rails-i18n-best-practices/)
- [@video@Intro To I18n Localizations With Ruby On Rails 7](https://www.youtube.com/watch?v=gkaxM1AqBss)

## Rails Logger

# Rails Logger

The Rails Logger is a built-in component within Ruby on Rails that provides a standardized way to record events and messages during the execution of an application. It allows developers to track application behavior, diagnose issues, and monitor performance by writing information to various output destinations, such as files or the console. The logger offers different severity levels (e.g., debug, info, warn, error, fatal) to categorize messages based on their importance, enabling developers to filter and prioritize logged information effectively.

Visit the following resources to learn more:

- [@official@The Logger](https://guides.rubyonrails.org/debugging_rails_applications.html#the-logger)
- [@article@How to Start Logging With Ruby on Rails](https://betterstack.com/community/guides/logging/how-to-start-logging-with-ruby-on-rails/#step-6-configuring-logger)
- [@video@Debugging And Logging | Intro To Ruby On Rails 7 Part 24](https://www.youtube.com/watch?v=9rDK2rbm6DI)

## Raw Sql

# Raw SQL in Active Record

Active Record typically provides an abstraction layer for database interactions, allowing you to work with objects and methods instead of writing SQL queries directly. However, sometimes you need more control or access to database-specific features. Raw SQL allows you to bypass Active Record's abstraction and execute SQL queries directly against your database, giving you the flexibility to perform complex operations or optimize performance in specific scenarios.

Visit the following resources to learn more:

- [@roadmap@Visit the Dedicated SQL Roadmap](https://roadmap.sh/sql)
- [@official@Finding by SQL](https://guides.rubyonrails.org/active_record_querying.html#finding-by-sql)

## Redirects

# Redirects

Redirects in web applications are mechanisms to automatically forward a user from one URL to another. This is commonly used for various reasons, such as moving content to a new location, handling outdated URLs, or guiding users through a specific workflow. In Rails, redirects are implemented within controllers to send an HTTP response that instructs the browser to navigate to a different URL.

## Rendering Views

# Rendering Views

Rendering views in Ruby on Rails involves generating HTML (or other formats) to be displayed to the user. This process typically uses templates written in ERB or other templating languages, combining data from the controller with the template to produce the final output. Rails provides mechanisms for rendering different types of content, including partials, layouts, and collections, offering flexibility in structuring and organizing the presentation layer of an application.

Visit the following resources to learn more:

- [@official@Layouts and Rendering in Rails](https://guides.rubyonrails.org/layouts_and_rendering.html)

## Request Reponse Flow

# Request-Response Flow in Rails Routing

The request-response flow in Rails describes how a web application handles incoming requests from users and generates appropriate responses. When a user interacts with a Rails application (e.g., clicks a link or submits a form), the request is first received by the Rails router. The router then analyzes the request and determines which controller and action should handle it. The controller action processes the request, interacts with the model if necessary, and renders a view. Finally, the rendered view is sent back to the user as a response.

## Restful Routes

# RESTful Routes

RESTful routes provide a standardized way to map HTTP verbs (GET, POST, PUT, DELETE) to controller actions, representing Create, Read, Update, and Delete (CRUD) operations on resources. This convention promotes a clean and predictable URL structure, making applications easier to understand and maintain by aligning routes with the underlying data model. By following REST principles, developers can create well-organized and scalable web applications.

## Routing Fundamentals

# Routing Fundamentals

Routing in a web application is the process of mapping incoming HTTP requests (like GET or POST requests) to specific controller actions. It acts as a traffic director, examining the URL and other request parameters to determine which part of the application should handle the request and generate a response. This mechanism allows you to define how your application responds to different URLs, creating a structured and organized web experience for users.

## Rspec

# RSpec

RSpec is a testing framework for Ruby. It provides a domain-specific language (DSL) for writing tests that are easy to read and understand. RSpec focuses on behavior-driven development (BDD), allowing developers to describe the desired behavior of their code in a clear and concise manner, leading to more maintainable and reliable applications.

Visit the following resources to learn more:

- [@official@RSpec](https://rspec.info/)
- [@opensource@rspec-rails](https://github.com/rspec/rspec-rails)
- [@article@Ruby on Rails Testing with RSpec: Writing your First Tests](https://medium.com/nerd-for-tech/ruby-on-rails-testing-with-rspec-writing-your-first-tests-6330920928fd)
- [@article@Getting Started With Testing In Rails (Using Minitest and RSpec)](https://medium.com/@ethanryan/getting-started-with-testing-in-rails-using-minitest-and-rspec-113fe1f866a)
- [@article@Minitest vs. RSpec in Rails](https://www.honeybadger.io/blog/minitest-rspec-rails/)
- [@video@Automated testing with rspec](https://www.youtube.com/playlist?list=PLS6F722u-R6Ik3fbeLXbSclWkT6Qsp9ng)
- [@video@Test Driven RSpec](https://www.youtube.com/playlist?list=PLr442xinba86s9cCWxoIH_xq5UE9Wwo4Z)

## Scopes

# Scopes

Scopes in Rails models are pre-defined database queries that you can reuse throughout your application. They allow you to encapsulate common query logic, making your code cleaner, more readable, and easier to maintain. Scopes can be simple, like finding all active users, or more complex, involving joins and conditions. They are defined within the model and can be chained together to create more specific queries.

Visit the following resources to learn more:

- [@official@Scopes](https://guides.rubyonrails.org/active_record_querying.html#scopes)
- [@article@Scopes](https://www.theodinproject.com/lessons/ruby-on-rails-active-record-queries#scopes)
- [@article@How to Use Scopes in Ruby on Rails](https://www.rubyguides.com/2019/10/scopes-in-ruby-on-rails/)
- [@article@ActiveRecord Scopes: Ruby On Rails Best Practices](https://medium.com/nyc-ruby-on-rails/mastering-activerecord-scopes-5d7082122c0d)
- [@video@Taking A Look At Scopes In Ruby On Rails 7](https://www.youtube.com/watch?v=nzgf1LRqxvg)
- [@video@How to use Scopes in Ruby on Rails](https://www.youtube.com/watch?v=_LerTMQW76w)

## Security

# Security

Security in web applications involves protecting data and functionality from unauthorized access, use, disclosure, disruption, modification, or destruction. It encompasses various practices and techniques to ensure confidentiality, integrity, and availability of the application and its data. This includes addressing vulnerabilities like cross-site scripting (XSS), SQL injection, and authentication bypasses.

Visit the following resources to learn more:

- [@official@Securing Rails Applications](https://guides.rubyonrails.org/security.html)
- [@article@A Complete Guide to Ruby on Rails Security Measures 🛡️](https://railsdrop.com/2025/05/11/a-complete-guide-to-ruby-on-rails-security-measures/)
- [@article@The inadequate guide to Rails security](https://www.honeybadger.io/blog/ruby-security-tutorial-and-rails-security-guide/)
- [@article@Essential Security Best Practices for Ruby on Rails](https://dev.to/harsh_u115/essential-security-best-practices-for-ruby-on-rails-4d68)
- [@article@Securing Ruby on Rails Applications: Best Practices](https://medium.com/@vaishnaviganeshkar15/securing-ruby-on-rails-applications-best-practices-787f2cc03f02)

## Sessions

# Sessions in Rails Controllers

Beyond processing requests and rendering views, controllers also provide a mechanism for maintaining user sessions. Sessions allow you to store data related to a specific user across multiple requests, enabling features like login persistence, shopping carts, and personalized experiences. This data is typically stored on the server and associated with a unique session ID that is sent to the client's browser as a cookie.

Visit the following resources to learn more:

- [@official@Session](https://guides.rubyonrails.org/action_controller_overview.html#session)
- [@article@Mastering Sessions and Cookies in Rails: A Comprehensive Guide](https://medium.com/@carriekarft/mastering-sessions-and-cookies-in-rails-a-comprehensive-guide-0446422d7b22)
- [@article@Cookies & Sessions in Rails](https://dev.to/matthewkohn/cookies-sessions-in-rails-54b8)
- [@video@Rails Cookies and Session](https://www.youtube.com/watch?v=iOR-9fMMmLM)

## Setting Up Ruby On Rails

# Setting up Ruby on Rails

Setting up Ruby on Rails involves installing the necessary software and configuring your environment to develop and run Rails applications. This typically includes installing Ruby, the Rails gem, a database system (like PostgreSQL or MySQL), and any other dependencies required for your project. Once these components are installed, you can create a new Rails application using the `rails new` command and start building your web application.

## Sqlite

# SQLite in Rails

SQLite is a lightweight, file-based database engine. It requires no separate server process and stores the entire database in a single file on disk. This makes it a convenient choice for development, testing, and small-scale applications where a full-fledged database server isn't necessary. Rails supports SQLite out of the box, making it easy to set up and use.

Visit the following resources to learn more:

- [@official@Configuring an SQLite3 Database](https://guides.rubyonrails.org/configuring.html#configuring-an-sqlite3-database)
- [@official@SQLite](https://www.sqlite.org/index.html)
- [@article@SQLite in Production? Rails 8 Made Me a Believer](https://bhavyansh001.medium.com/sqlite-in-production-rails-8-made-me-a-believer-28a621db864a)
- [@article@Configuring Rails Applications](https://edgeguides.rubyonrails.org/configuring.html#locations-for-initialization-code)
- [@video@Stephen Margheim - SQLite on Rails: Supercharging the One-Person Framework - Rails World 2024](https://www.youtube.com/watch?v=wFUy120Fts8)

## Storage

# Storage in Ruby on Rails

Rails itself doesn't directly manage file storage; instead, it relies on external services or libraries to handle the actual saving and retrieval of these files. This allows you to store files locally on your server, or more commonly, in cloud storage services like Amazon S3, Google Cloud Storage, or Azure Blob Storage. These services offer scalability, reliability, and often lower costs compared to managing storage yourself.

Visit the following resources to learn more:

- [@official@Active Storage Overview](https://guides.rubyonrails.org/active_storage_overview.html)
- [@article@Using Active Storage for Ruby on Rails](https://medium.com/@bwrosen20/using-active-storage-for-ruby-on-rails-a84991e45d93)
- [@video@Active Storage For File Uploads | Ruby on Rails 7 Tutorial](https://www.youtube.com/watch?v=jjjAJeWJ2xE)
- [@video@Active Storage in Ruby on Rails 5.2](https://www.youtube.com/playlist?list=PL3mtAHT_eRexVRWcjcqgfTvYQD2scoTlk)

## Strong Parameters

# Strong Parameters

Controller parameters are the data sent from a client (like a web browser) to your Rails application, typically through forms or API requests. These parameters are accessible within your controller actions. Strong parameters are a security feature in Rails that helps protect your application from mass assignment vulnerabilities. They work by requiring you to explicitly permit which parameters are allowed to be used when creating or updating database records, effectively filtering out any unexpected or malicious data that might be included in the request.

Visit the following resources to learn more:

- [@official@Parameters](https://guides.rubyonrails.org/action_controller_overview.html#parameters)
- [@official@Strong Parameters](https://guides.rubyonrails.org/action_controller_overview.html#strong-parameters)
- [@article@Rails Params: Where do they come from?](https://medium.com/launch-school/params-in-rails-where-do-they-come-from-b172cdb46eb4)
- [@article@How the Rails params hash works](https://www.honeybadger.io/blog/how-the-rails-params-hash-works/)
- [@video@Understanding Rails Params & How to Use Them](https://www.youtube.com/watch?v=01xF2U2oA2M)
- [@video@Ruby On Rails - Strong Parameters in Your Controllers](https://www.youtube.com/watch?v=Z8IrqXK86UM)

## Testing

# Testing

Testing in software development involves verifying that individual units of code (unit tests) and the application as a whole (integration and system tests) function as expected. It helps ensure code quality, prevents regressions, and facilitates easier refactoring by providing a safety net to catch errors early in the development process. Different types of tests, such as unit, integration, and system tests, focus on different aspects of the application to provide comprehensive coverage.

Visit the following resources to learn more:

- [@official@Testing Rails Applications](https://guides.rubyonrails.org/testing.html)
- [@article@A journey towards better Ruby on Rails testing practices](https://thoughtbot.com/blog/a-journey-towards-better-testing-practices)
- [@article@What are all the Rails testing tools and how do I use them?](https://www.codewithjason.com/rails-testing-tools/)
- [@video@Testing in Ruby on Rails Applications (Unit, Integration, & Functional Tests)](https://www.youtube.com/watch?v=eXmA1vWGDfs)
- [@video@Testing A Rails App That Uses Devise Sessions | Ruby On Rails 7 Tutorial](https://www.youtube.com/watch?v=PtGjHGdJQrQ)

## Transactions

# Transactions

Transactions are a sequence of operations performed as a single logical unit of work. They ensure data integrity by treating a series of database operations as an "all or nothing" proposition. If any operation within the transaction fails, the entire transaction is rolled back, reverting the database to its original state before the transaction began. This prevents partial updates and maintains consistency.

Visit the following resources to learn more:

- [@official@Active Record Transactions](https://api.rubyonrails.org/classes/ActiveRecord/Transactions/ClassMethods.html)
- [@article@What Is A Transaction?](https://www.honeybadger.io/blog/database-transactions-rails-activerecord/)
- [@article@Rails transactions: The Complete Guide](https://medium.com/@kristenrogers.kr75/rails-transactions-the-complete-guide-7b5c00c604fc)
- [@article@107.ActiveRecord Transactions in depth](https://courses.bigbinaryacademy.com/learn-rubyonrails/activerecord-transactions-in-depth/)
- [@article@5 Tips to Design Ruby on Rails Transactions the Right Way](https://blog.appsignal.com/2022/03/30/5-tips-to-design-ruby-on-rails-transactions-the-right-way.html)

## Validations

# Validations

Validations are rules that you define for your models to ensure that only valid data is saved into your database. They help maintain data integrity by checking if attributes meet specific criteria, such as presence, format, uniqueness, or custom conditions, before a record is created or updated. If a validation fails, the record will not be saved, and an error message will be added to the object's `errors` collection.

Visit the following resources to learn more:

- [@official@Active Record Validations](https://guides.rubyonrails.org/active_record_validations.html)
- [@article@Ruby on Rails - Validation](https://www.tutorialspoint.com/ruby-on-rails/rails-validation.htm)
- [@article@A Deep Dive into Active Record Validations](https://www.honeybadger.io/blog/active-record-validations/)
- [@video@Active Record Validations For Beginners | Ruby On Rails 7 Tutorial](https://www.youtube.com/watch?v=gLRm5UajMiE)
- [@video@Understanding Ruby on Rails ActiveRecord Validations](https://www.youtube.com/watch?v=c3hoXWO_6ao)

## Viewcomponent

# ViewComponent

ViewComponent is a framework for building reusable, testable & encapsulated UI components in Ruby on Rails. It encourages a component-based architecture within your Rails application, allowing you to define UI elements as Ruby classes with associated templates, similar to components in frameworks like React or Vue. This approach promotes better organization, maintainability, and reusability of your view code.

Visit the following resources to learn more:

- [@official@ViewComponent](https://viewcomponent.org/)
- [@opensource@view_component](https://github.com/ViewComponent/view_component)
- [@article@Building reusable UI components in Rails with ViewComponent](https://www.honeybadger.io/blog/rails-viewcomponent/)
- [@video@ViewComponent Crash Course with Ruby on Rails](https://www.youtube.com/watch?v=Mc19pB784Us)
- [@video@Intro To View Components In Ruby On Rails 7](https://www.youtube.com/watch?v=z077hg7Zzyk)

## Why Web Frameworks

# Why Web Frameworks?

Web frameworks provide a structured and efficient way to build web applications by offering pre-built components, tools, and conventions. They handle common tasks like routing, database interaction, and templating, allowing developers to focus on the unique features of their application rather than reinventing the wheel. This leads to faster development, more maintainable code, and improved security.
