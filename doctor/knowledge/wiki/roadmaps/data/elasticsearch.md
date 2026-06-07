# Elasticsearch Roadmap

## Api Keys

# API Keys

API keys in Elasticsearch provide a mechanism for authentication and authorization, allowing users or applications to securely access Elasticsearch APIs. They are a more granular alternative to using usernames and passwords, enabling you to restrict access to specific resources and actions. API keys can be configured with specific roles and privileges, limiting what a user or application can do within the Elasticsearch cluster.

Visit the following resources to learn more:

- [@official@Elasticsearch API keys](https://www.elastic.co/docs/deploy-manage/api-keys/elasticsearch-api-keys)
- [@official@Create an API key](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-security-create-api-key)
- [@article@Creating API Keys in Elasticsearch: An Advanced Guide](https://opster.com/guides/elasticsearch/security/api-keys-in-elasticsearch/)

## Authentication

# Authentication

Authentication is the process of verifying the identity of a user or system attempting to access a resource. It ensures that only authorized individuals or applications can gain entry by requiring them to prove who they are, typically through credentials like usernames and passwords, API keys, or certificates. This process confirms that the user or system is indeed who they claim to be before granting access.

Visit the following resources to learn more:

- [@official@User authentication](https://www.elastic.co/docs/deploy-manage/users-roles/cluster-or-deployment-auth/user-authentication)
- [@official@Authentication](https://www.elastic.co/docs/api/doc/elasticsearch/authentication)
- [@official@Minimal security setup](https://www.elastic.co/docs/deploy-manage/security/set-up-minimal-security)
- [@article@Elasticsearch Basic Authentication for Cluster (EN)](https://medium.com/@kaangorur/elasticsearch-basic-authentication-for-cluster-en-3728ba7acf8a)
- [@article@Implementing Elasticsearch API Authentication for Enhanced Security](https://opster.com/guides/elasticsearch/security/elasticsearch-api-authentication/)
- [@video@File-Based Realm User Authentication | Elasticsearch Self-Managed | Support Troubleshooting](https://www.youtube.com/watch?v=sueO7sz1buw)
- [@video@Token Based Authentication Using API Keys to access Elasticsearch](https://www.youtube.com/watch?v=5vBa7AwfslE)

## Autoscaling

# Autoscaling

Autoscaling is the ability of a system to automatically adjust its resources (like compute, memory, or storage) based on the current demand. This means that the system can scale up (add more resources) when demand increases and scale down (remove resources) when demand decreases, all without manual intervention. This ensures optimal performance and cost efficiency by only using the resources that are actually needed.

Visit the following resources to learn more:

- [@official@Autoscaling](https://www.elastic.co/docs/deploy-manage/autoscaling)
- [@official@Autoscaling example](https://www.elastic.co/guide/en/cloud-enterprise/3.7/ece-autoscaling-example.html)
- [@article@Unlocking Elastic Scalability: A Comprehensive Guide to Enable Autoscaling in Elasticsearch](https://medium.com/@prosenjeet.saha88/unlocking-elastic-scalability-a-comprehensive-guide-to-enable-autoscaling-in-elasticsearch-ff6ab1000b65)
- [@video@Autoscale your Elastic Cloud deployment](https://www.youtube.com/watch?v=kS-_uJMxotU&t=14s)
- [@video@Autoscaling - Daily Elastic Byte S04E11](https://www.youtube.com/watch?v=g3_YddGpMrs&t=10s)

## Avg  Sum  Min  Max

# Avg, Sum, Min, and Max Aggregations

These aggregations are fundamental tools for calculating statistical summaries of numerical data. They compute the average (Avg), total (Sum), smallest value (Min), and largest value (Max) respectively, across a set of documents that match a query. These aggregations operate on numeric fields within your Elasticsearch indices, providing insights into the distribution and range of your data.

Visit the following resources to learn more:

- [@official@Aggregations](https://www.elastic.co/docs/explore-analyze/query-filter/aggregations)
- [@official@Avg aggregation](https://www.elastic.co/docs/reference/aggregations/search-aggregations-metrics-avg-aggregation)
- [@official@Sum aggregation](https://www.elastic.co/docs/reference/aggregations/search-aggregations-metrics-sum-aggregation)
- [@official@Max aggregation](https://www.elastic.co/docs/reference/aggregations/search-aggregations-metrics-max-aggregation)
- [@official@Min aggregation](https://www.elastic.co/docs/reference/aggregations/search-aggregations-metrics-min-aggregation)
- [@article@A Basic Guide To Elasticsearch Aggregations](https://logz.io/blog/elasticsearch-aggregations/)
- [@article@ElasticSearch Aggregation & Queries](https://medium.com/@souravchoudhary0306/elasticsearch-aggregation-queries-557131ef5ea4)
- [@video@Learn about elastic search aggregation in 15 minutes](https://www.youtube.com/watch?v=ZziIEDfA8ZE)

## Bm25 Algorithm

# BM25 Algorithm

BM25 (Best Matching 25) is a ranking function used by search engines to estimate the relevance of documents to a given search query. It's a bag-of-words retrieval function that scores documents based on the query terms appearing in each document, taking into account term frequency and document length. The algorithm adjusts for document length, preventing longer documents from being unfairly favored, and also considers how frequently a term appears in the entire collection of documents.

Visit the following resources to learn more:

- [@official@Practical BM25 - Part 1: How Shards Affect Relevance Scoring in Elasticsearch](https://www.elastic.co/blog/practical-bm25-part-1-how-shards-affect-relevance-scoring-in-elasticsearch)
- [@official@Practical BM25 — Part 2: The BM25 Algorithm and its variables](https://www.elastic.co/blog/practical-bm25-part-2-the-bm25-algorithm-and-its-variables)
- [@official@Practical BM25 - Part 3: Considerations for Picking b and k1 in Elasticsearch](https://www.elastic.co/blog/practical-bm25-part-3-considerations-for-picking-b-and-k1-in-elasticsearch)
- [@official@Improved Text Scoring with BM25](https://www.elastic.co/elasticon/conf/2016/sf/improved-text-scoring-with-bm25)
- [@article@Okapi BM25](https://en.wikipedia.org/wiki/Okapi_BM25)

## Boolean

# Boolean Data Type

A boolean data type represents a logical value, which can be either true or false. It's used to store binary information, indicating whether a condition is met or not, or representing a simple yes/no state. This data type is fundamental for filtering, decision-making, and representing flags within a dataset.

Visit the following resources to learn more:

- [@official@Boolean field type](https://www.elastic.co/docs/reference/elasticsearch/mapping-reference/boolean)

## Boosting Queries

# Boosting Queries

Boosting queries in Elasticsearch allows you to influence the relevance score of documents based on specific criteria. It works by increasing or decreasing the score of documents that match certain query clauses, effectively prioritizing some results over others. This helps to fine-tune search results to better align with user intent and improve the overall precision of your search.

Visit the following resources to learn more:

- [@official@Boosting query](https://www.elastic.co/docs/reference/query-languages/query-dsl/query-dsl-boosting-query)
- [@official@Relevance Tuning Guide, Weights and Boosts](https://www.elastic.co/guide/en/app-search/current/relevance-tuning-guide.html)
- [@article@Elasticsearch Boosting Query](https://opster.com/guides/elasticsearch/search-apis/boosting-query/)
- [@article@Elasticsearch Boosting Query - Syntax, Example, and Tips](https://pulse.support/kb/elasticsearch-boosting-query)

## Bulk Index

# Bulk Indexing

Bulk indexing in Elasticsearch is a way to send multiple indexing, updating, or deleting operations to the Elasticsearch cluster in a single request. Instead of sending each document individually, you batch them together, which significantly reduces the overhead of network communication and processing, leading to faster indexing speeds. This approach is particularly useful when dealing with large datasets or when needing to ingest data quickly.

Visit the following resources to learn more:

- [@official@Bulk index or delete documents](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-bulk)
- [@article@Tune for indexing speed](https://www.elastic.co/docs/deploy-manage/production-guidance/optimize-performance/indexing-speed)
- [@article@How to Index Elasticsearch Documents with the Bulk API in Python](http://towardsdatascience.com/how-to-index-elasticsearch-documents-with-the-bulk-api-in-python-b5bb01ed3824/)
- [@article@Optimizing Elasticsearch Bulk Indexing for High Performance](https://opster.com/guides/elasticsearch/how-tos/optimizing-elasticsearch-bulk-indexing-high-performance/)
- [@video@Bulk API for Multiple Document Indexing and Modification [ElasticSearch 7 for Beginners #3.3]](https://www.youtube.com/watch?v=6IYkfn9me-w)

## Cardinality

# Cardinality Aggregation

Cardinality aggregation is used to estimate the number of unique values in a field. It's particularly useful when you need to count distinct items but don't need the actual unique values themselves. This aggregation provides an approximate count, balancing accuracy with performance, especially when dealing with large datasets.

Visit the following resources to learn more:

- [@official@Cardinality aggregation](https://www.elastic.co/docs/reference/aggregations/search-aggregations-metrics-cardinality-aggregation)
- [@article@Elasticsearch Cardinality – Low + High Cardinality Fields](https://opster.com/guides/elasticsearch/data-architecture/elasticsearch-cardinality/)
- [@article@Elasticsearch Cardinality Aggregation - Syntax, Example, and Tips](https://pulse.support/kb/elasticsearch-cardinality-aggregation)
- [@video@Beginner’s Crash Course to Elastic Stack - Part 4: Aggregations](https://www.youtube.com/watch?v=iGKOdep1Iss&t=1184s)

## Cat Api

# CAT API

The CAT API in Elasticsearch provides a simple, human-readable way to access cluster-level information using a command-line interface or a RESTful API. It returns data in a tabular format, making it easy to understand and interpret the status, health, and performance metrics of your Elasticsearch cluster. This API is primarily used for monitoring and troubleshooting purposes.

Visit the following resources to learn more:

- [@official@Compact and aligned text (CAT)](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-cat)
- [@official@Get the cluster health status](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-cat-health)
- [@article@Mastering the Elasticsearch Cat API for Efficient Cluster Management](https://opster.com/guides/elasticsearch/search-apis/elasticsearch-cat-api/)
- [@article@Elasticsearch - Cat APIs](https://www.tutorialspoint.com/elasticsearch/elasticsearch_cat_apis.htm)

## Cluster Monitoring

# Cluster Monitoring

Cluster monitoring involves continuously observing the health, performance, and resource utilization of an Elasticsearch cluster. This process helps identify potential issues, bottlenecks, and anomalies that could impact the cluster's stability and responsiveness. Effective monitoring allows administrators to proactively address problems, optimize resource allocation, and ensure the cluster operates efficiently.

Visit the following resources to learn more:

- [@official@Monitoring](https://www.elastic.co/docs/deploy-manage/monitor)
- [@official@Track what's happening in your Elastic Stack](https://www.elastic.co/elasticsearch/monitoring)
- [@official@Stack monitoring](https://www.elastic.co/docs/deploy-manage/monitor/stack-monitoring)

## Cluster System

# Cluster (System)

A cluster is a collection of one or more Elasticsearch nodes that work together to store and process data. It provides a distributed and scalable system where data is divided into shards and distributed across multiple nodes for redundancy and performance. The cluster manages indexing, searching, and analysis operations across all nodes, presenting a unified view of the data to the user.

Visit the following resources to learn more:

- [@official@Deploy an Elasticsearch cluster](http://elastic.co/docs/deploy-manage/deploy/self-managed/installing-elasticsearch)
- [@official@Clusters, nodes, and shards](https://www.elastic.co/docs/deploy-manage/distributed-architecture/clusters-nodes-shards)
- [@article@How to setup and install Elasticsearch: From a single node to a cluster of nodes](http://severalnines.com/blog/how-to-setup-and-install-elasticsearch-cluster/)
- [@article@Mastering the Art of Elasticsearch Cluster Setup](https://opster.com/guides/elasticsearch/operations/elasticsearch-cluster-setup/)
- [@video@Elasticsearch basic concepts | cluster, shards, nodes | Elasticsearch tutorial for beginners](https://www.youtube.com/watch?v=GH6hO2L4LR0)

## Controlling Search Results

# Controlling Search Results

Controlling search results involves influencing the order and relevance of documents returned by a search query. This includes techniques to boost the score of certain documents, filter out unwanted results, and tailor the search experience to meet specific user needs. It allows for fine-tuning the search process beyond basic keyword matching.

Visit the following resources to learn more:

- [@official@Result Settings Guide](https://www.elastic.co/guide/en/app-search/current/result-settings-guide.html)
- [@official@Filter search results](https://www.elastic.co/docs/reference/elasticsearch/rest-apis/filter-search-results)
- [@article@Elasticsearch in Action: Manipulating Search Results](https://mkonda007.medium.com/elasticsearch-in-action-manipulating-search-results-6c312ea0495b)

## Coordinating Nodes

# Coordinating Nodes

Coordinating nodes in Elasticsearch are like traffic controllers. They receive client requests, route them to the appropriate data nodes that hold the relevant data shards, and then consolidate the results before sending them back to the client. These nodes don't hold any data themselves, but they play a crucial role in distributing the workload and ensuring efficient query execution across the cluster.

Visit the following resources to learn more:

- [@official@Coordinating node](https://www.elastic.co/docs/deploy-manage/distributed-architecture/clusters-nodes-shards/node-roles#coordinating-node)
- [@official@Coordinating only node](https://www.elastic.co/docs/deploy-manage/distributed-architecture/clusters-nodes-shards/node-roles#coordinating-only-node-role)

## Create Index

# Create Index

Creating an index in Elasticsearch using the Document API involves sending a PUT request to the Elasticsearch server. This request specifies the name of the index you want to create. You can also include settings and mappings in the request body to configure how the index should store and analyze your data. If the index doesn't already exist, Elasticsearch will create it based on the provided configuration. If the index exists, you will get an error.

Visit the following resources to learn more:

- [@official@Create an index](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-indices-create)
- [@article@Elasticsearch Index – How to create, list, query and delete indices](https://opster.com/guides/elasticsearch/glossary/elasticsearch-index/)
- [@article@10 Elastic Search Tutorial - How to Create Elastic Index and Settings](https://www.youtube.com/watch?v=74lS14dqyBs)
- [@video@09 Elastic Search Tutorial - How to create Index Document in Elastic Search](https://www.youtube.com/watch?v=YWDm6uNtk0U)

## Cross Cluster Replication

# Cross-Cluster Replication

Cross-cluster replication (CCR) allows you to replicate indices and their data from one Elasticsearch cluster to another. This enables scenarios like disaster recovery, where a secondary cluster can take over if the primary fails, and data locality, where data is replicated closer to users in different geographic regions for faster access. CCR ensures data consistency across clusters, providing a reliable and efficient way to maintain data availability and resilience.

Visit the following resources to learn more:

- [@official@Cross-cluster replication](https://www.elastic.co/docs/deploy-manage/tools/cross-cluster-replication)
- [@official@Set up cross-cluster replication](https://www.elastic.co/docs/deploy-manage/tools/cross-cluster-replication/set-up-cross-cluster-replication)
- [@official@Replicate Elasticsearch Data with Cross-Cluster Replication (CCR)](https://www.elastic.co/virtual-events/replicate-elasticsearch-data-cross-cluster-replication-ccr)
- [@official@Follow the Leader: An Introduction to Cross-Cluster Replication in Elasticsearch](https://www.elastic.co/blog/follow-the-leader-an-introduction-to-cross-cluster-replication-in-elasticsearch)
- [@video@Elasticsearch Cross-Cluster Replication (CCR)](https://www.youtube.com/watch?v=2Uwh-H_qazE)

## Custom Analyzers

# Custom Analyzers

Custom analyzers in Elasticsearch provide a way to define how text is processed both when indexing documents and when searching. They allow you to combine character filters, tokenizers, and token filters in a specific order to tailor the analysis process to your specific needs, such as handling language-specific nuances or removing unwanted characters. This customization ensures that your search results are more relevant and accurate.

Visit the following resources to learn more:

- [@official@Create a custom analyzer](https://www.elastic.co/docs/manage-data/data-store/text-analysis/create-custom-analyzer)
- [@official@Specify an analyzer](https://www.elastic.co/docs/manage-data/data-store/text-analysis/specify-an-analyzer)
- [@article@Mastering Elasticsearch Custom Analyzers for Enhanced Search Capabilities](https://opster.com/guides/elasticsearch/data-architecture/elasticsearch-custom-analyzers/)
- [@article@Custom analyzer building in Elasticsearch](https://medium.com/elasticsearch/custom-analyzer-building-in-elasticsearch-4e86f7c9c3be)
- [@video@Elasticsearch Custom Analyzers - V1](https://www.youtube.com/watch?v=0ZuRExiHn1A)

## Data Nodes

# Data Nodes

Data nodes in Elasticsearch are the workhorses of the cluster, responsible for storing data and performing CPU and I/O intensive operations like searching, indexing, and data analysis. These nodes hold shards of Elasticsearch indices and manage the actual data storage on disk. They contribute significantly to the cluster's overall performance and scalability.

Visit the following resources to learn more:

- [@official@Data nodes](https://www.elastic.co/docs/deploy-manage/distributed-architecture/clusters-nodes-shards/node-roles#data-node-role)

## Data Tiers

# Data Tiers

Data tiers in Elasticsearch refer to the strategy of categorizing and storing data based on its access frequency and importance. This approach involves segregating data into different storage types (like hot, warm, cold, and frozen) to optimize performance, cost, and resource utilization. By aligning data storage with its usage patterns, organizations can efficiently manage large volumes of data while maintaining acceptable query speeds and minimizing infrastructure expenses.

Visit the following resources to learn more:

- [@official@Data tiers](https://www.elastic.co/docs/manage-data/lifecycle/data-tiers)
- [@official@Elastic data tiering strategy: Optimizing for a resilient and efficient implementation](https://www.elastic.co/blog/elastic-data-tiering-strategy)
- [@official@What’s the difference? Elastic and Splunk data tiers](https://www.elastic.co/blog/elastic-splunk-data-tiers-differences)
- [@article@Elasticsearch Multi-Tier Architecture – How to Set Up a Hot/Warm/Cold/Frozen Elasticsearch Architecture](https://opster.com/guides/elasticsearch/capacity-planning/elasticsearch-hot-warm-cold-frozen-architecture/)
- [@article@Managing Elasticsearch Storage Tiers: Hot, Warm, Cold, and Frozen](https://www.hyperflex.co/solution-and-best-practices/managing-elasticsearch-storage-tiers-hot-warm-cold-and-frozen)
- [@video@Setting Up Data Tiers (Snippet)](https://www.youtube.com/watch?v=f9MS5Kw3H8U)

## Data Types

# Data Types

Data types define the kind of values that can be stored in a field. They specify how Elasticsearch should interpret and store the data, influencing how it can be searched and analyzed. Common examples include text, numbers, dates, booleans, and geo-locations, each optimized for different use cases.

Visit the following resources to learn more:

- [@official@Field data types](https://www.elastic.co/docs/reference/elasticsearch/mapping-reference/field-data-types)
- [@article@Elasticsearch For Dummies Part 2: Datatypes](https://tim-estes.medium.com/elasticsearch-for-dummies-part-2-datatypes-c7a9494b48e8)

## Dates

# Dates

Dates in Elasticsearch represent points in time. They are stored internally as the number of milliseconds since the Unix epoch (January 1, 1970, 00:00:00 UTC). Elasticsearch provides flexibility in how you format date values when indexing documents, allowing you to use strings in various formats or numeric values representing milliseconds since the epoch. When querying, you can use date ranges and other date-specific operations to filter and analyze your data based on time.

Visit the following resources to learn more:

- [@official@Date field type](https://www.elastic.co/docs/reference/elasticsearch/mapping-reference/date)
- [@official@Date nanoseconds field type](https://www.elastic.co/docs/reference/elasticsearch/mapping-reference/date_nanos)

## Delete By Query

# Delete by Query

Delete by Query allows you to remove documents from an Elasticsearch index that match a specific query. Instead of deleting documents individually by their ID, you can define criteria based on field values or other search parameters. This is useful for removing outdated, irrelevant, or incorrect data from your index in bulk.

Visit the following resources to learn more:

- [@official@Delete documents](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-delete-by-query)
- [@article@Elasticsearch Delete By Query](https://opster.com/guides/elasticsearch/how-tos/elasticsearch-delete-by-query/)

## Delete Documents

# Delete Documents

Deleting a document in Elasticsearch involves sending a DELETE request to a specific index and document ID. This action permanently removes the document from the index. After a successful deletion, the document will no longer be searchable. The operation requires specifying the index name and the unique identifier of the document you wish to remove.

Visit the following resources to learn more:

- [@official@Delete a document](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-delete)
- [@article@Elasticsearch Delete Document](https://opster.com/guides/elasticsearch/glossary/elasticsearch-delete-document/)
- [@article@Ways to delete documents from elasticsearch](https://medium.com/@prashant.n.khunt/ways-to-delete-documents-from-elasticsearch-a490195f794)
- [@article@Elasticsearch API | Index API, Update API, Get API, Delete API | Elasticsearch Tutorial | ELK Stack](https://www.youtube.com/watch?v=MPjily-rb1A)

## Delete Index

# Delete Index

Deleting an index in Elasticsearch removes the entire index and all its associated data. You can achieve this using the Delete Index API. Simply send a DELETE request to the index's name endpoint (e.g., `DELETE /your_index_name`). This action is permanent and irreversible, so it's crucial to ensure you're deleting the correct index and have a backup if needed.

Visit the following resources to learn more:

- [@course@Delete indices](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-indices-delete)
- [@article@Removing Old Indices in Elasticsearch](https://betterstack.com/community/questions/removing-old-indices-in-elasticsearch/)
- [@article@When and How to Delete an Elasticsearch Index?](https://sematext.com/blog/elasticsearch-delete-index/)
- [@video@How to create/delete index in elasticsearch](https://www.youtube.com/watch?v=Kq3A1evwIWs)

## Doc Values

# Doc Values

Doc values are a data structure in Elasticsearch that stores field values in a column-oriented fashion, optimized for aggregations, sorting, and scripting. Instead of storing the data alongside the inverted index, doc values are stored separately on disk, making them efficient for retrieving values for a large number of documents. This allows Elasticsearch to perform operations like sorting and aggregations much faster than if it had to retrieve the data from the inverted index.

Visit the following resources to learn more:

- [@official@doc_values](https://www.elastic.co/docs/reference/elasticsearch/mapping-reference/doc-values)
- [@article@Elasticsearch doc-values-only Fields](https://opster.com/guides/elasticsearch/data-architecture/elasticsearch-doc-values-only-fields/)
- [@article@Elasticsearch _source, doc_values and store Performance](https://sease.io/2021/02/field-retrieval-performance-in-elasticsearch.html)
- [@video@Field Data vs Doc Values | Understanding Elasticsearch Performance Issues](https://www.youtube.com/watch?v=l99lIuvQULk)

## Document Row

# Document (Row)

A document is a basic unit of information in Elasticsearch, analogous to a row in a relational database table. It's a JSON object containing a set of fields, each with a name and one or more values. These fields can hold various data types like text, numbers, dates, booleans, and even nested objects or arrays.

Visit the following resources to learn more:

- [@official@Index basics](https://www.elastic.co/docs/manage-data/data-store/index-basics)
- [@article@Elasticsearch Document](https://www.dremio.com/wiki/elasticsearch-document/)
- [@article@Elasticsearch Document](https://opster.com/guides/elasticsearch/glossary/elasticsearch-document/)
- [@video@How Elasticsearch Works: Documents, JSON & Index Explained](https://www.youtube.com/watch?v=wHZ3JsRzukI)

## Dynamic

# Dynamic Mappings

Dynamic mapping in Elasticsearch allows the index to automatically detect and add new fields to the mapping when new documents containing previously unseen fields are indexed. This means you don't have to predefine the schema for every field in your data; Elasticsearch infers the data type and adds the field to the index mapping on the fly. This is useful for quickly indexing data without upfront schema design.

Visit the following resources to learn more:

- [@official@Dynamic mapping](https://www.elastic.co/docs/manage-data/data-store/mapping/dynamic-mapping)
- [@official@Dynamic field mapping](https://www.elastic.co/docs/manage-data/data-store/mapping/dynamic-field-mapping)
- [@official@Elasticsearch Dynamic Mapping: Advanced Insights and Best Practices](https://opster.com/guides/elasticsearch/data-architecture/elasticsearch-dynamic-mapping/)
- [@video@Dynamic index mappings in Elasticsearch and OpenSearch](https://www.youtube.com/watch?v=KBMTES9lMOM)

## Elastic Cloud

# Elastic Cloud

Elastic Cloud is a suite of Elasticsearch-based services offered by Elastic, the company behind Elasticsearch. It provides a managed platform for deploying, managing, and scaling Elasticsearch clusters in the cloud, eliminating the need for users to handle the underlying infrastructure. This includes tasks like provisioning servers, configuring networking, and managing backups, allowing users to focus on analyzing and visualizing their data.

Visit the following resources to learn more:

- [@official@Accelerate results in Elastic Cloud](https://www.elastic.co/cloud)
- [@official@Elastic Cloud Serverless](https://www.elastic.co/cloud/serverless)
- [@video@Getting Started with Elasticsearch Service and Elastic Cloud](https://www.youtube.com/watch?v=mIHYcxe70fc)

## Elasticsearch Usecases

# Elasticsearch Usecases

Elastic use cases can be classified into three main categories:

*   **Elasticsearch** is a distributed, open-source search and analytics engine for all types of data, including textual, numerical, geospatial, structured, and unstructured.
*   **Elastic Observability** builds on this foundation to provide a unified view of logs, metrics, and traces, enabling users to monitor and troubleshoot their systems.
*   **Elastic Security** leverages Elasticsearch's search and analytics capabilities to offer threat detection, prevention, and response, helping organizations protect themselves from cyber threats. Elasticsearch use cases are diverse, ranging from application search and website search to logging and log analytics, security analytics, and business analytics.

Visit the following resources to learn more:

- [@official@Elasticsearch solution overview](https://www.elastic.co/docs/solutions/search)
- [@official@Elastic Observability overview](https://www.elastic.co/docs/solutions/observability)
- [@official@Elastic Security overview](https://www.elastic.co/docs/solutions/security)
- [@video@Getting Started with Elastic Observability](https://www.youtube.com/watch?v=SWUgqOSAyqU)
- [@video@Elastic Security Solutions Overview](https://www.youtube.com/watch?v=wzPMtmINEhU)

## Eql

# Event Query Language (EQL)

Event Query Language (EQL) is a powerful query language designed for security event analysis and threat hunting. It allows users to search for sequences of events that match specific patterns, enabling the detection of complex attack behaviors. EQL focuses on identifying relationships and dependencies between events over time, making it well-suited for uncovering malicious activities within large datasets.

Visit the following resources to learn more:

- [@official@EQL](https://www.elastic.co/docs/explore-analyze/query-filter/languages/eql)
- [@official@Introducing Event Query Language](https://www.elastic.co/blog/introducing-event-query-language)
- [@video@EQL Basics: Intro to Elastic's Event Query Language, Including Usage Example](https://www.youtube.com/watch?v=WbqYbzAkF94)
- [@video@Event Query Language (EQL) - Overview, Usage, Importance & Modeling Detections](https://www.youtube.com/watch?v=C-Kxzj-Dw_U)

## Esql

# ES|QL

ES|QL is a query language designed for Elasticsearch that allows users to search, transform, and analyze data using a SQL-like syntax. It provides a more familiar and accessible way to interact with Elasticsearch data compared to the traditional JSON-based query DSL, enabling users to perform complex data manipulations and aggregations with relative ease.

Visit the following resources to learn more:

- [@official@ES|QL](https://www.elastic.co/docs/reference/query-languages/esql)
- [@official@Getting started with ES|QL (Elasticsearch Query Language)](https://www.elastic.co/blog/getting-started-elasticsearch-query-language)
- [@official@Simplify data investigation: Elasticsearch Piped Query Language (ES|QL)](https://www.elastic.co/elasticsearch/piped-query-language)
- [@article@How to Leverage the New ES|QL Query Language](https://opster.com/guides/elasticsearch/how-tos/how-to-leverage-es-ql-query-language/)

## Exists Query

# Exists Query

An exists query in Elasticsearch is used to find documents that contain a specific field, regardless of its value. It checks for the presence of the field in the document's source data. This is useful when you need to filter documents based on whether a particular field has been defined or not.

Visit the following resources to learn more:

- [@official@Exists query](https://www.elastic.co/docs/reference/query-languages/query-dsl/query-dsl-exists-query)
- [@article@Elasticsearch Exists Query - Syntax, Example, and Tips](https://pulse.support/kb/elasticsearch-exists-query)
- [@article@Elasticsearch DSL Exists Query](https://opster.com/guides/elasticsearch/search-apis/elasticsearch-dsl-exists-query/)
- [@video@Exists Query | Elasticsearch | Check a field is exists in a document](https://www.youtube.com/watch?v=_1xLTLln6KQ)

## Explicit

# Explicit Mappings

Explicit mappings in Elasticsearch involve defining the structure and data types of fields within an index before indexing any documents. This allows you to have precise control over how Elasticsearch analyzes and stores your data, ensuring that fields are treated as intended (e.g., a field containing dates is treated as a date, not just text). By explicitly defining mappings, you can optimize search performance and data integrity.

Visit the following resources to learn more:

- [@official@Explicit mapping](https://www.elastic.co/docs/manage-data/data-store/mapping/explicit-mapping)
- [@video@Explicit index mappings in Elasticsearch and OpenSearch](https://www.youtube.com/watch?v=KRd4Ud-5_wM)

## Fielddata

# Fielddata

Fielddata is an on-disk data structure used by Elasticsearch to enable aggregations, sorting, and scripting on text fields. Because text fields are analyzed (broken down into individual terms), Elasticsearch needs a way to quickly access all the terms for a specific document when performing these operations. Fielddata loads all the terms for a field into memory, allowing for fast access during these operations.

Visit the following resources to learn more:

- [@article@What is Elasticsearch Fielddata?](https://pulse.support/kb/what-is-elasticsearch-fielddata)
- [@article@Elasticsearch Fielddata](https://opster.com/guides/elasticsearch/glossary/elasticsearch-fielddata/)
- [@video@Field Data vs Doc Values | Understanding Elasticsearch Performance Issues](https://www.youtube.com/watch?v=l99lIuvQULk)

## Filter Aggregations

# Filter Aggregations

Filter aggregations narrow down the documents that are used to calculate metrics within an aggregation. They work by applying a filter to the documents before the aggregation is performed, effectively creating a subset of the data for analysis. This allows you to focus on specific segments of your data and gain insights into particular subsets of your documents.

Visit the following resources to learn more:

- [@official@Filter aggregation](https://www.elastic.co/docs/reference/aggregations/search-aggregations-bucket-filter-aggregation)
- [@official@Multi-bucket filters aggregation](https://www.elastic.co/docs/reference/aggregations/search-aggregations-bucket-filters-aggregation)
- [@article@Elasticsearch Filter Aggregation: Advanced Usage and Optimization Techniques](https://opster.com/guides/elasticsearch/search-apis/elasticsearch-filter-aggregation/)

## Filter

# Filter

A filter in Elasticsearch is a query that returns documents matching specific criteria in a boolean (yes/no) manner. Unlike regular queries that calculate a relevance score, filters simply determine whether a document matches the condition or not. They are often used to narrow down the search results based on specific attributes or ranges, such as price, date, or category.

Visit the following resources to learn more:

- [@official@Query and filter context](https://www.elastic.co/docs/reference/query-languages/query-dsl/query-filter-context)
- [@official@Query DSL](https://www.elastic.co/docs/explore-analyze/query-filter/languages/querydsl)
- [@article@Deep Dive into Elastic Search Querying, Filter vs Query Context](https://mahajanjatin-14.medium.com/deep-dive-into-elastic-search-querying-filter-vs-query-context-920fdbfd31de)

## Filter

# Bool Query Filter Context

The `filter` context within a Bool query in Elasticsearch is used to narrow down the documents that match a query without affecting the relevance score. It's like a pre-filter that efficiently excludes documents that don't meet specific criteria before the scoring process even begins, making it ideal for exact matches, range queries, and other conditions where relevance isn't a factor.

Visit the following resources to learn more:

- [@official@Boolean query](https://www.elastic.co/docs/reference/query-languages/query-dsl/query-dsl-bool-query)
- [@official@Lost in Translation: Boolean Operations and Filters in the Bool Query](https://www.elastic.co/blog/lost-in-translation-boolean-operations-and-filters-in-the-bool-query)
- [@video@Elasticsearch Bool Query (Should & Filter Clauses) - S1E14: Mini Beginner's Crash Course](https://www.youtube.com/watch?v=Uh1F2lezIfY)
- [@video@Boolean Query in Elasticsearch | Bool, Filter, Must, Must Not, Should, DSL | ES7 for Beginners #4.3](https://www.youtube.com/watch?v=ba2Qn3y486M)

## Flattened

# Flattened Data Type

The flattened data type in Elasticsearch allows you to index an entire JSON object as a single field. This is useful when you have objects with many fields, but you only need to search or aggregate on a small subset of them. Instead of mapping each individual field, the flattened type indexes the entire object as a string, enabling you to query specific values within the object using specialized queries.

Visit the following resources to learn more:

- [@official@Flattened field type](https://www.elastic.co/docs/reference/elasticsearch/mapping-reference/flattened)
- [@article@Flattened Datatype Mappings — Elasticsearch Tutorial](https://alirezadp10.medium.com/flattened-datatype-mappings-elasticsearch-tutorial-1cf77497e706)
- [@video@Flattened Datatype](https://www.youtube.com/watch?v=UhPaEMR4pJ4)

## Function Score Query

# Function Score Query

The Function Score Query allows you to modify the score of documents retrieved by a query. It provides a way to apply a function to each document that matches the base query, influencing its final relevance score. This function can be based on factors like document fields, pre-defined weights, or even custom scripts, enabling fine-grained control over search results ranking.

Visit the following resources to learn more:

- [@official@Function score query](https://www.elastic.co/docs/reference/query-languages/query-dsl/query-dsl-function-score-query)
- [@official@A Gentle Intro to Function Scoring](https://www.elastic.co/blog/found-function-scoring)
- [@article@Elasticsearch Function Score: Boosting Relevance with Custom Scoring](https://opster.com/guides/elasticsearch/search-apis/elasticsearch-function-score/)
- [@article@Elasticsearch Function Score Query - Syntax, Example, and Tips](https://pulse.support/kb/elasticsearch-function-score-query)

## Geo Points

# Geo Points

Geo points are a specific data type in Elasticsearch used to store and index latitude and longitude coordinates. They allow you to represent locations on Earth and perform geospatial queries, such as finding points within a certain distance of a location or identifying points within a defined area. These coordinates are typically stored as a pair of numbers, with latitude representing the north-south position and longitude representing the east-west position.

Visit the following resources to learn more:

- [@official@Geopoint field type](https://www.elastic.co/docs/reference/elasticsearch/mapping-reference/geo-point)

## Get Document

# Get Document

To retrieve a specific document from an Elasticsearch index, you need to know its unique identifier. You can then use the Get API, providing the index name and the document ID. Elasticsearch will then search for the document with that ID within the specified index and return it. The response will include the document's source data (the fields and their values), along with metadata like the index, ID, version, and whether the document was found.

Visit the following resources to learn more:

- [@official@Get a document by its ID](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-get)
- [@article@Efficiently Searching by Document ID in Elasticsearch](https://opster.com/guides/elasticsearch/search-apis/efficiently-searching-by-document-id-elasticsearch/)
- [@video@How to retrieve documents in Elasticsearch?](https://www.youtube.com/watch?v=QRtRsWSn3n4)

## Highlighting

# Highlighting

Highlighting in Elasticsearch helps users quickly identify the search terms within the returned documents. It works by surrounding the search keywords in the results with special tags, like `<em>` and `</em>`, making them visually distinct. This allows users to easily see why a particular document matched their query without having to read the entire document. You can customize the tags used for highlighting, the fields that are highlighted, and even the way the highlighting is performed to suit your specific needs.

Visit the following resources to learn more:

- [@official@Highlighting](https://www.elastic.co/docs/reference/elasticsearch/rest-apis/highlighting)
- [@article@Semantic text in Elasticsearch: Simpler, better, leaner, stronger](https://www.elastic.co/search-labs/blog/elasticsearch-semantic-text-ga)
- [@video@Elasticsearch Highlighting - Part 1 - Getting Started](https://www.youtube.com/watch?v=3F2qjKNO6S4)

## Histogram

# Histogram Aggregation

A histogram aggregation calculates the distribution of numeric values across a set of intervals, or "buckets." It groups data into these buckets based on their values, providing a count of how many data points fall within each bucket's range. This allows you to visualize the frequency of values within specific ranges, revealing patterns and trends in your data.

Visit the following resources to learn more:

- [@official@Histogram aggregation](https://www.elastic.co/docs/reference/aggregations/search-aggregations-bucket-histogram-aggregation)
- [@article@Mastering Elasticsearch Histogram Aggregations](https://opster.com/guides/elasticsearch/how-tos/elasticsearch-histogram-aggregations/)
- [@article@Elasticsearch Date Histogram Aggregation - Syntax, Example, and Tips](https://pulse.support/kb/elasticsearch-date-histogram-aggregation)
- [@video@Elasticsearch Bucket Aggregations Part 1, Date Histogram Aggregation - S1E16: Mini Beginner's Course](https://www.youtube.com/watch?v=iDaAW3__hb8)

## How Search Works

# How Search Works

Search, at its core, involves matching a user's query against the data stored in an index. This process typically begins with the user entering a search term, which is then analyzed and processed. The system then retrieves documents that contain terms matching the processed query, ranking them based on relevance to present the most suitable results to the user.

Visit the following resources to learn more:

- [@official@What is a search engine?](https://www.elastic.co/what-is/search-engine)
- [@article@Elasticsearch: An In-Depth Explanation](https://dev.to/kakarotdevv/elasticsearch-an-in-depth-explanation-2bpf)

## Hybrid Search

# Hybrid Search

Hybrid search combines multiple search techniques to improve the relevance and accuracy of search results. It leverages the strengths of different approaches, such as keyword-based search and semantic search, to provide a more comprehensive and nuanced understanding of the user's query and the available data. By blending these methods, hybrid search aims to overcome the limitations of any single approach and deliver more relevant and meaningful results.

Visit the following resources to learn more:

- [@official@What is hybrid search?](https://www.elastic.co/what-is/hybrid-search)
- [@official@Elasticsearch hybrid search](https://www.elastic.co/search-labs/blog/hybrid-search-elasticsearch)
- [@official@Hybrid Search: Combined Full-Text and kNN Results](https://www.elastic.co/search-labs/tutorials/search-tutorial/vector-search/hybrid-search)
- [@video@What is hybrid search in Elasticsearch?](https://www.youtube.com/watch?v=IPGIU2QmZjw)
- [@video@How to build an advanced semantic search engine with hybrid search | Elasticsearch Coding Sessions](https://www.youtube.com/watch?v=inaBjdvdFgA)

## Id Primary Key

# ID (Primary Key)

An ID, or Primary Key, is a unique identifier for each document stored within an Elasticsearch index. It distinguishes one document from another, allowing for specific retrieval, updating, and deletion of individual data entries. This unique identifier is crucial for maintaining data integrity and enabling efficient data management within the Elasticsearch system.

Visit the following resources to learn more:

- [@official@_id field](http://elastic.co/docs/reference/elasticsearch/mapping-reference/mapping-id-field)
- [@official@Index basics](https://www.elastic.co/docs/manage-data/data-store/index-basics)
- [@official@Get a document by its ID](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-get)

## Id Query

# ID Query

An ID query retrieves documents from an index based on their unique identifier. It's a simple and efficient way to fetch specific documents when you already know their IDs. This query directly accesses the document using its `_id` field.

Visit the following resources to learn more:

- [@official@IDs](https://www.elastic.co/docs/reference/query-languages/query-dsl/query-dsl-ids-query)
- [@official@Get a document by its ID](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-get)
- [@article@Elasticsearch ids query](http://opster.com/guides/elasticsearch/search-apis/elasticsearch-ids-query/)
- [@article@Stop using the _id field in Elasticsearch](https://luis-sena.medium.com/stop-using-the-id-field-in-elasticsearch-6fb650d1fbae)

## Ilm

# Index Lifecycle Management (ILM)

Index Lifecycle Management (ILM) automates the process of managing Elasticsearch indices over time. It defines policies to control how indices are stored, moved, and deleted based on factors like age, size, or performance. This helps optimize resource utilization, reduce storage costs, and ensure data is available when needed.

Visit the following resources to learn more:

- [@official@Index lifecycle management](https://www.elastic.co/docs/manage-data/lifecycle/index-lifecycle-management)
- [@official@Index lifecycle management settings in Elasticsearch](https://www.elastic.co/docs/reference/elasticsearch/configuration-reference/index-lifecycle-management-settings)
- [@official@Monitoring Elasticsearch index lifecycle management with the history index](https://www.elastic.co/blog/elasticsearch-index-lifecycle-management-history-index)
- [@article@An Introduction to Index Life Cycle Management in Elasticsearch](https://medium.com/knowledgelens/an-introduction-to-index-life-cycle-management-in-elasticsearch-da6b0ff579c3)
- [@video@Setting Up Elasticsearch ILM - Index Lifecycle Management](https://www.youtube.com/watch?v=TPO6WzRp6Vo)

## Index Database

# Index (Database)

An index is a collection of documents that have similar characteristics. Think of it as a database in a relational database system. It's where Elasticsearch stores and organizes data, allowing for efficient searching and retrieval. Each index is identified by a name, which is used when performing indexing, searching, updating, and deleting operations.

Visit the following resources to learn more:

- [@official@Index basics](https://www.elastic.co/docs/manage-data/data-store/index-basics)
- [@official@What is an Elasticsearch index?](https://www.elastic.co/docs/manage-data/data-store/index-basics)
- [@article@Elasticsearch Index – How to create, list, query and delete indices](https://opster.com/guides/elasticsearch/glossary/elasticsearch-index/)
- [@video@How Elasticsearch Works: Documents, JSON & Index Explained](https://www.youtube.com/watch?v=wHZ3JsRzukI)
- [@video@What's ElasticSearch Used For? | Search Indexes | Systems Design Interview 0 to 1 with Ex-Google SWE](https://www.youtube.com/watch?v=wmCWCVAl1Us)

## Index Document

# Index Document

To add data to Elasticsearch, you use the Index API. This API lets you create a new document within a specific index. You need to specify the index name, a unique ID for the document (or let Elasticsearch generate one), and the document's content in JSON format. When you send this information to Elasticsearch via a PUT or POST request, it analyzes the data, indexes it, and makes it searchable.

Visit the following resources to learn more:

- [@official@Create a new document in the index](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-create)
- [@official@Create or update a document in an index](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-index)
- [@video@How to index a document inside Elastic Search](https://www.youtube.com/watch?v=ZdV45CLO0to)

## Introduction

# Elasticsearch

Elasticsearch is a distributed, open-source search and analytics engine for all types of data, including textual, numerical, geospatial, structured, and unstructured. It's built on Apache Lucene and provides a distributed, multitenant-capable full-text search engine with an HTTP web interface and schema-free JSON documents. Elasticsearch is commonly used for log analytics, full-text search, security intelligence, business analytics, and operational intelligence use cases.

Visit the following resources to learn more:

- [@book@Elasticsearch The Definitive Guide](https://hlaszny.com/booksAndPapers/buckets/b8_IT/elasticsearch-the-definitive-guide.pdf)
- [@official@Elasticsearch](https://www.elastic.co/elasticsearch)
- [@official@Elasticsearch solution overview](https://www.elastic.co/docs/solutions/search)
- [@official@Get started with Elasticsearch](https://www.elastic.co/docs/solutions/search/get-started)
- [@official@Elasticsearch Labs Tutorial](https://www.elastic.co/search-labs/tutorials)
- [@article@Elasticsearch Tutorial](https://www.tutorialspoint.com/elasticsearch/index.htm)
- [@video@Elasticsearch Course for Beginners](https://www.youtube.com/watch?v=a4HBKEda_F8)

## Json

# JSON

JSON (JavaScript Object Notation) is a lightweight data-interchange format that is easy for humans to read and write and easy for machines to parse and generate. It's based on a subset of the JavaScript programming language, and uses a text-based format to represent data objects consisting of attribute-value pairs and array data types. JSON is commonly used for transmitting data in web applications (e.g., sending some data from the server to the client, so it can be displayed on a web page) and is a standard format for APIs and configuration files.

Visit the following resources to learn more:

- [@article@Introducing JSON](https://www.json.org/json-en.html)
- [@article@JavaScript JSON](https://www.w3schools.com/js/js_json.asp)
- [@article@Working with JSON](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting/JSON)
- [@video@How Elasticsearch Works: Documents, JSON & Index Explained](https://www.youtube.com/watch?v=wHZ3JsRzukI)
- [@video@What Is JSON | Explained](https://www.youtube.com/watch?v=cj3h3Fb10QY)

## Keyword

# Keyword Data Type

The Keyword data type in Elasticsearch is used for indexing fields that contain structured, string-based data. Unlike the Text data type, Keyword fields are not analyzed or tokenized; the entire string is indexed as a single term. This makes them ideal for filtering, sorting, and exact-match queries, where you need to find documents with a specific, complete value.

Visit the following resources to learn more:

- [@official@Keyword type family](https://www.elastic.co/docs/reference/elasticsearch/mapping-reference/keyword)

## Kibana Console

# Kibana Console

Kibana is a web interface that allows you to explore, visualize, and manage data indexed in Elasticsearch. It provides tools for searching, analyzing, and visualizing your data in real-time. Through Kibana, you can create dashboards, charts, and maps to gain insights from your Elasticsearch data. It also offers features for managing your Elasticsearch cluster, including monitoring its health and performance.

Visit the following resources to learn more:

- [@official@Elastic Console](https://www.elastic.co/docs/explore-analyze/query-filter/tools/console)
- [@video@Kibana Dev Tools: Overview, Usage & Examples - Daily Elastic Byte S02E05](https://www.youtube.com/watch?v=ZiHiH3wfgas)

## Kql

# KQL

Kibana Query Language (KQL) is a query language used within Kibana to search and filter data in Elasticsearch. It allows users to construct queries using a human-readable syntax, making it easier to find specific information within their Elasticsearch indices without needing to write complex JSON-based Elasticsearch queries. KQL supports features such as free-text search, field-based filtering, Boolean operators, and range queries.

Visit the following resources to learn more:

- [@official@KQL](https://www.elastic.co/docs/explore-analyze/query-filter/languages/kql)
- [@official@Kibana Query Language](https://www.elastic.co/docs/reference/query-languages/kql)
- [@article@How to Query Elasticsearch in Kibana](https://dattell.com/data-architecture-blog/how-to-query-elasticsearch-in-kibana/)
- [@video@Exploring and querying your data with Kibana](https://www.youtube.com/watch?v=t3cebUxRliA)
- [@video@Understanding the Kibana Query Language (KQL)](https://www.youtube.com/watch?v=wfqItAlUy8g)

## Latest

# Latest Transformation

The "latest" transformation in Elasticsearch is used to identify and extract the most recent document within a group of documents that share a common field value. It allows you to find the most up-to-date information for each unique entity based on a specified sorting criteria, such as a timestamp or version number. This is particularly useful when dealing with time-series data or scenarios where you need to retrieve the latest state of an object.

Visit the following resources to learn more:

- [@official@Latest transforms](https://www.elastic.co/docs/explore-analyze/transforms/transform-overview#latest-transform-overview)
- [@official@Transform and enrich data](https://www.elastic.co/docs/manage-data/ingest/transform-enrich)

## Leaf Vs Compound Queries

# Leaf vs. Compound Queries

Leaf queries in Elasticsearch target specific fields with simple search criteria, like finding documents where a field matches a particular value or falls within a certain range. Compound queries, on the other hand, combine multiple leaf or other compound queries to create more complex search logic, allowing you to specify how these individual queries should interact (e.g., must all match, at least one must match, or none should match).

Visit the following resources to learn more:

- [@official@Query DSL](https://www.elastic.co/docs/explore-analyze/query-filter/languages/querydsl)
- [@official@Compound queries](https://www.elastic.co/docs/reference/query-languages/query-dsl/compound-queries)
- [@article@Introduction to Elasticsearch Queries](https://medium.com/elasticsearch/introduction-to-elasticsearch-queries-b5ea254bf455)
- [@article@An introduction to Query DSL: creating queries in Elasticsearch](https://kwan.com/blog/an-introduction-to-query-dsl-creating-queries-in-elasticsearch/)

## Lucene

# Lucene Query Syntax

Lucene is a powerful text search engine library. Its query syntax provides a way to specify search criteria using terms, phrases, wildcards, and boolean operators. This enables users to conduct complex searches within text-based data, surpassing simple keyword matching to define precise and nuanced search criteria.

Visit the following resources to learn more:

- [@official@Lucene query syntax](https://www.elastic.co/docs/explore-analyze/query-filter/languages/lucene-query-syntax)
- [@article@Apache Lucene Core](https://lucene.apache.org/core/)

## Mapping Explosion

# Mapping Explosion

Mapping explosion in Elasticsearch refers to the uncontrolled growth of fields within an index's mapping. This typically happens when Elasticsearch automatically creates mappings for new fields as it encounters them in incoming documents. Suppose a large number of unique and unexpected field names are introduced. In that case, the index mapping can become excessively large, consuming significant memory and impacting cluster performance due to increased resource usage during mapping updates and search operations.

## Mappings

# Mappings

Mappings are like schemas in relational databases; they define how a document and its fields are stored and indexed. They specify the data type of each field (like text, keyword, date, or number) and how Elasticsearch should handle that data for searching and analysis. Mappings are crucial for ensuring data is indexed correctly and that queries return accurate and relevant results.

Visit the following resources to learn more:

- [@official@Mapping](https://www.elastic.co/docs/manage-data/data-store/mapping)
- [@article@Elasticsearch Mapping](https://opster.com/guides/elasticsearch/glossary/elasticsearch-mapping/)
- [@article@[Beginner's guide] Understanding mapping with Elasticsearch and Kibana](https://dev.to/lisahjung/beginner-s-guide-understanding-mapping-with-elasticsearch-and-kibana-3646)
- [@video@What Are Mappings in Elasticsearch? (Explained Simply)](https://www.youtube.com/watch?v=ryXCer_rJcg)
- [@video@Beginner’s Crash Course to Elastic Stack - Part 5: Mapping](https://www.youtube.com/watch?v=FQAHDrVwfok)

## Master Elegible Nodes

# Master-Eligible Nodes

Master-eligible nodes in Elasticsearch are the nodes that can be elected as the master node. The master node is responsible for cluster-wide management tasks, such as creating or deleting indices, tracking which nodes are part of the cluster, and deciding how to allocate shards across the cluster. These nodes participate in the master election process and have the potential to become the cluster's central controller.

Visit the following resources to learn more:

- [@official@Node roles](https://www.elastic.co/docs/deploy-manage/distributed-architecture/clusters-nodes-shards/node-roles)
- [@article@Elasticsearch Nodes](https://opster.com/guides/elasticsearch/glossary/elasticsearch-node/)
- [@video@Adding Nodes to an Elasticsearch Cluster](https://www.youtube.com/watch?v=XyQ4AN1Jn78)

## Match Phrase Query

# Match Phrase Query

The Match Phrase query searches for documents that contain the exact phrase specified in the query. This means the terms must appear in the precise order and be adjacent to each other, as defined in the query string. It's a stricter form of matching compared to a standard match query, which only requires the terms to be present in the document, regardless of their order or proximity.

## Match Query

# Match Query

The Match Query is a fundamental full-text search query in Elasticsearch. It allows you to search for documents that contain specific terms within a field. It analyzes the query string provided, breaking it down into individual terms based on the field's analyzer, and then searches for those terms in the specified field.

Visit the following resources to learn more:

- [@official@Match query](https://www.elastic.co/docs/reference/query-languages/query-dsl/query-dsl-match-query)
- [@article@Elasticsearch Match Query Usage and Examples](https://openobserve.ai/articles/elasticsearch-matching/)
- [@video@Elasticsearch Match Query: Overview, Usage & Examples - S1E1 Query DSL Series](https://www.youtube.com/watch?v=ji8TJtLO6bI)

## Must

# Must Queries

A "must" query in Elasticsearch is a type of compound query that specifies conditions that documents must satisfy to be included in the search results. It contributes to the relevance score of each matching document. Essentially, it acts as a mandatory filter, ensuring that only documents matching the specified criteria are returned.

Visit the following resources to learn more:

- [@official@Bool Queries](https://www.elastic.co/docs/reference/query-languages/query-dsl/query-dsl-bool-query)
- [@article@Elasticsearch Query Bool](https://opster.com/guides/elasticsearch/search-apis/elasticsearch-query-bool/)
- [@article@Elasticsearch Boolean Clauses](https://dattell.com/data-architecture-blog/how-to-query-elasticsearch-with-boolean-queries/)
- [@video@Boolean Query in Elasticsearch | Bool, Filter, Must, Must Not, Should, DSL | ES7 for Beginners #4.3](https://www.youtube.com/watch?v=ba2Qn3y486M)
- [@video@Elasticsearch Bool Query (Must & Must_not Clauses) - S1E13: Mini Beginner's Crash Course](https://www.youtube.com/watch?v=DhkTerHrXsM)

## Must Not

# Must_Not Queries

`must_not` is a clause within a `bool` query that filters out documents matching the specified query. It defines conditions that documents should _not_ satisfy to be included in the search results. Essentially, it excludes documents that would otherwise be considered relevant based on other clauses in the `bool` query.

Visit the following resources to learn more:

- [@official@Boolean query](https://www.elastic.co/docs/reference/query-languages/query-dsl/query-dsl-bool-query)
- [@article@Elasticsearch Bool Query - Syntax, Example, and Tips](https://pulse.support/kb/elasticsearch-bool-query)
- [@video@Boolean Query in Elasticsearch | Bool, Filter, Must, Must Not, Should, DSL | ES7 for Beginners #4.3](https://www.youtube.com/watch?v=ba2Qn3y486M)
- [@video@Elasticsearch Bool Query (Must & Must_not Clauses) - S1E13: Mini Beginner's Crash Course](https://www.youtube.com/watch?v=DhkTerHrXsM&t=12s)

## Nested Aggregations

# Nested Aggregations

Nested aggregations allow you to perform aggregations on nested objects within your documents. These nested objects are stored as separate documents internally by Elasticsearch, and nested aggregations provide a way to access and analyze the data within these nested structures as if they were part of the parent document. This is particularly useful when you have complex data structures where related information is embedded within a single document.

Visit the following resources to learn more:

- [@official@Nested aggregation](https://www.elastic.co/docs/reference/aggregations/search-aggregations-bucket-nested-aggregation)
- [@article@Elasticsearch Nested Aggregation](https://opster.com/guides/elasticsearch/data-architecture/elasticsearch-nested-aggregation/)
- [@article@How to Optimize Nested Aggregations in Elasticsearch](https://opster.com/guides/elasticsearch/search-apis/optimizing-nested-aggregations-elasticsearch/)
- [@video@Nested Aggregations](https://www.youtube.com/watch?v=G1ExN9cBVCw)

## Nested

# Nested Data Type

The nested data type is used to represent arrays of objects within a document. Each object in the array can be indexed as a separate document, allowing you to query and filter based on the properties of individual objects within the array, without affecting other objects in the same array. This is particularly useful when you need to perform complex queries on related objects stored within a single document.

Visit the following resources to learn more:

- [@official@Nested field type](https://www.elastic.co/docs/reference/elasticsearch/mapping-reference/nested)
- [@video@Nested vs object elasticsearch | How do I query nested objects in Elasticsearch?](https://www.youtube.com/watch?v=YIFDzfImSF8)
- [@video@Querying Nested Objects in Elasticsearch](https://www.youtube.com/watch?v=UeAHBLJDFR8)

## Node Instance

# Node (Instance)

A node is a single server within an Elasticsearch cluster that stores data and participates in the cluster's indexing and search capabilities. Each node is configured with a name and can be assigned specific roles, such as master, data, or ingest, to optimize resource allocation and cluster performance. Nodes communicate with each other to distribute data, manage cluster state, and handle search requests.

Visit the following resources to learn more:

- [@official@Node settings](https://www.elastic.co/docs/reference/elasticsearch/configuration-reference/node-settings)
- [@official@Clusters, nodes, and shards](https://www.elastic.co/docs/deploy-manage/distributed-architecture/clusters-nodes-shards)
- [@official@Add and Remove Elasticsearch nodes](https://www.elastic.co/docs/deploy-manage/maintenance/add-and-remove-elasticsearch-nodes)
- [@video@Nodes, Clusters & Shards - Elasticsearch 101 Course, Episode 2](https://www.youtube.com/watch?v=sAySPSyL2qE)

## Numeric

# Numeric Data Types

Numeric data types in Elasticsearch are used to store numerical values, such as integers and floating-point numbers. These types allow you to efficiently store and query numerical data, enabling operations like range queries, aggregations, and sorting based on numerical values. Elasticsearch offers various numeric types to optimize storage and performance based on the expected range and precision of your data.

Visit the following resources to learn more:

- [@official@Numeric field types](https://www.elastic.co/docs/reference/elasticsearch/mapping-reference/number)

## Object

# Object Data Type

An object is a data type that allows you to store nested JSON documents within a single document. This means you can represent complex, hierarchical data structures where a field can contain other fields and their corresponding values, similar to how objects are structured in programming languages. These nested objects can be indexed and searched, enabling you to query based on the properties within the nested structure.

Visit the following resources to learn more:

- [@official@Object field type](https://www.elastic.co/docs/reference/elasticsearch/mapping-reference/object)

## Optimizing Bulk Indexing

# Optimizing Bulk Indexing

Bulk indexing in Elasticsearch is the process of sending multiple indexing, updating, or deleting operations in a single request. Optimizing this process involves tuning various parameters and strategies to maximize throughput and minimize resource consumption, ensuring data is efficiently loaded into Elasticsearch. This includes adjusting batch sizes, managing thread pools, and leveraging techniques like request routing and refresh interval adjustments.

Visit the following resources to learn more:

- [@official@Tune for indexing speed](https://www.elastic.co/docs/deploy-manage/production-guidance/optimize-performance/indexing-speed)
- [@article@Optimizing Elasticsearch Bulk Indexing for High Performance](https://opster.com/guides/elasticsearch/how-tos/optimizing-elasticsearch-bulk-indexing-high-performance/)
- [@article@Tips and Tricks for Elasticsearch Indexing](https://medium.com/@nile.bits/tips-and-tricks-for-elasticsearch-indexing-ead3ddbc11de)

## Pagination

# Pagination

Pagination divides search results into discrete pages, allowing users to navigate through large datasets in manageable chunks. Instead of displaying all results at once, which can be overwhelming and resource-intensive, pagination presents a subset of results per page, improving user experience and reducing server load. This involves specifying the starting point (from) and the number of results to return (size) for each page.

Visit the following resources to learn more:

- [@official@Paginate search results](https://www.elastic.co/docs/reference/elasticsearch/rest-apis/paginate-search-results)
- [@article@Explaining Pagination in ElasticSearch](https://dev.to/lazypro/explaining-pagination-in-elasticsearch-2g26)
- [@article@Elasticsearch Pagination – Which Technique to Use Depending on Your Use Case](https://opster.com/guides/how-tos/elasticsearch-pagination-techniques/)
- [@video@4 Ways to do Pagination or scrolling in Elastic Search Tutorials Python](https://www.youtube.com/watch?v=P8Eu6sotkCw)
- [@video@Pagination of results in Elasticsearch | from & size, scroll, search after [ES7 for Beginners #4.4]](https://www.youtube.com/watch?v=8noSYHuTeSM)

## Pipeline Aggregations

# Pipeline Aggregations

Pipeline aggregations in Elasticsearch take the results of other aggregations as their input, allowing you to perform calculations and derive new insights based on the aggregated data. Instead of operating on the documents themselves, they process the output of other aggregations, enabling you to create complex analytical pipelines within your search queries. This allows for calculations like moving averages, derivatives, and cumulative sums to be performed directly within Elasticsearch.

Visit the following resources to learn more:

- [@official@Pipeline](https://www.elastic.co/docs/reference/aggregations/pipeline)
- [@article@Comprehensive Guide to Elasticsearch Pipeline Aggregations: Part I](https://medium.com/qbox-search-as-a-service/comprehensive-guide-to-elasticsearch-pipeline-aggregations-part-i-be77aff65630)
- [@article@Comprehensive Guide to Elasticsearch Pipeline Aggregations: Part II](https://medium.com/qbox-search-as-a-service/comprehensive-guide-to-elasticsearch-pipeline-aggregations-part-ii-f7d3dd34e4bb)
- [@video@Pipeline Aggregations in Elasticsearch [ElasticSearch 7 for Beginners 5.3]](https://www.youtube.com/watch?v=nLSdwtqWqtk)

## Pivot

# Pivot Transformation

The pivot transformation in Elasticsearch is a way to reshape your data by aggregating values from one or more fields into columns. It essentially rotates the data, turning unique values in a field into separate fields in the output. This allows you to analyze and visualize data in a different format, making it easier to identify trends and patterns that might be hidden in the original structure.

Visit the following resources to learn more:

- [@official@Transforming data](https://www.elastic.co/docs/explore-analyze/transforms)
- [@official@Pivot transforms](https://www.elastic.co/docs/explore-analyze/transforms/transform-overview#pivot-transform-overview)
- [@official@Transforms examples](https://www.elastic.co/docs/explore-analyze/transforms/transform-examples)

## Prefix Query

# Prefix Query

A prefix query finds documents that contain terms starting with a specific prefix. It operates at the term level, meaning it searches for the prefix directly within the indexed terms of a field. This query is useful for implementing features like autocompletion or searching for products based on the beginning of their names.

Visit the following resources to learn more:

- [@official@Prefix query](https://www.elastic.co/docs/reference/query-languages/query-dsl/query-dsl-prefix-query)
- [@article@Elasticsearch Prefix Query](https://opster.com/guides/elasticsearch/how-tos/elasticsearch-prefix-query/)
- [@article@Elasticsearch Prefix Query - Syntax, Example, and Tips](https://pulse.support/kb/elasticsearch-prefix-query)
- [@article@Elasticsearch in Action: Prefix Queries](https://mkonda007.medium.com/elasticsearch-in-action-prefix-queries-f5891cdd2457)
- [@video@Elasticsearch match phrase prefix query with definition and examples](https://www.youtube.com/watch?v=cP8fa3orte0)

## Primary Shards

# Primary Shards

Primary shards are the fundamental units of data storage in Elasticsearch. An index is logically divided into one or more primary shards, each of which contains a portion of the index's data. These shards allow Elasticsearch to distribute data across multiple nodes in a cluster, enabling horizontal scaling and improved performance. The number of primary shards is defined at index creation and determines the maximum level of parallelism for indexing and searching.

Visit the following resources to learn more:

- [@official@Clusters, nodes, and shards](https://www.elastic.co/docs/deploy-manage/distributed-architecture/clusters-nodes-shards)
- [@official@Size your shards](https://www.elastic.co/docs/deploy-manage/production-guidance/optimize-performance/size-shards)
- [@article@Understanding Shards in Elasticsearch](https://opster.com/guides/elasticsearch/glossary/what-are-shards-in-elasticsearch/)
- [@article@Elasticsearch shards and replicas: A practical guide](https://www.elastic.co/search-labs/blog/elasticsearch-shards-and-replicas-guide)
- [@video@Nodes, clusters, and shards in Elasticsearch - S1E3:Mini Beginner's Crash Course](https://www.youtube.com/watch?v=9uJNksCj2f8)

## Query Dsl

# Query DSL

Query DSL (Domain Specific Language) is a JSON-based language used to define and execute search queries in Elasticsearch. It provides a structured way to express complex search criteria, including boolean logic, term matching, range queries, and more, allowing users to precisely specify what data they want to retrieve.

Visit the following resources to learn more:

- [@official@Query DSL](https://www.elastic.co/docs/explore-analyze/query-filter/languages/querydsl)
- [@official@Get started with Query DSL search and filters](https://www.elastic.co/docs/reference/query-languages/query-dsl/full-text-filter-tutorial)
- [@article@Elasticsearch Queries: A Guide to Query DSL](https://logz.io/blog/elasticsearch-queries/)
- [@article@Elasticsearch Query DSL Examples](https://opster.com/guides/elasticsearch/search-apis/elasticsearch-query-dsl-examples/)
- [@video@Elasticsearch query DSL](https://www.youtube.com/playlist?list=PLGZAAioH7ZlMQGCt8GeAaJLvgehhq-gEK)

## Query

# Query

A query is a request for information from a data source. It specifies the criteria for retrieving specific data that matches the defined conditions. In Elasticsearch, queries are used to search and retrieve documents that match certain criteria within an index. These queries can range from simple keyword searches to complex combinations of filters and conditions.

Visit the following resources to learn more:

- [@official@Query and filter context](https://www.elastic.co/docs/reference/query-languages/query-dsl/query-filter-context)
- [@official@Query DSL](https://www.elastic.co/docs/explore-analyze/query-filter/languages/querydsl)
- [@article@Deep Dive into Elastic Search Querying, Filter vs Query Context](https://mahajanjatin-14.medium.com/deep-dive-into-elastic-search-querying-filter-vs-query-context-920fdbfd31de)

## Range  Date Range

# Range/Date Range Aggregations

Range and Date Range aggregations are used to categorize documents into buckets based on numeric or date values falling within specified ranges. These aggregations allow you to define custom intervals for grouping data, providing flexibility in analyzing distributions and trends across your dataset. You can define specific start and end points for each range, enabling you to create meaningful segments for your analysis.

Visit the following resources to learn more:

- [@official@Range aggregation](https://www.elastic.co/docs/reference/aggregations/search-aggregations-bucket-range-aggregation)
- [@official@Date range aggregation](https://www.elastic.co/docs/reference/aggregations/search-aggregations-bucket-daterange-aggregation)
- [@article@Elasticsearch Range Aggregation - Syntax, Example, and Tips](https://pulse.support/kb/elasticsearch-range-aggregation)
- [@article@Elasticsearch Date Range Aggregation - Syntax, Example, and Tips](https://pulse.support/kb/elasticsearch-date-range-aggregation)
- [@video@Elasticsearch Bucket, Histogram, Range & Terms Aggregations - S1E17 Mini Beginner's Crash Course](https://www.youtube.com/watch?v=R114ib2D9mU)
- [@video@Bucket Aggregations in Elasticsearch | ElasticSearch 7 for Beginners #5.2](https://www.youtube.com/watch?v=8QmBZLOl9Y8&t=277s)

## Range Query

# Range Query

A range query allows you to find documents where the value of a specific field falls within a specified range. This range can be defined using upper and lower bounds, which can be inclusive or exclusive. It's useful for filtering data based on numerical values, dates, or even strings that can be lexicographically compared.

Visit the following resources to learn more:

- [@article@Range query](https://www.elastic.co/docs/reference/query-languages/query-dsl/query-dsl-range-query)
- [@article@Elasticsearch Range Query: Advanced Usage and Optimization Techniques](https://opster.com/guides/elasticsearch/search-apis/elasticsearch-range-query/)
- [@article@Elasticsearch Range Query - Syntax, Example, and Tips](https://pulse.support/kb/elasticsearch-range-query)
- [@article@How to use range query - Spring Data Elasticsearch - Part 5](https://www.youtube.com/watch?v=KmDvh9OLt-Y)

## Reindex Api

# Reindex API

The Reindex API in Elasticsearch allows you to copy documents from one index to another. This is useful for a variety of tasks, including changing the mapping of an index, upgrading to a new Elasticsearch version, or splitting a large index into smaller ones. It essentially reads documents from a source index and writes them into a destination index, optionally applying transformations along the way.

Visit the following resources to learn more:

- [@official@Reindex documents](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-reindex)
- [@article@Reindex indices examples](https://www.elastic.co/docs/reference/elasticsearch/rest-apis/reindex-indices)
- [@article@Elasticsearch Reindexing: When to Reindex, Best Practices and Alternatives](https://medium.com/@jmills2010/elasticsearch-reindexing-when-to-reindex-best-practices-and-alternatives-7ebfa11667a0)
- [@article@Elasticsearch Reindex API: A Guide to Data Management](https://last9.io/blog/elasticsearch-reindex-api/)

## Replica Shards

# Replica Shards

Replica shards are copies of primary shards within an Elasticsearch index. They provide redundancy, ensuring data availability even if a primary shard fails. Additionally, replica shards serve read requests, distributing the load and improving search performance by allowing Elasticsearch to process queries in parallel across multiple shards.

Visit the following resources to learn more:

- [@official@Reading and writing documents](https://www.elastic.co/docs/deploy-manage/distributed-architecture/reading-and-writing-documents)
- [@article@Elasticsearch shards and replicas: A practical guide](https://www.elastic.co/search-labs/blog/elasticsearch-shards-and-replicas-guide)
- [@video@Nodes, clusters, and shards in Elasticsearch - S1E3:Mini Beginner's Crash Course](https://www.youtube.com/watch?v=9uJNksCj2f8)

## Rest Api Basics

# REST API Basics

REST API (Representational State Transfer Application Programming Interface) is an architectural style for building networked applications. It relies on a stateless, client-server communication protocol, typically HTTP, to perform operations on resources. These operations, often referred to as CRUD (Create, Read, Update, Delete), are executed using standard HTTP methods like GET, POST, PUT, and DELETE, allowing different software systems to interact with each other over a network.

Visit the following resources to learn more:

- [@roadmap@Visit the Dedicated API Design Roadmap](https://roadmap.sh/api-design)
- [@article@What is REST API?](http://cloud.google.com/discover/what-is-rest-api?hl=en)
- [@article@What is REST API? - IBM](https://www.ibm.com/think/topics/rest-apis)
- [@video@What Is REST API? Examples And How To Use It: Crash Course System Design #3](https://www.youtube.com/watch?v=-mN3VyJuCjM)
- [@video@What is a REST API?](https://www.youtube.com/watch?v=lsMQRaeKNDk)

## Roles  Users

# Roles & Users

Roles and users are fundamental components of security in Elasticsearch. Roles define a set of privileges, specifying what actions a user can perform on which resources (like indices or clusters). Users are then assigned one or more roles, granting them the combined permissions of those roles. This system allows administrators to control access to data and cluster operations, ensuring that only authorized individuals can perform specific tasks within the Elasticsearch environment.

Visit the following resources to learn more:

- [@official@User roles](https://www.elastic.co/docs/deploy-manage/users-roles/cluster-or-deployment-auth/user-roles)
- [@official@Users and roles](https://www.elastic.co/docs/deploy-manage/users-roles)
- [@official@User roles and privileges](https://www.elastic.co/docs/deploy-manage/users-roles/cloud-organization/user-roles)
- [@official@Manage users and roles](https://www.elastic.co/docs/deploy-manage/users-roles/cloud-enterprise-orchestrator/manage-users-roles)
- [@video@Managing Kibana Users, Roles & Permissions - Daily Elastic Byte S02E12](https://www.youtube.com/watch?v=mLRnNk1ZpTQ)

## Rollover Policies

# Rollover Policies

Rollover policies in Elasticsearch automate the management of indices over time. They define conditions, such as index size, document count, or age, that trigger the creation of a new index and the transition of write operations to it. This process helps maintain manageable index sizes, optimize search performance, and simplify data retention strategies.

Visit the following resources to learn more:

- [@official@About rollover](https://www.elastic.co/docs/manage-data/lifecycle/index-lifecycle-management/rollover)
- [@official@Rollover](https://www.elastic.co/docs/reference/elasticsearch/index-lifecycle-actions/ilm-rollover)
- [@official@Roll over to a new index](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-indices-rollover)
- [@official@Configuring rollover](https://www.elastic.co/docs/manage-data/lifecycle/index-lifecycle-management/ilm-tutorials#configuring-rollover)
- [@article@Elasticsearch Index Life cycle and Rollover Policy](https://www.elastic.co/docs/reference/elasticsearch/index-lifecycle-actions/ilm-rollover)
- [@video@Optimizing Index Operations in Elasticsearch: Shrink & Rollover - Daily Elastic Byte S01E05](https://www.youtube.com/watch?v=9U9OBWfxC-M)

## Running With Docker

# Running Elasticsearch with Docker

Docker provides a convenient and isolated environment to run applications, including Elasticsearch. Using Docker, you can quickly set up an Elasticsearch instance without worrying about operating system compatibility or dependency conflicts. This involves pulling the official Elasticsearch image from a registry like Docker Hub, configuring the necessary environment variables and port mappings, and then starting the container. This approach simplifies deployment and ensures consistency across different environments.

Visit the following resources to learn more:

- [@roadmap@Visit the Dedicated Docker Roadmap](https://roadmap.sh/docker)
- [@official@Install Elasticsearch with Docker](https://www.elastic.co/docs/deploy-manage/deploy/self-managed/install-elasticsearch-with-docker)
- [@official@Start a single-node cluster in Docker](https://www.elastic.co/docs/deploy-manage/deploy/self-managed/install-elasticsearch-docker-basic)
- [@article@Elastic Stack with Docker getting started. Elasticsearch, Kibana, and Filebeat.](https://medium.com/@vosarat1995/elastic-stack-with-docker-getting-started-elasticsearch-kibana-and-filebeat-ebe75fd13041)
- [@article@A beginner's guide to running Elasticsearch with Docker and Docker Compose](https://geshan.com.np/blog/2023/06/elasticsearch-docker/)
- [@video@How to Install Elasticsearch using Docker - Step by Step Guide](https://www.youtube.com/watch?v=p9IWwTDHgcU)

## Search Analyzer

# Search Analyzer

A search analyzer in Elasticsearch is responsible for processing the query text provided by a user before it's used to search the index. It transforms the query text into a format that matches the indexed data, ensuring relevant results are retrieved. This process typically involves character filtering, tokenization, and token filtering, similar to the analysis process performed on documents during indexing, but tailored for search queries.

Visit the following resources to learn more:

- [@official@Anatomy of an analyzer](https://www.elastic.co/docs/manage-data/data-store/text-analysis/anatomy-of-an-analyzer)
- [@official@Index and search analysis](https://www.elastic.co/docs/manage-data/data-store/text-analysis/index-search-analysis)
- [@official@Specify an analyzer](https://www.elastic.co/docs/manage-data/data-store/text-analysis/specify-an-analyzer)
- [@article@https://pulse.support/kb/what-is-elasticsearch-analyzer](https://pulse.supphttps//pulse.support/kb/what-is-elasticsearch-analyzerort/kb/what-is-elasticsearch-analyzer)
- [@video@Elastic Search Analyzer explained in a easy way](https://www.youtube.com/watch?v=9VhTnWuely4)
- [@video@Mapping and Analysers [ElasticSearch 7 for Beginners #3.2]](https://www.youtube.com/watch?v=_OjUoZ5NbYY)

## Search Engines Vs Relational Dbs

# Search Engines vs. Relational Databases

Search engines are designed for quickly finding relevant information within large volumes of unstructured or semi-structured text, prioritizing speed and relevance scoring. Relational databases, on the other hand, are structured systems optimized for managing and querying structured data with strong consistency and transactional integrity, using predefined schemas and relationships between tables.

Visit the following resources to learn more:

- [@roadmap@Visit the Dedicated SQL Roadmap](https://roadmap.sh/sql)
- [@official@What is a search engine?](https://www.elastic.co/what-is/search-engine)
- [@article@A Guide to Search Engine Databases](https://www.influxdata.com/search-engine-database/)
- [@article@Full Text Search Engines vs. DBMS](https://lucidworks.com/blog/full-text-search-engines-vs-dbms)

## Segment Merging

# Segment Merging

Segment merging is the process of combining multiple smaller segments in an Elasticsearch index into larger segments. This optimization reduces the number of segments the search engine needs to consult during a query, leading to faster search performance and more efficient resource utilization. The process involves reading the data from the smaller segments, merging them, and writing the merged data into a new, larger segment.

Visit the following resources to learn more:

- [@official@Merge settings](https://www.elastic.co/docs/reference/elasticsearch/index-settings/merge)
- [@article@Mastering ElasticSearch Write Performance: Refresh, Merge & Flush Explained](https://medium.com/@mokshteng/mastering-elasticsearch-write-performance-refresh-merge-flush-explained-290631930e4a)

## Semantic Search

# Semantic Search

Semantic search aims to improve search accuracy by understanding the intent and contextual meaning of search queries. Instead of relying solely on keyword matching, it analyzes the relationships between words and concepts to deliver more relevant results. This involves using techniques like natural language processing (NLP) and machine learning to interpret the meaning behind the query and match it with documents that have similar meaning, even if they don't contain the exact keywords.

Visit the following resources to learn more:

- [@official@Semantic search](https://www.elastic.co/docs/solutions/search/semantic-search)
- [@official@What is semantic search?](https://www.elastic.co/what-is/semantic-search)
- [@article@Vector-Based Semantic Search using Elasticsearch](https://medium.com/version-1/vector-based-semantic-search-using-elasticsearch-48d7167b38f5)
- [@article@Semantic Searches with Elasticsearch](https://heidloff.net/article/semantic-search-vector-eslasticsearch/)
- [@video@Semantic Search Made Easy & Complex by Sander Philipse, Elastic](https://www.youtube.com/watch?v=tOCwVkoPtI8)
- [@video@Semantic Search Explained: Search with intent [Quick Question Ep. 3]](https://www.youtube.com/watch?v=eZNV_jkbdW0&t=15s)
- [@video@What Is Vector Search? Difference Between Vector & Semantic Search Explained [Quick Question Ep. 5]](https://www.youtube.com/watch?v=BKbScJ2P2P0&t=45s)

## Should

# Should Query

The `should` query is a boolean query that returns documents matching one or more of its sub-queries. It increases the relevance score for each matching clause, but doesn't require any clauses to match for a document to be included in the results. If no other boolean queries like `must` or `filter` are present, at least one `should` clause must match.

Visit the following resources to learn more:

- [@official@Boolean query](https://www.elastic.co/docs/reference/query-languages/query-dsl/query-dsl-bool-query)
- [@article@Elasticsearch Query Bool](https://opster.com/guides/elasticsearch/search-apis/elasticsearch-query-bool/)
- [@article@Elasticsearch Bool Query - Syntax, Example, and Tips](https://pulse.support/kb/elasticsearch-bool-query)
- [@video@Boolean Query in Elasticsearch | Bool, Filter, Must, Must Not, Should, DSL | ES7 for Beginners #4.3](https://www.youtube.com/watch?v=ba2Qn3y486M)
- [@video@Elasticsearch Bool Query (Should & Filter Clauses) - S1E14: Mini Beginner's Crash Course](https://www.youtube.com/watch?v=Uh1F2lezIfY)

## Slm

# SLM

Snapshot Lifecycle Management (SLM) provides a way to automate the creation, retention, and deletion of Elasticsearch snapshots. It allows you to define policies that specify when snapshots should be taken, how long they should be kept, and how they should be named, ensuring consistent and reliable backups of your Elasticsearch data.

Visit the following resources to learn more:

- [@official@Create, monitor and delete snapshots](https://www.elastic.co/docs/deploy-manage/tools/snapshot-and-restore/create-snapshots)
- [@official@Start snapshot lifecycle management](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-slm-start)
- [@article@Elasticsearch SLM – Elasticsearch Snapshot Lifecycle Management](https://opster.com/guides/elasticsearch/operations/elasticsearch-slm-elasticsearch-snapshot-lifecycle-management/)
- [@video@Index Lifecycle Management (ILM) & Snapshot Lifecycle Management (SLM) - Daily Elastic Byte S01E15](https://www.youtube.com/watch?v=JhxMpUY5upg)
- [@video@32 Cluster Management: Automate snapshots with Snapshot Lifecycle Management](https://www.youtube.com/watch?v=-ZNTL1uzFP8)

## Snapshots  Restore

# Snapshots and Restores

Snapshots are backups of your Elasticsearch cluster's data and state, stored in a repository. Restoring from a snapshot allows you to recover data in case of failure, corruption, or accidental deletion. This mechanism provides a way to revert your cluster to a previous point in time, ensuring data safety and disaster recovery capabilities.

Visit the following resources to learn more:

- [@official@Snapshot and restore docs](https://www.elastic.co/docs/deploy-manage/tools/snapshot-and-restore)
- [@official@Restore from snapshot](https://www.elastic.co/docs/troubleshoot/elasticsearch/restore-from-snapshot)
- [@official@Snapshot and Restore](https://www.elastic.co/blog/found-elasticsearch-snapshot-and-restore)
- [@article@Elasticsearch Snapshot and Restore Feature](https://medium.com/orion-innovation-techclub/elasticsearch-snapshot-and-restore-feature-f7d52a9fd40)
- [@video@Elasticsearch Snapshot & Restore: Managing Snapshots within Kibana - Daily Elastic Byte S02E14](https://www.youtube.com/watch?v=hc6V-1aR33E)
- [@video@Backup Elasticsearch Data - Snapshot and Restore -Let's Deploy a Host Intrusion Detection System #15](https://www.youtube.com/watch?v=gIZNez_gmMQ)

## Sorting

# Sorting

Sorting in Elasticsearch lets you order the search results based on the values of specific fields. By default, Elasticsearch sorts results by relevance score, but you can change this to sort by other criteria like date, price, or any other field in your documents. This allows you to present the most relevant or useful information to users based on their specific needs, such as showing the newest products first or listing items from lowest to highest price.

Visit the following resources to learn more:

- [@official@Sort search results](https://www.elastic.co/docs/reference/elasticsearch/rest-apis/sort-search-results)
- [@article@Learn Elasticsearch Sorting in 5 minutes](https://medium.appbase.io/sort-elasticsearch-a-tutorial-on-sorting-with-elasticsearch-762b6c02557f)
- [@article@Elasticsearch in Action: Sorting the Results on Relevancy Score](https://mkonda007.medium.com/elasticsearch-in-action-sorting-the-results-on-relevancy-2913f6389a37)
- [@video@Sorting of results in Elasticsearch | Asc, Desc, Keyword fields [ElasticSearch 7 for Beginners #4.5]](https://www.youtube.com/watch?v=qt5qpfr5s4o)
- [@video@Elasticsearch Part 5: Optimizing Search Results Rendering](https://www.youtube.com/watch?v=qmHY8mlkXZE)

## Source Filtering

# Source Filtering

Source filtering in Elasticsearch allows you to control which fields are returned in the `_source` field of your search results. Instead of retrieving the entire document, you can specify which fields you need, reducing network traffic and improving performance. This is achieved by including or excluding specific fields based on patterns or exact names.

Visit the following resources to learn more:

- [@official@_source field](https://www.elastic.co/docs/reference/elasticsearch/mapping-reference/mapping-source-field)
- [@article@An Overview of Source Filtering, Stored Fields, Fields and Docvalues Fields](https://opster.com/guides/elasticsearch/data-architecture/source-filtering-stored-fields-docvalue/)
- [@article@Elasticsearch in Action: Source Filtering](https://mkonda007.medium.com/elasticsearch-in-action-source-filtering-658ea1a90d24)

## Sql

# Elasticsearch SQL

Elasticsearch SQL allows you to query Elasticsearch data using the familiar SQL syntax. Instead of using Elasticsearch's native query DSL (Domain Specific Language), you can write SQL statements to retrieve, filter, and aggregate data stored in Elasticsearch indices. This provides a more accessible way for users familiar with SQL to interact with Elasticsearch, enabling them to leverage their existing skills to analyze and extract insights from their data.

Visit the following resources to learn more:

- [@official@Tap into Elasticsearch with a familiar syntax](https://www.elastic.co/elasticsearch/sql)
- [@official@SQL overview](https://www.elastic.co/docs/explore-analyze/query-filter/languages/sql)
- [@official@Getting started with SQL](https://www.elastic.co/docs/reference/query-languages/sql/sql-getting-started)
- [@article@Elasticsearch SQL — Leveraging Your SQL Skills for Querying ELK Search Engine Document DB](https://medium.com/@stavsofer/elasticsearch-sql-leveraging-your-sql-skills-for-querying-elk-search-engine-document-db-4be2ac7c4cd0)

## Standard Analyzer

# Standard Analyzer

The Standard Analyzer is a default text analyzer in Elasticsearch that breaks text into individual words based on whitespace and punctuation. It also converts all terms to lowercase and removes common English stop words like "the," "a," and "is." This analyzer is a good general-purpose choice for many text indexing and searching tasks.

Visit the following resources to learn more:

- [@official@Standard analyzer](https://www.elastic.co/docs/reference/text-analysis/analysis-standard-analyzer)
- [@official@Configure text analysis](https://www.elastic.co/docs/manage-data/data-store/text-analysis/configure-text-analysis)
- [@official@Configuring built-in analyzers](https://www.elastic.co/docs/manage-data/data-store/text-analysis/configuring-built-in-analyzers)
- [@article@Elasticsearch Text Analyzers – Tokenizers, Standard Analyzers, Stopwords and More](https://opster.com/guides/elasticsearch/data-architecture/elasticsearch-text-analyzers/)
- [@article@Elasticsearch in Action: Standard Text Analyzer](https://mkonda007.medium.com/elasticsearch-in-action-standard-text-analyzer-87d4164e412e)

## Stats  Extended Stats

# Stats and Extended Stats Aggregations

Stats and Extended Stats aggregations are used to calculate various statistical measures from a set of numeric values. The Stats aggregation provides basic statistics like count, min, max, average, and sum. The Extended Stats aggregation builds upon this by adding standard deviation, sum of squares, variance, and other related metrics, offering a more comprehensive statistical overview of the data.

Visit the following resources to learn more:

- [@official@Stats aggregation](https://www.elastic.co/docs/reference/aggregations/search-aggregations-metrics-stats-aggregation)
- [@official@Extended stats aggregation](https://www.elastic.co/docs/reference/aggregations/search-aggregations-metrics-extendedstats-aggregation)
- [@article@Elasticsearch Stats Aggregation - Syntax, Example, and Tips](https://pulse.support/kb/elasticsearch-stats-aggregation)
- [@article@Elasticsearch Extended Stats Aggregation - Syntax, Example, and Tips](https://pulse.support/kb/elasticsearch-extended-stats-aggregation)

## Synonyms Graph

# c

Synonyms Graph is a feature in Elasticsearch that allows you to expand your search queries by including words or phrases that have similar meanings. Instead of just searching for the exact terms entered by a user, Elasticsearch can also search for related terms defined as synonyms, improving the recall of search results. The "graph" aspect refers to how these synonyms are represented internally, allowing for more complex relationships between terms, including multi-word synonyms and different synonym types.

Visit the following resources to learn more:

- [@official@Search with synonyms](https://www.elastic.co/docs/solutions/search/full-text/search-with-synonyms)
- [@official@Update your synonyms in Elasticsearch: Introducing the synonyms Synonyms Guide](https://www.elastic.co/guide/en/app-search/current/synonyms-guide.html)
- [@official@Multi-Token Synonyms and Graph Queries in Elasticsearch](https://www.elastic.co/blog/multitoken-synonyms-and-graph-queries-in-elasticsearch)
- [@official@Update your synonyms in Elasticsearch: Introducing the synonyms API](https://www.elastic.co/search-labs/blog/update-synonyms-elasticsearch-introducing-synonyms-api)
- [@video@How to use the Elasticsearch Synonym API to improve search accuracy](https://www.youtube.com/watch?v=lJaiVZbCpbY)
- [@video@ElasticSearch in Python #25 - Synonyms API](https://www.youtube.com/watch?v=kOm8r7v0yu4)

## Term Query

# Term Query

A term query is a simple search that looks for documents containing an exact, unanalyzed term in a specific field. It's like searching for a specific word or value without any stemming, synonyms, or other text processing applied. This query is useful when you know the precise value you're looking for and want to find documents that contain it exactly as is.

Visit the following resources to learn more:

- [@official@Term query](https://www.elastic.co/docs/reference/query-languages/query-dsl/query-dsl-term-query)
- [@article@Elasticsearch Term Query - Syntax, Example, and Tips](https://pulse.support/kb/elasticsearch-term-query)
- [@article@Elasticsearch match query vs term query](https://medium.com/@musabdogan/elasticsearch-match-query-vs-term-query-42d9d0cef694)
- [@video@Term queries in Elasticsearch and OpenSearch](https://www.youtube.com/watch?v=YzU-HOn2uns)

## Terms

# Terms Aggregation

The Terms aggregation is a multi-bucket aggregation that groups documents based on the terms found in a specific field. It analyzes the field's values and creates buckets for each unique term, counting the number of documents that contain that term. This allows you to identify the most frequent terms within your data and gain insights into the distribution of values in a field.

Visit the following resources to learn more:

- [@official@Terms aggregation](https://www.elastic.co/docs/reference/aggregations/search-aggregations-bucket-terms-aggregation)
- [@official@Multi Terms aggregation](https://www.elastic.co/docs/reference/aggregations/search-aggregations-bucket-multi-terms-aggregation)
- [@official@Unveiling unique patterns: A guide to significant terms aggregation in Elasticsearch](https://www.elastic.co/search-labs/blog/significant-terms-aggregation-elasticsearch)
- [@official@Bucket](https://www.elastic.co/docs/reference/aggregations/bucket)
- [@article@Elasticsearch Terms Aggregation - Syntax, Example, and Tips](https://pulse.support/kb/elasticsearch-terms-aggregation)
- [@article@Terms Aggregation on High-Cardinality Fields in Elasticsearch](https://opster.com/guides/elasticsearch/search-apis/terms-aggregation-on-high-cardinality-fields-in-elasticsearch/)
- [@video@Elasticsearch Bucket, Histogram, Range & Terms Aggregations - S1E17 Mini Beginner's Crash Course](https://www.youtube.com/watch?v=R114ib2D9mU)

## Text

# Text Data Type

The `text` data type in Elasticsearch is designed for storing and indexing full-text content, such as blog posts, articles, or product descriptions. When you index a field as `text`, Elasticsearch analyzes the text using an analyzer. This process involves breaking the text into individual terms (tokens), lowercasing them, removing stop words, and applying stemming. This analysis enables Elasticsearch to perform full-text searches, allowing users to find documents based on relevant keywords or phrases within the text.

Visit the following resources to learn more:

- [@official@Text type family](https://www.elastic.co/docs/reference/elasticsearch/mapping-reference/text-type-family)
- [@official@Text analysis](https://www.elastic.co/docs/manage-data/data-store/text-analysis)
- [@article@Elasticsearch Keyword vs. Text](https://opster.com/guides/elasticsearch/search-apis/elasticsearch-strings-keyword-vs-text-vs-wildcard/)
- [@article@Elasticsearch: Text vs. Keyword](https://www.codecurated.com/blog/elasticsearch-text-vs-keyword/)

## The Analyze Api

# The Analyze API

The Analyze API in Elasticsearch allows you to break down a text string into its individual terms, which are the basic building blocks for searching and indexing. It simulates the analysis process that Elasticsearch performs when indexing or searching documents, letting you see how a specific analyzer would process a given piece of text. This is useful for testing and debugging your analysis configuration.

Visit the following resources to learn more:

- [@official@Get tokens from text analysis](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-indices-analyze)
- [@official@Test an analyzer](https://www.elastic.co/docs/manage-data/data-store/text-analysis/test-an-analyzer)
- [@article@Leveraging the Elasticsearch Analyze API for Advanced Text Analysis](https://www.dhiwise.com/post/leveraging-the-elasticsearch-analyze-api-for-text-analysis)

## The Elk Stack

# The ELK Stack

The ELK Stack is a collection of three open-source projects: Elasticsearch, Logstash, and Kibana. Elasticsearch is a search and analytics engine. Logstash is a data processing pipeline that ingests data from various sources, transforms it, and then feeds it into Elasticsearch. Kibana lets users visualize data with charts and graphs in Elasticsearch. Together, they form a powerful solution for log management, security analytics, and observability.

Visit the following resources to learn more:

- [@official@Meet the search platform that helps you search, solve, and succeed](https://www.elastic.co/elastic-stack)
- [@article@What is ELK Stack?](https://aws.amazon.com/what-is/elk-stack/)
- [@video@What is Elasticsearch?](https://www.youtube.com/watch?v=ZP0NmfyfsoM)
- [@video@Install ElasticSearch Logstash and Kibana on Windows 10 (ELK Stack) (Elastic Stack)](https://www.youtube.com/watch?v=8iXZTS7f_hY&list=PLS1QulWo1RIYkDHcPXUtH4sqvQQMH3_TN)

## The Inverted Index

# The Inverted Index

The inverted index is a data structure that stores a mapping from content, such as words or numbers, to their locations in a document or a set of documents. Instead of listing documents and then the words they contain, an inverted index lists words and then the documents in which those words appear. This allows for very fast full-text searches.

Visit the following resources to learn more:

- [@official@Elasticsearch from the Bottom Up, Part 1](https://www.elastic.co/blog/found-elasticsearch-from-the-bottom-up)
- [@article@What is the inverted index in elastic search?](https://medium.com/@sujathamudadla1213/what-is-the-inverted-index-in-elastic-search-f04df6f0c806)
- [@article@Elasticsearch Inverted Index: The Key to Fast Data Retrieval](https://www.datasunrise.com/knowledge-center/elasticsearch-inverted-index/)
- [@article@Indexing: Inverted Index](https://www.baeldung.com/cs/indexing-inverted-index)
- [@video@Inverted Index - The Data Structure Behind Search Engines](https://www.youtube.com/watch?v=iHHqnyThrqE)

## The Split Brain Problem

# The "Split Brain" Problem

The "split brain" problem occurs in distributed systems when a cluster of nodes becomes partitioned into two or more independent sub-clusters that are unable to communicate with each other. Each sub-cluster may then believe it is the primary cluster and start making independent decisions, potentially leading to data inconsistencies and conflicts as each sub-cluster operates as if it's the only authority. This situation can result in data loss or corruption when the partitions eventually rejoin.

Visit the following resources to learn more:

- [@official@Quorum-based decision making](https://www.elastic.co/docs/deploy-manage/distributed-architecture/discovery-cluster-formation/modules-discovery-quorums)
- [@article@Avoiding the Elasticsearch split brain problem, and how to recover](https://bigdataboutique.com/blog/avoiding-the-elasticsearch-split-brain-problem-and-how-to-recover-f6451c)
- [@article@Split-Brain in Distributed Systems](https://dzone.com/articles/split-brain-in-distributed-systems)

## Transform Api

# Transform API

The Transform API in Elasticsearch provides a way to summarize and transform data from one or more Elasticsearch indices into a new index. It essentially automates the process of creating aggregated views of your data, allowing you to perform tasks like data reduction, feature engineering, and creating summary indices for faster analysis and visualization. This API enables you to create new indices that contain pre-computed aggregations and transformations of your source data.

Visit the following resources to learn more:

- [@official@Create a transform](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-transform-put-transform)
- [@official@Get transforms](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-transform-get-transform)
- [@article@Elasticsearch Transform APIs](https://opster.com/guides/elasticsearch/data-architecture/transform-apis-in-elasticsearch/)

## Understanding Similarity

# Understanding Similarity

Similarity in information retrieval refers to the algorithm used to calculate the relevance score between a search query and a document. It determines how closely a document matches the search terms, influencing the order in which search results are presented. Different similarity algorithms consider factors like term frequency, inverse document frequency, and field length to produce a score reflecting the degree of relevance.

Visit the following resources to learn more:

- [@official@similarity](https://www.elastic.co/docs/reference/elasticsearch/mapping-reference/similarity)
- [@official@Similarity settings](https://www.elastic.co/docs/reference/elasticsearch/index-settings/similarity)
- [@official@Similarity in Elasticsearch](https://www.elastic.co/blog/found-similarity-in-elasticsearch)
- [@official@Vector similarity techniques and scoring](https://www.elastic.co/search-labs/blog/vector-similarity-techniques-and-scoring)

## Update By Query

# Update by Query

Update by Query is a way to update documents that match a specific query. Instead of retrieving each document individually, modifying it, and then re-indexing it, Update by Query allows you to perform updates on multiple documents in a single operation based on a search query. This is particularly useful for making bulk changes to your data based on certain criteria.

Visit the following resources to learn more:

- [@official@_update_by_query](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-update-by-query)
- [@official@Update by query API examples](https://www.elastic.co/docs/reference/elasticsearch/rest-apis/update-by-query-api)
- [@video@How to use Update by Query in Elastic Search to add fields or update fields](https://www.youtube.com/watch?v=KcEnajtYAJM)

## Update Document

# Update Document

Updating a document in Elasticsearch involves modifying an existing document's data. You can achieve this using the Update API, which allows you to change specific fields or the entire document. The API uses a script or a partial document to specify the changes. When using a script, you can perform complex updates based on the document's current state. Alternatively, providing a partial document will merge the provided fields with the existing document. Elasticsearch then reindexes the document with the updated information.

Visit the following resources to learn more:

- [@official@Update a document](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-update)
- [@official@Update a document](https://www.elastic.co/docs/reference/elasticsearch/rest-apis/update-document)
- [@article@Elasticsearch Update Document Field](https://opster.com/guides/elasticsearch/operations/elasticsearch-update-document-field/)
- [@video@How to Update a Document in Elasticsearch that Has Already Been Indexed](https://www.youtube.com/watch?v=Uo_Avtu_aY4v)

## Value Count

# Value Count Aggregation

Value Count is a type of metric aggregation that calculates the total number of values present in a specific field. It essentially counts how many documents have a value for the chosen field, including duplicates if they exist. This aggregation is useful for determining the overall occurrence or frequency of a particular field within your dataset.

Visit the following resources to learn more:

- [@official@Aggregations](https://www.elastic.co/docs/explore-analyze/query-filter/aggregations)
- [@official@Count search results](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-count)
- [@official@Value count aggregation](https://www.elastic.co/docs/reference/aggregations/search-aggregations-metrics-valuecount-aggregation)
- [@article@Elasticsearch Value Count Aggregation - Syntax, Example, and Tips](https://pulse.support/kb/elasticsearch-value-count-aggregation)
- [@video@Elasticsearch Aggregations & go-elasticsearch - Elastic Meetup](https://www.youtube.com/watch?v=y5MUNPJzMsI)

## Vector Search

# Vector Search

Vector search is a method of searching for data based on its meaning or context, rather than exact keyword matches. It involves representing data as high-dimensional vectors, where each vector captures the semantic properties of the data. Search queries are also converted into vectors, and the system finds data points with vectors that are "close" to the query vector, indicating semantic similarity.

Visit the following resources to learn more:

- [@official@Vector search in Elasticsearch](https://www.elastic.co/docs/solutions/search/vector)
- [@official@What is vector search?](https://www.elastic.co/what-is/vector-search)
- [@official@How to set up vector search in Elasticsearch](https://www.elastic.co/search-labs/blog/vector-search-set-up-elasticsearch)
- [@official@A quick introduction to vector search](https://search-labs-redesign.vercel.app/search-labs/blog/introduction-to-vector-search)
- [@article@Elasticsearch Was Great, But Vector Databases Are the Future](https://thenewstack.io/elasticsearch-was-great-but-vector-databases-are-the-future/)
- [@video@What Is Vector Search? Difference Between Vector & Semantic Search Explained [Quick Question Ep. 5]](https://www.youtube.com/watch?v=BKbScJ2P2P0)
- [@video@Elastic Snackable Series: Elasticsearch Vector Search](https://www.youtube.com/watch?v=GYtLxyvWE0w)
- [@video@ElasticON EMEA: The Search for Relevance with Vector Search](https://www.youtube.com/watch?v=MUve9LiEAeI)

## Wildcard Query

# Wildcard Query

A wildcard query lets you search for terms that match a specified pattern. This pattern can include special characters like `*` (representing zero or more characters) and `?` (representing any single character). It's a way to perform flexible text searches when you don't know the exact term you're looking for, allowing you to find variations or partial matches within your data.

Visit the following resources to learn more:

- [@official@Find strings within strings faster with the new wildcard field](https://www.elastic.co/blog/find-strings-within-strings-faster-with-the-new-elasticsearch-wildcard-field)
- [@article@Elasticsearch Wildcard Queries](https://opster.com/guides/elasticsearch/search-apis/elasticsearch-wildcard-queries/)
- [@article@Elasticsearch Wildcard Query - Syntax, Example, and Tips](https://pulse.support/kb/elasticsea)
- [@video@Elasticsearch Query DSL part 6 | Prefix query, wildcard query | Elk Stack](https://www.youtube.com/watch?v=lTJzT8sZmXs)
