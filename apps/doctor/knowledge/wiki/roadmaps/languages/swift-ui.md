# Swift Ui Roadmap

---
renderer: editor
---

---

## Access Control

# Access Control

Access control lets you restrict which parts of your code can be used and accessed by other parts of your code, or from code in other files and modules. It's like setting permissions on different components of your app, ensuring that sensitive data and internal workings are protected from unintended use or modification. You can specify different access levels, such as `private`, `fileprivate`, `internal`, `public`, and `open`, to control the visibility and accessibility of entities like classes, structures, properties, and functions.

Visit the following resources to learn more:

- [@official@Access Control](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/accesscontrol)
- [@article@Swift Access Control](https://www.programiz.com/swift-programming/access-control)
- [@article@Swift Access Control: A Developer’s Guide to open, public, internal, fileprivate and private](https://mehrdad-ahmadian.medium.com/swift-access-control-a-developers-guide-to-open-public-internal-fileprivate-and-private-79d2dd595287)
- [@video@Introduction to Swift: Access control](https://www.youtube.com/watch?v=SVXtWw63C8k)

## Accessibility

# Accessibility

Accessibility focuses on making your app usable by everyone, including people with disabilities. This involves providing alternative ways to interact with your app's content and controls, such as using screen readers, switch controls, or larger fonts. By implementing accessibility features, you ensure that your app is inclusive and provides a positive experience for all users, regardless of their abilities.

Visit the following resources to learn more:

- [@official@Accessibility modifiers](https://developer.apple.com/documentation/swiftui/view-accessibility)
- [@article@Accessibility: Introduction](https://www.hackingwithswift.com/books/ios-swiftui/accessibility-introduction)
- [@article@Mastering SwiftUI Accessibility: A Comprehensive Guide](https://medium.com/@GetInRhythm/mastering-swiftui-accessibility-a-comprehensive-guide-919358e9c01a)
- [@video@Catch up on accessibility in SwiftUI](https://developer.apple.com/videos/play/wwdc2024/10073/)

## Actors

# Actors

Actors are a concurrency model that provides a way to isolate state and prevent data races in concurrent Swift programs. They encapsulate mutable state and allow access to that state only through asynchronous message passing. This ensures that only one task can access the actor's state at any given time, eliminating the need for locks or other complex synchronization mechanisms. Actors are particularly useful in Swift and SwiftUI for managing shared data across different parts of your application, especially when dealing with asynchronous operations.

Visit the following resources to learn more:

- [@official@Actors](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/concurrency/#Actors)
- [@article@What is an actor and why does Swift have them?](https://www.hackingwithswift.com/quick-start/concurrency/what-is-an-actor-and-why-does-swift-have-them)
- [@video@How to use Actors and non-isolated in Swift | Swift Concurrency #9](https://www.youtube.com/watch?v=UUdi137FySk)

## Alamofire

# Alamofire

Alamofire is a Swift-based HTTP networking library that simplifies the process of making network requests in your iOS, macOS, tvOS, and watchOS applications. It provides an elegant interface built on top of Apple's `URLSession` to handle common networking tasks like making GET, POST, PUT, and DELETE requests, handling response data, and managing request parameters. Alamofire abstracts away much of the complexity involved in working directly with `URLSession`, making network code cleaner and easier to read.

Visit the following resources to learn more:

- [@opensource@Alamofire](https://github.com/Alamofire/Alamofire)
- [@article@Alamofire Tutorial with Swift (Quickstart)](https://codewithchris.com/alamofire/)

## Animatable Protocol

# Animatable Protocol

The `Animatable` protocol allows you to customize how changes to your custom data types are animated in SwiftUI. By conforming to this protocol, you define a `var animatableData: Self.AnimatableData` property that SwiftUI uses to interpolate between the starting and ending values of your data during an animation. This enables smooth transitions for properties that aren't directly animatable by default, giving you fine-grained control over animation behavior.

Visit the following resources to learn more:

- [@official@Animatable](https://developer.apple.com/documentation/SwiftUI/Animatable)
- [@article@How to create animatable views, modifiers, and more](https://www.hackingwithswift.com/quick-start/swiftui/how-to-create-animatable-views-modifiers-and-more)
- [@article@The magic of Animatable values in SwiftUI](https://swiftwithmajid.com/2020/06/17/the-magic-of-animatable-values-in-swiftui/)
- [@video@Animate Custom shapes with AnimateableData in SwiftUI | Advanced Learning #7](https://www.youtube.com/watch?v=kzrtiPbR3LQ)

## Animations

# Animations

Animations allow you to visually enhance your app's user interface by creating smooth transitions and dynamic effects. They involve changing properties of views over time, making your app feel more responsive and engaging. You can animate things like size, position, opacity, and color, adding a layer of polish and feedback to user interactions.

Visit the following resources to learn more:

- [@official@Animations](https://developer.apple.com/documentation/swiftui/animations)
- [@official@Animating views and transitions](https://developer.apple.com/tutorials/swiftui/animating-views-and-transitions)
- [@video@WWDC23: Explore SwiftUI animation | Apple](https://www.youtube.com/watch?v=IuSuHJs5-KE)
- [@video@Customizing animations in SwiftUI – Animation SwiftUI Tutorial 2/8](https://www.youtube.com/watch?v=8TG_dMF0s7g)

## App Architecture

# App Architecture

App architecture is the structural design of an application, defining its components, their relationships, and how they interact to achieve the app's functionality. It provides a blueprint for organizing code, managing data, and handling user interactions, ensuring the app is maintainable, scalable, and testable. A well-defined architecture helps developers understand the codebase, collaborate effectively, and adapt to changing requirements.

Visit the following resources to learn more:

- [@official@Exploring the structure of a SwiftUI app](https://developer.apple.com/tutorials/swiftui-concepts/exploring-the-structure-of-a-swiftui-app)
- [@article@xChoosing a Design Pattern for your SwiftUI App](https://medium.com/@alexanderson_16451/choosing-a-design-pattern-for-your-swiftui-app-163c06ffcd9b)

## App Lifecycle

# App Lifecycle

The app lifecycle manages the state and behavior of your application from launch to termination. It's primarily handled through the `@main` attribute, which designates the entry point of your app. The `App` protocol defines the structure of your application, including the initial scene that's displayed to the user. SwiftUI automatically manages the creation and destruction of your app's scenes, responding to system events like activation, deactivation, and backgrounding, allowing you to react to these state changes and manage resources accordingly.

Visit the following resources to learn more:

- [@article@The Simple Life(cycle) of a SwiftUI View in 2025](https://captainswiftui.substack.com/p/the-simple-lifecycle-of-a-swiftui)
- [@video@SwiftUI View Lifecycle](https://www.youtube.com/watch?v=5pqc7y43auQ)

## Arc

# Automatic Reference Counting (ARC)

Automatic Reference Counting (ARC) is a memory management feature in Swift that automatically frees up memory used by class instances when they are no longer needed. It works by tracking how many references exist to each object. When the reference count drops to zero, meaning no other parts of the code are using that object, ARC deallocates the memory, preventing memory leaks. This process is automatic, reducing the need for manual memory management like in some other languages.

Visit the following resources to learn more:

- [@official@Automatic Reference Counting](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/automaticreferencecounting/)
- [@article@A detailed explanation of how ARC works in Swift](https://medium.com/@ahmed044/a-detailed-explanation-of-how-arc-works-in-swift-8076fc79e03b)
- [@article@Understanding Swift ARC: The Complete Guide to Memory Management](https://www.dhiwise.com/post/understanding-swift-arc-complete-guide-to-memory-management)
- [@video@WWDC21: ARC in Swift: Basics and beyond | Apple](https://www.youtube.com/watch?v=GFq6sV2jD_c)

## Arithmetic

# Arithmetic Operators in Swift

Arithmetic operators are special symbols that perform mathematical calculations on values. Swift provides standard arithmetic operators like addition (+), subtraction (-), multiplication (*), and division (/). It also includes the remainder operator (%), which calculates the remainder after division. These operators are fundamental for performing calculations and manipulating numerical data within your Swift code.

Visit the following resources to learn more:

- [@official@Arithmetic Operators](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/basicoperators/#Arithmetic-Operators)

## Asynchronous Functions

# Asynchronous Functions

Asynchronous functions allow your program to start a potentially long-running task and then continue executing other code without waiting for that task to complete. When the asynchronous task finishes, it can notify your program, which can then process the results. This approach prevents your app from freezing or becoming unresponsive while waiting for operations like network requests or file processing to finish.

Visit the following resources to learn more:

- [@official@Concurrency](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/concurrency/)
- [@article@Asynchronous Functions](https://www.hackingwithswift.com/quick-start/concurrency/what-is-an-asynchronous-function)

## Asynchronous Sequences

# Asynchronous Sequences

Asynchronous sequences allow you to iterate over a series of values that arrive over time, potentially from different threads or even across a network. Unlike regular sequences, where all elements are immediately available, asynchronous sequences produce elements as they become available, enabling you to handle data streams, network responses, or any other data source that emits values asynchronously. This is particularly useful for managing concurrent operations and building responsive user interfaces.

Visit the following resources to learn more:

- [@official@Asynchronous Sequences](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/concurrency/#Asynchronous-Sequences)
- [@official@AsyncSequence](https://developer.apple.com/documentation/swift/asyncsequence)
- [@article@AsyncSequence explained with Code Examples](https://www.avanderlee.com/concurrency/asyncsequence/)
- [@video@Meet AsyncSequence](https://developer.apple.com/videos/play/wwdc2021/10058/)

## Background

# Background View Modifier

The `background` view modifier in SwiftUI allows you to set a background for a view. This background can be a color, a shape, or even another view. It's applied behind the content of the view it modifies, effectively layering content on top of the background you specify. You can customize the appearance of the background, such as its color, shape, and how it fills the available space.

Visit the following resources to learn more:

- [@official@Background](https://developer.apple.com/documentation/swiftui/view/background(alignment:content:))
- [@official@Adding a background to your view](https://developer.apple.com/documentation/swiftui/adding-a-background-to-your-view)

## Basic Functions

# Basic Functions

Functions are self-contained blocks of code that perform a specific task. You define a function with a name, a set of inputs (parameters), and a return type. When you call a function, you execute the code within its block, potentially passing in values for the parameters, and the function may return a value as a result. They help organize code, make it reusable, and improve readability.

Visit the following resources to learn more:

- [@official@Functions](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/functions/#Defining-and-Calling-Functions)
- [@article@Swift Functions](https://www.programiz.com/swift-programming/functions)
- [@video@How to use Functions in Swift | Swift Basics #5](https://www.youtube.com/watch?v=kr3SSplrJlw)

## Binding

# @Binding

`@Binding` creates a two-way connection between a view and a source of truth that lives elsewhere. It essentially provides a way for a view to read and modify a value that's owned and managed by another view or data structure. When the view modifies the bound value, the original source of truth is automatically updated, and vice versa, ensuring data consistency across your application.

Visit the following resources to learn more:

- [@official@Binding](https://developer.apple.com/documentation/swiftui/binding)
- [@article@What is the @Binding property wrapper?](https://www.hackingwithswift.com/quick-start/swiftui/what-is-the-binding-property-wrapper)
- [@video@SwiftUI - @Binding Property Wrapper Explained - Passing Data](https://www.youtube.com/watch?v=lgtB3WLEOYg)

## Booleans

# Booleans

Booleans represent truth values, either `true` or `false`. They are fundamental for controlling program flow, making decisions based on conditions, and representing binary states. In Swift, you declare a Boolean variable using the `Bool` keyword and assign it either `true` or `false`.

Visit the following resources to learn more:

- [@official@Booleans](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/thebasics/#Booleans)
- [@article@Data Types in Swift](https://medium.com/@andyandmishel15/data-types-in-swift-b6d0e6cc65fa)
- [@video@Swift Tutorial for Beginners: Lesson 2 Data Types](https://www.youtube.com/watch?v=zcLMOTEDd8Y)

## Button

# Button

A Button is a fundamental UI element that triggers an action when tapped or clicked. It's essentially a tappable area on the screen that, when interacted with, executes a predefined piece of code. Buttons are used to initiate actions like submitting forms, navigating to different screens, or performing specific tasks within an application.

Visit the following resources to learn more:

- [@official@Button](https://developer.apple.com/documentation/SwiftUI/Button)
- [@official@Populating SwiftUI menus with adaptive controls](https://developer.apple.com/documentation/swiftui/populating-swiftui-menus-with-adaptive-controls)
- [@article@SwiftUI Button: A Complete Tutorial](https://www.rootstrap.com/blog/swiftui-button-a-complete-tutorial)
- [@article@How to create a tappable button](https://www.hackingwithswift.com/quick-start/swiftui/how-to-create-a-tappable-button)
- [@video@SwiftUI Button Basics](https://www.youtube.com/watch?v=Gdu6WgIu37A)

## Catching

# Catching Errors in Swift

Handling errors involves catching potential problems that may occur during code execution. When a function or method can throw an error, you use a `do-catch` block to try executing the code that might fail. If an error is thrown within the `do` block, control is transferred to the `catch` block, allowing you to respond to the error gracefully and prevent your app from crashing, thereby providing a better user experience.

Visit the following resources to learn more:

- [@official@Handling Errors Using Do-Catch](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/errorhandling/#Handling-Errors-Using-Do-Catch)
- [@article@Error handling in Swift with do catch](https://www.donnywals.com/error-handling-in-swift-with-do-catch/)

## Clean Architecture

# Clean Architecture

Clean Architecture is a software design philosophy that emphasizes separation of concerns, making applications more maintainable, testable, and scalable. It achieves this by dividing the application into distinct layers, each with its own specific responsibility and dependencies. The core idea is to keep the business logic independent from the user interface, database, and external frameworks, allowing changes in one area without affecting others.

Visit the following resources to learn more:

- [@article@A Beginner’s Guide to Clean Architecture in SwiftUI: Building Better Apps Step by Step](https://medium.com/@walfandi/a-beginners-guide-to-clean-architecture-in-ios-building-better-apps-step-by-step-53e6ec8b3abd)
- [@article@Clean Architecture for SwiftUI](https://nalexn.github.io/clean-architecture-swiftui/)
- [@video@Clean iOS Architecture pt.1: Analytics Architecture Overview](https://www.youtube.com/watch?v=PnqJiJVc0P8&list=PLyjgjmI1UzlSWtjAMPOt03L7InkCRlGzb)

## Clipshape

# clipShape

`clipShape` in SwiftUI allows you to mask a view, effectively cropping it to a specific shape. Instead of displaying the entire rectangular area of a view, `clipShape` lets you define a shape (like a circle, rectangle with rounded corners, or even a custom shape), and only the portion of the view that falls within that shape will be visible. Anything outside the shape is hidden. This is useful for creating visually appealing designs and focusing attention on specific parts of a view.

Visit the following resources to learn more:

- [@official@ClipShape](https://developer.apple.com/documentation/swiftui/view/clipshape(_:style:))
- [@article@How to clip a view so only part is visible](https://www.hackingwithswift.com/quick-start/swiftui/how-to-clip-a-view-so-only-part-is-visible)
- [@article@SwiftUI: Bring back cornerRadius](https://lukaspistrol.com/blog/swiftui-bring-back-corner-radius/)

## Closures

# Closures

Closures in Swift are self-contained blocks of functionality that can be passed around and used in your code. Think of them as mini-functions without a name. They're similar to lambdas or anonymous functions in other programming languages, allowing you to define a function-like construct directly where it's needed, often for short, specific tasks. Closures can capture and store references to any constants and variables from the context in which they are defined, which means they can access and modify values from their surrounding scope, even after the original scope has ended.

Visit the following resources to learn more:

- [@official@Closures](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/closures)
- [@video@How to create and use closures – Swift for Complete Beginners](https://www.youtube.com/watch?v=F68lyXkkfCY)
- [@video@Swift Closures Explained](https://www.youtube.com/watch?v=ND44vQ5iJyc)

## Cloudkit

# CloudKit

CloudKit is Apple's cloud storage solution that allows developers to save and retrieve app data in iCloud. It provides a way to store structured data, like records with fields, and binary data, like images or videos, in the cloud. Users can access their data across all their devices logged into the same iCloud account, and you can also create public data that's accessible to all users of your app.

Visit the following resources to learn more:

- [@official@CloudKit](https://developer.apple.com/icloud/cloudkit/)
- [@article@CloudKit: A Concise Tutorial](https://medium.com/mackmobile/cloudkit-a-concise-tutorial-10e09d5a043b)
- [@video@Building a CloudKit-Powered To-Do App in SwiftUI: Step-by-Step Tutorial Part 1](https://www.youtube.com/watch?v=Guhn8VuHZ7k)
- [@video@Building a CloudKit-Powered To-Do App in SwiftUI: Step-by-Step Tutorial Part 2](https://www.youtube.com/watch?v=u53gxmdx-8I)

## Cocoalumberjack

# CocoaLumberjack

CocoaLumberjack is a logging framework for Objective-C and Swift that provides a flexible and powerful way to record and manage log messages in your applications. It allows you to log to multiple destinations simultaneously, such as the console, files, or even remote servers, and offers different log levels to filter messages based on their severity. CocoaLumberjack also supports asynchronous logging to avoid blocking the main thread and provides features like log file rotation and archiving.

Visit the following resources to learn more:

- [@opensource@CocoaLumberjack](https://github.com/CocoaLumberjack/CocoaLumberjack)
- [@article@iOS — How to Setup Logging Correctly with CocoaLumberjack](https://canopas.com/ios-how-to-setup-logging-correctly-with-cocoalumberjack-37836ec821b0)

## Comments

# Comments in Swift

Comments in Swift are notes within your code that the compiler ignores. They're used to explain what the code does, making it easier for you and others to understand. You can create single-line comments using two forward slashes `//`. Anything after `//` on that line will be treated as a comment. For multi-line comments, you can use `/*` to start the comment and `*/` to end it. Everything in between `/*` and `*/` will be ignored by the compiler, allowing you to write longer explanations or temporarily disable blocks of code.

Visit the following resources to learn more:

- [@official@Comments](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/thebasics/#Comments)
- [@article@Swift Comments](https://www.programiz.com/swift-programming/comments)

## Comparison

# Comparison Operators

Comparison operators are symbols used to compare two values. These operators evaluate to a Boolean value (either `true` or `false`) based on the relationship between the values being compared. Common comparison operators include equal to (`==`), not equal to (`!=`), greater than (`>`), less than (`<`), greater than or equal to (`>=`), and less than or equal to (`<=`).

Visit the following resources to learn more:

- [@official@Comparison Operators](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/basicoperators/#Comparison-Operators)

## Computed

# Computed Properties

Computed properties in Swift provide a way to calculate a value rather than storing it directly. Unlike stored properties, which hold a value in memory, computed properties offer a getter to retrieve a value and an optional setter to indirectly set other properties. This allows you to perform calculations or transformations on other data when accessing or modifying the computed property.

Visit the following resources to learn more:

- [@official@Computer Properties](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/properties#Computed-Properties)
- [@article@Swift Computed Property: Code Examples](https://www.avanderlee.com/swift/computed-property/)
- [@video@Computed Properties in Swift](https://www.youtube.com/watch?v=yze92fm54vU)

## Constants  Variables

# Constants & Variables

Constants and variables are fundamental building blocks in Swift for storing data. A variable holds a value that can be changed during the execution of a program, while a constant holds a value that, once assigned, cannot be altered. They are declared using the `var` and `let` keywords, respectively, followed by the name you choose for the constant or variable and its data type.

Visit the following resources to learn more:

- [@official@Constants & Variables](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/thebasics/#Constants-and-Variables)
- [@video@How to create constants and variables – Swift for Complete Beginners](https://www.youtube.com/watch?v=jlkcxTyM8m4)

## Continue  Break

# Continue & Break in Swift Loops

In Swift, `continue` and `break` are control flow statements used within loops (like `for`, `while`, and `repeat-while`) to alter their execution. The `continue` statement skips the rest of the current iteration of the loop and proceeds to the next iteration. The `break` statement, on the other hand, immediately terminates the entire loop, and the program execution resumes at the next statement after the loop.

Visit the following resources to learn more:

- [@article@Control Transfer Statements](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/controlflow/#Control-Transfer-Statements)
- [@video@How to skip loop items with break and continue – Swift for Complete Beginners](https://www.youtube.com/watch?v=z_kR4cP23c4)

## Core Data

# Core Data

Core Data is a framework provided by Apple for managing the model layer objects in your application. It's not a database itself, but rather an object graph management and persistence framework. Core Data allows you to treat data as objects, making it easier to work with and manage complex relationships between data entities, and it handles the underlying storage and retrieval of that data.

Visit the following resources to learn more:

- [@official@Core Data](https://developer.apple.com/documentation/coredata/)
- [@article@Introduction to using Core Data with SwiftUI](https://www.hackingwithswift.com/quick-start/swiftui/introduction-to-using-core-data-with-swiftui)
- [@article@Core Data (CRUD) in Swift Using Xcode for Beginners](https://medium.com/@elamaran_G/core-data-crud-in-swift-using-xcode-for-beginners-4b33788750bd)
- [@video@How to Save and Manage Data with Core Data in Swift - SwiftUI Basics Tutorial 2023](https://www.youtube.com/watch?v=nTcrzJ49m-U)

## Creating Packages

# Creating Swift Packages

The Swift Package Manager is a tool for managing the distribution of Swift code. Creating a Swift package allows you to bundle your code into reusable modules, making it easy to share and use in other projects. This involves defining the package's structure, specifying dependencies, and building the code into a distributable format.

Visit the following resources to learn more:

- [@official@Creating a Library Package](https://docs.swift.org/swiftpm/documentation/packagemanagerdocs/gettingstarted#Creating-a-Library-Package)
- [@official@Creating a standalone Swift package with Xcode](https://developer.apple.com/documentation/xcode/creating-a-standalone-swift-package-with-xcode)
- [@article@Swift Package Manager framework creation in Xcode](https://www.avanderlee.com/swift/creating-swift-package-manager-framework/)
- [@video@Creating and Publishing Swift Packages (Swift Package Manager)](https://www.youtube.com/watch?v=4Rxuc4BcW8o)
- [@video@Create a Swift Package from Your SwiftUI Project (SF Symbol Picker)](https://www.youtube.com/watch?v=_KYc2wJVIDE)

## Data Flow

# Data Flow

Data flow refers to how data moves and changes within your application. It describes the path data takes from its source, through various components, and ultimately to the user interface. Understanding data flow is crucial for building predictable and maintainable apps, as it helps you manage state and ensure that changes in data are reflected correctly in your UI.

Visit the following resources to learn more:

- [@official@Managing data flow between views](https://developer.apple.com/tutorials/app-dev-training/managing-data-flow-between-views)
- [@official@Model Data](https://developer.apple.com/documentation/swiftui/model-data)
- [@article@SwiftUI Data Flow: Passing Data Between Views](https://matteomanferdini.com/swiftui-data-flow/)
- [@video@Data Flow Through SwiftUI](https://developer.apple.com/la/videos/play/wwdc2019/226/)

## Data Persistance

# Data Persistence

Data persistence refers to the ability of an application to store data in a way that it remains available even after the application is closed or the device is restarted. This allows apps to remember user preferences, save progress, or maintain data across multiple sessions. In Swift and SwiftUI, various techniques can be employed to achieve data persistence, ranging from simple methods like storing data in UserDefaults to more complex solutions like using Core Data or external databases.

Visit the following resources to learn more:

- [@official@Persisting data](https://developer.apple.com/tutorials/app-dev-training/persisting-data)
- [@official@Adding and editing persistent data in your app](https://developer.apple.com/documentation/SwiftData/Adding-and-editing-persistent-data-in-your-app)
- [@article@A Guide to Persistence Storage in iOS](https://medium.com/mobile-app-development-publication/a-guide-to-persistence-storage-in-ios-a8b4f7355486)
- [@article@iOS Data Persistence: A Guide for Swift Developers](https://bugfender.com/blog/ios-data-persistence/)

## Databases

# Databases

Databases provide a structured way to store and manage data within your Swift applications. They allow you to persist information beyond the app's runtime, meaning data is saved even when the app is closed. This is essential for storing user information, application settings, or any other data that needs to be retained between sessions. You can interact with databases using various frameworks and libraries in Swift, enabling you to create, read, update, and delete data efficiently.

Visit the following resources to learn more:

- [@article@Working with Databases in Swift: A Comprehensive Guide](https://thatthinginswift.com/working-with-databases-in-swift-a-comprehensive-guide/)
- [@article@Databases & Persistance](https://www.swift.org/packages/database.html)

## Dependency Injection

# Dependency Injection

Dependency Injection is a design pattern where a component receives its dependencies from external sources rather than creating them itself. This promotes loose coupling, making code more modular, testable, and reusable. Instead of a class being responsible for instantiating the objects it needs, those objects are "injected" into the class, often through its initializer or properties.

Visit the following resources to learn more:

- [@article@Complete Guide to Dependency Injection in Swift](https://www.swiftanytime.com/blog/dependency-injection-in-swift)
- [@article@Dependency Injection in SwiftUI: From Basics to Advanced DI Containers](https://medium.com/@nimjea/dependency-injection-in-swiftui-from-basics-to-advanced-di-containers-241b8de76d7a)

## Docc

# DocC

DocC is Apple's documentation compiler that allows developers to create rich, interactive documentation directly from their Swift or Objective-C code. It transforms specially formatted comments within your code into a structured and navigable documentation set, complete with articles, tutorials, and API reference. This helps developers understand how to use your code effectively and efficiently.

Visit the following resources to learn more:

- [@official@DocC](https://www.swift.org/documentation/docc/)
- [@video@Meet DocC documentation in Xcode](https://developer.apple.com/la/videos/play/wwdc2021/10166/)
- [@video@WWDC21: Host and automate your DocC documentation | Apple](https://www.youtube.com/watch?v=Fkeih0S_d2k)

## Drag  Drop

# Drag & Drop

Drag and drop is a user interface interaction that allows users to select an item (the "drag") and move it to a different location (the "drop"). This interaction is commonly used for rearranging items in a list, moving files between folders, or transferring data between different parts of an application. It provides a direct and intuitive way for users to manipulate elements within a graphical user interface.

Visit the following resources to learn more:

- [@official@Drag & Drop](https://developer.apple.com/documentation/swiftui/drag-and-drop)
- [@official@Adopting drag and drop using SwiftUI](https://developer.apple.com/documentation/SwiftUI/Adopting-drag-and-drop-using-SwiftUI)
- [@official@Making a view into a drag source](https://developer.apple.com/documentation/swiftui/making-a-view-into-a-drag-source)
- [@article@Drag and Drop in SwiftUI](https://medium.com/@jpmtech/drag-and-drop-in-swiftui-2ff65c263d2e)
- [@video@SwiftUI Drag and Drop with Transferable Custom Object](https://www.youtube.com/watch?v=lsXqJKm4l-U)

## Emacs

# Emacs

Emacs is a highly customizable and extensible text editor, known for its powerful editing capabilities and extensive ecosystem of packages. It's more than just a text editor; it's often described as an operating system within an operating system, allowing users to tailor the environment to their specific needs through Lisp programming. While not as commonly used as Xcode for Swift and SwiftUI development, Emacs can be configured to provide a robust coding environment with features like syntax highlighting, code completion, and debugging support.

Visit the following resources to learn more:

- [@official@Configuring Emacs for Swift Development](https://www.swift.org/documentation/articles/zero-to-swift-emacs.html)

## Enumerations

# Enumerations

Enumerations, often shortened to enums, are a way to define a group of related values under a common type. They essentially let you create your own custom data types where the possible values are explicitly defined. This makes your code more readable and safer by restricting the values a variable can hold to only those you've specified in the enum.

Visit the following resources to learn more:

- [@official@Enumerations](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/enumerations/)
- [@video@Introduction to Swift: Enumerations](https://www.youtube.com/watch?v=1Deixr4KQ3Q&embeds_referring_euri=https%3A%2F%2Fwww.hackingwithswift.com%2F&source_ve_path=MjM4NTE)

## Environmentobject

# @EnvironmentObject

`@EnvironmentObject` allows you to share data across your entire app or specific parts of your view hierarchy without having to manually pass it down through each view. It's a way to make data accessible to any view that needs it, acting like a global state container that SwiftUI manages. This is particularly useful for things like user settings, app configurations, or shared data models.

Visit the following resources to learn more:

- [@official@EnvironmentObject](https://developer.apple.com/documentation/swiftui/environmentobject)
- [@article@How to use @EnvironmentObject to share data between views](https://www.hackingwithswift.com/quick-start/swiftui/how-to-use-environmentobject-to-share-data-between-views)
- [@article@@EnvironmentObject explained for sharing data between views in SwiftUI](https://www.avanderlee.com/swiftui/environmentobject/)

## Error Handling

# Error Handling

Error handling is a mechanism for responding to and recovering from error conditions that your program may encounter during execution. It allows you to gracefully manage unexpected situations, such as invalid input, network failures, or file access issues, preventing your app from crashing and providing a more robust user experience. Swift provides built-in mechanisms to throw, catch, and propagate errors, ensuring that errors are properly addressed at the appropriate level of your code.

Visit the following resources to learn more:

- [@official@Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html)
- [@article@Swift Error Handling Made Easy: A Practical Guide with Code Examples](https://vikramios.medium.com/swift-error-handling-4a206acd9710)
- [@article@Swift Error Handling: Try, Throw & Do-Catch Explained](https://bugfender.com/blog/swift-error-handling/)

## Explicit Animations

# Explicit Animations

Explicit animations involve directly controlling the animation's behavior by specifying its parameters, such as duration, delay, and easing. Instead of relying on implicit transitions triggered by state changes, you define exactly how a view's properties animate from one value to another. This gives you fine-grained control over the animation's appearance and timing, allowing for more complex and customized visual effects.

Visit the following resources to learn more:

- [@official@WithAnimation](https://developer.apple.com/documentation/swiftui/withanimation(_:_:))
- [@video@Creating explicit animations – Animation SwiftUI Tutorial 4/8](https://www.youtube.com/watch?v=Sk24dfBUnmg)

## Extensions

# Extensions

Extensions in Swift are a way to add new functionality to an existing class, structure, enumeration, or protocol type. They allow you to extend types even if you don't have access to the original source code. Extensions can add computed instance properties, define instance methods and type methods, provide new initializers, define subscripts, define and use new nested types, and make an existing type conform to a protocol.

Visit the following resources to learn more:

- [@official@Extensions](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/extensions/)
- [@article@Extensions in Swift: How and when to use them](https://www.avanderlee.com/swift/extensions/)
- [@video@How to create and use extensions – Swift for Complete Beginners](https://www.youtube.com/watch?v=ALsr3hANqD0)

## Filemanager

# FileManager

FileManager provides a way to interact with the file system. It allows you to perform operations like creating, reading, writing, deleting, and moving files and directories. You can use it to manage data stored locally on the device, such as user preferences, cached data, or downloaded content.

Visit the following resources to learn more:

- [@official@FileManager](https://developer.apple.com/documentation/Foundation/FileManager)
- [@article@Swift File Manager: Reading, Writing, and Deleting Files and Directories](https://www.swiftyplace.com/blog/file-manager-in-swift-reading-writing-and-deleting-files-and-directories)
- [@article@File handling in Swift using FileManager](https://how.dev/answers/file-handling-in-swift-using-filemanager)
- [@video@Save data and images to FileManager in Xcode | Continued Learning #26](https://www.youtube.com/watch?v=Yiq-hdhLzVM)

## Firabase

# Firebase

Firebase is a Backend-as-a-Service (BaaS) platform that provides developers with a suite of tools and services to build, manage, and grow their apps. It handles many backend tasks, such as data storage, user authentication, hosting, and analytics, allowing developers to focus on building the front-end user experience. Firebase offers both NoSQL and real-time database solutions, making it a versatile choice for various application needs.

Visit the following resources to learn more:

- [@official@Firebase](https://firebase.google.com/)
- [@official@Add Firebase to your Apple project](https://firebase.google.com/docs/ios/setup)
- [@video@Getting started with Firebase on Apple platforms](https://www.youtube.com/watch?v=F9Gs_pfT3hs)

## Floats  Doubles

# Floats and Doubles

Floats and Doubles are fundamental data types in Swift used to represent numbers with fractional components (decimal numbers). A `Float` represents a 32-bit floating-point number, offering a balance between memory usage and precision. A `Double` represents a 64-bit floating-point number, providing greater precision than `Float` but requiring more memory. You would use these when you need to represent values like prices, measurements, or any other non-integer quantity.

Visit the following resources to learn more:

- [@official@Floats](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/thebasics/#Floating-Point-Numbers)
- [@article@Data Types in Swift](https://medium.com/@andyandmishel15/data-types-in-swift-b6d0e6cc65fa)
- [@video@Swift Tutorial for Beginners: Lesson 2 Data Types](https://www.youtube.com/watch?v=zcLMOTEDd8Y)

## Font

# Font Modifier

The `font` modifier in SwiftUI allows you to customize the appearance of text within your views by specifying the typeface, weight, and size. It provides a way to control how text is displayed, enabling you to create visually appealing and consistent user interfaces. You can apply different font styles to various text elements in your app, such as labels, buttons, and text fields, to enhance readability and overall design.

Visit the following resources to learn more:

- [@official@Font](https://developer.apple.com/documentation/swiftui/view/font(_:))
- [@article@SwiftUI Font and Texts](https://www.swiftyplace.com/blog/swiftui-font-and-texts)
- [@article@SwiftUI .font()](https://www.codecademy.com/resources/docs/swiftui/viewmodifier/font)
- [@video@Why SwiftUI's Built-In Font is OP](https://www.youtube.com/watch?v=e4s37VcWCj0)

## For

# For-in Loops in Swift

In Swift, a `for` loop provides a clean and concise way to iterate over a sequence of items, such as elements in an array, characters in a string, or a range of numbers. It executes a block of code repeatedly for each item in the sequence. The basic structure involves specifying a loop variable that takes on the value of each item in the sequence during each iteration, allowing you to perform operations on each item within the loop's body.

Visit the following resources to learn more:

- [@official@For-in loops](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/controlflow/#For-In-Loops)
- [@video@How to use For Loops in Swift | Swift Basics](https://www.youtube.com/watch?v=7hAmXRwBQxc)

## Form

# Form

In Swift and SwiftUI, a `Form` is a container view that's designed to organize and display input controls, such as text fields, toggles, and pickers. It automatically handles the layout and styling of these controls, making it easier to create structured and user-friendly interfaces for collecting data or configuring settings. Think of it as a pre-built structure that simplifies the process of creating forms in your app.

Visit the following resources to learn more:

- [@official@Form](https://developer.apple.com/documentation/swiftui/displaying-data-in-lists)
- [@article@What is SwiftUI Form](https://sarunw.com/posts/swiftui-form/)
- [@video@Creating a form – WeSplit SwiftUI Tutorial 2/11](https://www.youtube.com/watch?v=4Ui09XbYf1A&t=1s)

## Function Types

# Function Types

In Swift, functions are first-class citizens, meaning they can be treated like any other data type. A function type describes the parameters a function accepts and the type of value it returns. This allows you to assign functions to variables, pass them as arguments to other functions, and return them as values from functions, providing a powerful way to abstract and reuse code.

Visit the following resources to learn more:

- [@official@Function Types](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/functions#Function-Types)
- [@video@#55 Swift Programming - Using Functions Types](https://www.youtube.com/watch?v=UhE1VZjDK_c)

## Generics

# Generics

Generics allow you to write flexible and reusable code that can work with any type. Instead of writing separate functions or structs for each data type you want to support, you can define a single function or struct that works with a placeholder type. This placeholder type is then specified when the function or struct is used, making your code more adaptable and less repetitive.

Visit the following resources to learn more:

- [@official@Generics](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/generics/)
- [@article@Generics in Swift explained with code examples](https://www.avanderlee.com/swift/generics-constraints/)
- [@video@Swift Generics for Beginners - Eliminate Code Duplication](https://www.youtube.com/watch?v=a3AH0ItFTKU)

## Geometryreader

# GeometryReader

GeometryReader is a container view that provides information about its own size and position within its parent view. It allows you to access the available space offered by the parent, enabling you to create views that adapt dynamically to different screen sizes and orientations. By using a closure, you can access a `GeometryProxy` object, which contains the frame (size and position) of the GeometryReader. This information can then be used to calculate and position other views relative to the GeometryReader's frame.

Visit the following resources to learn more:

- [@official@GeometryReader](https://developer.apple.com/documentation/swiftui/geometryreader)
- [@article@Understanding frames and coordinates inside GeometryReader](https://www.hackingwithswift.com/books/ios-swiftui/understanding-frames-and-coordinates-inside-geometryreader)
- [@video@GeometryReader in SwiftUI to get a view's size and location | Continued Learning #6](https://www.youtube.com/watch?v=lMteVjlOIbM)

## Gestures

# Gestures

Gestures are actions performed by a user to interact with a device's screen, such as tapping, swiping, pinching, or rotating. They allow users to directly manipulate and control elements within an application, providing a more intuitive and engaging experience. By recognizing and responding to these gestures, developers can create interactive user interfaces that feel natural and responsive.

Visit the following resources to learn more:

- [@official@Gerstures](https://developer.apple.com/documentation/swiftui/gestures)
- [@official@Adding interactivity with gestures](https://developer.apple.com/documentation/swiftui/adding-interactivity-with-gestures)
- [@video@How to use gestures in SwiftUI – Flashzilla SwiftUI Tutorial 1/13](https://www.youtube.com/watch?v=Kl_3xrZBEFY)

## Grdb

# GRDB

GRDB is a Swift library that provides a convenient and reliable way to interact with SQLite databases. It allows you to perform database operations like creating tables, inserting, querying, updating, and deleting data using Swift code. GRDB focuses on safety, performance, and ease of use, making it a good choice for managing local data storage in your Swift and SwiftUI applications.

Visit the following resources to learn more:

- [@opensource@GRDB](https://github.com/groue/GRDB.swift)
- [@official@GRDB](https://swiftpackageindex.com/groue/GRDB.swift/v7.8.0/documentation/grdb)
- [@article@How to build an iOS application with SQLite and GRDB.swift](https://medium.com/@gwendal.roue/how-to-build-an-ios-application-with-sqlite-and-grdb-swift-d023a06c29b3)
- [@video@SwiftUI: GRDB.swift - Set up](https://www.youtube.com/watch?v=11AMFUH6rro)
- [@video@SwiftUI: GRDB.swift - Usage](https://www.youtube.com/watch?v=CjYxAXBzrjo)

## Grid

# Grid

A Grid is a layout container that arranges views in a two-dimensional grid, similar to a table. It allows you to organize content into rows and columns, providing a structured way to display information and create complex layouts. You can customize the appearance and behavior of the grid by specifying the number of columns, row spacing, column spacing, and alignment of the views within the grid cells.

Visit the following resources to learn more:

- [@official@Grid](https://developer.apple.com/documentation/swiftui/grid)
- [@article@SwiftUI Grid, LazyVGrid, LazyHGrid Explained with Code Examples](https://www.avanderlee.com/swiftui/grid-lazyvgrid-lazyhgrid-gridviews/)
- [@article@LazyVGrid](https://www.swiftuifieldguide.com/layout/lazyvgrid/)
- [@video@How to use Grid in SwiftUI | Bootcamp #73](https://www.youtube.com/watch?v=LnPMsG0sV50)
- [@video@SwiftUI Grids - LazyVGrid, LazyHGrid, Static Grid](https://www.youtube.com/watch?v=vfUalXtwth0)

## Hstack

# HStack

An `HStack` is a layout container that arranges its child views in a horizontal line. It's like a row where you place different UI elements side-by-side. You can control the spacing between these elements and how they align vertically within the row. `HStack` simplifies creating horizontal layouts without needing to manually calculate positions and sizes.

Visit the following resources to learn more:

- [@official@HStack](https://developer.apple.com/documentation/swiftui/hstack)
- [@official@Building layouts with stack views](https://developer.apple.com/documentation/swiftui/building-layouts-with-stack-views)
- [@article@HStack](https://www.swiftuifieldguide.com/layout/hstack/)
- [@video@VStack, HStack, and ZStack in SwiftUI | Bootcamp](https://www.youtube.com/watch?v=pv-vbUEzimk)

## Hummingbird

# Hummingbird

Hummingbird is an open-source server-side framework written in Swift, designed to help developers build high-performance web applications and APIs. It leverages Swift's type safety and concurrency features to provide a robust and efficient platform for handling HTTP requests, routing, and middleware. Hummingbird aims to simplify server-side development in Swift, offering a clean and expressive syntax for defining endpoints and processing data.

Visit the following resources to learn more:

- [@opensource@Hummingbird](https://github.com/hummingbird-project/hummingbird)
- [@official@Hummingbird](https://hummingbird.codes/)
- [@article@Getting Started with Hummingbird](https://swiftonserver.com/getting-started-with-hummingbird/)
- [@video@Introduction to Hummingbird 2 - Joannis Orlandos](https://www.youtube.com/watch?v=FHO_BfidQlQ)

## Ides

# IDEs

An Integrated Development Environment (IDE) is a software application that provides comprehensive facilities to computer programmers for software development. An IDE typically includes a source code editor, build automation tools, and a debugger. These tools are designed to streamline the process of writing, testing, and debugging code, making software development more efficient.

Visit the following resources to learn more:

- [@article@5 Best Swift IDEs & Text Editors](https://www.bairesdev.com/blog/best-swift-ide-text-editor/)

## If  Else

# If / Else Statements

`if` and `else` statements are fundamental control flow structures in Swift that allow your code to execute different blocks of code based on whether a condition is true or false. The `if` statement evaluates a Boolean expression, and if the expression is `true`, the code within the `if` block is executed. Optionally, you can include an `else` block, which will be executed if the `if` condition is `false`. You can also chain multiple conditions together using `else if` to handle more complex scenarios.

Visit the following resources to learn more:

- [@official@Conditional Statements](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/controlflow/#Conditional-Statements)
- [@article@Swift if, else statements](https://www.programiz.com/swift-programming/if-else-statement)
- [@video@Swift Tutorial for Beginners: Lesson 3 IF Statements](https://www.youtube.com/watch?v=H_xErt38mWg)

## Image

# Image

`Image` is a fundamental view used to display pictures or graphics within your app's user interface. It allows you to load images from various sources, such as your app's asset catalog, the file system, or even remote URLs, and present them to the user. You can customize the appearance of an `Image` by applying modifiers to control its size, scaling behavior, and other visual properties.

Visit the following resources to learn more:

- [@official@Image](https://developer.apple.com/documentation/swiftui/image)
- [@article@How to draw images using Image views](https://www.hackingwithswift.com/quick-start/swiftui/how-to-draw-images-using-image-views)
- [@video@Mastering Images in SwiftUI – Assets, Bundles, Remote URLs & Effects](https://www.youtube.com/watch?v=KnuKc9eICM4)
- [@video@Adding images to a SwiftUI application | Bootcamp #7](https://www.youtube.com/watch?v=MeoiHFdIeR8)

## Implicit Animations

# Implicit Animations

Implicit animations in Swift UI provide a simple way to animate changes to a view's properties. When a property that affects the view's appearance changes, and an animation modifier is attached to the view, Swift UI automatically animates the transition between the old and new values. This creates smooth and visually appealing effects without requiring explicit animation blocks or complex code.

Visit the following resources to learn more:

- [@official@Animation](https://developer.apple.com/documentation/swiftui/animation)
- [@article@Difference Between Implicit and Explicit Animations in SwiftUI](https://holyswift.app/difference-between-implicit-and-explicit-animations-in-swiftui/)
- [@video@Creating implicit animations](https://www.youtube.com/watch?v=D3N-GA_J73g)

## Inheritance

# Inheritance

Inheritance is a fundamental concept in object-oriented programming where a new class (called a subclass or derived class) can inherit properties and methods from an existing class (called a superclass or base class). This allows you to create a hierarchy of classes, where subclasses inherit and extend the functionality of their superclasses, promoting code reuse and establishing relationships between different types of objects.

Visit the following resources to learn more:

- [@official@Inheritance](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/inheritance/)
- [@article@Swift Inheritance](https://www.programiz.com/swift-programming/inheritance)
- [@video@Swift For Beginners - Class & Inheritance Explained](https://www.youtube.com/watch?v=EhDML-fAqTM)

## Initialization

# Initialization

Initialization is the process of preparing an instance of a class, structure, or enumeration for use. This involves setting an initial value for each stored property on that instance and performing any other setup or initialization required before the new instance is ready. Initializers are special methods that are called when a new instance is created, ensuring that the instance is in a valid and usable state.

Visit the following resources to learn more:

- [@official@Initialization](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/initialization/)
- [@article@Swift init()](https://www.digitalocean.com/community/tutorials/swift-init)
- [@video@Understanding Swift Initializers](https://www.youtube.com/watch?v=ElfPQZ9MVTQ)

## Installing Swift

# Installing Swift

Installing Swift involves setting up the Swift compiler and related tools on your system, allowing you to write and run Swift code. This typically involves downloading a Swift toolchain from the official Swift.org website or using a package manager like Homebrew on macOS or apt on Linux. The installation process configures your environment to recognize Swift commands, allowing you to compile and execute Swift programs.

Visit the following resources to learn more:

- [@official@Installing Swift](https://www.swift.org/install/macos/)
- [@article@Quick and Easy Guide to Install Swift on Your System](https://www.dhiwise.com/post/quick-and-easy-guide-to-install-swift-on-your-system)

## Integers

# Integers in Swift

Integers in Swift are whole numbers, meaning they don't have any fractional or decimal parts. They can be positive, negative, or zero. Swift provides different integer types (like `Int`, `Int8`, `Int16`, `Int32`, `Int64`, `UInt`, `UInt8`, etc.) that vary in the range of values they can store, allowing you to choose the most appropriate type based on the expected size of the number you're working with. The default `Int` type is usually sufficient for most general-purpose integer storage, and its size depends on the platform (typically 32-bit or 64-bit).

Visit the following resources to learn more:

- [@official@Integers](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/thebasics/#Integers)
- [@article@Data Types in Swift](https://medium.com/@andyandmishel15/data-types-in-swift-b6d0e6cc65fa)
- [@video@(2020) Swift Tutorial for Beginners: Lesson 2 Data Types](https://www.youtube.com/watch?v=zcLMOTEDd8Y)

## Introduction

# Introduction to Swift & SwiftUI

Swift is a powerful and intuitive programming language developed by Apple, designed for building apps across all Apple platforms, including iOS, macOS, watchOS, and tvOS. SwiftUI is a declarative UI framework that enables developers to create user interfaces straightforwardly and efficiently using Swift. It offers a modern approach to UI development, emphasizing simplicity, readability, and live previews, which makes it easier to build dynamic and visually appealing applications.

Visit the following resources to learn more:

- [@official@Swift](https://www.swift.org/about/)
- [@article@SwiftUI](https://developer.apple.com/documentation/swiftui)
- [@article@What’s the difference between Swift and SwiftUI?](https://www.hackingwithswift.com/quick-start/understanding-swift/whats-the-difference-between-swift-and-swiftui)
- [@video@Swift in 100 Seconds](https://www.youtube.com/watch?v=nAchMctX4YA)
- [@video@What Is SwiftUI? | In Under 10 Minutes](https://www.youtube.com/watch?v=K_OaH4nUI_Q)

## List

# List

A `List` is a container view that arranges data in a single column, making it easy to display scrollable collections of items. It's similar to a table view in UIKit, but with a more declarative and flexible approach. You can populate a `List` with static content or dynamically generate rows based on data from an array or other data source.

Visit the following resources to learn more:

- [@official@List](https://developer.apple.com/documentation/swiftui/list)
- [@official@Displaying data in lists](https://developer.apple.com/documentation/swiftui/displaying-data-in-lists)
- [@video@SwiftUI Tutorial: How to create List View, Custom Cells, and use List Styles](https://www.youtube.com/watch?v=X5hy3M47OC4)
- [@video@Add, edit, move, and delete items in a List in SwiftUI | Bootcamp #31](https://www.youtube.com/watch?v=tkOnXG-sNks)

## Localization

# Localization

Localization is the process of adapting your app to different languages, regions, and cultures. This involves translating text, adjusting layouts for different reading directions, and formatting dates, times, and currencies according to local conventions. By localizing your app, you can reach a wider audience and provide a more user-friendly experience for people around the world.

Visit the following resources to learn more:

- [@official@Preparing views for localization](https://developer.apple.com/documentation/SwiftUI/Preparing-views-for-localization)
- [@article@Localize Your Apps to Support Multiple Languages — iOS Localization in SwiftUI](https://medium.com/simform-engineering/localize-your-apps-to-support-multiple-languages-ios-localization-in-swiftui-c72d891a3e9)
- [@article@A Step-by-Step SwiftUI Tutorial](https://phrase.com/blog/posts/swiftui-tutorial-localization/)
- [@video@WWDC25: Code-along: Explore localization with Xcode | Apple](https://www.youtube.com/watch?v=dcfrrz9iCEE)
- [@video@How to translate and localize an iOS app with string catalogs in Xcode 15](https://www.youtube.com/watch?v=slOQbTacj4k&t=182s)

## Logging  Debugging

# Logging & Debugging

Logging and debugging are essential practices in software development for identifying and resolving issues in your code. Logging involves recording information about your application's behavior as it runs, allowing you to trace events and diagnose problems. Debugging, on the other hand, is the process of stepping through your code, examining variables, and understanding the flow of execution to pinpoint the source of errors. These techniques help ensure your Swift and SwiftUI applications function correctly and provide a smooth user experience.

Visit the following resources to learn more:

- [@official@https://developer.apple.com/documentation/os/logging](https://developer.apple.com/documentation/os/logging)
- [@official@Diagnosing and resolving bugs in your running app](https://developer.apple.com/documentation/xcode/diagnosing-and-resolving-bugs-in-your-running-app)
- [@video@Xcode 16 Debugging Tutorial for Beginners (2025)](https://www.youtube.com/watch?v=ZJmUeOT6c-Y)

## Logical

# Logical Operators

Logical operators in Swift allow you to combine or modify Boolean (true/false) values. They are used to create more complex conditions in your code. The primary logical operators are AND (`&&`), OR (`||`), and NOT (`!`). These operators enable you to control the flow of your program based on multiple conditions being met or not met.

Visit the following resources to learn more:

- [@official@Logical Operators](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/basicoperators/#Logical-Operators)

## Loops

# Loops

Loops are fundamental programming constructs that allow you to execute a block of code repeatedly. They provide a way to automate repetitive tasks, iterate over collections of data, and perform actions until a specific condition is met. In Swift, you'll primarily encounter `for-in` loops for iterating over sequences and `while` loops for repeating code based on a condition.

Visit the following resources to learn more:

- [@official@Loops](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/controlflow)
- [@article@Loops in Swift](https://medium.com/icommunity/loops-in-swift-8a9181fb364a)

## Macros

# Macros

Macros are a way to generate code at compile time. They allow you to write code that transforms or expands into other code, effectively automating repetitive tasks and enabling more expressive and concise syntax. This can lead to improved code readability, reduced boilerplate, and enhanced compile-time safety.

Visit the following resources to learn more:

- [@official@Macros](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/attributes/#resultBuilder)
- [@official@Applying Macros](https://developer.apple.com/documentation/swift/applying-macros)
- [@article@Swift Macros: Extend Swift with New Kinds of Expressions](https://www.avanderlee.com/swift/macros/)
- [@article@Macros](https://www.hackingwithswift.com/swift/5.9/macros)
- [@video@Swift Macros 101: Your Step-by-Step Guide To Crafting Your First Macro!](https://www.youtube.com/watch?v=NGpM9-t9tgs)

## Memory Safety

# Memory Safety

Memory safety in Swift is a set of language features that prevent common programming errors related to memory access. It ensures that your program accesses memory predictably and safely, preventing issues like accessing memory that has already been deallocated (dangling pointers) or writing outside the bounds of an allocated memory region (buffer overflows). Swift achieves this through features like automatic memory management (ARC), strong typing, and compile-time checks.

Visit the following resources to learn more:

- [@official@Memory Safety](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/memorysafety/)
- [@official@Automatic Reference Counting](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/automaticreferencecounting/)
- [@article@A detailed explanation of how ARC works in Swift](https://medium.com/@ahmed044/a-detailed-explanation-of-how-arc-works-in-swift-8076fc79e03b)

## Methods

# Methods in Swift Structures and Classes

Methods are functions that are associated with a particular type, like a structure or a class. They provide a way to encapsulate behavior and data together.  You can define methods to perform actions related to instances of that type, allowing you to interact with and manipulate the data stored within those instances.

Visit the following resources to learn more:

- [@official@Methods](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/methods)
- [@article@Swift Methods](https://www.programiz.com/swift-programming/methods)

## Mongokitten

# MongoKitten

MongoKitten is a native Swift driver for MongoDB, a popular NoSQL database. It allows Swift applications, including those built with SwiftUI, to interact with MongoDB databases for storing and retrieving data. This interaction involves establishing a connection, performing CRUD (Create, Read, Update, Delete) operations, and managing data structures within the MongoDB environment, all directly from Swift code.

Visit the following resources to learn more:

- [@opensource@MongoKitten](https://github.com/orlandos-nl/MongoKitten)
- [@article@Getting Started with MongoDB in Swift using MongoKitten](https://swiftonserver.com/getting-started-with-mongokitten/)
- [@article@MongoKitten Tutorial](https://swiftpackageindex.com/orlandos-nl/mongokitten/7.9.8/tutorials/intro)

## Moya

# Moya

Moya is a Swift networking library that simplifies the process of making API requests. It acts as an abstraction layer on top of URLSession, providing a cleaner and more organized way to define and manage your API endpoints. Instead of directly dealing with URLs, HTTP methods, and request parameters, you define your API as a set of "targets" (enums) that encapsulate all the necessary information for each request. This approach promotes code reusability, testability, and overall maintainability when working with network communication in your Swift applications.

Visit the following resources to learn more:

- [@opensource@Moya](https://github.com/Moya/Moya)
- [@article@Handling Network calls in Swift with Moya](https://medium.com/simform-engineering/handling-network-calls-in-swift-with-moya-c82908c93e5)

## Mvvm

# MVVM

MVVM (Model-View-ViewModel) is a software architectural pattern that facilitates the separation of concerns in application development. It divides an application into three interconnected parts: the Model (data and business logic), the View (the user interface), and the ViewModel (an intermediary that prepares data for the View and handles user input). This separation makes code more testable, maintainable, and reusable.

Visit the following resources to learn more:

- [@article@Swift Tutorial: An Introduction to the MVVM Design Pattern](https://www.toptal.com/ios/swift-tutorial-introduction-to-mvvm)
- [@article@Introducing MVVM into your SwiftUI project](https://www.hackingwithswift.com/books/ios-swiftui/introducing-mvvm-into-your-swiftui-project)
- [@video@SwiftUI - Intro to MVVM | Example Refactor | Model View ViewModel](https://www.youtube.com/watch?v=FwGMU_Grnf8)

## Navigationlink

# NavigationLink

`NavigationLink` enables navigation between different views within your app. It acts as a button or tappable element that, when activated, pushes a new view onto the navigation stack, displaying it to the user. This allows you to create hierarchical navigation structures, where users can drill down into more detailed content and then easily return to previous screens.

Visit the following resources to learn more:

- [@official@NavigationLink](https://developer.apple.com/documentation/swiftui/navigationlink)
- [@video@Displaying a detail screen with NavigationLink](https://www.hackingwithswift.com/quick-start/swiftui/displaying-a-detail-screen-with-navigationlink)
- [@video@The problem with a simple NavigationLink – Navigation SwiftUI Tutorial](https://www.youtube.com/watch?v=o8YHHQJzGz4)

## Navigationpath

# NavigationPath

`NavigationPath` provides a way to manage the navigation stack programmatically. Instead of relying solely on `NavigationLink` to push views onto the stack, `NavigationPath` allows you to manipulate the navigation history directly. This is particularly useful for scenarios where you need to navigate based on complex logic, deep linking, or when you want to programmatically control the back button behavior. It essentially acts as a data-driven representation of the navigation stack, enabling you to push, pop, or replace views more dynamically and flexibly.

Visit the following resources to learn more:

- [@official@NavigationPath](https://developer.apple.com/documentation/swiftui/navigationpath)
- [@article@Mastering NavigationStack in SwiftUI. NavigationPath.](https://swiftwithmajid.com/2022/10/05/mastering-navigationstack-in-swiftui-navigationpath/)
- [@video@Navigating to different data types using NavigationPath](https://www.youtube.com/watch?v=PU8q5UPHTS0)

## Navigationstack

# NavigationStack

`NavigationStack` provides a way to manage hierarchical navigation within your app. It allows users to move forward and backward through a stack of views, similar to how you navigate through folders on a computer. Each view pushed onto the stack becomes a new level in the navigation hierarchy, and the `NavigationStack` provides a back button (or gesture) to return to the previous view. This is the modern replacement for `NavigationView`, offering more flexibility and control over navigation.

Visit the following resources to learn more:

- [@official@NavigationStack](https://developer.apple.com/documentation/SwiftUI/NavigationStack)
- [@article@Programmatic navigation with NavigationStack](https://www.hackingwithswift.com/books/ios-swiftui/programmatic-navigation-with-navigationstack)
- [@official@Migrating to new navigation types](https://developer.apple.com/documentation/swiftui/migrating-to-new-navigation-types)

## Neovim

# Neovim

Neovim is a free and open-source, heavily refactored and extended version of the Vim text editor. It aims to improve Vim's extensibility, user experience, and maintainability. It allows developers to use plugins and extensions to customize their editing environment, and it can be used for coding in various languages, including Swift and Swift UI.

Visit the following resources to learn more:

- [@official@Neovim](https://neovim.io/)
- [@opensource@Neovim](https://github.com/neovim/neovim)
- [@official@Configuring Neovim for Swift Development](https://www.swift.org/documentation/articles/zero-to-swift-nvim.html)

## Nested Functions

# Nested Functions

Nested functions are functions defined inside the body of another function. The outer function is called the enclosing function, and the inner function is the nested function. Nested functions can access variables from their enclosing function's scope, even after the enclosing function has returned, creating a closure. This allows you to encapsulate and organize code, making it more readable and maintainable by keeping related functionality together.

Visit the following resources to learn more:

- [@official@Nested Functions](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/functions#Nested-Functions)
- [@article@Swift Nested Functions](https://www.programiz.com/swift-programming/nested-functions)

## Networking Libraries

# Networking Libraries

Networking libraries provide tools and abstractions to simplify the process of making network requests, handling responses, and managing data transfer. They handle tasks like creating URLs, managing connections, serializing data into formats like JSON, and parsing responses, allowing developers to focus on the application logic rather than the low-level details of network communication. These libraries often offer features like asynchronous operations, error handling, and request cancellation, making network operations more robust and easier to manage.

## Nil Coalescing

# Nil-Coalescing Operator

The nil-coalescing operator ( `??` ) provides a default value when an optional is nil. It's a shorthand way to unwrap an optional if it contains a value, or to provide an alternative value if the optional is nil. This operator simplifies code by avoiding verbose `if let` or `guard let` statements when handling optional values.

Visit the following resources to learn more:

- [@official@Nil-Coalescing Operator](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/basicoperators/#Nil-Coalescing-Operator)
- [@video@Nil coalescing – Swift in Sixty Seconds](https://www.youtube.com/watch?v=zXtCdd4JSlU)

## Observedobject

# @ObservedObject

`@ObservedObject` is a property wrapper in SwiftUI used to subscribe to an external class that conforms to the `ObservableObject` protocol.  When the observable object publishes changes (typically through `@Published` properties), any views observing it will automatically update to reflect the new data. This allows you to manage and share state across different parts of your SwiftUI application, ensuring that the UI stays synchronized with the underlying data model.

Visit the following resources to learn more:

- [@official@ObservedObject](https://developer.apple.com/documentation/swiftui/observedobject)
- [@article@How to use @ObservedObject to manage state from external objects](https://www.hackingwithswift.com/quick-start/swiftui/how-to-use-observedobject-to-manage-state-from-external-objects)
- [@video@DON'T Make this MISTAKE || StateObject vs ObservedObject | What's the Difference?](https://www.youtube.com/watch?v=RvzJLekIjRs)

## Observers

# Property Observers

Property observers in Swift allow you to monitor and respond to changes in a property's value. You can define code that will be executed before (willSet) or after (didSet) a property's value is set. This is useful for tasks like updating the user interface, performing calculations based on the new value, or validating data.

Visit the following resources to learn more:

- [@official@Property Observers](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/properties#Computed-Properties)
- [@video@Property observers: didSet – 7 Swifty Words, part 5](https://www.swiftbysundell.com/articles/property-observers-in-swift/)

## Operators

# Operators in Swift

Operators are special symbols or phrases that you use to check, change, or combine values. Swift supports a variety of operators, from familiar arithmetic operators like `+` and `-`, to more advanced operators for logic and bit manipulation. These operators allow you to perform calculations, make comparisons, and manipulate data within your Swift code.

Visit the following resources to learn more:

- [@official@Basic operators](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/basicoperators/)
- [@official@Advanced Operators](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/advancedoperators/)
- [@article@Swift Operators](https://www.programiz.com/swift-programming/operators)
- [@article@The Ultimate Guide to Operators in Swift](https://www.appypievibe.ai/blog/swift-code/operators-swift-how-to/)
- [@video@Introduction to Swift: Operators](https://www.youtube.com/watch?v=Svaq3jVy8sU)

## Optional Chaining

# Optional Chaining

Optional chaining is a feature that allows you to access properties, methods, and subscripts of an optional value. If the optional contains a value, the property, method, or subscript is accessed as normal. However, if the optional is `nil`, the entire chain gracefully fails and returns `nil` without causing a runtime error. This provides a concise way to conditionally access nested properties or methods when dealing with optionals.

Visit the following resources to learn more:

- [@official@Optional Chaining](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/optionalchaining/)
- [@article@Optional Binding vs. Optional Chaining: Swift Techniques to Avoid Runtime Errors](https://www.dhiwise.com/post/optional-binding-vs-optional-chaining-swift-techniques)
- [@video@Introduction to Swift: Optional chaining](https://www.youtube.com/watch?v=S8-QO2wUbRg)

## Optionals  Nil

# Optionals and nil

In Swift, an optional is a type that can hold either a value or the absence of a value (represented by `nil`). It's a way to indicate that a variable might not have a value at a particular time. `nil` itself represents the lack of a value for a variable of an optional type. Optionals are used to handle situations where a value might be missing, preventing unexpected errors and crashes in your code.

Visit the following resources to learn more:

- [@official@Optionals](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/thebasics/#Optionals)
- [@video@Introduction to Optionals](https://www.hackingwithswift.com/read/0/12/optionals)

## Padding

# Padding

Padding in Swift and SwiftUI is used to add space around the content of a view. It essentially creates a buffer zone between the view's content and its surrounding elements or the edges of its parent view. This helps improve the visual appearance and readability of your user interface by preventing elements from appearing cramped or too close together. You can control the amount of padding applied to all sides of a view or specify different padding values for each side (top, leading, bottom, trailing).

Visit the following resources to learn more:

- [@official@Padding](https://developer.apple.com/documentation/SwiftUI/View/padding(_:_:))
- [@article@SwiftUI .padding()](https://www.codecademy.com/resources/docs/swiftui/viewmodifier/padding)
- [@video@Adding Padding in SwiftUI View | Bootcamp #11](https://www.youtube.com/watch?v=MuOtLPQ4jR4)

## Parameters

# Parameters in Swift Functions and Closures

Parameters are named values that you pass into a function or closure when you call it. They act as inputs, allowing the function or closure to operate on specific data.  Each parameter has a name and a type, and you specify these in the function or closure's definition. When calling the function or closure, you provide arguments that correspond to these parameters, allowing you to customize the behavior of the code being executed.

Visit the following resources to learn more:

- [@official@Function Parameters and Return Values](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/functions/#Functions-With-Multiple-Parameters)
- [@video@How to use Functions in Swift | Swift Basics #5](https://www.youtube.com/watch?v=kr3SSplrJlw)

## Plugins

# Swift Package Manager Plugins

Swift Package Manager plugins allow you to extend the build process of your Swift packages with custom tools and scripts. These plugins can automate tasks like code generation, linting, formatting, and other pre-build or post-build operations, streamlining your development workflow and ensuring consistency across your projects. They essentially provide a way to integrate external tools and scripts directly into the Swift build system.

Visit the following resources to learn more:

- [@official@Plugins](https://docs.swift.org/swiftpm/documentation/packagemanagerdocs/plugins/)
- [@article@Meet Swift Package plugins](https://wwdcnotes.com/documentation/wwdcnotes/wwdc22-110359-meet-swift-package-plugins/)
- [@video@WWDC22: Create Swift Package plugins | Apple](https://www.youtube.com/watch?v=JiyZmB6aX30)
- [@video@WWDC22: Meet Swift Package plugins | Apple](https://www.youtube.com/watch?v=Oe5JPnVNhRo)

## Print  String Interpolation

# Print & String Interpolation

In Swift, `print()` is a function used to display values in the console, which helps debug and see the output of your code. String interpolation allows you to embed variables or expressions directly within a string. You do this by wrapping the variable or expression in parentheses preceded by a backslash: `\(variableName)`. This makes it easy to create dynamic strings that include the values of variables or the results of calculations.

Visit the following resources to learn more:

- [@official@Printing Constants and Variables](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/thebasics/#Printing-Constants-and-Variables)
- [@official@String Interpolation](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/stringsandcharacters#String-Interpolation)
- [@video@Introduction to Swift: String interpolation](https://www.youtube.com/watch?v=3-I43GvrzsA)

## Propagating

# Error Propagation

Error propagation in Swift is the process of passing an error up the call stack until it's handled by a `catch` block. When a function encounters an error it can't resolve, it `throws` the error. The calling function then has the responsibility to either handle the error using a `do-catch` block or to propagate the error further up the chain by also declaring that it `throws`. This continues until the error is caught and handled, preventing the program from crashing and allowing for graceful error recovery.

Visit the following resources to learn more:

- [@official@Propagating Errors Using Throwing Functions](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/errorhandling/#Propagating-Errors-Using-Throwing-Functions)
- [@article@Propagate Swift Errors Using Throwing Functions](https://www.kodeco.com/books/swift-cookbook/v1.0/chapters/2-propagate-swift-errors-using-throwing-functions)

## Properties

# Properties

Properties associate values with a particular class, structure, or enumeration. Stored properties store constant or variable values as part of an instance, whereas computed properties calculate (rather than store) a value. You can also define type properties, which are associated with the type itself, rather than with an instance of that type.

Visit the following resources to learn more:

- [@official@Properties](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/properties)
- [@article@Swift Properties](https://www.programiz.com/swift-programming/properties)
- [@video@Introduction to Swift: Properties](https://www.youtube.com/watch?v=AabqZodJ2xM&t=1s)
- [@video@How to compute property values dynamically – Swift for Complete Beginners](https://www.youtube.com/watch?v=UEvKhKviPRw)

## Protocols

# Protocols

A protocol in Swift defines a blueprint of methods, properties, and other requirements that suit a particular task or piece of functionality. Classes, structures, and enumerations can then adopt these protocols, providing concrete implementations for the requirements specified by the protocol. This allows you to define a common interface for different types, enabling polymorphism and code reusability.

Visit the following resources to learn more:

- [@official@Protocols](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/protocols/)
- [@article@Swift Protocols](https://www.programiz.com/swift-programming/protocols)
- [@article@The Power of Protocols in Swift](https://medium.com/@mumensh/the-power-of-protocols-in-swift-4cffcfa62ab1)
- [@video@Swift Protocols - An Introduction](https://www.youtube.com/watch?v=vmQnTMWaDiY)
- [@video@What is a Protocol in Swift and SwiftUI View protocol | Swift Basics #17](https://www.youtube.com/watch?v=nJmrkRlRu88)

## Realm

# Realm

Realm is a mobile database solution that offers a convenient and efficient way to store and manage data directly on a user's device. It's designed to be faster and easier to use than traditional databases like SQLite, providing a developer-friendly API for reading, writing, and querying data. Realm supports features like object relationships, data encryption, and real-time data synchronization, making it suitable for a wide range of mobile applications.

Visit the following resources to learn more:

- [@official@Realm](https://realm.netlify.app/)
- [@opensource@Realm Swift](https://github.com/realm/realm-swift)
- [@article@Integrating Realm Swift into Your iOS Projects: A Comprehensive Guide](https://bugfender.com/blog/realm-swift/)
- [@video@Swift Realm Tutorial: How to use a local realm database with SwiftUI - iOS Basics](https://www.youtube.com/watch?v=oCVsFsY3TvM)

## Repeatwhile

# Repeat...While Loop

The `repeat...while` loop in Swift executes a block of code at least once, and then continues to repeat the block as long as a specified condition is true.  Unlike the `while` loop, which checks the condition *before* executing the code, the `repeat...while` loop checks the condition *after* executing the code. This guarantees that the code block will always run at least once.

Visit the following resources to learn more:

- [@official@Repeat-while Loop](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/controlflow/#Repeat-While)
- [@video@Repeat loops – Swift in Sixty Seconds](https://www.youtube.com/watch?v=ROnXl0H45KE)

## Result Builders

# Result Builders

Result builders in Swift provide a way to build up data structures, like views in SwiftUI, using a sequence of statements. They essentially transform a series of expressions into a single value, often an array or a more complex data structure. This allows you to write more declarative and readable code, especially when dealing with complex view hierarchies or data transformations.

Visit the following resources to learn more:

- [@official@Result-Building Methods](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/attributes/#resultBuilder)
- [@article@Result builders](https://www.hackingwithswift.com/swift/5.4/result-builders)
- [@article@Result builders in Swift explained with code examples](https://www.avanderlee.com/swift/result-builders/)
- [@video@Result Builders in Action: Simplifying HTML Generation in Swift](https://www.youtube.com/watch?v=kZ7JPFUVv1w)
- [@video@WWDC21: Write a DSL in Swift using result builders | Apple](https://www.youtube.com/watch?v=JODl427Ff_0)

## Return Types

# Return Types

In Swift, a return type specifies the kind of data a function or closure sends back to the caller after it has finished executing. If a function performs a calculation or processes data, the return type indicates what type of result you can expect. If a function doesn't return any value, its return type is `Void`, often represented as `()`.

Visit the following resources to learn more:

- [@official@Functions with Multiple Return Values](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/functions/#Defining-and-Calling-Functions)
- [@article@Use Function Return Types in Swift](https://www.kodeco.com/books/swift-cookbook/v1.0/chapters/2-use-function-return-types-in-swift)
- [@video@How to use Functions in Swift | Swift Basics #5](http://youtube.com/watch?v=kr3SSplrJlw)

## Sdks For Wasm

# SDKs for WebAssembly (Wasm)

WebAssembly (Wasm) is a binary instruction format designed as a portable compilation target for programming languages, enabling high-performance applications on the web and other environments. SDKs for Wasm allow developers to compile Swift and Swift UI code into Wasm, making it possible to run Swift applications in web browsers or other Wasm-compatible environments, effectively extending the reach of Swift beyond Apple's platforms.

Visit the following resources to learn more:

- [@article@Getting Started with Swift SDKs for WebAssembly](https://www.swift.org/documentation/articles/wasm-getting-started.html)

## Semicolons

# Semicolons in Swift

Semicolons (`;`) are used in Swift to separate multiple statements on a single line. While Swift doesn't require semicolons at the end of each statement like some other languages, they are necessary when you want to write more than one statement on the same line of code. Otherwise, Swift infers the end of a statement based on the line break.

Visit the following resources to learn more:

- [@official@Semicolons](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/thebasics/#Semicolons)

## Server Frameworks

# Server Frameworks

Server frameworks provide the tools and structure needed to build backend applications, APIs, and web services. They handle tasks like routing requests, managing data, and interacting with databases, allowing developers to focus on the core logic of their server-side applications. These frameworks enable Swift developers to create robust and scalable server-side solutions, complementing the client-side capabilities of Swift and SwiftUI.

## State

# @State

`@State` is a property wrapper in SwiftUI that allows you to manage the state of a view. It's used to store values that can change over time and trigger updates to the view when they do. When a property is marked with `@State`, SwiftUI automatically manages the storage and ensures that the view is re-rendered whenever the value changes, reflecting the updated data in the user interface.

Visit the following resources to learn more:

- [@official@@State](https://developer.apple.com/documentation/swiftui/state)
- [@official@Managing user interface state](https://developer.apple.com/documentation/swiftui/managing-user-interface-state)
- [@article@What is the @State property wrapper?](https://www.hackingwithswift.com/quick-start/swiftui/what-is-the-state-property-wrapper)
- [@video@SwiftUI - @State Property Wrapper Explained](https://www.youtube.com/watch?v=48JYBb5yJ0s)

## Stateobject

# @StateObject

`@StateObject` is a property wrapper used to manage the lifecycle of reference type objects (classes) that hold state for a view. It ensures that the object is created only once when the view appears and persists across view updates, preventing the object from being re-initialized every time the view redraws. This is particularly useful for managing data that needs to be shared and maintained within a specific view's scope.

Visit the following resources to learn more:

- [@official@StateObject](https://developer.apple.com/documentation/swiftui/stateobject)
- [@article@What is the @StateObject property wrapper?](https://www.hackingwithswift.com/quick-start/swiftui/what-is-the-stateobject-property-wrapper)
- [@article@SwiftUI: StateObject x ObservedObject, when to use each one](https://pedroalvarez-29395.medium.com/swiftui-stateobject-x-observedobject-when-to-use-each-one-f738eb57ba6e)
- [@video@DON'T Make this MISTAKE || StateObject vs ObservedObject | What's the Difference?](https://www.youtube.com/watch?v=RvzJLekIjRs)

## Static Linux Sdk

# Static Linux SDK

A Static Linux SDK allows you to compile Swift code into standalone executables that can run on Linux systems without requiring a full Swift runtime environment to be installed. This is achieved by bundling all necessary Swift libraries and dependencies directly into the executable file, making it self-contained and portable. This approach simplifies deployment and reduces dependency conflicts, as the application carries everything it needs to run.

Visit the following resources to learn more:

- [@official@Getting Started withStatic Linux SDK](https://www.swift.org/documentation/articles/static-linux-getting-started.html)

## Stored

# Stored Properties

Stored properties are variables or constants that are part of a structure or class. They hold data directly within an instance of that structure or class.  Think of them as the "things" an object *has*.  You define them with `var` for variables (values that can change) and `let` for constants (values that cannot change after initialization).

Visit the following resources to learn more:

- [@official@Stored Properties](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/properties#Stored-Properties)
- [@video@How to compute property values dynamically – Swift for Complete Beginners](https://www.youtube.com/watch?v=UEvKhKviPRw)

## Strict Concurrency Checking

# Strict Concurrency Checking

Strict concurrency checking is a feature that helps you write safer and more reliable concurrent code. It detects potential data races and other concurrency-related issues at compile time, preventing unexpected behavior and crashes when your app runs. By enforcing rules about how data can be accessed from different threads, it ensures that your concurrent code is predictable and avoids common pitfalls like simultaneous modification of shared resources.

Visit the following resources to learn more:

- [@official@Updating an app to use strict concurrency](https://developer.apple.com/documentation/Swift/updating-an-app-to-use-strict-concurrency)
- [@official@Adopting strict concurrency in Swift 6 apps](https://developer.apple.com/documentation/swift/adoptingswift6)
- [@article@Understanding the New Swift 6 Concurrency Features](https://medium.com/@nimjea/understanding-the-new-swift-6-concurrency-features-3bff267426cc)
- [@video@Swift concurrency: Update a sample app](https://developer.apple.com/videos/play/wwdc2021/10194/)

## Strings

# Strings in Swift

In Swift, a string is a sequence of characters, like letters, numbers, and symbols. It's a fundamental data type used to represent text. You can create strings using string literals (text enclosed in double quotes) or by combining other strings and values. Strings in Swift are Unicode-compliant, meaning they can represent characters from various languages.

Visit the following resources to learn more:

- [@official@Strings and Characters](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/stringsandcharacters/)
- [@article@Working with Strings in Swift: A Developer’s Handbook](https://vikramios.medium.com/strings-in-swift-76a21b4268c6)
- [@video@Working with strings in Swift – Swift Strings, part 3](https://www.youtube.com/watch?v=AthqAjYhZLw)

## Structures  Classes

# Structures & Classes

Structures and classes are fundamental building blocks in Swift for creating custom data types. They allow you to group related variables (properties) and functions (methods) into a single, reusable unit. Structures are value types, meaning they are copied when passed around, while classes are reference types, meaning they share a single instance in memory. This difference impacts how data is modified and shared within your application.

Visit the following resources to learn more:

- [@official@Structures & Classes](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/classesandstructures)
- [@official@Choosing Between Structures and Classes](https://developer.apple.com/documentation/swift/choosing-between-structures-and-classes)
- [@article@Class vs Struct in swift](https://medium.com/@muhammad.cse11/class-vs-struct-in-swift-dcc7ad6f5a99)
- [@video@Introduction to Swift: Structs](https://www.youtube.com/watch?v=d13uCPrmEXM)
- [@video@Introduction to Swift: Classes](https://www.youtube.com/watch?v=s_x49coTM4g)
- [@video@Swift - Class vs. Struct Explained](https://www.youtube.com/watch?v=LtlbB4-6k_U)

## Subscripts

# Subscripts

Subscripts are shortcuts for accessing elements within a collection, list, or sequence. They allow you to query instances of a type by writing one or more values in square brackets after the instance name. You can define subscripts on classes, structures, and enumerations, and they can take a single parameter or multiple parameters of any type. Subscripts make it possible to access and set values using a familiar syntax, similar to how you access elements in an array or dictionary.

Visit the following resources to learn more:

- [@official@Subscripts](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/subscripts/)
- [@article@Swift - Subscripts](https://medium.com/@jaisingh.darshana/understanding-subscripts-in-swift-and-the-need-for-safe-subscripts-c1c306ed8083)
- [@article@Custom subscripts in Swift explained with code examples](https://www.avanderlee.com/swift/custom-subscripts/)
- [@video@How to use Subscripts in Swift | Advanced Learning #32](https://www.youtube.com/watch?v=hiOjTJgl6GU)

## Swift Charts

# Swift Charts

Swift Charts is a framework within Swift that allows you to create a variety of visually appealing and informative charts directly in your applications. It provides a declarative syntax for defining chart types, data sources, and visual customizations, making it easier to represent data clearly and understandably. With Swift Charts, you can build charts like bar charts, line charts, scatter plots, and more, all while leveraging the power and flexibility of the Swift language and SwiftUI.

Visit the following resources to learn more:

- [@official@Swift Charts](https://developer.apple.com/documentation/charts)
- [@official@Creating a chart using Swift Charts](https://developer.apple.com/documentation/charts/creating-a-chart-using-swift-charts)
- [@video@Hello Swift Charts](https://developer.apple.com/videos/play/wwdc2022/10136/)

## Swift For Server Apps

# Swift for Server Apps

Swift isn't just for iOS and macOS apps; it can also be used to build server-side applications. This allows developers to use their existing Swift knowledge to create backends, APIs, and other server-side components, potentially leading to more efficient development workflows and code sharing between client and server. Frameworks like Vapor and Kitura provide the necessary tools and libraries to build robust and scalable server applications using Swift.

Visit the following resources to learn more:

- [@official@Swift on Server](https://www.swift.org/documentation/server/)

## Swift Log

# Swift-Log

`swift-log` is a logging API for Swift that provides a standardized way to record messages from your code. It allows you to capture information about your application's behavior, errors, and performance, making it easier to diagnose issues and understand how your code is running. With `swift-log`, you can configure different logging levels (such as debug, info, warning, and error) and direct the output to various destinations, including the console, files, or external logging services.

Visit the following resources to learn more:

- [@official@swift-log](https://github.com/apple/swift-log)
- [@official@Log Levels](https://www.swift.org/documentation/server/guides/libraries/log-levels.html)
- [@official@Generating Log Messages from Your Code](https://developer.apple.com/documentation/os/generating-log-messages-from-your-code)

## Swift Nio

# SwiftNIO

SwiftNIO is a low-level, cross-platform asynchronous event-driven network application framework. It enables the development of high-performance protocol servers and clients in Swift. It provides building blocks for handling network connections, data transfer, and event processing without blocking the main thread, making it suitable for applications requiring scalability and responsiveness.

Visit the following resources to learn more:

- [@opensource@swift-nio](https://github.com/apple/swift-nio)
- [@article@SwiftNIO Fundamentals](https://swiftonserver.com/using-swiftnio-fundamentals/)
- [@video@Swift NIO MUD tutorial](https://www.youtube.com/watch?v=-xVrOwNLPTg&list=PLhUrOtMlcKDAa0_WYh_J4vQ6Lzw0DvLLK)

## Swift Package Index

# Swift Package Index

The Swift Package Index is a comprehensive catalog and search engine for Swift packages. It allows developers to discover, explore, and evaluate Swift packages that can be integrated into their projects. It provides information about package compatibility, documentation, and other relevant details, making it easier to find and use open-source Swift libraries.

Visit the following resources to learn more:

- [@official@Swift Package Index](https://swiftpackageindex.com/)
- [@video@Swift Package Index - How To Use It](https://www.youtube.com/watch?v=ePzGOuvjlpI)

## Swift Package Manager

# Swift Package Manager

The Swift Package Manager is a tool for managing dependencies in your Swift projects. It automates the process of downloading, building, and linking external libraries and frameworks into your code. This allows you to easily reuse code written by others and share your own code with the Swift community, promoting modularity and code reuse.

Visit the following resources to learn more:

- [@official@Swift Package Manager](https://docs.swift.org/swiftpm/documentation/packagemanagerdocs/)
- [@opensource@swift-package-manager](https://github.com/swiftlang/swift-package-manager)
- [@article@Mastering Swift Package Manager: A Comprehensive Guide](https://medium.com/@dipenapanchasara/mastering-swift-package-manager-a-comprehensive-guide-5e06f29d812d)

## Swift Playgrounds

# Swift Playgrounds

Swift Playgrounds is an Apple application designed to teach coding in a fun and interactive way. It uses a game-like environment where users learn Swift programming concepts by solving puzzles and completing challenges. It's available on iPad and Mac, making it accessible for beginners and experienced programmers alike to experiment with Swift and build interactive projects.

Visit the following resources to learn more:

- [@official@Learn to code with Swift Playground](https://www.apple.com/swift/playgrounds/)
- [@video@Swift Playgrounds- Boxed In Tutorial](https://www.youtube.com/watch?v=0gC0kcg0_jM)

## Swift Testing

# Swift Testing

The Swift Testing library allows you to leverage the powerful and expressive capabilities of the Swift programming language to develop tests with more confidence and less code. The library integrates seamlessly with Swift Package Manager testing workflow, supports flexible test organization, customizable metadata, and scalable test execution.

Visit the following resources to learn more:

- [@official@Swift Testing](https://developer.apple.com/documentation/testing)
- [@official@Swift Testing](https://developer.apple.com/xcode/swift-testing/)
- [@opensource@swift-testing](https://github.com/swiftlang/swift-testing)
- [@article@Swift Testing: Writing a Modern Unit Tests](https://www.avanderlee.com/swift-testing/modern-unit-test/)
- [@video@WWDC24: Meet Swift Testing | Apple](https://www.youtube.com/watch?v=WFnkNcvLnCI)
- [@video@Getting Started with Unit Testing for iOS Development in Swift | Xcode 16](https://www.youtube.com/watch?v=CsuUwdoVwyw)

## Swift Vs Objective C

# Swift vs. Objective-C

Swift and Objective-C are both programming languages used to develop applications for Apple's operating systems (iOS, macOS, watchOS, tvOS). Objective-C is an older language, built as an extension of C, while Swift is a more modern language designed to be safer, faster, and easier to learn. Swift offers features like type safety, optionals, and a more concise syntax, making it a preferred choice for new Apple platform development.

Visit the following resources to learn more:

- [@article@Objective-C vs Swift: iOS Comparison [2025 Update]](https://www.netguru.com/blog/objective-c-vs-swift)
- [@article@Swift and Objective-C: An In-Depth Comparison of iOS Programming Languages](https://shakuro.com/blog/swift-vs-objective-c)

## Swiftdata

# SwiftData

SwiftData is Apple's modern framework for managing an app's data model and persisting data locally. It provides a declarative and type-safe way to define your data schema, interact with the underlying storage (typically SQLite), and manage relationships between different data entities. SwiftData integrates seamlessly with SwiftUI, making it easy to fetch, display, and modify data directly within your user interface.

Visit the following resources to learn more:

- [@official@SwiftData](https://developer.apple.com/documentation/swiftdata)
- [@article@SwiftData by Example](https://www.hackingwithswift.com/quick-start/swiftdata)
- [@video@SwiftData Basics in 15 minutes](https://www.youtube.com/watch?v=krRkm8w22A8)

## Swiftui Inspector

# SwiftUI Inspector

The SwiftUI Inspector is a built-in tool within Xcode that allows developers to examine and modify the properties of SwiftUI views in real-time while an app is running, either in the simulator or on a physical device. It provides a visual interface to inspect the view hierarchy, adjust attributes like colors, fonts, and layout constraints, and immediately see the changes reflected in the app's UI, facilitating rapid prototyping and debugging.

Visit the following resources to learn more:

- [@official@inspector](https://developer.apple.com/documentation/SwiftUI/View/inspector(isPresented:content:))
- [@article@How to add an inspector to any view](https://www.hackingwithswift.com/quick-start/swiftui/how-to-add-an-inspector-to-any-view)
- [@article@Presenting an Inspector with SwiftUI](https://www.createwithswift.com/presenting-an-inspector-with-swiftui/)
- [@video@Inspectors in SwiftUI: Discover the details](https://www.youtube.com/watch?v=l0ksmCylJRc)

## Swiftui With Asyncawait

# SwiftUI with Async/Await

Async/Await is a programming paradigm that simplifies asynchronous code, making it easier to read and manage. In SwiftUI, it allows you to perform long-running tasks, like network requests or data processing, without blocking the main thread, ensuring your app remains responsive. This approach replaces traditional completion handlers with a more sequential and cleaner syntax, improving code readability and reducing complexity when dealing with asynchronous operations in your SwiftUI applications.

Visit the following resources to learn more:

- [@official@Defining and Calling Asynchronous Functions](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/concurrency/#Defining-and-Calling-Asynchronous-Functions)
- [@official@Updating an App to Use Swift Concurrency](https://developer.apple.com/documentation/swift/updating_an_app_to_use_swift_concurrency)
- [@article@Async await in Swift explained with code examples](https://www.avanderlee.com/swift/async-await/)
- [@article@Async await](https://www.hackingwithswift.com/swift/5.5/async-await)
- [@article@Async/await in Swift and SwiftUI](https://dev.to/matteom/asyncawait-in-swift-and-swiftui-2b8n)

## Switch  Case

# Switch/Case Statements

A `switch` statement allows you to control which block of code is executed based on the value of a variable or expression. It compares the value against several possible cases, and executes the code associated with the first matching case. Unlike some other languages, Swift's `switch` statements don't require a `break` statement after each case; execution automatically stops after the code for a matching case is run.

Visit the following resources to learn more:

- [@official@Switch](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/controlflow/#Switch)
- [@video@How to use switch statements to check multiple conditions – Swift for Complete Beginners](https://www.youtube.com/watch?v=cDpJy4Y7OYE)

## Tabview

# TabView

TabView allows you to create an interface with multiple distinct views, each accessible through a tab bar at the bottom (or top, depending on the platform). It's a container view that manages a collection of child views, presenting one at a time based on the user's tab selection. Each tab can be associated with an image and text label, providing a clear and intuitive way for users to navigate between different sections of your app.

Visit the following resources to learn more:

- [@official@TabView](https://developer.apple.com/documentation/swiftui/tabview)
- [@official@Enhancing your app’s content with tab navigation](https://developer.apple.com/documentation/swiftui/enhancing-your-app-content-with-tab-navigation)
- [@article@SwiftUI TabView: Explained with Code Examples](https://www.avanderlee.com/swiftui/tabview-tabbed-views/)
- [@video@SwiftUI TabView Tutorial](https://www.youtube.com/watch?v=JqQQozkFeJU)

## Tasks  Task Groups

# Tasks & Task Groups

Tasks in Swift's concurrency model represent units of work that can be executed concurrently. Task Groups allow you to create and manage collections of child tasks, enabling you to perform parallel operations and aggregate their results. This provides a structured way to break down complex operations into smaller, manageable, and concurrent units, improving performance and responsiveness in your applications.

Visit the following resources to learn more:

- [@official@Tasks & Task Groups](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/concurrency/#Tasks-and-Task-Groups)
- [@article@What are tasks and task groups?](https://www.hackingwithswift.com/quick-start/concurrency/what-are-tasks-and-task-groups)
- [@article@How to create a task group and add tasks to it](https://www.hackingwithswift.com/quick-start/concurrency/how-to-create-a-task-group-and-add-tasks-to-it)
- [@article@Task Groups in Swift explained with code examples](https://www.avanderlee.com/concurrency/task-groups-in-swift/)
- [@video@How to use Task and .task in Swift | Swift Concurrency #4](https://www.youtube.com/watch?v=fTtaEYo14jI)
- [@video@How to use TaskGroup to perform concurrent Tasks in Swift | Swift Concurrency #6](https://www.youtube.com/watch?v=epBbbysk5cU)

## Testing

# Testing

Testing involves writing code to verify that your app functions correctly automatically. This includes checking individual units of code (unit tests), ensuring different parts of your app work together seamlessly (integration tests), and validating the overall user experience (UI tests). By writing tests, you can catch bugs early, prevent regressions, and ensure the reliability of your application.

## Text

# Text

`Text` is a fundamental view used to display static, read-only text on the screen. It allows you to present strings, apply formatting like fonts, colors, and styles, and handle localization for different languages. You can use `Text` to create labels, descriptions, headings, and any other textual content within your app's user interface.

Visit the following resources to learn more:

- [@official@Text](https://developer.apple.com/documentation/swiftui/text)
- [@article@How to style text views with fonts, colors, line spacing, and more](https://www.hackingwithswift.com/quick-start/swiftui/how-to-style-text-views-with-fonts-colors-line-spacing-and-more)
- [@article@Creating a SwiftUI text view with tappable links](https://danielsaidi.com/blog/2024/12/18/creating-a-swiftui-text-view-with-tappable-links)
- [@video@Styling SwiftUI Text Views](https://www.youtube.com/watch?v=rbtIcKKxQ38)

## Throwing

# Throwing Errors in Swift

Throwing errors allows you to signal that something unexpected or problematic has occurred during the execution of your code. When a function encounters a situation it can't handle normally, it can `throw` an error. This error is then passed up the call stack until it's `caught` and handled by an appropriate error handling mechanism, preventing the program from crashing and allowing for graceful recovery or reporting of the issue.

Visit the following resources to learn more:

- [@official@Throwing Errors](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/errorhandling/#Representing-and-Throwing-Errors)
- [@article@Error handling in Swift](https://blorenzop.medium.com/error-handling-in-swift-f9ca87490e26)

## Trailing Closures

# Trailing Closures

A trailing closure is a closure that's written after the function's parentheses. If a function's last parameter is a closure, you can pass the closure outside of the parentheses when you call the function. This syntax makes the code more readable, especially when the closure is long and complex. It's a syntactic sugar that simplifies how you pass closures as arguments to functions.

Visit the following resources to learn more:

- [@official@Trailing Closures](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/closures#Trailing-Closures)
- [@video@Trailing closure syntax](https://www.hackingwithswift.com/sixty/6/5/trailing-closure-syntax)

## Transitions

# Transitions

Transitions define how views appear and disappear from the screen. They control the visual effects applied during these changes, allowing you to create smooth and engaging user experiences. You can customize transitions to include effects like fading, sliding, scaling, or even more complex animations, making your app feel polished and responsive.

Visit the following resources to learn more:

- [@official@Transition](https://developer.apple.com/documentation/swiftui/transition)
- [@official@Animating views and transitions](https://developer.apple.com/tutorials/swiftui/animating-views-and-transitions)
- [@article@Creating view transitions in SwiftUI](https://www.createwithswift.com/creating-view-transitions-in-swiftui/)
- [@article@How to add and remove views with a transition](https://www.hackingwithswift.com/quick-start/swiftui/how-to-add-and-remove-views-with-a-transition)
- [@video@How to use Transition in SwiftUI | Bootcamp #27](https://www.youtube.com/watch?v=X6FAIa0nJoA)

## Tuples

# Tuples in Swift

Tuples in Swift are a way to group multiple values into a single compound value. Unlike arrays, the values within a tuple can be of different types. You define a tuple by enclosing the values within parentheses, separated by commas. For example, `(1, "hello", true)` is a tuple containing an integer, a string, and a boolean. You can access the individual values in a tuple either by their position (starting from 0) or by naming the elements when you define the tuple.

Visit the following resources to learn more:

- [@official@Tuples](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/thebasics/#Tuples)
- [@video@How to use Tuples in Swift | Swift Basics](https://www.youtube.com/watch?v=zsjCrtENsZA)

## Type Annotations

# Type Annotations

Type annotations in Swift are a way to explicitly specify the type of a variable or constant.  Instead of letting Swift infer the type based on the initial value, you tell the compiler exactly what kind of data the variable will hold, such as an `Int`, `String`, or `Bool`. This provides clarity and can help catch errors during compilation.

Visit the following resources to learn more:

- [@article@Type Annotations](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/thebasics/#Type-Annotations)
- [@video@How to use type annotations – Swift for Complete Beginners](https://www.youtube.com/watch?v=_FX8xCBmbeA)

## Type Casting

# Type Casting

Type casting is a way to check the type of an instance, or to treat that instance as if it were a different superclass or subclass from somewhere else in its own class hierarchy. It's essentially a way to access an object as a different type than it was originally declared to be. Swift provides `is` and `as` operators to perform type checking and casting, allowing you to safely work with different types at runtime.

Visit the following resources to learn more:

- [@official@Type Casting](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/typecasting/)
- [@article@Type Casting in Swift](https://medium.com/@talhasaygili/type-casting-in-swift-f42102ea5700)
- [@article@What is Type Casting in Swift?](https://www.tutorialspoint.com/swift/swift_type_casting.htm)

## Type Inference

# Type Inference

Type inference is a feature in Swift that allows the compiler to automatically deduce the data type of a variable or constant based on the value assigned to it. This means you don't always have to explicitly declare the type when creating variables; Swift can figure it out for you, making your code cleaner and more concise.

Visit the following resources to learn more:

- [@course@Type Inference](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/thebasics/#Type-Safety-and-Type-Inference)
- [@video@#10 Swift Programming - Clear Clean Code Using Type Safety and Inference](https://www.youtube.com/watch?v=bgtU62Mkj0A)

## Type Safety

# Type Safety in Swift

Thanks to type safety, Swift prevents you from accidentally using a value in a way that's not intended. Swift checks the types of your variables and constants during compilation. If you try to assign a value of the wrong type to a variable (like assigning a string to an integer variable), Swift will give you an error. This helps catch mistakes early, making your code more reliable and preventing unexpected behavior at runtime.

Visit the following resources to learn more:

- [@official@Type Safety](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/thebasics/#Type-Safety-and-Type-Inference)
- [@article@Understanding Type Safety and Type Inference in Swift](https://medium.com/@akshitsharma904/understanding-type-safety-and-type-inference-in-swift-bcf84ae273e9)
- [@video@Swift Programming - Clear Clean Code Using Type Safety and Inference](https://www.youtube.com/watch?v=bgtU62Mkj0A)

## Ui Controls

# UI Controls

UI Controls are the visual building blocks that users interact with in an app's interface. These elements, such as buttons, text fields, sliders, and switches, allow users to input data, trigger actions, and navigate through the application. They provide a way for the user to communicate with the app and for the app to respond accordingly.

Visit the following resources to learn more:

- [@official@Controls and indicators](https://developer.apple.com/documentation/swiftui/controls-and-indicators)
- [@official@Working with UI controls](https://developer.apple.com/tutorials/swiftui/working-with-ui-controls)
- [@official@Populating SwiftUI menus with adaptive controls](https://developer.apple.com/documentation/swiftui/populating-swiftui-menus-with-adaptive-controls)
- [@official@Button](https://developer.apple.com/documentation/swiftui/button)
- [@official@Toggle](https://developer.apple.com/documentation/swiftui/toggle)
- [@official@Slider](https://developer.apple.com/documentation/swiftui/slider)
- [@official@Divider](https://developer.apple.com/documentation/swiftui/divider)
- [@article@SwiftUI - UI Controls](https://developer.apple.com/documentation/swiftui/controls-and-indicators)

## Uikit Vs Swiftui

# UIKit vs. SwiftUI

UIKit and SwiftUI are both frameworks for building user interfaces on Apple platforms (iOS, iPadOS, macOS, watchOS, and tvOS). UIKit is the older, imperative framework that has been around since the first iPhone was introduced. SwiftUI is a newer, declarative framework introduced in 2019 that offers a more modern and concise way to design and develop user interfaces. The key difference lies in how you describe the UI: UIKit uses code to directly manipulate views, while SwiftUI describes the desired state of the UI, and the system handles the updates.

Visit the following resources to learn more:

- [@official@UIKit](https://developer.apple.com/documentation/uikit)
- [@article@Answering the big question: should you learn SwiftUI, UIKit, or both?](https://www.hackingwithswift.com/quick-start/swiftui/answering-the-big-question-should-you-learn-swiftui-uikit-or-both)
- [@article@What Really Are The Differences Between SwiftUI and UIKit?](https://dev.to/raphacmartin/what-really-are-the-differences-between-swiftui-and-uikit-1o2j)
- [@video@Should I Learn SwiftUI or UIKit?](https://www.youtube.com/watch?v=HIiVxbEbK1s)

## Unstructured Concurrency

# Unstructured Concurrency

Unstructured concurrency in Swift allows you to create and manage concurrent tasks without adhering to a strict parent-child relationship. This means you can launch asynchronous operations independently, and their lifecycles are not necessarily tied to the scope in which they were created. It provides flexibility in managing concurrency but requires careful handling to avoid issues like resource leaks or unexpected behavior.

Visit the following resources to learn more:

- [@official@Unstructured Concurrency](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/concurrency#Unstructured-Concurrency)
- [@article@Understanding unstructured and detached tasks in Swift](https://www.donnywals.com/understanding-unstructured-and-detached-tasks-in-swift/)
- [@article@Unstructured vs Structured Concurrency in Swift](https://medium.com/@moutamanuel26/unstructured-vs-structured-concurrency-in-swift-dc5ed50eb1f1)

## User Interaction

# User Interaction

User interaction refers to how users engage with your app. This includes everything from tapping buttons and entering text to swiping through lists and responding to alerts. It's about making your app responsive and intuitive, so users can easily navigate and accomplish their goals. SwiftUI provides various tools and modifiers to handle user input and create interactive elements.

## Userdefaults Appstorage

# UserDefaults & AppStorage

UserDefaults and AppStorage are mechanisms in Swift and SwiftUI for storing small amounts of data persistently on a user's device. UserDefaults is a traditional way to store simple data types like strings, numbers, and booleans, using key-value pairs. AppStorage, built on top of UserDefaults, provides a more SwiftUI-friendly way to bind data directly to UI elements, automatically saving and loading values as the user interacts with the app.

Visit the following resources to learn more:

- [@official@UserDefaults](https://developer.apple.com/documentation/foundation/userdefaults)
- [@article@User Defaults reading and writing in Swift](https://www.avanderlee.com/swift/user-defaults-preferences/)
- [@video@Storing user settings with UserDefaults](https://www.hackingwithswift.com/books/ios-swiftui/storing-user-settings-with-userdefaults)
- [@official@AppStorage](https://developer.apple.com/documentation/swiftui/appstorage)
- [@article@What is the @AppStorage property wrapper?](https://www.hackingwithswift.com/quick-start/swiftui/what-is-the-appstorage-property-wrapper)
- [@article@@AppStorage explained and replicated for a better alternative](https://www.avanderlee.com/swift/appstorage-explained/)
- [@video@How to use @AppStorage in SwiftUI | Bootcamp #52](https://www.youtube.com/watch?v=zyuSUrfelw8)

## Using Packages

# Using Packages

Swift Package Manager lets you add external libraries and tools to your Swift projects. Using packages involves declaring dependencies in your `Package.swift` file, which tells Swift Package Manager where to find the code you want to use. Once declared, Swift Package Manager handles downloading, building, and linking the package into your project, making the functionality available for you to use in your code.

Visit the following resources to learn more:

- [@official@Swift packages](https://developer.apple.com/documentation/xcode/swift-packages)
- [@official@Introducing Packages](https://docs.swift.org/swiftpm/documentation/packagemanagerdocs/introducingpackages)
- [@video@Adding Swift package dependencies in Xcode](https://www.hackingwithswift.com/books/ios-swiftui/adding-swift-package-dependencies-in-xcode)
- [@video@How to use Third Party Swift Packages in SwiftUI | Swift Packages #0](https://www.youtube.com/watch?v=yp9n5oYONDs)

## Vapor

# Vapor

Vapor is an open-source web framework written in Swift that allows developers to build robust and scalable server-side applications, APIs, and websites. It provides a clean and expressive syntax, making it easier to handle tasks like routing, database interaction, and templating, all while leveraging the performance and safety features of the Swift language.

Visit the following resources to learn more:

- [@opensource@Vapor](https://github.com/vapor/vapor)
- [@official@Vapor](https://vapor.codes/)
- [@official@Build a Web Service with Vapor](https://www.swift.org/getting-started/vapor-web-server/)
- [@video@Getting Started with Vapor 4](https://www.youtube.com/watch?v=CD283bLteP0&list=PLMRqhzcHGw1Z7xNnqS_yUNm1k9dvq-HbM&index=1)

## Viewbuilder

# ViewBuilder

`ViewBuilder` is a result builder attribute in Swift that allows you to build complex views in a declarative and concise way. It essentially transforms a series of statements into a single view, automatically handling the logic of combining multiple views together. This is particularly useful when creating custom views or complex layouts where you need to conditionally display different content based on certain conditions.

Visit the following resources to learn more:

- [@official@ViewBuilder](https://developer.apple.com/documentation/swiftui/viewbuilder)
- [@official@Declaring a custom view](https://developer.apple.com/documentation/swiftui/declaring-a-custom-view)
- [@article@Tips and tricks for when using SwiftUI’s ViewBuilder](https://www.swiftbysundell.com/articles/swiftui-viewbuilder-tips-and-tricks/)
- [@video@How to use @ViewBuilder in SwiftUI | Advanced Learning](https://www.youtube.com/watch?v=pXmBRK1BjLw)

## Views

# Views

In Swift and SwiftUI, a View is a fundamental building block for creating user interfaces. It represents a rectangular area on the screen that displays content and responds to user interactions. Views can be simple, like a text label or an image, or complex, composed of multiple nested views arranged in a hierarchy to create intricate layouts. They are the core components you use to design and structure the visual elements of your app.

Visit the following resources to learn more:

- [@official@View fundamentals](https://developer.apple.com/documentation/swiftui/view-fundamentals)
- [@official@View](https://developer.apple.com/documentation/swiftui/view)
- [@official@Creating and combining views Tuttorial](https://developer.apple.com/tutorials/swiftui/creating-and-combining-views)
- [@video@5 SwiftUI Concepts Every Beginning SwiftUI Developer Needs To Know (2020)](https://www.youtube.com/watch?v=51xIHDm_BDs)

## Vscode

# VSCode

VSCode (Visual Studio Code) is a free and popular source code editor developed by Microsoft. It's known for its lightweight design, extensive customization options through extensions, and robust support for various programming languages, including Swift.  It provides features like syntax highlighting, debugging, an integrated terminal, and Git integration, making it a versatile tool for software development.

Visit the following resources to learn more:

- [@official@Configuring VS Code for Swift Development](https://www.swift.org/documentation/articles/getting-started-with-vscode-swift.html)
- [@article@How to Set Up VS Code for iOS Development (Full Guide with Tips)](https://www.youtube.com/watch?v=eUizIb2_vaM)

## Vstack

# VStack

A `VStack` is a layout container that arranges its child views in a vertical line. It's like stacking building blocks on top of each other. You can use it to group related UI elements, such as text labels, images, and buttons, so they appear one above the other on the screen. `VStack` automatically manages the positioning and sizing of its children within the vertical stack.

Visit the following resources to learn more:

- [@official@VStack](https://developer.apple.com/documentation/swiftui/vstack)
- [@official@Building layouts with stack views](https://developer.apple.com/documentation/swiftui/building-layouts-with-stack-views)
- [@article@VStack](https://www.swiftuifieldguide.com/layout/vstack/)
- [@video@VStack, HStack, and ZStack in SwiftUI | Bootcamp](https://www.youtube.com/watch?v=pv-vbUEzimk)

## What Is Swift

# What is Swift?

Swift is a modern, general-purpose programming language developed by Apple. It's designed to be safe, fast, and expressive, making it a great choice for building applications across Apple's platforms, including iOS, macOS, watchOS, and tvOS. Swift combines the best aspects of C and Objective-C without the constraints of C compatibility.

Visit the following resources to learn more:

- [@official@Swift Docs](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/aboutswift)
- [@official@Swift](https://developer.apple.com/swift/)
- [@course@Learn Swift | Codeacademy](https://www.codecademy.com/learn/learn-swift)
- [@video@Swift Programming Tutorial – Full Course for Beginners](https://www.youtube.com/watch?v=8Xg7E9shq0U)

## What Is Swiftui

# SwiftUI

SwiftUI is a declarative UI framework from Apple that allows developers to build user interfaces across all Apple platforms (iOS, macOS, watchOS, tvOS, and visionOS) using Swift code. Instead of imperatively defining UI elements and their behavior, you describe the desired state of your UI, and SwiftUI automatically handles the rendering and updates. This approach simplifies UI development, promotes code reuse, and enables features such as live previews and hot reloading.

Visit the following resources to learn more:

- [@official@SwiftUI](https://developer.apple.com/swiftui/)
- [@official@SwiftUI essentials](https://developer.apple.com/videos/play/wwdc2024/10150/)
- [@official@SwiftUI Docs](https://developer.apple.com/documentation/swiftui)
- [@video@SwiftUI Fundamentals | FULL COURSE | Beginner Friendly](https://www.youtube.com/watch?v=b1oC7sLIgpI)
- [@video@Learn SwiftUI online for FREE | Bootcamp #0](https://www.youtube.com/watch?v=-Yp0LS61Nxk&list=PLwvDm4VfkdphqETTBf-DdjCoAvhai1QpO)

## Where Swift Is Used

# Where Swift is Used

Swift is a versatile programming language developed by Apple, primarily known for building applications across the Apple ecosystem. This includes creating apps for iPhones, iPads, Macs, Apple Watches, and Apple TVs. Beyond Apple platforms, Swift can also be used for server-side development, command-line tools, and even some embedded systems, making it a language with a growing range of applications.

Visit the following resources to learn more:

- [@official@Develop for iOS](https://developer.apple.com/ios/)
- [@official@Develop for macOS](https://developer.apple.com/macos/)
- [@official@Swift on the Server](https://www.swift.org/documentation/server/)
- [@article@What You Can Do with Swift Outside the Apple Ecosystem](https://arc-sosangyo.medium.com/what-you-can-do-with-swift-outside-the-apple-ecosystem-a201778a7830)

## While

# While Loops in Swift

A `while` loop in Swift repeatedly executes a block of code as long as a specified condition is true. The loop checks the condition before each execution of the code block. If the condition is initially false, the code block is never executed. This makes it suitable for situations where you want to repeat a task until a certain condition is met.

Visit the following resources to learn more:

- [@official@While Loops](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/controlflow/#While-Loops)
- [@video@How to use a while loop to repeat work – Swift for Complete Beginners](https://www.youtube.com/watch?v=NduMuU0xeqk)

## Why Use Swift

# Why Use Swift?

Swift is a modern, powerful, and intuitive programming language developed by Apple. It's designed to be safe, fast, and expressive, making it an excellent choice for building applications across Apple's ecosystems, including iOS, macOS, watchOS, and tvOS. Its clean syntax and focus on developer productivity contribute to a more efficient and enjoyable development experience.

Visit the following resources to learn more:

- [@official@About Swift](https://www.swift.org/about/)
- [@article@Programming in Swift: Benefits of This Popular Coding Language](https://www.coursera.org/articles/programming-in-swift)
- [@video@Why learn Swift – Swift for Complete Beginners](https://www.youtube.com/watch?v=ug6T-iFk5OY)

## Wrappers

# Property Wrappers

Property wrappers in Swift provide a way to add a layer of code between the property and the code that manages it. They essentially encapsulate code that gets executed when a property is accessed or modified. This allows you to reuse the same property logic across multiple properties, such as enforcing constraints, managing data storage, or providing thread safety.

Visit the following resources to learn more:

- [@article@Property Wrappers](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/properties#Property-Wrappers)
- [@article@Property Wrappers in Swift explained with code examples](https://www.avanderlee.com/swift/property-wrappers/)
- [@article@SwiftUI Property Wrappers](https://swiftuipropertywrappers.com/)
- [@video@Getting Started with Property Wrappers in Swift 🔥](https://www.youtube.com/watch?v=61lr5ZI_-6E)
- [@video@SwiftUI Property Wrappers](https://www.youtube.com/watch?v=yWdJ3dRRDlk)

## Xcode Debugging

# Xcode Debugger

The Xcode debugger is a powerful tool built into the Xcode IDE that allows developers to step through their code line by line, inspect variables, and understand the flow of execution. It helps identify and fix bugs by providing insights into the application's state at various points in time. You can set breakpoints to pause execution, examine the call stack to trace the sequence of function calls, and use the console to print out values or execute custom commands.

Visit the following resources to learn more:

- [@official@Debugging](https://developer.apple.com/documentation/xcode/debugging)
- [@official@Stepping through code and inspecting variables to isolate bugs](https://developer.apple.com/documentation/xcode/stepping-through-code-and-inspecting-variables-to-isolate-bugs)
- [@official@Building your app to include debugging information](https://developer.apple.com/documentation/xcode/building-your-app-to-include-debugging-information)
- [@video@Xcode 16 Debugging Tutorial for Beginners (2025)](https://www.youtube.com/watch?v=ZJmUeOT6c-Y)
- [@video@WWDC24: Xcode essentials | Apple](https://www.youtube.com/watch?v=EN7-6Oj7cL0)

## Xcode

# Xcode

Xcode is Apple's integrated development environment (IDE) used for developing software for macOS, iOS, watchOS, and tvOS. It provides a comprehensive suite of tools for writing, debugging, and testing code, as well as designing user interfaces. Xcode includes a code editor, compiler, debugger, and build system, all integrated into a single application.

Visit the following resources to learn more:

- [@official@Xcode](https://developer.apple.com/xcode/)
- [@video@Introduction to Xcode (Xcode 16 Updated)](https://www.youtube.com/watch?v=7RTHzBh3nkg)

## Xctest

# XCTest

XCTest is Apple's framework for writing unit, integration, and UI tests for your Swift and Objective-C code. It allows developers to verify the correctness of their code by writing assertions that check for expected outcomes. While XCTest has been the standard for iOS testing for a long time, the Swift Testing framework is emerging as a modern alternative, promising a more streamlined and Swift-native approach to testing in the future.

Visit the following resources to learn more:

- [@official@XCTest](https://developer.apple.com/documentation/xctest)
- [@official@Migrating a test from XCTest](https://developer.apple.com/documentation/Testing/MigratingFromXCTest)
- [@article@Creating our first unit test using XCTest](https://www.hackingwithswift.com/read/39/8/user-interface-testing-with-xctest)
- [@article@Hello Swift Testing, Goodbye XCTest](https://leocoout.medium.com/welcome-swift-testing-goodbye-xctest-7501b7a5b304)
- [@video@Unit Testing in iOS with XCTest](https://www.youtube.com/watch?v=YR3PgwKKraw)

## Zstack

# ZStack

ZStack is a layout container that overlays views on top of each other, aligning them in both the horizontal and vertical axes. The views are stacked in the order they are declared, with the last view in the code appearing on top. This allows you to create layered effects, such as placing text over an image or creating custom button styles with multiple layers.

Visit the following resources to learn more:

- [@official@ZStack](https://developer.apple.com/documentation/swiftui/zstack)
- [@article@ZStack](https://www.swiftuifieldguide.com/layout/zstack/)
- [@video@VStack, HStack, and ZStack in SwiftUI | Bootcamp](https://www.youtube.com/watch?v=pv-vbUEzimk)
