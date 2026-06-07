# Code Review Roadmap

## Api Semantics

# Questions to Ask

- API as small as possible, as large as needed?
- Is there one way of doing one thing, not multiple ones?
- Is it consistent, does it follow the principle of least surprise?
- Clean split of API/internals without internals leaking into the API?
- Are there no breaking changes to user-facing parts (API classes, configuration, metrics, log formats, etc)?
- Is a new API generally useful and not overly specific to a single use case?

Learn more from the following resources:

- [@article@API Design Best Practices Guide - Fern](https://buildwithfern.com/post/api-design-best-practices-guide)
- [@article@RESTful API Resource Naming](https://restfulapi.net/resource-naming/)
- [@article@Web API Design Best Practices - Microsoft Azure](https://learn.microsoft.com/en-us/azure/architecture/best-practices/api-design)

## Code Style

# Questions to Ask

- Is the project's formatting style applied?
- Does it adhere to the agreed-upon naming conventions?
- Is it DRY?
- Is the code sufficiently "readable" (method lengths, etc.)?

Learn more from the following resources:

- [@article@The Standard of Code Review - Google](https://google.github.io/eng-practices/review/reviewer/standard.html)
- [@article@Creating a Coding Style Guide for Your Team - Graphite](https://graphite.com/guides/creating-coding-style-guide)
- [@article@Code Smells - Refactoring Guru](https://refactoring.guru/refactoring/smells)

## Documentation

# Questions to Ask

- Are the new features reasonably documented?
- Are all relevant types of documentation covered, such as README, API docs, user guide, reference docs, etc?
- Is the documentation understandable and free of significant typos and grammar mistakes?

Learn more from the following resources:

- [@article@How to Write Software Documentation - Write the Docs](https://www.writethedocs.org/guide/writing/beginners-guide-to-docs/)
- [@article@8 Essential Code Documentation Best Practices - Heretto](https://www.heretto.com/blog/best-practices-for-writing-code-documentation)
- [@article@Looking for Things in a Code Review - Google](https://google.github.io/eng-practices/review/reviewer/looking-for.html)

## Implementation Semantics

# Questions to Ask

- Does it satisfy the original requirements?
- Is it logically correct?
- Is there no unnecessary complexity?
- Is it robust (i.e., no concurrency issues, proper error handling, etc.)?
- Is it performant?
- Is it secure (i.e., no SQL injections, etc.)?
- Is it observable (i.e., metrics, logging, tracing, etc.)?
- Do newly added dependencies pull their weight? Is their license acceptable?

Learn more from the following resources:

- [@article@Three Pillars of Observability: Logs, Metrics and Traces - IBM](https://www.ibm.com/think/insights/observability-pillars)
- [@article@Security Code Review Checklist - Redwerk](https://redwerk.com/blog/security-code-review-checklist/)
- [@article@What Is Clean Code? - Codacy](https://blog.codacy.com/what-is-clean-code)

## Index

# 

Learn more from the following resources:

- [@official@Google Engineering Practices](https://github.com/google/eng-practices)

## Tests

# Questions to Ask

- Are all tests passing?
- Are new features reasonably tested?
- Are corner cases tested?
- Is it using unit tests where possible, integration tests where necessary?
- Are there tests for NFRs, e.g. performance?

Learn more from the following resources:

- [@article@Unit Testing Best Practices - IBM](https://www.ibm.com/think/insights/unit-testing-best-practices)
- [@article@Integration Testing - Microsoft Engineering Playbook](https://microsoft.github.io/code-with-engineering-playbook/automated-testing/integration-testing/)
- [@article@The Practical Test Pyramid - Martin Fowler](https://martinfowler.com/articles/practical-test-pyramid.html)
