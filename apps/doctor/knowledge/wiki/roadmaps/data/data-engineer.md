# Data Engineer Roadmap

## Ab Testing

# A/B Testing

A/B testing is a way to compare two versions of something to see which one works better. You split your audience into two groups, one sees version A, the other sees version B — and then you measure which version gets better results, like more clicks, sales, or sign-ups. This helps you make decisions based on real data instead of guesses.

Visit the following resources to learn more:

- [@article@A software engineer's guide to A/B testing](https://posthog.com/product-engineers/ab-testing-guide-for-engineers)
- [@video@A/B Testing for Beginners](https://www.youtube.com/watch?v=VpTlNRUcIDo)

## Amazon Ec2  Compute

# Amazon EC2 ( Compute)

Amazon Elastic Compute Cloud (EC2) is a web service that provides secure, resizable compute capacity in the cloud. It is designed to make web-scale cloud computing easier for developers. EC2’s simple web service interface allows you to obtain and configure capacity with minimal friction. EC2 enables you to scale your compute capacity, develop and deploy applications faster, and run applications on AWS's reliable computing environment. You have the control of your computing resources and can access various configurations of CPU, Memory, Storage, and Networking capacity for your instances.

Visit the following resources to learn more:

- [@official@EC2 - User Guide](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html)
- [@video@Introduction to Amazon EC2](https://www.youtube.com/watch?v=eaicwmnSdCs)

## Amazon Rds Database

# Amazon RDS (Database)

Amazon RDS (Relational Database Service) is a web service from Amazon Web Services. It's designed to simplify the setup, operation, and scaling of relational databases in the cloud. This service provides cost-efficient, resizable capacity for an industry-standard relational database and manages common database administration tasks. RDS supports six database engines: Amazon Aurora, PostgreSQL, MySQL, MariaDB, Oracle Database, and SQL Server. These engines give you the ability to run instances ranging from 5GB to 6TB of memory, accommodating your specific use case. It also ensures the database is up-to-date with the latest patches, automatically backs up your data and offers encryption at rest and in transit.

Visit the following resources to learn more:

- [@official@Amazon RDS](https://aws.amazon.com/rds/)

## Amazon Rds Database

# Amazon RDS (Database)

Amazon RDS (Relational Database Service) is a web service from Amazon Web Services. It's designed to simplify the setup, operation, and scaling of relational databases in the cloud. This service provides cost-efficient, resizable capacity for an industry-standard relational database and manages common database administration tasks. RDS supports six database engines: Amazon Aurora, PostgreSQL, MySQL, MariaDB, Oracle Database, and SQL Server. These engines give you the ability to run instances ranging from 5GB to 6TB of memory, accommodating your specific use case. It also ensures the database is up-to-date with the latest patches, automatically backs up your data and offers encryption at rest and in transit.

Visit the following resources to learn more:

- [@official@Amazon RDS](https://aws.amazon.com/rds/)

## Amazon Redshift

# Amazon Redshift

Amazon Redshift is a cloud-based data warehouse service from Amazon that lets you store and analyze large amounts of data quickly. It’s designed for running complex queries on huge datasets, so businesses can use it to turn raw data into useful reports and insights. You can load data into Redshift from many sources, and then use SQL to explore it, just like you would with a regular database — but it’s optimized to handle much bigger data and run faster.

Visit the following resources to learn more:

- [@official@Amazon Redshift](https://aws.amazon.com/redshift/)
- [@video@Getting Started with Amazon Redshift - AWS Online Tech Talks](https://www.youtube.com/watch?v=dfo4J5ZhlKI)

## Apache Airflow

# Apache Airflow

Apache Airflow is an open-source tool that helps you schedule, organize, and monitor workflows. Think of it like a to-do list for your data tasks, but smarter — you can set tasks to run in a specific order, track their progress, and see what happens if something fails. It’s often used for automating data pipelines so that data moves, gets processed, and is ready for use without manual work.

Visit the following resources to learn more:

- [@official@Apache Airflow](https://airflow.apache.org/)

## Apache Hadoop Yarn

# Apache Hadoop YARN

Apache Hadoop YARN (Yet Another Resource Negotiator) is the part of Hadoop that manages resources and runs jobs on a cluster. It has a ResourceManager that controls all cluster resources and an ApplicationMaster for each job that schedules and runs tasks. YARN lets different tools like MapReduce and Spark share the same cluster, making it more efficient, flexible, and reliable.

Visit the following resources to learn more:

- [@video@Hadoop Yarn Tutorial](https://www.youtube.com/watch?v=6bIF9VwRwE0)

## Apache Kafka

# Apache Kafka

Apache Kafka is an open-source stream-processing software platform developed by LinkedIn and donated to the Apache Software Foundation. It is written in Scala and Java and operates based on a message queue, designed to handle real-time data feeds. Kafka functions as a kind of message broker service in between the data producers and the consumers, facilitating efficient transmission of data. It can be viewed as a durable message broker where applications can process and reprocess streamed data. Kafka is a highly scalable and fault-tolerant system which ensures data delivery without loss.

Visit the following resources to learn more:

- [@official@Apache Kafka](https://kafka.apache.org/quickstart)
- [@article@Apache Kafka Streams](https://docs.confluent.io/platform/current/streams/concepts.html)
- [@article@Kafka Streams Confluent](https://kafka.apache.org/documentation/streams/)
- [@video@Apache Kafka Fundamentals](https://www.youtube.com/watch?v=B5j3uNBH8X4)
- [@video@Kafka in 100 Seconds](https://www.youtube.com/watch?v=uvb00oaa3k8)
- [@feed@Explore top posts about Kafka](https://app.daily.dev/tags/kafka?ref=roadmapsh)

## Apache Spark

# Apache Spark

Apache Spark is an open-source distributed computing system designed for big data processing and analytics. It offers a unified interface for programming entire clusters, enabling efficient handling of large-scale data with built-in support for data parallelism and fault tolerance. Spark excels in processing tasks like batch processing, real-time data streaming, machine learning, and graph processing. It’s known for its speed, ease of use, and ability to process data in-memory, significantly outperforming traditional MapReduce systems. Spark is widely used in big data ecosystems for its scalability and versatility across various data processing tasks.

Visit the following resources to learn more:

- [@official@ApacheSpark](https://spark.apache.org/documentation.html)
- [@article@Spark By Examples](https://sparkbyexamples.com)
- [@feed@Explore top posts about Apache Spark](https://app.daily.dev/tags/spark?ref=roadmapsh)

## Apis

# APIs and Data Collection

Application Programming Interfaces, better known as APIs, play a fundamental role in the work of data engineers, particularly in the process of data collection. APIs are sets of protocols, routines, and tools that enable different software applications to communicate with each other. An API allows developers to interact with a service or platform through a defined set of rules and endpoints, enabling data exchange and functionality use without needing to understand the underlying code. In data engineering, APIs are used extensively to collect, exchange, and manipulate data from different sources in a secure and efficient manner.

Visit the following resources to learn more:

- [@article@What is an API?](https://aws.amazon.com/what-is/api/)
- [@article@A Beginner's Guide to APIs](https://www.postman.com/what-is-an-api/)

## Argocd

# ArgoCD

Argo CD is a continuous delivery tool for Kubernetes that is based on the GitOps methodology. It is used to automate the deployment and management of cloud-native applications by continuously synchronizing the desired application state with the actual application state in the production environment. In an Argo CD workflow, changes to the application are made by committing code or configuration changes to a Git repository. Argo CD monitors the repository and automatically deploys the changes to the production environment using a continuous delivery pipeline. The pipeline is triggered by changes to the Git repository and is responsible for building, testing, and deploying the changes to the production environment. Argo CD is designed to be a simple and efficient way to manage cloud-native applications, as it allows developers to make changes to the system using familiar tools and processes and it provides a clear and auditable history of all changes to the system. It is often used in conjunction with tools such as Helm to automate the deployment and management of cloud-native applications.

Visit the following resources to learn more:

- [@official@Argo CD - Argo Project](https://argo-cd.readthedocs.io/en/stable/)
- [@video@ArgoCD Tutorial for Beginners](https://www.youtube.com/watch?v=MeU5_k9ssrs)
- [@video@What is ArgoCD](https://www.youtube.com/watch?v=p-kAqxuJNik)
- [@feed@Explore top posts about ArgoCD](https://app.daily.dev/tags/argocd?ref=roadmapsh)

## Async Vs Sync Communication

# Async vs Sync Communication

Synchronous and asynchronous data refer to different approaches in data transmission and processing. **Synchronous** ingestion is a process where the system waits for a response from the data source before proceeding. In contrast, **asynchronous** ingestion is a process where data is ingested without waiting for a response from the data source. Normally, data is queued in a buffer and sent in batches for efficiency.

Each approach has its benefits and drawbacks, and the choice depends on the specific requirements of the data ingestion process and the business needs.

Visit the following resources to learn more:

- [@article@Synchronous And Asynchronous Data Transmission: The Differences And How to Use Them](https://www.computer.org/publications/tech-news/trends/synchronous-asynchronous-data-transmission)
- [@article@Synchronous vs Asynchronous Communication: What’s the Difference?](https://www.getguru.com/reference/synchronous-vs-asynchronous-communication)

## Aurora Db

# Aurora DB

Amazon Aurora (Aurora) is a fully managed relational database engine that's compatible with MySQL and PostgreSQL. Aurora includes a high-performance storage subsystem. Its MySQL- and PostgreSQL-compatible database engines are customized to take advantage of that fast distributed storage. The underlying storage grows automatically as needed. Aurora also automates and standardizes database clustering and replication, which are typically among the most challenging aspects of database configuration and administration.

Visit the following resources to learn more:

- [@official@SAmazon Aurora](https://aws.amazon.com/rds/aurora/)
- [@article@SAmazon Aurora: What It Is, How It Works, and How to Get Started](https://www.datacamp.com/tutorial/amazon-aurora)

## Authentication Vs Authorization

# Authentication vs Authorization

Authentication and authorization are popular terms in modern computer systems that often confuse people. **Authentication** is the process of confirming the identity of a user or a device (i.e., an entity). During the authentication process, an entity usually relies on some proof to authenticate itself, i.e. an authentication factor. In contrast to authentication, **authorization** refers to the process of verifying what resources entities (users or devices) can access, or what actions they can perform, i.e., their access rights.

Visit the following resources to learn more:

- [@article@Basic Authentication](https://roadmap.sh/guides/basic-authentication)
- [@article@What is Authentication vs Authorization?](https://auth0.com/intro-to-iam/authentication-vs-authorization)

## Aws Cdk

# AWS CDK

The AWS Cloud Development Kit (AWS CDK) is an open-source software development framework used to provision cloud infrastructure resources in a safe, repeatable manner through AWS CloudFormation. AWS CDK offers the flexibility to write infrastructure as code in popular languages like Python, Java, Go, and C#.

Visit the following resources to learn more:

- [@course@AWS CDK Crash Course for Beginners](https://www.youtube.com/watch?v=D4Asp5g4fp8)
- [@official@AWS CDK](https://aws.amazon.com/cdk/)
- [@official@AWS CDK Documentation](https://docs.aws.amazon.com/cdk/index.html)
- [@opensource@AWS CDK Examples](https://github.com/aws-samples/aws-cdk-examples)
- [@feed@Explore top posts about AWS](https://app.daily.dev/tags/aws?ref=roadmapsh)

## Aws Eks

# EKS

Amazon Elastic Kubernetes Service (EKS) is a managed service that simplifies the deployment, management, and scaling of containerized applications using Kubernetes, an open-source container orchestration platform. EKS manages the Kubernetes control plane for the user, making it easy to run Kubernetes applications without the operational overhead of maintaining the Kubernetes control plane. With EKS, you can leverage AWS services such as Auto Scaling Groups, Elastic Load Balancer, and Route 53 for resilient and scalable application infrastructure. Additionally, EKS can support Spot and On-Demand instances use, and includes integrations with AWS App Mesh service and AWS Fargate for serverless compute.

Visit the following resources to learn more:

- [@official@Amazon Elastic Kubernetes Service (EKS)](https://aws.amazon.com/eks/)
- [@official@Concepts of Amazon EKS](https://docs.aws.amazon.com/eks/)

## Aws Sns

# AWS SNS

Amazon Simple Notification Service (Amazon SNS) is a web service that makes it easy to set up, operate, and send notifications from the cloud. It provides developers with a highly scalable, flexible, and cost-effective capability to publish messages from an application and immediately deliver them to subscribers or other applications. It is designed to make web-scale computing easier for developers. Amazon SNS follows the “publish-subscribe” (pub-sub) messaging paradigm, with notifications being delivered to clients using a “push” mechanism that eliminates the need to periodically check or “poll” for new information and updates. With simple APIs requiring minimal up-front development effort, no maintenance or management overhead and pay-as-you-go pricing, Amazon SNS gives developers an easy mechanism to incorporate a powerful notification system with their applications.

Visit the following resources to learn more:

- [@official@Amazon Simple Notification Service (SNS) ](http://aws.amazon.com/sns/)
- [@official@Send Fanout Event Notifications](https://aws.amazon.com/getting-started/hands-on/send-fanout-event-notifications/)
- [@article@What is Pub/Sub Messaging?](https://aws.amazon.com/what-is/pub-sub-messaging/)

## Aws Sqs

# AWS SQS

Amazon Simple Queue Service (Amazon SQS) offers a secure, durable, and available hosted queue that lets you integrate and decouple distributed software systems and components. Amazon SQS offers common constructs such as dead-letter queues and cost allocation tags. It provides a generic web services API that you can access using any programming language that the AWS SDK supports.

Visit the following resources to learn more:

- [@official@Amazon Simple Queue Service](https://aws.amazon.com/sqs/)
- [@official@What is Amazon Simple Queue Service?](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html)
- [@article@Amazon Simple Queue Service (SQS): A Comprehensive Tutorial](https://www.datacamp.com/tutorial/amazon-sqs)

## Azure Blob Storage

# Azure Blob Storage

Azure Blob Storage is Microsoft's object storage solution for the cloud. “Blob” stands for Binary Large Object, a term used to describe storage for unstructured data like text, images, and video. Azure Blob Storage is Microsoft Azure’s solution for storing these blobs in the cloud. It offers flexible storage—you only pay based on your usage. Depending on the access speed you need for your data, you can choose from various storage tiers (hot, cool, and archive). Being cloud-based, it is scalable, secure, and easy to manage.

Visit the following resources to learn more:

- [@official@Azure Blob Storage](https://azure.microsoft.com/en-us/products/storage/blobs)
- [@official@Introduction to Azure Blob Storage](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blobs-introduction)
- [@video@A Beginners Guide to Azure Blob Storage](https://www.youtube.com/watch?v=ah1XqItWkuc&t=300s)

## Azure Sql Database

# Azure SQL Database

Azure SQL Database is a fully managed Platform as a Service (PaaS) offering. It abstracts the underlying infrastructure, enabling developers to focus on building and deploying applications without worrying about database maintenance tasks.

Visit the following resources to learn more:

- [@official@Azure SQL Database](https://azure.microsoft.com/en-us/products/azure-sql/database)
- [@official@What is Azure SQL Database?](https://learn.microsoft.com/en-us/azure/azure-sql/database/sql-database-paas-overview?view=azuresql)
- [@article@Azure SQL Database: Step-by-Step Setup and Management](https://www.datacamp.com/tutorial/azure-sql-database)
- [@video@Azure SQL for Beginners](https://www.youtube.com/playlist?list=PLlrxD0HtieHi5c9-i_Dnxw9vxBY-TqaeN)

## Azure Virtual Machines

# Azure Virtual Machines

Azure Virtual Machines (VMs) enable virtualization without requiring hardware investments. They provide customizable environments for development, testing, and cloud applications so you can run different operating systems like Ubuntu on a Windows host based on your needs. One of the key advantages of Azure VMs is the pay-as-you-go pricing model. It allows you to scale resources up or down as needed, ensuring cost efficiency without wasting resources.

Visit the following resources to learn more:

- [@official@Azure Virtual Machines](https://azure.microsoft.com/en-us/products/virtual-machines)
- [@official@Virtual Machines in Azure](https://learn.microsoft.com/en-us/azure/virtual-machines/overview)
- [@video@AVirtual Machines in Azure | Beginner's Guide](https://www.youtube.com/watch?v=_abaWXoQFZU)

## Batch

# Batch

Batch processing is a method in which large volumes of collected data are processed in chunks or batches. This approach is especially effective for resource-intensive jobs, repetitive tasks, and managing extensive datasets where real-time processing isn’t required. It is ideal for applications like data warehousing, ETL (Extract, Transform, Load), and large-scale reporting. Data batch processing is mainly automated, requiring minimal human interaction once the process is set up. Tasks are predefined, and the system executes them according to a scheduled timeline, typically during off-peak hours when computing resources are readily available.

Visit the following resources to learn more:

- [@article@What is Batch Processing?](https://aws.amazon.com/what-is/batch-processing/)
- [@article@Batch And Streaming Demystified For Unification](https://towardsdatascience.com/batch-and-streaming-demystified-for-unification-dee0b48f921d/)

## Best Practices

# Best Practices

1.  **Ensure Reliability.** A robust messaging system must guarantee that messages aren’t lost, even during node failures or network issues. This means using acknowledgments, replication across multiple brokers, and durable storage on disk. These measures ensure that producers and consumers can recover seamlessly without data loss when something goes wrong.
    
2.  **Design for Scalability.** Scalability should be baked in from the start. Partition topics strategically to distribute load across brokers and consumer groups, enabling horizontal scaling.
    
3.  **Maintain Message Ordering.** For systems that depend on message sequence, ensure ordering within partitions and design producers to consistently route related messages to the same partition.
    
4.  **Secure Communication.** Messaging queues often carry sensitive data, so encrypt messages both in transit and at rest. Implement authentication techniques to ensure only trusted clients can publish or consume, and enforce authorization rules to limit access to specific topics or operations.
    
5.  **Monitor & Alert.** Continuous visibility into your messaging system is essential. Track metrics such as message lag, throughput, consumer group health, and broker disk usage. Set alerts for abnormal patterns, like growing lag or dropped connections, so you can respond before they affect downstream systems.

Visit the following resources to learn more:

- [@article@Best Practices for Message Queue Architecture](https://abhishek-patel.medium.com/best-practices-for-message-queue-architecture-f69d47e3565)

## Big Data Tools

# Big Data Tools

Big data tools are specialized software and platforms designed to handle the massive volume, velocity, and variety of data that traditional data processing tools cannot effectively manage. These tools provide the infrastructure, frameworks, and capabilities to process, analyze, and extract meaningful knowledge from vast datasets. They are essential for modern data-driven organizations seeking to gain insights, make informed decisions, and achieve a competitive advantage.

Hadoop and Spark are two of the most prominent frameworks in big data they handle the processing of large-scale data in very different ways. While Hadoop can be credited with democratizing the distributed computing paradigm through a robust storage system called HDFS and a computational model called MapReduce, Spark is changing the game with its in-memory architecture and flexible programming model.

Visit the following resources to learn more:

- [@article@What is Big Data?](https://cloud.google.com/learn/what-is-big-data?hl=en)
- [@article@Hadoop vs Spark: Which Big Data Framework Is Right For You?](https://www.datacamp.com/blog/hadoop-vs-spark)
- [@video@introduction to Big Data with Spark and Hadoop](http://youtube.com/watch?v=vHlwg4ciCsI&t=80s&ab_channel=freeCodeAcademy)

## Bigtable

# BigTable

Bigtable is a high-performance, scalable database that excels at capturing, processing, and analyzing data in real-time. It aggregates data as it's written, providing immediate insights into user behavior, A/B testing results, and engagement metrics. This real-time capability also fuels AI/ML models for interactive applications. Bigtable integrates seamlessly with both Dataflow, enriching streaming pipelines with low-latency lookups, and BigQuery, enabling real-time serving of analytics in user facing application and ad-hoc querying on the same data.

Visit the following resources to learn more:

- [@official@Bigtable: Fast, Flexible NoSQL](https://cloud.google.com/bigtable?hl=en#scale-your-latency-sensitive-applications-with-the-nosql-pioneer)
- [@article@Google Bigtable](https://www.techtarget.com/searchdatamanagement/definition/Google-BigTable)

## Business Intelligence

# Business Intelligence

Business intelligence encompasses a set of techniques and technologies to transform raw data into meaningful insights that drive strategic decision-making within an organization. BI tools enable business users to access different types of data, historical and current, third-party and in-house, as well as semistructured data and unstructured data such as social media. Users can analyze this information to gain insights into how the business is performing and what it should do next.

BI platforms traditionally rely on data warehouses for their baseline information. The strength of a data warehouse is that it aggregates data from multiple data sources into one central system to support business data analytics and reporting. BI presents the results to the user in the form of reports, charts and maps, which might be displayed through a dashboard.

Visit the following resources to learn more:

- [@article@What is business intelligence (BI)?](https://www.ibm.com/think/topics/business-intelligence)
- [@article@Business intelligence: A complete overview](https://www.tableau.com/business-intelligence/what-is-business-intelligence)
- [@video@What is business intelligence?](https://www.youtube.com/watch?v=l98-BcB3UIE)

## Cap Theorem

# CAP Theorem

The CAP Theorem, also known as Brewer's Theorem, is a fundamental principle in distributed database systems. It states that in a distributed system, it's impossible to simultaneously guarantee all three of the following properties: Consistency (all nodes see the same data at the same time), Availability (every request receives a response, without guarantee that it contains the most recent version of the data), and Partition tolerance (the system continues to operate despite network failures between nodes). According to the theorem, a distributed system can only strongly provide two of these three guarantees at any given time. This principle guides the design and architecture of distributed systems, influencing decisions on data consistency models, replication strategies, and failure handling. Understanding the CAP Theorem is crucial for designing robust, scalable distributed systems and for choosing appropriate database solutions for specific use cases in distributed computing environments.

Visit the following resources to learn more:

- [@article@What is CAP Theorem?](https://www.bmc.com/blogs/cap-theorem/)
- [@article@An Illustrated Proof of the CAP Theorem](https://mwhittaker.github.io/blog/an_illustrated_proof_of_the_cap_theorem/)
- [@article@CAP Theorem and its applications in NoSQL Databases](https://www.ibm.com/uk-en/cloud/learn/cap-theorem)
- [@video@What is CAP Theorem?](https://www.youtube.com/watch?v=_RbsFXWRZ10)

## Cassandra

# Cassandra

Apache Cassandra is a highly scalable, distributed NoSQL database designed to handle large amounts of structured data across multiple commodity servers. It provides high availability with no single point of failure, offering linear scalability and proven fault-tolerance on commodity hardware or cloud infrastructure. Cassandra uses a masterless ring architecture, where all nodes are equal, allowing for easy data distribution and replication. It supports flexible data models and can handle both unstructured and structured data. Cassandra excels in write-heavy environments and is particularly suitable for applications requiring high throughput and low latency. Its data model is based on wide column stores, offering a more complex structure than key-value stores. Widely used in big data applications, Cassandra is known for its ability to handle massive datasets while maintaining performance and reliability.

Visit the following resources to learn more:

- [@official@Apache Cassandra](https://cassandra.apache.org/_/index.html)
- [@article@article@Cassandra - Quick Guide](https://www.tutorialspoint.com/cassandra/cassandra_quick_guide.htm)
- [@video@Apache Cassandra - Course for Beginners](https://www.youtube.com/watch?v=J-cSy5MeMOA)
- [@feed@Explore top posts about Backend Development](https://app.daily.dev/tags/backend?ref=roadmapsh)

## Census

# Census

Census is a reverse ETL platform that synchronizes data from a data warehouse to various business applications and SaaS apps like Salesforce and Hubspot. It's a crucial part of the modern data stack, enabling businesses to operationalize their data by making it available in the tools where teams work, like CRMs, marketing platforms, and more.

Visit the following resources to learn more:

- [@official@Census](https://www.getcensus.com/reverse-etl)
- [@official@Census Documentation](https://developers.getcensus.com/getting-started/introduction)
- [@article@A starter guide to reverse ETL with Census](https://www.getcensus.com/blog/starter-guide-for-first-time-census-users)
- [@video@How to "Reverse ETL" with Census](https://www.youtube.com/watch?v=XkS7DQFHzbA)

## Choosing The Right Technologies

# Choosing the Right Technologies

The data engineering ecosystem is rapidly expanding, and selecting the right technologies for your use case can be challenging. Below you can find some considerations for choosing data technologies across the data engineering lifecycle:

*   **Team size and capabilities.** Your team's size will determine the amount of bandwidth your team can dedicate to complex solutions. For small teams, try to stick to simple solutions and technologies your team is familiar with.
*   **Interoperability**. When choosing a technology or system, you’ll need to ensure that it interacts and operates smoothly with other technologies.
*   **Cost optimization and business value,** Consider direct and indirect costs of a technology and the opportunity cost of choosing some technologies over others.
*   **Location** Companies have many options when it comes to choosing where to run their technology stack, including cloud providers, on-premises systems, hybrid clouds, and multicloud.
*   **Build versus buy**. Depending on your needs and capabilities, you can either invest in building your own technologies, implement open-source solutions, or purchase proprietary solutions and services.
*   **Server versus serverless**. Depending on your needs, you may prefer server-based setups, where developers manage servers, or serverless systems, which translates the server management to cloud providers, allowing developers to focus solely on writing code.

Visit the following resources to learn more:

- [@book@Fundamentals of Data Engineering](https://www.oreilly.com/library/view/fundamentals-of-data/9781098108298/)
- [@article@Build hybrid and multicloud architectures using Google Cloud](https://cloud.google.com/architecture/hybrid-multicloud-patterns)
- [@article@The Unfulfilled Promise of Serverless](https://www.lastweekinaws.com/blog/the-unfulfilled-promise-of-serverless/)

## Cicd

# CI / CD

**Continuous Integration** is a software development method where team members integrate their work at least once daily. An automated build checks every integration to detect errors in this method. In Continuous Integration, the software is built and tested immediately after a code commit. In a large project with many developers, commits are made many times during the day. With each commit, code is built and tested.

**Continuous Delivery** is a software engineering method in which a team develops software products in a short cycle. It ensures that software can be easily released at any time. The main aim of continuous delivery is to build, test, and release software with good speed and frequency. It helps reduce the cost, time, and risk of delivering changes by allowing for frequent updates in production.

Visit the following resources to learn more:

- [@article@What is CI/CD? Continuous Integration and Continuous Delivery](https://www.guru99.com/continuous-integration.html)
- [@article@Continuous Integration vs Delivery vs Deployment](https://www.guru99.com/continuous-integration-vs-delivery-vs-deployment.html)
- [@article@CI/CD Pipeline: Learn with Example](https://www.guru99.com/ci-cd-pipeline.html)

## Circle Ci

# CircleCI

CircleCI is a CI/CD service that can be integrated with GitHub, BitBucket and GitLab repositories. The service that can be used as a SaaS offering or self-managed using your own resources.

Visit the following resources to learn more:

- [@official@CircleCI](https://circleci.com/)
- [@official@CircleCI Documentation](https://circleci.com/docs)
- [@official@Configuration Tutorial](https://circleci.com/docs/config-intro)
- [@feed@Explore top posts about CI/CD](https://app.daily.dev/tags/cicd?ref=roadmapsh)

## Cloud Architectures

# Cloud Architectures

Cloud architecture refers to how various cloud technology components, such as hardware, virtual resources, software capabilities, and virtual network systems interact and connect to create cloud computing environments. Cloud architecture dictates how components are integrated so that you can pool, share, and scale resources over a network. It acts as a blueprint that defines the best way to strategically combine resources to build a cloud environment for a specific business need.

Cloud architecture components can included, among others:

*   A frontend platform
*   A backend platform
*   A cloud-based delivery model
*   A network (internet, intranet, or intercloud)

Visit the following resources to learn more:

- [@article@What is cloud architecture? - Google](https://cloud.google.com/learn/what-is-cloud-architecture)
- [@video@WWhat is Cloud Architecture and Common Models?](https://www.youtube.com/watch?v=zTP-bx495hU)

## Cloud Computing

# Cloud Computing

**Cloud Computing** refers to the delivery of computing services over the internet rather than using local servers or personal devices. These services include servers, storage, databases, networking, software, analytics, and intelligence. Cloud Computing enables faster innovation, flexible resources, and economies of scale. There are various types of cloud computing such as public clouds, private clouds, and hybrids clouds. Furthermore, it's divided into different services like Infrastructure as a Service (IaaS), Platform as a Service (PaaS), and Software as a Service (SaaS). These services differ mainly in the level of control an organization has over their data and infrastructures.

Visit the following resources to learn more:

- [@article@Cloud Computing - IBM](https://www.ibm.com/think/topics/cloud-computing)
- [@article@What is Cloud Computing? - Azure](https://azure.microsoft.com/en-gb/resources/cloud-computing-dictionary/what-is-cloud-computing)
- [@video@What is Cloud Computing? - Amazon Web Services](https://www.youtube.com/watch?v=mxT233EdY5c)

## Cloud Sql Database

# Cloud SQL (Database)

Google Cloud SQL is a fully-managed, cost-effective and scalable database service that makes it easy to set-up, maintain, manage and administer MySQL, PostgreSQL, and SQL Server databases in the cloud. Hosted on Google Cloud Platform, Cloud SQL provides a database infrastructure for applications running anywhere.

Visit the following resources to learn more:

- [@course@Cloud SQL](https://www.cloudskillsboost.google/course_templates/701)
- [@official@Cloud SQL](https://cloud.google.com/sql)
- [@official@Cloud SQL overview](https://cloud.google.com/sql/docs/introduction)

## Cluster Computing Basics

# Cluster Computing Basics

Cluster computing is the process of using multiple computing nodes, called clusters, to increase processing power for solving complex problems, such as Big Data analytics and AI model training. These tasks require parallel processing of millions of data points for complex classification and prediction tasks. Cluster computing technology coordinates multiple computing nodes, each with its own CPUs, GPUs, and internal memory, to work together on the same data processing task. Applications on cluster computing infrastructure run as if on a single machine and are unaware of the underlying system complexities.

## Cluster Management Tools

# Cluster Management Tools

Cluster management software maximizes the work that a cluster of computers can perform. A cluster manager balances workload to reduce bottlenecks, monitors the health of the elements of the cluster, and manages failover when an element fails. A cluster manager can also help a system administrator to perform administration tasks on elements in the cluster.

Some of the most popular Cluster Management Tools are Kubernetes and Apache Hadoop YARN.

## Column

# Column

A columnar database is a type of No-SQL database that stores data by columns instead of by rows. In a traditional SQL database, all the information for one record is stored together, but in a columnar database, all the values for a single column are stored together. This makes it much faster to read and analyze large amounts of data, especially when you only need a few columns instead of the whole record. For example, if you want to quickly find the average sales price from millions of rows, a columnar database can scan just the "price" column instead of every piece of data. This design is often used in data warehouses and analytics systems because it speeds up queries and saves storage space through better compression.

Visit the following resources to learn more:

- [@article@What are columnar databases? Here are 35 examples.](https://www.tinybird.co/blog-posts/what-is-a-columnar-database)
- [@article@Columnar Databases](https://www.techtarget.com/searchdatamanagement/definition/columnar-database)
- [@video@WWhat is a Columnar Database? (vs. Row-oriented Database)](https://www.youtube.com/watch?v=1MnvuNg33pA)

## Compute Engine Compute

# Compute Engine (Compute)

Compute Engine is a computing and hosting service that lets you create and run virtual machines on Google infrastructure. Compute Engine offers scale, performance, and value that lets you easily launch large compute clusters on Google's infrastructure. There are no upfront investments, and you can run thousands of virtual CPUs on a system that offers quick, consistent performance. You can configure and control Compute Engine resources using the Google Cloud console, the Google Cloud CLI, or using a REST-based API. You can also use a variety of programming languages to run Compute Engine, including Python, Go, and Java.

Visit the following resources to learn more:

- [@course@The Basics of Google Cloud Compute](https://www.cloudskillsboost.google/course_templates/754)
- [@official@Compute Engine overview](https://cloud.google.com/compute/docs/overview)
- [@video@WCompute Engine in a minute](https://www.youtube.com/watch?v=IuK4gQeHRcI)

## Containers  Orchestration

# Containers & Orchestration

**Containers** are lightweight, portable, and isolated environments that package applications and their dependencies, enabling consistent deployment across different computing environments. They encapsulate software code, runtime, system tools, libraries, and settings, ensuring that the application runs the same regardless of where it's deployed. Containers share the host operating system's kernel, making them more efficient than traditional virtual machines.

**Orchestration** refers to the automated coordination and management of complex IT systems. It involves combining multiple automated tasks and processes into a single workflow to achieve a specific goal. Orchestration is one of the key components of any software development process and it should never be avoided nor preferred over manual configuration. As an automation practice, orchestration helps to remove the chance of human error from the different steps of the data engineering lifecycle. This is all to ensure efficient resource utilization and consistency.

Visit the following resources to learn more:

- [@article@What are Containers?](https://cloud.google.com/learn/what-are-containers)
- [@article@Containers - The New Stack](https://thenewstack.io/category/containers/)
- [@article@An Introduction to Data Orchestration: Process and Benefits](https://www.datacamp.com/blog/introduction-to-data-orchestration-process-and-benefits)
- [@article@What is Container Orchestration?](https://www.redhat.com/en/topics/containers/what-is-container-orchestration)
- [@video@What are Containers?](https://www.youtube.com/playlist?list=PLawsLZMfND4nz-WDBZIj8-nbzGFD4S9oz)
- [@video@Why You Need Data Orchestration](https://www.youtube.com/watch?v=ZtlS5-G-gng)

## Cosmosdb

# CosmosDB

Azure Cosmos DB is a native No-SQL database service and vector database for working with the document data model. It can arbitrarily store native JSON documents with flexible schema. Data is indexed automatically and is available for query using a flavor of the SQL query language designed for JSON data. It also supports vector search. You can access the API using SDKs for popular frameworks such [as.NET](http://as.NET), Python, Java, and Node.js.

Visit the following resources to learn more:

- [@official@What are Containers?](https://azure.microsoft.com/en-us/products/cosmos-db#FAQ)
- [@official@CAzure Cosmos DB - Database for the AI Era](https://learn.microsoft.com/en-us/azure/cosmos-db/introduction)
- [@article@CAzure Cosmos DB: A Global-Scale NoSQL Cloud Database](https://www.datacamp.com/tutorial/azure-cosmos-db)
- [@video@What is Azure Cosmos DB?](https://www.youtube.com/watch?v=hBY2YcaIOQM&)

## Couchdb

# CouchDB

Apache CouchDB is an open source NoSQL document database that collects and stores data in JSON-based document formats. Unlike relational databases, CouchDB uses a schema-free data model, which simplifies record management across various computing devices, mobile phones and web browsers. In CouchDB, each document is uniquely named in the database, and CouchDB provides a RESTful HTTP API for reading and updating (add, edit, delete) database documents. Documents are the primary unit of data in CouchDB and consist of any number of fields and attachments.

Visit the following resources to learn more:

- [@official@CouchDB](hhttps://couchdb.apache.org/)
- [@official@CouchDB Documentation](https://docs.couchdb.org/en/stable/intro/overview.html)
- [@article@What is CouchDB?](https://www.ibm.com/think/topics/couchdb)

## Data Analytics

# Data Analytics

Data Analytics involves extracting meaningful insights from raw data to drive decision-making processes. It includes a wide range of techniques and disciplines ranging from the simple data compilation to advanced algorithms and statistical analysis. Data analysts, as ambassadors of this domain, employ these techniques to answer various questions:

*   Descriptive Analytics _(what happened in the past?)_
*   Diagnostic Analytics _(why did it happened in the past?)_
*   Predictive Analytics _(what will happen in the future?)_
*   Prescriptive Analytics _(how can we make it happen?)_

Visit the following resources to learn more:

- [@course@Introduction to Data Analytics](https://www.coursera.org/learn/introduction-to-data-analytics)
- [@article@The 4 Types of Data Analysis: Ultimate Guide](https://careerfoundry.com/en/blog/data-analytics/different-types-of-data-analysis/)
- [@article@What is Data Analysis? An Expert Guide With Examples](https://www.datacamp.com/blog/what-is-data-analysis-expert-guide)
- [@video@Descriptive vs Diagnostic vs Predictive vs Prescriptive Analytics: What's the Difference?](https://www.youtube.com/watch?v=QoEpC7jUb9k)
- [@video@Types of Data Analytics](https://www.youtube.com/watch?v=lsZnSgxMwBA)

## Data Collection Considerations

# Data Collection Considerations

Before designing the technology archecture to collect and store data, you should consider the following factors:

*   **Bounded versus unbounded**. Bounded data has defined start and end points, forming a finite, complete dataset, like the daily sales report. Unbounded data has no predefined limits in time or scope, flowing continuously and potentially indefinitely, such as user interaction events or real-time sensor data. The distinction is critical in data processing, where bounded data is suitable for batch processing, and unbounded data is processed in stream processing or real-time systems.
*   **Frequency.** Collection processes can be batch, micro-batch, or real-time, depending on the frequency you need to store the data.
*   **Synchronous versus asynchronous.** Synchronous ingestion is a process where the system waits for a response from the data source before proceeding. In contrast, asynchronous ingestion is a process where data is ingested without waiting for a response from the data source. Each approach has its benefits and drawbacks, and the choice depends on the specific requirements of the data ingestion process and the business needs.
*   **Throughput and scalability.** As data demands grow, you will need scalable ingestion solutions to keep pace. Scalable data ingestion pipelines ensure that systems can handle increasing data volumes without compromising performance. Without scalable ingestion, data pipelines face challenges like bottlenecks and data loss. Bottlenecks occur when components can't process data fast enough, leading to delays and reduced throughput. Data loss happens when systems are overwhelmed, causing valuable information to be discarded or corrupted.
*   **Reliability and durability.** Data reliability in the ingestion phase means ensuring that the acquired data from various sources is accurate, consistent, and trustworthy as it enters the data pipeline. Durability entails making sure that data isn’t lost or corrupted during the data collection process.

Visit the following resources to learn more:

- [@book@Fundamentals of Data Engineering](https://www.oreilly.com/library/view/fundamentals-of-data/9781098108298/)

## Data Engineering Lifecycle

# Data Engineering Lifecycle

The data engineering lifecycle encompasses the entire process of transforming raw data into a useful end product. It involves several stages, each with specific roles and responsibilities. This lifecycle ensures that data is handled efficiently and effectively, from its initial generation to its final consumption.

It involves 4 steps:

1.  Data Generation: Collecting data from various source systems.
2.  Data Storage: Safely storing data for future processing and analysis.
3.  Data Ingestion: Transforming and bringing data into a centralized system.
4.  Data Serving: Providing data to end-users for decision-making and operational purposes.

Visit the following resources to learn more:

- [@book@Fundamentals of Data Engineering](https://www.oreilly.com/library/view/fundamentals-of-data/9781098108298/)
- [@article@Data Engineering Lifecycle](https://medium.com/towards-data-engineering/data-engineering-lifecycle-d1e7ee81632e)
- [@video@Getting Into Data Engineering](https://www.youtube.com/watch?v=hZu_87l62J4)

## Data Engineering Lifecycle

# Data Engineering Lifecycle

The data engineering lifecycle encompasses the entire process of transforming raw data into a useful end product. It involves several stages, each with specific roles and responsibilities. This lifecycle ensures that data is handled efficiently and effectively, from its initial generation to its final consumption.

It involves 4 steps:

1.  Data Generation: Collecting data from various source systems.
2.  Data Storage: Safely storing data for future processing and analysis.
3.  Data Ingestion: Transforming and bringing data into a centralized system.
4.  Data Serving: Providing data to end-users for decision-making and operational purposes.

Visit the following resources to learn more:

- [@book@Fundamentals of Data Engineering](https://www.oreilly.com/library/view/fundamentals-of-data/9781098108298/)
- [@article@Data Engineering Lifecycle](https://medium.com/towards-data-engineering/data-engineering-lifecycle-d1e7ee81632e)
- [@video@Getting Into Data Engineering](https://www.youtube.com/watch?v=hZu_87l62J4)

## Data Engineering Vs Data Science

# Data Engineering vs Data Science

Data engineering and data science are distinct but complementary roles within the field of data. Data engineering focuses on building and maintaining the infrastructure for data collection, storage, and processing, essentially creating the systems that make data available for downstream users. On the other hand, data science professionals, like data analysts and data scientists, uses that data to extract insights, build predictive models, and ultimately inform decision-making.

Visit the following resources to learn more:

- [@article@Data Scientist vs Data Engineer](https://www.datacamp.com/blog/data-scientist-vs-data-engineer)
- [@video@Should You Be a Data Scientist, Analyst or Engineer?](https://www.youtube.com/watch?v=dUnKYhripIE)

## Data Fabric

# Data Fabric

A data fabric is a single environment consisting of a unified architecture with services and technologies running on it that architecture that helps a company manage their data. It enables accessing, ingesting, integrating, and sharing data in a environment where the data can be batched or streamed and be in the cloud or on-prem. The ultimate goal of data fabric is to use all your data to gain better insights into your company and make better business decisions. A data fabric includes building blocks such as data pipeline, data access, data lake, data store, data policy, ingestion framework, and data visualization. These building blocks would be used to build platforms or “products” such as a client data integration platform, data hub, governance framework, and a global semantic layer, giving you centralized governance and standardization

Visit the following resources to learn more:

- [@article@What is a data fabric?](http://ibm.com/think/topics/data-fabric)
- [@article@Data Fabric defined](https://www.jamesserra.com/archive/2021/06/data-fabric-defined/)
- [@article@How Data Fabric Can Optimize Data Delivery](https://www.gartner.com/en/data-analytics/topics/data-fabric)

## Data Factory Etl

# Data Factory (ETL)

Data Factory, most commonly referring to Microsoft's Azure Data Factory, is a cloud-based data integration service that allows you to create, schedule, and orchestrate workflows to move and transform data from various sources into a centralized location for analysis. It provides tools for building Extract, Transform, and Load (ETL) pipelines, enabling businesses to prepare data for analytics, business intelligence, and other data-driven initiatives without extensive coding, thanks to its visual, code-free interface and native connectors.

Visit the following resources to learn more:

- [@course@Microsoft Azure - Data Factory](https://www.coursera.org/learn/microsoft-azure---data-factory)
- [@official@What is Azure Data Factory?](https://learn.microsoft.com/en-us/azure/data-factory/introduction)
- [@official@Azure Data Factory Documentation](https://learn.microsoft.com/en-gb/azure/data-factory/)
- [@official@Azure Data Factory Documentation](https://learn.microsoft.com/en-gb/azure/data-factory/)

## Data Generation

# Data Generation

Data generation refers to the different ways data is produced and generated. Thanks to progress in computing power and storage, as well as technology breakthrough in sensor technology (for example, IoT devices), the number of these so-called source systems is rapidly growing. Data is created in many ways, both analog and digital.

**Analog data** refers to continuous, real-world information that is represented by a range of values. It can take on any value within a given range and is often used to describe physical quantities like temperature or sounds.

By contrast, **digital data** is either created by converting analog data to digital form (eg. images or videos) or is the native product of a digital system, such as logs from a mobile app or syntetic data.

Visit the following resources to learn more:

- [@article@The Concept of Data Generation](https://www.marktechpost.com/2023/02/27/the-concept-of-data-generation/)
- [@video@Analog vs. Digital](https://www.youtube.com/watch?v=zzvglgC5ut0)

## Data Hub

# Data Hub

A **data hub** is an architecture that provides a central point for the flow of data between multiple sources and applications, enabling organizations to collect, integrate, and manage data efficiently. Unlike traditional data storage solutions, a data hub’s purpose focuses on data integration and accessibility. The design supports real-time data exchange, which makes accessing, analyzing, and acting on the data faster and easier.

A data hub differs from a data warehouse in that it is generally unintegrated and often at different grains. It differs from an operational data store because a data hub does not need to be limited to operational data. A data hub differs from a data lake by homogenizing data and possibly serving data in multiple desired formats, rather than simply storing it in one place, and by adding other value to the data such as de-duplication, quality, security, and a standardized set of query services.

Visit the following resources to learn more:

- [@article@Data hub](https://en.wikipedia.org/wiki/Data_hub)
- [@article@What is a Data Hub? Definition, 7 Key Benefits & Why You Might Need One](https://www.cdata.com/blog/what-is-a-data-hub)

## Data Ingestion

# Data Ingestion

Data ingestion is the third step in the data engineering lifecycle. It entails the process of collecting and importing data files from various sources into a database for storage, processing and analysis. The goal of data ingestion is to clean and store data in an accessible and consistent central repository to prepare it for use within the organization.

Visit the following resources to learn more:

- [@article@What is Data Ingestion?](https://www.ibm.com/think/topics/data-ingestion)
- [@article@WData Ingestion](https://www.qlik.com/us/data-ingestion)

## Data Interoperability

# Data Interoperability

Data interoperability is the ability of diverse systems and applications to access, exchange, and cooperatively use data in a coordinated and meaningful way, even across organizational boundaries. It ensures that data can flow freely, maintaining its integrity and context, allowing for improved efficiency, collaboration, and decision-making by breaking down data silos. Achieving data interoperability often relies on data standards, metadata, and common data elements to define how data is collected, formatted, and interpreted.

Visit the following resources to learn more:

- [@article@Data Interoperability](https://www.sciencedirect.com/topics/computer-science/data-interoperability)
- [@article@What is Data Interoperability? – Exploring the Process and Benefits](https://www.codelessplatforms.com/blog/what-is-data-interoperability/)

## Data Lake

# Data lakes

**Data Lakes** are large-scale data repository systems that store raw, untransformed data, in various formats, from multiple sources. They're often used for big data and real-time analytics requirements. Data lakes preserve the original data format and schema which can be modified as necessary.

Visit the following resources to learn more:

- [@article@Data Lake Definition](https://azure.microsoft.com/en-gb/resources/cloud-computing-dictionary/what-is-a-data-lake)
- [@video@What is a Data Lake?](https://www.youtube.com/watch?v=LxcH6z8TFpI)

## Data Lineage

# Data Lineage

**Data Lineage** refers to the life-cycle of data, including its origins, movements, characteristics and quality. It's a critical component in Data Engineering for tracking the journey of data through every process in a pipeline, from raw input to model output. Data lineage helps in maintaining transparency, ensuring compliance, and facilitating data debugging or tracing data related bugs. It provides a clear representation of data sources, transformations, and dependencies thereby aiding in audits, governance, or reproduction of machine learning models.

Visit the following resources to learn more:

- [@article@What is Data Lineage? - IBM](https://www.ibm.com/topics/data-lineage)
- [@article@What is Data Lineage? - Datacamp](https://www.datacamp.com/blog/data-lineage)

## Data Mart

# Data Mart

A data mart is a subset of a data warehouse, focused on a specific business function or department. A data mart is streamlined for quicker querying and a more straightforward setup, catering to the specialized needs of a particular team, or function. Data marts only hold data relevant to a specific department or business unit, enabling quicker access to specific datasets, and simpler management

Visit the following resources to learn more:

- [@article@What is a Data Mart?](https://www.ibm.com/think/topics/data-mart)
- [@article@WData Mart vs Data Warehouse: a Detailed Comparison](https://www.datacamp.com/blog/data-mart-vs-data-warehouse)
- [@video@Data Lake VS Data Warehouse VS Data Marts](https://www.youtube.com/watch?v=w9-WoReNKHk)

## Data Masking

# Data Masking

Data masking is a process that creates a copy of real data but replaces sensitive information with false but realistic-looking data, preserving the format and structure of the original data for non-production uses like software testing, training, and development. The goal is to protect confidential information and ensure compliance with data protection regulations by preventing unauthorized access to real sensitive data without compromising the usability of the data for other business functions.

Visit the following resources to learn more:

- [@article@Data masking](https://en.wikipedia.org/wiki/Data_masking)
- [@article@What is data masking?](https://aws.amazon.com/what-is/data-masking/)

## Data Mesh

# Data Mesh

A data mesh is a modern approach to data architecture that shifts data management from a centralized model to a decentralized one. It emphasizes domain-oriented ownership, where data management aligns with specific business areas. This alignment makes data operations more scalable and flexible, leveraging the knowledge and expertise of those closest to the data. Data mesh is defined by four principles: data domains, data products, self-serve data platform, and federated computational governance.

Visit the following resources to learn more:

- [@article@What Is a Data Mesh? - AWS](https://aws.amazon.com/what-is/data-mesh)
- [@article@What Is a Data Mesh? - Datacamp](https://www.datacamp.com/blog/data-mesh)
- [@video@Data Mesh Architecture](https://www.datamesh-architecture.com/)

## Data Modelling Techniques

# Data Modelling Techniques

A data model is a specification of data structures and business rules. It creates a visual representation of data and illustrates how different data elements are related to each other. Different techniques are employed depending on the complexity of the data and the goals. Below you can find a list with the most common data modelling techniques:

*   **Entity-relationship modeling.** It's one of the most common techniques used to represent data. It's based on three elements: Entities (objects or things within the system), relationships (how these entities interact with each other), and attributes (properties of the entities).
*   **Dimensional modeling.** Dimensional modeling is widely used in data warehousing and analytics, where data is often represented in terms of facts and dimensions. This technique simplifies complex data by organizing it into a star or snowflake schema.
*   **Object-oriented modeling.** Object-oriented modeling is used to represent complex systems, where data and the functions that operate on it are encapsulated as objects. This technique is preferred for modeling applications with complex, interrelated data and behaviors
*   **NoSQL modeling.** NoSQL modeling techniques are designed for flexible, schema-less databases. These approaches are often used when data structures are less rigid or evolve over time

Visit the following resources to learn more:

- [@article@7 data modeling techniques and concepts for business](https://www.techtarget.com/searchdatamanagement/tip/7-data-modeling-techniques-and-concepts-for-business)
- [@article@@articleData Modeling Explained: Techniques, Examples, and Best Practices](https://www.datacamp.com/blog/data-modeling)

## Data Normalization

# Database Normalization

Database normalization is the process of structuring a relational database in accordance with a series of so-called normal forms in order to reduce data redundancy and improve data integrity. It was first proposed by Edgar F. Codd as part of his relational model. Normalization entails organizing the columns (attributes) and tables (relations) of a database to ensure that their dependencies are properly enforced by database integrity constraints. It is accomplished by applying some formal rules either by a process of synthesis (creating a new database design) or decomposition (improving an existing database design).

Visit the following resources to learn more:

- [@article@What is Normalization in DBMS (SQL)? 1NF, 2NF, 3NF, BCNF Database with Example](https://www.guru99.com/database-normalization.html)
- [@video@Complete guide to Database Normalization in SQL](https://www.youtube.com/watch?v=rBPQ5fg_kiY)
- [@feed@Explore top posts about Database](https://app.daily.dev/tags/database?ref=roadmapsh)

## Data Obfuscation

# Data Obfuscation

Statistical data obfuscation involves altering the values of sensitive data in a way that preserves the statistical properties and relationships within the data. It ensures that the masked data maintains the overall distribution, patterns, and correlations of the original data for accurate statistical analysis. Statistical data obfuscation techniques include applying mathematical functions or perturbation algorithms to the data.

## Data Pipelines

# Data Pipelines

Data pipelines are a series of automated processes that transport and transform data from various sources to a destination for analysis or storage. They typically involve steps like data extraction, cleaning, transformation, and loading (ETL) into databases, data lakes, or warehouses. Pipelines can handle batch or real-time data, ensuring that large-scale datasets are processed efficiently and consistently. They play a crucial role in ensuring data integrity and enabling businesses to derive insights from raw data for reporting, analytics, or machine learning.

Visit the following resources to learn more:

- [@article@What is a Data Pipeline? - IBM](https://www.ibm.com/topics/data-pipeline)
- [@video@What are Data Pipelines?](https://www.youtube.com/watch?v=oKixNpz6jNo)

## Data Quality

# Data Quality

Ensuring quality involves validating the accuracy, completeness, consistency, and reliability of the data collected from each source. The fact that you do it from one source or multiple is almost irrelevant since the only extra task would be to homogenize the final schema of the data, ensuring deduplication and normalization.

This last part typically includes verifying the credibility of each data source, standardizing formats (like date/time or currency), performing schema alignment, and running profiling to detect anomalies, duplicates, or mismatches before integrating the data for analysis.

## Data Quality

# Data Quality

Data quality refers to the degree to which a dataset is accurate, complete, consistent, relevant, and timely, making it fit for its intended use. High-quality data is reliable and trustworthy, enabling better decision-making, accurate analysis, and effective strategies, while poor data quality can lead to flawed insights, wasted resources, and negative consequences for an organization.

Visit the following resources to learn more:

- [@article@What is Data Quality?](https://www.ibm.com/think/topics/data-quality)

## Data Serving

# Data Serving

Data serving is the last step in the data engineering process. Once the data is stored in your data architectures and transformed into coherent and useful format, it's time for get value from it. Data serving refers to the different ways data is used by downstream applications and users to create value. There are many ways companies can extract value from data, including training machine learning models, BI Analytics, and reverse ETL.

## Data Storage

# Data Storage

Data storage is the process of saving and preserving digital information on various physical or cloud-based media for future retrieval and use. It encompasses the use of technologies and devices like hard drives and cloud platforms to store data.

Visit the following resources to learn more:

- [@article@What is data storage?](https://www.ibm.com/think/topics/data-storage)

## Data Structures And Algorithms

# DataStructures and Algorithms

**Data Structures** are primarily used to collect, organize and perform operations on the stored data more effectively. They are essential for designing advanced-level Android applications. Examples include Array, Linked List, Stack, Queue, Hash Map, and Tree.

**Algorithms** are a sequence of instructions or rules for performing a particular task. Algorithms can be used for data searching, sorting, or performing complex business logic. Some commonly used algorithms are Binary Search, Bubble Sort, Selection Sort, etc. A deep understanding of data structures and algorithms is crucial in optimizing the performance and the memory consumption of data pipelines

Visit the following resources to learn more:

- [@article@Interview Questions about Data Structures](https://www.csharpstar.com/csharp-algorithms/)
- [@video@Data Structures Illustrated](https://www.youtube.com/watch?v=9rhT3P1MDHk&list=PLkZYeFmDuaN2-KUIv-mvbjfKszIGJ4FaY)
- [@video@Intro to Algorithms](https://www.youtube.com/watch?v=rL8X2mlNHPM)
- [@feed@Explore top posts about Algorithms](https://app.daily.dev/tags/algorithms?ref=roadmapsh)

## Data Warehouse

# Data Warehouse

**Data Warehouses** are data storage systems which are designed for analyzing, reporting and integrating with transactional systems. The data in a warehouse is clean, consistent, and often transformed to meet wide-range of business requirements. Hence, data warehouses provide structured data but require more processing and management compared to data lakes.

Visit the following resources to learn more:

- [@article@What Is a Data Warehouse?](https://www.oracle.com/database/what-is-a-data-warehouse/)
- [@video@@hat is a Data Warehouse?](https://www.youtube.com/watch?v=k4tK2ttdSDg)

## Data Warehousing Architectures

# Data Warehousing Architectures

Data Warehousing Architectures refers to the different systems and solutions for storing data. Options include traditional data warehouse, data marts, data lakes and data mesh architectures.

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

## Database

# Database

A database is an organized, structured collection of electronic data that is stored, managed, and accessed via a computer system, usually controlled by a Database Management System (DBMS). Databases organize various types of data, such as words, numbers, images, and videos, allowing users to easily retrieve, update, and modify it for various purposes, from managing customer information to analyzing business processes.

## Databricks Delta Lake

# Databricks Delta Lake

Delta Lake is the optimized storage layer that provides the foundation for tables in a lakehouse on Databricks. Delta Lake is open source software that extends Parquet data files with a file-based transaction log for ACID transactions and scalable metadata handling. Delta Lake is fully compatible with Apache Spark APIs, and was developed for tight integration with Structured Streaming, allowing you to easily use a single copy of data for both batch and streaming operations and providing incremental processing at scale.

Visit the following resources to learn more:

- [@book@The Delta Lake Series — Fundamentals and Performance](https://www.databricks.com/resources/ebook/the-delta-lake-series-fundamentals-performance)
- [@official@What is Delta Lake in Databricks?](https://docs.databricks.com/aws/en/delta)
- [@article@Delta Table in Databricks: A Complete Guide](https://www.datacamp.com/tutorial/delta-table-in-databricks)
- [@video@Delta Lake](https://www.databricks.com/resources/demos/videos/lakehouse-platform/delta-lake)

## Datadog

# Datadog

Datadog is a monitoring and analytics platform for large-scale applications. It encompasses infrastructure monitoring, application performance monitoring, log management, and user-experience monitoring. Datadog aggregates data across your entire stack with 400+ integrations for troubleshooting, alerting, and graphing.

Visit the following resources to learn more:

- [@official@Datadog](https://www.datadoghq.com/)
- [@official@Datadog Documentation](https://docs.datadoghq.com/)

## Dataflow

# Dataflow

Dataflow is a Google Cloud service that provides unified stream and batch data processing at scale. Typical use cases for Dataflow include Data movement,ETL processes, BI dashboarding, and applying ML in real time to streaming data.

Visit the following resources to learn more:

- [@official@Dataflow](https://cloud.google.com/products/dataflow)
- [@article@Dataflow](https://en.wikipedia.org/wiki/Google_Cloud_Dataflow)
- [@video@What is Google Dataflow](https://www.youtube.com/watch?v=KalJ0VuEM7s)

## Dbt

# dbt

dbt, also known as the data build tool, is designed to simplify the management of data warehouses and transform the data within. This is primarily the T, or transformation, within ELT (or sometimes ETL) processes. It allows for easy transition between data warehouse types, such as Snowflake, BigQuery, Postgres, or DuckDB. dbt also provides the ability to use SQL across teams of multiple users, simplifying interaction. In addition, dbt translates between SQL dialects as appropriate to connect to different data sources and warehouses.

Visit the following resources to learn more:

- [@course@dbt Official Courses](https://learn.getdbt.com/catalog)
- [@official@dbt](https://www.getdbt.com/product/what-is-dbt)
- [@official@dbt Documentation](https://docs.getdbt.com/docs/build/documentation)

## Declarative Vs Imperative

# Declarative vs Imperative

When it comes to Infrastructure as Code (IaC), there are two fundamental styles: imperative and declarative.

In **imperative IaC**, you specify a list of steps the IaC tool should follow to provision a new resource. You tell your IaC tool how to create each environment using a sequence of command imperatives. Imperative IaC can offer more flexibility as it allows you to dictate each step. However, this can result in increased complexity. Popular imperative IaC tools are Chef and Puppet

In **declarative IaC**, you specify the name and properties of the infrastructure resources you wish to provision, and then the IaC tool figures out how to achieve that end result on its own. You declare to your IaC tool what you want, but not how to get there. Declarative IaC, while less flexible, tends to be simpler and more manageable. Terraform is the most popular declarative IaC tool

Visit the following resources to learn more:

- [@article@Infrastructure as Code: From Imperative to Declarative and Back Again](https://thenewstack.io/infrastructure-as-code-from-imperative-to-declarative-and-back-again/)
- [@article@Declarative vs Imperative Programming for Infrastructure as Code (IaC)](https://www.copado.com/resources/blog/declarative-vs-imperative-programming-for-infrastructure-as-code-iac)

## Distributed File Systems

# Distributed File Systems

A Distributed File System (DFS) allows multiple computers to access and share files across a network as if they were stored on a single local machine. It distributes data across multiple servers, enhancing accessibility and data redundancy. This enables users to access files from various locations and devices, promoting collaboration and data availability.

Visit the following resources to learn more:

- [@article@What is a Distributed File System (DFS)? A Complete Guide](http://starwindsoftware.com/blog/what-is-a-distributed-file-system-dfs-a-complete-guide/)

## Distributed Systems Basics

# Distributed Systems

A distributed system is a collection of independent computers that communicate and coordinate to appear as a single unified system. They are widely used for scalability, fault tolerance, and high availability in modern applications. However, they bring challenges such as synchronization, consistency trade-offs (CAP theorem), concurrency, and network latency.

Visit the following resources to learn more:

- [@article@Introduction to Distributed Systems](https://www.freecodecamp.org/news/a-thorough-introduction-to-distributed-systems-3b91562c9b3c/)
- [@article@Distributed Systems Guide](https://www.baeldung.com/cs/distributed-systems-guide)
- [@video@Quick overview](https://www.youtube.com/watch?v=IJWwfMyPu1c)

## Docker

# Docker

Docker is an open-source platform that automates the deployment, scaling, and management of applications using containerization technology. It enables developers to package applications with all their dependencies into standardized units called containers, ensuring consistent behavior across different environments. Docker provides a lightweight alternative to full machine virtualization, using OS-level virtualization to run multiple isolated systems on a single host. Its ecosystem includes tools for building, sharing, and running containers, such as Docker Engine, Docker Hub, and Docker Compose. Docker has become integral to modern DevOps practices, facilitating microservices architectures, continuous integration/deployment pipelines, and efficient resource utilization in both development and production environments.

Visit the following resources to learn more:

- [@roadmap@Visit Dedicated Docker Roadmap](https://roadmap.sh/docker)
- [@official@Docker Documentation](https://docs.docker.com/)
- [@video@Docker Tutorial](https://www.youtube.com/watch?v=RqTEHSBrYFw)
- [@video@Docker simplified in 55 seconds](https://youtu.be/vP_4DlOH1G4)
- [@feed@Explore top posts about Docker](https://app.daily.dev/tags/docker?ref=roadmapsh)

## Document

# Document

\*\*Document Databases are a type of No-SQL databases that store data in JSON, BSON, or XML formats, allowing for flexible, semi-structured and hierarchical data structures. These databases are characterized by their dynamic schema, scalability through distribution, and ability to intuitively map data models to application code. Popular examples include MongoDB, which allows for easy storage and retrieval of varied data types without requiring a rigid, predefined schema.

Visit the following resources to learn more:

- [@article@What is a Document Database?](https://www.mongodb.com/resources/basics/databases/document-databases)
- [@article@HDocument-oriented database](https://en.wikipedia.org/wiki/Document-oriented_database)

## Dynamodb

# DynamoDB

Amazon DynamoDB is a fully managed NoSQL database solution that provides fast and predictable performance with seamless scalability. It is a key-value and document database that delivers single-digit millisecond performance at any scale. DynamoDB can handle more than 10 trillion requests per day and support peaks of more than 20 million requests per second. It maintains high durability of data via automatic replication across three different zones in an Amazon defined region.

Visit the following resources to learn more:

- [@official@Amazon DynamoDB](https://aws.amazon.com/dynamodb/)

## Ecpa

# ECPA

The California Consumer Privacy Act (CCPA) is a California state law enacted in 2020 that protects and enforces the rights of Californians regarding the privacy of consumers’ personal information (PI).

Visit the following resources to learn more:

- [@official@California Consumer Privacy Act (CCPA)](https://oag.ca.gov/privacy/ccpa)
- [@article@What is the California Consumer Privacy Act (CCPA)?](https://www.ibm.com/think/topics/ccpa-compliance)
- [@video@What is the California Consumer Privacy Act? | CCPA Explained?](https://www.youtube.com/watch?v=dpzsAgrDAO4)

## Elasticsearch

# Elasticsearch

Elastic search at its core is a document-oriented search engine. It is a document based database that lets you INSERT, DELETE , RETRIEVE and even perform analytics on the saved records. But, Elastic Search is unlike any other general purpose database you have worked with, in the past. It's essentially a search engine and offers an arsenal of features you can use to retrieve the data stored in it, as per your search criteria. And that too, at lightning speeds.

Visit the following resources to learn more:

- [@official@Elasticsearch Website](https://www.elastic.co/elasticsearch/)
- [@official@Elasticsearch Documentation](https://www.elastic.co/guide/index.html)
- [@video@What is Elasticsearch](https://www.youtube.com/watch?v=ZP0NmfyfsoM)
- [@feed@Explore top posts about ELK](https://app.daily.dev/tags/elk?ref=roadmapsh)

## Encryption

# Encryption

Encryption is used to protect data from being stolen, changed, or compromised and works by scrambling data into a secret code that can only be unlocked with a unique digital key. Encrypted data can be protected while at rest on computers or in transit between them, or while being processed, regardless of whether those computers are located on-premises or are remote cloud servers.

Visit the following resources to learn more:

- [@article@What is Encryption?](https://cloud.google.com/learn/what-is-encryption)
- [@video@What is Encryption?](https://www.youtube.com/watch?v=9chKCUQ8_VQ)

## End To End Testing

# End-to-End Testing

End-to-end or (E2E) testing is a form of testing used to assert your entire application works as expected from start to finish or "end-to-end". E2E testing differs from unit testing in that it is completely decoupled from the underlying implementation details of your code. It is typically used to validate an application in a way that mimics the way a user would interact with it.

Visit the following resources to learn more:

- [@article@End to End Testing](https://microsoft.github.io/code-with-engineering-playbook/automated-testing/e2e-testing/)
- [@article@End to End Testing: Importance, Process, Best Practices & Frameworks](https://testgrid.io/blog/end-to-end-testing-a-detailed-guide/)

## Environmental Management

# Environmental Management

Environmental management, or Environment as Code (EaC) takes the concept of Infrastructure as Code (IaC) one step further. EaC applies DevOps principles to manage and automate entire software environments—including infrastructure, applications, and configurations—using code, making them reproducible, versionable, and reliable. It extends IaC by focusing not just on the underlying servers and networks but on the complete, connected system of services and applications that run on top of it. This approach helps increase efficiency, speeds up deployments, and provides a consistent, auditable process for creating and managing development, testing, and production environments.

Visit the following resources to learn more:

- [@article@EWhat Is Environment as Code (EaaC)?](https://www.bunnyshell.com/blog/what-is-environment-as-code-eaac/)

## Etl Vs Reverse Etl

# ETL vs Reverse ETL

ETL (Extract, Transform, Load) is a key process in data warehousing, enabling the integration of data from multiple sources into a centralized database.

Reverse ETL emerged as organizations recognized that their carefully curated data warehouses, while excellent for analysis, created a new form of data silo that prevented operational teams from accessing valuable insights. This methodology addresses the critical gap between analytical insights and operational execution by systematically moving processed data from centralized repositories back to the operational systems where business teams interact with customers and manage daily operations.

Visit the following resources to learn more:

- [@article@What is ETL?](https://www.snowflake.com/guides/what-etl)
- [@article@ETL vs Reverse ETL vs Data Activation](https://airbyte.com/data-engineering-resources/etl-vs-reverse-etl-vs-data-activation)
- [@article@ETL vs Reverse ETL: An Overview, Key Differences, & Use Cases](https://portable.io/learn/etl-vs-reverse-etl)

## Eu Ai Act

# EU AI Act

The Artificial Intelligence Act of the European Union, also known as the EU AI Act, is a comprehensive regulatory framework that is established to ensure safety and that fundamental human rights are upheld in the use of AI technologies. It governs the development and/or use of AI in the European Union. The act takes a risk-based approach to regulation, applying different rules to AI systems according to the risk they pose.

Considered the world's first comprehensive regulatory framework for AI, the EU AI Act prohibits some AI uses outright and implements strict governance, risk management and transparency requirements for others.

Visit the following resources to learn more:

- [@official@The EU AI Act Explorer](https://artificialintelligenceact.eu/ai-act-explorer/)
- [@article@AI Act - European Commission](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)
- [@article@Artificial Intelligence Act](https://en.wikipedia.org/wiki/Artificial_Intelligence_Act)
- [@video@The EU AI Act Explained](https://www.youtube.com/watch?v=s_rxOnCt3HQ)

## Extract Data

# Extract Data

The first step in ETL processes involves extract data from data sources to a staging area. Data can come in various types and formats, from SQL or NoSQL databases and plan text to image and video files.

## Functional Testing

# Functional Testing

Functional testing is a type of software testing that validates the software system against the functional requirements/specifications. The purpose of functional tests is to test each function of the software application by providing appropriate input and verifying the output against the functional requirements.

Visit the following resources to learn more:

- [@article@What is Functional Testing? Types & Examples](https://www.guru99.com/functional-testing.html)
- [@article@Functional Testing : A Detailed Guide](https://www.browserstack.com/guide/functional-testing)
- [@feed@Explore top posts about Testing](https://app.daily.dev/tags/testing?ref=roadmapsh)

## Gdpr

# GDPR in API Design

The General Data Protection Regulation (GDPR) is an essential standard in API Design that addresses the storage, transfer, and processing of personal data of individuals within the European Union. With regards to API Design, considerations must be given on how APIs handle, process, and secure the data to conform with GDPR's demands on data privacy and security. This includes requirements for explicit consent, right to erasure, data portability, and privacy by design. Non-compliance with these standards not only leads to hefty fines but may also erode trust from users and clients. As such, understanding the impact and integration of GDPR within API design is pivotal for organizations handling EU residents' data.

Visit the following resources to learn more:

- [@official@GDPR](https://gdpr-info.eu/)
- [@article@What is GDPR Compliance in Web Application and API Security?](https://probely.com/blog/what-is-gdpr-compliance-in-web-application-and-api-security/)

## Git And Github

# Git and GitHub

**Git** is a free and open source distributed version control system designed to handle everything from small to very large projects with speed and efficiency.

**GitHub** is a web-based platform that provides hosting for software development and version control using Git. It is widely used by developers and organizations around the world to manage and collaborate on software projects.

Visit the following resources to learn more:

- [@roadmap@Visit Dedicated Git & GitHub Roadmap](https://roadmap.sh/git-github)
- [@official@Git Documentation](https://git-scm.com/)
- [@official@GitHub Documentation](https://docs.github.com/en/get-started/quickstart)
- [@article@Learn Git with Tutorials, News and Tips - Atlassian](https://www.atlassian.com/git)
- [@article@Git Cheat Sheet](https://cs.fyi/guide/git-cheatsheet)
- [@video@What is GitHub?](https://www.youtube.com/watch?v=w3jLJU7DT5E)
- [@video@Git & GitHub Crash Course For Beginners](https://www.youtube.com/watch?v=SWYqp7iY_Tc)

## Github Actions

# GitHub Actions

GitHub Actions is a CI/CD tool integrated directly into GitHub, allowing developers to automate workflows, such as building, testing, and deploying code directly from their repositories. It uses YAML files to define workflows, which can be triggered by various events like pushes, pull requests, or on a schedule. GitHub Actions supports a wide range of actions and integrations, making it highly customizable for different project needs. It provides a marketplace with reusable workflows and actions contributed by the community. With its seamless integration with GitHub, developers can take advantage of features like matrix builds, secrets management, and environment-specific configurations to streamline and enhance their development and deployment processes.

Visit the following resources to learn more:

- [@official@GitHub Actions Documentation](https://docs.github.com/en/actions)

## Gitlab Ci

# GitLab CI

GitLab offers a CI/CD service that can be used as a SaaS offering or self-managed using your own resources. You can use GitLab CI with any GitLab hosted repository, or any BitBucket Cloud or GitHub repository in the GitLab Premium self-managed, GitLab Premium SaaS and higher tiers.

Visit the following resources to learn more:

- [@official@GitLab](https://gitlab.com/)
- [@official@GitLab Documentation](https://docs.gitlab.com/)
- [@official@Get Started with GitLab CI](https://docs.gitlab.com/ee/ci/quick_start/)
- [@official@Learn GitLab Tutorials](https://docs.gitlab.com/ee/tutorials/)
- [@official@GitLab CI/CD Examples](https://docs.gitlab.com/ee/ci/examples/)
- [@feed@Explore top posts about GitLab](https://app.daily.dev/tags/gitlab?ref=roadmapsh)

## Glue Etl

# Amazon RDS (Database)

Amazon RDS (Relational Database Service) is a web service from Amazon Web Services. It's designed to simplify the setup, operation, and scaling of relational databases in the cloud. This service provides cost-efficient, resizable capacity for an industry-standard relational database and manages common database administration tasks. RDS supports six database engines: Amazon Aurora, PostgreSQL, MySQL, MariaDB, Oracle Database, and SQL Server. These engines give you the ability to run instances ranging from 5GB to 6TB of memory, accommodating your specific use case. It also ensures the database is up-to-date with the latest patches, automatically backs up your data and offers encryption at rest and in transit.

Visit the following resources to learn more:

- [@official@Amazon RDS](https://aws.amazon.com/rds/)

## Go

# Go

Go, also known as Golang, is a statically typed, compiled programming language designed by Google. It combines the efficiency of compiled languages with the ease of use of dynamically typed interpreted languages. Go features built-in concurrency support through goroutines and channels, making it well-suited for networked and multicore systems. It has a simple and clean syntax, fast compilation times, and efficient garbage collection. Go's standard library is comprehensive, reducing the need for external dependencies. The language emphasizes simplicity and readability, with features like implicit interfaces and a lack of inheritance. Go is particularly popular for building microservices, web servers, and distributed systems. Its performance, simplicity, and robust tooling make it a favored choice for cloud-native development, DevOps tools, and large-scale backend systems.

Visit the following resources to learn more:

- [@roadmap@Visit Dedicated Go Roadmap](https://roadmap.sh/golang)
- [@official@Go Reference Documentation](https://go.dev/doc/)
- [@article@Go by Example - annotated example programs](https://gobyexample.com/)
- [@article@Go, the Programming Language of the Cloud](https://thenewstack.io/go-the-programming-language-of-the-cloud/)
- [@video@Go Programming â€“ Golang Course with Bonus Projects](https://www.youtube.com/watch?v=un6ZyFkqFKo)
- [@feed@Explore top posts about Golang](https://app.daily.dev/tags/golang?ref=roadmapsh)

## Google Bigquery

# Google BigQuery

BigQuery is a managed, serverless data warehouse product by Google, offering scalable analysis over large quantities of data. It is a Platform as a Service (PaaS) that supports querying using a dialect of SQL. BigQuery is NoOps, meaning there is no infrastructure to manage and you don't need a database administrator. BigQuery lets you focus on analyzing data to find meaningful insights while using familiar SQL and built-in machine learning at unmatched price-performance.

Visit the following resources to learn more:

- [@official@BigQuery overview](https://cloud.google.com/bigquery/docs/introduction)
- [@official@From data warehouse to autonomous data and AI platform](https://cloud.google.com/bigquery)
- [@video@What is BigQuery?](https://www.youtube.com/watch?v=d3MDxC_iuaw)

## Google Cloud Gke

# undefined

GKE - Google Kubernetes Engine
------------------------------

Google Kubernetes Engine (GKE) is a managed Kubernetes service provided by Google Cloud Platform. It allows organizations to deploy, manage, and scale containerized applications using Kubernetes orchestration. GKE automates cluster management tasks, including upgrades, scaling, and security patches, while providing integration with Google Cloud services. It offers features like auto-scaling, load balancing, and private clusters, enabling developers to focus on application development rather than infrastructure management.

Visit the following resources to learn more:

- [@official@GKE](https://cloud.google.com/kubernetes-engine)
- [@video@What is Google Kubernetes Engine (GKE)?](https://www.youtube.com/watch?v=Rl5M1CzgEH4)

## Google Cloud Storage

# Google Cloud Storage

Google Cloud Storage (GCS) is a scalable, secure, and durable object storage service within Google Cloud Platform (GCP) designed for storing and retrieving unstructured data of any type or size. It allows users to store data in "buckets" and access it through APIs, web interfaces, or command-line tools for applications, backups, media hosting, and big data analytics. GCS offers different storage classes to optimize costs based on data access frequency, strong security with encryption, and high availability through redundant data storage across multiple locations.

Visit the following resources to learn more:

- [@article@Cloud Storage](https://cloud.google.com/storage)
- [@article@Google Cloud Storage](https://en.wikipedia.org/wiki/Google_Cloud_Storage)
- [@article@Cloud Storage in a minute](https://www.youtube.com/watch?v=wNOs3LlsH6k)

## Google Deployment  Mgr

# Google Deployment  Mgr.

Google Cloud Deployment Manager is an infrastructure deployment service that automates the creation and management of Google Cloud resources. It provides users with flexible template and configuration files to create deployments that have a variety of Google Cloud services, such as Cloud Storage, Compute Engine, and Cloud SQL, configured to work together.

Important, Google Deployment Manager will reach end of support on 31 December 2025. An alternative to this tool is **Google Infrastructure Manager**. Infrastructure Manager (Infra Manager) automates the deployment and management of Google Cloud infrastructure resources using Terraform. Infra Manager allows users to deploy programmatically to Google Cloud, allowing to use this service rather than maintaining a different toolchain to work with Terraform on Google Cloud.

Visit the following resources to learn more:

- [@official@Infrastructure Manager Overview](https://cloud.google.com/infrastructure-manager/docs/overview)
- [@official@Google Cloud Deployment Manager documentation](https://cloud.google.com/deployment-manager/docs)

## Graph

# Graph Databases

In a graph database, each node is a record and each arc is a relationship between two nodes. Graph databases are optimized to represent complex relationships with many foreign keys or many-to-many relationships.

Graphs databases offer high performance for data models with complex relationships, such as a social network. They are relatively new and are not yet widely-used; it might be more difficult to find development tools and resources. Many graphs can only be accessed with REST APIs.

Visit the following resources to learn more:

- [@article@What is a Graph database?](https://aws.amazon.com/nosql/graph/)
- [@article@What is A Graph Database? A Beginner's Guide](https://www.datacamp.com/blog/what-is-a-graph-database)
- [@article@Graph database](https://en.wikipedia.org/wiki/Graph_database)
- [@video@Introduction to NoSQL](https://www.youtube.com/watch?v=qI_g07C_Q5I)

## Hbase

# HBase

HBase is a column-oriented No-SQL database management system that runs on top of Hadoop Distributed File System (HDFS), a main component of Apache Hadoop. HBase provides a fault-tolerant way of storing sparse data sets, which are common in many big data use cases. It is well suited for real-time data processing or random read/write access to large volumes of data. HBase applications are written in Java™ much like a typical Apache MapReduce application.

Visit the following resources to learn more:

- [@official@Apacha HBase?](https://hbase.apache.org/)
- [@article@What is HBase?](https://www.ibm.com/think/topics/hbase)
- [@article@Apache HBase](https://en.wikipedia.org/wiki/Apache_HBase)

## Hdfs

# HDFS

HDFS (Hadoop Distributed File System) is Hadoop’s primary storage system. It is designed to reliably store data across a cluster of machines. Its architecture is set up for this type of access to large datasets and is optimized for fault tolerance, scalability, and data locality.

Visit the following resources to learn more:

- [@official@HDFS Architecture Guide](https://hadoop.apache.org/docs/r1.2.1/hdfs_design.html)
- [@article@Hadoop Distributed File System (HDFS)](https://www.databricks.com/glossary/hadoop-distributed-file-system-hdfs)
- [@article@What is Hadoop Distributed File System (HDFS)?](https://www.ibm.com/think/topics/hdfs)

## Hdfs

# HDFS

HDFS (Hadoop Distributed File System) is Hadoop’s primary storage system. It is designed to reliably store data across a cluster of machines. Its architecture is set up for this type of access to large datasets and is optimized for fault tolerance, scalability, and data locality.

Visit the following resources to learn more:

- [@official@HDFS Architecture Guide](https://hadoop.apache.org/docs/r1.2.1/hdfs_design.html)
- [@article@Hadoop Distributed File System (HDFS)](https://www.databricks.com/glossary/hadoop-distributed-file-system-hdfs)
- [@article@What is Hadoop Distributed File System (HDFS)?](https://www.ibm.com/think/topics/hdfs)

## Hightouch

# Hightouch

Hightouch is a reverse ETL and AI platform crafted for marketing and personalization, allowing companies to uncover insights, execute campaigns, and develop AI agents using their data. It features an AI Decisioning Platform for lifecycle marketing and a Composable Customer Data Platform (CDP) that is adaptable, secure, and quick to deploy, built on top of a data warehouse.

Visit the following resources to learn more:

- [@official@Hightouch Docs](https://hightouch.com/docs)
- [@video@What is Hightouch? - The Data Activation Platform](https://www.youtube.com/watch?v=vMm87-MC7og)

## Horizontal Vs Vertical Scaling

# Horizontal vs Vertical Scaling

Horizontal scaling is the process of adding more machines or nodes to an existing pool in a system to distribute the workload and address increased load.

By contrast, vertical scaling involves increasing the computing power of individual machines in a system. This is achieved by adjusting or upgrading hardware components, such as CPU, RAM, and network speed.

Visit the following resources to learn more:

- [@article@Horizontal Vs. Vertical Scaling: Which Should You Choose?](https://www.cloudzero.com/blog/horizontal-vs-vertical-scaling/)
- [@video@Vertical Vs Horizontal Scaling: Key Differences You Should Know](https://www.youtube.com/watch?v=dvRFHG2-uYs)

## Hybrid

# Hybrid

Hybrid data ingestion combines aspects of both real-time and batch ingestion. This approach gives you the flexibility to adapt your data ingestion strategy as your needs evolve. For example, you could process data in real-time for critical applications and in batches for less time-sensitive tasks. Two common hybrid methods are Lambda architecture-based and micro-batching.

Visit the following resources to learn more:

- [@article@What is Data Ingestion: Types, Tools, and Real-Life Use Cases](https://estuary.dev/blog/data-ingestion/)
- [@article@Lambda Architecture](https://www.databricks.com/glossary/lambda-architecture)
- [@article@What is Micro Batching: A Comprehensive Guide 101](https://hevodata.com/learn/micro-batching/)

## Idempotency

# Idempotency

Idempotency is a crucial concept in IaC. An idempotent operation produces the same result regardless of how many times it’s executed. In the context of IaC, this means that applying the same configuration multiple times should not change the end state of the system. The role of idempotency in IaC scripts is to ensure consistency and prevent unintended side effects. For example, if a script to create a virtual machine (VM) is run twice, it should not create two VMs. Instead, it should recognize that the VM already exists and take no action.

Visit the following resources to learn more:

- [@article@Why idempotence was important to DevOps](https://dev.to/startpher/why-idempotence-was-important-to-devops-2jn3)
- [@article@Idempotency: The Secret to Seamless DevOps and Infrastructure](https://medium.com/@tiwari.sushil/idempotency-the-secret-to-seamless-devops-and-infrastructure-bf22e63e1be5)

## Indexing

# Indexing

Indexing is a data structure technique to efficiently retrieve data from a database. It essentially creates a lookup that can be used to quickly find the location of data records on a disk. Indexes are created using a few database columns and are capable of rapidly locating data without scanning every row in a database table each time the database table is accessed. Indexes can be created using any combination of columns in a database table, reducing the amount of time it takes to find data.

Indexes can be structured in several ways: Binary Tree, B-Tree, Hash Map, etc., each having its own particular strengths and weaknesses. When creating an index, it's crucial to understand which type of index to apply in order to achieve maximum efficiency. Indexes, like any other database feature, must be used wisely because they require disk space and need to be maintained, which can slow down insert and update operations.

## Infrastructure As Code   Iac

# Infrastructure as Code - IaC

Infrastructure as code (IaC) is the ability to provision and support your computing infrastructure using code instead of manual processes and settings. Manual infrastructure management is time-consuming and prone to error—especially when you manage applications at scale. Infrastructure as code lets you define your infrastructure's desired state without including all the steps to get to that state. It automates infrastructure management so developers can focus on building and improving applications instead of managing environments. Organizations use infrastructure as code to control costs, reduce risks, and respond with speed to new business opportunities.

Visit the following resources to learn more:

- [@article@What is Infrastructure as Code?](https://aws.amazon.com/what-is/iac/)
- [@article@Infrastructure as Code](https://en.wikipedia.org/wiki/Infrastructure_as_code)
- [@video@What is Infrastructure as Code?](https://www.youtube.com/watch?v=zWw2wuiKd5o)

## Integration Testing

# Integration Testing

Integration Testing is a type of testing where software modules are integrated logically and tested as a group. A typical software project consists of multiple software modules coded by different programmers. This testing level aims to expose defects in the interaction between these software modules when they are integrated. Integration Testing focuses on checking data communication amongst these modules.

Visit the following resources to learn more:

- [@article@Integration Testing Tutorial](https://www.guru99.com/integration-testing.html)
- [@feed@Explore top posts about Testing](https://app.daily.dev/tags/testing?ref=roadmapsh)

## Introduction

# Introduction

Data engineers are responsible for laying the foundations for the acquisition, storage, transformation, and management of data in an organization. They manage the design, creation, and maintenance of database architecture and data processing systems, ensuring that the subsequent work of analysis, BI, and machine learning model development can be carried out seamlessly, continuously, securely, and effectively.

Data engineers are one of the most technical profiles in the field of data science, bridging the gap between software and application developers and traditional data science positions.

Visit the following resources to learn more:

- [@article@How to Become a Data Engineer in 2025: 5 Steps for Career Success](https://www.datacamp.com/blog/how-to-become-a-data-engineer)
- [@video@What Does a Data Engineer ACTUALLY Do?](https://www.youtube.com/watch?v=hTjo-QVWcK0)

## Iot

# IoT

IoT, or Internet of Things, defines a network of connected devices interacting with their environment. IoT devices extend beyond standard devices such as PC's, Laptops or Smartphones, including smart locks, connected thermostats and temperature sensors. In industrial settings, this also includes connected machines, robots, and package tracking devices, and many more. IoT Devices measure and collect data about their environment and some also interact by performing certain predefined actions, for example turning the heat up or down.

Visit the following resources to learn more:

- [@article@What is the Internet of Things (IoT)?](https://www.ibm.com/think/topics/internet-of-things)
- [@article@Internet of Things](https://en.wikipedia.org/wiki/Internet_of_things)
- [@video@What is IoT (Internet of Things)? An Introduction](https://www.youtube.com/watch?v=4FxU-xpuCww)

## Java

# Java

Java has had a big influence on data engineering because many core big data tools and frameworks, like Hadoop, Spark (originally in Scala, which runs on the JVM), and Kafka, are built using Java or run on the Java Virtual Machine (JVM). This means Java’s performance, scalability, and cross-platform capabilities have shaped how large-scale data processing systems are designed.

Visit the following resources to learn more:

- [@book@Thinking in Java](https://www.amazon.co.uk/Thinking-Java-Eckel-Bruce-February/dp/B00IBON6C6)
- [@book@Java: The Complete Reference](https://www.amazon.co.uk/gp/product/B09JL8BMK7/ref=dbs_a_def_rwt_bibl_vppi_i2)
- [@article@@courseIntroduction to Java by Hyperskill (JetBrains Academy)](https://hyperskill.org/courses/8)
- [@article@Effective Java](https://www.amazon.com/Effective-Java-Joshua-Bloch/dp/0134685997)
- [@video@Java Tutorial for Beginners](https://www.youtube.com/watch?v=eIrMbAQSU34&feature=youtu.be)
- [@video@Java + DSA + Interview Preparation Course (For beginners)](https://www.youtube.com/playlist?list=PL9gnSGHSqcnr_DxHsP7AW9ftq0AtAyYqJ)
- [@feed@Explore top posts about Java](https://app.daily.dev/tags/java?ref=roadmapsh)

## Job Scheduling

# Job Scheduling

A scheduling system manages and distributes computational jobs across multiple interconnected computers (a cluster) to optimize resource utilization and job completion. The goal is to efficiently allocate cluster resources (like processors and memory) to incoming jobs based on factors such as user priority, job requirements, and deadlines.

Visit the following resources to learn more:

- [@article@Job scheduler](https://en.wikipedia.org/wiki/Job_scheduler)
- [@article@Cluster Resources — Job Scheduling](https://supun-kamburugamuve.medium.com/cluster-resources-job-scheduling-bb63644476bc)

## Key Value

# Key-Value

Key value databases, also known as key value stores, are NoSQL database types where data is stored as key value pairs and optimized for reading and writing that data. The data is fetched by a unique key or a number of unique keys to retrieve the associated value with each key. Both keys and values can be anything, ranging from simple objects to complex compound objects. Key-value databases are highly partitionable and allow horizontal scaling at a level that other types of databases cannot achieve.

Visit the following resources to learn more:

- [@article@What is a Key Value Database? - AWS](https://aws.amazon.com/nosql/key-value/)
- [@article@What Is A Key-Value Database? - MongoDB](https://www.mongodb.com/resources/basics/databases/key-value-database)

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

## Learn Sql

# Learn SQL Concepts

SQL stands for Structured Query Language. It is a standardized programming language designed to manage and interact with relational database management systems (RDBMS). SQL allows you to create, read, edit, and delete data stored in database tables by writing specific queries.

Visit the following resources to learn more:

- [@roadmap@Visit Dedicated SQL Roadmap](https://roadmap.sh/sql)
- [@article@SQL Tutorial - Essential SQL For The Beginners](https://www.sqltutorial.org/)

## Linux Basics

# Linux Basics

Knowledge of UNIX is a must for almost all kind of development as most of the code that you write is most likely going to be finally deployed on a UNIX/Linux machine. Linux has been the backbone of the free and open source software movement, providing a simple and elegant operating system for almost all your needs.

Visit the following resources to learn more:

- [@roadmap@Visit Dedicated Linux Roadmap](https://roadmap.sh/linux)
- [@course@Coursera - Unix Courses](https://www.coursera.org/courses?query=unix)
- [@article@Linux Basics](https://dev.to/rudrakshi99/linux-basics-2onj)
- [@article@Unix / Linux Tutorial](https://www.tutorialspoint.com/unix/index.htm)
- [@video@Linux Operating System - Crash Course](https://www.youtube.com/watch?v=ROjZy1WbCIA)
- [@feed@Explore top posts about Linux](https://app.daily.dev/tags/linux?ref=roadmapsh)

## Load Data

# Load Data

In the third step, the transformed data is moved from the staging area into the targe data storage solution, such as a data warehouse or data lake. For most organizations, the data loading process is automated, well-defined, continuous and batch-driven.

## Load Testing

# Load Testing

Load Testing is a type of Performance Testing that determines the performance of a system, software product, or software application under real-life-based load conditions. Load testing determines the behavior of the application when multiple users use it at the same time. It is the response of the system measured under varying load conditions.

Visit the following resources to learn more:

- [@article@Load testing and Best Practices](https://loadninja.com/load-testing/)
- [@feed@Explore top posts about Load Testing](https://app.daily.dev/tags/load-testing?ref=roadmapsh)

## Logs

# Logs

Logs are files that record events, activities, and system operations over time. They provide a detailed historical record of what has happened within a system, including timestamps, event details, performance data, errors, and user actions. Logs are crucial for troubleshooting problems, monitoring system health and performance, investigating security incidents, and understanding how users interact with a system.

## Looker

# Looker

Looker is a Google cloud-based business intelligence and data analytics platform. It allows users to explore, analyze, and visualize data to gain insights and make data-driven decisions. Looker is known for its ability to connect to various data sources, create custom dashboards, and generate reports. It also facilitates the integration of analytics, visualizations, and relevant information into business processes.

Visit the following resources to learn more:

- [@official@Looker business intelligence platform embedded analytics](https://cloud.google.com/looker)
- [@video@What is Looker?](https://www.youtube.com/watch?v=EmkNPAzla0Y&pp=0gcJCfwAo7VqN5tD)

## Luigi

# Luigi

Luigi is a powerful, easy-to-use open-source framework for building data pipelines with Python. It handles dependency resolution, workflow management, visualization etc. Luigi helps to build the data pipeline, typically associated with long-running batch processes.

Visit the following resources to learn more:

- [@official@Luigi Docs](https://luigi.readthedocs.io/)
- [@article@Getting Started with Luigi—What, Why & How](https://medium.com/big-data-processing/getting-started-with-luigi-what-why-how-f8e639a1f2a5)

## Machine Learning

# Machine Learning - A Key Concept for Data Analysts

Machine learning, a subset of artificial intelligence, is an indispensable tool in the hands of a data analyst. It provides the ability to automatically learn, improve from experience and make decisions without being explicitly programmed. In the context of a data analyst, machine learning contributes significantly in uncovering hidden insights, recognising patterns or making predictions based on large amounts of data. Through the use of varying algorithms and models, data analysts are able to leverage machine learning to convert raw data into meaningful information, making it a critical concept in data analysis.

Visit the following resources to learn more:

- [@article@What is Machine Learning (ML)?](https://www.ibm.com/topics/machine-learning)
- [@video@What is Machine Learning?](https://www.youtube.com/watch?v=9gGnTQTYNaE)

## Mapreduce

# MapReduce

MapReduce is a prominent data processing technique used by Data Analysts around the world. It allows them to handle large data sets with complex, unstructured data efficiently. MapReduce breaks down a big data problem into smaller sub-tasks (Map) and then takes those results to create an output in a more usable format (Reduce). This technique is particularly useful in conducting exploratory analysis, as well as in handling big data operations such as text processing, graph processing, or more complicated machine learning algorithms.

Visit the following resources to learn more:

- [@article@MapReduce](https://www.databricks.com/glossary/mapreduce)
- [@article@What is Apache MapReduce?](https://www.ibm.com/topics/mapreduce)

## Mariadb

# MariaDB

MariaDB server is a community developed fork of MySQL server. Started by core members of the original MySQL team, MariaDB actively works with outside developers to deliver the most feature rich, stable, and sanely licensed open SQL server in the industry. MariaDB was created with the intention of being a more versatile, drop-in replacement version of MySQL

Visit the following resources to learn more:

- [@official@MariaDB](https://mariadb.org/)
- [@article@MariaDB vs MySQL](https://www.guru99.com/mariadb-vs-mysql.html)
- [@video@MariaDB Tutorial For Beginners in One Hour](https://www.youtube.com/watch?v=_AMj02sANpI)
- [@feed@Explore top posts about Infrastructure](https://app.daily.dev/tags/infrastructure?ref=roadmapsh)

## Memcached

# Memcached

Memcached (pronounced variously mem-cash-dee or mem-cashed) is a general-purpose distributed memory-caching system. It is often used to speed up dynamic database-driven websites by caching data and objects in RAM to reduce the number of times an external data source (such as a database or API) must be read. Memcached is free and open-source software, licensed under the Revised BSD license. Memcached runs on Unix-like operating systems (Linux and macOS) and on Microsoft Windows. It depends on the `libevent` library. Memcached's APIs provide a very large hash table distributed across multiple machines. When the table is full, subsequent inserts cause older data to be purged in the least recently used (LRU) order. Applications using Memcached typically layer requests and additions into RAM before falling back on a slower backing store, such as a database.

Visit the following resources to learn more:

- [@opensource@memcached/memcached](https://github.com/memcached/memcached#readme)
- [@article@Memcached Tutorial](https://www.tutorialspoint.com/memcached/index.htm)
- [@video@Redis vs Memcached](https://www.youtube.com/watch?v=Gyy1SiE8avE)

## Messages Vs Streams

# Messages vs Streams

Messages and Streams are often used interchange‐ably but a subtle but essential differences exists between the two. A message is raw data communicated across two or more systems. Messages are discrete and singular signals in an event-driven system.

By contrast, a stream is an append-only log of event records. As events occur, streams are accumulated in an ordered sequence, using a timestamp or an ID to record events order. Streams are used when you need to analyze what happened over many events. Because of the append-only nature of streams, records in a stream are persisted over a long retention window—often weeks or months—allowing for complex operations on records such as aggregations on multiple records or the ability to rewind to a point in time within the stream.

## Messaging Systems

# Messaging Systems

Messaging systems, commonly known as messaging queus, make it possible for applications to communicate asynchronously, by sending messages to each other via a queue. A message queue provides temporary storage between the sender and the receiver so that the sender can keep operating without interruption when the destination program is busy or not connected.

Visit the following resources to learn more:

- [@article@Messaging Queues](https://aws.amazon.com/message-queue/)
- [@article@Messaging Queues Tutorial](https://www.tutorialspoint.com/inter_process_communication/inter_process_communication_message_queues.htm)

## Metadata First Architecture

# Metadata-first Architecture

## Metadata Management

# Metadata Management

## Microsoft Power Bi

# Microsoft Power BI

PowerBI, an interactive data visualization and business analytics tool developed by Microsoft, plays a crucial role in the field of a data analyst's work. It helps data analysts to convert raw data into meaningful insights through it's easy-to-use dashboards and reports function. This tool provides a unified view of business data, allowing analysts to track and visualize key performance metrics and make better-informed business decisions. With PowerBI, data analysts also have the ability to manipulate and produce visualizations of large data sets that can be shared across an organization, making complex statistical information more digestible.

Visit the following resources to learn more:

- [@official@Power BI](https://www.microsoft.com/en-us/power-platform/products/power-bi)
- [@video@Power BI for beginners](https://www.youtube.com/watch?v=NNSHu0rkew8)

## Mlops

# MLOps

MLOps is a practice for collaboration and communication between data scientists and operations professionals to help manage production ML lifecycle. It is a set of best practices that aims to automate the ML lifecycle, including training, deployment, and monitoring. MLOps helps organizations to scale ML models and deliver business value faster.

## Mobile Apps

# Mobile apps

Mobile apps are programs for phones and tablets, usually from app stores. They can be native (for one OS like iOS or Android), hybrid (web tech in a native shell), or cross-platform (like React Native). Apps use phone features like GPS and cameras. They do many things from games to shopping. Good mobile apps focus on easy use, speed, offline working, and security.

## Mongodb

# MongoDB

MongoDB is a NoSQL, open-source database designed for storing and managing large volumes of unstructured or semi-structured data. It uses a document-oriented data model where data is stored in BSON (Binary JSON) format, which allows for flexible and hierarchical data representation. Unlike traditional relational databases, MongoDB doesn't require a fixed schema, making it suitable for applications with evolving data requirements or varying data structures. It supports horizontal scaling through sharding and offers high availability with replica sets. MongoDB is commonly used for applications requiring rapid development, real-time analytics, and large-scale data handling, such as content management systems, IoT applications, and big data platforms.

Visit the following resources to learn more:

- [@roadmap@Visit Dedicated MongoDB Roadmap](https://roadmap.sh/mongodb)
- [@official@MongoDB Website](https://www.mongodb.com/)
- [@official@Learning Path for MongoDB Developers](https://learn.mongodb.com/catalog)
- [@article@MongoDB Online Sandbox](https://mongoplayground.net/)
- [@feed@daily.dev MongoDB Feed](https://app.daily.dev/tags/mongodb)

## Monitoring

# Monitoring

Monitoring involves continuously observing and tracking the performance, availability, and health of systems, applications, and infrastructure. It typically includes collecting and analyzing metrics, logs, and events to ensure systems are operating within desired parameters. Monitoring helps detect anomalies, identify potential issues before they escalate, and provides insights into system behavior. It often involves tools and platforms that offer dashboards, alerts, and reporting features to facilitate real-time visibility and proactive management. Effective monitoring is crucial for maintaining system reliability, performance, and for supporting incident response and troubleshooting.

A few popular tools are Prometheus, Sentry, Datadog, and NewRelic.

Visit the following resources to learn more:

- [@article@Top Monitoring Tools](https://thectoclub.com/tools/best-application-monitoring-software/)
- [@feed@daily.dev Monitoring Feed](https://app.daily.dev/tags/monitoring)

## Ms Sql

# MS SQL

Microsoft SQL Server (MS SQL) is a relational database management system developed by Microsoft for managing and storing structured data. It supports a wide range of data operations, including querying, transaction management, and data warehousing. SQL Server provides tools and features for database design, performance optimization, and security, including support for complex queries through T-SQL (Transact-SQL), data integration with SQL Server Integration Services (SSIS), and business intelligence with SQL Server Analysis Services (SSAS) and SQL Server Reporting Services (SSRS). It is commonly used in enterprise environments for applications requiring reliable data storage, transaction processing, and reporting.

Visit the following resources to learn more:

- [@roadmap@Visit Dedicated SQL Roadmap](https://roadmap.sh/sql)
- [@official@MS SQL](https://www.microsoft.com/en-ca/sql-server/)
- [@article@Tutorials for SQL Server](https://docs.microsoft.com/en-us/sql/sql-server/tutorials-for-sql-server-2016?view=sql-server-ver15)
- [@video@SQL Server tutorial for beginners](https://www.youtube.com/watch?v=-EPMOaV7h_Q)

## Mysql

# MySQL

MySQL is an open-source relational database management system (RDBMS) known for its speed, reliability, and ease of use. It uses SQL (Structured Query Language) for database interactions and supports a range of features for data management, including transactions, indexing, and stored procedures. MySQL is widely used for web applications, data warehousing, and various other applications due to its scalability and flexibility. It integrates well with many programming languages and platforms, and is often employed in conjunction with web servers and frameworks in popular software stacks like LAMP (Linux, Apache, MySQL, PHP/Python/Perl). MySQL is maintained by Oracle Corporation and has a large community and ecosystem supporting its development and use.

Visit the following resources to learn more:

- [@official@MySQL](https://www.mysql.com/)
- [@article@MySQL for Developers](https://planetscale.com/courses/mysql-for-developers/introduction/course-introduction)
- [@article@MySQL Tutorial](https://www.mysqltutorial.org/)
- [@video@MySQL Complete Course](https://www.youtube.com/watch?v=5OdVJbNCSso)
- [@feed@Explore top posts about MySQL](https://app.daily.dev/tags/mysql?ref=roadmapsh)

## Neo4J

# NEO4J

Neo4j is a highly popular open-source graph database designed to store, manage, and query data as interconnected nodes and relationships. Unlike traditional relational databases that use tables and rows, Neo4j uses a graph model where data is represented as nodes (entities) and edges (relationships), allowing for highly efficient querying of complex, interconnected data. It supports Cypher, a declarative query language specifically designed for graph querying, which simplifies operations like traversing relationships and pattern matching. Neo4j is well-suited for applications involving complex relationships, such as social networks, recommendation engines, and fraud detection, where understanding and leveraging connections between data points is crucial.

Visit the following resources to learn more:

- [@official@Neo4j Website](https://neo4j.com)
- [@video@Neo4j in 100 Seconds](https://www.youtube.com/watch?v=T6L9EoBy8Zk)
- [@video@Neo4j Course for Beginners](https://www.youtube.com/watch?v=_IgbB24scLI)
- [@feed@Explore top posts about Backend Development](https://app.daily.dev/tags/backend?ref=roadmapsh)

## Neptune

# AWS Neptune

Amazon Neptune is a fully managed graph database service provided by Amazon Web Services (AWS). It's designed to store and navigate highly connected data, supporting both property graph and RDF (Resource Description Framework) models. Neptune uses graph query languages like Gremlin and SPARQL, making it suitable for applications involving complex relationships, such as social networks, recommendation engines, fraud detection systems, and knowledge graphs. It offers high availability, with replication across multiple Availability Zones, and supports up to 15 read replicas for improved performance. Neptune integrates with other AWS services, provides encryption at rest and in transit, and offers fast recovery from failures. Its scalability and performance make it valuable for handling large-scale, complex data relationships in enterprise-level applications.

Visit the following resources to learn more:

- [@official@AWS Neptune](https://aws.amazon.com/neptune/)
- [@article@Setting Up Amazon Neptune Graph Database](https://cliffordedsouza.medium.com/setting-up-amazon-neptune-graph-database-2b73512a7388)
- [@video@Getting Started with Neptune Serverless](https://www.youtube.com/watch?v=b04-jjM9t4g)

## Networking Fundamentals

# Networking

Networking is the process of connecting two or more computing devices together for the purpose of sharing data. In a data network, shared data may be as simple as a printer or as complex as a global financial transaction.

If you have networking experience or want to be a reliability engineer or operations engineer, expect questions from these topics. Otherwise, this is just good to know.

Visit the following resources to learn more:

- [@article@Khan Academy - Networking](https://www.khanacademy.org/computing/code-org/computers-and-the-internet)
- [@video@Computer Networking Course - Network Engineering](https://www.youtube.com/watch?v=qiQR5rTSshw)
- [@video@Networking Video Series (21 videos)](https://www.youtube.com/playlist?list=PLEbnTDJUr_IegfoqO4iPnPYQui46QqT0j)
- [@feed@Explore top posts about Networking](https://app.daily.dev/tags/networking?ref=roadmapsh)

## New Relic

# New Relic

New Relic is an observability platform that helps you build better software. You can bring in data from any digital source so that you can fully understand your system and how to improve it.

Visit the following resources to learn more:

- [@official@New Relic](https://newrelic.com/)
- [@official@Learn New Relic](https://learn.newrelic.com/)
- [@feed@Explore top posts about DevOps](https://app.daily.dev/tags/devops?ref=roadmapsh)

## Nosql Databsases

# NoSQL databases

NoSQL databases are a category of database management systems designed for handling unstructured, semi-structured, or rapidly changing data. Unlike traditional relational databases, which use fixed schemas and SQL for querying, NoSQL databases offer flexible data models and can be classified into several types:

1.  **Document Stores**: Store data in JSON, BSON, or XML formats, allowing for flexible and hierarchical data structures (e.g., MongoDB, CouchDB).
2.  **Key-Value Stores**: Store data as key-value pairs, suitable for high-speed read and write operations (e.g., Redis, Riak).
3.  **Column-Family Stores**: Store data in columns rather than rows, which is useful for handling large volumes of data and wide columnar tables (e.g., Apache Cassandra, HBase).
4.  **Graph Databases**: Optimize the storage and querying of data with complex relationships using graph structures (e.g., Neo4j, Amazon Neptune).

NoSQL databases are often used for applications requiring high scalability, flexibility, and performance, such as real-time analytics, content management systems, and distributed data storage.

Visit the following resources to learn more:

- [@article@NoSQL Explained](https://www.mongodb.com/nosql-explained)
- [@video@How do NoSQL Databases work](https://www.youtube.com/watch?v=0buKQHokLK8)
- [@video@SQL vs NoSQL Explained](https://www.youtube.com/watch?v=ruz-vK8IesE)
- [@feed@Explore top posts about NoSQL](https://app.daily.dev/tags/nosql?ref=roadmapsh)

## Oltp Vs Olap

# OLTP vs OLAP

Online Transaction Processing (OLTP) refers to a class of systems designed to manage transaction-oriented applications, typically for data entry and retrieval transactions in database systems. OLTP systems are characterized by a large number of short online transactions (INSERT, UPDATE, DELETE), where the emphasis is on speed, efficiency, and maintaining data integrity in multi-access environments. PostgreSQL supports OLTP workloads through features like ACID compliance (Atomicity, Consistency, Isolation, Durability), MVCC (Multi-Version Concurrency Control) for high concurrency, efficient indexing, and robust transaction management. These features ensure reliable, fast, and consistent processing of high-volume, high-frequency transactions critical to OLTP applications.

Online Analytical Processing (OLAP) refers to a class of systems designed for query-intensive tasks, typically used for data analysis and business intelligence. OLAP systems handle complex queries that aggregate large volumes of data, often from multiple sources, to support decision-making processes.

Visit the following resources to learn more:

- [@article@What is OLTP?](https://www.oracle.com/uk/database/what-is-oltp/)
- [@article@What is OLAP? - Online Analytical Processing Explained](https://aws.amazon.com/what-is/olap/)
- [@video@OLTP vs OLAP](https://www.youtube.com/watch?v=iw-5kFzIdgY)

## Onehouse

# Onehouse

Onehouse Managed Lakehouse is a cloud-native SaaS product built on top of Apache Hudi. It replaces painful, inefficient do-iy-yourseld data lake management around file sizing, masking, deletion, clustering, access control, caching, etc. with foundational data infrastructure as a service, to ingest, store, optimize and transform your data on industry-leading open data formats.

Visit the following resources to learn more:

- [@official@Onehouse](https://www.onehouse.ai/)

## Opentofu

# OpenTofu

OpenTofu is an infrastructure as code tool that lets you define both cloud and on-prem resources in human-readable configuration files that you can version, reuse, and share. You can then use a consistent workflow to provision and manage all of your infrastructure throughout its lifecycle. OpenTofu can manage low-level components like compute, storage, and networking resources, as well as high-level components like DNS entries and SaaS features.

Visit the following resources to learn more:

- [@official@OpenTofu Docs](https://opentofu.org/docs/)
- [@video@OpenWhat is OpenTofu ?Explained with Demo](https://www.youtube.com/watch?v=6eHV63BVqmA)

## Oracle

# Oracle

Oracle Database is a highly robust, enterprise-grade relational database management system (RDBMS) developed by Oracle Corporation. Known for its scalability, reliability, and comprehensive features, Oracle Database supports complex data management tasks and mission-critical applications. It provides advanced functionalities like SQL querying, transaction management, high availability through clustering, and data warehousing. Oracle's database solutions include support for various data models, such as relational, spatial, and graph, and offer tools for security, performance optimization, and data integration. It is widely used in industries requiring large-scale, secure, and high-performance data processing.

Visit the following resources to learn more:

- [@official@Oracle Website](https://www.oracle.com/database/)
- [@official@Oracle Docs](https://docs.oracle.com/en/database/index.html)
- [@video@Oracle SQL Tutorial for Beginners](https://www.youtube.com/watch?v=ObbNGhcxXJA)
- [@feed@Explore top posts about Oracle](https://app.daily.dev/tags/oracle?ref=roadmapsh)

## Perfect

# Prefect

Prefect is an open-source orchestration engine that turns your Python functions into production-grade data pipelines with minimal friction. You can build and schedule workflows in pure Python—no DSLs or complex config files—and run them anywhere you can run Python. Prefect handles the heavy lifting for you out of the box: automatic state tracking, failure handling, real-time monitoring, and more.

Visit the following resources to learn more:

- [@official@Prefect Docs](https://docs.prefect.io/v3/get-started)
- [@video@Getting Started with Prefect](https://www.youtube.com/watch?v=D5DhwVNHWeU)

## Postgresql

# PostgreSQL

PostgreSQL is an advanced, open-source relational database management system (RDBMS) known for its robustness, extensibility, and standards compliance. It supports a wide range of data types and advanced features, including complex queries, foreign keys, and full-text search. PostgreSQL is highly extensible, allowing users to define custom data types, operators, and functions. It supports ACID (Atomicity, Consistency, Isolation, Durability) properties for reliable transaction processing and offers strong support for concurrency and data integrity. Its capabilities make it suitable for various applications, from simple web apps to large-scale data warehousing and analytics solutions.

Visit the following resources to learn more:

- [@roadmap@Visit Dedicated PostgreSQL DBA Roadmap](https://roadmap.sh/postgresql-dba)
- [@official@Official Website](https://www.postgresql.org/)
- [@article@Learn PostgreSQL - Full Tutorial for Beginners](https://www.postgresqltutorial.com/)
- [@video@PostgreSQL in 100 Seconds](https://www.youtube.com/watch?v=n2Fluyr3lbc)
- [@video@Postgres tutorial for Beginners](https://www.youtube.com/watch?v=SpfIwlAYaKk)
- [@feed@Explore top posts about PostgreSQL](https://app.daily.dev/tags/postgresql?ref=roadmapsh)

## Programming Skills

# Programming Skills

To be successful as a data engineer, you need to be proficient in coding. This involves knowning basic concepts and principles that form the foundation of any computer programming language. These include understanding variables, which store data for processing, control structures such as loops and conditional statements that direct the flow of a program, data structures which organize and store data efficiently, and algorithms which step by step instructions to solve specific problems or perform specific tasks.

## Prometheus

# Prometheus

Prometheus is a free software application used for event monitoring and alerting. It records real-time metrics in a time series database built using a HTTP pull model, with flexible queries and real-time alerting.

Visit the following resources to learn more:

- [@official@Prometheus Website](https://prometheus.io/)
- [@official@Prometheus Documentation](https://prometheus.io/docs/introduction/overview/)
- [@official@Getting Started with Prometheus](https://prometheus.io/docs/tutorials/getting_started/)
- [@feed@Explore top posts about Prometheus](https://app.daily.dev/tags/prometheus?ref=roadmapsh)

## Python

# Python

Python’s inherent characteristics and the wealth of resources that have grown around it have made it the data engineer’s language of choice. Python is a high-level, interpreted, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation. Python is dynamically-typed and garbage-collected.

Visit the following resources to learn more:

- [@official@Python Website](https://www.python.org/)
- [@article@Python - Wiki](https://en.wikipedia.org/wiki/Python_(programming_language))
- [@article@Tutorial Series: How to Code in Python](https://www.digitalocean.com/community/tutorials/how-to-write-your-first-python-3-program)
- [@article@Google's Python Class](https://developers.google.com/edu/python)
- [@video@Learn Python - Full Course](https://www.youtube.com/watch?v=4M87qBgpafk)
- [@feed@Explore top posts about Python](https://app.daily.dev/tags/python?ref=roadmapsh)

## Rabbitmq

# RabbitMQ

RabbitMQ is an open-source message broker that facilitates the exchange of messages between distributed systems using the Advanced Message Queuing Protocol (AMQP). It enables asynchronous communication by queuing and routing messages between producers and consumers, which helps decouple application components and improve scalability and reliability. RabbitMQ supports features such as message durability, acknowledgments, and flexible routing through exchanges and queues. It is highly configurable, allowing for various messaging patterns, including publish/subscribe, request/reply, and point-to-point communication. RabbitMQ is widely used in enterprise environments for handling high-throughput messaging and integrating heterogeneous systems.

Visit the following resources to learn more:

- [@official@RabbitMQ Tutorials](https://www.rabbitmq.com/getstarted.html)
- [@video@RabbitMQ Tutorial - Message Queues and Distributed Systems](https://www.youtube.com/watch?v=nFxjaVmFj5E)
- [@video@RabbitMQ in 100 Seconds](https://m.youtube.com/watch?v=NQ3fZtyXji0)
- [@feed@Explore top posts about RabbitMQ](https://app.daily.dev/tags/rabbitmq?ref=roadmapsh)

## Realtime

# Realtime

Real-time processing, also known as streaming processing, involves the immediate ingestion, as well as analysis, of data as it is generated, providing instantaneous insights and enabling timely decisions in time-sensitive applications like financial trading, medical monitoring, and autonomous vehicles. This differs from batch processing, which handles data in later batches, and typically involves continuous data streaming, low latency, and high availability to deliver immediate outcomes for critical tasks.

## Redis

# Redis

Redis is an open-source, in-memory data structure store known for its speed and versatility. It supports various data types, including strings, lists, sets, hashes, and sorted sets, and provides functionalities such as caching, session management, real-time analytics, and message brokering. Redis operates as a key-value store, allowing for rapid read and write operations, and is often used to enhance performance and scalability in applications. It supports persistence options to save data to disk, replication for high availability, and clustering for horizontal scaling. Redis is widely used for scenarios requiring low-latency access to data and high-throughput performance.

Visit the following resources to learn more:

- [@roadmap@Visit Dedicated Redis Roadmap](https://roadmap.sh/redis)
- [@course@Redis Crash Course](https://www.youtube.com/watch?v=XCsS_NVAa1g)
- [@official@Redis](https://redis.io/)
- [@official@Redis Documentation](https://redis.io/docs/latest/)
- [@video@Redis in 100 Seconds](https://www.youtube.com/watch?v=G1rOthIU-uo)
- [@feed@Explore top posts about Redis](https://app.daily.dev/tags/redis?ref=roadmapsh)

## Relational Databases

# Relational Databases

Relational databases are a type of database management system (DBMS) that organizes data into structured tables with rows and columns, using a schema to define data relationships and constraints. They employ Structured Query Language (SQL) for querying and managing data, supporting operations such as data retrieval, insertion, updating, and deletion. Relational databases enforce data integrity through keys (primary and foreign) and constraints (such as unique and not-null), and they are designed to handle complex queries, transactions, and data relationships efficiently. Examples of relational databases include MySQL, PostgreSQL, and Oracle Database. They are commonly used for applications requiring structured data storage, strong consistency, and complex querying capabilities.

Visit the following resources to learn more:

- [@course@Databases and SQL](https://www.edx.org/course/databases-5-sql)
- [@article@Relational Databases](https://www.ibm.com/cloud/learn/relational-databases)
- [@article@51 Years of Relational Databases](https://learnsql.com/blog/codd-article-databases/)
- [@article@Intro To Relational Databases](https://www.udacity.com/course/intro-to-relational-databases--ud197)
- [@video@What is Relational Database](https://youtu.be/OqjJjpjDRLc)
- [@feed@Explore top posts about Backend Development](https://app.daily.dev/tags/backend?ref=roadmapsh)

## Reusability

# Reusability

One of the goals of Infrastructure as Code (IaC) is to creat modular, standardized units of code—like modules or templates that can be used across multiple projects, environments, and teams, embodying the "Don't Repeat Yourself" (DRY) principle. This approach significantly boosts efficiency, consistency, and maintainability, as it allows for rapid deployment of identical infrastructure patterns, enforces organizational standards, simplifies complex setups, and improves collaboration by providing shared, tested building blocks for infrastructure management.

Visit the following resources to learn more:

- [@article@What is Infrastructure as Code (IaC)?](https://www.redhat.com/en/topics/automation/what-is-infrastructure-as-code-iac)

## Reverse Etl Usecases

# Reverse ETL Usecases

## Reverse Etl

# Reverse ETL

Reverse ETL is the process of extracting data from a data warehouse, transforming it to fit the requirements of operational systems, and then loading it into those other systems. This approach contrasts with traditional ETL, where data is extracted from operational systems, transformed, and loaded into a data warehouse.

Visit the following resources to learn more:

- [@article@What is Reverse ETL? A Helpful Guide](https://www.datacamp.com/blog/reverse-etl)
- [@video@What is Reverse ETL?](https://www.youtube.com/watch?v=DRAGfc5or2Y)

## S3 Storage

# S3

Amazon S3 (Simple Storage Service) is an object storage service offered by Amazon Web Services (AWS). It provides scalable, secure and durable storage on the internet. Designed for storing and retrieving any amount of data from anywhere on the web, it is a key tool for many companies in the field of data storage, including mobile applications, websites, backup and restore, archive, enterprise applications, IoT devices, and big data analytics.

Visit the following resources to learn more:

- [@official@S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html)

## Scala

# Scala

Scala is a programming language that combines the strengths of object-oriented and functional programming, and it runs on the Java Virtual Machine (JVM). In data engineering, Scala is especially important because Apache Spark, one of the most popular big data processing frameworks, was written in Scala. This means Scala can use Spark’s features directly and efficiently, often with cleaner and more concise code than Java. Its ability to handle complex data transformations with less code makes it a powerful tool for building fast, scalable data pipelines.

Visit the following resources to learn more:

- [@official@The Scala Programming Language](https://www.scala-lang.org/)
- [@article@Scala for Beginners: An Introduction](https://daily.dev/blog/scala-for-beginners-an-introduction)
- [@video@Scala Tutorial](https://www.youtube.com/playlist?list=PLS1QulWo1RIagob5D6kMIAvu7DQC5VTh3)

## Segment

# Segment

Segment is an analytics platform that provides a single API for collecting, storing, and routing customer data from various sources. With Segment, data engineers can easily add analytics tracking to their app, without having to integrate with multiple analytics tools individually. Segment acts as a single point of integration, allowing developers to send data to multiple analytics tools with a single API.

Visit the following resources to learn more:

- [@official@flutter_segment](https://pub.dev/packages/flutter_segment)

## Sentry

# Sentry

Sentry tracks your software performance, measuring metrics like throughput and latency, and displaying the impact of errors across multiple systems. Sentry captures distributed traces consisting of transactions and spans, which measure individual services and individual operations within those services.

Visit the following resources to learn more:

- [@official@Sentry](https://sentry.io)
- [@official@Sentry Documentation](https://docs.sentry.io/)

## Serverless Options

# Serverless Options

Serverless data storage involves using cloud provider services for databases and object storage that automatically scale infrastructure and implement a consumption-based, pay-as-you-go model, eliminating the need for developers to manage, provision, or maintain any physical or virtual servers. This approach simplifies development, reduces operational overhead, and offers cost-effectiveness by charging only for the resources used, allowing teams to focus on applications rather than infrastructure management.

Visit the following resources to learn more:

- [@article@What Is Serverless Computing?](https://www.ibm.com/think/topics/serverless)

## Skills And Responsibilities

# Skills and Responsibilities

Here’s a list of essential data engineering skills:

1.  SQL & Database Management: Ability to query, manipulate, and design relational databases efficiently using SQL. This is the bread-and-butter for extracting, transforming, and analyzing data.
    
2.  Data Modeling: Designing schemas and structures (star, snowflake, normalized forms) to optimize storage, performance, and usability of data.
    
3.  ETL/ELT Development: Building Extract-Transform-Load (or Load-Transform) pipelines to move and reshape data between systems while ensuring quality and consistency.
    
4.  Big Data Frameworks: Proficiency with tools like Apache Spark, Hadoop, or Flink to process and analyze massive datasets in distributed environments.
    
5.  Cloud Platforms: Working knowledge of AWS, Azure, or GCP for storage, compute, and orchestration (e.g., S3, BigQuery, Dataflow, Redshift).
    
6.  Data Warehousing: Understanding concepts and tools (Snowflake, BigQuery, Redshift) for centralizing, optimizing, and querying large volumes of business data.
    
7.  Workflow Orchestration: Using tools like Apache Airflow, Prefect, or Dagster to automate and schedule complex data pipelines reliably.
    
8.  Scripting & Programming: Strong skills in Python or Scala for building data processing scripts, automation tasks, and integration with APIs.
    
9.  Data Governance & Security: Applying practices for data quality, lineage tracking, access control, compliance (GDPR, HIPAA), and encryption.
    
10.  Monitoring & Performance Optimization: Setting up alerts, logging, and tuning pipelines to ensure they run efficiently, catch errors early, and scale smoothly.

Visit the following resources to learn more:

- [@article@Top Data Engineer Skills and Responsibilities](https://www.simplilearn.com/data-engineer-role-article)
- [@article@5 Essential Data Engineering Skills For 2025](https://www.datacamp.com/blog/essential-data-engineering-skills)
- [@video@What skills do you need as a Data Engineer?](https://www.youtube.com/watch?v=sF04UxNAvmg)

## Slowly Changing Dimension   Scd

# Slowly Changing Dimension - SCD

Slowly Changing Dimensions (SCDs) are a data warehousing technique used to track changes in dimension data over time. Instead of simply overwriting old data with new data, SCDs allow you to maintain historical records of how dimension attributes have changed. This is crucial for accurate analysis of historical trends and business performance.

Visit the following resources to learn more:

- [@article@WMastering Slowly Changing Dimensions (SCD)](https://www.datacamp.com/tutorial/mastering-slowly-changing-dimensions-scd)
- [@article@Implementing Slowly Changing Dimensions (SCDs) in Data Warehouses](https://www.sqlshack.com/implementing-slowly-changing-dimensions-scds-in-data-warehouses/)

## Smoke Testing

# Smoke Testing

Smoke Testing is a software testing process that determines whether the deployed software build is stable or not. Smoke testing is a confirmation for QA team to proceed with further software testing. It consists of a minimal set of tests run on each build to test software functionalities.

Visit the following resources to learn more:

- [@article@Smoke Testing | Software Testing](https://www.guru99.com/smoke-testing.html)
- [@feed@Explore top posts about Testing](https://app.daily.dev/tags/testing?ref=roadmapsh)

## Snowflake

# Snowflake

Snowflake is a cloud-based data platform that provides a data warehouse as a service. It allows organizations to store, analyze, and share data, offering features like data engineering, data governance, and collaboration capabilities. Snowflake is known for its scalability, ease of use, and ability to handle diverse workloads, including data warehousing, data lakes, and machine learning.

Visit the following resources to learn more:

- [@official@Snowflake Docs](https://docs.snowflake.com/)
- [@official@Snowflake in 20 minutes](https://docs.snowflake.com/en/user-guide/tutorials/snowflake-in-20minutes)
- [@article@Snowflake Tutorial For Beginners: From Architecture to Running Databases](https://www.datacamp.com/tutorial/introduction-to-snowflake-for-beginners)
- [@video@Learn Snowflake in 2 Hours](https://www.youtube.com/watch?v=mP3QbYURT9k)

## Snowflake

# Snowflake

Snowflake is a cloud-based data platform that provides a data warehouse as a service. It allows organizations to store, analyze, and share data, offering features like data engineering, data governance, and collaboration capabilities. Snowflake is known for its scalability, ease of use, and ability to handle diverse workloads, including data warehousing, data lakes, and machine learning.

Visit the following resources to learn more:

- [@official@Snowflake Docs](https://docs.snowflake.com/)
- [@official@Snowflake in 20 minutes](https://docs.snowflake.com/en/user-guide/tutorials/snowflake-in-20minutes)
- [@article@Snowflake Tutorial For Beginners: From Architecture to Running Databases](https://www.datacamp.com/tutorial/introduction-to-snowflake-for-beginners)
- [@video@Learn Snowflake in 2 Hours](https://www.youtube.com/watch?v=mP3QbYURT9k)

## Sources Of Data

# Sources of Data

Sources of data are origins or locations from which data is collected, categorized as primary (direct, firsthand information) or secondary (collected by others). Common primary sources include surveys, interviews, experiments, and sensor data. Secondary sources encompass databases, published reports, government data, books, articles, and web data like social media posts. Data sources can also be classified as internal (within an organization) or external (from outside sources).

## Star Vs Snowflake Schema

# Star vs Snowflake Schema

A star schema is a way to organize data in a database, namely in data warehouses, to make it easier and faster to analyze. At the center, there's a main table called the **fact table**, which holds measurable data like sales or revenue. Around it are **dimension tables**, which add details like product names, customer info, or dates. This layout forms a star-like shape.

A snowflake schema is another way of organizing data. In this schema, dimension tables are split into smaller sub-dimensions to keep data more organized and detailed, just like snowflakes in a large lake.

The star schema is simple and fast -ideal when you need to extract data for analysis quickly. On the other hand, the snowflake schema is more detailed. It prioritizes storage efficiency and managing complex data relationships.

Visit the following resources to learn more:

- [@official@Star Schema vs Snowflake Schema: Differences & Use Cases](https://www.datacamp.com/blog/star-schema-vs-snowflake-schema)

## Streaming

# Streaming

Streaming processing, also known as real-time processing, involves the immediate ingestion, as well as analysis, of data as it is generated, providing instantaneous insights and enabling timely decisions in time-sensitive applications like financial trading, medical monitoring, and autonomous vehicles. This differs from batch processing, which handles data in later batches, and typically involves continuous data streaming, low latency, and high availability to deliver immediate outcomes for critical tasks.

## Streamlit

# Streamlit

Streamlit is a free and open-source framework to rapidly build and share machine learning and data science web apps. It is a Python-based library specifically designed for data and machine learning engineers. Data scientists or machine learning engineers are not web developers and they're not interested in spending weeks learning to use these frameworks to build web apps. Instead, they want a tool that is easier to learn and to use, as long as it can display data and collect needed parameters for modeling.

Visit the following resources to learn more:

- [@official@Streamlit Docs](https://docs.streamlit.io/)
- [@official@Streamlit Python: Tutorial](https://www.datacamp.com/tutorial/streamlit)
- [@video@EStreamlit Explained: Python Tutorial for Data Scientists](https://www.youtube.com/watch?v=c8QXUrvSSyg)

## Tableu

# Tableau

Tableau is a powerful data visualization tool utilized extensively by data analysts worldwide. Its primary role is to transform raw, unprocessed data into an understandable format without any technical skills or coding. Data analysts use Tableau to create data visualizations, reports, and dashboards that help businesses make more informed, data-driven decisions. They also use it to perform tasks like trend analysis, pattern identification, and forecasts, all within a user-friendly interface. Moreover, Tableau's data visualization capabilities make it easier for stakeholders to understand complex data and act on insights quickly.

Visit the following resources to learn more:

- [@official@Tableau](https://www.tableau.com/en-gb)
- [@video@What is Tableau?](https://www.youtube.com/watch?v=NLCzpPRCc7U)

## Terraform

# Terraform

Terraform is an open-source infrastructure as code (IaC) tool developed by HashiCorp, used to define, provision, and manage cloud and on-premises infrastructure using declarative configuration files. It supports multiple cloud providers like AWS, Azure, and Google Cloud, as well as various services and platforms, enabling infrastructure automation across diverse environments. Terraform's state management and modular structure allow for efficient scaling, reusability, and version control of infrastructure. It is widely used for automating infrastructure provisioning, reducing manual errors, and improving infrastructure consistency and repeatability.

Visit the following resources to learn more:

- [@roadmap@Visit Dedicated Terraform Roadmap](https://roadmap.sh/terraform)
- [@course@Complete Terraform Course](https://www.youtube.com/watch?v=7xngnjfIlK4)
- [@official@Terraform Documentation](https://www.terraform.io/docs)
- [@official@Terraform Tutorials](https://learn.hashicorp.com/terraform)
- [@article@How to Scale Your Terraform Infrastructure](https://thenewstack.io/how-to-scale-your-terraform-infrastructure/)
- [@feed@Explore top posts about Terraform](https://app.daily.dev/tags/terraform?ref=roadmapsh)

## Testing

# Testing

Testing is a systematic process used to evaluate the functionality, performance, and quality of software or systems to ensure they meet specified requirements and standards. It involves various methodologies and levels, including unit testing (testing individual components), integration testing (verifying interactions between components), system testing (assessing the entire system's behavior), and acceptance testing (confirming it meets user needs). Testing can be manual or automated and aims to identify defects, validate that features work as intended, and ensure the system performs reliably under different conditions. Effective testing is critical for delivering high-quality software and mitigating risks before deployment.

Visit the following resources to learn more:

- [@article@What is Software Testing?](https://www.guru99.com/software-testing-introduction-importance.html)
- [@article@Testing Pyramid](https://www.browserstack.com/guide/testing-pyramid-for-test-automation)
- [@feed@Explore top posts about Testing](https://app.daily.dev/tags/testing?ref=roadmapsh)

## Tokenization

# Tokenization

Tokenization is the step where raw text is broken into small pieces called tokens, and each token is given a unique number. A token can be a whole word, part of a word, a punctuation mark, or even a space. The list of all possible tokens is the model’s vocabulary. Once text is turned into these numbered tokens, the model can look up an embedding for each number and start its math. By working with tokens instead of full sentences, the model keeps the input size steady and can handle new or rare words by slicing them into familiar sub-pieces. After the model finishes its work, the numbered tokens are turned back into text through the same vocabulary map, letting the user read the result.

Visit the following resources to learn more:

- [@article@Explaining Tokens — the Language and Currency of AI](https://blogs.nvidia.com/blog/ai-tokens-explained/)
- [@article@What is Tokenization? Types, Use Cases, Implementation](https://www.datacamp.com/blog/what-is-tokenization)

## Transactions

# Transactions

Transactions in SQL are units of work that group one or more database operations into a single, atomic unit. They ensure data integrity by following the ACID properties: Atomicity (all or nothing), Consistency (database remains in a valid state), Isolation (transactions don't interfere with each other), and Durability (committed changes are permanent). Transactions are essential for maintaining data consistency in complex operations and handling concurrent access to the database.

Visit the following resources to learn more:

- [@article@Transactions](https://www.tutorialspoint.com/sql/sql-transactions.htm)
- [@article@A Guide to ACID Properties in Database Management Systems](https://www.mongodb.com/resources/basics/databases/acid-transactions)

## Transform Data

# Transform Data

In the second step, ETL tools transform and consolidate the raw data in the staging area to prepare it for the target data warehouse. The data transformation phase is normally the most complex and prone to errors, as it can involved multiple transformations, including basic data cleaning operations, deduplication, cata casting, filtering, grouping, encrypting, and many more.

## Types Of Data Ingestion

# Types of Data Ingestion

The primary types of data ingestion are Batch, Streaming, and Hybrid. Batch ingestion processes data in large, scheduled chunks, suitable for non-time-sensitive tasks like monthly reports. Streaming (or Real-time) ingestion handles data as it arrives, ideal for time-sensitive applications such as fraud detection or IoT monitoring. Hybrid ingestion combines both methods, offering flexibility for diverse business needs.

## Unit Testing

# Unit Testing

Unit testing is where individual **units** (modules, functions/methods, routines, etc.) of software are tested to ensure their correctness. This low-level testing ensures smaller components are functionally sound while taking the burden off of higher-level tests. Generally, a developer writes these tests during the development process and they are run as automated tests.

Visit the following resources to learn more:

- [@article@Unit Testing Tutorial](https://www.guru99.com/unit-testing-guide.html)
- [@video@What is Unit Testing?](https://youtu.be/3kzHmaeozDI)
- [@feed@Explore top posts about Testing](https://app.daily.dev/tags/testing?ref=roadmapsh)

## What And Why Use Them

# What and why use them?

In data engineering, messaging systems act as central brokers for data communication, allowing different applications and services to send and receive data in a decoupled, scalable, and fault-tolerant way. They are crucial for handling high-volume, real-time data streams, building resilient data pipelines, and enabling event-driven architectures by acting as buffers and communication channels between data producers and consumers. Key benefits include decoupling systems for agility, ensuring data reliability through queuing and retries, and horizontal scalability to manage growing data loads, while common examples include Apache Kafka and message queues like RabbitMQ and AWS SQS.

## What Is Cluster Computing

# What is Cluster Computing

Cluster computing is a type of distributing computing where multiple computers are connected so they work together as a single system. By working together, a cluster of machines can address complex tasks with higher computational power and efficiency.

The term “cluster” refers to the network of linked computer systems programmed to perform the same task. Computing clusters typically consist of servers, workstations and personal computers (PCs) that communicate over a local area network (LAN) or a wide area network (WAN). Each computer or “node,” in a computer network has an operating system (OS) and a central processing unit (CPU) core that handles the tasks required for the software to run properly.

Visit the following resources to learn more:

- [@article@What is cluster computing? - IBM](https://www.ibm.com/think/topics/cluster-computing)
- [@article@What is cluster computing? - AWS](https://aws.amazon.com/what-is/cluster-computing/)
- [@article@Computer cluster - Wikipedia](http://en.wikipedia.org/wiki/Computer_cluster)
- [@video@WUnderstand the Basic Cluster Concepts](https://www.youtube.com/watch?v=8BBDxzJL6fY)

## What Is Data Engineering

# What is Data Engineering?

Data engineering is the practice of designing and building systems for the aggregation, storage and analysis of data at scale. Data engineers excel at creating and deploying algorithms, data pipelines and workflows that sort raw data into ready-to-use datasets. Data engineering is an integral component of the modern data platform and makes it possible for businesses to analyze and apply the data they receive, regardless of the data source or format.

Visit the following resources to learn more:

- [@article@What is data engineering?](https://www.ibm.com/think/topics/data-engineering)
- [@article@How to Become a Data Engineer in 2025: 5 Steps for Career Success](https://www.datacamp.com/blog/how-to-become-a-data-engineer)
- [@video@How Data Engineering Works?](https://www.youtube.com/watch?v=qWru-b6m030)

## What Is Data Warehouse

# Data Warehouse

**Data Warehouses** are data storage systems which are designed for analyzing, reporting and integrating with transactional systems. The data in a warehouse is clean, consistent, and often transformed to meet wide-range of business requirements. Hence, data warehouses provide structured data but require more processing and management compared to data lakes.

Visit the following resources to learn more:

- [@article@What Is a Data Warehouse?](https://www.oracle.com/database/what-is-a-data-warehouse/)
- [@video@What is a Data Warehouse?](https://www.youtube.com/watch?v=k4tK2ttdSDg)

## Yarn

# Apache Hadoop YARN

Apache Hadoop YARN (Yet Another Resource Negotiator) is the part of Hadoop that manages resources and runs jobs on a cluster. It has a ResourceManager that controls all cluster resources and an ApplicationMaster for each job that schedules and runs tasks. YARN lets different tools like MapReduce and Spark share the same cluster, making it more efficient, flexible, and reliable.

Visit the following resources to learn more:

- [@video@Hadoop Yarn Tutorial](https://www.youtube.com/watch?v=6bIF9VwRwE0)
