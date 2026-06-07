# Forward Deployed Engineer Roadmap

## Agent Architectures

# Agent Architectures

Agent architectures define how an AI agent is structured: how it reasons, selects tools, manages memory, and decides when to stop. Common patterns include ReAct (reason + act), plan-and-execute, and tree-of-thought. Choosing the right architecture depends on how much control the application needs over model behavior and how tolerant the customer is of unpredictable agent outputs.

Visit the following resources to learn more:

- [@article@What is agentic architecture?](https://www.ibm.com/think/topics/agentic-architecture)
- [@article@The Complete Guide to AI Agent Architecture](https://medium.com/@amarg3891/the-complete-guide-to-ai-agent-architecture-25dc2cbe7016)
- [@video@AI Agents, Clearly Explained](https://www.youtube.com/watch?v=FwOTs4UxQS4)

## Ai Agents

# AI Agents
 
AI agents are systems where a language model is given tools and a goal, and takes a sequence of actions to complete a task rather than responding to a single prompt. In practice, most well-designed agents use one LLM call as an orchestrating layer with a series of tool calls around it. Overloading an agent with AI at every step increases token costs and often produces worse results.

Visit the following resources to learn more:

- [@roadmap@Visit the Dedicated AI Agents Roadmap](https://roadmap.sh/ai-agents)
- [@article@Agents in Artificial Intelligence Explained](https://aws.amazon.com/what-is/ai-agents/)
- [@video@What are AI Agents?](https://www.youtube.com/watch?v=F8NKVhkZZWI)

## Ai Engineering Skills

AI Engineering

AI engineering involves building software systems that use machine learning models and large language models (LLMs) as components. This includes selecting models, integrating them via APIs, engineering prompts, managing context, and deploying AI features in production. AI engineering is at the core of the job of FDEs. It's what turns an AI model into a product that runs reliably inside a company's infrastructure.

Visit the following resources to learn more:

- [@article@What Is an AI Engineer? (And How to Become One)](https://www.coursera.org/articles/ai-engineer)
- [@video@AI, Machine Learning, Deep Learning and Generative AI Explained](https://www.youtube.com/watch?v=qYNweeDHiyU)

## Ai Engineering

# AI Engineering

AI engineering involves building software systems that use machine learning models and large language models (LLMs) as components. This includes selecting models, integrating them via APIs, engineering prompts, managing context, and deploying AI features in production. For FDEs, AI engineering is often the core of the engagement to deliver a working AI-powered feature within the customer's existing environment.

Visit the following resources to learn more:

- [@roadmap@Visit the Dedicated AI Engineer Roadmap](https://roadmap.sh/ai-engineer)
- [@article@What Is an AI Engineer? (And How to Become One)](https://www.coursera.org/articles/ai-engineer)
- [@video@AI, Machine Learning, Deep Learning and Generative AI Explained](https://www.youtube.com/watch?v=qYNweeDHiyU)

## Ai Governance

# AI Governance

AI governance refers to the policies, processes, and controls that ensure AI systems behave safely, fairly, and in compliance with regulations and organizational standards. This includes defining acceptable use, managing model risk, ensuring transparency, and monitoring for harmful or biased outputs. Enterprise customers increasingly require AI governance frameworks before they will deploy AI features in production.

Visit the following resources to learn more:

- [@article@What is AI governance?](https://www.ibm.com/think/topics/ai-governance)
- [@video@The Importance of AI Governance](https://www.youtube.com/watch?v=Q020C-Jw0o8)

## Airflow

# Airflow

Apache Airflow is an open-source workflow orchestration platform for scheduling and monitoring data pipelines. Pipelines are defined as Directed Acyclic Graphs (DAGs) in Python, where each node is a task. Many enterprise data teams use Airflow to manage their pipelines, and FDEs may need to add new DAGs, debug failures, or integrate new data sources into an existing Airflow setup.

Visit the following resources to learn more:

- [@official@Airflow Docs](https://airflow.apache.org/docs/)
- [@opensource@airflow](https://airflow.apache.org/docs/)
- [@video@Airflow Tutorial for Beginners](https://www.youtube.com/watch?v=K9AnJ9_ZAXE&list=PLwFJcsJ61oujAqYpMp1kdUBcPG0sE0QMT)

## Api Design

# APIs Design

API design is the process of defining how services communicate with each other through well-structured interfaces. Good API design involves choosing the right protocol (REST, GraphQL, gRPC), defining clear resource models, handling errors consistently, and versioning carefully.

Visit the following resources to learn more:

- [@roadmap@Visit the Dedicated API Design Roadmap](https://roadmap.sh/api-design)
- [@article@What is an API (application programming interface)?](https://www.ibm.com/think/topics/api)
- [@video@What is an API? (in 3 minutes)](https://www.youtube.com/watch?v=s7wmiS2mSXY)

## Api Security

# API Security

API security covers the practices and controls needed to protect APIs from unauthorized access and abuse. This includes authentication, authorization, rate limiting, input validation, and protection against common attacks. When building APIs, it's important to follow the customer's security standards and design endpoints that are not vulnerable to misuse, especially when those APIs expose AI capabilities.

Visit the following resources to learn more:

- [@roadmap@API Security Best Practices](https://roadmap.sh/api-security-best-practices)
- [@article@What Is API Security?](https://www.fortinet.com/resources/cyberglossary/api-security)
- [@video@Top 12 Tips For API Security](https://www.youtube.com/watch?v=6WZ6S-qmtqY)

## Apis Design

# APIs Design
 
API design is the process of defining how services communicate with each other through well-structured interfaces. Good API design involves choosing the right protocol (REST, GraphQL, gRPC), defining clear resource models, handling errors consistently, and versioning carefully.

## Authentication

# Authentication

Authentication is the process of verifying the identity of a user or system. Common mechanisms include username/password, API keys, OAuth 2.0 tokens, and JWTs. In customer environments, FDEs typically need to integrate with an existing identity provider rather than build authentication from scratch, which requires understanding how common auth flows work and how to connect new services to them securely.

Visit the following resources to learn more:

- [@video@Session vs Token Authentication in 100 Seconds](https://www.youtube.com/watch?v=UBUNrFtufWo)
- [@video@How will AI Agents Manage Identity & Build Trust in Complex Systems](https://www.youtube.com/watch?v=wiU7VEvi1LM)

## Aws

# AWS

Amazon Web Services (AWS) is the largest cloud platform by market share, offering services across compute (EC2, Lambda), storage (S3), databases (RDS, DynamoDB), networking, and AI/ML tooling. A large proportion of customer environments run on AWS, making it one of the most common cloud platforms an FDE will need to work within.

Visit the following resources to learn more:

- [@roadmap@Visit the Dedicated AWS Roadmap](https://roadmap.sh/aws)
- [@official@AWS Cloud Essentials](https://aws.amazon.com/getting-started/cloud-essentials/)
- [@official@AWS Training and Certification](https://aws.amazon.com/training/?trk=50fd1d88-f5af-4fa6-9b0b-5a8afc70d2f0&sc_channel=ps&trk=50fd1d88-f5af-4fa6-9b0b-5a8afc70d2f0&sc_channel=ps&ef_id=Cj0KCQjw2_TQBhCnARIsAF3-XhyfwvjJ5p5jx-ax1ZtJ-OhBvXe_kMG6L2PQ-4tzdtYR04RkwTcZ7a4aAq3kEALw_wcB:G:s&s_kwcid=AL!4422!3!795841471846!e!!g!!aws%20courses!23533256377!189966199662&trk=50fd1d88-f5af-4fa6-9b0b-5a8afc70d2f0&sc_channel=ps&ef_id=Cj0KCQjw2_TQBhCnARIsAF3-XhyfwvjJ5p5jx-ax1ZtJ-OhBvXe_kMG6L2PQ-4tzdtYR04RkwTcZ7a4aAq3kEALw_wcB:G:s&s_kwcid=AL!4422!3!795841471846!e!!g!!aws%20courses!23533256377!189966199662&gad_campaignid=23533256377&gbraid=0AAAAADjHtp-d6KYp4kcG8UBYRNKgIuXZy&gclid=Cj0KCQjw2_TQBhCnARIsAF3-XhyfwvjJ5p5jx-ax1ZtJ-OhBvXe_kMG6L2PQ-4tzdtYR04RkwTcZ7a4aAq3kEALw_wcB)
- [@video@AWS Certified Cloud Practitioner Certification Course](https://www.youtube.com/watch?v=7HKot-brXFE)

## Azrue

# Azure

Microsoft Azure is Microsoft's cloud platform with particularly strong adoption in enterprise environments, especially those using Microsoft products like Active Directory, Office 365, and .NET.

Visit the following resources to learn more:

- [@official@Azure Docs](https://learn.microsoft.com/en-us/azure/?product=popular)
- [@video@Microsoft Azure Fundamentals](https://www.youtube.com/watch?v=NPEsD6n9A_I&list=PLGjZwEtPN7j-Q59JYso3L4_yoCjj2syrM)

## Backend Skills

# Backend

Backend development refers to the server-side logic of a web application, including handling requests, running business logic, interacting with databases, and returning responses. Backend systems are typically built with Python, Node.js, Java, or Go, connected to databases and external services. FDEs who can build solid backend systems can own the full delivery of a feature rather than handing off at the API boundary.

Visit the following resources to learn more:

- [@article@What is backend? A comprehensive intro to server-side development](https://alokai.com/blog/what-is-backend)
- [@video@How The Backend Works](https://www.youtube.com/watch?v=4r6WdaY3SOA)

## Backend

# Backend

Backend development refers to the server-side logic of a web application, including handling requests, running business logic, interacting with databases, and returning responses. Backend systems are typically built with Python, Node.js, Java, or Go, connected to databases and external services. FDEs who can build solid backend systems can own the full delivery of a feature rather than handing off at the API boundary.

Visit the following resources to learn more:

- [@roadmap@Visit the Dedicated Backend Developer Roadmap](https://roadmap.sh/backend)
- [@article@What is backend? A comprehensive intro to server-side development](https://alokai.com/blog/what-is-backend)
- [@video@How The Backend Works](https://www.youtube.com/watch?v=4r6WdaY3SOA)

## Build Your Agent

# Build your Agent

You have learned the concepts. Now build one. Pick a real task, something you actually want automated, and build an agent that can do it: define the tools, write the orchestration logic, handle failures, and test it against inputs that are likely to break it. It does not matter if the first version is rough. Getting hands-on with a real agent exposes the gaps that no amount of reading covers, and what you learn from debugging a misbehaving agent is exactly the knowledge you will need when doing it inside a customer environment.

## Building Eval Pipelines

# Building Eval Pipelines

Evaluation pipelines are automated systems for measuring the quality of an AI model or application across a set of test cases. They run inputs through the system, compare outputs to expected results or use a judge model, and surface quality metrics. Eval pipelines give customers a way to measure whether AI features are working, which makes it easier to iterate and build confidence in the system over time.

Visit the following resources to learn more:

- [@article@LLM evaluation: a beginner's guide](https://www.evidentlyai.com/llm-guide/llm-evaluation)
- [@article@Building an Evaluation Harness for Production AI Agents:](https://towardsdatascience.com/building-an-evaluation-harness-for-production-ai-agents-a-12-metric-framework-from-100-deployments/)
- [@video@LLM Evaluation course](https://www.youtube.com/watch?v=rHs0sP7b5fM&list=PL9omX6impEuMgDFCK_NleIB0sMzKs2boI)

## Business Acumen

# Business Acumen

Business acumen is the ability to understand how an organization operates, what its priorities are, how it makes money, and where technology can create real value. Being able to connect engineering decisions to business outcomes is what makes FDEs different from traditional software engineers.

## C

# C++

C++ is a high-performance, statically typed language that gives developers fine-grained control over memory and system resources. It is used in systems programming, game engines, embedded software, and performance-critical applications. While less common in typical web or AI deployments, some customer environments in hardware, robotics, or real-time systems will require at least reading and navigating C++ codebases.

Visit the following resources to learn more:

- [@roadmap@Visit the Dedicated C++ Developer Roadmap](https://roadmap.sh/cpp)
- [@official@Get Started with C++](https://isocpp.org/get-started)
- [@course@Modern Cpp Series By Mike Shah](https://courses.mshah.io/courses/cpp-programming-language)

## Choosing Your Model Provider

# Choosing your Model Provider

Different LLM providers offer models with different tradeoffs in capability, cost, latency, context length, and licensing terms. Common providers include OpenAI, Anthropic, Google, and Meta, as well as providers of open-source models like Hugging Face. FDEs need to be able to evaluate and recommend the right model for a customer's use case, considering not just benchmark performance but also data privacy requirements, cost at scale, and the customer's existing cloud agreements.

Visit the following resources to learn more:

- [@article@Choosing the right model](https://bentoml.com/llm/getting-started/choosing-the-right-model)
- [@article@Beyond vibes: How to properly select the right LLM for the right task](https://aws.amazon.com/blogs/machine-learning/beyond-vibes-how-to-properly-select-the-right-llm-for-the-right-task/)

## Claude Code

# Claude Code

Claude Code is a terminal-based AI tool built by Anthropic. It is designed to reason through complex code problems, explain unfamiliar codebases, and help with debugging. It works best when you need to understand what a piece of code is doing before modifying it; give it a specific problem and it will walk through it step by step.

Visit the following resources to learn more:

- [@roadmap@Visit the Dedicated Claude Code Roadmap](https://roadmap.sh/claude-code)
- [@official@Claude Code Overview](https://code.claude.com/docs/en/overview)
- [@course@Claude Code in Action](https://anthropic.skilljar.com/claude-code-in-action)
- [@article@Vibe coding tutorial: Build your first app with Claude Code](https://roadmap.sh/vibe-coding/tutorial)

## Cloud Platforms

# Cloud Platforms

Cloud platforms provide on-demand access to computing resources, including servers, storage, networking, databases, and managed services. Almost every customer environment runs on one or more cloud providers, so FDEs need to be comfortable operating across at least one of the major platforms, understanding how to deploy services, manage permissions, and navigate the ecosystem of managed offerings.

Visit the following resources to learn more:

- [@article@Cloud Platforms: Revolutionizing Business Operations](https://www.coursera.org/articles/cloud-platforms)
- [@video@Cloud Computing In 6 Minutes](https://www.youtube.com/watch?v=M988_fsOSWo)

## Codex

# Codex

Codex is OpenAI's code-focused model, trained on large amounts of public code, and the model that powers GitHub Copilot. It can generate code from natural language descriptions, complete functions, and assist with documentation. It is one of the foundational tools in the AI-assisted coding ecosystem that FDEs may use or encounter in customer engineering teams.

Visit the following resources to learn more:

- [@official@Codex Overview](https://chatgpt.com/codex)
- [@course@Codex for Builders](https://academy.openai.com/public/clubs/builders-etkn1/resources/codex-for-builders)
- [@video@Codex Full Course 2026](https://www.youtube.com/watch?v=KXIdYEdOPys)

## Communication

# Communication

If you cannot explain what AI can and cannot do to a non-technical VP, you cannot be an FDE. Communication in this role is about translating between two different worlds: the technical reality of what you are building and the business reality of what the customer needs to justify the investment. That means being able to speak about token costs and latency in the same conversation where you are explaining ROI to an executive. It also means knowing when to say AI is not the right answer.

## Complete App With Observability

# Complete App with Observability
 
Take a complete application and make it production-ready by building a sandbox first: a replica of the deployment environment where you can run, test, and debug the system before it touches production. Then add the operational layer: structured logging, distributed tracing, error tracking, performance metrics, and alerts. Once it is running, break something intentionally and use those tools to find it. In a real customer engagement, you will not be there forever. Observability is what lets the customer's team keep the system running after you leave.

## Complete Apps

# Complete Apps

This is where everything connects. Take an idea and build it fully, from the database schema to the API to the frontend. No mocking, no placeholders, no "this would normally connect to X." The point is to experience what it feels like to own a full system: making decisions at every layer, dealing with the friction between them, and ending up with something that actually works. Building complete apps on your own is the best way to develop that instinct before you are doing it under customer pressure.

## Computer Science

# Computer Science

Computer science covers the foundational principles behind how software and computing systems work. This includes programming, algorithms, data structures, system design, and software architecture. These fundamentals matter because FDEs often need to quickly evaluate a customer's existing systems, identify bottlenecks, and make sound architectural decisions.

Visit the following resources to learn more:

- [@roadmap@Visit the Dedicated Computer Science Roadmap](https://roadmap.sh/computer-science)
- [@article@Computer science - Wikipedia](https://en.wikipedia.org/wiki/Computer_science)
- [@video@Early Computing: Crash Course Computer Science](https://www.youtube.com/watch?v=O5nskjZ_GoI)

## Containers

# Containers

Containers are a lightweight way to package an application along with its dependencies and configuration so it runs consistently across environments. Unlike virtual machines, containers share the host operating system kernel, making them fast to start and efficient to run. Containerizing an application is often the first step toward making it deployable in a customer's cloud environment.

Visit the following resources to learn more:

- [@article@What is a Container?](https://www.docker.com/resources/what-container/)
- [@video@What are Containers?](https://www.youtube.com/playlist?list=PLawsLZMfND4nz-WDBZIj8-nbzGFD4S9oz)

## Css

# CSS

CSS, or Cascading Style Sheets, controls the visual appearance of HTML elements on a web page. It handles layout, colors, typography, spacing, animations, and responsive design. Modern CSS includes Flexbox, Grid, and custom properties. Being fluent in CSS is key to produce clean, presentable demos and prototypes.

Visit the following resources to learn more:

- [@roadmap@Visit the Dedicated CSS Roadmap](https://roadmap.sh/css)
- [@article@Learn CSS](https://web.dev/learn/css/)
- [@video@CSS Full Course for Beginners](https://www.youtube.com/watch?v=n4R2E7O-Ngo)

## Cursor

# Cursor

Cursor is a code editor built on top of VS Code with AI assistance integrated throughout. It is particularly useful for navigating and editing large codebases you did not write yourself, which makes it well-suited for working with AI-generated code. You can select any part of the code and ask it to explain, fix, or rewrite it without having to read every line around it.

Visit the following resources to learn more:

- [@official@Cursor Docs](https://cursor.com/docs)
- [@article@Claude Code vs Cursor: Which AI Coding Tool To Choose](https://roadmap.sh/claude-code/vs-cursor)
- [@video@Cursor 2.0 Tutorial for Beginners (Full Course)](https://www.youtube.com/watch?v=2aldTxnbNt0)

## Data Engineering

# Data Engineering

Data engineering involves building and maintaining the systems that collect, store, process, and move data at scale. This includes designing pipelines, working with data warehouses, and ensuring data quality for downstream consumers like analysts and ML systems. FDEs working with enterprise customers often find that data access, transformation, and availability are the first real blockers to building anything useful with AI.

Visit the following resources to learn more:

- [@roadmap@Visit the Dedicated Data Engineer Roadmap](https://roadmap.sh/data-engineer)
- [@article@What is data engineering?](https://www.ibm.com/think/topics/data-engineering)
- [@video@Data Engineering Course for Beginners](https://www.youtube.com/watch?v=PHsC_t0j1dU)
- [@video@Data Engineering Boot camp](https://www.youtube.com/watch?v=myhe0LXpCeo&list=PLwUdL9DpGWU0lhwp3WCxRsb1385KFTLYE)

## Data Pipelines

# Data Pipelines

A data pipeline is a series of steps that move and transform data from one place to another, usually from source systems into a warehouse or processing layer. Pipelines can be batch-based (running on a schedule) or streaming (processing data in real time). Building reliable pipelines means handling failures, schema changes, and data quality issues, all of which are common realities in customer environments.

## Data Privacy  Compliance

# Data Privacy & Compliance

Data privacy ensures personal or sensitive data is handled according to applicable laws and organizational policies, including GDPR, CCPA, HIPAA, and others. For AI systems, this includes what data is sent to third-party model APIs, what is stored, and how long it is retained.

Visit the following resources to learn more:

- [@article@Exploring privacy issues in the age of AI](https://www.ibm.com/think/insights/ai-privacy)
- [@article@AI Data Privacy: A Guide for Modern Industries](https://trustarc.com/resource/ai-applications-used-in-privacy-compliance/)

## Data Structures  Algorithms

# Data Structures & Algorithms

Data structures are ways of organizing data in memory, such as arrays, linked lists, trees, graphs, and hash maps. Algorithms are step-by-step procedures for solving problems, like sorting, searching, or traversal. Knowing these well means being able to evaluate performance characteristics of code, debug inefficiencies in customer systems, and reason clearly about solutions to technical problems.

Visit the following resources to learn more:

- [@roadmap@Visit the Dedicated Data Structures & Algorithms Roadmap](https://roadmap.sh/datastructures-and-algorithms)
- [@article@Data Structures and Algorithms (DSA) Tutorial](https://www.tutorialspoint.com/data_structures_algorithms/index.htm)
- [@video@What Are Data Structures?](https://www.youtube.com/watch?v=bum_19loj9A)

## Devops  Cicd

# DevOps & CI/CD

DevOps is a set of practices that combine software development and IT operations to shorten delivery cycles and ship software more reliably. CI/CD automates the process of testing, building, and deploying code. Understanding the customer's CI/CD setup is often necessary for FDEs to integrate new work into their delivery pipeline without disrupting existing processes.

Visit the following resources to learn more:

- [@roadmap@Visit the Dedicated DevOps Roadmap](https://roadmap.sh/devops)
- [@article@What is CI/CD?](https://www.ibm.com/think/topics/ci-cd)
- [@video@DevOps In 5 Minutes](https://www.youtube.com/watch?v=Xrgk023l4lI)

## Devops Skills

# DevOps Skills
 
DevOps is the practice of automating and streamlining how software is built, tested, and deployed. A forward-deployed engineer who knows DevOps can own the full deployment lifecycle, from spinning up infrastructure to shipping a containerized agent into a client's cloud environment, without depending on another team to get there.

Visit the following resources to learn more:

- [@article@What Is DevOps? A Guide to the Basics](https://www.coursera.org/articles/what-is-devops)
- [@video@DevOps In 5 Minutes](https://www.youtube.com/watch?v=Xrgk023l4lI)

## Discovery  Scoping

# Discovery & Scoping

Discovery and scoping is the phase of a customer engagement where the team identifies the problem to solve, understands the current state of the customer's systems and processes, and defines what success looks like. It involves asking the right questions, identifying constraints, and setting realistic expectations before any building begins. Getting this phase right determines whether the rest of the engagement goes smoothly or runs into avoidable problems.

Visit the following resources to learn more:

- [@article@AI Techniques (Production): Use Case Discovery & System Scoping](https://academy.openai.com/public/clubs/builders-etkn1/videos/ai-techniques-production-use-case-discovery-and-system-scoping-2025-12-11)
- [@article@AI Discovery & Scoping Session](https://www.elevatecorporatetraining.com.au/ai-discovery-scoping/)

## Docker

# Docker

Docker is the leading platform for building, shipping, and running containers. A Dockerfile defines the steps to build a container image, and Docker provides tools to run those images locally or push them to a registry for deployment. Docker is the standard way to package work so it runs reliably in customer environments regardless of local differences in setup.

Visit the following resources to learn more:

- [@roadmap@Visit the Dedicated Docker Roadmap](https://roadmap.sh/docker)
- [@official@Docker Docs](https://docs.docker.com/)
- [@video@Complete Docker Course](https://www.youtube.com/watch?v=RqTEHSBrYFw)

## Dsa  System Design

# DSA & System Design

Data Structures & Algorithms is the study of how to organize and process data efficiently. System Design is the practice of architecting large-scale, reliable systems. Together, they give FDEs the tools to make the right trade-offs when it comes to choosing the right data structure for an agent's memory layer, designing APIs that won't break under enterprise load, or architecting a multi-agent pipeline that scales across an organization.

Visit the following resources to learn more:

- [@article@Data Structures and Algorithms (DSA) Tutorial](https://www.tutorialspoint.com/data_structures_algorithms/index.htm)
- [@article@AI System Design: A Complete Guide](https://www.systemdesignhandbook.com/guides/ai-system-design/)
- [@article@System Design: Complete Guide](https://swimm.io/learn/system-design/system-design-complete-guide-with-patterns-examples-and-techniques)
- [@video@What Are Data Structures?](https://www.youtube.com/watch?v=bum_19loj9A)

## Enterprise Workflow

# Enterprise Workflow

Enterprise workflows are the processes and systems through which large organizations operate, including approvals, handoffs, integrations with existing tools, and compliance requirements. Building for enterprise environments requires understanding these workflows and designing solutions that fit within them.

Visit the following resources to learn more:

- [@article@What is enterprise workflow management?](https://www.manageengine.com/appcreator/enterprise-workflow-management.html)

## From X To Fde

# From X to FDE
 
Three backgrounds tend to transition well into the FDE role: software engineers, consultants, and product managers. Software engineers already have the technical foundation but often need to develop the ability to communicate AI tradeoffs to non-technical stakeholders and build a portfolio that shows they can own a full deployment, not just write code. Consultants and PMs can already translate data into business outcomes, which is half the job, but need to close the gap on engineering by building real agents, RAG pipelines, and eval frameworks from scratch.

Visit the following resources to learn more:

- [@article@The Definitive Guide to Forward Deployed Engineer Interviews in 2026](https://www.sundeepteki.org/advice/the-definitive-guide-to-forward-deployed-engineer-interviews-in-2026)

## From X To Fde

# From X to FDE
 
Three backgrounds tend to transition well into the FDE role: software engineers, consultants, and product managers. Software engineers already have the technical foundation but often need to develop the ability to communicate AI tradeoffs to non-technical stakeholders and build a portfolio that shows they can own a full deployment, not just write code. Consultants and PMs can already translate data into business outcomes, which is half the job, but need to close the gap on engineering by building real agents, RAG pipelines, and eval frameworks from scratch.

Visit the following resources to learn more:

- [@article@The Definitive Guide to Forward Deployed Engineer Interviews in 2026](https://www.sundeepteki.org/advice/the-definitive-guide-to-forward-deployed-engineer-interviews-in-2026)

## Frontend Apps

# Frontend Apps

Put the frontend skills together and build something that lives entirely in the browser. A weather dashboard, a personal finance tracker, a Pomodoro timer, a markdown editor. Use mock data or a public API if you need data, but keep the focus on the frontend itself: how you structure components, manage state, handle routing, and make the interface feel responsive and usable. The goal is to get comfortable making frontend decisions on your own, without a backend to hide behind.

## Frontend Skills

# Frontend

Frontend development refers to the part of web development concerned with what users see and interact with in a browser. It covers HTML for structure, CSS for styling, and JavaScript for interactivity. FDEs who can build functional frontends are more self-sufficient in customer engagements, able to deliver end-to-end demos and working prototypes without depending on a separate frontend team.

Visit the following resources to learn more:

- [@book@Frontend Development Handbook](https://github.com/FrontendMasters/front-end-handbook-2019/blob/master/exports/Front-end%20Developer%20Handbook%202019.pdf)
- [@video@Frontend web development - a complete overview](https://www.youtube.com/watch?v=WG5ikvJ2TKA)

## Frontend

# Frontend

Frontend development refers to the part of web development concerned with what users see and interact with in a browser. It covers HTML for structure, CSS for styling, and JavaScript for interactivity. FDEs who can build functional frontends are more self-sufficient in customer engagements, able to deliver end-to-end demos and working prototypes without depending on a separate frontend team.

Visit the following resources to learn more:

- [@roadmap@Visit the Dedicated Frontend Developer Roadmap](https://roadmap.sh/frontend)
- [@book@Frontend Development Handbook](https://github.com/FrontendMasters/front-end-handbook-2019/blob/master/exports/Front-end%20Developer%20Handbook%202019.pdf)
- [@video@Frontend web development - a complete overview](https://www.youtube.com/watch?v=WG5ikvJ2TKA)

## Full Stack

# Full Stack

Full stack development refers to working across both the frontend and backend of a web application. A full stack developer understands how the client-side and server-side interact and can build across all layers.

Visit the following resources to learn more:

- [@roadmap@Visit the Dedicated Full Stack Developer Roadmap](https://roadmap.sh/full-stack)
- [@article@What is Full Stack Development?](https://aws.amazon.com/what-is/full-stack-development/)
- [@video@Become a Fullstack Developer from Scratch](https://www.youtube.com/watch?v=LzMnsfqjzkA)

## Gcp

# GCP

Google Cloud Platform (GCP) is Google's cloud offering, known for strong data and analytics services like BigQuery and AI/ML infrastructure like Vertex AI. It is often the preferred choice for data-intensive workloads and organizations using Google Workspace.

Visit the following resources to learn more:

- [@official@GCP Docs](https://docs.cloud.google.com/docs)
- [@official@Google Cloud overview](https://docs.cloud.google.com/docs/overview)
- [@video@Google Cloud Essentials](https://www.youtube.com/watch?v=kzKFuHk8ovk&list=PLIivdWyY5sqKh1gDR0WpP9iIOY00IE0xL)

## Gemini

# Gemini

Gemini CLI is Google's command-line AI tool for developers. It assists with code generation, explanation, and refactoring directly in the terminal. It is a practical option if you are already working within Google's ecosystem or want a powerful AI assistant without switching away from your existing terminal workflow.

Visit the following resources to learn more:

- [@official@Google Gemini](https://gemini.google.com/)
- [@video@Gemini Essentials](https://www.youtube.com/watch?v=XKOR4h3CrwE)

## Git  Github

# Git & GitHub

Git is a distributed version control system that tracks changes to code over time and allows multiple people to collaborate on the same codebase. GitHub adds features like pull requests, code review, issue tracking, and CI/CD integrations on top of Git. FDEs regularly work inside customer repositories, contribute to shared codebases, and need to follow existing branching and review conventions from day one.

Visit the following resources to learn more:

- [@roadmap@Visit the Dedicated Git and GitHub Roadmap](https://roadmap.sh/git-github)
- [@official@Getting Started - Installing Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [@video@What is GitHub?](https://www.youtube.com/watch?v=pBy1zgt0XPc)

## Github Actions

# GitHub Actions

GitHub Actions is a CI/CD and automation platform built into GitHub. Workflows are defined in YAML files and triggered by events like pushes, pull requests, or schedules. They can run tests, build container images, and deploy to cloud environments.

Visit the following resources to learn more:

- [@official@GitHub Actions Docs](https://docs.github.com/en/actions)
- [@opensource@Awesome GitHub Actions](https://github.com/sdras/awesome-actions)
- [@video@Automate your Workflow with GitHub Actions](https://www.youtube.com/watch?v=nyKZTKQS_EQ)

## Go

# Go

Go is a statically typed, compiled language developed by Google, designed for simplicity and performance. It is commonly used for building backend services, command-line tools, and cloud infrastructure components. FDEs working in cloud-native or infrastructure-heavy customer environments will often encounter Go-based tooling and services.

Visit the following resources to learn more:

- [@roadmap@Visit the Dedicated Go Developer Roadmap](https://roadmap.sh/golang)
- [@official@Get Started with Go](https://go.dev/doc/tutorial/getting-started)
- [@video@Learn GO Fast: Full Tutorial](https://www.youtube.com/watch?v=8uiZC0l4Ajw)

## Graphql

# GraphQL

GraphQL is a query language and runtime for APIs that lets clients request exactly the fields they need, rather than consuming fixed endpoints with predefined shapes. This makes APIs more flexible and reduces over-fetching, especially in frontend-heavy applications. Some customer stacks use GraphQL, and understanding it makes it easier to integrate with or extend their data layer.

Visit the following resources to learn more:

- [@roadmap@Visit the Dedicated GraphQL Roadmap](https://roadmap.sh/graphql)
- [@official@Get started with GraphQL](https://graphql.org/learn/)
- [@video@GraphQL Course for Beginners](https://www.youtube.com/watch?v=5199E50O7SI)

## Html

# HTML

HTML, or HyperText Markup Language, is the standard language for structuring content on the web. It defines the elements of a page, such as headings, paragraphs, links, forms, and images. It forms the foundation that CSS and JavaScript build on. Understanding HTML is necessary for any frontend work and for reading or modifying web-based customer interfaces.

Visit the following resources to learn more:

- [@roadmap@Visit the Dedicated HTML Roadmap](https://roadmap.sh/html)
- [@official@HTML Docs](https://developer.mozilla.org/en-US/docs/Web/HTML)
- [@video@HTML Tutorial for Beginners: HTML Crash Course](https://www.youtube.com/watch?v=qz0aGYrrlhU)

## Inference Optimization

# Inference Optimization

Inference optimization refers to techniques for making model predictions faster and cheaper without significantly reducing quality. Common approaches include quantization, distillation, response caching, and request batching. Inference costs can become a real issue quickly, and knowing how to optimize without degrading the user experience is a practical skill FDEs should have.

Visit the following resources to learn more:

- [@article@Mastering LLM Techniques: Inference Optimization](https://developer.nvidia.com/blog/mastering-llm-techniques-inference-optimization/)
- [@article@How can I optimize for an inference application?](https://cloud.google.com/discover/inference-optimization?hl=en)
- [@video@AI Inference: The Secret to AI's Superpowers](https://www.youtube.com/watch?v=XtT5i0ZeHHE&t=19s)

## Introduction

# Introduction
 
A Forward Deployed Engineer is a software engineer who works directly inside a customer's environment to build, deploy, and stabilize AI systems. The role originated at Palantir, where engineers called Deltas would embed with clients, sometimes on military bases, to ship code overnight based on feedback from the field that same day. That same idea is now at the center of how companies like OpenAI and Anthropic are bringing AI into large enterprises. The job requires technical depth, the ability to read an unfamiliar codebase quickly, and the communication skills to explain what AI can and cannot do to a non-technical decision maker.

Visit the following resources to learn more:

- [@article@Forward deployed engineer is AI’s hottest job](https://thenewstack.io/forward-deployed-engineer-fde-openai-google/)
- [@article@Forward-deployed engineer: The complete guide](https://www.rocketlane.com/blogs/forward-deployed-engineer)

## Introduction

# Introduction

A Forward Deployed Engineer is a software engineer who works directly inside a customer's environment to build, deploy, and stabilize AI systems. The role originated at Palantir, where engineers called Deltas would embed with clients, sometimes on military bases, to ship code overnight based on feedback from the field that same day. That same idea is now at the center of how companies like OpenAI and Anthropic are bringing AI into large enterprises. The job requires technical depth, the ability to read an unfamiliar codebase quickly, and the communication skills to explain what AI can and cannot do to a non-technical decision maker.

Visit the following resources to learn more:

- [@article@orward deployed engineer is AI’s hottest job](https://thenewstack.io/forward-deployed-engineer-fde-openai-google/)
- [@article@Forward-deployed engineer: The complete guide](https://www.rocketlane.com/blogs/forward-deployed-engineer)

## Java  Scala

# Java / Scala

Java is a statically typed, object-oriented language that runs on the Java Virtual Machine (JVM) and is widely used in enterprise systems, backend services, and Android development. Scala is also a JVM language that blends object-oriented and functional styles, commonly used with Apache Spark. Many enterprise customers, especially in finance or large tech organizations, run significant infrastructure on the JVM.

Visit the following resources to learn more:

- [@roadmap@Visit the Dedicated Java Developer Roadmap](https://roadmap.sh/java)
- [@roadmap@Visit the Dedicated Scala Developer Roadmap](https://roadmap.sh/scala)
- [@official@Scala Docs](https://docs.scala-lang.org/)
- [@article@Introduction to Java](https://hyperskill.org/courses/8)
- [@video@Java for Beginners](https://www.youtube.com/watch?v=eIrMbAQSU34)

## Javascript  Typescript

# JavaScript / TypeScript

JavaScript is the programming language of the web, running natively in browsers and on servers via Node.js. TypeScript is a superset of JavaScript that adds static type annotations, which help catch errors early and improve code maintainability. Together, they cover a large portion of the customer codebases and frontend work that an FDE is likely to encounter.

Visit the following resources to learn more:

- [@roadmap@Visit the Dedicated JavaScript Roadmap](https://roadmap.sh/javascript)
- [@roadmap@Visit the Dedicated TypeScript Roadmap](https://roadmap.sh/typescript)
- [@official@TypeScript for the New Programmer](https://www.typescriptlang.org/docs/handbook/typescript-from-scratch.html)
- [@official@JavaScript Docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
- [@video@JavaScript Crash Course For Beginners](https://www.youtube.com/watch?v=hdI2bqOjy3c&t=2s)

## Javascript

# JavaScript

JavaScript is the scripting language that runs in web browsers, giving web pages dynamic behavior. It handles user interactions, DOM manipulation, API requests, and more. On the server side, JavaScript runs via Node.js. Understanding JavaScript well means being able to work across the full web stack.

Visit the following resources to learn more:

- [@roadmap@Visit the Dedicated JavaScript Roadmap](https://roadmap.sh/javascript)
- [@official@JavaScript Docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
- [@course@JavaScript Tutorial Full Course - Beginner to Pro](https://www.youtube.com/watch?v=EerdGm-ehJQ)

## Kubernetes

# Kubernetes

Kubernetes is an open-source container orchestration system that automates the deployment, scaling, and management of containerized applications. It handles scheduling containers across a cluster, managing service discovery, load balancing, rolling updates, and self-healing. Many enterprise customers run Kubernetes in production, and FDEs need to know enough to deploy and operate services within existing clusters.

Visit the following resources to learn more:

- [@roadmap@Visit the Dedicated Kubernetes Roadmap](https://roadmap.sh/kubernetes)
- [@official@Kubernetes Docs](https://kubernetes.io/docs/home/)
- [@video@Kubernetes Crash Course for Absolute Beginners](https://www.youtube.com/watch?v=s_o8dwzRlu4)

## Latency And Cost Optimization

# Latency and Cost Optimization

Latency and cost optimization in AI systems involves reducing the time and money needed to serve model predictions. Strategies include choosing smaller or faster models, caching responses for repeated queries, batching requests, and routing simpler inputs to cheaper models. These tradeoffs become very real when a customer starts using an AI feature at scale and the initial architecture no longer holds up economically.

Visit the following resources to learn more:

- [@article@The LLM Inference Trilemma: Throughput, Latency, Cost](https://www.digitalocean.com/blog/llm-inference-tradeoffs)
- [@article@LLM Cost Optimization: 5 Levers That Cut API Spend 70-85%](https://www.morphllm.com/llm-cost-optimization)

## Linux Skills

# Linux

Linux is an open-source operating system used widely in servers, cloud environments, and developer workstations. Most production software runs on Linux, so being comfortable navigating a Linux system, managing processes, reading logs, and configuring services is a practical necessity for anyone building and deploying in real customer environments.

Visit the following resources to learn more:

- [@course@Linux for Noobs](https://labex.io/courses/linux-for-noobs)
- [@article@Practice Linux Fundamentals](https://labex.io/linuxjourney)
- [@video@Linux Fundamentals](ttps://www.youtube.com/watch?v=kPylihJRG70)

## Linux

# Linux

Linux is an open-source operating system used widely in servers, cloud environments, and developer workstations. Most production software runs on Linux, so being comfortable navigating a Linux system, managing processes, reading logs, and configuring services is a practical necessity for anyone building and deploying in real customer environments.

Visit the following resources to learn more:

- [@roadmap@Visit the Dedicated Linux Roadmap](https://roadmap.sh/linux)
- [@course@Linux for Noobs](https://labex.io/courses/linux-for-noobs)
- [@article@Practice Linux Fundamentals](https://labex.io/linuxjourney)
- [@video@Linux Fundamentals](https://www.youtube.com/watch?v=kPylihJRG70)

## Llm Fundamentals

# LLM Fundamentals

Large language models (LLMs) are machine learning models trained on large amounts of text data that can generate, summarize, classify, and reason about language. They work by predicting the most likely next tokens given a context window of input. Understanding how LLMs work, including their limitations around hallucination, context length, and latency, helps FDEs build more reliable systems around them and set realistic expectations with customers.

Visit the following resources to learn more:

- [@official@What is a large language model (LLM)?](https://www.cloudflare.com/en-gb/learning/ai/what-is-large-language-model/)
- [@video@How Large Language Models Work](https://www.youtube.com/watch?v=5sLYAQS9sWQ)
- [@video@Building Large Language Models (LLMs) - Standford University](https://www.youtube.com/watch?v=9vM4p9NN0Ts)

## Manage Ml Services

# Managed ML Services

Major Cloud providers offer services that abstract away the infrastructure for training, deploying, and serving machine learning models. Examples include AWS SageMaker, Gemini Enterprise Agent Platform, and Azure Machine Learning. For FDEs building AI features inside customer cloud environments, these services can significantly reduce the time needed to get a model into production.

Visit the following resources to learn more:

- [@official@Amazon SageMaker AI Documentation](https://docs.aws.amazon.com/sagemaker/)
- [@official@Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
- [@official@Azure Machine Learning documentation](https://learn.microsoft.com/en-us/azure/machine-learning/?view=azureml-api-2)

## Mcp

# MCP

The Model Context Protocol (MCP) is an open standard for connecting AI models to external tools and data sources through a unified interface. Instead of building custom integrations for every tool, developers implement MCP servers that expose tools and resources in a standardized way. MCP can simplify connecting AI agents to a customer's existing systems and internal APIs.

Visit the following resources to learn more:

- [@official@What is the Model Context Protocol (MCP)?](https://modelcontextprotocol.io/docs/getting-started/intro)
- [@course@Model Context Protocol (MCP) Course](https://huggingface.co/learn/mcp-course/en/unit0/introduction)
- [@video@What is MCP? Integrate AI Agents with Databases & APIs](https://www.youtube.com/watch?v=eur8dUO9mvE)

## Memory  State Management

# Memory & State Management

Memory refers to how information is stored and retrieved across steps in a conversation or task. Short-term memory lives in the context window, while long-term memory requires external storage like a database or vector store. Managing state well is important when building agents for customer workflows that span multiple steps, sessions, or users.

Visit the following resources to learn more:

- [@article@What is AI agent memory?](https://www.ibm.com/think/topics/ai-agent-memory)
- [@video@Building Brain-Like Memory for AI | LLM Agent Memory Systems](https://www.youtube.com/watch?v=VKPngyO0iKg)
- [@video@The Four Types of Memory Every AI Agent Needs](https://www.youtube.com/watch?v=BacJ6sEhqMo)

## Mlops

# MLOps

MLOps applies DevOps principles to machine learning systems, covering the processes and tooling needed to reliably build, deploy, monitor, and update ML models in production. This includes versioning data and models, automating training pipelines, serving inference at scale, and detecting degradation over time. FDEs building AI features for customers increasingly need MLOps knowledge to ensure those features stay reliable after handoff.

Visit the following resources to learn more:

- [@roadmap@Visit the Dedicated MLOps Roadmap](https://roadmap.sh/mlops)
- [@article@What is MLOps? - Machine Learning Operations Explained](https://aws.amazon.com/what-is/mlops/)
- [@video@What is MLOps?](https://www.youtube.com/watch?v=OejCJL2EC3k)

## Model Deployment

# Model Deployment

Model deployment is the process of making a trained machine learning model available to serve predictions in a production environment. This involves packaging the model, setting up an inference server, exposing an API, and ensuring the system can handle required throughput and latency.

Visit the following resources to learn more:

- [@course@Machine Learning Engineering for Production (MLOps) Specialization](https://imp.i384100.net/nLA5mx)
- [@article@What Is Model Deployment?](https://www.ibm.com/think/topics/model-deployment)
- [@video@Top 5 Most-Used Deployment Strategies](https://www.youtube.com/watch?v=AWVTKBUnoIg)

## Multi Agents

# Multi-Agents

Multi-agent systems involve multiple AI agents working together, where each agent has a specific role or capability, and they coordinate to complete a larger task. One agent might plan the work while others execute specific subtasks. This pattern becomes relevant for complex customer workflows where a single agent would struggle to manage all the context and steps reliably.

Visit the following resources to learn more:

- [@article@Guide to multi-agent systems (MAS)](https://cloud.google.com/discover/what-is-a-multi-agent-system?hl=en)
- [@video@Multi Agent Systems Explained](https://www.youtube.com/watch?v=sWH0T4Zez6I)

## Nodejs

# Node.js

Node.js is a JavaScript runtime built on Chrome's V8 engine that lets developers run JavaScript on the server side. It uses a non-blocking, event-driven architecture well suited for I/O-heavy workloads like APIs and real-time applications. Many customer web stacks include Node.js services, and being able to read, debug, and extend them is a practical advantage.

Visit the following resources to learn more:

- [@roadmap@Visit the Dedicated Node.js Developer Roadmap](https://roadmap.sh/nodejs)
- [@official@Node.js Docs](https://nodejs.org/docs/latest/api/)
- [@video@Node.js Tutorial for Beginners: Learn Node in 1 Hour](https://www.youtube.com/watch?v=TlB_eWDSMt4)

## Nosql Databases

# NoSQL Databases

NoSQL databases store data in formats other than traditional relational tables, such as documents, key-value pairs, graphs, or wide columns. Examples include MongoDB, Redis, Cassandra, and DynamoDB. Customer environments often include NoSQL stores for specific use cases like caching, session management, or high-throughput writes, so knowing how these systems work helps FDEs navigate and extend existing architectures.

Visit the following resources to learn more:

- [@article@NoSQL Explained](https://www.mongodb.com/nosql-explained)
- [@video@SQL vs NoSQL Explained](https://www.youtube.com/watch?v=ruz-vK8IesE)
- [@video@How do NoSQL Databases work](https://www.youtube.com/watch?v=0buKQHokLK8)

## Observability

# Observability

Observability refers to the ability to understand the internal state of a system based on its external outputs, through logging, metrics, and distributed tracing. For AI-powered systems, observability also involves monitoring model outputs, tracking prompt and response quality, and detecting unexpected behavior in production.

Visit the following resources to learn more:

- [@article@What is LLM observability?](https://www.ibm.com/think/topics/llm-observability)
- [@article@LLM Evaluation and AI Observability for Agent Monitoring](https://blog.jetbrains.com/pycharm/2026/05/llm-evaluation-and-ai-observability-for-agent-monitoring/)
- [@video@https://www.youtube.com/watch?v=Q9zd548hqiQ](https://www.youtube.com/watch?v=Q9zd548hqiQ)

## Postgresql

# PostgreSQL

PostgreSQL is a powerful, open-source relational database system that supports advanced features like JSONB storage, full-text search, window functions, and custom data types. It is a widely used database in both startups and large organizations, and knowing it well means being able to work effectively with a large portion of customer backend stacks without a steep learning curve.

Visit the following resources to learn more:

- [@roadmap@Visit the Dedicated PostgreSQL DBA Roadmap](https://roadmap.sh/postgresql)
- [@official@PostgreSQL Docs](https://www.postgresql.org/docs/)
- [@video@Learn PostgreSQL Tutorial - Full Course for Beginners](https://www.youtube.com/watch?v=qw--VYLpxG4)

## Product Feedback Loop

# Product Feedback Loop

A product feedback loop is the cycle of shipping something, collecting feedback from users or stakeholders, and using that input to improve future iterations. This usually means working closely with the customer to observe how the delivered product is actually being used, identifying gaps between expectation and reality, and feeding those observations back into the build process while still on the engagement.

## Prompt Engineering

# Prompt Engineering

Prompt engineering is the practice of crafting inputs to language models in a way that produces more accurate, useful, or reliable outputs. Techniques include zero-shot and few-shot prompting, chain-of-thought reasoning, role assignment, and structured output formatting. Strong prompt engineering skills often determine whether a customer demo works convincingly or falls apart on edge cases.

Visit the following resources to learn more:

- [@roadmap@Visit the Dedicated Prompt Engineering Roadmap](https://roadmap.sh/prompt-engineering)
- [@course@Google Prompting Essentials Specialization](https://www.coursera.org/specializations/prompting-essentials-google)
- [@article@Prompt engineering: overview and guide](https://cloud.google.com/discover/what-is-prompt-engineering?hl=en)

## Prompt Management

# Prompt Management

Prompt management involves organizing, versioning, testing, and iterating on the prompts used in production AI systems. As customer applications grow and include more AI-powered features, managing prompts across different use cases becomes complex. Good prompt management practices ensure that changes to prompts do not introduce regressions and that improvements can be tracked and rolled back if needed.

Visit the following resources to learn more:

- [@article@Prompt management systems compared](https://nearform.com/digital-community/prompt-management-systems-compared/)
- [@video@Prompt Management 101 - Full Guide for AI Engineers](https://www.youtube.com/watch?v=Qddc_DNo9qY)

## Prompt Versioning

# Prompt Versioning

Prompt versioning is the practice of treating prompts like code, tracking changes over time with version control. This makes it possible to roll back to previous versions, compare outputs across versions, and understand what changed when behavior shifted. When handing AI systems to customers, prompt versioning is part of making those systems maintainable after the engagement ends.

## Python

# Python

Python is a general-purpose programming language known for its readable syntax and broad ecosystem. It is widely used in web development, data engineering, scripting, automation, and AI/ML workloads. For FDEs, Python is especially useful because it lets you move fast, prototype quickly, and work across a wide range of customer environments without heavy setup.

Visit the following resources to learn more:

- [@roadmap@Visit the Dedicated Python Developer Roadmap](https://roadmap.sh/python)
- [@article@Automate the Boring Stuff](https://automatetheboringstuff.com/)
- [@video@Python Full Course for free](https://www.youtube.com/watch?v=ix9cRaBkVe0)

## Rags

# RAGs

Retrieval-Augmented Generation (RAG) is a pattern where relevant documents or data are fetched from a knowledge source and injected into a model's context before generating a response. This gives the model access to customer-specific or up-to-date information without requiring fine-tuning. RAG is one of the most common patterns FDEs implement when building AI features on top of a customer's proprietary data.

Visit the following resources to learn more:

- [@article@What is RAG?](https://aws.amazon.com/what-is/retrieval-augmented-generation/)
- [@article@RAG Explained: Understanding Embeddings, Similarity, and Retrieval](https://towardsdatascience.com/rag-explained-understanding-embeddings-similarity-and-retrieval/?utm_source=roadmap&utm_medium=Referral&utm_campaign=TDS+roadmap+integration)
- [@video@What is Retrieval-Augmented Generation? IBM](https://www.youtube.com/watch?v=T-D1OfcDW1M)

## React

# React

React is a JavaScript library for building user interfaces using a component-based model. Each component manages its own state and rendering logic, and components are composed to build complete interfaces. React is one of the most common frontend frameworks in production (especially for building AI-powered apps), so familiarity with it makes it easier to contribute to or extend existing customer frontends quickly.

Visit the following resources to learn more:

- [@roadmap@Visit the Dedicated React Developer Roadmap](https://roadmap.sh/react)
- [@article@Getting Started with React](https://react.dev/learn/tutorial-tic-tac-toe)
- [@video@React Course - Beginners Tutorial for React](https://www.youtube.com/watch?v=bMknfKXIFA8)

## Regression Testing

# Regression Testing

Regression testing for AI systems involves running a set of test cases against a model or prompt to verify that a change has not degraded behavior relative to a previous baseline. Unlike traditional software tests, AI regression tests often use example inputs and expected output properties evaluated by another model or human review.

Visit the following resources to learn more:

- [@article@Watch the language: A tutorial on regression testing for LLMs](https://www.evidentlyai.com/blog/llm-regression-testing-tutorial)
- [@video@What is Regression Testing? A Software Testing FAQ - Why? How? When?](https://www.youtube.com/watch?v=xmQuLTarGI4)

## Requirements Gathering

# Requirements Gathering

Project requirements come from observation as much as from conversation. You watch how teams actually work, not just how they describe their work, because those two things are often different. The goal is to surface the undocumented workflow, the data source people actually trust, and the edge cases that would break an agent in its first week of production. Written requirements are useful, but the real requirements live in the room with the people doing the work.

Visit the following resources to learn more:

- [@course@Requirements Gathering in Business Analysis](https://www.coursera.org/learn/requirements-gathering-in-business-analysis)
- [@article@Requirements Gathering in Software Engineering](https://www.jamasoftware.com/requirements-management-guide/requirements-gathering-and-management-processes/what-is-requirements-gathering/)
- [@video@Requirement Gathering Techniques For A Business Analyst](https://www.youtube.com/watch?v=8EBWxW5Cn1g)

## Roi  Ai Impact

# ROI & AI Impact

Understanding return on investment (ROI) for AI projects means being able to quantify how an AI system creates value, whether through cost savings, productivity improvements, revenue growth, or risk reduction. It also means being honest about what AI can realistically deliver. FDEs who can frame AI work in business terms help customers build confidence in the investment and avoid overselling what the technology can do.

Visit the following resources to learn more:

- [@article@How to maximize AI ROI in 2026](https://www.ibm.com/think/insights/ai-roi)
- [@article@What is ROI and How to Calculate Return on Investment](https://www.esade.edu/beyond/en/what-is-roi-and-how-to-calculate-return-on-investment/)

## Roles  Responsabilities

# Roles & Responsibilities
 
The FDE job has three phases: audit, evals, and deployment. In the audit phase, you embed with different teams inside the customer's organization, map their workflows, identify bottlenecks, and decide where AI can create real value and where it cannot. In the evals phase, you build systems to measure whether the AI is actually working, not just whether it produces an answer, but whether it reasons through problems the way a skilled human would. In the deployment phase, you ship the system into production, starting with the smallest possible unit of autonomy and layering on capabilities only after each step is proven to work.

Visit the following resources to learn more:

- [@article@Forward-deployed engineer: The complete guide](https://www.rocketlane.com/blogs/forward-deployed-engineer)

## Roles  Responsabilities

# Roles & Responsibilities

The FDE job has three phases: audit, evals, and deployment. In the audit phase, you embed with different teams inside the customer's organization, map their workflows, identify bottlenecks, and decide where AI can create real value and where it cannot. In the evals phase, you build systems to measure whether the AI is actually working, not just whether it produces an answer, but whether it reasons through problems the way a skilled human would. In the deployment phase, you ship the system into production, starting with the smallest possible unit of autonomy and layering on capabilities only after each step is proven to work.

Visit the following resources to learn more:

- [@article@Forward-deployed engineer: The complete guide](https://www.rocketlane.com/blogs/forward-deployed-engineer)

## Security

# Security

FDEs are the last line of defense before an agent hits a client's production environment. You need to prove to the customer's security team that the system won't leak data, go rogue, or be manipulated.

Visit the following resources to learn more:

- [@article@What Is LLM (Large Language Model) Security? | Starter Guide](https://www.paloaltonetworks.com/cyberpedia/what-is-llm-security)
- [@video@OWASP's Top 10 Ways to Attack LLMs: AI Vulnerabilities Exposed](https://www.youtube.com/watch?v=gUNXZMcd2jU)
- [@video@LLM Security & Observability Course](https://www.youtube.com/watch?v=dj1H4g4YSlU&list=PLFDswngT2LSgxkC9QPpyr0Ir0zUTOF8Eo)

## Shell  Bash

# Shell / Bash

Bash is a command-line shell and scripting language available on most Unix-like systems. Shell scripts let you automate repetitive tasks, manage files, configure systems, and chain together command-line tools. Being fluent in Bash allows FDEs to move fast in terminal environments, debug deployment issues quickly, and write lightweight automation without reaching for a heavier tool.

Visit the following resources to learn more:

- [@roadmap@Visit the Dedicated Shell/Bash Roadmap](https://roadmap.sh/shell-bash)
- [@article@The Shell Scripting Tutorial](https://www.shellscript.sh/philosophy.html)
- [@video@Shell Scripting Tutorial for Beginners](https://www.youtube.com/playlist?list=PLS1QulWo1RIYmaxcEqw5JhK3b-6rgdWO_)

## Software Architecture

# Software Architecture

Software architecture is the high-level structure of a software system, including how components are organized, how they interact, and what principles guide those design decisions. Common patterns include layered architecture, microservices, event-driven design, and domain-driven design. FDEs need to quickly understand a customer's architecture and make decisions that fit within it, or clearly articulate why a different approach is needed.

Visit the following resources to learn more:

- [@roadmap@Visit the Dedicated Software Design and Architecture Roadmap](https://roadmap.sh/software-design-architecture)
- [@article@What is Software Architecture? A Comprehensive Guide](https://vfunction.com/blog/what-is-software-architecture/)
- [@video@Getting the Basics - Software Architecture Introduction](https://www.youtube.com/watch?v=8UlLgOf20Ho)

## Spark

# Spark

Apache Spark is a distributed computing framework for processing large datasets in parallel across a cluster. It supports batch processing, streaming, SQL queries, and machine learning through a unified API. Customers with large-scale data operations often use Spark as part of their data infrastructure, and knowing it makes it possible to work with or extend their existing pipelines.

Visit the following resources to learn more:

- [@official@Spark Docs](https://spark.apache.org/docs/latest/)
- [@article@What is Spark](https://aws.amazon.com/what-is/apache-spark)
- [@video@Apache Spark full course](https://www.youtube.com/watch?v=S2MUhGA3lEw)

## Sql

# SQL

SQL, or Structured Query Language, is the standard language for interacting with relational databases. It is used to create, read, update, and delete records, and to define the structure of tables and their relationships. FDEs regularly need to query customer databases, understand data models, and sometimes debug or optimize slow queries as part of investigating production issues.

Visit the following resources to learn more:

- [@roadmap@Visit the Dedicated SQL Roadmap](https://roadmap.sh/sql)
- [@article@Introduction to SQl](https://www.thoughtspot.com/sql-tutorial)
- [@article@SQL Tutorial](https://www.sqltutorial.org/)

## Stakeholder Management

# Stakeholder Management

Stakeholder management in FDE work is less about keeping people happy and more about making sure the right people know what is happening before it becomes a problem. This means identifying who the skeptics are early, giving them the evidence they need to trust the system (usually evals), managing expectations before a demo rather than after it goes wrong, and escalating blockers fast rather than letting them quietly slow the engagement. The technical work can be excellent, and the engagement can still fail if the people who need to approve, adopt, or fund the system never get bought in.

Visit the following resources to learn more:

- [@article@Stakeholder Management Guide: Definitions, Processes & More](https://simplystakeholders.com/resources/guides/stakeholder-management/)

## System Design

# System Design

System design is the process of defining the components, data flows, and infrastructure needed to build a scalable and reliable system. It involves decisions around databases, caching, load balancing, APIs, and service boundaries. For FDEs, system design often happens under time pressure and with incomplete information, so knowing common patterns well makes it possible to move quickly without making costly mistakes.

Visit the following resources to learn more:

- [@roadmap@Visit the Dedicated System Design Roadmap](https://roadmap.sh/system-design)
- [@article@AI System Design: A Complete Guide](https://www.systemdesignhandbook.com/guides/ai-system-design/)
- [@article@System Design: Complete Guide](https://swimm.io/learn/system-design/system-design-complete-guide-with-patterns-examples-and-techniques)

## Technical Scoping  Sequencing

# Technical Scoping & Sequencing

Technical scoping involves breaking a project into discrete tasks, estimating their complexity, and identifying dependencies. Sequencing means ordering those tasks logically, starting with the highest-risk or most uncertain parts. A well-scoped and sequenced project is easier to track and deliver on time, and gives the customer visibility into what is being built and in what order.

Visit the following resources to learn more:

- [@article@How to effectively scope your software projects](https://medium.com/free-code-camp/how-to-effectively-scope-your-software-projects-from-planning-to-execution-e96cbcac54b9)
- [@video@Project Scope Statement \[IN 4 EASY STEPS\]](https://www.youtube.com/watch?v=QDLk2QIuJkg)

## Technical Writing

# Technical Writing

Technical writing is the practice of producing clear, accurate, and useful documentation for software systems. This includes API docs, architecture decision records, runbooks, onboarding guides, and design documents. Technical writing is especially important because good documentation is often what allows a customer to operate and extend a system after the engagement ends, without needing to call the FDE back for every question.

Visit the following resources to learn more:

- [@roadmap@Visit the Dedicated Technical Writer Roadmap](https://roadmap.sh/technical-writer)

## Terraform

# Terraform

Terraform is an open-source infrastructure-as-code tool by HashiCorp that lets engineers define cloud resources in configuration files and provision or update them automatically. It works across multiple cloud providers and is the standard tool for managing infrastructure in a repeatable, version-controlled way. FDEs who can write Terraform can provision and tear down customer environments faster and more reliably than doing it manually through cloud consoles.

Visit the following resources to learn more:

- [@roadmap@Visit the Dedicated Terraform Roadmap](https://roadmap.sh/terraform)
- [@official@Terraform Docs](https://developer.hashicorp.com/terraform/docs)
- [@official@What is Terraform?](https://developer.hashicorp.com/terraform/intro)
- [@video@Complete Terraform Course](https://www.youtube.com/watch?v=7xngnjfIlK4)

## Tools  Functions

# Tools & Functions

Tools and functions are the mechanisms through which AI agents interact with the outside world. A tool might query a database, call an external API, run a code interpreter, or search the web. In practice, tools are defined as schemas the model can invoke, and the application handles executing the actual function and returning the result. Designing good tool interfaces is a significant part of making agents reliable.

Visit the following resources to learn more:

- [@article@What are Tools?](https://huggingface.co/learn/agents-course/unit1/tools)
- [@video@What is Tool Calling? Connecting LLMs to Your Data](https://www.youtube.com/watch?v=h8gMhXYAv1k)

## Tradeoffs Scope Speed Quality

# Tradeoffs: Scope, Speed, Quality

Every project involves tradeoffs between scope (how much is built), speed (how fast it is delivered), and quality (how well it holds up over time). Reducing scope can speed things up without sacrificing quality. Cutting corners on quality can speed things up in the short term but creates problems later. FDEs need to understand and communicate these tradeoffs clearly, helping customers make informed decisions rather than just agreeing to everything and delivering less than expected.

Visit the following resources to learn more:

- [@article@Project management triangle: Triple constraint guide](https://asana.com/resources/project-management-triangle)
- [@video@What is the Iron Triangle? Time, Cost, Quality, Scope?](https://www.youtube.com/watch?v=JHSHOAfV-uw)

## Vector Dbs

# Vector DBs

Vector databases store high-dimensional vector embeddings and support efficient similarity search. They are a core component of RAG systems and semantic search applications, where the goal is to find content semantically similar to a query rather than matching keywords exactly.

Visit the following resources to learn more:

- [@article@What is RAG (Retrieval-Augmented Generation)?](https://aws.amazon.com/what-is/retrieval-augmented-generation/)
- [@article@How to Implement Graph RAG Using Knowledge Graphs and Vector Databases](https://towardsdatascience.com/how-to-implement-graph-rag-using-knowledge-graphs-and-vector-databases-60bb69a22759)
- [@video@Complete RAG Tutorial](https://www.youtube.com/playlist?list=PLNIQLFWpQMRUMjxfe8o6g3uzJ6LH_VotY)

## Vibe Coding

# Vibe Coding

Vibe coding refers to using AI-assisted tools to write, edit, and iterate on code through natural language interaction, often at a higher level of abstraction than traditional coding. Instead of writing every line manually, the developer describes intent and guides the AI to produce working code, reviewing and refining the output. Vibe coding tools can significantly accelerate the productivity of FDEs, enabling them to work under tight delivery timelines.

Visit the following resources to learn more:

- [@roadmap@Visit the Dedicated Vibe Coding Roadmap](https://roadmap.sh/vibe-coding)
- [@article@Vibe coding tutorial: Build your first app with Claude Code](https://roadmap.sh/vibe-coding/tutorial)
- [@article@Vibe Coding Best Practices: How To Get Consistent Results](https://roadmap.sh/vibe-coding/best-practices)
- [@video@What is Vibe Coding?](https://www.youtube.com/watch?v=5OWurmg41tI)

## What Is An Fde

# From X to FDE

Three backgrounds tend to transition well into the FDE role: software engineers, consultants, and product managers. Software engineers already have the technical foundation but often need to develop the ability to communicate AI tradeoffs to non-technical stakeholders and build a portfolio that shows they can own a full deployment, not just write code. Consultants and PMs can already translate data into business outcomes, which is half the job, but need to close the gap on engineering by building real agents, RAG pipelines, and eval frameworks from scratch.

Visit the following resources to learn more:

- [@article@The Definitive Guide to Forward Deployed Engineer Interviews in 2026](https://www.sundeepteki.org/advice/the-definitive-guide-to-forward-deployed-engineer-interviews-in-2026)
