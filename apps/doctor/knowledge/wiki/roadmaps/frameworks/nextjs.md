# Nextjs Roadmap

---
jsonUrl: '/jsons/roadmaps/nextjs.json'
pdfUrl: '/pdfs/roadmaps/nextjs.pdf'
renderer: 'editor'
order: 23
briefTitle: 'Next.js'
briefDescription: 'Learn everything you need to master Next.js'
title: 'Next.js'
description: 'Learn everything you need to master Next.js'
hasTopics: true
isNew: true
dimensions:
  width: 968
  height: 3100
schema:
  headline: 'Next.js Roadmap'
  description: 'Learn Next.js with this interactive step by step guide in 2025. We also have resources and short descriptions attached to the roadmap items so you can get everything you want to learn in one place.'
  imageUrl: 'https://roadmap.sh/roadmaps/nextjs.png'
  datePublished: '2025-08-26'
  dateModified: '2025-08-26'
seo:
  title: 'Next.js Roadmap: Master Next.js Framework'
  description: 'Community driven, articles, resources, guides, interview questions, quizzes for learning Next.js. Master the Next.js framework by following the steps, skills, resources and guides listed in this roadmap.'
  keywords:
    - 'next.js roadmap 2025'
    - 'nextjs roadmap 2025'
    - 'learn next.js 2025'
    - 'nextjs learning path 2025'
    - 'guide to learning next.js'
    - 'next.js learning roadmap'
    - 'nextjs roadmap'
    - 'master next.js framework'
    - 'next.js skills'
    - 'next.js skills test'
    - 'next.js concepts'
    - 'learn next.js'
    - 'what is next.js'
    - 'next.js framework roadmap'
    - 'next.js quiz'
    - 'next.js interview questions'
    - 'next.js app router'
    - 'next.js pages router'
    - 'next.js 15 roadmap'
    - 'react framework roadmap'
    - 'full stack next.js'
    - 'next.js server components'
    - 'next.js client components'
relatedRoadmaps:
  - 'react'
  - 'frontend'
  - 'typescript'
  - 'javascript'
  - 'nodejs'
  - 'full-stack'
sitemap:
  priority: 1
  changefreq: 'monthly'
tags:
  - 'roadmap'
  - 'main-sitemap'
  - 'skill-roadmap'
---

---

## Adapters

# Adapter

Next.js can be adapted to run on different platforms to support their infrastructure capabilities, including AWS Amplify Hosting, Cloudflare, Deno Deploy, Netlify, and Vercel.

Visit the following resources to learn more:

- [@official@Deployment with Adapters](https://nextjs.org/docs/app/getting-started/deploying#adapters)

## Analytics

# Analytics

Next.js has built-in support for measuring and reporting performance metrics. You can either use the `useReportWebVitals` hook to manage reporting yourself, or alternatively, Vercel provides a managed service to automatically collect and visualize metrics for you.

Visit the following resources to learn more:

- [@official@How to add analytics to your Next.js application](https://nextjs.org/docs/app/guides/analytics)
- [@official@useReportWebVitals](https://nextjs.org/docs/app/api-reference/functions/use-report-web-vitals)

## Api Endpoints

# API Endpoints 

API Routes let you create an API endpoint inside a Next.js app. API endpoints work differently in Pages routers and App Routers:

* Pages Router: Historically, Next.js used pages/api/* for APIs. This approach relied on Node.js request/response objects and an Express-like API.
* App Router (Default): Introduced in Next.js 13, the App Router fully embraces web standard Request/Response APIs. Instead of pages/api/*, you can now place `route.ts` or `route.js` files anywhere inside the app/ directory.

Visit the following resources to learn more:

- [@official@Route Handlers and Middleware](https://nextjs.org/docs/app/getting-started/route-handlers-and-middleware)
- [@official@API Routes for Pages Router](https://nextjs.org/docs/pages/building-your-application/routing/api-routes)
- [@official@Building APIs with Next.js](https://nextjs.org/blog/building-apis-with-nextjs)
- [@video@Next.js 15 Tutorial - Route Handlers](https://www.youtube.com/watch?v=27Uj6BeIDV0)

## App

# App Router

The App Router is a file-system based router that uses React's latest features, such as [Server Components](https://react.dev/reference/rsc/server-components), [Suspense](https://react.dev/reference/react/Suspense), and [Server Functions](https://react.dev/reference/rsc/server-functions)

Visit the following resources to learn more:

- [@official@App Router Tutorial](https://nextjs.org/learn/dashboard-app)
- [@video@Next js Tutorial for Beginners | Nextjs 13 (App Router) with TypeScript](https://www.youtube.com/watch?v=ZVnjOPwW4ZA)

## Caching Data

# Caching Data

Caching data in Next.js involves storing the results of data fetches so that subsequent requests for the same data can be served faster. Instead of repeatedly fetching data from a database or API, Next.js can retrieve it from the cache. This improves performance and reduces the load on your data sources. Caching can be configured at different levels.

Caching behavior changes depending on whether the route is statically or dynamically rendered, data is cached or uncached, and whether a request is part of an initial visit or a subsequent navigation. Depending on your use case, you can configure the caching behavior for individual routes and data requests.

Visit the following resources to learn more:

- [@official@Caching and Revalidating](https://nextjs.org/docs/app/getting-started/caching-and-revalidating)

## Caching

# Caching API Endpoints in Next.js

When you don't know the exact route segment names ahead of time and want to create routes from dynamic data, you can use Dynamic Segments that are filled in at request time or prerendered at build time. One example is catch-all segments, which allow you to extend API Routes  to catch all subsequent paths.

Visit the following resources to learn more:

- [@official@Catch-all Segments for App Router](https://nextjs.org/docs/app/api-reference/file-conventions/dynamic-routes#catch-all-segments)
- [@official@Catch all API routes for Page Router](https://nextjs.org/docs/pages/building-your-application/routing/api-routes#catch-all-api-routes)
- [@video@Next.js 15 Tutorial - Catch all Segments](https://www.youtube.com/watch?v=d46hLIg1B3Q)

## Client Rendered

# Client-Side Rendering in Next.js

Client-Side Rendering (CSR) means the browser receives a minimal HTML page from the server. The browser then downloads the JavaScript code, which is responsible for rendering the entire user interface. The JavaScript code fetches the data and dynamically generates the HTML content in the browser. This approach shifts the rendering workload from the server to the client's browser.

Visit the following resources to learn more:

- [@official@Server and Client Components for App Router](https://nextjs.org/docs/app/getting-started/server-and-client-components)
- [@official@Client-side Rendering for Pages Router](https://nextjs.org/docs/pages/building-your-application/rendering/client-side-rendering)
- [@official@Client Components](https://nextjs.org/docs/14/app/building-your-application/rendering/client-components)
- [@video@Next.js 15 Tutorial - Server and Client Components](https://www.youtube.com/watch?v=dMCSiA5gzkU)

## Client

# Client-Side Data Fetching

Client-side data fetching involves retrieving data directly in the user's browser using JavaScript. This happens after the initial HTML content is loaded. When a user interacts with a page, or after a certain event, the browser makes a request to an API or data source. The fetched data is then used to update the user interface dynamically, without requiring a full page reload. 

Client-side data fetching is useful when your page doesn't require SEO indexing, when you don't need to pre-render your data, or when the content of your pages needs to update frequently.  It's important to note that using client-side data fetching can affect the performance of your application and the load speed of your pages. This is because the data fetching is done at the time of the component or pages mount, and the data is not cached.

Visit the following resources to learn more:

- [@official@Client-side Fetching for App Router](https://nextjs.org/docs/app/getting-started/fetching-data#client-components)
- [@official@Client-side Fetching for Pages Router](https://nextjs.org/docs/pages/building-your-application/data-fetching/client-side)
- [@video@Next.js 15 Tutorial - Fetching Data in Client Components](https://www.youtube.com/watch?v=7Kz4--kCBP0)

## Composition

# Rendering Composition

Rendering composition is the practice of building complex user interfaces by combining smaller, reusable components. In Next.js, this is important because it allows you to strategically decide which parts of your application should be pre-rendered on the server for better performance and SEO, and which parts can be rendered on the client for dynamic interactivity. By composing components effectively, you can optimize the rendering strategy for each part of your application, leading to a faster and more efficient user experience.

Visit the following resources to learn more:

- [@official@Server and Client Composition Patterns](https://nextjs.org/docs/14/app/building-your-application/rendering/composition-patterns)
- [@official@Server and Client Components](https://nextjs.org/docs/app/getting-started/server-and-client-components#how-do-server-and-client-components-work-in-nextjs)
- [@video@Next.js 15 Tutorial - Server and Client Components](https://www.youtube.com/watch?v=dMCSiA5gzkU)

## Create Next App

# create-next-app

The create-next-app CLI allow you to create a new Next.js application using the default template or an example from a public GitHub repository. It is the easiest way to get started with Next.js.

Visit the following resources to learn more:

- [@official@create-next-app](https://nextjs.org/docs/app/api-reference/cli/create-next-app)
- [@video@Create Next App | Create Next Js Project](https://www.youtube.com/watch?v=o1cRvsrHbfo)

## Csr

# Client-Side Rendering (CSR)

In Client-Side Rendering (CSR) with React, the browser downloads a minimal HTML page and the JavaScript needed for the page. The JavaScript is then used to update the DOM and render the page. When the application is first loaded, the user may notice a slight delay before they can see the full page, this is because the page isn't fully rendered until all the JavaScript is downloaded, parsed, and executed.

After the page has been loaded for the first time, navigating to other pages on the same website is typically faster, as only necessary data needs to be fetched, and JavaScript can re-render parts of the page without requiring a full page refresh.

Visit the following resources to learn more:

- [@official@Client-side Rendering (CSR)](https://nextjs.org/docs/pages/building-your-application/rendering/client-side-rendering)
- [@article@What is Client-side Rendering (CSR)?](https://prismic.io/blog/client-side-rendering)

## Css In Js

# CSS in JS

It's possible to use any existing CSS-in-JS solution in your existing Next.js Apps and Pages. CSS-in-JS is a technique where CSS styles are written in JavaScript files instead of separate CSS files. This approach allows you to use JavaScript's dynamic capabilities to manage and scope your styles, often using libraries that generate CSS at runtime or build time. It offers benefits like component-level styling, dynamic theming, and easier management of CSS dependencies.

Visit the following resources to learn more:

- [@official@How to use CSS-in-JS libraries in App Router](https://nextjs.org/docs/app/guides/css-in-js)
- [@official@How to use CSS-in-JS libraries in Pages Router](https://nextjs.org/docs/pages/guides/css-in-js)

## Css Modules

# CSS Modules

CSS Modules locally scope CSS by generating unique class names. This allows you to use the same class in different files without worrying about naming collisions.

Visit the following resources to learn more:

- [@official@CSS Modules](https://nextjs.org/docs/app/getting-started/css#css-modules)

## Custom Server

# How to set up a custom server in Next.js

Next.js includes its own server with `next start` by default. If you have an existing backend, you can still use it with Next.js (this is not a custom server). A custom Next.js server allows you to programmatically start a server for custom patterns. The majority of the time, you will not need this approach. However, it's available if you need to eject.

Visit the following resources to learn more:

- [@official@How to set up a custom server in Next.js](https://nextjs.org/docs/app/guides/custom-server)

## Cypress

# Cypress

Next.js supports Cypress for End-to-End (E2E) and Component Testing. With Cypress, you can easily create tests for your modern web applications, debug them visually, and automatically run them in your continuous integration builds.

Visit the following resources to learn more:

- [@official@How to set up Cypress with Next.js](https://nextjs.org/docs/app/guides/testing/cypress)
- [@official@Cypress](https://www.cypress.io/)

## Data Fetching Patterns

# Data Fetching Patterns in Next.js

There are a few recommended patterns and best practices for fetching data in React and Next.js, including: 
* Fetching data on the server.
* Fetching data only where it's necessary.
* Using React's streaming and Suspense features to progressively render and incrementally stream rendered units of the UI to the client.
* Using parallel or sequential fetching depending on your particular use case.
* Using preload data.

Visit the following resources to learn more:

- [@official@Patterns and Best Practices](https://nextjs.org/docs/14/app/building-your-application/data-fetching/patterns#fetching-data-on-the-server)

## Deployment Options

# Deployment Options

Next.js can be deployed in multiple ways, including as a :

* Node.js server, 
* Docker container, 
* static export,
* adapted to run on different platforms.

Visit the following resources to learn more:

- [@official@Deploying in Next.js](https://nextjs.org/docs/app/getting-started/deploying)

## Docker Container

# Docker Container

Next.js can be deployed to any provider that supports Docker containers. This includes container orchestrators like Kubernetes or a cloud provider that runs Docker. Docker deployments support all Next.js features.

Visit the following resources to learn more:

- [@roadmap@Visit the Dedicated Docker Roadmap](https://roadmap.sh/docker)
- [@official@Deployment with Docker](https://nextjs.org/docs/app/getting-started/deploying#nodejs-server)

## Edge

# Edge Runtime

The Edge Runtime is a lightweight JavaScript runtime environment based on V8, designed to execute code closer to the user. It allows you to run server-side logic, like API routes and middleware, on a globally distributed network of servers. This proximity reduces latency and improves the overall performance of your application by minimizing the distance data needs to travel.

Visit the following resources to learn more:

- [@official@What is Edge Runtime?](https://edge-runtime.vercel.app/)
- [@official@Edge Runtime](https://nextjs.org/docs/app/api-reference/edge)

## Environment Variables

# Environment Variables

Environment variables are dynamic values that can affect the behavior of programs on a computer. They are typically used to store configuration settings, API keys, and other sensitive information that should not be hardcoded directly into the application's source code. This allows you to easily change the application's behavior without modifying the code itself, making it more flexible and secure across different environments like development, testing, and production.

Next.js comes with built-in support for environment variables, which allows you to use `.env` to load environment variables, and bundle environment variables for the browser by prefixing with` NEXT_PUBLIC_`

Visit the following resources to learn more:

- [@official@How to use environment variables in Next.js](https://nextjs.org/docs/app/guides/environment-variables)

## Error States

# Error States

Error states in Next.js routing refer to how your application handles situations where a route cannot be successfully loaded or rendered. Errors can be divided into two categories: expected errors and uncaught exceptions.

Expected errors are those that can occur during the normal operation of the application, such as those from server-side form validation or failed requests. These errors should be handled explicitly and returned to the client.

Uncaught exceptions are unexpected errors that indicate bugs or issues that should not occur during the normal flow of your application. These should be handled by throwing errors, which will then be caught by error boundaries.

Visit the following resources to learn more:

- [@official@Error Handling](https://nextjs.org/docs/app/getting-started/error-handling#handling-expected-errors)
- [@video@Next.js 15 Tutorial - Error Handling](https://www.youtube.com/watch?v=fWV5WPSbgdg)

## Eslint

# ESLint

ESLint is an open-source static code analysis tool for JavaScript that identifies problematic patterns and style issues in your code, helping to enforce coding standards and prevent bugs before they occur

Next.js provides an ESLint plugin, `eslint-plugin-next`, already bundled within the base configuration that makes it possible to catch common issues and problems in a Next.js application.

Visit the following resources to learn more:

- [@official@ESLint Plugin](https://nextjs.org/docs/app/api-reference/config/eslint)

## Fetching Locations

# Fetching Location

Data fetching in Next.js allows you to render your content in different ways, depending on your application's use case. By default, layouts and pages are Server Components, which lets you fetch data and render parts of your UI on the server, optionally cache the result, and stream it to the client. When you need interactivity or browser APIs, you can use Client Components to layer in functionality.



These include pre-rendering with Server-side Rendering or Static Generation, and updating or creating content at runtime with Incremental Static Regeneration.

Visit the following resources to learn more:

- [@official@Fetching Data](https://nextjs.org/docs/app/getting-started/fetching-data)
- [@video@Next.js 15 Tutorial - Data Fetching](https://www.youtube.com/watch?v=DRsU93Lde2)

## Fonts

# Font Optimization

The `next/font` module automatically optimizes your fonts and removes external network requests for improved privacy and performance. It includes built-in self-hosting for any font file. This means you can optimally load web fonts with no layout shift.

Visit the following resources to learn more:

- [@official@Font Optimization](https://nextjs.org/docs/app/getting-started/fonts)

## Global Css

# Global CSS

Next.js provides several ways to style your application using CSS. One example is Global CSS, which refers to CSS styles that are applied across your entire application. This means that the styles defined in a global CSS file will affect all elements on every page of your website, unless specifically overridden by more specific CSS rules. It's a way to establish a consistent look and feel throughout your project.

Visit the following resources to learn more:

- [@official@Global CSS](https://nextjs.org/docs/app/getting-started/css#global-css)

## Handling Sensitive Data

# Handling Sensitive Data

Sensitive data, like API keys or user credentials, requires careful management to prevent exposure. In Next.js, you should avoid directly embedding such data in client-side code or committing it to your repository. Instead, leverage environment variables and server-side logic to securely access and utilize sensitive information, ensuring it remains protected from unauthorized access.

Visit the following resources to learn more:

- [@official@How to think about data security in Next.js](https://nextjs.org/docs/app/guides/data-security#data-fetching-approaches)
- [@article@How to Think About Security in Next.js](https://nextjs.org/blog/security-nextjs-server-components-actions)

## Images

# Images

 images account for a huge portion of the typical website’s page weight and can have a sizable impact on your website's LCP performance. The Next.js Image component extends the HTML <img> element with features for automatic image optimization, including:

* Size Optimization: Automatically serve correctly sized images for each device, using modern image formats like WebP and AVIF.
* Visual Stability: Prevent layout shift automatically when images are loading.
* Faster Page Loads: Images are only loaded when they enter the viewport using native browser lazy loading, with optional blur-up placeholders.
* Asset Flexibility: On-demand image resizing, even for images stored on remote servers

Visit the following resources to learn more:

- [@official@Image Optimization](https://nextjs.org/docs/app/getting-started/images)

## Instrumentation

# instrumentation

Instrumentation is the process of using code to integrate monitoring and logging tools into your application. This allows you to track the performance and behavior of your application, and to debug issues in production.

Visit the following resources to learn more:

- [@official@How to set up instrumentation](https://nextjs.org/docs/app/guides/instrumentation)

## Intercepting Routes

# Intercepting Routes

Intercepting routes allows you to load a route from another part of your application within the current layout. This routing paradigm can be useful when you want to display the content of a route without the user switching to a different context. For example, when clicking on a photo in a feed, you can display the photo in a modal, overlaying the feed.

Visit the following resources to learn more:

- [@official@Intercepting Routes](https://nextjs.org/docs/app/api-reference/file-conventions/intercepting-routes)
- [@video@Next.js 15 Tutorial - Intercepting Routes](https://www.youtube.com/watch?v=FTiwIVxWC00)

## Internationalization

# Internationalization

Internationalization is the process of designing and developing applications that can be adapted to various languages and regions without engineering changes. Next.js enables you to configure the routing and rendering of content to support multiple languages. Making your site adaptive to different locales includes translated content (localization) and internationalized routes.

Visit the following resources to learn more:

- [@official@How to implement internationalization in Next.js for App Router](https://nextjs.org/docs/app/guides/internationalization)
- [@official@How to implement internationalization in Next.js for Pages Router](https://nextjs.org/docs/pages/guides/internationalization)

## Introduction

# Introduction

Next.js is a React framework that enables functionalities like server-side rendering and static site generation for web applications. It provides a structure for organizing React components, handling routing, and optimizing performance. Next.js simplifies the process of building production-ready, full-stack web applications with React.

Visit the following resources to learn more:

- [@official@Next.js](https://nextjs.org/)
- [@official@Next.js Docs](https://nextjs.org/docs)
- [@official@Next.js Course](https://nextjs.org/learn)
- [@opensource@Next.js](https://github.com/vercel/next.js)

## Javascript Basics

# JavaScript Basics

JavaScript is a programming language that adds interactivity to websites. It allows you to create dynamic content, control multimedia, animate images, and much more. Think of HTML as the structure of a house, CSS as the interior design, and JavaScript as the electrical system that makes everything work. Understanding JavaScript is crucial before diving into Next.js because Next.js is built on top of React, which itself is a JavaScript library. Without a solid grasp of JavaScript fundamentals, you'll find it difficult to understand and effectively use Next.js's features and concepts.

Visit the following resources to learn more:

- [@roadmap@Visit Dedicated JavaScript Roadmap](https://roadmap.sh/javascript)
- [@article@The Modern JavaScript Tutorial](https://javascript.info/)
- [@video@JavaScript Crash Course for Beginners](https://youtu.be/hdI2bqOjy3c)
- [@feed@Explore top posts about JavaScript](https://app.daily.dev/tags/javascript?ref=roadmapsh)

## Jest

# Jest

Next.js allows you to use Jest for unit testing and snapshot testing. Jest is a JavaScript testing framework created by Facebook, designed for ensuring the correctness of JavaScript code, especially React applications. It provides a complete and easy-to-use solution for writing unit, integration, and end-to-end tests. Jest includes features like a test runner, assertion library, mocking capabilities, and code coverage reporting, making it a popular choice for developers looking to thoroughly test their code.

Visit the following resources to learn more:

- [@official@How to set up Jest with Next.js](https://nextjs.org/docs/app/guides/testing/jest)
- [@official@Jest](https://jestjs.io/)

## Layouts And Templates

# Layouts and Templates

Layouts and templates provide a way to share UI elements across multiple pages, maintaining state and avoiding unnecessary re-renders. Layouts wrap around pages, persisting across route changes to preserve things like navigation bars or sidebars. 

Templates are similar to layouts in that they wrap each child layout or page. Unlike layouts that persist across routes and maintain state, templates create a new instance for each of their children on navigation. This means that when a user navigates between routes that share a template, a new instance of the component is mounted, DOM elements are recreated, state is not preserved, and effects are re-synchronized.

Visit the following resources to learn more:

- [@official@Layouts for App Router](https://nextjs.org/docs/app/api-reference/file-conventions/layout#root-layouts)
- [@official@Layouts for Pages Router](https://nextjs.org/docs/pages/building-your-application/routing/pages-and-layouts)
- [@official@Templates for App Router](https://nextjs.org/docs/app/api-reference/file-conventions/template)
- [@article@A guide to Next.js layouts and nested layouts](https://blog.logrocket.com/guide-next-js-layouts-nested-layouts/)
- [@video@Next.js 15 Tutorial - Layouts](https://www.youtube.com/watch?v=NK-8a8EzWrU)
- [@video@Next.js 15 Tutorial - Templates](https://www.youtube.com/watch?v=yfww2kplO-k)

## Lazy Loading

# Lazy Loading

Lazy loading in Next.js helps improve the initial loading performance of an application by decreasing the amount of JavaScript needed to render a route. It allows you to defer loading of Client Components and imported libraries, and only include them in the client bundle when they're needed. For example, you might want to defer loading a modal until a user clicks to open it.

Visit the following resources to learn more:

- [@official@How to lazy load Client Components and libraries](https://nextjs.org/docs/app/guides/lazy-loading)
- [@article@Lazy loading](https://developer.mozilla.org/en-US/docs/Web/Performance/Guides/Lazy_loading)

## Loading And Streaming

# Loading and Streaming

The special file `loading.js` helps you create meaningful Loading UI with React Suspense. With this convention, you can show an instant loading state from the server while the content of a route segment loads. The new content is automatically swapped in once rendering is complete.

In addition to `loading.js`, you can also manually create Suspense Boundaries for your own UI components. The App Router supports streaming with Suspense for both Node.js and Edge runtimes.

Visit the following resources to learn more:

- [@official@Loading UI and Streaming](https://nextjs.org/docs/14/app/building-your-application/routing/loading-ui-and-streaming)
- [@official@Instant Loading States](https://nextjs.org/docs/14/app/building-your-application/routing/loading-ui-and-streaming#instant-loading-states)
- [@official@Suspense](https://react.dev/reference/react/Suspense)
- [@article@Next.js 15 Tutorial - Loading UI](https://www.youtube.com/watch?v=0OVg4ikUaz0)

## Markdown And Mdx

# Markdown and MDX

Markdown is a lightweight markup language used to format text. It allows you to write using plain text syntax and convert it to structurally valid HTML. It's commonly used for writing content on websites and blogs. MDX is a superset of markdown that lets you write JSX directly in your markdown files. It is a powerful way to add dynamic interactivity and embed React components within your content.

Next.js can support both local MDX content inside your application, as well as remote MDX files fetched dynamically on the server. The Next.js plugin handles transforming markdown and React components into HTML, including support for usage in Server Components (the default in App Router).

Visit the following resources to learn more:

- [@official@How to use markdown and MDX in Next.js](https://nextjs.org/docs/app/guides/mdx)

## Memoization In Fetch

# Memoization in Fetch

Memoization is an optimization technique that speeds up subsequent function calls by caching the results of previous calls with the same input parameters. This approach allows for re-use of data in a React Component tree, prevents redundant network calls and enhances performance
For the initial request, data is fetched from an external source and the result is stored in memory
Subsequent requests for the same data within the same render pass retrieve the result from memory, bypassing the need to make the request again.

Visit the following resources to learn more:

- [@official@Request Memoization](https://nextjs.org/docs/app/guides/caching#request-memoization)
- [@video@Next.js 14 Tutorial - vRequest Memoization](https://www.youtube.com/watch?v=tcLe3Xi0fJE)

## Memory Usage

# Memory Usage

As applications grow and become more feature rich, they can demand more resources when developing locally or creating production builds. Next.js provides several strategies and techniques to optimize memory and address common memory issues in Next.js.

Visit the following resources to learn more:

- [@official@How to optimize memory usage](https://nextjs.org/docs/app/guides/memory-usage)

## Metadata

# Metadata

The Metadata APIs can be used to define your application metadata for improved SEO and web shareability and include:

* The static `metadata` object
* The dynamic `generateMetadata` function
* Special file conventions that can be used to add static or dynamically generated favicons and OG images.

Visit the following resources to learn more:

- [@official@Metadata and OG images](https://nextjs.org/docs/app/getting-started/metadata-and-og-images#static-open-graph-images)

## Middleware

# Middleware

Middleware is a powerful feature that allows you to intercept and run code on the server before a request is completed. Then, based on the incoming request, you can modify the response by rewriting, redirecting, modifying the request or response headers, or responding directly. Middleware executes before routes are rendered. It's particularly useful for implementing custom server-side logic like authentication, logging, or handling redirects.

Visit the following resources to learn more:

- [@official@Middleware for App Router](https://nextjs.org/docs/app/api-reference/file-conventions/middleware)
- [@official@Middleware for Pages Router](https://nextjs.org/docs/pages/api-reference/file-conventions/middleware)
- [@video@Next.js 15 Tutorial - Middleware](https://www.youtube.com/watch?v=t1KTTZbqCm0)

## Nextjs Routing Basics

# Next.js Routing Basics

Routing is the process of defining how an application responds to client requests to specific endpoints (URIs). In Next.js, routing is primarily file-system based. This means that the structure of your `pages` directory directly corresponds to the routes of your application. Each file in the `pages` directory becomes a route based on its filename. For example, a file named `about.js` in the `pages` directory will be accessible at the `/about` route.

Visit the following resources to learn more:

- [@official@https://nextjs.org/docs/pages/building-your-application/routing](https://nextjs.org/docs/pages/building-your-application/routing)
- [@official@Defining Routes](https://nextjs.org/docs/14/app/building-your-application/routing/defining-routes)
- [@video@Next.js 15 Routing Explained For Beginners](https://www.youtube.com/watch?v=qivq_vDYFGk)

## Nextjs

# Next.js

Next.js is a React framework that provides extra features and optimizations on top of React for building web applications. It simplifies development by offering solutions for routing, data fetching, and server-side rendering out of the box. This allows developers to create performant and scalable web applications with less configuration.

Visit the following resources to learn more:

- [@official@Next.js](https://nextjs.org/)
- [@article@Mastering Next.js](https://masteringnextjs.com)
- [@video@Next.js Full course](https://www.youtube.com/watch?v=9P8mASSREYM)
- [@video@Next.js for Beginners - freeCodeCamp](https://youtu.be/KjY94sAKLlw?si=orve81YcY8Fm2vDy)

## Nodejs Server

# Node.js Server

Next.js can be deployed to any provider that supports Node.js. You just have to build your application and start a Node.js server using simple commands. This server supports all Next.js features. If needed, you can also eject to a custom server. Node.js deployments support all Next.js features.

Visit the following resources to learn more:

- [@official@Node.js Server](https://nextjs.org/docs/app/getting-started/deploying#nodejs-server)

## Nodejs

# Node.js

Node.js is a JavaScript runtime environment that executes JavaScript code outside of a web browser. It allows developers to use JavaScript for server-side scripting and to build scalable network applications. Node.js uses an event-driven, non-blocking I/O model that makes it efficient and well-suited for real-time applications.

Visit the following resources to learn more:

- [@roadmap@Visit de Dedicated Node.js Roadmap](https://roadmap.sh/nodejs)
- [@official@Node.js](https://nodejs.org/en/about/)
- [@official@Edge Runtime](https://nextjs.org/docs/app/api-reference/edge)

## Opentelemetry

# OpenTelemetry

Observability is crucial for understanding and optimizing the behavior and performance of your Next.js app. With observability, developers can proactively address issues before they become major problems and provide a better user experience. 

Next.js recommends using OpenTelemetry for instrumenting your apps. It's a platform-agnostic way to instrument apps that allows you to change your observability provider without changing your code. Next.js supports OpenTelemetry instrumentation out of the box, which means that we already instrumented Next.js itself.

Visit the following resources to learn more:

- [@official@How to set up instrumentation with OpenTelemetry](https://nextjs.org/docs/app/guides/open-telemetry)
- [@official@OpenTelemetry Docs](https://opentelemetry.io/docs/)

## Package Bundling

# Package Bundling

Bundling external packages can significantly improve the performance of your application. By default, packages imported inside Server Components and Route Handlers are automatically bundled by Next.js for enhanced optimization.

Visit the following resources to learn more:

- [@official@How to optimize package bundling](https://nextjs.org/docs/app/guides/package-bundling)

## Pages

# Pages Router

The Pages Router in Next.js is a file-system based router built around the `pages` directory. Each file in the `pages` directory becomes a route based on its file name. For example, a file named `about.js` would create a route at `/about`. This approach simplifies routing by automatically mapping files to routes, making it easy to create and manage different pages within your application.

Visit the following resources to learn more:

- [@official@Pages Router](https://nextjs.org/docs/pages)
- [@official@Pages Router Tutorial](https://nextjs.org/learn/pages-router)

## Parallel Routes

# Parallel Routes

Parallel Routes allows you to simultaneously or conditionally render one or more pages within the same layout. They are useful for highly dynamic sections of an app, such as dashboards and feeds on social sites.

Visit the following resources to learn more:

- [@official@Parallel Routes](https://nextjs.org/docs/app/api-reference/file-conventions/parallel-routes)
- [@video@Next.js 15 Tutorial - Parallel Routes](https://www.youtube.com/watch?v=697kNwfU-4M)

## Parallel Vs Sequential

# Parallel vs Sequential

When fetching data inside React components, you need to be aware of two data fetching patterns: Parallel and Sequential. 

With sequential data fetching, requests in a route are dependent on each other and therefore create waterfalls. There may be cases where you want this pattern because one fetch depends on the result of the other, or you want a condition to be satisfied before the next fetch to save resources. However, this behavior can also be unintentional and lead to longer loading times. 

With parallel data fetching, requests in a route are eagerly initiated and will load data at the same time. This reduces client-server waterfalls and the total time it takes to load data.

Visit the following resources to learn more:

- [@official@Parallel and sequential data fetching](https://nextjs.org/docs/14/app/building-your-application/data-fetching/patterns#parallel-and-sequential-data-fetching)

## Playwright

# Playwright 

Next.js supports Playwright for End-to-End (E2E) testing. Playwright is a testing framework that lets you automate Chromium, Firefox, and WebKit with a single API. You can use it to write E2E testing.

Visit the following resources to learn more:

- [@official@How to set up Playwright with Next.js](https://nextjs.org/docs/app/guides/testing/playwright)
- [@official@Playwright](https://playwright.dev/)

## Preloading Data

# Preloading data

Another way to optimize data fetching is to use the preload pattern. You can optionally create a preload function to further optimize parallel data fetching. With this approach, you don't have to pass promises down as props. The preload function can also have any name as it's a pattern, not an API.

Visit the following resources to learn more:

- [@official@Preloading data](https://nextjs.org/docs/14/app/building-your-application/data-fetching/patterns#preloading-data)

## Preparing For Production

# Preparing for Production

Before taking Next.js application to production, there are some optimizations and patterns you should consider implementing for the best user experience, performance, and security. Next.js provides a list of best practices when building your application and before going to production. In addition, you should be aware of the automatic Next.js optimizations.

Visit the following resources to learn more:

- [@official@How to optimize your Next.js application for production](https://nextjs.org/docs/app/guides/production-checklist)

## Prettier

# Prettier

Prettier is an opinionated code formatter that supports many languages, including JavaScript, TypeScript, and CSS. It automatically formats your code to adhere to a consistent style, ensuring readability and maintainability across your project. 

The ESLint Plugin contains code formatting rules, which may conflict with your existing Prettier setup. To make ESLint and Prettier work together, you can include `eslint-config-prettier` in your ESLint config.

Visit the following resources to learn more:

- [@official@ESLint Plugin with Prettier](https://nextjs.org/docs/app/api-reference/config/eslint#with-prettier)
- [@opensource@eslint-config-prettier](https://github.com/prettier/eslint-config-prettier)

## React Cache

# React Cache function

The React `cache` function allows you to memoize the return value of a function, allowing you to call the same function multiple times while only executing it once.

`fetch` requests using the `GET` or `HEAD` methods are automatically memoized, so you do not need to wrap it in React `cache`. However, for other `fetch` methods, or when using data fetching libraries (such as some database, CMS, or GraphQL clients) that don't inherently memoize requests, you can use `cache` to manually memoize data requests.

Visit the following resources to learn more:

- [@official@React cache function](https://nextjs.org/docs/app/guides/caching#react-cache-function)

## React Frameworks

# React Frameworks

React frameworks provide structure and tools to streamline the development of React applications. They offer solutions for common challenges like routing, data fetching, state management, and build processes, allowing developers to focus on building features rather than configuring infrastructure. These frameworks often include pre-built components, optimized performance configurations, and conventions that promote code organization and maintainability.

Visit the following resources to learn more:

- [@article@Comparing The Top React Frameworks](https://dev.to/surajondev/comparing-the-top-cra-alternatives-9cg)

## Reditects

# Redirects in Next.js API Endpoints

Redirects in Next.js API endpoints allow you to send a user from one URL to another. This is useful for various scenarios, such as moving or renaming pages, handling temporary content changes, or guiding users to a different part of your application based on specific conditions. By sending an HTTP redirect response, the server instructs the client's browser to navigate to the new URL.

Visit the following resources to learn more:

- [@official@How to handle redirects in Next.js for App Router](https://nextjs.org/docs/app/guides/redirecting)
- [@official@redirectHow to handle redirects in Next.js for Pages Router](https://nextjs.org/docs/pages/guides/redirecting)

## Remix

# Remix

Remix is a full-stack web framework that focuses on web standards and modern web development patterns. It emphasizes server-side rendering and progressive enhancement to deliver fast and resilient user experiences. Remix leverages web fundamentals like HTTP caching and distributed systems to build robust and performant web applications.

Visit the following resources to learn more:

- [@official@Remix](https://remix.run/)
- [@official@Remix Docs](https://v2.remix.run/docs/)
- [@video@Remix Crash Course 2023](https://www.youtube.com/watch?v=RBYJTop1e-g)

## Rendering Pages

# Rendering Pages in Next.js

Rendering refers to the process of converting your code into HTML that can be displayed in a web browser. Next.js offers different strategies for this, including server-side rendering (SSR), static site generation (SSG), incremental static regeneration (ISR), and client-side rendering (CSR). Each method determines when and where the HTML is generated, impacting performance, SEO, and interactivity. Choosing the right rendering strategy depends on the specific needs of each page in your application.

Recently, Next.js has launched a partial prerendering feature, that allows you to combine static and dynamic content in the same route. This improves the initial page performance while still supporting personalized, dynamic data. However, this feature is currently experimental and subject to change, it's not recommended for production.

Visit the following resources to learn more:

- [@official@Rendering Strategies](https://nextjs.org/learn/seo/rendering-strategies)
- [@official@Partial Prerendering](https://nextjs.org/docs/app/getting-started/partial-prerendering)
- [@official@Rendering User Interfaces (UI)](https://nextjs.org/learn/react-foundations/rendering-ui)

## Rendering Strategies

# Rendering Strategies

Rendering strategies determine how your application's user interface is generated and delivered to the user's browser. Different strategies offer varying trade-offs between performance, SEO, and data freshness. Choosing the right rendering strategy is crucial for optimizing your application based on its specific requirements and content characteristics.

Visit the following resources to learn more:

- [@official@Rendering Strategies](https://nextjs.org/learn/seo/rendering-strategies)
- [@official@How to build single-page applications with Next.js](https://nextjs.org/docs/app/guides/single-page-applications)
- [@article@Next.js Rendering Strategies: SSR, SSG, and ISR Compared](https://hybridheroes.de/blog/2023-05-31-next-js-rendering-strategies/)

## Revalidating Cached Data

# Revalidating Cached Data

Revalidation is the process of updating cached data. When you cache data, it's stored for a certain period. After that period, or based on specific events, you might want to refresh the data to ensure your application displays the most up-to-date information. Revalidation allows you to control when and how your cached data is updated, balancing performance with data freshness. Revalidating in Next.js is conducted through the `revalidatePath` and `revalidateTag` functions.

Visit the following resources to learn more:

- [@official@Revalidating](https://nextjs.org/docs/app/guides/caching#revalidating-1)
- [@official@Caching and Revalidating](https://nextjs.org/docs/app/getting-started/caching-and-revalidating#revalidatetag)

## Revalidation Errors

# Revalidation Errors

When revalidation fails, it means the attempt to refresh the cached data encountered an issue, preventing the application from displaying the most up-to-date information. These errors can stem from various sources, such as network connectivity problems, issues with the data source itself (e.g., a database being unavailable), or problems within the revalidation logic. In Next.js, If an error is thrown while attempting to revalidate data, the last successfully generated data will continue to be served from the cache. On the next subsequent request, Next.js will retry revalidating the data.

Visit the following resources to learn more:

- [@official@Error handling and revalidation](https://nextjs.org/docs/14/app/building-your-application/data-fetching/fetching-caching-and-revalidating)

## Route Matcher

# Route Matcher

A route matcher in Next.js middleware allows you to conditionally execute middleware based on the incoming request's path. It defines specific patterns or conditions that the request path must satisfy for the middleware to run. This enables you to apply middleware logic only to certain routes or groups of routes within your application, providing fine-grained control over request handling.

Visit the following resources to learn more:

- [@official@Matcher for App Router](https://nextjs.org/docs/app/api-reference/file-conventions/middleware#matcher)
- [@official@Matcher for Pages Router](https://nextjs.org/docs/pages/api-reference/file-conventions/middleware#matcher)

## Routing Patterns

# Routing Patterns

The App Router provides a set of conventions to help you implement more advanced routing patterns. These include:

* Parallel Routes: Allow you to simultaneously show two or more pages in the same view that can be navigated independently.
* Intercepting Routes: Allow you to intercept a route and show it in the context of another route. 

These patterns allow you to build richer and more complex UIs, democratizing features that were historically complex for small teams and individual developers to implement.

Visit the following resources to learn more:

- [@official@Advanced Routing Patterns](https://nextjs.org/docs/13/app/building-your-application/routing#advanced-routing-patterns)

## Routing Terminology

# Routing Terminology in Next.js

In Next.js, routing is primarily handled through the `app` directory (introduced in Next.js 13) and the older `pages` directory. Key terms include:

*   **Route:** A specific URL path that maps to a particular component or page. For example, `/blog/my-first-post`.

*   **Route Segment:** A part of the URL path. In `/blog/my-first-post`, `blog` and `my-first-post` are route segments.

*   **File-System Routing:** Next.js uses a file-system based router. The structure of your directories and files within the `app` or `pages` directory directly defines your application's routes.

*   **Dynamic Routes:** Routes that include parameters, allowing you to create pages based on data. For example, `/blog/[slug]` where `[slug]` is a dynamic parameter.

*   **Index Route:** The route that is served when a user visits a directory. Typically represented by an `index.js` or `page.js` file within a directory.

*   **Layout:** A component that wraps multiple pages, providing a consistent UI structure (like headers and footers) across different routes.

*   **Link Component:** The `<Link>` component from `next/link` is used for client-side navigation between routes, providing better performance than traditional `<a>` tags.

Visit the following resources to learn more:

- [@official@Project structure and organization](https://nextjs.org/docs/app/getting-started/project-structure)
- [@video@Next.js 15 Tutorial - Routing](https://www.youtube.com/watch?v=9602Yzvd7i)
- [@video@Next.js 15 Tutorial - Nested Routes](https://www.youtube.com/watch?v=H7JjKjkC33c)
- [@video@Next.js 15 Tutorial - Dynamic Routes](https://www.youtube.com/watch?v=k9g6aVLH3p4)
- [@video@Next.js 15 Tutorial - Nested Dynamic Routes](https://www.youtube.com/watch?v=edrJf0GKfAI)

## Runtimes And Types

# Runtimes and Types

In the context of Next.js, runtime refers to the set of libraries, APIs, and general functionality available to your code during execution. On the server, there are two runtimes where parts of your application code can be rendered:

* The Node.js Runtime (default), which has access to all Node.js APIs and is used for rendering your application.
* The Edge Runtime which contains a more limited set of APIs, used in Middleware.

Visit the following resources to learn more:

- [@official@https://nextjs.org/docs/app/api-reference/edge](https://nextjs.org/docs/app/api-reference/edge)

## Sass

# Sass in Next.js

Sass (Syntactically Awesome Style Sheets) is a CSS preprocessor that extends the capabilities of standard CSS. It allows you to use features like variables, nesting, mixins, and functions to write more organized, maintainable, and efficient stylesheets. These features are then compiled into standard CSS that browsers can understand.

Next.js has built-in support for integrating with Sass after the package is installed using both the `.scss` and `.sass` extensions. You can use component-level Sass via CSS Modules and the `.module.scss` or `.module.sass` extension.

Visit the following resources to learn more:

- [@official@Sass](https://sass-lang.com/)
- [@opensource@Sass](https://github.com/sass/sass)
- [@article@How to use Sass in Next.js](https://nextjs.org/docs/app/guides/sass)

## Scripts

# Third-Party Scripts

Third-party scripts are code snippets from external sources that add functionality to your website, such as analytics, advertising, or social media widgets. Next.js allows you to load a third-party script for multiple routes through the `next/script` component, optimizing performance and enhancing control over when and how scripts are executed within your application.




These scripts can impact your website's performance because they often require downloading and executing code from external servers. Managing these scripts effectively is crucial for maintaining a fast and responsive user experience.

Visit the following resources to learn more:

- [@official@How to load and optimize scripts](https://nextjs.org/docs/app/guides/scripts)

## Server Actions

# Server Functions

Server Functions are asynchronous functions that are executed on the server. They can be used in Server and Client Components to handle form submissions and data mutations in Next.js applications. In an `action` or mutation context, they are also called Server Actions.

Visit the following resources to learn more:

- [@official@What are Server Functions?](https://nextjs.org/docs/app/getting-started/updating-data)
- [@video@Next.js Server Actions](https://www.youtube.com/watch?v=gQ2bVQPFS4U)

## Server Rendered

# Server-Side Rendering (SSR)

Server-Side Rendering (SSR) is a technique where a web application's initial HTML is generated on the server in response to a user's request. This pre-rendered HTML is then sent to the client's browser, allowing the user to see the content immediately, even before the JavaScript code is fully executed. This approach contrasts with client-side rendering, where the browser downloads a minimal HTML page and then uses JavaScript to render the content.

Visit the following resources to learn more:

- [@official@Server and Client Components for App Router](https://nextjs.org/docs/app/getting-started/server-and-client-components#when-to-use-server-and-client-components)
- [@official@Server-side Rendering (SSR) for App Router](https://nextjs.org/docs/pages/building-your-application/rendering/server-side-rendering)
- [@official@Server Components](https://nextjs.org/docs/14/app/building-your-application/rendering/server-components)
- [@video@Next.js 15 Tutorial - Server and Client Components](https://www.youtube.com/watch?v=dMCSiA5gzkU)

## Server

# Server-Side Data Fetching for Locations

Fetching data on the server in Next.js allows you to retrieve location information before the page is rendered. This approach improves performance by reducing the amount of work the client's browser needs to do, leading to faster initial page loads and better SEO. Server-side data fetching ensures that the data is available when the page is initially rendered, providing a seamless user experience.

Visit the following resources to learn more:

- [@official@Client-side Fetching](https://nextjs.org/docs/app/getting-started/fetching-data#server-components)
- [@video@Next.js 15 Tutorial - Fetching Data in Server Components](https://www.youtube.com/watch?v=WKfPctdIDek)

## Setting Headers

# Setting Headers in Next.js Middleware

Middleware in Next.js allows you to run code before a request is completed. Setting headers within middleware enables you to modify the HTTP response headers, controlling aspects like caching, security policies, or custom information passed to the client. This provides a flexible way to manage response behavior based on incoming requests.

Visit the following resources to learn more:

- [@official@Setting Headers for App Router](https://nextjs.org/docs/app/api-reference/file-conventions/middleware#setting-headers)
- [@official@Setting Headers for Pages Router](https://nextjs.org/docs/pages/api-reference/file-conventions/middleware#setting-headers)

## Setting Things Up

# Setting Things Up

Next.js allows you to customize your project to meet specific requirements. This includes integrations with TypeScript, ESlint, and more, as well as internal configuration options such as Absolute Imports and Environment Variables.

Visit the following resources to learn more:

- [@official@Configuration](https://nextjs.org/docs/app/api-reference/config)

## Spa Vs Ssr

# SPA vs SSR

Single-Page Applications (SPAs) load a single HTML page and dynamically update the content using JavaScript, providing a fluid user experience without full page reloads. Server-Side Rendering (SSR), on the other hand, generates the HTML on the server for each request, sending a fully rendered page to the client. Next.js allows you to choose between these approaches or even combine them, offering flexibility in optimizing for performance, SEO, and user experience.

Visit the following resources to learn more:

- [@official@How to build single-page applications with Next.js](https://nextjs.org/docs/app/guides/single-page-applications)
- [@official@Server-side Rendering (SSR)](https://nextjs.org/docs/pages/building-your-application/rendering/server-side-rendering)
- [@article@https://dev.to/santhanam87/ssr-vs-spa-showdown-choosing-the-right-rendering-approach-for-your-web-app-4439](https://dev.to/santhanam87/ssr-vs-spa-showdown-choosing-the-right-rendering-approach-for-your-web-app-4439)

## Spa

# Single-Page Application (SPA) Rendering

A Single-Page Application (SPA) is a web application that loads a single HTML page and dynamically updates that page as the user interacts with the application. This is achieved by using JavaScript to manipulate the DOM (Document Object Model) directly, rather than requesting new HTML pages from the server for each interaction. This approach provides a more fluid and responsive user experience, as the browser doesn't need to reload the entire page for every change.

Visit the following resources to learn more:

- [@official@https://nextjs.org/docs/app/guides/single-page-applications](https://nextjs.org/docs/app/guides/single-page-applications)
- [@article@Single-page application](https://en.wikipedia.org/wiki/Single-page_application)
- [@article@Building Single-Page Applications (SPAs) with React and Next.js](https://medium.com/@blog.iroidsolutions/building-single-page-applications-spas-with-react-and-next-js-c8e02d806145)

## Ssg

# Static Site Generation (SSG)

Static Site Generation (SSG) is a rendering method that generates HTML pages at build time. This means that when a user requests a page, the server sends a pre-rendered HTML file, rather than dynamically generating it on each request. This approach leads to faster load times and improved SEO, as search engines can easily crawl and index the static content.

Visit the following resources to learn more:

- [@official@Static Site Generation (SSG)](https://nextjs.org/docs/pages/building-your-application/rendering/static-site-generation)

## Ssr

# Server-Side Rendering (SSR)

Server-Side Rendering (SSR) is a technique where a web application's HTML is generated on the server in response to each user request. The server then sends the fully rendered HTML to the client's browser, which displays it. This differs from client-side rendering, where the browser downloads a minimal HTML page and then uses JavaScript to render the content.

Visit the following resources to learn more:

- [@official@Server-side Rendering (SSR)](https://nextjs.org/docs/pages/building-your-application/rendering/server-side-rendering)
- [@article@What is Server-Side Rendering: Definition, Benefits and Risks](https://solutionshub.epam.com/blog/post/what-is-server-side-rendering)

## Static Assets

# Static Assets

Static content is any file that is stored in a server and is the same every time it is delivered to users. HTML files and images are examples of this kind of content. Next.js can serve static files under a folder called `public` in the root directory. Files inside `public` can then be referenced by your code starting from the base URL (`/`). It's important to note that Next.js cannot safely cache assets in the public folder because they may change.

Visit the following resources to learn more:

- [@official@public Folder](https://nextjs.org/docs/app/api-reference/file-conventions/public-folder)

## Static Export

# Static Export

Next.js enables starting as a static site or Single-Page Application (SPA), then later optionally upgrading to use features that require a server. Since Next.js supports static exports, it can be deployed and hosted on any web server that can serve HTML/CSS/JS static assets. This includes tools like AWS S3, Nginx, or Apache.

Running as a static export does not support Next.js features that require a server.

Visit the following resources to learn more:

- [@official@Static Export Deployment](https://nextjs.org/docs/app/getting-started/deploying#static-export)

## Static Vs Dynamic

# Static vs Dynamic API Endpoints

API endpoints in Next.js allow you to create serverless functions that handle requests. These endpoints can be either static or dynamic, depending on how their routes are defined and how they process data. Static API endpoints have predefined routes and typically return the same response for every request, while dynamic API endpoints use parameters in their routes to handle different requests and generate responses based on those parameters.

Visit the following resources to learn more:

- [@official@Route Handlers and Middleware](https://nextjs.org/docs/app/getting-started/route-handlers-and-middleware)
- [@official@Dynamic API Routes for Pages Routers](https://nextjs.org/docs/pages/building-your-application/routing/api-routes#dynamic-api-routes)
- [@official@Building APIs with Next.js](https://nextjs.org/blog/building-apis-with-nextjs#12-app-router-vs-pages-router)

## Streaming

# Streaming in Next.js API Endpoints

Streaming in Next.js API endpoints allows you to send data to the client in chunks, rather than waiting for the entire response to be generated on the server before sending anything. This can significantly improve perceived performance, especially for long-running processes or when dealing with large datasets. By sending data incrementally, the client can start processing and displaying information sooner, leading to a more responsive user experience.

Visit the following resources to learn more:

- [@official@Streaming](https://nextjs.org/docs/app/api-reference/file-conventions/route#streaming)
- [@official@Streaming responses](https://nextjs.org/docs/pages/building-your-application/routing/api-routes#streaming-responses)
- [@video@Next.js 15 Tutorial - Streaming](https://www.youtube.com/watch?v=oSf1gUDGJOA)

## Structuring Routes

# Structuring Routes

Structuring routes in Next.js involves organizing your project's file system to define the different URLs (or routes) of your application. Each file within the `app` directory (or `pages` directory in older versions) corresponds to a specific route. The file's location and name directly determine the URL path that users will access. This file-system-based routing simplifies navigation and makes it easy to create a well-organized web application.

Visit the following resources to learn more:

- [@official@Project structure and organization for App Router](https://nextjs.org/docs/app/getting-started/project-structure)
- [@official@Project Structure and Organization for Pages Router](https://nextjs.org/docs/pages/getting-started/project-structure)
- [@video@Next.js 15 Tutorial - Project Structure](https://www.youtube.com/watch?v=L0g87N0piT0)

## Tailwind Css

# Tailwind CSS

Next.js support Tailwind CSS to style your apps. Tailwind CSS is a utility-first CSS framework that provides a set of pre-defined CSS classes that you can use to style your HTML elements directly in your markup. Instead of writing custom CSS rules, you compose styles by applying these utility classes, allowing for rapid UI development and consistent design. This approach promotes a more streamlined workflow by reducing the need to switch between HTML and CSS files.

Visit the following resources to learn more:

- [@official@Tailwind CSS](https://tailwindcss.com/)
- [@official@Tailwind CSS in Next.js](https://nextjs.org/docs/app/getting-started/css#tailwind-css)

## Third Party Libraries

# Third Party Libraries

`@next/third-parties` is a library that provides a collection of components and utilities that improve the performance and developer experience of loading popular third-party libraries, like Google Tag Manager and Google Analytics,  in your Next.js application. All third-party integrations provided by `@next/third-parties` have been optimized for performance and ease of use.

Visit the following resources to learn more:

- [@official@How to optimize third-party libraries](https://nextjs.org/docs/app/guides/third-party-libraries)

## Types Of Routers

# Types of Routers

Next.js has two different routers:

*   **App Router**: The newer router that supports new React features like Server Components.
*   **Pages Router**: The original router, still supported and being improved.

Before Next.js 13, the Pages Router was the main way to create routes in Next.js. It's still supported in newer versions of Next.js, but Next.js recommends migrating to the new App Router to leverage React's latest features.

Visit the following resources to learn more:

- [@official@Next.js Docs](https://nextjs.org/docs#app-router-and-pages-router)
- [@video@Next.js App vs. Pages Router - Which One is Better?](https://www.youtube.com/watch?v=EYDOXzpTRvw)

## Typescript

# TypeScript

TypeScript is a syntactic superset of JavaScript which adds static typing. This means that TypeScript adds syntax on top of JavaScript, allowing developers to add types.

Next.js comes with built-in TypeScript, automatically installing the necessary packages and configuring the proper settings when you create a new project with create-next-app. To add TypeScript to an existing project, rename a file to `.ts` / `.tsx`. Run `next dev` and `next build` to automatically install the necessary dependencies and add a `tsconfig.json` file with the recommended config options.

Visit the following resources to learn more:

- [@official@TypeScript](https://nextjs.org/docs/app/api-reference/config/typescript)

## Use Cases

# Middleware Use Cases

Middleware in Next.js allows you to run code before a request is completed. This provides a flexible way to modify the response by rewriting, redirecting, adding headers, or even directly responding. Common use cases include authentication, authorization, redirecting users based on their location (localization), handling bots, and implementing advanced security measures.

Visit the following resources to learn more:

- [@official@Middleware for App Router](https://nextjs.org/docs/app/api-reference/file-conventions/middleware)
- [@official@Middleware for Pages Router](https://nextjs.org/docs/pages/api-reference/file-conventions/middleware)

## Using Cookies

# Using Cookies in Next.js Middleware

Cookies are small pieces of data that websites store on a user's computer to remember information about them, such as login details, preferences, or shopping cart items. In Next.js middleware, you can access and modify these cookies before a request is handled by your application's routes, allowing you to implement features like authentication, personalization, and A/B testing based on cookie values. This provides a powerful way to control the user experience at the edge.

Visit the following resources to learn more:

- [@official@Using Cookies for App Router](https://nextjs.org/docs/app/api-reference/file-conventions/middleware#using-cookies)
- [@official@Using Cookies for Pages Router](https://nextjs.org/docs/pages/api-reference/file-conventions/middleware#using-cookies)

## Videos

# Videos in Next.js

Next.js provides various approaches and techniques to store and display video files without affecting performance. Videos can be embedded on the page using the HTML `<video>` tag for direct video files and `<iframe>` for external platform-hosted videos.

Visit the following resources to learn more:

- [@official@How to use and optimize videos](https://nextjs.org/docs/app/guides/videos)
- [@video@Add high-performance video to your Nextjs app](https://next-video.dev/docs)

## Vitest

# Vitest

Next.js allows you to use Vitest for unit testing. Vitest is a fast unit test framework powered by Vite. It offers a development experience similar to Vite, making it easy to set up and use in projects that already use Vite for building. Vitest focuses on speed and simplicity, providing features like instant hot module replacement (HMR) and built-in support for TypeScript and JSX.

Visit the following resources to learn more:

- [@official@How to set up Vitest with Next.js](https://nextjs.org/docs/app/guides/testing/vitest)
- [@official@Vitest](https://vitest.dev/)

## Why Frontend Frameworks

# Why Frontend Frameworks?

Building modern web applications often involves managing complex user interfaces, handling data efficiently, and ensuring a smooth user experience. Frontend frameworks like React, Angular, and Next.js provide a structured approach to these challenges. They offer pre-built components, routing solutions, state management tools, and optimized build processes, allowing developers to focus on building features rather than reinventing the wheel. This leads to faster development cycles, more maintainable code, and ultimately, better web applications.

Visit the following resources to learn more:

- [@article@Web3 Frontend – Everything You Need to Learn About Building Dapp Frontends](https://moralis.io/web3-frontend-everything-you-need-to-learn-about-building-dapp-frontends/)
- [@video@What is the difference between a framework and a library?](https://www.youtube.com/watch?v=D_MO9vIRBcA)
- [@video@Which JS Framework is best?](https://www.youtube.com/watch?v=cuHDQhDhvPE)
- [@feed@Explore top posts about Frontend Development](https://app.daily.dev/tags/frontend?ref=roadmapsh)

## Why Nextjs

# Why Next.js?

Next.js is a React framework that provides extra features and optimizations beyond what React offers on its own. When choosing a framework built on React, Next.js stands out because it simplifies development with features like built-in routing, server-side rendering, and static site generation. These capabilities improve performance, SEO, and the overall developer experience compared to building a React application from scratch or using other frameworks that require more manual configuration.

Visit the following resources to learn more:

- [@article@10 Must-Know Benefits of Next.js for Modern Web Apps](https://www.designrush.com/agency/web-development-companies/nextjs/trends/benefits-of-next-js)
- [@article@Next.js 15 Tutorial - Introduction](https://www.youtube.com/watch?v=b4ba60j_4o8)

## Why React

# Why React?

React is a JavaScript library designed for building user interfaces in a declarative and component-based way. It simplifies the process of creating dynamic and interactive web applications by allowing developers to break down complex UIs into smaller, reusable pieces. This approach promotes code maintainability, reusability, and efficiency, making it easier to manage and update large-scale frontend projects. React also works with tools like Redux for data management and React Native for mobile apps. It's popular because it's clear, fast, and has a big community.

Visit the following resources to learn more:

- [@roadmap@Visit Dedicated React Roadmap](https://roadmap.sh/react)
- [@official@React Website](https://react.dev)
- [@video@Full Stack React Developer Course](https://www.youtube.com/watch?v=Bvwq_S0n2pk)
- [@feed@Explore top posts about React](https://app.daily.dev/tags/react?ref=roadmapsh)

## Why Use App Router

# App Router

The App Router in Next.js is a new routing system built on React Server Components, offering enhanced flexibility and performance compared to the traditional Pages Router. Before Next.js 13, the Pages Router was the main way to create routes in Next.js. It's still supported in newer versions of Next.js, but Next.js recommends migrating to the new App Router to leverage React's latest features.

Visit the following resources to learn more:

- [@article@Next.js: App Router vs Pages Router](https://dev.to/dcs-ink/nextjs-app-router-vs-pages-router-3p57)
