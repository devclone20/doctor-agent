# Software Architect Roadmap

## Acid Cap Theorem

# ACID & CAP Theorem

ACID (Atomicity, Consistency, Isolation, Durability) and CAP (Consistency, Availability, Partition Tolerance) are essential concepts in distributed systems. They are often used to explain the trade-offs between consistency and availability.

CAP is an acronym for Consistency, Availability, and Partition Tolerance. According to the CAP theorem, any distributed system can only guarantee two of the three properties at any time. You can't guarantee all three properties at once.

ACID is an acronym that stands for Atomicity, Consistency, Isolation, Durability. ACID is a set of properties of database transactions intended to guarantee validity even in the event of errors, power failures, etc.

Visit the following resources to learn more:

- [@article@What is CAP Theorem?](https://www.bmc.com/blogs/cap-theorem/)
- [@article@CAP Theorem - Wikipedia](https://en.wikipedia.org/wiki/CAP_theorem)
- [@article@An Illustrated Proof of the CAP Theorem](https://mwhittaker.github.io/blog/an_illustrated_proof_of_the_cap_theorem/)
- [@article@CAP Theorem and its applications in NoSQL Databases](https://www.ibm.com/uk-en/cloud/learn/cap-theorem)
- [@article@ACID - Wikipedia](https://en.wikipedia.org/wiki/ACID)
- [@video@What is CAP Theorem?](https://www.youtube.com/watch?v=_RbsFXWRZ10)

## Actors

# Actors

Actor Model is a model that represents actors as the basic unit of a system, they can only communicate through messages and have their own private state, and they can also manage other actors, resulting in an encapsulated and fault-tolerant system.

Visit the following resources to learn more:

- [@article@The actor model in 10 minutes](https://www.brianstorti.com/the-actor-model/)
- [@video@Actor Model Explained](https://www.youtube.com/watch?v=ELwEdb_pD0k)

## Apache Spark

# Apache spark

Apache Spark is a multi-language engine for executing data engineering, data science, and machine learning on single-node machines or clusters.

Visit the following resources to learn more:

- [@official@Apache Spark](https://spark.apache.org/)
- [@feed@Explore top posts about Apache](https://app.daily.dev/tags/apache?ref=roadmapsh)

## Apis  Integrations

# APIs and Integrations

APIs (Application Programming Interfaces) are essential for enabling communication between different software applications, allowing them to share data and functionality seamlessly. They serve as the bridge that connects disparate systems, making it possible for applications to interact without needing to know the internal workings of one another. Integration, on the other hand, refers to the process of connecting these systems to work together effectively, often utilizing APIs to facilitate data exchange and process automation. By leveraging APIs in integrations, organizations can enhance operational efficiency, reduce data silos, and improve user experiences through seamless data flow between applications.

Visit the following resources to learn more:

- [@article@What is API Integration](https://www.ibm.com/topics/api-integration)
- [@article@API Integration - Postman](https://www.postman.com/api-platform/api-integration/)
- [@article@API First Integration](https://www.infoq.com/articles/api-first-integration/)

## Application Architecture

# Application Level Architecture

The lowest level of architecture. Focus on one single application. Very detailed, low level design. Communication is usually within one development team.

Visit the following resources to learn more:

- [@article@Application Architecture](https://www.codesee.io/learning-center/application-architecture)

## Architecture

# Architectures

Architecture refers to the approach of designing and implementing software architecture with a focus on the tools and technologies that will be used during the development process. This perspective emphasizes that the selection of tools can significantly influence architectural decisions and the overall design of the system.

## Atlassian Tools

# Atlassian Tools

Atlassian tools offer a suite of solutions designed to streamline collaboration, project management, and incident handling for various teams. Jira serves as the core workflow engine, allowing organizations to track tasks through customizable workflows with granular permissions. Specialized tools like Jira Service Desk cater to help desk teams for managing incoming requests, while Jira Core enables business teams to organize and execute task-oriented projects across departments like marketing, HR, and operations. For enhanced collaboration, Confluence acts as a knowledge-sharing wiki, allowing teams to create, share, and audit content changes seamlessly. Bitbucket provides Git repository management for enterprise teams, fostering efficient collaboration on codebases.

Other tools cater to more specific needs. **Statuspage** focuses on communication during outages or maintenance, keeping users informed from investigation to resolution. **Opsgenie** ensures smooth incident management for always-on services, helping dev and ops teams stay in control of alerts. **Advanced Roadmaps** for Jira assists multiple teams in capacity planning and dependency tracking, while **Jira Align** supports enterprise-level agile planning to align strategy with execution and drive digital transformation. Together, these tools empower teams to improve efficiency, transparency, and adaptability across various workflows.

Visit the following resources to learn more:

- [@official@Jira Service Desk](https://www.atlassian.com/software/jira/service-management/features/service-desk)
- [@official@Jira Core](https://www.atlassian.com/software/jira/work-management)
- [@official@Confluence](https://www.atlassian.com/wac/software/confluence?)
- [@official@Bitbucket](https://bitbucket.org/product/)
- [@official@Statuspage](https://www.atlassian.com/software/statuspage)
- [@official@Opsgenie](https://www.atlassian.com/software/opsgenie)
- [@official@Advanced Roadmaps for Jira](https://www.atlassian.com/software/jira/features/roadmaps)
- [@official@Jira Align](https://www.atlassian.com/software/jira/align)
- [@feed@Explore top posts about Atlassian](https://app.daily.dev/tags/atlassian?ref=roadmapsh)

## Auth Strategies

# Authentication Strategies

Authentication strategies are essential for ensuring secure access to applications and systems. They define how users are verified before being granted access to resources. Here are some common authentication strategies:

Password-Based Authentication

Multi-Factor Authentication (MFA)

OAuth and OpenID Connect

Token-Based Authentication:

Biometric Authentication

Certificate-Based Authentication

Visit the following resources to learn more:

- [@article@JSON Web Token - Handbook](https://auth0.com/resources/ebooks/jwt-handbook)
- [@article@Authentication vs Authorization](https://www.cerbos.dev/blog/authentication-vs-authorization)
- [@video@SAML Overview](https://www.youtube.com/watch?v=i8wFExDSZv0)
- [@video@A Developers Guide to SAML](https://www.youtube.com/watch?v=l-6QSEqDJPo)
- [@video@SAML 2.0: Technical Overview](https://www.youtube.com/watch?v=SvppXbpv-5k)
- [@video@An Illustrated Guide to OAuth and OpenID Connect](https://www.youtube.com/watch?v=t18YB3xDfXI)
- [@video@OAuth 2.0 & OpenID Connect (OIDC): Technical Overview](https://www.youtube.com/watch?v=rTzlF-U9Y6Y)

## Babok

# Babok

The guide to the Business Analysis Body of Knowledge (BABOK Guide) is a book from the International Institute of Business Analysis (IIBA) that provides business analysts (BAs) with strategies for using data to improve an organization's workflow processes, technology, products and services.

Visit the following resources to learn more:

- [@official@Babok](https://www.iiba.org/career-resources/a-business-analysis-professionals-foundation-for-success/babok/)
- [@article@Wikipedia](https://en.wikipedia.org/wiki/A_Guide_to_the_Business_Analysis_Body_of_Knowledge)

## Balance

# Balance

Achieving balance in architecture requires managing trade-offs between quality, cost, and development speed, avoiding over-engineering while aligning functional and non-functional requirements. Architects must navigate conflicting goals, like balancing short-term simplicity with long-term vision, ensuring solutions fit future needs while involving developers, businesses, and managers in understanding the financial and strategic impact. Additionally, architects often mediate between diverse groups, resolving conflicts and aligning strategies through effective communication, such as the “Four-Ears Model” by Schulze von Thun, which aids in fostering collaboration and achieving balanced, strategic outcomes.

Visit the following resources to learn more:

- [@article@Wikipedia](https://en.wikipedia.org/wiki/Balance_(architecture))

## Bpm Bpel

# BPM BPEL

BPM: Business Process Management
--------------------------------

Medium or large enterprises needs robust processes to streamline their business needs by reducing the cost incurred per process and diminishing the turn around time for each activity. To achieve the above, there are various BPM tools like PEGA, IBM BPM, Appian, etc. Basically these tools automate the processes through a robust process modelling and implementation.

BPMN: Business Process Management Notations
-------------------------------------------

Its is a standard for representing business processes graphically. While modelling the process, the notations used are complied with BPMN (there are other like EPC, etc.). So BPMN is a standard notation that BPM consultants follow to model the business process. BPMN has versions and now BPMN 2.0 is the standard one.

BPEL : Business Process Execution Language
------------------------------------------

Programmers use BPEL to define how a business process that involves web services will be executed. BPEL messages are typically used to invoke remote services, orchestrate process execution and manage events and exceptions. BPEL is often associated with Business Process Management Notation. In many organizations, analysts use BPMN to visualize business processes and developers transform the visualizations to BPEL for execution.

Visit the following resources to learn more:

- [@article@What is BPM?](https://www.redhat.com/en/topics/automation/what-is-business-process-management)
- [@article@BPEL described](https://www.ibm.com/docs/en/baw/19.x?topic=SS8JB4_19.x/com.ibm.wbpm.wid.main.doc/prodoverview/topics/cbpelproc.html)
- [@video@BPM vs BPEL](https://www.youtube.com/watch?v=V6nr5dnb1JQ)

## Ci  Cd

# CI / CD

CI/CD is a method to frequently deliver apps to customers by introducing automation into the stages of app development. The main concepts attributed to CI/CD are continuous integration, continuous delivery, and continuous deployment. CI/CD is a solution to the problems integrating new code can cause for development and operations teams (AKA "integration hell").

Visit the following resources to learn more:

- [@article@CI/CID - GitHub](https://github.com/resources/articles/devops/ci-cd)
- [@article@What is CI/CD? - Redhat](https://www.redhat.com/en/topics/devops/what-is-ci-cd)
- [@article@Continuous Integration and Continuous Delivery Explained](https://www.infoworld.com/article/3271126/what-is-cicd-continuous-integration-and-continuous-delivery-explained.html)
- [@feed@Explore top posts about CI/CD](https://app.daily.dev/tags/cicd?ref=roadmapsh)

## Client  Server

# Client-Server Architecture

Client-server architecture is a computing model that separates tasks or workloads between service providers (servers) and service requesters (clients). This architecture is widely used in networked applications, including web applications, where clients interact with servers to access resources, services, and data.

Visit the following resources to learn more:

- [@article@What is Client-Server Architecture](https://www.simplilearn.com/what-is-client-server-architecture-article)
- [@feed@Explore top posts about Architecture](https://app.daily.dev/tags/architecture?ref=roadmapsh)

## Cloud Design Patterns

# Cloud Design Patterns

These design patterns are useful for building reliable, scalable, secure applications in the cloud. The cloud design patterns where each pattern describes the problem that the pattern addresses, considerations for applying the pattern, and an example based on Microsoft Azure. Most patterns include code samples or snippets that show how to implement the pattern on Azure. However, most patterns are relevant to any distributed system, whether hosted on Azure or other cloud platforms.

Visit the following resources to learn more:

- [@article@Cloud Design Patterns](https://learn.microsoft.com/en-us/azure/architecture/patterns/)
- [@feed@Explore top posts about Cloud](https://app.daily.dev/tags/cloud?ref=roadmapsh)

## Cloud Providers

# Cloud Providers

Cloud providers provide a layer of APIs to abstract infrastructure and provision it based on security and billing boundaries. The cloud runs on servers in data centers, but the abstractions cleverly give the appearance of interacting with a single “platform” or large application. The ability to quickly provision, configure, and secure resources with cloud providers has been key to both the tremendous success and complexity of modern DevOps.

Visit the following resources to learn more:

- [@article@Cloud Service Provider](https://www.techtarget.com/searchitchannel/definition/cloud-service-provider-cloud-provider)
- [@article@What are Cloud Providers?](https://www.redhat.com/en/topics/cloud-computing/what-are-cloud-providers)
- [@feed@Explore top posts about Cloud](https://app.daily.dev/tags/cloud?ref=roadmapsh)

## Communication

# Communication

From my observations this is one of the most underestimated skill. If you are brilliant in design but cannot communicate your ideas, your thoughts are likely to have less impact or even fail to succeed.

Communication is a critical yet often underestimated skill, especially for architects. It involves clearly conveying ideas, structuring discussions effectively, and driving meetings. Tools like “UZMO — Thinking With Your Pen” can enhance visual communication skills. Public speaking, whether to small or large groups, requires practice and stepping out of one’s comfort zone. Tailoring communication to the audience is essential—developers focus on details, while managers prioritize cost and outcomes. Regular, transparent communication ensures alignment across all levels, making the rationale behind decisions clear. Always being prepared with key slides and answers can boost confidence and efficiency during interactions.

Visit the following resources to learn more:

- [@article@Communication Skills](https://en.wikipedia.org/wiki/Communication)

## Consult  Coach

# Consult and Coach

Proactive consulting and coaching are essential to prevent architectural issues from escalating. Architects must anticipate future needs and prepare the organization by setting a clear vision of mid- and long-term goals, often using maturity models to provide structure and measure progress against SMART criteria. Building a **Community of Practice (CoP)** fosters collaboration, standardization, and knowledge sharing among professionals with shared interests, such as developers and architects, enhancing individual and organizational growth. Open-door sessions, held regularly without a strict agenda, encourage open communication, resolve minor issues promptly, and address complex topics through follow-ups, reducing misconceptions and ambiguity.

Visit the following resources to learn more:

- [@article@Wikipedia](https://en.wikipedia.org/wiki/Consulting)

## Containers

# Containers

Containers are a construct in which cgroups, namespaces, and chroot are used to fully encapsulate and isolate a process. This encapsulated process, called a container image, shares the kernel of the host with other containers, allowing containers to be significantly smaller and faster than virtual machines. These images are designed for portability, allowing for full local testing of a static image, and easy deployment to a container management platform.

Visit the following resources to learn more:

- [@article@cgroups](https://en.wikipedia.org/wiki/Cgroups)
- [@article@namespaces](https://en.wikipedia.org/wiki/Linux_namespaces)
- [@article@chroot](https://en.wikipedia.org/wiki/Chroot)
- [@article@What are Containers?](https://cloud.google.com/learn/what-are-containers)
- [@article@What is a Container?](https://www.docker.com/resources/what-container/)
- [@article@Articles about Containers - The New Stack](https://thenewstack.io/category/containers/)
- [@video@What are Containers?](https://www.youtube.com/playlist?list=PLawsLZMfND4nz-WDBZIj8-nbzGFD4S9oz)
- [@feed@Explore top posts about Containers](https://app.daily.dev/tags/containers?ref=roadmapsh)

## Cqrs Eventual Consistency

# CQRS eventual consistency

CQRS (Segregation of Responsibility for Command Queries) is an architecture pattern that comes with the idea of separating read and write operations into two distinct logical processes.

Visit the following resources to learn more:

- [@article@CQRS](https://martinfowler.com/bliki/CQRS.html)
- [@article@Introduction to CQRS](https://learn.microsoft.com/en-us/azure/architecture/patterns/cqrs)

## Datawarehouse Principles

# Datawarehouses Principles

It is based on the assumption that every system should take care of a concern in a way that such concern should be encapsulated by the system itself.

Visit the following resources to learn more:

- [@article@Toptal Developers Website](https://www.toptal.com/data-science/data-warehouse-concepts-principles)

## Ddd

# Domain-Driven Design

Domain-driven design (DDD) is a software design approach focusing on modeling software to match a domain according to input from that domain's experts.

In terms of object-oriented programming, it means that the structure and language of software code (class names, class methods, class variables) should match the business domain. For example, if a software processes loan applications, it might have classes like LoanApplication and Customer, and methods such as AcceptOffer and Withdraw.

DDD connects the implementation to an evolving model and it is predicated on the following goals:

*   Placing the project's primary focus on the core domain and domain logic;
*   Basing complex designs on a model of the domain;
*   Initiating a creative collaboration between technical and domain experts to iteratively refine a conceptual model that addresses particular domain problems.

Visit the following resources to learn more:

- [@article@DDD Starter Modelling Process](https://github.com/ddd-crew/ddd-starter-modelling-process/)
- [@article@Domain Driven Design Quickly](https://web.archive.org/web/20230606035225/https://matfrs2.github.io/RS2/predavanja/literatura/Avram%20A,%20Marinescu%20F.%20-%20Domain%20Driven%20Design%20Quickly.pdf)
- [@feed@Explore top posts about Architecture](https://app.daily.dev/tags/architecture?ref=roadmapsh)

## Decision Making

# Decision Making

Effective decision-making is crucial for architects to guide projects and organizations in the right direction. Focus on what’s important by emphasizing **conceptual integrity** (sticking to consistent decisions for simplicity and maintainability) and **uniformity** (ensuring standards like naming conventions are applied consistently). Prioritize critical decisions early to avoid costly workarounds or project delays, using tools like the Weighted Shortest Job First (WSJF) model for prioritization. Stay within your scope of competence to maintain credibility, collaborate with peers, and clarify responsibilities within the architectural hierarchy.

When making decisions, evaluate multiple options to ensure thorough analysis and foster stakeholder confidence. Comparing options based on measurable criteria, such as cost or feasibility, leads to better, fact-driven decisions. This process not only supports sustainable outcomes but also prepares you with strong arguments during discussions, ensuring alignment across teams and stakeholders.

Visit the following resources to learn more:

- [@article@Decision Making - Wikipedia](https://en.wikipedia.org/wiki/Decision-making)

## Design  Architecture

# Design and Architecture

Good design in software architecture blends theoretical knowledge with practical experience. Theoretically, architects should master fundamental design patterns, such as those detailed in _"Design Patterns: Elements of Reusable Object-Oriented Software"_, which remain foundational for modern architecture. Advanced knowledge of patterns and anti-patterns, like those in _"Enterprise Integration Patterns"_, extends this understanding. Architects must also focus on quality measures, ensuring designs meet non-functional requirements like scalability, security, and adaptability.

Practically, architects improve by experimenting with various technology stacks, gaining insights into their strengths and limitations. Exploring frameworks like Angular reveals real-world pattern applications, such as Observables, and fosters deeper understanding through hands-on coding. Attending user groups and engaging in communities, like those on Meetup, broadens perspectives and encourages curiosity, enabling architects to stay updated and continuously refine their craft.

Visit the following resources to learn more:

- [@roadmap@Visit Dedicated Software Design Roadmap](https://roadmap.sh/software-design-architecture)
- [@opensource@Design Patterns for Humans](https://github.com/nilbuild/design-patterns-for-humans)

## Distributed Systems

# Distributed Systems

Distributed systems are a type of computing architecture where components located on networked computers communicate and coordinate their actions by passing messages. These systems are designed to work together to achieve a common goal, often providing services or processing data in a collaborative manner.

Visit the following resources to learn more:

- [@article@Free Distributed Systems book from Maarten van Steen](https://www.distributed-systems.net/index.php/books/ds3/)
- [@article@Distributed Architectures](https://estuary.dev/distributed-architecture/)
- [@feed@Explore top posts about Architecture](https://app.daily.dev/tags/architecture?ref=roadmapsh)

## Documentation

# Documentation

Architectural documentation is sometimes more and sometimes less important. Important documents are for example architectural decisions or code guidelines. Initial documentation is often required before coding starts and need to be refined continuously. Other documentation can be automatically generated as code can also be documentation, e.g. UML class diagrams.

Visit the following resources to learn more:

- [@article@Wikipedia](https://en.wikipedia.org/wiki/Documentation)
- [@article@The Ultimate Guide To Software Architecture Documentation](https://www.workingsoftware.dev/software-architecture-documentation-the-ultimate-guide/)

## Emc Dms

# EMC and DMS

EMC (Enterprise Metadata Catalog) and DMS (Document Management System) are two distinct concepts in the realm of data management and information systems. Below is an overview of each:

An Enterprise Metadata Catalog (EMC) is a centralized repository that stores metadata about data assets within an organization. This metadata provides context, meaning, and structure to the data, enabling better data management and utilization.

A Document Management System (DMS) is a software solution that helps organizations capture, store, manage, and track electronic documents and images of paper-based information. DMS solutions are essential for organizing and securing documents in a digital format.

Visit the following resources to learn more:

- [@article@DMS](https://www.opentext.com/products/documentum-content-management)
- [@article@EMC Softwares](https://www.spiceworks.com/collaboration/content-collaboration/articles/top-10-enterprise-content-management-software-systems/)

## Enterprise Architecture

# Enterprise Level Architecture

The highest level of architecture. Focus on multiple solutions. High level, abstract design, which needs to be detailed out by solution or application architects. Communication is across the organization.

Visit the following resources to learn more:

- [@article@Enterprise Software Architecture](https://medium.com/@hsienwei/enterprise-software-architecture-957288829daa)
- [@article@Enterprise Architect vs Software Architect](https://www.linkedin.com/pulse/enterprise-architect-vs-software-who-you-luigi-saggese/)
- [@feed@Explore top posts about Architecture](https://app.daily.dev/tags/architecture?ref=roadmapsh)

## Enterprise Software

# Enterprise Software

Enterprise software refers to software applications that are designed to meet the needs of large organizations or enterprises. These applications are typically complex, scalable, and capable of integrating with other systems to support a wide range of business functions. Enterprise software is used to improve efficiency, streamline processes, and enhance productivity across various departments within an organization.

Visit the following resources to learn more:

- [@article@Enterprise Softwares](https://en.wikipedia.org/wiki/Enterprise_software)

## Esb Soap

# ESB and SOAP

ESB (Enterprise Service Bus) and SOAP (Simple Object Access Protocol) are two technologies that enable communication between different systems. ESB is a software architecture that allows for the integration of various systems, such as databases, web services, and mobile applications. SOAP is a messaging protocol that enables the exchange of structured data between systems over the internet.

Visit the following resources to learn more:

- [@article@Understanding SOAP: The Old Guard of Web Services](https://mariomthree.medium.com/understanding-soap-the-old-guard-of-web-services-6ca89d8ec312)
- [@article@Enterprise Service Bus](https://en.wikipedia.org/wiki/Enterprise_service_bus)
- [@article@ESB - IBM](https://www.ibm.com/topics/esb)

## Estimate And Evaluate

# Estimate and Evaluate

Estimation and evaluation are critical skills for architects and lead developers. Architects must understand basic project management principles to provide estimates for timelines, resources, and costs, considering all project phases like requirements, testing, and debugging. Using past data or models like COCOMO helps refine estimates. For agile projects, resources like _"Agile Estimating and Planning"_ by Mike Cohn can offer valuable guidance.

Evaluating "unknown" architectures involves assessing their suitability for current and future contexts through prepared questions. These should cover design practices (e.g., patterns and structure), development practices (e.g., code guidelines and deployment), quality assurance (e.g., test automation and peer reviews), and security measures (e.g., built-in security and penetration tests). This structured approach ensures informed decisions and promotes robust, maintainable solutions.

Visit the following resources to learn more:

- [@article@Evaluating Software Architectures](https://medium.com/oolooroo/evaluating-digital-architectures-a-deep-dive-into-modern-software-systems-analysis-dff3b0d2da8f)
- [@article@How to Evaluate Software Architecture: Methods and Tools](https://www.linkedin.com/advice/0/what-most-common-software-architecture-evaluation)

## Etl Datawarehouses

# ETL Datawarehouses

ETL (Extract, Transform, Load) is a key process in data warehousing, enabling the integration of data from multiple sources into a centralized database. The process begins by **extracting** data from original sources, followed by **transforming** it to ensure quality, deduplication, and combination, and finally **loading** it into the target database. ETL tools streamline this process, allowing companies to consolidate diverse data types and ensure seamless integration for effective data analysis and decision-making.

Visit the following resources to learn more:

- [@article@What is ETL?](https://www.snowflake.com/guides/what-etl)
- [@video@ETL Explained](https://www.youtube.com/watch?v=OW5OgsLpDCQ)
- [@feed@Explore top posts about ETL](https://app.daily.dev/tags/etl?ref=roadmapsh)

## Firewalls

# Firewalls

A Firewall is a network security device that monitors and filters incoming and outgoing network traffic based on an organization's previously established security policies. Firewalls usually sit between a trusted network and an untrusted network; oftentimes the untrusted network is the Internet. For example, office networks often use a firewall to protect their network from online threats.

Visit the following resources to learn more:

- [@article@What is a Firewall? - Cloudflare](https://www.cloudflare.com/learning/security/what-is-a-firewall/)
- [@article@Firewall - Cisco](https://www.cisco.com/site/us/en/learn/topics/security/what-is-a-firewall.html)

## Frameworks

# Architect Frameworks

Architect frameworks are tools that provide a structured approach to software architecture. They help architects organize their work, manage dependencies, and ensure consistency across projects. Some popular frameworks include:

Visit the following resources to learn more:

- [@article@Architect Frameworks](https://www.techtarget.com/searchapparchitecture/definition/enterprise-architecture-framework)
- [@article@Common Software Architecture Frameworks](https://medium.com/@publicapplicationcenter/tutorial-notes-common-software-architecture-frameworks-1a9915e1d806)

## Functional Programming

# Functional Programming

Functional programming is a programming paradigm designed to handle pure mathematical functions. This paradigm is totally focused on writing more compounded and pure functions.

Visit the following resources to learn more:

- [@article@Functional Programming](https://en.wikipedia.org/wiki/Functional_programming)
- [@article@Functional Programming with JavaScript](https://www.telerik.com/blogs/functional-programming-javascript)
- [@video@Learning Functional Programming](https://youtube.com/watch?v=e-5obm1G_FY)

## Git

# Git

Git is a distributed version control system designed to handle projects of any size with speed and efficiency. Created by Linus Torvalds in 2005, Git tracks changes in source code during software development, allowing multiple developers to work together on non-linear development. It provides strong support for branching, merging, and distributed development workflows. Git maintains a complete history of all changes, enabling easy rollbacks and comparisons between versions. Its distributed nature means each developer has a full copy of the repository, allowing for offline work and backup. Git's speed, flexibility, and robust branching and merging capabilities have made it the most widely used version control system in software development, particularly for open-source projects.

Visit the following resources to learn more:

- [@roadmap@Visit Dedicated Git & GitHub Roadmap](https://roadmap.sh/git-github)
- [@article@Git Cheat Sheet](https://cs.fyi/guide/git-cheatsheet)
- [@article@Tutorial: Git for Absolutely Everyone](https://thenewstack.io/tutorial-git-for-absolutely-everyone/)
- [@video@Git & GitHub Crash Course For Beginners](https://www.youtube.com/watch?v=SWYqp7iY_Tc)
- [@feed@Explore top posts about Git](https://app.daily.dev/tags/git?ref=roadmapsh)

## Github

# GitHub

GitHub has become a central hub for open-source projects and is widely used by developers, companies, and organizations for both private and public repositories. It was acquired by Microsoft in 2018 but continues to operate as a relatively independent entity. GitHub's popularity has made it an essential tool in modern software development workflows and a key platform for showcasing coding projects and contributing to open-source software.

Visit the following resources to learn more:

- [@roadmap@Visit Dedicated Git & GitHub Roadmap](https://roadmap.sh/git-github)
- [@official@GitHub](https://github.com)
- [@official@GitHub: Quickstart](https://docs.github.com/en/get-started/quickstart/hello-world)
- [@official@GitHub Documentation](https://docs.github.com/en/get-started/quickstart)
- [@official@Learn GitHub by doing](https://skills.github.com/)
- [@video@What is GitHub?](https://www.youtube.com/watch?v=w3jLJU7DT5E)
- [@feed@Explore top posts about GitHub](https://app.daily.dev/tags/github?ref=roadmapsh)

## Go

# Go

Go is an open source programming language supported by Google. Go can be used to write cloud services, CLI tools, used for API development, and much more.

Visit the following resources to learn more:

- [@roadmap@Visit Dedicated Go Roadmap](https://roadmap.sh/golang)
- [@official@A Tour of Go – Go Basics](https://go.dev/tour/welcome/1)
- [@official@Go Reference Documentation](https://go.dev/doc/)
- [@article@Go by Example - annotated example programs](https://gobyexample.com/)
- [@feed@Explore top posts about Golang](https://app.daily.dev/tags/golang?ref=roadmapsh)

## Graphql

# Graphql

GraphQL is a query language and runtime for APIs, developed by Facebook. GraphQL's flexibility and efficiency make it popular for building complex applications, especially those with diverse client requirements. It's particularly useful for mobile applications where bandwidth efficiency is crucial. While it requires a paradigm shift from REST, many developers and organizations find GraphQL's benefits outweigh the learning curve, especially for large-scale or rapidly evolving APIs.

Visit the following resources to learn more:

- [@roadmap@visit Dedicated GraphQL Roadmap](https://roadmap.sh/graphql)
- [@official@Introduction to GraphQL](https://graphql.org/learn/)
- [@article@Introduction to GraphQL](https://thenewstack.io/introduction-to-graphql/)
- [@article@How to Execute a Simple GraphQL Query](https://thenewstack.io/how-to-execute-a-simple-graphql-query/)
- [@video@GraphQL Course for Beginners](https://www.youtube.com/watch?v=ed8SzALpx1Q)
- [@feed@Explore top posts about GraphQL](https://app.daily.dev/tags/graphql?ref=roadmapsh)

## Grpc

# gRPC

gRPC is a platform agnostic serialization protocol that is used to communicate between services. Designed by Google in 2015, it is a modern alternative to REST APIs. It is a binary protocol that uses HTTP/2 as a transport layer. It is a high performance, open source, general-purpose RPC framework that puts mobile and HTTP/2 first.

It's main use case is for communication between two different languages within the same application. You can use Python to communicate with Go, or Java to communicate with C#. gRPC uses the protocol buffer language to define the structure of the data that is

Visit the following resources to learn more:

- [@official@gRPC Website](https://grpc.io/)
- [@official@gRPC Introduction](https://grpc.io/docs/what-is-grpc/introduction/)
- [@official@gRPC Core Concepts](https://grpc.io/docs/what-is-grpc/core-concepts/)
- [@video@Stephane Maarek - gRPC Introduction](https://youtu.be/XRXTsQwyZSU)
- [@feed@Explore top posts about gRPC](https://app.daily.dev/tags/grpc?ref=roadmapsh)

## Hadoop Spark Mapreduce

# Spark, Hadoop MapReduce

Spark is a data processing framework that can quickly perform processing tasks on very large data sets, and can also distribute data processing tasks across multiple computers, either on its own or in tandem with other distributed computing tools.

Hadoop MapReduce is a software framework for easily writing applications which process vast amounts of data (multi-terabyte data-sets) in-parallel on large clusters (thousands of nodes) of commodity hardware in a reliable, fault-tolerant manner.

Visit the following resources to learn more:

- [@official@Apache Spark](https://spark.apache.org/)
- [@article@Spark vs Hadoop MapReduce](https://www.integrate.io/blog/apache-spark-vs-hadoop-mapreduce)
- [@video@Hadoop explained in 5 minutes](https://www.youtube.com/watch?v=aReuLtY0YMI)
- [@feed@Explore top posts about Apache Spark](https://app.daily.dev/tags/spark?ref=roadmapsh)

## Hadoop

# Hadoop

The Apache Hadoop software library is a framework that allows for the distributed processing of large data sets across clusters of computers using simple programming models.

Visit the following resources to learn more:

- [@official@Apache Hadoop](https://hadoop.apache.org/)
- [@article@Apache Hadoop - Wikipedia](https://en.wikipedia.org/wiki/Apache_Hadoop)
- [@feed@Explore top posts about Apache Hadoop](https://app.daily.dev/tags/apache-hadoop?ref=roadmapsh)

## Hashing Algorithms

# Hashing Algorithms

Hashing algorithms are used to generate a unique value for a given input. This value is called a hash. Hashing algorithms are used to verify the integrity of data, to store passwords, and to generate unique identifiers for data.

Visit the following resources to learn more:

- [@article@What is Hashing?](https://www.codecademy.com/resources/blog/what-is-hashing/)
- [@video@Hashing Algorithms and Security - Computerphile](https://www.youtube.com/watch?v=b4b8ktEV4Bg)
- [@video@Top Hashing Algorithms In Cryptography | MD5 and SHA 256 Algorithms Expalined | Simplilearn](https://www.youtube.com/watch?v=Plp4F3ZfC7A)
- [@video@SHA: Secure Hashing Algorithm - Computerphile](https://www.youtube.com/watch?v=DMtFhACPnTY)
- [@feed@Explore top posts about Algorithms](https://app.daily.dev/tags/algorithms?ref=roadmapsh)

## How To Code

# How to Code

Even as an Enterprise Architect, staying connected to coding practices is essential to understand developers’ challenges and earn their trust. Maintaining a **side project** allows you to explore new technologies, tools, and methodologies hands-on, building practical experience beyond theoretical knowledge. This helps in forming informed decisions and keeping pace with evolving trends in development.

To prioritize what to explore, structured resources like ThoughtWorks’ Technology Radar can guide you. It categorizes technologies into **Adopt**, **Trial**, **Assess**, and **Hold**, helping architects focus on impactful and enterprise-ready innovations. Staying informed and involved ensures better collaboration and alignment with developers.

Visit the following resources to learn more:

- [@article@How to Code – Coding for Beginners and How to Learn Programming for Free](https://www.freecodecamp.org/news/how-to-code-coding-for-beginners-and-how-to-learn-programming-for-free/)
- [@article@Technology Radar](https://www.thoughtworks.com/radar)
- [@video@coding is easy, actually](https://www.youtube.com/watch?v=qkFYqY3vr84)

## Http Https

# Http Https

HTTP is the `TCP/IP` based application layer communication protocol which standardizes how the client and server communicate with each other. It defines how the content is requested and transmitted across the internet.

HTTPS (Hypertext Transfer Protocol Secure) is the secure version of HTTP, which is the primary protocol used to send data between a web browser and a website.

`HTTPS = HTTP + SSL/TLS`

Visit the following resources to learn more:

- [@article@What is HTTPS?](https://www.cloudflare.com/en-gb/learning/ssl/what-is-https/)
- [@article@What is HTTP?](https://www.cloudflare.com/en-gb/learning/ddos/glossary/hypertext-transfer-protocol-http/)
- [@article@Overview of HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview)
- [@article@Everything you need to know about HTTP](https://cs.fyi/guide/http-in-depth)
- [@article@HTTP/3 From A To Z: Core Concepts](https://www.smashingmagazine.com/2021/08/http3-core-concepts-part1/)
- [@article@Why HTTPS Matters](https://developers.google.com/web/fundamentals/security/encrypt-in-transit/why-https)
- [@article@Enabling HTTPS on Your Servers](https://developers.google.com/web/fundamentals/security/encrypt-in-transit/enable-https)
- [@video@HTTP Crash Course & Exploration](https://www.youtube.com/watch?v=iYM2zFP3Zn0)

## Iaf

# Iaf

The Integrated Architecture Framework (IAF) is an enterprise architecture framework that covers business, information, information system and technology infrastructure.

Visit the following resources to learn more:

- [@article@Wikipedia](https://en.wikipedia.org/wiki/Integrated_Architecture_Framework)
- [@article@IAF PDF](https://www.capgemini.com/wp-content/uploads/2018/03/architecture-for-the-information-age.pdf)

## Ibm Bpm

# IBM BPM

IBM BPM is a comprehensive business process management platform. It provides a robust set of tools to author, test, and deploy business processes, as well as full visibility and insight to managing those business processes.

Visit the following resources to learn more:

- [@official@Overview BPM](https://www.ibm.com/docs/en/bpm/8.5.5?topic=manager-business-process-overview)
- [@video@BPM Demo](https://www.youtube.com/watch?v=6yn4nCWMNLI)
- [@feed@Explore top posts about IBM](https://app.daily.dev/tags/ibm?ref=roadmapsh)

## Important Skills To Learn

# Important Skills

To support the laid-out activities specific skills are required. From my experience, read books and discussions we can boil this down to these ten skills every software architect should have:

*   Design
*   Decide
*   Simplify
*   Code
*   Document
*   Communicate
*   Estimate
*   Balance
*   Consult
*   Market

## Infrastructure As Code

# Infrastructure as Code

Sometimes referred to as IaC, this section refers to the techniques and tools used to define infrastructure, typically in a markup language like YAML or JSON. Infrastructure as code allows DevOps Engineers to use the same workflows used by software developers to version, roll back, and otherwise manage changes.

The term Infrastructure as Code encompasses everything from bootstrapping to configuration to orchestration, and it is considered a best practice in the industry to manage all infrastructure as code. This technique precipitated the explosion in system complexity seen in modern DevOps organizations.

Visit the following resources to learn more:

- [@article@What is Infrastructure as Code](https://www.redhat.com/en/topics/automation/what-is-infrastructure-as-code-iac)
- [@article@GUIs, CLI, APIs: Learn Basic Terms of Infrastructure-as-Code](https://thenewstack.io/guis-cli-apis-learn-basic-terms-of-infrastructure-as-code/)
- [@video@What is Infrastructure as Code?](https://www.youtube.com/watch?v=zWw2wuiKd5o)
- [@video@What is Infrastructure as Code? Difference of Infrastructure as Code Tools](https://www.youtube.com/watch?v=POPP2WTJ8es)
- [@video@Introduction to Infrastructure as Code](https://www.youtube.com/watch?v=zWw2wuiKd5o)
- [@feed@Explore top posts about Infrastructure](https://app.daily.dev/tags/infrastructure?ref=roadmapsh)

## Itil

# ITIL

**ITIL (Information Technology Infrastructure Library)** is a set of best practices for IT service management, designed to align IT services with business needs. Its primary focus is the efficient and effective delivery of value through managing the IT service lifecycle, which includes five phases: `Strategy`, `Design`, `Transition`, `Operation`, and `Continual Service Improvement`. ITIL includes key processes such as incident management, problem management, change management, configuration management, and service level agreements (SLAs). These practices aim to optimize performance, service quality, and customer satisfaction. Adopting ITIL helps organizations improve operational efficiency, reduce risks, and maintain clear control over IT services over time.

Visit the following resources to learn more:

- [@official@ITIL Documentation](https://www.axelos.com/certifications/itil-service-management/itil-4-foundation)
- [@video@What is ITIL?](https://www.youtube.com/watch?v=wgnpfMK8vDk)

## Java  Kotlin  Scala  Swift

# Java/Kotlin/Scala

*   **Java**: Java is a widely-used, object-oriented programming language known for its platform independence, reliability, and scalability. It’s commonly used for building large-scale enterprise applications, Android development, and web services. Java’s extensive libraries, frameworks, and strong community support make it a popular choice for developers.
    
*   **Scala**: Scala is a statically-typed programming language that combines object-oriented and functional programming paradigms. It runs on the Java Virtual Machine (JVM) and is known for its concise syntax, expressive power, and compatibility with Java. Scala is often used in data engineering, backend services, and applications requiring high concurrency.
    
*   **Kotlin**: Kotlin is a modern, statically-typed programming language designed to be fully interoperable with Java while offering more concise and expressive syntax. It is particularly popular for Android development due to its simplicity and safety features, such as null safety, and is gaining traction in backend development as well.

Visit the following resources to learn more:

- [@roadmap@Visit Dedicated Java Roadmap](https://roadmap.sh/java)
- [@official@Java](https://www.java.com/)
- [@roadmap@Visit Dedicated Kotlin Roadmap](https://roadmap.sh/kotlin)
- [@official@Kotlin](https://kotlinlang.org/)
- [@official@Scala Documentation](https://docs.scala-lang.org/)
- [@official@Swift Docs](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/guidedtour)
- [@article@Explore top posts about Java](https://app.daily.dev/tags/java?ref=roadmapsh)

## Javascript  Typescript

# JavaScript

JavaScript allows you to add interactivity to your pages. Common examples that you may have seen on the websites are sliders, click interactions, popups and so on. Apart from being used on the frontend in browsers, there is Node.js which is an open-source, cross-platform, back-end JavaScript runtime environment that runs on the V8 engine and executes JavaScript code outside a web browser. TypeScript adds optional types to JavaScript that support tools for large-scale JavaScript applications for any browser, for any host, on any OS. TypeScript compiles to readable, standards-based JavaScript.

Visit the following resources to learn more:

- [@roadmap@Visit Dedicated JavaScript Roadmap](https://roadmap.sh/javascript)
- [@roadmap@Visit Dedicated TypedScript Roadmap](https://roadmap.sh/typescript)
- [@official@TypeScript](https://www.typescriptlang.org/)
- [@official@TypeScript Docs for Deep Dives](https://www.typescriptlang.org/docs/)
- [@article@The Modern JavaScript Tutorial](https://javascript.info/)
- [@video@JavaScript Crash Course for Beginners](https://youtu.be/hdI2bqOjy3c)
- [@video@Node.js Crash Course](https://www.youtube.com/watch?v=fBNz5xF-Kx4)
- [@video@Node.js Tutorial for Beginners](https://www.youtube.com/watch?v=TlB_eWDSMt4)
- [@video@TypeScript for Beginners](https://www.youtube.com/watch?v=BwuLxPH8IDs)
- [@feed@Explore top posts about JavaScript](https://app.daily.dev/tags/javascript?ref=roadmapsh)

## Kanban

# Kanban

`Kanban` is a popular agile methodology that focuses on visualizing workflow and continuously improving that flow. It's a more flexible approach than Scrum, without the rigid framework.

Visit the following resources to learn more:

- [@article@What Is Kanban? A Simple Guide to Improve Efficiency.](https://businessmap.io/kanban-resources/getting-started/what-is-kanban)
- [@article@Kanban Methodology: The Simplest Agile Framework ](https://kissflow.com/project/agile/kanban-methodology/)
- [@article@What is Kanban Methodology? The Ultimate Guide](https://www.wrike.com/kanban-guide/what-is-kanban/)

## Layered

# Layered Architecture

Layered architecture is a software design pattern where an application is divided into distinct layers, each with a specific responsibility, such as presentation, business logic, and data access. This approach promotes modularity, easier maintenance, testing, and component reusability. The most common implementation is the three-tier architecture, which separates concerns between the user interface, business rules, and data handling. However, it can introduce complexity, performance issues, tight coupling, and overhead if not carefully implemented. Despite these challenges, layered architecture is widely used in scalable and maintainable systems, particularly in enterprise applications.

Visit the following resources to learn more:

- [@article@Wikipedia](https://en.wikipedia.org/wiki/Layered_architecture)

## Less

# Less

**LeSS** (Large-Scale-Scrum) is an agile framework designed to scale Scrum across multiple teams working on a single product. It adheres to Scrum's principles, emphasizing simplicity and continuous improvement. LeSS encourages coordination between teams by using a single backlog and a common Product Owner. Each team is responsible for parts of the product, but they collaborate in its joint development, with frequent feedback loops to adjust project direction. Its goal is to minimize bureaucracy and maximize value delivery in an agile and efficient way.

Visit the following resources to learn more:

- [@official@LeSS Framework](https://less.works/less/framework)
- [@video@Introduction to LeSS](https://www.youtube.com/watch?v=1BZf_Oa7W94)

## Levels Of Architecture

# Levels of Architecture

Architecture can be done on several “levels” of abstractions. The level influences the importance of necessary skills. As there are many categorizations possible my favorite segmentation includes these 3 levels:

*   **Application Level:** The lowest level of architecture. Focus on one single application. Very detailed, low level design. Communication is usually within one development team.
*   **Solution Level:** The mid-level of architecture. Focus on one or more applications which fulfill a business need (business solution). Some high, but mainly low-level design. Communication is between multiple development teams.
*   **Enterprise Level:** The highest level of architecture. Focus on multiple solutions. High level, abstract design, which needs to be detailed out by solution or application architects. Communication is across the organization.

## Linux  Unix

# Linux / Unix

Knowledge of UNIX is a must for almost all kind of development as most of the codes that you write is most likely going to be finally deployed on a UNIX/Linux machine. Linux has been the backbone of the free and open source software movement, providing a simple and elegant operating system for almost all your needs.

Visit the following resources to learn more:

- [@roadmap@Visit Dedicated Linux Roadmap](https://roadmap.sh/linux)
- [@course@Coursera - Unix Courses](https://www.coursera.org/courses?query=unix)
- [@article@Unix & Linux Tutorial](https://www.tutorialspoint.com/unix/index.htm)
- [@article@Linux Basics ](https://dev.to/rudrakshi99/linux-basics-2onj)
- [@video@Linux Operating System - Crash Course](https://www.youtube.com/watch?v=ROjZy1WbCIA)
- [@feed@Explore top posts about Linux](https://app.daily.dev/tags/linux?ref=roadmapsh)

## Management

# Management

Management in software architects encompasses various responsibilities and practices that ensure the successful design, development, and implementation of software systems. Software architects play a critical role in bridging the gap between business requirements and technical implementation.

Visit the following resources to learn more:

- [@article@Wikipedia](https://en.wikipedia.org/wiki/Management)

## Marketing Skills

# Marketing Skills

Marketing skills are essential for promoting your ideas effectively, especially when others may not immediately embrace them. To convince others, it's crucial to motivate them by demonstrating the value and benefits of your ideas in an easily digestible format, such as through prototypes or videos. Persistence is key; if you're convinced of your idea’s worth, you need to fight for it, even if it's met with resistance. Establishing allies who support your ideas can also make it easier to gain traction, so start building a network. Repeating your message regularly can help, but be cautious not to overdo it, as credibility is essential for long-term success.

Visit the following resources to learn more:

- [@article@Marketing Skills for Architects](https://openasset.com/blog/marketing-for-architects/)

## Messaging Queues

# Messaging queues

Message queuing makes it possible for applications to communicate asynchronously, by sending messages to each other via a queue. A message queue provides temporary storage between the sender and the receiver so that the sender can keep operating without interruption when the destination program is busy or not connected.

Visit the following resources to learn more:

- [@article@Messaging Queues](https://aws.amazon.com/message-queue/)
- [@article@Messaging Queues Tutorial](https://www.tutorialspoint.com/inter_process_communication/inter_process_communication_message_queues.htm)

## Microfrontends

# Microfrontends

Microfrontends is an architectural style where independently deliverable frontend applications built by different teams using different technologies are composed into a greater whole. Simply, a Micro-Frontend is a portion of a webpage (not the entire page). There is a “Host” or a “Container” page in the Micro-Frontend Architecture page that can host one or more Micro-Frontends.

Visit the following resources to learn more:

- [@article@Micro Frontends](https://micro-frontends.org/)
- [@video@Micro-Frontends Course - Beginner to Expert](https://www.youtube.com/watch?v=lKKsjpH09dU)
- [@feed@Explore top posts about Web Development](https://app.daily.dev/tags/webdev?ref=roadmapsh)

## Microservices

# Microservices

Microservice architecture is a pattern in which highly cohesive, loosely coupled services are separately developed, maintained, and deployed. Each component handles an individual function, and when combined, the application handles an overall business function.

Visit the following resources to learn more:

- [@official@Pattern: Microservice Architecture](https://microservices.io/patterns/microservices.html)
- [@article@What is Microservices?](https://smartbear.com/solutions/microservices/)
- [@article@Microservices 101](https://thenewstack.io/microservices-101/)
- [@article@Primer: Microservices Explained](https://thenewstack.io/primer-microservices-explained/)
- [@article@Articles about Microservices](https://thenewstack.io/category/microservices/)
- [@feed@Explore top posts about Microservices](https://app.daily.dev/tags/microservices?ref=roadmapsh)

## Ms Dynamics

# MS Dynamics

Microsoft Dynamics 365 is a combination of both Enterprise Resource Planning (ERP) software and Customer Relationship Management (CRM) software.

Visit the following resources to learn more:

- [@article@Everything you ever wanted to know about Microsoft Dynamics](https://www.nigelfrank.com/insights/everything-you-ever-wanted-to-know-about-dynamics-crm)
- [@video@What is Microsoft Dynamics?](https://www.youtube.com/watch?v=ogfclHWgqgE)

## Mvc Mvp Mvvm

# MVC MVP MVVM

Model-view-controller, or MVC, is a pattern used to separate user-interface, data and application logic. It does this by separating an application into three parts: Model, View, and Controller. The model holds the data, the view encompasses the user-interface, and the controller acts as a mediator between the two.

Model-view-presenter, or MVP, was designed to ease automated unit testing and improve the separation of concerns in presentation logic. MVP is a variant of the MVC pattern, though differs in that it divides the application into the user-interface (view), data (model) and presentation logic (presenter). While the model and the view represent stay the same as in the model-view-controller pattern, the presenter differs from the controller in that it manipulates the model and updates the view.

Another variant of the MVC is the model-view-viewmodel pattern. The Model-view-viewmodel, or MVVM, separates the application into three core components: Model, View, and View Model. While the view and model represent all that they did in their parent pattern, the view model acts as a link between the model and view, retrieves data from the model and exposes it to the view through two-way data binding and can manipulate the model's data.

Visit the following resources to learn more:

- [@article@MVC, MVP and MVVM Design Pattern](https://medium.com/@ankit.sinhal/mvc-mvp-and-mvvm-design-pattern-6e169567bbad)
- [@feed@Explore top posts about General Programming](https://app.daily.dev/tags/general-programming?ref=roadmapsh)

## Net Framework Based

# .NET Framework

.NET is an open-source platform with tools and libraries for building web, mobile, desktop, games, IoT, cloud, and microservices.

Officially supported languages in .NET: C#, F#, Visual Basic.

Visit the following resources to learn more:

- [@official@.NET Website](https://dotnet.microsoft.com/en-us/)
- [@official@What is .NET?](https://dotnet.microsoft.com/en-us/learn/dotnet/what-is-dotnet)
- [@official@Why Choose .NET?](https://dotnet.microsoft.com/en-us/platform/why-choose-dotnet)
- [@official@C# Documentation](https://learn.microsoft.com/en-us/dotnet/csharp/?WT.mc_id=dotnet-35129-website)
- [@official@F# Documentation](https://learn.microsoft.com/en-us/dotnet/fsharp/?WT.mc_id=dotnet-35129-website)
- [@official@Visual Basic Documentation](https://learn.microsoft.com/en-us/dotnet/visual-basic/?WT.mc_id=dotnet-35129-website)
- [@feed@Explore top posts about .NET](https://app.daily.dev/tags/.net?ref=roadmapsh)

## Networks

# Networks

A computer network is a set of computers sharing resources located on or provided by network nodes. Computers use common communication protocols over digital interconnections to communicate with each other. These interconnections are made up of telecommunication network technologies based on physically wired, optical, and wireless radio-frequency methods that may be arranged in a variety of network topologies.

Visit the following resources to learn more:

- [@article@Networking - IBM](https://www.ibm.com/topics/networking)
- [@article@Networking - Wikipedia](https://en.wikipedia.org/wiki/Networking)
- [@article@Networking Basics](https://www.cisco.com/c/en/us/solutions/small-business/resource-center/networking/networking-basics.html)

## Nosql Databases

# Nosql databases

NoSQL databases (aka "not only SQL") are non-tabular databases and store data differently than relational tables. NoSQL databases come in a variety of types based on their data model. The main types are document, key-value, wide-column, and graph. They provide flexible schemas and scale easily with large amounts of data and high user loads.

Types of NoSQL databases

*   Document databases Ex. MongoDB
*   Key-value databases Ex. Redis
*   Wide-column databases Ex. Cassandra
*   Graph databases Ex. Neo4J

Visit the following resources to learn more:

- [@article@NoSQL Database - AWS](https://aws.amazon.com/nosql/)
- [@article@NoSQL Databases](https://www.mongodb.com/resources/basics/databases/nosql-explained)
- [@feed@Explore top posts about NoSQL](https://app.daily.dev/tags/nosql?ref=roadmapsh)

## Oop

# OOP

Object-oriented programming (OOP) is a computer programming model that organizes software design around data, or objects, rather than functions and logic. An object can be defined as a data field that has unique attributes and behavior.

Visit the following resources to learn more:

- [@article@OOP - Wikipedia](https://en.wikipedia.org/wiki/Object-oriented_programming)
- [@article@Basic Concepts of Object-Oriented Programming](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Object-oriented_programming)
- [@video@FreeCodeCamp - (OOP) in C++](https://www.youtube.com/watch?v=wN0x9eZLix4)
- [@video@FreeCodeCamp - (OPP) in Python](https://www.youtube.com/watch?v=Ej_02ICOIgs)

## Operations Knowledge

# Operations Knowledge

Operational knowledge refers to the understanding and insights that software architects need to effectively design, implement, and manage software systems throughout their lifecycle. This knowledge encompasses various aspects of software development, deployment, and maintenance, and it is crucial for ensuring that systems operate efficiently, reliably, and securely.

## Osi

# OSI and TCP/IP Models

The OSI and TCP/IP model is used to help the developer to design their system for interoperability. The OSI model has 7 layers while the TCP/IP model has a more summarized form of the OSI model only consisting 4 layers. This is important if you're trying to design a system to communicate with other systems.

Visit the following resources to learn more:

- [@article@Cloudflare - What is the OSI model](https://www.cloudflare.com/learning/ddos/glossary/open-systems-interconnection-model-osi/)

## Owasp

# OWASP

OWASP or Open Web Application Security Project is an online community that produces freely-available articles, methodologies, documentation, tools, and technologies in the field of web application security.

Visit the following resources to learn more:

- [@opensource@OWASP Web Application Security Testing Checklist](https://github.com/0xRadi/OWASP-Web-Checklist)
- [@article@Wikipedia - OWASP](https://en.wikipedia.org/wiki/OWASP)
- [@article@OWASP Top 10 Security Risks](https://sucuri.net/guides/owasp-top-10-security-vulnerabilities-2021/)
- [@article@OWASP Cheatsheets](https://cheatsheetseries.owasp.org/cheatsheets/AJAX_Security_Cheat_Sheet.html)

## Patterns  Design Principles

# Patterns and design principles

In the realm of software architecture, patterns and design principles are foundational tools that enable architects to create robust, scalable, and maintainable systems. They offer proven solutions to common problems and guide decision-making throughout the software development lifecycle. Understanding these concepts is essential for anyone following a software architect roadmap, as they bridge the gap between high-level architecture and practical implementation.

## Pki

# PKI

A public key infrastructure (PKI) is a set of roles, policies, hardware, software, and procedures to create, manage, distribute, use, store and revoke digital certificates and public-key encryption. The purpose of a PKI is to facilitate the secure electronic transfer of information for a range of network activities such as e-commerce, internet banking, and confidential email. It is required for activities where simple passwords are an inadequate authentication method, and the more rigorous proof is required to confirm the identity of the parties involved in the communication and to validate the information being transferred.

Visit the following resources to learn more:

- [@article@PKI - Wikipedia](https://en.wikipedia.org/wiki/Public_key_infrastructure)
- [@article@PKI - DoD Cyber Exchange](https://public.cyber.mil/pki-pke/)

## Pmi

# PMI

The PMI certification (Project Management Institute) is an internationally recognized credential in project management. The most well-known is the PMP® (Project Management Professional), which validates the skills and knowledge of professionals to manage projects effectively by applying best practices and standards defined in the PMBOK® (Project Management Body of Knowledge) guide.

Visit the following resources to learn more:

- [@official@Project Management Institute](https://www.pmi.org/)

## Prince2

# Prince2

Prince2 is a structured project management method and practitioner certification programme. Prince2 emphasizes dividing projects into manageable and controllable stages. It is adopted in many countries worldwide, including the UK, Western European countries, and Australia.

Visit the following resources to learn more:

- [@course@Prince2 Project Management Course](https://www.simplilearn.com/project-management/prince2-foundation-and-practitioner-certification-training)
- [@official@Prince2 Certification](https://www.axelos.com/certifications/propath/prince2-project-management)

## Programming Languages

# Programming Languages

A programming language is a system of notation for writing computer programs. Programming languages are described in terms of their syntax and semantics, usually defined by a formal language. Languages usually provide features such as a type system, variables, and mechanisms for error handling.

Visit the following resources to learn more:

- [@article@Programming Language](https://en.wikipedia.org/wiki/Programming_language)

## Proxies

# Proxies

In computer networking, a proxy server is a server application that acts as an intermediary between a client requesting a resource and the server providing that resource.

Visit the following resources to learn more:

- [@article@Proxy Server](https://en.wikipedia.org/wiki/Proxy_server)

## Python

# Python

Python is a multi-paradigm language. Being an interpreted language, code is executed as soon as it is written and the Python syntax allows for writing code in functional, procedural or object-oriented programmatic ways. Python is frequently recommended as the first language new coders should learn, because of its focus on readability, consistency, and ease of use. This comes with some downsides, as the language is not especially performant in most production tasks.

Visit the following resources to learn more:

- [@roadmap@Visit Dedicated Python Roadmap](https://roadmap.sh/python)
- [@official@Python Website](https://www.python.org/)
- [@official@Python Getting Started](https://www.python.org/about/gettingstarted/)
- [@article@Automate the Boring Stuff](https://automatetheboringstuff.com/)
- [@article@Python Crash Course](https://ehmatthes.github.io/pcc/)
- [@feed@Explore top posts about Python](https://app.daily.dev/tags/python?ref=roadmapsh)

## React Vue Angular

# React

React is the most popular front-end JavaScript library for building user interfaces. React can also render on the server using Node and power mobile apps using React Native.

Vue.js is a progressive JavaScript framework designed for building user interfaces and single-page applications.

Angular is a TypeScript-based open-source front-end web application framework led by the Angular Team at Google.

Visit the following resources to learn more:

- [@roadmap@Visit Dedicated React Roadmap](https://roadmap.sh/react)
- [@roadmap@Visit Dedicated Vue Roadmap](https://roadmap.sh/vue)
- [@roadmap@Visit Dedicated Angular Roadmap](https://roadmap.sh/angular)
- [@official@React](https://react.dev/)
- [@official@Vue.js](https://vuejs.org/)
- [@official@Angular](https://angular.dev/)
- [@video@React JS Course for Beginners](https://www.youtube.com/watch?v=nTeuhbP7wdE)
- [@video@Vue.js Course for Beginners](https://www.youtube.com/watch?v=FXpIoQ_rT_c)
- [@video@Angular Course for Beginners](https://www.youtube.com/watch?v=3qBXWUpoPHo)
- [@feed@Explore top posts about Angular](https://app.daily.dev/tags/angular?ref=roadmapsh)

## Reactive Programming

# Reactive Programming

Reactive programming describes a design paradigm that relies on asynchronous programming logic to handle real-time updates to otherwise static content. It provides an efficient means -- the use of automated data streams -- to handle data updates to content whenever a user makes an inquiry.

Visit the following resources to learn more:

- [@article@What is Reactive Programming?](https://www.techtarget.com/searchapparchitecture/definition/reactive-programming)

## Responsibilities

# Architect Responsibilities

To understand the necessary skills an architect needs, we first need to understand typical activities. The following list contains from my perspective the most important activities:

*   Define and decide development technology and platform
*   Define development standards, e.g., coding standards, tools, review processes, test approach, etc.
*   Support identifying and understanding business requirements
*   Design systems and take decisions based on requirements
*   Document and communicate architectural definitions, design and decisions
*   Check and review architecture and code, e.g., check if defined patterns and coding standards are implemented properly
*   Collaborate with other architects and stakeholders
*   Coach and consult developers
*   Make sure that as implementation takes place, the architecture is being adhered to
*   Play a key part in reviewing code
*   Detail out and refine higher level design into lower level design

Visit the following resources to learn more:

- [@article@Software Architect](https://en.wikipedia.org/wiki/Software_architect)

## Rest

# REST

REST, or REpresentational State Transfer, is an architectural style for providing standards between computer systems on the web, making it easier for systems to communicate with each other.

Visit the following resources to learn more:

- [@article@What is a REST API?](https://www.redhat.com/en/topics/api/what-is-a-rest-api)
- [@article@Roy Fieldings dissertation chapter, Representational State Transfer (REST)](https://www.ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm)
- [@article@Learn REST: A RESTful Tutorial](https://restapitutorial.com/)
- [@feed@Explore top posts about REST API](https://app.daily.dev/tags/rest-api?ref=roadmapsh)

## Ruby

# Ruby

Ruby is a high-level, interpreted programming language that blends Perl, Smalltalk, Eiffel, Ada, and Lisp. Ruby focuses on simplicity and productivity along with a syntax that reads and writes naturally. Ruby supports procedural, object-oriented and functional programming and is dynamically typed.

Visit the following resources to learn more:

- [@official@Ruby](https://www.ruby-lang.org/en/)
- [@official@Learn Ruby in 20 minutes](https://www.ruby-lang.org/en/documentation/quickstart/)
- [@feed@Explore top posts about Ruby](https://app.daily.dev/tags/ruby?ref=roadmapsh)

## Rup

# RUP

The RUP (**Rational Unified Process**) is not a widely recognized certification like PMP or Scrum, but rather a software development framework created by Rational Software (now IBM). It follows an iterative and incremental approach to project development, based on best practices for delivering high-quality software on time and within budget.

Visit the following resources to learn more:

- [@official@IBM Certified Solution Designer RUP](https://www.ibm.com/training/certification/ibm-certified-solution-designer-ibm-rational-unified-process-v70-38008003)

## Safe

# SAFe

**SAFe** is an agile framework designed to scale agile practices in large and complex organizations. Unlike LeSS, SAFe is more structured and provides a formal approach to coordinating multiple teams, programs, and portfolios. It incorporates elements of `Lean`, `DevOps`, and `agile principles`, and defines additional roles, ceremonies, and artifacts to align teams' goals with the business strategy. SAFe enables **large-scale planning**, **continuous delivery**, and **improvement of organizational efficiency**, offering a comprehensive framework for agile transformation at the corporate level.

Visit the following resources to learn more:

- [@official@SAFe 6.0](https://scaledagileframework.com/SAFE)
- [@video@SAFe explained in five minutes](https://www.youtube.com/watch?v=aW2m-BtCJyE&t=2s)

## Salesforce

# Salesforce

Salesforce is a cloud platform helping companies to manage relationships with their customers

Visit the following resources to learn more:

- [@article@What is Salesforce and what is it used for?](https://ascendix.com/blog/what-is-salesforce-what-salesforce-is-used-for/)
- [@video@What is Salesforce?](https://www.youtube.com/watch?v=xx2sK-QiBjw)
- [@feed@Explore top posts about Salesforce](https://app.daily.dev/tags/salesforce?ref=roadmapsh)

## Sap Erp Hana Business Objects

# SAP ERP, HANA, Business Objects

SAP (Systems, Applications, and Products in Data Processing) is a leading enterprise resource planning (ERP) software provider that helps organizations manage their business operations and customer relations effectively. SAP ERP integrates various business processes, such as finance, sales, procurement, and human resources, into a unified system, enabling real-time data access and improved decision-making. SAP HANA (High-Performance Analytic Appliance) is an in-memory database and application development platform that allows businesses to process large volumes of data quickly and efficiently, supporting advanced analytics and real-time reporting. BusinessObjects, part of the SAP Business Intelligence suite, provides powerful tools for data visualization, reporting, and analysis, enabling users to transform raw data into actionable insights. Together, these solutions empower organizations to streamline operations, enhance productivity, and drive strategic decision-making through data-driven insights.

Visit the following resources to learn more:

- [@official@SAP](https://www.sap.com/)

## Scrum

# Scrum

`Scrum` is a popular agile framework used for project management, particularly in software development. It emphasizes iterative development, collaboration, and flexibility to deliver high-quality products.

Key elements of Scrum:

*   **Sprints**: Time-boxed iterations (usually 2-4 weeks) where teams work on specific goals.
*   **Product Backlog**: Prioritized list of features or requirements for the product.
*   **Sprint Backlog**: Selected items from the Product Backlog to be completed during a Sprint.
*   **Daily Scrum (Stand-up)**: Brief daily meeting where team members share progress, challenges, and plans for the day.
*   **Sprint Review**: Meeting at the end of a Sprint to demonstrate completed work and gather feedback.
*   **Sprint Retrospective**: Meeting to reflect on the Sprint, identify improvements, and adjust processes for the next Sprint.

Visit the following resources to learn more:

- [@article@What is Scrum and How to Get Started](https://www.atlassian.com/agile/scrum.)
- [@article@Scrum Methodology: The Complete Guide & Best Practices](https://thedigitalprojectmanager.com/projects/pm-methodology/scrum-methodology-complete-guide/)
- [@article@Essential Topics for the Scrum Product Owner](https://www.scrum.org/resources/blog/essential-topics-scrum-product-owner)
- [@article@Scrum • Topics - Thriving Technologist](https://thrivingtechnologist.com/topics/scrum/)

## Security

# Security

Security is a broad field that encompasses various measures and practices designed to protect information, systems, and networks from unauthorized access, damage, or theft. It is essential in safeguarding sensitive data and maintaining the integrity and availability of resources.

Visit the following resources to learn more:

- [@article@Security - Wikipedia](https://en.wikipedia.org/wiki/Security)
- [@article@Architect Security](https://aws.amazon.com/blogs/architecture/lets-architect-security-in-software-architectures/)

## Serverless Concepts

# Serverless Concepts

Serverless is a cloud-native development model that allows developers to build and run applications without having to manage servers. There are still servers in serverless, but they are abstracted away from app development. A cloud provider handles the routine work of provisioning, maintaining, and scaling the server infrastructure. Developers can simply package their code in containers for deployment.

Visit the following resources to learn more:

- [@article@What is Serverless?](https://www.redhat.com/en/topics/cloud-native-apps/what-is-serverless)
- [@article@What is Serverless Computing?](https://www.cloudflare.com/learning/serverless/what-is-serverless/)
- [@article@Serverless on AWS](https://aws.amazon.com/serverless/)
- [@feed@Explore top posts about Serverless](https://app.daily.dev/tags/serverless?ref=roadmapsh)

## Serverless

# Serverless

Serverless architecture (also known as serverless computing or function as a service, FaaS) is a software design pattern where applications are hosted by a third-party service, eliminating the need for server software and hardware management by the developer. Applications are broken up into individual functions that can be invoked and scaled individually.

Visit the following resources to learn more:

- [@article@Serverless Architectures By AWS](https://aws.amazon.com/lambda/serverless-architectures-learn-more/)
- [@article@Serverless in Detail](https://martinfowler.com/articles/serverless.html)
- [@feed@Explore top posts about Serverless](https://app.daily.dev/tags/serverless?ref=roadmapsh)

## Service Mesh

# Service Mesh

A Service Mesh is a dedicated infrastructure layer for handling service-to-service communication. It’s responsible for the reliable delivery of requests through the complex topology of services that comprise a modern, cloud native application. In layman's terms, it's a tool which helps you to control how different services communicate with each other.

Visit the following resources to learn more:

- [@article@Red Hat - What is a Service Mesh?](https://www.redhat.com/en/topics/microservices/what-is-a-service-mesh)
- [@article@Kubernetes Service Mesh - Blog Post](https://platform9.com/blog/kubernetes-service-mesh-a-comparison-of-istio-linkerd-and-consul/)
- [@video@Service Mesh explained in 15 Minutes](https://youtu.be/16fgzklcF7Y)
- [@feed@Explore top posts about Service Mesh](https://app.daily.dev/tags/service-mesh?ref=roadmapsh)

## Service Oriented

# Service oriented

Service-oriented architecture (SOA) is an enterprise-wide approach to software development of application components that takes advantage of reusable software components, or services.

SOA provides four different service types:

1.  Functional services (i.e., business services), which are critical for business applications.
2.  Enterprise services, which serve to implement functionality.
3.  Application services, which are used to develop and deploy apps.
4.  Infrastructure services, which are instrumental for backend processes like security and authentication.

Visit the following resources to learn more:

- [@article@SOA Architecture By AWS](https://aws.amazon.com/what-is/service-oriented-architecture/)

## Simplifying Things

# Simplifying Things

Simplifying solutions is critical for effective problem-solving, aligning with Occam’s Razor, which favors simplicity by reducing unnecessary assumptions. To achieve this, “shake” your solution by analyzing it from different perspectives and questioning its assumptions. After complex discussions, take a step back to review the big picture and refactor if needed, giving your brain time to process ideas. Apply the _divide and conquer_ method to break problems into smaller parts and validate their integration afterward. Finally, remember that refactoring is a valuable process to improve overly complex solutions, provided there’s adequate test coverage and stakeholder support.

Visit the following resources to learn more:

- [@article@Simplifying Things](https://www.infoq.com/articles/driving-architectural-simplicity/)

## Slack

# Slack

Slack is a messaging app for business that connects people to the information that they need. By bringing people together to work as one unified team, Slack transforms the way that organisations communicate.

Visit the following resources to learn more:

- [@official@Slack](https://slack.com)
- [@official@Getting Started with Slack](https://slack.com/intl/en-in/help/categories/360000049043)
- [@video@What is Slack?](https://www.youtube.com/watch?v=q19RtuCHt1Q)
- [@feed@Explore top posts about Slack](https://app.daily.dev/tags/slack?ref=roadmapsh)

## Solid

# SOLID

SOLID is a set of principles applied to object-oriented design (OOD) to create maintainable, understandable, and flexible code, while avoiding code smells and defects. The principles are:

*   Single Responsibility
*   Open/Closed
*   Liskov Substitution
*   Interface Segregation
*   Dependency Inversion

Visit the following resources to learn more:

- [@article@SOLID Principles](https://www.baeldung.com/solid-principles)
- [@article@SOLID: The First 5 Principles of Object Oriented Design](https://www.digitalocean.com/community/conceptual_articles/s-o-l-i-d-the-first-five-principles-of-object-oriented-design)

## Solution Architecture

# Solution Level Architecture

The mid-level of architecture. Focus on one or more applications which fulfill a business need (business solution). Some high, but mainly low-level design. Communication is between multiple development teams.

Visit the following resources to learn more:

- [@article@Solution Architecture](https://www.leanix.net/en/wiki/it-architecture/solution-architecture)

## Spa Ssr Ssg

# SPA vs SSG vs SSR

*   **SPA**: A single page application loads only a single web document from the server and then updates the content of that document on demand via `Javascript APIs` without reloading the entire document. React, Vue, Angular are the top frameworks used to create single page applications.
*   **SSR**: This technique uses a server like `Node.js` to fully render the web document upon the receival of a request and then send it back to the client. This way the user get an interactive document with all the necessary information without having to wait for any JavaScript or CSS files to load.
*   **SSG**: Static site generation renders the web document in the server(like SSR), however the page is rendered at **build time**. So, instead of rendering the page on the server upon the receival of a request, the page is already rendered in the server, waiting to be served to the client.

Visit the following resources to learn more:

- [@article@Web Design Patterns — SSR, SSG, and SPA](https://medium.com/codex/web-design-patterns-ssr-ssg-and-spa-fadad7673dfe)
- [@article@Rendering on the Web](https://web.dev/rendering-on-the-web/)
- [@feed@Explore top posts about Web Development](https://app.daily.dev/tags/webdev?ref=roadmapsh)

## Sql Databases

# Sql databases

SQL stands for Structured Query Language. It's used for relational databases. A SQL database is a collection of tables that stores a specific set of structured data. Examples of SQL Databases includes MariaDB, MySQL and PostgreSQL.

Visit the following resources to learn more:

- [@roadmap@Visit Dedicated SQL Roadmap](https://roadmap.sh/sql)
- [@article@What is SQL? - AWS](https://aws.amazon.com/what-is/sql/)
- [@article@SQL Databases](https://www.openlogic.com/blog/what-sql-database)
- [@feed@Explore top posts about SQL](https://app.daily.dev/tags/sql?ref=roadmapsh)

## Tcpip Model

# TCP/IP Model

The `TCP/IP model` defines how devices should transmit data between them and enables communication over networks and large distances. The model represents how data is exchanged and organized over networks. It is split into four layers, which set the standards for data exchange and represent how data is handled and packaged when being delivered between applications, devices, and servers.

*   **Network Access Layer**: The network access layer is a group of applications requiring network communications. This layer is responsible for generating the data and requesting connections.
    
*   **Internet Layer**: The internet layer is responsible for sending packets from a network and controlling their movement across a network to ensure they reach their destination.
    
*   **Transport Layer**: The transport layer is responsible for providing a solid and reliable data connection between the original application or device and its intended destination.
    
*   **Application Layer**: The application layer refers to programs that need TCP/IP to help them communicate with each other.

Visit the following resources to learn more:

- [@article@What is Transmission Control Protocol TCP/IP? - Fortinet](https://www.fortinet.com/resources/cyberglossary/tcp-ip#:~:text=The%20TCP%2FIP%20model%20defines,exchanged%20and%20organized%20over%20networks.)
- [@article@What is TCP/IP and How Does it Work?](https://www.techtarget.com/searchnetworking/definition/TCP-IP)

## Tdd

# Test Driven Development

Test driven development (TDD) is the process of writing tests for software's requirements which will fail until the software is developed to meet those requirements. Once those tests pass, then the cycle repeats to refactor code or develop another feature/requirement. In theory, this ensures that software is written to meet requirements in the simplest form, and avoids code defects.

Visit the following resources to learn more:

- [@article@What is Test Driven Development (TDD)?](https://www.guru99.com/test-driven-development.html)
- [@article@Test-driven development](https://www.ibm.com/garage/method/practices/code/practice_test_driven_development/)
- [@video@Agile in Practice: Test Driven Development](https://youtu.be/uGaNkTahrIw)
- [@feed@Explore top posts about TDD](https://app.daily.dev/tags/tdd?ref=roadmapsh)

## Technical Skills

# Technical Skills

*   Experience in software development
*   Experience in project management
*   Knowledge of one or more programming languages, such as Java, Python, JavaScript, Ruby, Rust, and C
*   Knowledge of different development platforms
*   Understanding of web applications, cybersecurity, and open source technologies
*   Proficiency in analyzing code for issues and errors
*   Experience in database platforms
*   Experience with Operations and DevOps Skills

## Togaf

# Togaf

The TOGAF content framework provides a detailed model of architectural work products, including deliverables, artifacts within deliverables, and the architectural building blocks that artifacts represent.

Visit the following resources to learn more:

- [@official@Togaf](https://www.opengroup.org/togaf)
- [@article@Wikipedia](https://en.wikipedia.org/wiki/The_Open_Group_Architecture_Framework)

## Tools

# Architect Tools

Architect tools are software tools that help architects to design, document, and manage software architectures. These tools can be used to create architecture diagrams, generate code, and automate the software development process.

## Trello

# Trello

Trello is the visual tool that empowers your team to manage any type of project, workflow, or task tracking.

Visit the following resources to learn more:

- [@official@Trello](https://trello.com)
- [@official@Trello Guide](https://trello.com/guide)
- [@video@A Tour Of Trello](https://www.youtube.com/watch?v=AyfupeWS0yY)

## Uml

# UML

The Unified Modeling Language, or UML, is a modeling language that is intended to provide a standard way to visualize and describe the design of a system.

Visit the following resources to learn more:

- [@official@UML Website](https://www.uml.org)
- [@article@UML Pattern - IBM](https://www.ibm.com/docs/en/rational-soft-arch/9.6.1?topic=files-uml-pattern-frameworks)
- [@article@The Unified Modeling Language Reference Manual (Second Edition)](https://personal.utdallas.edu/~chung/Fujitsu/UML_2.0/Rumbaugh--UML_2.0_Reference_CD.pdf)
- [@article@Wikipedia](https://en.wikipedia.org/wiki/Unified_Modeling_Language)

## Understand The Basics

# Software Architect Basics

Understand different concepts such as what is software architecture, software architect, different types of architects and so on.

## W3C And Whatwg

# W3c and WHATWG Standards

World Wide Web Consortium (W3C) standards define the best practices for web development to enable developers to build rich interactive experiences that are available on any device. Theses standards range from recommended web technologies such as HTML, CSS, XML to the generally accepted principles of web architecture, semantics and services.

Web Hypertext Application Technology Working Group (WHATWG) is another set of web standards that came into existence after W3C announced that it was going to be focusing on XHTML over HTML.

Visit the following resources to learn more:

- [@official@W3C Standards](https://www.w3.org/standards/)
- [@official@WHATWG Standards](https://spec.whatwg.org/)

## Web Mobile

# Web and Mobile

Web apps and mobile apps are two distinct types of software applications designed to run on different platforms. Web apps are accessed through web browsers and run on various devices using internet connectivity. They are platform-independent, making them easy to update and maintain, but often require an active internet connection. Mobile apps, on the other hand, are specifically developed for mobile operating systems like Android and iOS, providing enhanced performance, offline functionality, and seamless access to device features such as GPS, cameras, and sensors. While web apps prioritize accessibility and cost-effectiveness, mobile apps focus on delivering a tailored and optimized user experience.

Visit the following resources to learn more:

- [@article@Web vs Mobile](https://buildfire.com/difference-between-web-app-and-mobile-app/)

## What Is A Software Architect

# What is Software Architect?

An expert developer who design software solutions from the ground up, making high-level decisions about each stage of the process including technical standards, tools, design principles, platforms to be used, etc., leading a team of engineers to create the final product.

Visit the following resources to learn more:

- [@article@12 Skills a Software Architect Needs](https://www.redhat.com/architect/what-is-software-architect)

## What Is Software Architecture

# What is Software Architecture?

Describes how an application is built including its components, how they interact with each other, environment in which they operate and so on.

Visit the following resources to learn more:

- [@article@What is Software Architecture in Software Engineering?](https://www.computer.org/resources/software-architecture)
- [@article@Software Architecture: It might not be what you think it is](https://www.infoq.com/articles/what-software-architecture/)
- [@feed@Explore top posts about Architecture](https://app.daily.dev/tags/architecture?ref=roadmapsh)

## Working With Data

# Working with Databases

Working with databases involves storing, managing, and retrieving data efficiently to support applications and business processes. Databases can be relational, like MySQL and PostgreSQL, which use structured tables and SQL for querying, or non-relational (NoSQL), like MongoDB and Cassandra, which handle unstructured or semi-structured data. Effective database management requires designing normalized schemas for relational databases, ensuring data integrity, and optimizing queries for performance. For NoSQL databases, it's important to choose the right type (e.g., document, key-value, columnar) based on application needs. Additionally, managing transactions, indexing, backups, and security are crucial for maintaining reliable and scalable database systems.

Visit the following resources to learn more:

- [@article@Introduction to Databases](https://www.digitalocean.com/community/conceptual-articles/an-introduction-to-databases)

## Xp

# Extreme Programming (XP)

`Extreme Programming (XP)` is a popular agile software development framework that emphasizes speed, simplicity, and quality. It was developed by Kent Beck in the late 1990s and is based on five values:

*   **Communication**: Open and honest communication among team members and stakeholders is essential.
*   **Simplicity**: The simplest solution that works is always preferred.
*   **Feedback**: Continuous feedback from customers and team members is used to improve the product.
*   **Courage**: Team members must be willing to make changes and take risks.
*   **Respect**: Everyone on the team is treated with respect.

Visit the following resources to learn more:

- [@article@What is Extreme Programming (XP)?](https://www.agilealliance.org/glossary/xp/)
- [@article@It's Values, Principles, And Practices](https://www.nimblework.com/agile/extreme-programming-xp/)
- [@article@Extreme Programming (XP)](https://scrum-master.org/en/extreme-programming-xp-a-beginners-guide-to-the-agile-method/)
