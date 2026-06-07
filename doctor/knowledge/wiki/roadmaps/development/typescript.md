# Typescript Roadmap

## Abstract Classes

# Abstract Classes

An abstract class is a class that cannot be instantiated directly. Its primary purpose is to define a blueprint for other classes. It can contain abstract methods (methods without implementation) and concrete methods (methods with implementation). Subclasses must provide concrete implementations for all abstract methods inherited from the abstract class, unless the subclass is also declared abstract. This ensures that subclasses adhere to a specific interface or contract.

Visit the following resources to learn more:

- [@official@Abstract Classes](https://www.typescriptlang.org/docs/handbook/2/classes.html#abstract-classes-and-members)

## Access Modifiers

# Access Modifiers

Access modifiers in object-oriented programming control the visibility of class members (properties and methods). They determine which parts of your code, or even external code, can access and modify those members. Common access modifiers include `public`, `private`, and `protected`, each offering different levels of accessibility and encapsulation.

Visit the following resources to learn more:

- [@official@TypeScript Access Modifiers](https://www.typescripttutorial.net/typescript-tutorial/typescript-access-modifiers/)

## Advanced Types

# Advanced Types

TypeScript's advanced types allow for more precise and flexible type definitions beyond basic primitives. Intersection types combine multiple types into one, requiring a value to satisfy all combined types. Union types allow a value to be one of several specified types. Type aliases create a name for a type, making complex type definitions easier to reuse. Conditional types allow types to be determined based on a condition, often using generics. Index types enable you to extract the type of a property from another type using a key. Mapped types transform each property in a type, creating a new type based on the original. Type guards are functions that narrow down the type of a variable within a specific scope.

Visit the following resources to learn more:

- [@official@Advanced Topics](https://www.typescriptlang.org/docs/handbook/type-compatibility.html#advanced-topics)
- [@video@Tutorial of Typescript - Advanced Types](https://www.youtube.com/playlist?list=PLw5h0DiJ-9PBIgIyd2ZA1CVnJf0BLFJg2)

## Ambient Modules

# Ambient Modules

Ambient modules in TypeScript are used to describe the shape of existing JavaScript code when you don't have the TypeScript declaration files (`.d.ts`) readily available. They essentially allow you to tell the TypeScript compiler about the existence and structure of a JavaScript module, so you can import and use it in your TypeScript code without getting type errors, even if the module itself wasn't written in TypeScript.

Visit the following resources to learn more:

- [@official@Ambient Modules](https://www.typescriptlang.org/docs/handbook/modules/reference.html#ambient-modules)

## Any

# Any

TypeScript has a special type, `any`, that you can use whenever you don’t want a particular value to cause typechecking errors.

When a value is of type `any`, you can access any properties of it (which will in turn be of type `any`), call it like a function, assign it to (or from) a value of any type, or pretty much anything else that’s syntactically legal:

    let obj: any = { x: 0 };
    // None of the following lines of code will throw compiler errors.
    // Using `any` disables all further type checking, and it is assumed
    // you know the environment better than TypeScript.
    obj.foo();
    obj();
    obj.bar = 100;
    obj = 'hello';
    const n: number = obj;

Visit the following resources to learn more:

- [@official@any type in TypeScript](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#any)

## Array

# Array

An array is a data structure that stores an ordered collection of elements, where each element is accessed using its numerical index. Arrays are fundamental for managing lists of items, and in TypeScript, you define the types of elements that an array can hold, enforcing consistency and preventing errors. An array's length is mutable allowing you to dynamically add or remove elements.

Visit the following resources to learn more:

- [@official@Arrays](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#arrays)

## As Any

# As Any

`any` is a special type in TypeScript that represents a value of any type. When a value is declared with the any type, the compiler will not perform any type checks or type inference on that value.

For example:

    let anyValue: any = 42;
    
    // we can assign any value to anyValue, regardless of its type
    anyValue = 'Hello, world!';
    anyValue = true;

Visit the following resources to learn more:

- [@official@any](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#any)

## As Const

# as const

`as const` is a TypeScript feature that allows you to tell the compiler to infer the narrowest or most specific type possible for an expression. Instead of the compiler widening the type of a value to its general type (like inferring a string variable as `string`), `as const` makes the compiler infer the value as a constant type (like inferring a string variable as the specific string literal type `"hello"`). This is useful for creating immutable data structures or when you need the compiler to enforce the exact values allowed.

Visit the following resources to learn more:

- [@official@const assertions](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-3-4.html#const-assertions)

## As Type

# Type Assertions with `as`

Type assertions in TypeScript are a way to tell the compiler the specific type of a variable. They allow you to override TypeScript's type inference when you know more about the type of a value than the compiler does. Using `as [type]` is one syntax for type assertions, allowing you to explicitly cast a variable to a more specific type. This doesn't perform any runtime type checking or conversion, it simply instructs the compiler to treat the variable as if it were of the specified type.

Visit the following resources to learn more:

- [@official@Type assertions](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#type-assertions)

## Awaited

# Awaited

`Awaited` is a utility type in TypeScript that is used to recursively unwrap the `Promise` type. It simulates the `await` operator's behavior in JavaScript. If you have a type that represents a `Promise`, `Awaited` can extract the underlying type that the `Promise` resolves to. It handles nested `Promise` types and other thenables, continually unwrapping until it reaches a non-promise type.

Visit the following resources to learn more:

- [@official@Awaited<Type>](https://www.typescriptlang.org/docs/handbook/utility-types.html#awaitedtype)

## Boolean

# Boolean Type in TypeScript

A boolean type represents a logical value that can be either `true` or `false`. It is commonly used in programming to control the flow of execution based on certain conditions, allowing programs to make decisions and execute different code blocks depending on whether a condition is met. Boolean values are fundamental for expressing logical operations and comparisons.

Visit the following resources to learn more:

- [@article@Number, String, Boolean, Symbol and Object](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#the-primitives-string-number-and-boolean)

## Build Tools

# Build Tools

Task runners automatically execute commands and carry out processes behind the scenes. This helps automate your workflow by performing mundane, repetitive tasks that you would otherwise waste an egregious amount of time repeating. Common usages of task runners include numerous development tasks such as: spinning up development servers, compiling code (ex. SCSS to CSS), running linters, serving files up from a local port on your computer, and many more!

Visit the following resources to learn more:

- [@official@webpack is a static module bundler for modern JavaScript applications](https://webpack.js.org/)
- [@official@Vite Next Generation Frontend Tooling](https://vitejs.dev)
- [@official@Parcel is a zero configuration build tool for the web](https://parceljs.org/)
- [@official@esbuild is an extremely fast JavaScript bundler and minifier](https://esbuild.github.io/)
- [@official@swc is a super-fast compiler written in Rust](https://swc.rs/)

## Class

# Class

A class is a blueprint for creating objects (instances) that share similar characteristics. It defines the properties (data) and methods (functions) that the objects will possess. Classes allow you to create reusable code structures by defining a template that you can then use to instantiate multiple objects with the same basic features.

Visit the following resources to learn more:

- [@official@TypeScript Classes](https://www.typescriptlang.org/docs/handbook/2/classes.html)

## Classes

# Classes

Classes are blueprints for creating objects, encapsulating data (properties) and behavior (methods) into a single unit. They provide a structured way to define the characteristics and actions that an object of that class can possess. This allows for creating multiple instances of the same object type with consistent properties and methods.

Visit the following resources to learn more:

- [@official@Tutorial - Classes](https://www.typescriptlang.org/docs/handbook/2/classes.html)

## Combining Types

# Combining Types

Combining types in TypeScript allows you to create new, more complex types from existing ones. This is achieved through features like unions and intersections. A union type lets a variable hold values of different types, while an intersection type combines multiple types into a single type that has all the properties of each individual type. These mechanisms provide flexibility and expressiveness when defining the shape of your data.

Visit the following resources to learn more:

- [@official@Union Types in TypeScript](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#union-types)
- [@article@Intersection Types in TypeScript](https://www.typescripttutorial.net/typescript-tutorial/typescript-intersection-types/)
- [@article@Type Aliases](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#type-aliases)
- [@article@Keyof Type Operator](https://www.typescriptlang.org/docs/handbook/2/keyof-types.html#handbook-content)

## Compiler Options

# Compiler Options

Compiler options in TypeScript provide fine-grained control over how the TypeScript compiler (`tsc`) transforms `.ts` files into JavaScript. These options are typically configured within a `tsconfig.json` file or passed directly via the command line.  They dictate aspects like target ECMAScript version, module system, strictness of type checking, source map generation, and many other behaviors of the compilation process.

Visit the following resources to learn more:

- [@official@Compiler Options](https://www.typescriptlang.org/docs/handbook/compiler-options.html)

## Conditional Types

# Conditional Types

Conditional types in TypeScript allow you to define types that depend on other types, similar to a ternary operator in JavaScript. They enable you to express type relationships that change based on whether a specific type condition is met. This feature makes your type definitions more flexible and capable of handling complex scenarios where the resulting type depends on the structure or nature of another type.

Visit the following resources to learn more:

- [@official@Conditional Types](https://www.typescriptlang.org/docs/handbook/2/conditional-types.html#handbook-content)
- [@video@Conditional Types - Advanced TypeScript](https://www.youtube.com/watch?v=QFWrbNehKk0)

## Constructor Overloading

# Constructor Overloading

Constructor overloading allows a class to have multiple constructors with different parameter lists.  This enables you to create objects of the class in different ways, providing flexibility in initialization based on the provided arguments. Each constructor variation handles the object's initialization differently depending on the types and number of arguments passed during instantiation.

Visit the following resources to learn more:

- [@official@Constructors - TypeScript](https://www.typescriptlang.org/docs/handbook/2/classes.html#constructors)

## Constructor Params

# Constructor Parameters

In TypeScript classes, constructor parameters provide a concise way to define and initialize class properties directly within the constructor's parameter list. By using access modifiers like `public`, `private`, or `protected` before a constructor parameter, TypeScript automatically creates a corresponding class property with that name and assigns the constructor argument's value to it. This streamlines the process of property declaration and initialization, reducing boilerplate code.

Visit the following resources to learn more:

- [@official@TypeScript - Construct](https://www.typescriptlang.org/docs/handbook/2/classes.html#constructors)

## Decorators

# Decorators

Decorators are a special kind of declaration that can be attached to a class declaration, method, accessor, property, or parameter. They use the form `@expression`, where `expression` must evaluate to a function that will be called at runtime with information about the decorated declaration. Decorators provide a way to add both annotations and a meta-programming syntax for class declarations and members. They essentially modify the behavior or functionality of the decorated code in a declarative way.

Visit the following resources to learn more:

- [@official@Decorators](https://www.typescriptlang.org/docs/handbook/decorators.html#handbook-content)

## Ecosystem

# TypeScript Ecosystem

The TypeScript ecosystem refers to the collection of tools, libraries, frameworks, and resources that support and enhance TypeScript development. It includes everything from build tools and linters to UI libraries and server-side frameworks that have TypeScript definitions available or are specifically designed to work well with TypeScript. The ecosystem also incorporates community resources like documentation, tutorials, and open-source projects that help developers learn and use TypeScript effectively.

## Enum

# Enum

An "enum" (short for enumeration) is a way to define a set of named constants. It provides a way to give more friendly names to sets of numeric values, making code more readable and maintainable. Enums allow you to define a type by enumerating its possible values, which can represent options, states, or any other set of distinct possibilities.

Visit the following resources to learn more:

- [@official@TypeScript - Enums](https://www.typescriptlang.org/docs/handbook/enums.html)

## Equality

# Equality in Type Guards and Narrowing

Equality in the context of type guards and narrowing refers to using comparison operators (like `===`, `!==`, `==`, `!=`) to refine the type of a variable within a TypeScript program. By comparing a variable against a specific value (or another variable), TypeScript can infer a more specific type for that variable within a certain scope, enabling safer and more accurate code execution by ruling out possibilities. This mechanism enhances type safety by allowing the compiler to understand the possible values and types a variable can hold at different points in the code.

Visit the following resources to learn more:

- [@official@Equality Narrowing](https://www.typescriptlang.org/docs/handbook/2/narrowing.html#equality-narrowing)

## Exclude

# Exclude

`Exclude` is a utility type in TypeScript that constructs a new type by removing types from a union type. Given two types, `Type` and `ExcludedUnion`, `Exclude<Type, ExcludedUnion>` creates a type that includes all members of `Type` that are *not* assignable to `ExcludedUnion`. This is useful for filtering out specific types from a union, resulting in a more refined and specific type.

Visit the following resources to learn more:

- [@official@Exclude<UnionType, ExcludedMembers>](https://www.typescriptlang.org/docs/handbook/utility-types.html#excludeuniontype-excludedmembers)

## Extending Interfaces

# Extending Interfaces

Extending interfaces in TypeScript allows you to create new interfaces based on existing ones. This means a new interface can inherit all the properties and methods of a parent interface and add its own unique members, promoting code reuse and establishing a clear hierarchy of types. Think of it like inheritance in classes, but for interface definitions.

Visit the following resources to learn more:

- [@official@Extending Interfaces](https://www.typescriptlang.org/docs/handbook/2/objects.html)

## External Modules

# External Modules in TypeScript

External modules in TypeScript are files containing code that can be imported and used in other files. They help organize and structure your project by dividing code into logical units, improving maintainability and reusability. Each external module has its own scope, preventing naming conflicts and allowing you to explicitly control what is exposed from the module using `export` and what is consumed from other modules using `import`.

Visit the following resources to learn more:

- [@article@TypeScript - External Module](https://learncodeweb.com/typescript/modules-in-typescript-explain-with-an-example/)

## Extract

# Extract

Extract allows you to create a new type by picking out specific types from a union based on a condition.  Essentially, it filters a union type, keeping only those members that are assignable to a specified type. This is useful when you need to narrow down the possible types in a union to only those that meet a certain criteria.

Visit the following resources to learn more:

- [@official@Extract<Type, Union>](https://www.typescriptlang.org/docs/handbook/utility-types.html#extracttype-union)

## Formatting

# Formatting

Formatting tools automatically adjust the way your code looks, making it consistent and easier to read. These tools can handle things like spacing, indentation, and line breaks. This makes your code cleaner and helps everyone on a team follow the same style. A popular tool for formatting code is Prettier. It supports TypeScript and can be configured to enforce a specific style guide.

Visit the following resources to learn more:

- [@article@Prettier Website](https://prettier.io)
- [@article@Why Prettier](https://prettier.io/docs/en/why-prettier.html)
- [@article@BiomeJS Website](https://biomejs.dev)

## Function Overloading

# Function Overloading

Function overloading allows you to define multiple function signatures with the same name but different parameter types or numbers of parameters. This lets you provide specific type information based on how the function is called, enhancing type safety and code clarity. When you call an overloaded function, TypeScript picks the most appropriate function signature based on the provided arguments.

Visit the following resources to learn more:

- [@official@Function Overloads](https://www.typescriptlang.org/docs/handbook/2/functions.html#function-overloads)

## Generic Constraints

# Generic Constraints

Generic constraints in TypeScript allow you to limit the types that can be used as type arguments for a generic type or function. They ensure that the type argument satisfies a specific requirement, like having certain properties or methods. This provides more type safety and enables you to work with specific properties of the generic type, knowing they are guaranteed to exist.

Visit the following resources to learn more:

- [@official@Generic Constraints - TypeScript](https://www.typescriptlang.org/docs/handbook/2/generics.html#generic-constraints)

## Generic Types

# Generic Types

Generic types allow you to write code that can work with a variety of types without sacrificing type safety. Think of them as placeholders for types that you specify later when you use the code. To create a generic type, you use angle brackets `<>` to define type parameters. These parameters act as variables that represent the specific type you want to work with, allowing you to write reusable components that adapt to different data types.

Visit the following resources to learn more:

- [@official@Hello World of Generics](https://www.typescriptlang.org/docs/handbook/2/generics.html#hello-world-of-generics)

## Generics

# Generics

Generics are a way to write code that can work with a variety of types without knowing those types ahead of time. They allow you to define type variables that can be used to represent the specific type that will be used when the code is actually executed. This makes your code more reusable and type-safe by preventing errors that could occur if you were to use `any` or other less specific types.

Visit the following resources to learn more:

- [@official@Hello World of Generics](https://www.typescriptlang.org/docs/handbook/2/generics.html#hello-world-of-generics)

## Global Augmentation

# Global Augmentation

Global augmentation in TypeScript lets you add or modify existing global types and interfaces. This is particularly useful when working with JavaScript libraries that don't have TypeScript definitions or when you want to extend existing TypeScript definitions to suit your specific project needs.  It essentially allows you to declare properties or methods on globally available objects (like `window` or built-in JavaScript objects) from within your TypeScript code.

Visit the following resources to learn more:

- [@official@Global augmentation](https://www.typescriptlang.org/docs/handbook/declaration-merging.html#global-augmentation)

## Hybrid Types

# Hybrid Types

Hybrid types describe objects that act as both an object and a function. In essence, they possess properties and methods like a regular object, but they can also be invoked or called directly like a function. This unusual structure is often used when a function needs to maintain state or have additional properties associated with it.

## Inheritance Vs Polymorphism

# Inheritance vs. Polymorphism

Inheritance is a mechanism where a class (the subclass or derived class) acquires the properties and methods of another class (the superclass or base class), establishing an "is-a" relationship. Polymorphism, meaning "many forms," allows objects of different classes to be treated as objects of a common type, enabling you to write code that can work with objects of multiple classes without knowing their specific types at compile time.

Visit the following resources to learn more:

- [@article@Dev.to - Mastering OOP in TypeScript](https://dev.to/rajrathod/mastering-object-oriented-programming-with-typescript-encapsulation-abstraction-inheritance-and-polymorphism-explained-c6p)
- [@video@Inheritance and Polymorphism In TypeScript](https://www.youtube.com/watch?v=Sn6K57YSuwU)

## Installation And Configuration

# Installation and Configuration

The installation process of TypeScript generally includes installing the TypeScript compiler, which translates TypeScript code into JavaScript, and configuring your project with a `tsconfig.json` file to manage compiler options and project settings. This setup enables you to write, compile, and run TypeScript code effectively.

Visit the following resources to learn more:

- [@official@Install and Configure TypeScript](https://www.typescriptlang.org/download)
- [@article@TypeScript Getting Started](https://thenewstack.io/typescript-tutorial-a-guide-to-using-the-programming-language/)

## Instanceof

# instanceof Operator

The `instanceof` operator checks if an object is an instance of a specific class or constructor function. It determines if the prototype property of a constructor appears anywhere in the prototype chain of an object. The result of this check is a boolean value, indicating whether the object is considered an instance of the specified type.

Visit the following resources to learn more:

- [@official@instanceOf Operator](https://www.typescriptlang.org/docs/handbook/2/narrowing.html#instanceof-narrowing)

## Instancetype

# InstanceType

`InstanceType` is a conditional type in TypeScript that extracts the instance type of a constructor function type. In simpler terms, given a type that represents a class or a constructor function, `InstanceType` determines the type of the object that would be created when you use the `new` keyword with that constructor. This allows you to easily work with the specific type of instances generated by a class constructor within your type system.

Visit the following resources to learn more:

- [@official@InstanceType<Type>](https://www.typescriptlang.org/docs/handbook/utility-types.html#instancetypetype)

## Interface Declaration

# Interface Declaration

An interface declaration introduces a new named type into the TypeScript type system. It specifies a contract that an object (or other type) can adhere to, defining the names and types of properties and methods that implementing objects must possess. Interfaces do not produce JavaScript code; they exist purely for type-checking purposes, enabling stronger static typing and improved code maintainability.

Visit the following resources to learn more:

- [@official@Extending Interfaces](https://www.typescriptlang.org/docs/handbook/2/objects.html)

## Interface

# Interface

An interface in TypeScript is a way to define a contract for the shape of an object. It names a set of properties and their types that an object must have. Think of it as a blueprint that specifies the properties (and optionally, methods) that an object should possess, allowing you to ensure that different parts of your code work together smoothly by enforcing a consistent structure.

Visit the following resources to learn more:

- [@official@Object Types - Interfaces](https://www.typescriptlang.org/docs/handbook/2/objects.html)

## Intersection Types

# Intersection Types

Intersection types in TypeScript allow you to combine multiple types into a single type. The resulting type has all the features (properties, methods, etc.) of all the constituent types. This is particularly useful when you want to create a type that represents an object that must satisfy multiple type constraints simultaneously.

Visit the following resources to learn more:

- [@article@Intersection Types in TypeScript](https://www.typescripttutorial.net/typescript-tutorial/typescript-intersection-types/)

## Introduction To Typescript

# Introduction to TypeScript

TypeScript is a programming language that builds on JavaScript by adding static types. It essentially acts as a superset of JavaScript, meaning that all valid JavaScript code is also valid TypeScript code. The key addition of static typing allows developers to define the expected data types of variables, function parameters, and return values, which helps catch errors during development and improves code maintainability.

Visit the following resources to learn more:

- [@official@Overview of TypeScript](https://www.typescriptlang.org/docs/handbook/typescript-from-scratch.html)
- [@official@TypeScript Official Handbook](https://www.typescriptlang.org/docs/handbook/intro.html)
- [@article@What Is TypeScript?](https://thenewstack.io/what-is-typescript/)
- [@video@Video: Where TypeScript Excels](https://youtu.be/BUo7B6UuoJ4)

## Keyof Operator

# keyof Operator

The `keyof` operator in TypeScript creates a union of all the keys (property names) of a given object type. It essentially extracts the names of the properties as string literal types. This allows you to work with the properties of an object type in a type-safe way, especially when dealing with generic functions or situations where you need to ensure that you're only accessing valid properties.

Visit the following resources to learn more:

- [@official@keyof Type Operator](https://www.typescriptlang.org/docs/handbook/2/keyof-types.html#handbook-content)

## Linting

# Linting

Linting is the process of running a program that analyzes code for potential errors, stylistic issues, and code quality problems. It helps developers identify and fix issues early in the development cycle, leading to more maintainable and consistent codebases. ESLint is a popular linting tool for JavaScript and TypeScript that can be configured with rules to enforce specific coding standards and best practices.

Visit the following resources to learn more:

- [@article@ESLint Official Website](https://eslint.org/)
- [@article@Introduction to ESLint](https://dev.to/shivambmgupta/eslint-what-why-when-how-5f1d)
- [@video@ESLint Quickstart - find errors automatically](https://www.youtube.com/watch?v=qhuFviJn-es)

## Literal Types

# Literal Types

Literal types are a feature that allows you to specify the exact value a variable can hold. Instead of just saying a variable is a `string` or a `number`, you can specify that it can only be a particular string like `"hello"` or a particular number like `42`. This enables more precise type checking and helps catch errors at compile time by ensuring that variables only hold the intended values.

Visit the following resources to learn more:

- [@official@Literal Types](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#literal-types)

## Mapped Types

# Mapped Types

Mapped types in TypeScript allow you to create new types based on existing ones by transforming each property. They iterate over the keys of an existing type and apply a transformation to each key and/or value, effectively mapping the original type to a new type structure. This provides a concise and powerful way to generate types that are variations of other types, promoting code reuse and reducing redundancy.

Visit the following resources to learn more:

- [@official@Mapped Types](https://www.typescriptlang.org/docs/handbook/2/mapped-types.html#handbook-content)

## Method Overriding

# Method Overriding

Method overriding allows a subclass to provide a specific implementation for a method that is already defined in its superclass. When a method in a subclass has the same name, same parameters, and same return type (or a more specific return type, known as covariant return type) as a method in its superclass, the subclass's method overrides the superclass's method. This means that when the method is called on an object of the subclass, the subclass's version of the method will be executed instead of the superclass's version.

Visit the following resources to learn more:

- [@official@TypeScript - Overriding Methods](https://www.typescriptlang.org/docs/handbook/2/classes.html#overriding-methods)

## Namespace Augmentation

# Namespace Augmentation

Namespace augmentation in TypeScript allows you to add new properties or methods to an existing namespace, even if that namespace is defined in a separate file or module. This feature is particularly useful for extending namespaces declared in external libraries or modules without directly modifying the original source code. It provides a way to customize or add functionality to existing namespaces in a modular and organized manner.

Visit the following resources to learn more:

- [@official@Module Augmentation](https://www.typescriptlang.org/docs/handbook/declaration-merging.html#module-augmentation)

## Namespaces

# Namespaces

Namespaces in TypeScript are a way to organize code into logical groups, preventing naming collisions and improving code maintainability. They create a named container where you can define variables, functions, classes, and interfaces. By using namespaces, you can encapsulate related functionality under a specific name, making your code more structured and easier to understand.

Visit the following resources to learn more:

- [@official@Overview of Namespaces](https://www.typescriptlang.org/docs/handbook/namespaces.html)
- [@official@Namespaces and Modules](https://www.typescriptlang.org/docs/handbook/namespaces-and-modules.html)
- [@official@TypeScript - Using Namespaces](https://typescriptlang.org/docs/handbook/namespaces-and-modules.html#using-namespaces)

## Never

# Never Type

The `never` type in TypeScript represents the type of values that will never occur. This means a function that always throws an error or runs forever (infinite loop) implicitly returns `never`. It is also useful for exhaustive checking in discriminated unions, ensuring that all possible cases are handled. Essentially, you cannot assign any type to a variable of type `never` (except `never` itself), making it the bottom type in TypeScript's type system.

Visit the following resources to learn more:

- [@official@Never Type](https://www.typescriptlang.org/docs/handbook/2/narrowing.html#the-never-type)

## Non Null Assertion

# Non-null Assertion

The non-null assertion operator in TypeScript is a way to tell the compiler that you are certain a value is not null or undefined, even if the TypeScript's type checker thinks it could be. It is denoted by an exclamation mark (`!`) placed after a variable or expression. Using this operator effectively tells the compiler to suppress strict null checks for that particular expression, trusting that you, the developer, have enough context to know the value will be present at runtime.

Visit the following resources to learn more:

- [@official@Non-null assertion operator](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-2-0.html#non-null-assertion-operator)

## Nonnullable

# NonNullable Utility Type

`NonNullable` is a utility type that removes `null` and `undefined` from a type. If you have a type that could potentially be `null` or `undefined`, applying `NonNullable` ensures that the resulting type will only consist of the original type's other possible values, effectively guaranteeing that `null` and `undefined` are excluded.

## Null

# Null Type in TypeScript

The `null` type represents the intentional absence of a value. It's a primitive data type that has only one possible value: `null`. It signifies that a variable or property has no value assigned to it, or that a value has been explicitly removed.

Visit the following resources to learn more:

- [@official@null and undefined](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#null-and-undefined)

## Number

# Number Type in TypeScript

The `number` type in TypeScript represents numeric values. This includes integers (whole numbers like 1, 42, -10) and floating-point numbers (numbers with decimal points like 3.14, -0.5).  TypeScript uses double-precision 64-bit floating point format (IEEE 754) to represent all numbers.

Visit the following resources to learn more:

- [@official@Number, String, Boolean, Symbol and Object](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#the-primitives-string-number-and-boolean)

## Object

# Object Types in TypeScript

In TypeScript, an object type defines the structure of a JavaScript object. It specifies the names, types, and optionality of the properties an object should have. You can define object types using curly braces `{}` and listing the properties with their corresponding types, separated by semicolons or commas. This allows TypeScript to enforce that objects conform to a specific shape, enhancing code safety and providing better autocompletion during development.

Visit the following resources to learn more:

- [@official@Object Types in TypeScript](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#object-types)

## Omit

# Omit

`Omit` is a utility type in TypeScript that constructs a new type by picking all properties from an existing type and then removing the specified properties (keys). Essentially, it creates a subset of the original type by excluding certain keys you define. The resulting type will only contain the properties that were not omitted.

Visit the following resources to learn more:

- [@official@Omit<Type, Keys>](https://www.typescriptlang.org/docs/handbook/utility-types.html#omittype-keys)

## Parameters

# Parameters Utility Type

The `Parameters` utility type in TypeScript extracts the parameter types of a function type into a tuple. This allows you to programmatically determine the expected arguments of a function and use them in other type definitions, providing type safety and flexibility when working with function signatures. The result is a tuple type where each element represents the type of a parameter in the function.

## Partial

# Partial Type

The `Partial<Type>` utility type in TypeScript constructs a type where all properties of the original `Type` are set to optional. This means that when you use `Partial<Type>`, you can create objects that only include a subset of the properties defined in the original `Type`, or even have no properties at all. Essentially, it makes all properties of a type nullable.

## Pick

# Pick

`Pick` is a utility type that constructs a new type by selecting a set of properties from an existing type. You specify which properties you want to include in the new type using their keys. This is useful when you need a subset of properties from a larger type definition.

Visit the following resources to learn more:

- [@official@Pick<Type, Keys>](https://www.typescriptlang.org/docs/handbook/utility-types.html#picktype-keys)

## Readonly

# Readonly

The `Readonly` utility type in TypeScript constructs a new type where all properties of the original type are set as read-only. This means that once a property is initialized, its value cannot be changed later. This is useful for creating immutable objects and ensuring that data is not accidentally modified.

## Record

# Record Utility Type

The `Record` utility type in TypeScript is used to construct a new type where the keys are of a specific type (typically a string, number, or symbol) and the values are of another specified type. This is useful when you want to define an object structure with a predefined set of keys and a consistent type for the values associated with those keys. Essentially, it's a shorthand for defining object types with specific key-value pairings.

Visit the following resources to learn more:

- [@official@Record<Keys, Type>](https://www.typescriptlang.org/docs/handbook/utility-types.html#recordkeys-type)

## Recursive Types

# Recursive Types

Recursive types in TypeScript allow you to define types that refer to themselves. This is especially useful for representing data structures that have a nested or hierarchical structure, like trees or linked lists. By using recursion in type definitions, you can ensure that the type system accurately reflects the self-referential nature of these data structures, enabling strong type checking throughout your code.

Visit the following resources to learn more:

- [@official@Recursive Types in TypeScript](https://www.typescriptlang.org/play/3-7/types-and-code-flow/recursive-type-references.ts.html)

## Returntype

# ReturnType

`ReturnType` is a utility type that extracts the return type of a function. Given a function type, `ReturnType<Type>` produces a new type that represents the type of value that the function returns. This is useful when you need to work with the output of a function without knowing its exact return type beforehand.

## Running Typescript

# Running TypeScript

Running TypeScript involves converting your `.ts` files into JavaScript files that can be executed by a JavaScript runtime environment, such as a web browser or Node.js. This conversion, known as compilation or transpilation, is performed by the TypeScript compiler (`tsc`). After compilation, the resulting JavaScript files can then be run in the appropriate environment, allowing you to leverage the benefits of TypeScript during development while maintaining compatibility with standard JavaScript execution environments.

Visit the following resources to learn more:

- [@official@Running your TypeScript](https://www.typescriptlang.org/docs/handbook/typescript-tooling-in-5-minutes.html)

## Satisfies Keyword

# Satisfies Keyword

The `satisfies` keyword in TypeScript is used to ensure that a value conforms to a specific type without explicitly declaring that type. This is particularly useful when you want to check that an object's structure matches a type definition but still allow TypeScript to infer a more specific type for the object's properties. It validates the shape of the value against the specified type, and if valid it retains the initial type information.

Visit the following resources to learn more:

- [@official@satisfies Keyword](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-4-9.html#the-satisfies-operator)

## String

# String

A string represents a sequence of characters. It's used to store and manipulate textual data, like words, sentences, or any sequence of symbols.  Strings are typically enclosed in single quotes (`'...'`), double quotes (`"..."`), or backticks (`` `...` ``).

Visit the following resources to learn more:

- [@official@Number, String, Boolean, Symbol and Object](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#the-primitives-string-number-and-boolean)

## Template Literal Types

# Template Literal Types

Template literal types in TypeScript are a way to create new string literal types by combining existing string literal types, much like template literals in JavaScript. They allow you to define string types that are composed of other string types with specific patterns or structures. This is done by embedding other types within a string literal definition, enabling you to enforce stricter type safety and create more descriptive types based on string manipulation.

Visit the following resources to learn more:

- [@official@Template Literal Types](https://www.typescriptlang.org/docs/handbook/2/template-literal-types.html#handbook-content)

## Truthiness

# Truthiness

Truthiness in TypeScript, as in JavaScript, refers to the concept of a value evaluating to `true` when encountered in a Boolean context.  Certain values are inherently "truthy" while others are "falsy."  TypeScript uses this understanding to refine the type of a variable based on the outcome of a truthiness check, effectively narrowing its potential types to those that are compatible with a `true` outcome. This allows for more precise type checking within conditional blocks.

Visit the following resources to learn more:

- [@official@Truthiness Narrowing](https://www.typescriptlang.org/docs/handbook/2/narrowing.html#truthiness-narrowing)

## Ts And Js Interoperability

# TS and JS Interoperability

TypeScript and JavaScript interoperability refers to the ability of TypeScript code to work seamlessly with existing JavaScript code and vice versa. This means you can use JavaScript libraries in your TypeScript projects and gradually migrate JavaScript code to TypeScript without rewriting everything at once. It allows for a smooth transition by leveraging existing codebases and libraries while adopting the benefits of TypeScript.

Visit the following resources to learn more:

- [@official@Type Checking JavaScript Files](https://www.typescriptlang.org/docs/handbook/type-checking-javascript-files.html)
- [@video@Using JavaScript in TypeScript](https://youtu.be/AZhZlEbBaB4)

## Ts Node

# ts-node

ts-node is a package that lets you directly run TypeScript code without needing to pre-compile it into JavaScript. It does this by providing a TypeScript execution environment for Node.js, allowing you to execute `.ts` files directly from the command line or by using it as a Node.js module. Essentially, it combines the TypeScript compiler (`tsc`) and Node.js into a single, streamlined process.

Visit the following resources to learn more:

- [@opensource@ts-node - GitHub Project](https://github.com/TypeStrong/ts-node)
- [@article@How To Run TypeScript Scripts with ts-node](https://www.digitalocean.com/community/tutorials/typescript-running-typescript-ts-node)
- [@feed@Explore top posts about TypeScript](https://app.daily.dev/tags/typescript?ref=roadmapsh)

## Ts Playground

# TS Playground

The TS Playground is an online, interactive environment that allows you to write, compile, and share TypeScript code directly in your web browser. It provides immediate feedback on your code, showing compilation errors and the resulting JavaScript output in real-time. This makes it a convenient tool for experimenting with TypeScript features, prototyping small projects, and quickly testing code snippets without needing a local development environment.

Visit the following resources to learn more:

- [@official@TypeScript Official - Playground](https://www.typescriptlang.org/play)
- [@feed@Explore top posts about TypeScript](https://app.daily.dev/tags/typescript?ref=roadmapsh)

## Tsc

# tsc

`tsc` is the command-line compiler for TypeScript. It takes TypeScript code as input and transforms it into JavaScript code that can be executed by browsers or other JavaScript runtimes like Node.js. You use `tsc` to check for type errors, enforce coding standards, and ultimately prepare your TypeScript code for deployment.

Visit the following resources to learn more:

- [@official@tsc CLI Options](https://www.typescriptlang.org/docs/handbook/compiler-options.html#using-the-cli)

## Tsconfigjson

# tsconfig.json

`tsconfig.json` is a configuration file that specifies how the TypeScript compiler should transpile your TypeScript code into JavaScript. It controls various compilation options such as target ECMAScript version, module system, and source maps. This file lives at the root of a TypeScript project and allows you to define the project's compilation settings in a declarative and reproducible manner.

Visit the following resources to learn more:

- [@official@What is a tsconfig.json](https://www.typescriptlang.org/docs/handbook/tsconfig-json.html#handbook-content)

## Tuple

# Tuple

A tuple is a typed array with a pre-defined length and types for each index. Each position in the tuple can have its own specific type, allowing you to create arrays with a known structure where the type of element is known at each index. Tuples ensure that the number of elements matches the defined length and that each element is of the expected type.

Visit the following resources to learn more:

- [@official@Tuple Types](https://www.typescriptlang.org/docs/handbook/2/objects.html#tuple-types)

## Type Aliases

# Type Aliases

Type aliases in TypeScript create a new name for an existing type. This new name can then be used anywhere you would normally use the original type. They don't create a new type; instead, they offer a more readable and convenient way to refer to potentially complex or frequently used types, such as unions, intersections, or tuple types.

Visit the following resources to learn more:

- [@official@Type Aliases](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#type-aliases)

## Type Compatibility

# Type Compatibility

TypeScript uses structural typing to determine type compatibility. This means that two types are considered compatible if they have the same structure, regardless of their names.

Here's an example of type compatibility in TypeScript:

    interface Point {
      x: number;
      y: number;
    }
    
    let p1: Point = { x: 10, y: 20 };
    let p2: { x: number; y: number } = p1;
    
    console.log(p2.x); // Output: 10
    

In this example, `p1` has the type `Point`, while `p2` has the type `{ x: number; y: number }`. Despite the fact that the two types have different names, they are considered compatible because they have the same structure. This means that you can assign a value of type `Point` to a variable of type `{ x: number; y: number }`, as we do with `p1` and `p2` in this example.

Visit the following resources to learn more:

- [@official@Type Compatibility](https://www.typescriptlang.org/docs/handbook/type-compatibility.html)

## Type Guards  Narrowing

# Type Guards / Narrowing

Type guards and narrowing are techniques in TypeScript used to refine the type of a variable within a specific scope. They allow you to tell the TypeScript compiler that a variable is more specific than its declared type, enabling you to safely perform operations that would otherwise result in type errors. This is particularly useful when dealing with union types or situations where the initial type of a variable is broad.

Visit the following resources to learn more:

- [@official@Type Guards - TypeScript Docs](https://www.typescriptlang.org/docs/handbook/2/narrowing.html#typeof-type-guards)

## Type Inference

# Type Inference

Type inference is the automatic deduction of the data type of an expression in a programming language. Instead of explicitly declaring the type of a variable, the compiler or interpreter can infer it based on the value assigned to it or how it's used within the code. This reduces the need for verbose type annotations, making code more concise and readable while still providing the benefits of type safety.

Visit the following resources to learn more:

- [@official@Type Inference](https://www.typescriptlang.org/docs/handbook/type-inference.html#handbook-content)

## Type Predicates

# Type Predicates

Type predicates are a way to refine the type of a variable within a TypeScript function. They're used to tell the TypeScript compiler that a specific condition guarantees a variable is of a certain type. Instead of the compiler inferring the type based on basic checks, a type predicate explicitly asserts that if a function returns `true`, the argument must be of the specified type.

Visit the following resources to learn more:

- [@official@Type Guards and Differentiating Types](https://www.typescriptlang.org/docs/handbook/2/narrowing.html#using-type-predicates)

## Typeof

# typeof Type Guards

`typeof` in TypeScript is a way to narrow down the type of a variable based on its JavaScript `typeof` operator result. This allows you to write more precise code by checking the type of a variable (like string, number, boolean, symbol, or object) and then treating it accordingly within a specific block of code. By inspecting a variable's fundamental JavaScript type, TypeScript can infer a more specific type within that conditional block, helping catch potential errors and enabling safer operations.

Visit the following resources to learn more:

- [@official@Type Guards and Differentiating Types](https://www.typescriptlang.org/docs/handbook/2/narrowing.html#typeof-type-guards)

## Types Vs Interfaces

# Types vs Interfaces

In TypeScript, both types and interfaces are ways to define the shape of an object. They specify what properties an object should have and the data type of those properties. Types can describe simple types like primitives (string, number, boolean) or more complex structures like unions and intersections, while interfaces are primarily used to define the structure of objects, including their properties and methods. The key difference lies in their extensibility and use cases.

Visit the following resources to learn more:

- [@official@Interfaces vs. Type Aliases](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#differences-between-type-aliases-and-interfaces)
- [@article@Interfaces vs Types in TypeScript](https://stackoverflow.com/questions/37233735/interfaces-vs-types-in-typescript)

## Typescript Functions

# TypeScript Functions

Functions in TypeScript are reusable blocks of code designed to perform specific tasks. They can accept inputs (parameters), process them, and return a result. TypeScript enhances JavaScript functions by adding type annotations to parameters and return values, enabling better code clarity and error checking during development. This helps ensure that functions receive and produce the expected data types, leading to more robust and maintainable code.

Visit the following resources to learn more:

- [@official@Functions in TypeScript](https://www.typescriptlang.org/docs/handbook/2/functions.html)

## Typescript Interfaces

# TypeScript Interfaces

Interfaces in TypeScript are a way to define a contract for the structure of an object. They describe the shape that an object should have, specifying the names, types, and optionality of its properties. Essentially, an interface names a specific combination of fields and their types. These interfaces don't compile into JavaScript; they are purely a TypeScript construct used for type-checking during development.

Visit the following resources to learn more:

- [@official@TypeScript - Interfaces](https://www.typescriptlang.org/docs/handbook/2/objects.html)

## Typescript Modules

# TypeScript Modules

Modules in TypeScript (and JavaScript) are a way to organize code into reusable and manageable blocks. Each module encapsulates its own variables, functions, classes, and interfaces, preventing naming collisions and promoting code modularity. Modules explicitly export parts that other code can use and import modules to gain access to their exported functionalities.

Visit the following resources to learn more:

- [@official@Modules](https://www.typescriptlang.org/docs/handbook/modules.html#handbook-content)
- [@video@TypeScript - Modules](https://www.youtube.com/watch?v=EpOPR03z4Vw)

## Typescript Types

# TypeScript Types

TypeScript Types define the kind of values a variable can hold. They essentially act as labels that specify the allowed data types, like numbers, strings, or more complex objects. By assigning types, TypeScript can perform static type checking, catching potential errors during development before the code is even run. This helps improve code reliability and makes it easier to understand how data flows through your application.

Visit the following resources to learn more:

- [@official@TypeScript - Everyday Types](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html)
- [@feed@Explore top posts about TypeScript](https://app.daily.dev/tags/typescript?ref=roadmapsh)

## Typescript Vs Javascript

# TypeScript vs JavaScript

TypeScript and JavaScript are both programming languages used for web development. JavaScript is a dynamic language that is interpreted at runtime by the browser, meaning that type errors are only caught when the code is executed. TypeScript, on the other hand, is a superset of JavaScript that adds optional static typing. This allows developers to catch errors during development and before runtime, leading to more robust and maintainable code. TypeScript code must be compiled into JavaScript before it can be run in a browser or other JavaScript environment.

Visit the following resources to learn more:

- [@official@Learning JavaScript and TypeScript](https://www.typescriptlang.org/docs/handbook/typescript-from-scratch.html#learning-javascript-and-typescript)
- [@article@TypeScript vs. JavaScript](https://thenewstack.io/typescript-vs-javascript/)
- [@feed@Explore top posts about JavaScript](https://app.daily.dev/tags/javascript?ref=roadmapsh)

## Typing Functions

# Typing Functions

Functions in programming are reusable blocks of code that perform specific tasks. Typing functions in TypeScript means defining the types of the parameters a function accepts and the type of value it returns. This allows the TypeScript compiler to verify that functions are used correctly, preventing type-related errors at runtime and enhancing code maintainability and readability.

Visit the following resources to learn more:

- [@official@TypeScript Functions](https://www.typescriptlang.org/docs/handbook/2/functions.html)

## Undefined

# undefined

JavaScript has two primitive values used to signal absent or uninitialized value: `null` (absent) and `undefined` (uninitialized).

TypeScript has two corresponding _types_ by the same names. How these types behave depends on whether you have the `strictNullChecks` option on.

With `strictNullChecks` off, values that might be `null` or `undefined` can still be accessed normally, and the values `null` and `undefined` can be assigned to a property of any type. This is similar to how languages without `null` checks (e.g. C#, Java) behave. The lack of checking for these values tends to be a major source of bugs; TypeScript always recommend people turn `strictNullChecks` on if it’s practical to do so in the codebase.

With `strictNullChecks` on, when a value is `null` or `undefined`, you will need to test for those values before using methods or properties on that value. Just like checking for `undefined` before using an optional property, we can use narrowing to check for values that might be `null`:

    function doSomething(x: string | null) {
      if (x === null) {
        // do nothing
      } else {
        console.log('Hello, ' + x.toUpperCase());
      }
    }

Visit the following resources to learn more:

- [@official@null and undefined](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#null-and-undefined)

## Union Types

# Union Types

Union types allow a variable to hold values of different types. This means you can specify that a variable can be, for example, either a `string` or a `number`. You define a union type using the pipe (`|`) symbol to separate the possible types. This provides flexibility in situations where a variable might accept multiple different data types.

Visit the following resources to learn more:

- [@official@Union Types in TypeScript](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#union-types)

## Unknown

# Unknown Type

The `unknown` type in TypeScript represents a value that can be anything. Unlike `any`, which essentially disables type checking, `unknown` forces you to perform type checks or type assertions before you can perform operations on a value declared as `unknown`. This helps prevent unexpected errors at runtime by ensuring you've handled the potential type of the value.

Visit the following resources to learn more:

- [@official@Unknown Type in TypeScript](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-3-0.html#new-unknown-top-type)

## Useful Packages

# Useful Packages

TypeScript has a large ecosystem of packages that can be used to extend the language or to add functionality to your project.

Visit the following resources to learn more:

- [@official@zod](https://zod.dev/)
- [@official@ts-node](https://typestrong.org/ts-node)
- [@opensource@ts-morph](https://github.com/dsherret/ts-morph)
- [@opensource@ts-jest](https://github.com/kulshekhar/ts-jest)
- [@opensource@typesync](https://github.com/jeffijoe/typesync)

## Utility Types

# Utility Types

Utility Types in TypeScript are built-in generic types that perform common type transformations. They allow you to create new types based on existing ones by applying operations like making properties optional, required, readonly, or picking specific properties. These utilities enhance type safety and code reusability by enabling you to express complex type manipulations in a concise and declarative way.

Visit the following resources to learn more:

- [@official@TypeScript - Utility Types](https://www.typescriptlang.org/docs/handbook/utility-types.html)
- [@article@TypeScript Utility Types Guide](https://camchenry.com/blog/typescript-utility-types)

## Void

# Void Type

The `void` type in TypeScript represents the absence of a value. It is commonly used as the return type of functions that do not return any value, essentially indicating that the function performs an action but doesn't produce a result. A function declared with a `void` return type is not expected to return any data back to the caller.

Visit the following resources to learn more:

- [@official@void - TypeScript Docs](https://www.typescriptlang.org/docs/handbook/2/functions.html#void)
