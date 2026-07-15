# React Native Roadmap

## Accessibility

# Accessibility

Accessibility (often abbreviated as a11y) in React Native is a crucial aspect of application development that ensures your applications are usable by everyone, including individuals with disabilities. This commitment to inclusivity is not just a legal requirement in many jurisdictions but also a moral imperative that enhances the user experience for all. React Native provides a comprehensive set of accessibility features, attributes, and APIs that allow developers to create applications that cater to diverse user needs. By implementing these features, developers can ensure that their applications are navigable and usable by individuals with visual, auditory, motor, or cognitive impairments.

Visit the following resources to learn more:

- [@official@Accessibility](https://reactnative.dev/docs/accessibility)

## Activityindicator

# Activity Indicator

The `ActivityIndicator` is a core component in React Native that provides a simple visual indication of some ongoing activity or loading state within your application. It shows a spinning animation, which gives the user feedback that something is happening in the background. This component is particularly useful when fetching data from an external source, like a server, or while performing time-consuming operations.

Visit the following resources to learn more:

- [@official@Activity Indicator](https://reactnative.dev/docs/activityindicator)

## Animations

# Animations

React Native supports two types of animations: `Animated` and `LayoutAnimation`. The `Animated` API provides a basic set of methods for creating and managing animations, while the `LayoutAnimation` API provides a way to animate changes from one layout to another.

`Animated` is a declarative API that focuses on handling animation-related calculations. It allows you to create and combine animations with fine-grained control over the specific properties that are being animated. You can use this API to create a variety of effects, such as fading, scaling, and translating components on the screen.

`LayoutAnimation` is a higher-level abstraction for animating changes to the layout. Instead of animating individual properties, you define how the changes should occur and React Native takes care of updating the layout accordingly. This is particularly useful for animating multiple components or modifying the layout in response to user interaction, such as adding/removing/reordering items in a list.

Visit the following resources to learn more:

- [@official@Animations](https://reactnative.dev/docs/animations)
- [@official@LayoutAnimations](https://reactnative.dev/docs/layoutanimation)
- [@official@Animated](https://reactnative.dev/docs/animated)

## Appium

# Appium

Appium is an open-source test automation framework for mobile devices, targeting native, hybrid, or mobile-web apps for iOS, Android, and Windows platforms. Appium works with multiple programming languages, including JavaScript, Ruby, Python, Java, and C#. Appium uses the WebDriver protocol, which allows you to write tests that can interact with your app through a series of commands. The WebDriver protocol interprets these commands into actions that are then performed on the app.

Visit the following resources to learn more:

- [@official@Appium Documentation](https://appium.io/docs/en/latest/)

## Apple App Store

# Publishing Apps in App Store

The App Store is Apple's official platform for distributing iOS apps to users with iPhones, iPads, and iPod Touch devices. To publish an app on the App Store, you need to follow specific guidelines and use the necessary tools provided by Apple.

Visit the following resources to learn more:

- [@official@Publishing to Apple App Store](https://reactnative.dev/docs/publishing-to-app-store)
- [@feed@Explore top posts about App Store](https://app.daily.dev/tags/app-store?ref=roadmapsh)

## Authentication

# Authentication

Authentication is a crucial aspect of securing your React Native application. It enables you to verify the identity of users and give access to protected resources and features. Here are the common methods used for authentication in React Native:

*   JWT Authentication
*   OAuth
*   Simple Token Authentication

Visit the following resources to learn more:

- [@official@Authentication and Deep Linking](https://reactnative.dev/docs/security#authentication-and-deep-linking)
- [@feed@Explore top posts about Authentication](https://app.daily.dev/tags/authentication?ref=roadmapsh)

## Button

# Button

A `Button` is a built-in React Native component used to create clickable buttons. It is a simple, customizable and easy-to-use component that captures touches and triggers an `onPress` event when pressed.

Visit the following resources to learn more:

- [@official@Button](https://reactnative.dev/docs/button)

## Common Problem Sources

# Common Problem Sources

In React Native, several common issues can impact application performance. Excessive console logs can slow down the app, particularly in debug mode, so it's advisable to minimize their use and remove unnecessary logs before release. Heavy and unoptimized images can also cause performance problems; therefore, it's important to optimize image size and resolution and use the `resizeMode` prop on the `Image` component for better rendering. Additionally, inline functions and styles can lead to unnecessary re-renders, so defining them outside the component's render method is recommended. While using `React.PureComponent` or `React.memo()` can enhance performance, they should be applied judiciously to avoid unnecessary re-renders. For handling large lists, replacing `ListView` with `FlatList` or `SectionList` is crucial for better performance. Lastly, blocking the JavaScript thread with heavy synchronous computations can degrade performance, so it's essential to handle such tasks asynchronously or offload them to native modules. Following these guidelines can help maintain optimal performance in React Native applications.

Visit the following resources to learn more:

- [@official@Performance Problems](https://reactnative.dev/docs/performance#common-sources-of-performance-problems)

## Components

# Components

React components are the building blocks of the user interface (UI) in a React application. They are used to break down the UI into reusable, isolated, and manageable pieces. Components handle rendering the UI and managing the logic and behavior.

Visit the following resources to learn more:

- [@official@Components](https://react.dev/learn/your-first-component)
- [@official@Props](https://react.dev/learn/passing-props-to-a-component)

## Connectivity Status

# Connectivity Status

Connectivity refers to the mechanisms that allow data transfer between your React Native app and external resources through various means of communication. It is essential to ensure efficient communication with APIs, servers, and external systems, to update your app's data, fetching content or enabling real-time interactions.

Visit the following resources to learn more:

- [@article@Managing network connection status in React Native](https://blog.logrocket.com/managing-network-connection-status-in-react-native/)

## Core Components

# Core Components

Core components are the essential building blocks provided by React Native to create a user interface for mobile applications. They are platform-agnostic, meaning they work across both iOS and Android devices. Some of the common core components include:

*   `View` is a fundamental component for constructing the user interface. It is equivalent to a `div` in HTML and can be used as a container for other components.
*   `Text` is used to display text content in your app. It is similar to the `p` or `span` elements in HTML.
*   `TextInput` is a basic input field that allows users to type text into your app. It is similar to the `input` element in HTML.
*   `TouchableOpacity` is a wrapper for making elements like `View` and `Text` respond properly to touch events. It provides feedback by reducing the opacity of the wrapped component when pressed.
*   `ScrollView` is a scrollable container that allows users to scroll through its content. It is useful when you have content that exceeds the available screen size.
*   `FlatList` is used to render a list of items using a performant approach. It only renders items that are currently visible on the screen and removes others to save memory.

Visit the following resources to learn more:

- [@official@Core Components and APIs](https://reactnative.dev/docs/components-and-apis)
- [@official@Core Components and Native Components](https://reactnative.dev/docs/intro-react-native-components)

## Create Expo App

# Create Expo App

`create-expo-app` is a command line tool that generates a React Native project that works out of the box with Expo. It is the easiest way to get started building a new React Native application.

Visit the following resources to learn more:

- [@official@Create Expo App](https://docs.expo.dev/tutorial/create-your-first-app/)

## Css Basics

# CSS Basics

CSS is a stylesheet language used for describing the look and formatting of a document written in HTML or XML. It is primarily used for styling web pages and user interfaces written in HTML and XHTML. React native uses CSS to style its components. You can learn some CSS basics to get started with React Native and learn more as you go.

Visit the following resources to learn more:

- [@official@CSS - W3.org](https://www.w3.org/Style/CSS/Overview.en.html)
- [@official@CSS - MDN](https://developer.mozilla.org/en-US/docs/Web/CSS)
- [@feed@Explore top posts about CSS](https://app.daily.dev/tags/css?ref=roadmapsh)

## Deeplinking

# Deep Linking

Deep linking in React Native allows your app to open and navigate to a specific screen or content when a user clicks on a URL or a custom URI scheme. It essentially creates a direct pathway into a particular section of your application, bypassing the typical app launch sequence and providing a more seamless user experience. This is useful for scenarios like opening a product page from a marketing email or directing users to a specific profile from a shared link.

Visit the following resources to learn more:

- [@article@Understanding deep linking in React Native](https://blog.logrocket.com/understanding-deep-linking-in-react-native/)
- [@article@Deep Linking in React Native: Navigating to Specific App Screens](https://clouddevs.com/react-native/deep-linking/)
- [@article@A Complete Guide to Deep Linking with Custom domain in React Native](https://dev.to/amitkumar13/a-complete-guide-to-deep-linking-with-custom-domain-in-react-native-bj3)

## Detox

# Detox

Detox is an end-to-end testing framework for React Native applications. It enables you to run tests on an actual device or in a simulator/emulator environment. The goal of Detox is to maintain a high level of confidence in your application's behavior while allowing for quick test runs and easy debugging.

Visit the following resources to learn more:

- [@official@Detox Documentation](https://wix.github.io/Detox/)

## Development Workflow

# Development Workflow

React native has a decent guide on how to get started with development workflow.

Visit the following resources to learn more:

- [@official@Running on Device](https://reactnative.dev/docs/running-on-device)
- [@article@Continuous Integration and Deployment for React Native Apps](https://dev.to/medaimane/continuous-integration-and-deployment-for-react-native-apps-streamlining-development-workflow-4i04)

## Devtools

# DevTools

React Native DevTools are essential tools that help developers debug and optimize their applications during the development process.

Visit the following resources to learn more:

- [@official@Devtools](https://reactnative.dev/docs/react-devtools)

## Enabling Fast Refresh

# Enabling Fast Refresh

Fast Refresh is a React Native feature that allows you to get near-instant feedback while making changes in your code. It achieves this by reloading only the portion of the app that was changed, without losing the current state. This makes the development process a lot smoother as you don't have to wait for the entire app to rebuild after making a change.

Visit the following resources to learn more:

- [@official@Fast Refresh](https://reactnative.dev/docs/fast-refresh)

## Environment Setup

# Environment Setup

In React Native, setting up the development environment is a crucial step. The environment setup process includes installing and configuring various tools and packages required for developing, building, and launching a React Native application. There are two main approaches when setting up your React Native development environment:

Expo CLI
--------

Expo CLI is a command-line tool built for creating and managing React Native projects easily. It streamlines your development process by providing an entire development environment, including building and deploying your app to both iOS and Android platforms.

React Native CLI
----------------

React Native CLI is the official command-line interface for building native mobile apps using React Native. This method requires you to manually set up the native development environment and tools needed for iOS and Android app development.

Visit the following resources to learn more:

- [@official@React Native CLI](https://reactnative.dev/docs/environment-setup?guide=native)
- [@official@Expo CLI Quickstart](https://docs.expo.dev/get-started/create-a-project)

## Expo File System

# Expo File System

Expo File System is a universal module that provides access to the file system on the device. Using this module, you can perform various file operations like reading, writing, copying, moving, and deleting files and folders. It also supports reading file metadata and querying file URI.

Visit the following resources to learn more:

- [@official@Expo File System](https://docs.expo.dev/versions/latest/sdk/filesystem/)

## Expo Secure Store

# expo-secure-store

Expo Secure Store is a built-in package provided by the Expo SDK to store encrypted data securely on users' devices. It is a key-value storage system, but it is not designed to store larger amounts of data such as app databases or complex data structures. It is most appropriate for storing secret keys, access tokens, and small user preferences.

Visit the following resources to learn more:

- [@official@secure-store](https://docs.expo.dev/versions/latest/sdk/securestore/)
- [@opensource@expo-secure-store package](https://www.npmjs.com/package/expo-secure-store?activeTab=readme)

## Expo Snack

# Expo Snack

Expo Snack is an online playground and development environment for creating and testing React Native projects. With Snack, you can easily edit and preview your code changes directly in your browser or on a mobile device using the Expo Go app. It offers a fast, easy, and convenient way to develop, test, and share your projects without needing to set up a local development environment.

Visit the following resources to learn more:

- [@official@Expo Snack](https://snack.expo.dev/)

## Expo Sqlite

# expo-sqlite

Expo SQLite is a powerful tool for handling local SQLite databases in your React Native application. By using this API, you can create, read, update, and delete data as needed, without writing native code. Expo SQLite is available as part of the expo-sqlite package, which provides an easy-to-use interface for SQLite functionalities.

With Expo SQLite, you can efficiently manage SQLite databases within your React Native applications. It enables you to perform various database operations without the need for writing native code.

Visit the following resources to learn more:

- [@official@expo-sqlite](https://docs.expo.dev/versions/latest/sdk/sqlite/)

## Expo Tradeoffs

# Expo Tradeoffs

Expo is a powerful tool that simplifies the React Native development process, but it has some tradeoffs to consider. One limitation is the availability of native modules; while Expo provides a set of pre-built modules, it may not cover all functionalities needed for specific apps, requiring developers to eject from the managed workflow for custom solutions. Performance can also be an issue, as the additional layer Expo adds may lead to slower apps, especially for larger projects, whereas the bare workflow offers more control and potentially better performance. Additionally, Expo apps tend to have a larger size due to the inclusion of the entire Expo SDK, which can be inefficient compared to non-Expo apps that only include necessary modules. Developers relying on Expo must also wait for their release cycle for updates, which can delay access to new React Native features or bug fixes. Ejecting from Expo can present challenges, as it may require significant code adjustments and dependency migrations. Lastly, Expo's abstraction limits customizability, meaning that for advanced customizations, developers may need to switch to a bare workflow. Overall, while Expo provides great tooling and simplifies development, its limitations should be carefully weighed before choosing it for app development.

Visit the following resources to learn more:

- [@article@Should you use Expo or Bare React Native?](https://medium.com/@andrew.chester/should-you-use-expo-or-bare-react-native-8dd400f4a468/)

## Expo

# Expo

Expo is an open-source framework and platform built around React Native, designed to streamline the development process for cross-platform mobile applications. It provides a managed workflow that includes a comprehensive set of tools, APIs, and services for building, testing, and deploying apps for iOS, Android, and web—all using JavaScript or TypeScript.

Expo simplifies mobile development by handling much of the native configuration behind the scenes. Developers can use the **Expo Go** app to preview and test their projects instantly on real devices, while the **Expo CLI** offers powerful commands for creating, running, and managing apps. The **Expo SDK** provides prebuilt modules for features like camera access, push notifications, geolocation, and more, allowing you to focus on app logic rather than native integrations. For production workflows, **EAS (Expo Application Services)** supports custom builds, over-the-air updates, and app store submissions.

Visit the following resources to learn more:

- [@official@Expo Documentation](https://docs.expo.dev/)

## Fetch

# Fetch

_Fetch_ is a JavaScript function available in React Native that is used to make network requests, similar to XMLHttpRequest in web applications. It allows you to handle requests and retrieve data from APIs or other sources. The Fetch API is built on Promises, making it simple to handle success and error cases.

Visit the following resources to learn more:

- [@article@Managing network connection status in React Native](https://blog.logrocket.com/managing-network-connection-status-in-react-native/)

## File Extensions

# File Extensions

In React Native, you can write platform-specific code by using specific file extensions, such as appending `.android.` or `.ios.` to your file names, allowing React Native to automatically load the appropriate file based on the platform. This approach is useful in two main scenarios: creating separate files for platform-specific components, like `Header.ios.js` and `Header.android.js`, which can have different implementations and styles for iOS and Android, and using the `Platform` module within a single file to conditionally render platform-specific code. By leveraging these techniques, developers can create tailored components and features for each platform while keeping their codebase organized and maintainable.

Visit the following resources to learn more:

- [@official@Platform-Specific Code](https://reactnative.dev/docs/platform-specific-code)
- [@official@App Extensions](https://reactnative.dev/docs/app-extensions)

## Flatlist

# FlatList

`FlatList` is a `React Native` core component that displays a scrolling list of changing, but similarly structured, data. It is an efficient list component that makes use of a limited scrolling `renderWindow`, reducing the memory footprint and creating smooth scrolling. Additionally, `FlatList` supports-Headers, Footers, Pull-to-refresh, and Horizontal scrolling, among other things.

Visit the following resources to learn more:

- [@official@FlatList](https://reactnative.dev/docs/flatlist)

## For Android

# For Android

Native modules in React Native provide a powerful way to access device-specific features and capabilities that are not available through the standard React Native APIs. For example, a Bluetooth module can be created using the Android Bluetooth API, allowing applications to scan for nearby Bluetooth devices, connect to them, and transfer data.

Visit the following resources to learn more:

- [@official@Android Native Modules](https://reactnative.dev/docs/legacy/native-modules-android)
- [@feed@Explore top posts about Android](https://app.daily.dev/tags/android?ref=roadmapsh)

## For Ios

# For iOS

iOS native modules in React Native allow developers to tap into the rich ecosystem of iOS features and functionalities that are not directly accessible through the standard React Native APIs. For instance, a Camera module can be implemented using the AVFoundation framework, enabling developers to capture photos and videos directly from their applications.

Visit the following resources to learn more:

- [@official@iOS Native Modules](https://reactnative.dev/docs/legacy/native-modules-ios)
- [@feed@Explore top posts about iOS](https://app.daily.dev/tags/ios?ref=roadmapsh)

## Gesture Handling

# Gesture Responder System

Gesture handling is an essential and powerful feature in React Native that helps create interactive and responsive user interfaces. React Native provides several built-in components and libraries to recognize and respond to different types of user gestures. Some of the common gestures include tapping, swiping, dragging, and pinching.

Visit the following resources to learn more:

- [@official@Animations](https://reactnative.dev/docs/animations)
- [@official@LayoutAnimations](https://reactnative.dev/docs/layoutanimation)
- [@official@Animated](https://reactnative.dev/docs/animated)

## Google Play Store

# Publishing React Native Apps on Google Store

Publishing your React Native app on Google Store consists of several steps.

Visit the following resources to learn more:

- [@official@Publishing to Google Play Store](https://reactnative.dev/docs/signed-apk-android)
- [@feed@Explore top posts about Google](https://app.daily.dev/tags/google?ref=roadmapsh)

## Image

# Image

The `Image` component is used to display images in a React Native application. It allows you to load and display local as well as remote images, providing essential props and methods for better image handling and customization.

Visit the following resources to learn more:

- [@official@Image](https://reactnative.dev/docs/image)

## Imagebackground

# ImageBackground

`ImageBackground` is a React Native core component that allows you to display an image as a background while still being able to place content inside the component. This helps in creating beautiful layouts with images and text or other content on top.

Visit the following resources to learn more:

- [@official@Image Background](https://reactnative.dev/docs/imagebackground)

## In App Developer Menu

# In-App Developer Menu

React Native provides an in-app developer menu which offers several debugging options. You can access the Dev Menu by shaking your device or via keyboard shortcuts:

*   Android: `Cmd + M` or `Ctrl + M`
*   iOS: `Cmd + D` or `Ctrl + D`

Visit the following resources to learn more:

- [@official@Debugging](https://reactnative.dev/docs/debugging)

## Interactions

# Interactions

Interaction in React Native means dealing with how the user can interact with your application. This typically involves handling touch events, gestures, and animations to provide a more engaging and dynamic user experience. There are several built-in components and libraries available in React Native to help you build interactive elements in your app.

Visit the following resources to learn more:

- [@official@Animations](https://reactnative.dev/docs/animations)
- [@official@LayoutAnimations](https://reactnative.dev/docs/layoutanimation)

## Introduction

# Introduction

React Native is an open-source framework developed by Facebook that allows developers to build mobile applications using JavaScript (or TypeScript) and React. It enables building apps for both iOS and Android platforms by offering a shared codebase, which significantly reduces development time and effort.

Visit the following resources to learn more:

- [@official@React Native](https://reactnative.dev/)
- [@official@Getting Started with React Native](https://reactnative.dev/docs/getting-started)
- [@video@React Native Course for Beginners in 2025 | Build a Full Stack React Native App](https://www.youtube.com/watch?v=f8Z9JyB2EIE)

## Javascript Basics

# JavaScript Basics

JavaScript is a very flexible and versatile programming language, considered as a core technology for web development. This is because it is the only language natively supported by all browsers, allowing developers to add dynamic behavior and create complex user experiences with this language.

There's a lot more to learn in JavaScript but my recommendation is to learn the basics and then learn as you go. You'll learn a lot more by building things than by reading about them.

Visit the following resources to learn more:

- [@roadmap@Visit Dedicated JavaScript Roadmap](https://roadmap.sh/javascript)
- [@feed@Explore top posts about JavaScript](https://app.daily.dev/tags/javascript?ref=roadmapsh)

## Jest

# Jest

Jest is a delightful JavaScript Testing Framework with a focus on simplicity. It works with projects using: Babel, TypeScript, Node, React, Angular, Vue and more!

Visit the following resources to learn more:

- [@official@Jest](https://jestjs.io/)
- [@official@Jest Documentation](https://jestjs.io/docs/getting-started)
- [@video@Jest Crash Course - Unit Testing in JavaScript](https://www.youtube.com/watch?v=7r4xVDI2vho)
- [@feed@Explore top posts about Jest](https://app.daily.dev/tags/jest?ref=roadmapsh)

## Jsx

# JSX

JSX is a syntax extension for JavaScript that allows you to write HTML-like code within your JavaScript code. It was developed to be used with React and has become an integral part of working with React.

Visit the following resources to learn more:

- [@official@Components](https://react.dev/learn/your-first-component)
- [@official@Writing Markup with JSX](https://react.dev/learn/writing-markup-with-jsx)
- [@official@JavaScript in JSX with Curly Braces](https://react.dev/learn/javascript-in-jsx-with-curly-braces)
- [@feed@Explore top posts about JSX](https://app.daily.dev/tags/jsx?ref=roadmapsh)

## Keyboardavoidingview

# KeyboardAvoidingView

`KeyboardAvoidingView` is a built-in React Native component that automatically adjusts its children components' position when the keyboard opens, preventing them from being obscured by the on-screen keyboard. It's a useful component, particularly for forms and input fields where the user needs to see the text they're typing.

Visit the following resources to learn more:

- [@official@KeyboardAvoidingView](https://reactnative.dev/docs/keyboardavoidingview)

## Layouts  Flexbox

# Layouts in React Native

In React Native, layouts are primarily managed using the Flexbox styling system. Flexbox is a powerful and flexible layout system that allows you to create responsive and complex UIs using a set of simple rules.

You can use these styles in various combinations to create flexible layouts in React Native. Flexbox makes it easy to create responsive UIs that adapt to changes in screen size or orientation. Note that some of these styles might not work as expected in React Native compared to in CSS for the web, but the overall concepts remain the same.

Visit the following resources to learn more:

- [@official@Flexbox](https://reactnative.dev/docs/flexbox)
- [@official@Layout Props](https://reactnative.dev/docs/layout-props)

## Learn The Pre Requisites

# Learn the Pre-requisites

Before you start learning React Native, you should have a basic knowledge of JavaScript and React. You don't need to fully master these topics, but you should be familiar with them. Learn the basics of JavaScript (e.g. topics marked for beginners in JavaScript Roadmap and continue with React Native.

Visit the following resources to learn more:

- [@roadmap@Visit Dedicated JavaScript Roadmap](https://roadmap.sh/javascript)
- [@roadmap@Visit Dedicated React Roadmap](https://roadmap.sh/react)
- [@official@React Native Basics](https://reactnative.dev/docs/getting-started)

## Listings

# Listings

## Listviews

# ListViews

## Logbox

# LogBox

LogBox is a new feature added to React Native to improve how logs are displayed and managed in your development environment. It provides better visualization and organization of logs, warnings, and errors, making it easier for developers to address issues in their code.

Visit the following resources to learn more:

- [@official@Debugging LogBox](https://reactnative.dev/docs/debugging#logbox)

## Metro Bundler

# Metro Bundler

Metro Bundler is the default bundler for React Native applications. It's a JavaScript module bundler that takes all your application code and dependencies, and bundles them together into a single JavaScript file or multiple files (based on platform).

Visit the following resources to learn more:

- [@official@Metro Bundler](https://facebook.github.io/metro/)

## Modal

# Modal

A `Modal` is a component that displays content on top of the current view, creating an overlay that can be used for various purposes, such as displaying additional information, confirmation messages, or a selection menu.

Visit the following resources to learn more:

- [@official@Modal](https://reactnative.dev/docs/modal)

## Networking

# Networking

React Native facilitates network requests and data management from remote sources through various techniques. The primary method is the `fetch` function, a promise-based API that allows developers to make HTTP requests and retrieve resources, typically in JSON format, from a specified URL. For example, a simple fetch request can be made as follows:

    fetch('https://jsonplaceholder.typicode.com/todos/1')
      .then((response) => response.json())
      .then((json) => console.log(json))
      .catch((error) => console.error(error));
    

Another popular option is Axios, a widely-used library that simplifies HTTP requests in JavaScript applications. Like fetch, Axios is promise-based and offers a user-friendly API, making it a preferred choice for many developers when handling network requests in React Native.

Visit the following resources to learn more:

- [@official@Networking](https://reactnative.dev/docs/network)
- [@official@Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API)
- [@official@Axios](https://axios-http.com/docs/intro)
- [@article@Managing network connection status in React Native](https://blog.logrocket.com/managing-network-connection-status-in-react-native/)

## Networking

# Networking

Networking in React Native primarily uses the Fetch API and XMLHttpRequest for making network requests. These APIs allow you to retrieve data from remote servers and handle asynchronous operations easily. React Native offers various ways to handle networking tasks like making API calls, sending/receiving data from remote servers, and handling different network protocols.

*   Fetch
*   HTTP Call Libraries
*   Web Sockets

These are the major ways to handle networking tasks in React Native. Choose the method that best suits your specific use case and allows you to take full advantage of the features offered.

Visit the following resources to learn more:

- [@official@Networking](https://reactnative.dev/docs/network)
- [@article@Efficient Network Communication](https://medium.com/@Blochware/efficient-network-communication-best-practices-for-handling-api-calls-in-react-native-b5bebbc8ba71)

## Optimizing Flatlist Config

# Optimizing FlatList Config

In React Native, the FlatList component is essential for efficiently displaying large lists of items, and optimizing its configuration is crucial for enhancing performance. Here are key tips for optimizing FlatList:

1.  **Set `windowSize`**: Adjust the `windowSize` prop, which determines the number of pages rendered above and below the current view. Reducing this value from the default of 21 can decrease off-screen component rendering.
    
2.  **Enable `removeClippedSubviews`**: This prop unmounts components that are off-screen, helping to free up resources.
    
3.  **Adjust `maxToRenderPerBatch`**: Control the number of items rendered per batch with this prop, which defaults to 10. Tailor this value to fit your list's needs.
    
4.  **Set `initialNumToRender`**: This prop defines how many items to render initially, helping to prevent blank screens during loading.
    
5.  **Use `getItemLayout`**: By specifying the exact dimensions of each item with this prop, you can avoid dynamic measurements, leading to better performance.

Visit the following resources to learn more:

- [@official@Optimizing Flatlist Configuration](https://reactnative.dev/docs/optimizing-flatlist-configuration)

## Other Storage Options

# Other Storage Options

Besides AsyncStorage, there are other options available for handling data storage in React Native applications. This guide will briefly cover some popular options: Realm, Firebase Realtime Database, and SQLite.

These are just a few examples of additional storage options for React Native. Depending on your requirements, you may choose the one that best fits your project.

Visit the following resources to learn more:

- [@official@Async Storage](https://reactnative.dev/docs/asyncstorage)
- [@opensource@Realm - GitHub](https://github.com/realm/realm-js)
- [@article@Firebase Realtime Database](https://firebase.google.com/docs/database)
- [@feed@Explore top posts about Storage](https://app.daily.dev/tags/storage?ref=roadmapsh)

## Performance

# Performance

Performance is a crucial aspect of any application, and React Native is no exception. Optimizing performance in your React Native apps will not only lead to a better user experience but also lessen the load on device resources.

Visit the following resources to learn more:

- [@official@Performance](https://reactnative.dev/docs/performance)

## Platform Module

# Platform Module

The Platform module, as the name suggests, is a part of React Native that detects the platform on which the app is running. This enables you to have specific code for either Android or iOS, allowing you to account for platform-specific differences in design or behavior.

To utilize the Platform module, you need to import it and then access the `OS` property. This property returns a string, which denotes the platform — either `'ios'` or `'android'`.

With the Platform module, you can easily create platform-specific code, enabling you to have the best user experience for each platform. Just remember to import the module and use the provided properties and methods.

Visit the following resources to learn more:

- [@official@Platform](https://reactnative.dev/docs/platform)
- [@official@Platform-Specific Code](https://reactnative.dev/docs/platform-specific-code)

## Pressable

# Pressable

Pressable is a core component in React Native that makes any view respond properly to touch or press events. It provides a wide range of event handlers for managing user interactions, such as onPress, onPressIn, onPressOut, and onLongPress. With Pressable, you can create custom buttons, cards, or any touchable elements within your app.

Visit the following resources to learn more:

- [@official@Pressable](https://reactnative.dev/docs/pressable)

## Profiling

# Profiling

Use the built-in profiler to get detailed information about work done in the JavaScript thread and main thread side-by-side. Access it by selecting Perf Monitor from the Debug menu.

For iOS, Instruments is an invaluable tool, and on Android you should learn to use `systrace`.

Visit the following resources to learn more:

- [@official@Profiling React Native](https://reactnative.dev/docs/profiling)

## Props

# Props

In React, **props** are short for _properties_ and are used to pass data from a parent component to a child component. They are similar to function arguments, and they help make components reusable and maintainable.

Visit the following resources to learn more:

- [@official@Components](https://react.dev/learn/your-first-component)
- [@official@Props](https://react.dev/learn/passing-props-to-a-component)

## Publishing Apps

# Publishing Apps

Publishing React Native apps is the process of deploying your application on various app stores so that users can download and use your app. The two most popular app stores for publishing are the Apple App Store (iOS) and the Google Play Store (Android).

Visit the following resources to learn more:

- [@official@Publishing to Apple App Store](https://reactnative.dev/docs/publishing-to-app-store)
- [@official@Publishing to Google Play Store](https://reactnative.dev/docs/signed-apk-android)

## Push Notifications

# Push Notifications

Push notifications in React Native allow you to send timely and relevant information to users even when they aren't actively using your app. The original native push notification functionality in React Native has been deprecated. Now, you'll typically rely on third-party services like Firebase Cloud Messaging (FCM), Expo Notifications, or OneSignal to handle the complexities of delivering notifications across different platforms (iOS and Android). These services provide robust APIs and infrastructure for managing device tokens, sending notifications, and tracking delivery success.

Visit the following resources to learn more:

- [@official@PushNotificationIOS](https://reactnative.dev/docs/pushnotificationios)
- [@official@Expo Notifications](https://docs.expo.dev/versions/latest/sdk/notifications/)
- [@article@Expo push notifications setup](https://docs.expo.dev/push-notifications/push-notifications-setup/)
- [@video@Expo Notifications with EAS | Complete Guide](https://www.youtube.com/watch?v=BCCjGtKtBjE)

## Ram Bundles  Inline Requires

# RAM Bundles + Inline Requires

If you have a large app you may want to consider the Random Access Modules (RAM) bundle format, and using inline requires. This is useful for apps that have a large number of screens which may not ever be opened during a typical usage of the app. Generally it is useful to apps that have large amounts of code that are not needed for a while after startup. For instance the app includes complicated profile screens or lesser used features, but most sessions only involve visiting the main screen of the app for updates. We can optimize the loading of the bundle by using the RAM format and requiring those features and screens inline (when they are actually used).

Visit the following resources to learn more:

- [@official@RAM Bundles and Inline Requires](https://reactnative.dev/docs/ram-bundles-inline-requires)

## React Native Alternatives

# React Native Alternatives

React Native is a popular choice for cross-platform application development, but there are other options available. Some of the common alternatives to React Native are Flutter, Ionic and Xamarin. Flutter being the most popular alternative to React Native.

Visit the following resources to learn more:

- [@official@Flutter](https://flutter.dev/)
- [@official@Ionic](https://ionicframework.com/)
- [@official@Xamarin](https://dotnet.microsoft.com/apps/xamarin)
- [@feed@Explore top posts about React](https://app.daily.dev/tags/react?ref=roadmapsh)

## React Native Async Storage

# React Native Async Storage

React Native AsyncStorage is an unencrypted, asynchronous, persistent key-value storage system that allows developers to store data globally within their applications. It is primarily used for persisting data offline, making it suitable for scenarios like saving user preferences or session data.

Visit the following resources to learn more:

- [@official@Async Storage](https://reactnative.dev/docs/asyncstorage)
- [@opensource@Async Storage - GitHub](https://github.com/react-native-async-storage/async-storage)

## React Native Cli

# React Native CLI

React Native CLI is the official command-line interface for building native mobile apps using React Native. This method requires you to manually set up the native development environment and tools needed for iOS and Android app development.

Visit the following resources to learn more:

- [@official@React Native CLI](https://reactnative.dev/docs/environment-setup?guide=native)

## React Native Testing Library

# React Native Testing Library

React Native Testing Library (RNTL) is a collection of tools and utilities to test React Native components. It is built on top of the Testing Library ecosystem, designed to work seamlessly with Jest and other testing frameworks. Its primary goal is to enable efficient and effective testing by providing simple and intuitive APIs that promote best practices, like testing UI components in isolation and promoting accessibility checks.

Visit the following resources to learn more:

- [@article@React Native Testing Library](https://callstack.github.io/react-native-testing-library/)
- [@article@React Native Testing Library (Docs)](https://testing-library.com/docs/react-native-testing-library/intro/)
- [@feed@Explore top posts about React](https://app.daily.dev/tags/react?ref=roadmapsh)

## React Native Web

# React Native Web

React Native Web is an extension of React Native which allows you to run your React Native apps not only on iOS and Android devices, but also on the web. It uses the same components and APIs you're familiar with in React Native, but renders them into the DOM of a webpage instead of native UI elements.

The main goal of React Native Web is to provide a consistent developer experience across platforms, reducing the effort needed to build and maintain multi-platform apps.

Visit the following resources to learn more:

- [@article@react-native-web - npm](https://www.npmjs.com/package/react-native-web)
- [@article@Complete Guide to React Native for Web](https://blog.logrocket.com/complete-guide-react-native-web/)

## React Test Renderer

# React Test Renderer

React Test Renderer is a library provided by the React team that allows you to render React components as JavaScript objects without depending on the DOM or a native mobile environment. It can be used to test components in Node.js environments where the actual rendering is not required.

Visit the following resources to learn more:

- [@official@React Test Renderer](https://jestjs.io/docs/tutorial-react)
- [@feed@Explore top posts about React](https://app.daily.dev/tags/react?ref=roadmapsh)

## Refreshcontrol

# Refresh Control

`RefreshControl` is a component in React Native that is used to provide pull-to-refresh functionality for scrollable components like `ScrollView`, `ListView`, and `FlatList`.

Visit the following resources to learn more:

- [@official@Refresh Control](https://reactnative.dev/docs/refreshcontrol)
- [@official@ScrollView](https://reactnative.dev/docs/ScrollView)
- [@official@FlatList](https://reactnative.dev/docs/FlatList)

## Running On Device

# Running on Device

It's always a good idea to test your app on an actual device before releasing it to your users.

Visit the following resources to learn more:

- [@official@Running on Device](https://reactnative.dev/docs/running-on-device)

## Safeareaview

# SafeAreaView

`SafeAreaView` is a React Native core component that helps to adjust your app's UI elements and layout to accommodate the notches, curved edges, or home indicator on iOS devices. It is particularly useful for the iPhone X and newer iPhone models, as it ensures that content is rendered within the visible portion of the screen.

Keep in mind that `SafeAreaView` only works on iOS devices, and has no effect on Android devices. To handle such cases, you can use platform-specific styles or libraries like `react-native-safe-area-context` which provide more control and customization options for additional platforms.

Visit the following resources to learn more:

- [@official@SafeAreaView](https://reactnative.dev/docs/safeareaview)

## Screen Navigation

# Screen Navigation

In React Native, navigating from one screen to another is a crucial aspect of app development. The most commonly used navigation libraries are React Navigation and React Native Navigation.

Visit the following resources to learn more:

- [@official@React Navigation](https://reactnavigation.org/)

## Scrolling  Swiping

# Scrolling and Swiping

In React Native, scrolling and swiping interactions can be defined and customized with a set of built-in components. These components are efficient and provide fluid navigation through the elements inside them.

Visit the following resources to learn more:

- [@official@Handling Touches](https://reactnative.dev/docs/handling-touches)
- [@official@Using a ScrollView](https://reactnative.dev/docs/using-a-scrollview)
- [@article@React Native Gesture Handler: Swipe, long-press, and more](https://blog.logrocket.com/react-native-gesture-handler-tutorial-examples/)

## Scrollview

# Scroll View

In React Native, the `ScrollView` is a generic scrolling container used to provide a scrollable view to its child components. It is useful when you need to display scrollable content larger than the screen, such as lists, images, or text. A `ScrollView` must have a bounded height in order to properly work.

Visit the following resources to learn more:

- [@official@ScrollView](https://reactnative.dev/docs/ScrollView)

## Sectionlist

# SectionList

`SectionList` is a component used to render sections and headers in a scroll view. It helps to manage and optimize a large list of items divided into categories. It is one of the List View components provided by React Native along with FlatList.

Visit the following resources to learn more:

- [@official@SectionList](https://reactnative.dev/docs/sectionlist)

## Security

# Security

Security is a vital consideration in React Native application development, as it helps protect user data and sensitive information. Key best practices include using secure storage solutions for sensitive data, such as authentication tokens and user credentials, with libraries like `react-native-keychain` and `react-native-encrypted-storage`. For secure communication, always use HTTPS for API interactions to ensure that data exchanged between the client and server is encrypted. Additionally, minimize permissions by requesting only those necessary for the app's functionality, ideally at runtime, using libraries like `react-native-permissions`.

Validating and sanitizing user input is crucial to prevent threats like SQL injection and cross-site scripting (XSS), which can be achieved with validation libraries such as `Yup`. Lastly, keeping dependencies up to date is essential to avoid known security vulnerabilities; tools like `npm audit` and Dependabot can assist in this process. By adhering to these best practices, developers can enhance the security of their React Native applications, safeguarding both application data and user information.

Visit the following resources to learn more:

- [@official@Security](https://reactnative.dev/docs/security)
- [@article@Secure Authentication and Authorization in React Native](https://medium.com/@christopherobocha/secure-authentication-and-authorisation-in-react-native-a260f1787a89)

## Sourcemaps

# Sourcemaps

Sourcemaps are files that map the original source code of a project to its minified or transpiled version. This is especially useful in environments, like React Native, where the code may be transformed before being executed in the device/emulator. Sourcemaps help developers to debug their code more easily by mapping errors in the transformed code back to their original location in the source code.

There are various types of sourcemaps which give different levels of detail to the debugging process:

*   `eval`: Uses `eval` function to generate the sourcemaps. This is faster but provides less detailed information than other options.
*   `cheap-source-map`: Simple line-to-line mapping without column information. Faster than `source-map` but less accurate.
*   `cheap-module-source-map`: Similar to `cheap-source-map` but with support for modules.
*   `source-map`: Full source mapping with both line and column information. It is accurate, though slower compared to other options.

After generating sourcemaps, you can use them to debug errors more efficiently, as they will reference the original locations in the source code. The browser's developer tools, like Google Chrome, have built-in support for sourcemaps, providing the ability to navigate and debug errors with ease.

Visit the following resources to learn more:

- [@official@SourceMaps](https://reactnative.dev/docs/debugging-release-builds#enabling-source-maps)
- [@article@Source Maps (MDN)](https://developer.mozilla.org/en-US/docs/Tools/Debugger/How_to/Use_a_source_map)

## Speeding Up Builds

# Speeding up Builds

Building your React Native app could be expensive and take several minutes of developers time. This can be problematic as your project grows and generally in bigger organizations with multiple React Native developers.

Visit the following resources to learn more:

- [@official@Speeding up your Build phase](https://reactnative.dev/docs/build-speed)

## State

# State

State is an object that holds data managed within a React component. It allows components to become dynamic and interactive by keeping track of its data changes. When the state of a component changes, React re-renders the component and updates the DOM accordingly.

Visit the following resources to learn more:

- [@official@Component State](https://react.dev/learn/managing-state)

## Statusbar

# StatusBar

The `StatusBar` component is used to control the appearance of the status bar on the top of the screen. It may strike as a bit unusual since, unlike other React Native components, it doesn't render any visible content. Instead, it sets some native properties that can help customize the look of status bars on Android, iOS, or other platforms.

Visit the following resources to learn more:

- [@official@StatusBar](https://reactnative.dev/docs/statusbar)

## Storage

# Storage

React Native provides a few ways to persist data locally in the app. Here's a brief summary of the storage options available:

*   Async Storage
*   Expo Secure Store
*   Expo File System
*   Expo SQLite

Choose the storage option that best fits your app's requirements and use cases. Keep in mind that AsyncStorage and SecureStorage are more suited for small-scale data storage, while Realm and SQLite support more complex storage and querying needs.

Visit the following resources to learn more:

- [@official@AsyncStorage](https://reactnative.dev/docs/asyncstorage)
- [@article@Best Data Storage Option for React Native Apps](https://dev.to/ammarahmed/best-data-storage-option-for-react-native-apps-42k)

## Storage

# Storage

React Native offers several methods for persisting data locally within applications, each catering to different storage needs and use cases. The primary options include Async Storage, which provides a simple key-value storage system suitable for small-scale data; Expo Secure Store, designed for securely storing sensitive information; Expo File System, which allows for file management and storage; and Expo SQLite, which supports more complex data storage and querying capabilities. When selecting a storage option, it's essential to consider the specific requirements of your app.

Visit the following resources to learn more:

- [@article@Best Data Storage Option for React Native Apps](https://dev.to/ammarahmed/best-data-storage-option-for-react-native-apps-42k)

## Stylesheets

# Stylesheets in React Native

In React Native, stylesheets are objects that define the appearance of components. They provide a way to separate styling from the component's logic. Stylesheets are created using `StyleSheet.create` method, which ensures a standardized and efficient way to manage styles for your components.

Visit the following resources to learn more:

- [@official@Stylesheets](https://reactnative.dev/docs/stylesheet)

## Styling

# Styling

Styling in React Native is accomplished through JavaScript and uses a subset of CSS properties. Unlike CSS in web development, React Native has its own set of components and styling rules. The main components used for styling are `StyleSheet`, `View`, and `Text`.

`StyleSheet` is a module provided by React Native to manage and optimize styles. It is similar to a CSS stylesheet and helps in creating and working with multiple styles efficiently.

Visit the following resources to learn more:

- [@official@Styling](https://reactnative.dev/docs/style)

## Switch

# Switch

A `Switch` is a core component in React Native used to implement a "toggle" or "on-off" input. It provides a UI for the user to switch between two different states, typically true or false. The primary use case is to enable or disable a feature or setting within an application.

`Switch` component has a boolean `value` prop (true for on, false for off) and an `onValueChange` event handler, which is triggered whenever the user toggles the switch.

Visit the following resources to learn more:

- [@official@Switch](https://reactnative.dev/docs/switch)

## Testing

# Testing

When it comes to testing, you can use a combination of Jest, React Test Renderer, React Native Testing Library, Detox and Appium for all sorts of API needs.

## Text Input

# Text Input

`TextInput` is a core component in React Native that allows the user to enter text. It is commonly used to collect user data, like emails or passwords. You can customize the appearance of `TextInput` by using various props such as `placeholder`, `multiline`, `maxLength`, and more.

Visit the following resources to learn more:

- [@official@Text Input](https://reactnative.dev/docs/textinput)

## Text

# Text Component

The `Text` component is a basic element in React Native used to display text content on the screen. While it has some basic styling properties, you usually nest it inside other components (e.g., `View`) to create more complex UIs.

Visit the following resources to learn more:

- [@official@Text](https://reactnative.dev/docs/text)

## Touchables

# Touchables

In React Native, `Touchable` components are used to handle user interactions like taps, long presses, and double-taps on the appropriate elements. Each of these components is from the `react-native` package, except `TouchableScale` which is from `react-native-touchable-scale`. They can be used interchangeably depending on the type of interaction you want to provide. The main `props` used with these components are `onPress`, `onLongPress`, and some component-specific ones like `underlayColor` for `TouchableHighlight`.

Visit the following resources to learn more:

- [@official@Handling Touches](https://reactnative.dev/docs/handling-touches)
- [@official@TouchableOpacity](https://reactnative.dev/docs/touchableopacity)

## Understand Frame Rates

# Understand Frame Rates

Frame rates represent the number of frames (or images) displayed per second in an animation or video. The performance of a React Native application can be highly impacted by the frame rate, so it is important to optimize your application for the best possible user experience. Higher frame rates provide smoother animations, but may require more system resources. To achieve the desired frame rate, the application should ensure that each frame is computed and rendered within the time budget.

To achieve high frame rates and smooth animations, developers can utilize the `Animated` library, which offers methods and components for efficient animation management. For instance, the library allows for declarative animation definitions, minimizes unnecessary render cycles, and enables the use of the native driver to offload animations from the JavaScript thread. By adhering to best practices and leveraging the `Animated` library, developers can enhance their React Native applications' performance and deliver high-quality animations.

## Using Native Modules

# Using Native Modules

Sometimes a React Native app needs to access a native platform API that is not available by default in JavaScript, for example the native APIs to access Apple or Google Pay. Maybe you want to reuse some existing Objective-C, Swift, Java or C++ libraries without having to reimplement it in JavaScript, or write some high performance, multi-threaded code for things like image processing.

The NativeModule system exposes instances of Java/Objective-C/C++ (native) classes to JavaScript (JS) as JS objects, thereby allowing you to execute arbitrary native code from within JS. While we don't expect this feature to be part of the usual development process, it is essential that it exists. If React Native doesn't export a native API that your JS app needs you should be able to export it yourself!

Visit the following resources to learn more:

- [@official@Native Modules Introduction](https://reactnative.dev/docs/native-platform)

## View

# View

## Websockets

# Websockets

WebSockets are a protocol that allows full-duplex communication between a client and a server over a single, long-lived connection. They are useful when real-time communication is needed, such as in chat applications, online gaming, or financial trading platforms.

Visit the following resources to learn more:

- [@article@The WebSocket API (WebSockets) - Web APIs](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API)

## What Is React Native

# React Native

React Native is a popular open-source framework developed by Facebook for building mobile applications using JavaScript (or TypeScript) and React. It enables developers to build native mobile apps for iOS and Android platforms using a single codebase, which significantly speeds up development without compromising on the performance and usability of the apps.

With React Native, you write components with JSX, a syntax that combines JavaScript and XML. These components can map to native UI elements like views, text, images, and more.

Visit the following resources to learn more:

- [@official@Getting Started with React Native](https://reactnative.dev/docs/getting-started)

## Why Use React Native

# Why React Native?

React Native is a popular framework for developing native mobile applications using JavaScript (or TypeScript) and React, offering several compelling advantages for mobile app development. Key benefits include **code reusability**, allowing developers to share a significant portion of the codebase between iOS and Android, which reduces development time and simplifies maintenance. It leverages **familiar React concepts**, making it accessible for those already experienced with ReactJS, as it applies similar principles of components and state management. React Native provides **near-native performance** by directly interacting with native components, avoiding intermediaries like WebView. The framework benefits from a **vast ecosystem** and community support, with numerous libraries and tools that enhance the development process, bolstered by contributions from major companies like Facebook. Additionally, **hot reloading** enables developers to see code changes in real-time on devices or emulators, streamlining the development workflow. Finally, React Native can be **integrated into existing applications**, allowing for flexible enhancements to specific parts of an app.

Visit the following resources to learn more:

- [@article@Why You Should Choose React Native?](https://www.geeksforgeeks.org/why-you-should-choose-react-native/)
- [@article@React Native: What is it? and, Why is it used?](https://medium.com/@thinkwik/react-native-what-is-it-and-why-is-it-used-b132c3581df)

## Writing Platform Specific Code

# Platform Specific Code

In React Native, managing platform-specific code for iOS and Android is essential for addressing differences in application behavior and appearance. This can be achieved in two primary ways: using the `Platform` module, which allows developers to detect the current platform and apply conditional styles or logic accordingly, as demonstrated by using `Platform.select` to set different background colors for iOS and Android; and utilizing file extensions like `.ios.js` and `.android.js`, which enables React Native to automatically load the appropriate file based on the platform. For instance, if you have `Header.ios.js` and `Header.android.js`, importing the `Header` component will automatically reference the correct file for the running platform, streamlining the development process.

Visit the following resources to learn more:

- [@official@Platform-Specific Code](https://reactnative.dev/docs/platform-specific-code)
- [@official@App Extensions](https://reactnative.dev/docs/app-extensions)
