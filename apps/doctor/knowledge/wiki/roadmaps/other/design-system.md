# Design System Roadmap

## Ab Tests  Experiments

# A/B Tests and Experiments

Understand how the team implements A/B tests and experiments on different screens and if the new design system should accommodate any necessary requirements.

## Accessibility Testing

# Accessibility Testing

Design systems should cover accessibility as much as possible. Making this automatic reduces the risk of inaccessible components or user flows in the product.

## Accessibility

# Accessibility

For icons that convey a meaning or serve a function, add the necessary support for screen readers. You can skip this for decorative icons.

## Accessibility

# Accessibility

Guidelines for how you approach accessibility and how you leverage colour, hierarchy and assistive technologies to help your users.

Visit the following resources to learn more:

- [@article@Introduction to Web Accessibility](https://www.w3.org/WAI/fundamentals/accessibility-intro/)
- [@article@What is Accessibility? by Mozilla](https://developer.mozilla.org/en-US/docs/Learn/Accessibility/What_is_accessibility)
- [@article@Accessibility Principles](https://www.w3.org/WAI/fundamentals/accessibility-principles/)
- [@article@WebAIMs Website (Web Accessibility In Mind)](https://webaim.org/)
- [@article@WAVE Web Accessibility Evaluation Tool](https://wave.webaim.org/)
- [@feed@Explore top posts about Accessibility](https://app.daily.dev/tags/accessibility?ref=roadmapsh)

## Accessibility

# Accessibility

Make sure to have accessible pairings between the main colours in your palette. More importantly, make sure that your background and text colours have at least an AA standard contrast ratio between them.

## Avatar

# Avatar

Avatars represent users or entities in interfaces. They should support multiple shapes (circular, square), various sizes, handle missing images with initials or default icons, include status indicators, maintain image quality standards, ensure accessibility, provide loading states, and support group arrangements with proper interactive feedback.

## Avatar

# Avatar

Avatars are used to show a thumbnail of a user photo or a visual representation of any other type of content.

- **Image:** Avatars should mask an image into their shape and work with any image size since they may get this image from unknown data sources.
- **Image Fallback:** There should be fallbacks when there’s no image available. This can be done with placeholder images or initials.
- **Accessibility:** Always provide a description for screen readers describing what’s displayed on the avatar image instead of just naming its role.
- **Sizes:** There are many contexts to use avatars and they all require different sizes for the component. For average projects use at least 2-3 different sizes and make sure there’s at least a small size available.
- **Icon:** Avatars can be used with an icon instead of an image to emphasize areas that don’t necessarily have (or need) an image associated with it.
- **Background Colors:** When used with icons or text, there has to be a background colour from the design system colour tokens applied to the avatar shape. Make sure that icons and text have enough contrast ratio with the background according to the WCAG AA standard.

## Badge

# Badge

Badges are elements that represent the status of an object or user input value.

- **Appearance:** Badges may play various roles in your product and having a predefined colour for each role should help users understand their meaning. When changing colours, make sure the text has enough contrast ratio with the background according to the WCAG AA standard.
- **Dismissible Action:** Badges can be used as a dynamic way to display selected values and there should be a way to dismiss them.

## Badges

# Badges

Badges are small status indicators that communicate information about objects or actions. Effective design should include numeric indicators for notifications, status badges with distinct colors, category labels, interactive states, multiple sizes, semantic color integration, consistent positioning, content guidelines, and proper accessibility.

## Banner

# Banner

Banners display an actionable message used as a prominent way of communicating with your users.

- **Appearance:** Banners are used to display different types of messages and it’s important to differentiate their visual appearance based on the role they’re playing. If you’re using background colours for role differentiation, make sure there’s enough contrast ratio with the content according to the WCAG AA standard.
- **Area for icons or images:** Banners can supplement their message using a supporting icon or image. They shouldn’t be used instead of text content.
- **Actions:** Actions in banners should relate to its text and provide a way to react to the message sent to the user.
- **Dismissible Action:** Don’t overwhelm the user with banners on the page and include a dismissable action. That may be either a separate close button or one of the actions provided.
- **Accessibility:** If a banner dynamically appears on the page, it should be announced to the user by their assistive technology.
- **Responsiveness:** Banners should adapt to the viewport size. This usually means that they become full-width for mobile to save some space.

## Banners

# Banners

Banners communicate important information at the top of pages. They should support different message types with distinct visuals, various positioning options, clear dismissal mechanisms, relevant actions, consistent iconography, mobile adaptations, subtle animations, content guidelines, proper accessibility, and stacking rules for multiple banners.

## Breakpoints

# Breakpoints

Predefine the screen sizes and orientations your grid will adapt to.

## Button

# Button

Buttons are interactive elements used for single-step actions.

- **Hover State:** Clearly show that the button is interactive when it gets hovered with a mouse cursor.
- **Active State:** Used when a button gets pressed. The same state can be used to represent the button responsible for toggling another element on the page while that element is visibly opened.
- **Focused State:** Used when a button gets selected through keyboard navigation.
- **Icon Support:** Icons easily communicate the purpose of the button when used next to its label or can be used without text when there’s not enough space. Make sure that the accessibility label is provided when used with an icon only.
- **Disabled:** Visually shows that a button is not interactive and restricts it from being pressed.
- **Loading:** Used when users have to wait for the result of their action after they press a button. If a spinner is used to display this state make sure that it’s not changing the original button width or height.
- **Full Width:** By default buttons take the width of their content, but they should also come with a full width variant that works well in mobile devices.
- **Variants:** When using multiple buttons, there should be a way to differentiate between primary and secondary actions. Buttons may play different roles for the user or be used on different types of surfaces and they have to change the way they look.
- **Sizes:** Buttons can be used in different areas of the website and may have multiple predefined sizes. On mobile, tappable areas have to be a minimum of 48px to be accessible according to iOS and Android accessibility guidelines.

## Buttons

# Buttons

Buttons enable user actions and require clear visual hierarchy (primary, secondary, tertiary), comprehensive interactive states, multiple sizes, icon support, content guidelines, minimum 44px touch targets, loading indicators, responsive behavior, proper accessibility with ARIA labels, and subtle animations.

## Card

# Card

Cards are used to group information about subjects and their related actions.

- **Supports any type of content:** Cards are one of the most used components in the product, so they have to be flexible enough to support any other components placed in them.
- **Information structure:** No matter how flexible cards are, it’s important for cards to have a specific structure for its elements for product consistency.
- **Supports media sections:** One of the most popular scenarios for using cards is mixing them with media content. The most popular options are having a full-width area on top of the content or full-height area at one of the card’s sides.
- **Supplementary actions:** Cards can be used with actions usually placed at the bottom of the card, or the card itself can be tappable and represent an action.
- **Responsiveness:** On mobile viewports cards are usually full-width in order to save space for the content.

## Cards

# Cards

Cards are flexible content containers that group related information and actions. They require clear content hierarchy, consistent elevation systems, responsive behavior, distinct interactive states, media support, defined action areas, content variants, loading states, proper accessibility, and consistent spacing aligned with the design system.

## Carousel

# Carousel

Carousels stack the same type of items and allows scrolling through them horizontally.

- **Navigation Controls:** Carousels should have easy-to-find navigation controls for scrolling through content.
- **Supports any content:** Carousels can be used in different contexts and shouldn’t be limited to a specific child component. In some scenarios you might want items within the same carousel to differ from each other.
- **Items width customisation:** For simple products, it might be fine to use multiple predefined sizes for carousel items. For more flexibility, it’s good to provide a way to define a custom width.
- **Touch events support:** Carousels should be scrollable on touch devices. Some of the best practices are to use native scrolling and to make sure you’re supporting the same behaviour for all touch devices, not just mobile phones.
- **Keyboard navigation:** It should be possible to scroll through content with keyboard arrows when focused on navigation controls.
- **Responsiveness:** It’s good practice to hide or reduce the size of navigation controls for mobile viewports to improve the visibility of the content.

## Code Style

# Code Style

Having a defined code style helps align the way code’s written in the system and increases development velocity. It should be automated with the tools provided for each platform.

## Color

# Color

Color establishes brand identity and visual hierarchy in design systems. A comprehensive color system should organize colors logically, meet WCAG accessibility standards, support light/dark themes, create semantic categories, establish systematic naming, balance brand expression with function, and provide multiple formats.

## Commit Guidelines

# Commit Guidelines

Automate the generation of your changelog by adopting a commit message guidelines that categorise and define the changes being made.

## Communication Channel

# Communication Channel

Most product development work happens digitally, so create a digital channel where people can reach out and ask questions.

## Community Meetings

# Community Meetings

Arrange community meetings with everyone who uses the design system. Share your knowledge and make proposals to improve the sense of community.

## Component Analytics

# Component Analytics

Track the usage of your components. For development you can use built-in tools like Figma’s Design System Analytics. For the end product you can have a separate way of tracking per platform depending on the technology.

## Component Catalog

# Component Catalog

Isolate your UI components’ environment outside of your product codebase to make sure they’re not dependent on any global dependencies and can be easily reused.

## Component Library

# Component Library

A component library is a collection of all the components used in a website, software or app. Some of the common tools to showcase and browse components in a component library include are given below:

Visit the following resources to learn more:

- [@article@Pattern Lab](https://patternlab.io/)
- [@article@Fractal](https://fractal.build/)
- [@article@Storybook](https://storybook.js.org/)

## Component

# Component

Components are the reusable building blocks of a design system. Each component meets a specific interaction or UI needs, and is specifically created to work together to create patterns and intuitive user experiences.

## Contribution Guidelines

# Contribution Guidelines

Define the process of contributing to the UI and UX of the design system and document it in a discoverable place to make it easier for everyone to contribute.

## Contribution Guidelines

# Contribution Guidelines

Define the process of contributing to the code of the design system. Document everything in a discoverable place to make it easier for everyone to contribute.

## Creating Core Components

# Core Components

Components are the main building blocks for user interfaces. Building a reusable component library enhances your product development workflow by reducing design and tech debt and speeding up the process. Core components can’t be broken down into granular pieces without losing their meaning.

## Creating Design Language

# Design Language

Like any language, a design language is a methodical way of communicating with your audience through your approach to product design. It’s the cornerstone of consistent customer experiences.

Visit the following resources to learn more:

- [@article@What is a Design Language.. really?](https://medium.com/thinking-design/what-is-a-design-language-really-cd1ef87be793)
- [@article@How to Develop a Design Language](https://xd.adobe.com/ideas/principles/web-design/how-to-develop-design-language/)
- [@article@What Actually Constitutes Design Language?](https://www.uxpin.com/studio/blog/design-language/)
- [@article@Visual Design Language: The Building Blocks Of Design](https://www.smashingmagazine.com/2020/03/visual-design-language-building-blocks/)

## Dark Mode

# Dark Mode

Preparing a dark mode version of your colour palette will allow your design system to adapt to dark mode and respect what your user wants to see.

## Defining Design Tokens

# Design Tokens

Variables that store values for the base layer of your design system, like colour and typography. They’re used in components, so changes on this level will resonate throughout the whole system.

Visit the following resources to learn more:

- [@article@What Are Design Tokens?](https://xd.adobe.com/ideas/principles/design-systems/what-are-design-tokens/)

## Design Editor

# Design Editor

There are many design editors available in the market today with the most popular names being Sketch, Figma and Adobe XD. If you're unsure which route to go down it's often best to speak with your team.

## Design Language

# Design Language

A design language or design vocabulary is an overarching scheme or style that guides the design of a complement of products or architectural settings, creating a coherent design system for styling.

Visit the following resources to learn more:

- [@article@What is a Design Language.. really?](https://medium.com/thinking-design/what-is-a-design-language-really-cd1ef87be793)
- [@article@How to Develop a Design Language](https://xd.adobe.com/ideas/principles/web-design/how-to-develop-design-language/)
- [@article@What Actually Constitutes Design Language?](https://www.uxpin.com/studio/blog/design-language/)
- [@article@Visual Design Language: The Building Blocks Of Design](https://www.smashingmagazine.com/2020/03/visual-design-language-building-blocks/)

## Design Principles

# Design Principles

The considerations that guide the basis of your practice. They outline how you approach design from a philosophical perspective and help with everyday decisions.

## Design System Examples

# Design System Examples

Visit the following resources to learn more:

- [@article@Material Design (Google)](https://material.io/)
- [@article@Carbon Design System (IBM)](https://carbondesignsystem.com/)
- [@article@Atlassian Design System](https://atlassian.design/)
- [@article@Polaris Design System (Shopify)](https://polaris.shopify.com/)
- [@article@Gov.uk Design System](https://design-system.service.gov.uk/)
- [@opensource@Collection of Open Source Design Systems](https://github.com/alexpate/awesome-design-systems)

## Design System Vs Component Library

# Design System vs Component Library

A component library is just a collection of visuals i.e. colours, button stylings, fonts, etc. A Design System takes it to the next level by including standards and documentation around the look and usage of each component. The Design System acts as the single-source of truth.

Visit the following resources to learn more:

- [@article@A Design System: So Much More Than A Component Library](https://www.architech.ca/a-design-system-so-much-more-than-a-component-library)
- [@article@Design System vs UI Component Library vs Brand Style Guide](https://prototype.net/blog/design-system-component-library-style-guide)
- [@article@Design Systems vs Pattern Libraries vs Style Guides vs Component Libraries](https://www.uxpin.com/studio/blog/design-systems-vs-pattern-libraries-vs-style-guides-whats-difference/)

## Documentation

# Documentation

Organize and document the results of visual audit, design elements, components with variations, states, patterns found, any existing documentation, current design process, and considerations. This documentation will be shared across the team and act as a guide when building the new design system.

## Documentation

# Documentation

Having your code documented is key to driving adoption and reducing the load on the contributors.

## Dropdown

# Dropdown

Dropdowns are used to display a contextual subview with a list of actions or content related to the area where the dropdown is.

- **Supports any type of content:** Dropdowns may be used in a lot of contexts like date pickers, language selection or other product features.
- **Action Menu:** One of the most used scenarios for dropdowns is providing an action menu for the user, so it’s useful to have this layout defined.
- **Focus Trapping:** Once the dropdown’s opened, the focus should work only for elements inside the dropdown. When it’s closed, the focus should move to the dropdown trigger.
- **Close Action:** Either some actions inside the dropdown should close it or there should be a separate close button. Also, it’s good practice to close the dropdown when a user clicks outside.
- **Keyboard Navigation:** It should be possible to navigate through dropdown children elements with the keyboard and close it with an Esc key.
- **Dynamic Position:** Dropdown content should be displayed based on the current position of the trigger element on the screen and always visible to the user.
- **Responsiveness:** Dropdown content should be adapted for mobile viewpoints as it may take a lot of space on desktops.

## Dropdowns

# Dropdowns

Dropdowns reveal option lists when activated to save space. They need clear triggers with visual indicators, organized options with grouping, search/filtering for long lists, multi-select support, smart positioning, full keyboard navigation, loading states, mobile adaptations, proper accessibility, and performance optimization.

## Existing Design Analysis

# Existing Design Analysis

First step in creating a design system from an existing design is performing a design analysis and understanding what you will be working with to identify the requirements and prepare a plan. Performing the analysis may consist of:

- Understanding the Existing Design Process
- Performing Visual Audit
- Identifying Design Elements
- Identify Common Components
- Understanding the A/B Testing and Experimentation Needs
- Understanding any Locale or regional requirements (such as LTR/RTL).
- Documenting your findings

## Faqs

# FAQs

To save everyone time, define which questions are asked frequently by your audience and document them in a discoverable place.

## File Formats

# Different File Formats

Providing a variety of formats for the vector version of your logo will make it easier for others to work and prevent anyone from redrawing it.

- [@article@What is a Vector Logo and Why You Need It](https://www.renderforest.com/blog/vector-logo)

## Forms

# Forms

Forms collect user input and require standardized input components, comprehensive validation systems, effective labeling strategies, consistent layouts, clear error handling, progressive disclosure, required field indicators, auto-complete integration, proper accessibility, and mobile optimization.

## Functional Colors

# Functional Colors

Besides your brand colours, make sure to have colours defined and made into variables for functions like disabled states, backgrounds, actions and high contrast text.

## Governance

# Governance

Governance is a framework for clarifying roles, responsibilities, and authority over decisions. Having that clarity ensures that decisions for the design system funnel smoothly through the governance process

Visit the following resources to learn more:

- [@article@Governance is a design system’s friend](https://zeroheight.com/blog/governance-is-a-design-systems-friend)
- [@article@Design System Governance – Scale Your Design](https://www.uxpin.com/studio/blog/design-system-governance/)
- [@article@Governance by design: Building successful design systems](https://rangle.io/blog/governance-by-design-building-successful-design-systems/)
- [@article@Team Models for Scaling a Design System](https://medium.com/eightshapes-llc/team-models-for-scaling-a-design-system-2cf9d03be6a0)

## Grid Relation

# Grid Relation

Draw your icons in a bounding box that plays well with your grid. This makes for a better pairing with other UI elements. A good example of this would be icons with bounding boxes paired with text.

## Grid Relation

# Grid Relation

Font sizes and leading should match your grid to allow better pairing between text and other UI elements. A good example of this is text paired with icons with bounding boxes.

## Grid

# Grid

Every layout should sit on a grid that brings order and hierarchy to the interface. Define a grid separately for mobile, tablet and desktop devices with columns, gutters, and margins so your interface can adapt to any platform easily.

## Guidelines

# Guidelines

Provide guidelines on how and when to use the pairings in your typography scale, what to keep in mind when working with them and how not to use them.

## Guidelines

# Guidelines

Provide guidelines on how and when to use the colours in your palette, what to keep in mind when working with them and how not to use them.

## Guidelines

# Guidelines

Provide guidelines on how and when to use icons, what to keep in mind when working with them and how not to use them.

## Guidelines

# Guidelines

Design guidelines are sets of recommendations on how to apply design principles to provide a positive user experience. Designers use such guidelines to judge how to adopt principles such as intuitiveness, learnability, efficiency and consistency so they can create compelling designs and meet and exceed user needs.

Visit the following resources to learn more:

- [@article@Design Guidelines](https://www.interaction-design.org/literature/topics/design-guidelines)

## Icon

# Icon

The icon component is a way to align the way iconography static assets are displayed in the product.

- **Sizes:** Icons should have a number of predefined sizes to provide a holistic experience across the product. Typography pairings may be used for these size values to ensure that they are aligned with the text sizes.
- **Colors:** Icons should be using values from the design system colour palette. Using parent element text colour for icon fill colour can make this automatic.

## Icons

# Icons

Icons are visual symbols that communicate meaning quickly. They should maintain consistent style, use a grid system, provide multiple sizes, organize into semantic categories, ensure accessibility, consider cultural neutrality, be available in multiple formats, include interactive states, and follow systematic versioning.

## Identify Existing Design Process

# Existing Design Process

To better understand the kind of design system you would like to implement, you need to start by reviewing and analyzing the current approach for design at your company. Find the answers to the following questions:

- What is the design process that your company follows?
- What are the existing tools that your company uses?

It’s also recommended to evaluate the level of design maturity of the product teams. This knowledge will help you estimate the time required to introduce the system to your organization.

## Input Checkbox

# Input Checkbox

An input checkbox is a form element used for selecting one or multiple options.

- **Checked State:** Used when the checkbox is selected and will use its value for the form submission.
- **Disabled State:** Prevents checkbox interactions and removes its value from the form submission.
- **Intermediate State:** Used when the checkbox has children selectable elements and only some of them are selected.
- **Label:** There should be a text label linked with the checkbox field. Clicking the label should also trigger the checkbox selection.
- **Error State:** The error state is used for form validation errors when the error is related to the checkbox field only. Always use a text error along with changing the colour of the field.
- **Keyboard State:** Checkbox selections should be triggered with the Space key. Using native elements for this should provide this kind of interaction out of the box.
- **Checkbox Group:** Checkboxes can be grouped to work with multiple values at the same time.

## Input Radio

# Input Radio

An input radio is a form element used for selecting one option from a list.

- **Checked State:** Used when the radio is selected and will use its value for the form submission. A radio input can’t be unselected by pressing it again.
- **Disabled State:** Prevents radio interactions and removes its value from the form submission.
- **Label:** There should be a text label linked with the radio field. Clicking the label should also trigger the radio selection.
- **Error State:** The error state is used for form validation errors when the error is related to the radio field only. Always use a text error along with changing the colour of the field.
- **Keyboard State:** A radio selection should be triggered when the Space key is pressed. Using native elements for this should provide this kind of interaction out of the box.
- **Radio Group:** Radio inputs should always be used in a group. If one of them is selected, it can be deselected only by choosing another radio.

## Input Switch

# Input Switch

Input switches toggle the state of a single item. Compared to the input checkbox, their changes usually apply without any additional submission.

- **Checked State:** Used when an input switch is turned on. It’s better to provide an additional way to indicate the checked state besides changing its colour when applicable.
- **Disabled State:** Prevents interacting with an input switch.
- **Label:** There should be a text label linked with the switch field. Clicking the label should also trigger the input selection.
- **Keyboard State:** A switch selection should be triggered when the Space key is pressed.

## Input Text

# Input Text

Input text lets users enter and edit text.

- **Disabled State:** Prevents input interactions and removes its value from the form submission.
- **Placeholder:** When there’s no value entered, show a placeholder with a potential value example. Don’t use placeholders as labels for the inputs.
- **Label:** There should be a text label linked with the text field. Clicking the label should move the focus to the field.
- **Error State:** The error state is used for form validation errors when the error is related to the text field only. Always use a text error along with changing the colour of the field.
- **Focused State:** The focused state should highlight the text field when users start to interact with it. There is always only one focused field in the form.
- **Autocomplete:** When applicable, adding support for the HTML autocomplete attribute will allow users to easily enter different data types.
- **Icon Support:** Icons are used to describe input methods, express a text field state or provide additional functionality.

## Keywords

# Keywords

Adding keywords will improve the discoverability of each icon and provide a better user experience for anyone using your system.

## List

# List

Lists define the layout of the page content or groups of elements stacking them vertically or horizontally.

- **Support any type of content:** Lists can be used in any context from page-level layout to managing offsets between granular components. hey should work with any component used inside.
- **Horizontal Stacking:** Lists can be used for inline elements and they have to manage how they’re stacked horizontally, including handling offsets between multiple rows of elements.
- **Divided Variant:** Lists with dividers are the best practice advised by many platform guidelines (especially on mobile).
- **Supports Actionable Content:** Sometimes lists are used for grouping tappable components, where the whole area of the list item should be clickable.

## Loading Indicator

# Loading Indicator

The loading indicator shows that an operation’s being performed and how long the process will take.

- **Linear and non-linear Variants:** Depending on the context and the component it’s used for, the loading indicator can be represented either with linear or with a non-linear (e.g. circular) variant.
- **Determinate or indeterminate wait time:** In some cases, the wait time can’t be determined. The loading indicator should be shown until the loading finishes or an error happens. In other cases, it’s better to indicate how much time’s left until the loading is done.
- **Light Variant:** The loading indicator should respect its parent element background and provide a variant to be used on darker background colours.
- **Reduced Motion:** The loading indicator should be synced with the system motion settings and reduce its animation speed when reduced motion settings are turned on.

## Logging

# Error Logging

Implement a way to track and pinpoint component-related outages in your product.

## Making A Design System

# Making a Design System

First step in building a design system is identifying [if you even need a design system](https://sparkbox.com/foundry/when_not_to_use_a_design_system).

Visit the following resources to learn more:

- [@video@Introducing Design Systems Into Chaos - Diana Mounter, GitHub](https://www.youtube.com/watch?v=FZSi1bK-BRM)
- [@video@Design Systems, when and how much?](https://www.youtube.com/watch?v=Hx02SaL_IH0)
- [@article@Design Systems: Step-by-Step Guide to Creating Your Own](https://www.uxpin.com/create-design-system-guide/)
- [@article@Does My Organization Need a Design System?](https://www.method.com/insights/does-my-organization-need-a-design-system/)
- [@video@Create a Design System with Figma - Full Course](https://www.youtube.com/watch?v=RYDiDpW2VkM)

## Making It From Existing Design

# From Existing Design

If you are creating a Design System from pre-existing product design, there is an additional step to perform the existing design analysis, understand the existing design process, perform a visual audit, identify design elements and components and so on.

Visit the following resources to learn more:

- [@video@Create a Design System with Figma - Full Course](https://www.youtube.com/watch?v=RYDiDpW2VkM)

## Making It From Scratch

# From Scratch

If you are building a Design System from Scratch, you may skip the "Existing Design Analysis" node of the roadmap and start with "Creating Design Language".

Visit the following resources to learn more:

- [@video@Create a Design System with Figma - Full Course](https://www.youtube.com/watch?v=RYDiDpW2VkM)

## Microcopy Guidelines

# Microcopy Guidelines

The standard way to write for the components in your design system. These take platform conventions and best practices for writing all into consideration.

## Milestones

# Milestones

Define milestones that act as bigger epics in your project management with the help of your roadmap. These will help you understand your progress.

## Modal

# Modal

Modals are containers appearing in front of the main content to provide critical information or an actionable piece of content.

- **Supports any type of Content:** Like any other container, modals can be used in different scenarios and you should be able to use it with any other component inside.
- **Supplementary Actions:** Since content in the modal may be actionable, it’s important to have an area for action elements. This area is usually located at the bottom of the modal container.
- **Close Action:** Modals should provide a clear way to be closed as they’re blocking content when open. This may be either a separate close button or one of the supplementary actions.
- **Information Structure:** Even though modals can be used as an empty container for the content, they need a defined information structure to provide a holistic experience. It may include defining how titles and subtitles look by default or where an action element’s area is.
- **Keyboard Navigation Support:** It should be possible to close a modal by pressing the Esc key and all the focusable elements inside the modal container should be accessible with keyboard navigation.
- **Focus Trapping:** Once a modal is opened, the focus should be moved to the first element inside the modal and should be looped within the modal container. Closing the modal should return the focus to the last focused element on the page.

## Monochrome Version

# Monochrome Version

A monochrome version of your logo that looks good on top of photography or when it’s printed with a poor quality printer.

## Naming

# Naming

Name your icons based on what they are, not what they represent. For instance, a trash icon should be named trash, not delete. You can still add related keywords to improve discoverability.

## Need Of Design System

# Need of design system

Having a solid design system speeds up your work by making the product team more efficient, and it creates consistency and harmony within the product and brand ecosystem. A strong design system takes the burden off individual designers to think through commonly recurring design problems. With a full library of pre-approved elements, designers can focus on bigger problems like creating seamless, intuitive flows that delight users. That kind of efficiency pays huge dividends over time.

Visit the following resources to learn more:

- [@video@Design Systems, when and how much?](https://www.youtube.com/watch?v=Hx02SaL_IH0)
- [@article@Why You Need a Strong Design System (and How to Build One)](https://www.drawbackwards.com/blog/why-you-need-a-strong-design-system-and-how-to-build-one)
- [@article@On Design Systems: Sell The Output, Not The Workflow](https://www.smashingmagazine.com/2016/05/design-systems-responsive-design-sell-output-not-workflow/)

## Open Hours

# Open Hours

Create open hours in which you can engage your audience in a more private setting where you can discuss things in more detail. You can also use these as peer coding or peer design opportunities.

## Other

# Other Components

Specialized elements beyond core components include badges for notifications, breadcrumbs for navigation, progress indicators, tooltips for help, pagination for browsing, tab systems, accordions for collapsible content, modals for focused interactions, notification systems, and basic data visualization elements.

## Pattern

# Pattern

Patterns are best practice design solutions for specific user-focused tasks and page types. Patterns often use one or more components and explain how to adapt them to the context. Some sample patterns could be user signing in to the application or performing the checkout operation.

## Performance

# Performance

Custom fonts need to be downloaded before they can be displayed, especially on the web. Make sure that you have sensible fallbacks and fast loading time for your typography assets. Using system fonts solves this performance problem.

## Performing A Visual Audit

# Visual Audit

Take screenshots of your current product with the help of your team. You can use any presentation software like Google Slides or print and pin them on foam-core boards. Group the screenshots into categories like buttons, navigation, forms, tables, charts, lists etc.

Now, review each category to find inconsistencies and note areas for improvement with your team. Use a tool like [CSS Stats](https://cssstats.com/) to see how many unique colors, typefaces you have in your style sheets.

## Pilot

# Pilot

Pilots are one of the best ways to put your design system through its paces, especially before the design system even gets to a v1. Like television pilots help test audience reactions to a series concept without investing significant resources to create the whole thing, application pilots are a good foundation for ensuring your design system’s design and code are battle-tested.

Visit the following resources to learn more:

- [@official@Design Systems: Pilots & Scorecards](https://danmall.com/posts/design-systems-pilots-scorecards/)
- [@article@How to run a design system pilot](https://university.obvious.in/product-design/design-system/how-to-run-a-design-system-pilot)

## Placement Guidance

# Placement Guidance

Logo placement guidance ensures consistent brand representation through clear positioning, sizing, and clearance rules. Effective guidelines should define minimum clearance areas, establish preferred positions for different contexts, provide size specifications, define background treatments, and account for platform-specific requirements.

## Plugins

# Plugins

Most popular Design Editors (Sketch and Figma, especially) come with third-party plugin support. Whilst it's best to use the editors in-built tools for laying out your components, plugins can bring in a range of useful data to populate them.

## Pr Templates

# Pull Request Templates

Create pull request templates that outline the change being proposed to facilitate productive discussions.

## Project Management

# Project Management

Design systems are no different than any other project your team might take on. In order to successfully build and maintain one, you need a clear strategy that’s well executed daily, and you‘ll need to create opportunities for your colleagues to give feedback to help share your design system together.

## Readability

# Readability

Optimising the letter spacing (tracking), line height (leading) and line length for your typography scale will help with the readability of text.

## Regional Requirements

# Regional Requirements

Understand any regional requirements such as LTR or any other UX variations that your design system should accommodate.

## Release Strategy

# Release Strategy

Design system releases should be automated and ideally use scripts ran locally or in remote CI pipelines to prevent broken releases.

## Reserved Icons

# Reserved Icons

Reserving icons that represent common actions will prevent their use in any other context. System icons for navigation or adding and deleting are a good example. This leads to a more intuitive user experience.

## Responsiveness

# Responsiveness

Desktop devices can usually afford to have bigger font sizes compared to mobile devices. Creating a typography scale that adapts to the viewport size will help with a more meaningful hierarchy and layout.

## Roadmap

# Roadmap

Setting your short and long term vision and mapping things out helps you decide the steps to take, understand your place in the bigger picture and prioritise day-to-day tasks.

## Select

# Select

Select lets user select a value from a list of values in a form context:

- **Disabled State:** Prevents input interactions and removes its value from the form submission.
- **Placeholder:** When there’s no value entered, show a placeholder with a potential value example. Don’t use placeholders as labels for the inputs.
- **Label:** There should be a text label linked with the text field. Clicking the label should move the focus to the field.
- **Error State:** The error state is used for form validation errors when the error is related to the text field only. Always use a text error along with changing the colour of the field.
- **Focused State:** The focused state should highlight the text field when users start to interact with it. There is always only one focused field in the form.
- **Autocomplete:** When applicable, adding support for the HTML autocomplete attribute will allow users to easily enter different data types.
- **Icon Support:** Icons are used to describe input methods, express a text field state or provide additional functionality.

## Semantic Versioning

# Semantic Versioning

Version your code with semantic versioning that dictates how version numbers are assigned and incremented.

## Service And Health Metrics

# Service and Health Metrics

Define service and health metrics for your design system to set a benchmark on how well you’re doing. Common examples can be the number of tickets closed, improvements made or bugs fixed.

## Sizes

# Sizes

Provide different sizes for icons that correlate to your grid. Provide a minimum size and remove unnecessary detail for your icons for smaller sizes.

## Sizing

# Sizing

Sizing tokens establish consistent dimensions across components and layouts. An effective system should establish a foundational unit, create predefined size variations, ensure minimum accessibility requirements, define standard icon sizes, establish container dimensions, implement fluid sizing, and account for platform-specific requirements.

## Small Use Guidance

# Small Use Guidance

Your logo must perform well and be recognisable at all sizes. Tips for using your logo in these cases will minimise the risk of it being misused.

- [@article@Everything You Need to Know About Logo Usage Guidelines](https://www.tailorbrands.com/blog/logo-usage-guidelines)

## Spaces

# Spacing

Spacing tokens define white space between elements, creating visual rhythm and clear relationships. An effective system should establish a foundational unit, create systematic scales, define consistent internal spacing, establish layout guidelines, implement fluid spacing, create meaningful categories, and ensure cross-platform consistency.

## Spacking

# Spacing

Horizontal and vertical rhythm plays a big role in a layout. You should provide easy methods for adding space between interface elements independent of your grid.

## Stakeholders Involved In Building

# Stakeholders

Building an effective design system is not an individual responsibility, you need more than just designers. Here’s a quick list of the disciplines that can be represented in your team to create an effective design system:

- **Designers:** to define the visual elements of the system
- **Frontend Developers:** To create modular efficient code
- **Accessibility Experts:** Accessibility experts to ensure your system conforms to standards like WCAG
- **Performance Experts:** who can ensure your system loads quickly on all devices
- **Content Strategists:** who can help the team nail the voice and tone of the system
- **Researchers:** who can help you understand customer needs
- **Product Managers:** to ensure the system is aligning to customer needs
- **Leaders:** (VPs and directors) to champion and align the vision throughout the company including up to executive leadership

Visit the following resources to learn more:

- [@article@Designing the Design System](https://www.designbetter.co/design-systems-handbook/designing-design-system)

## Style

# Style

Make sure that your icon family makes visual sense as a whole. Picking an outlined or filled style and sticking with it will lead to better visual consistency and predictability.

## Tabs

# Tabs

Tabs organise navigation between multiple pages or content sections.

- **Active Button State:** There should be a clear differentiation between selected and unselected tab buttons.
- **Button Icon Support:** Icons help show the purpose of the tab buttons when used next to its label.
- **Equally-sized tab buttons:** Tabs can be used in a relatively small-sized container where you need to switch between a definite number of sections. For such scenarios, it’s better to support a variant where the button’s area is divided equally.
- **Keyboard Navigation:** All tab buttons should be focusable and navigation between the tab’s component should be accessible from the keyboard.
- **Responsiveness:** If all tabs on mobile don’t fit into the viewport, users should still have access to all tab buttons. Ways to solve this can be making the button area scrollable for mobile or showing a More button containing a dropdown with the rest of the buttons.

## Terminology

# Terminology

Create the standard terms and phrases that need to be kept the same throughout the user experience, speeding up the design process and unifying your voice.

## Terminology

# Terminology

Design systems can be tricky if you don’t know what certain words mean. Have a look at the roadmap nodes as well as follow the link below to read the glossary.

Visit the following resources to learn more:

- [@article@Design Systems Glossary](https://web.archive.org/web/20220620075140/https://superfriendly.com/design-systems/glossary/)

## Textarea

# Textarea

Text area lets users enter and edit text.

- **Disabled State:** Prevents input interactions and removes its value from the form submission.
- **Placeholder:** When there’s no value entered, show a placeholder with a potential value example. Don’t use placeholders as labels for the inputs.
- **Label:** There should be a text label linked with the text field. Clicking the label should move the focus to the field.
- **Error State:** The error state is used for form validation errors when the error is related to the text field only. Always use a text error along with changing the colour of the field.
- **Focused State:** The focused state should highlight the text field when users start to interact with it. There is always only one focused field in the form.

## Ticketing

# Ticketing

Make it easier to track your day-to-day progress by using ticketing software like Jira, Trello or GitHub. This’ll make it easier for others to submit feature proposals or bug reports.

## Toast

# Toast

Toasts provide short meaningful feedback messages about the action results.

- **Dismissed Automatically:** Toast messages shouldn’t interrupt the user flow, block the screen for a long time or require additional action from the user.
- **Action Support:** Besides displaying the message, toasts may also provide an action related to the message like undoing an action.
- **Handles Multiple Instances:** Even though it doesn’t happen often, toasts can be called from multiple sources at the same time and all resulting toasts should be queued. It’s good practice not to show all the messages at the same time.
- **Accessibility:** Toast messages should be announced by the voice assistive technology and their action should be easily accessible from the keyboard.
- **Responsivenss:** Toasts should be aligned with the mobile viewport and their action should be easily reachable for tapping.

## Token

# Token

Design system tokens are the style values of UI elements such as color, typography, spacing, shadows, etc., that are used across products and capable of being converted to a format for any platform (web, mobile, desktop). Tokens are building blocks of the design system—think of them as sub atoms, the smallest pieces of style values that allow designers to create styles for a product.

Visit the following resources to learn more:

- [@article@What Are Design Tokens?](https://xd.adobe.com/ideas/principles/design-systems/what-are-design-tokens/)

## Tone Of Voice

# Tone of Voice

A clear tone of voice defines how you speak to your audience at every moment in their journey, helping them get wherever they want to go.

## Tooling Analytics

# Tooling Analytics

Track what tools are being used for your design system. Find out which ones are used the most and which features are the most popular.

## Tooling

# Tooling

Design system tooling encompasses technical infrastructure and workflows. Effective tooling should integrate with design tools, provide component libraries for frameworks, implement token management, utilize documentation platforms, establish automated versioning, create testing infrastructure, and enable collaboration workflows.

## Tooltip

# Tooltip

Tooltips are desktop-only components that display additional information when hovering over or focusing on an element.

- **Keyboard Hover Support:** Tooltips should be accessible when an element is focused using the keyboard.
- **Dynamic Positioning:** Tooltip content should be displayed based on the current position of the trigger element on the screen and always visible to the user.
- **Hover Timeout:** Having a small timeout before triggering a tooltip will help to prevent occasionally showing tooltips while users move their mouse cursor.
- **Light Variant:** The tooltip should respect its parent element background and provide a variant to be used on darker background colours.
- **Instant Transition for Element Groups:** If there’s a group of elements using tooltips, hovering over another element while a tooltip’s already active shouldn’t trigger the animation.

## Typography

# Typography

Typography establishes hierarchy, readability, and brand personality. An effective system should develop harmonious scales using mathematical ratios, choose appropriate typefaces, implement fluid typography, establish consistent line-heights, define font weight hierarchy, ensure accessibility compliance, and provide clear usage guidelines.

## Ui Kit

# UI Kit

As it relates to a design system, a UI Kit is a representation of coded components created in a way that designers who don’t know code can create interface mockups. Examples of UI kits are Sketch libraries and [Figma design systems](https://www.figma.com/blog/how-to-build-your-design-system-in-figma/).

Visit the following resources to learn more:

- [@article@Design System vs UI Kit](https://uigstudio.com/insights/design-system-vs-ui-kit)
- [@article@Your sketch library is not a design system](http://bradfrost.com/blog/post/your-sketch-library-is-not-a-design-system/)

## Understand The Basics

# Design System Basics

A design system is a set of standards to manage design at scale by reducing redundancy while creating a shared language and visual consistency across different pages and channels.

Visit the following resources to learn more:

- [@article@Design Systems 101](https://www.nngroup.com/articles/design-systems-101/)
- [@video@What is a Design System? Design Systems 101 for Designers](https://www.youtube.com/watch?v=wc5krC28ynQ)
- [@article@How to build your design system](https://www.figma.com/blog/design-systems-102-how-to-build-your-design-system/)
- [@article@Everything you need to know about Design Systems](https://uxdesign.cc/everything-you-need-to-know-about-design-systems-54b109851969)

## Unit Testing

# Unit Testing

Every part of the design system should be covered with unit tests. Once your system’s adopted, any change in the isolated environment may affect how the product works.

## Units

# Units

Units are the most granular building blocks for layout. Defining a set of values with consistent increments (such as 4, 8, 12 and 16 for a 4-point system) will provide you with the foundation when you’re designing your grid and spacing values.

## Usage Guidance

# Usage Guidance

Logo usage guidance provides rules for proper implementation to maintain brand consistency. Effective guidance should establish clear examples of proper usage and mistakes to avoid, define logo variations, specify color requirements, prohibit unauthorized alterations, and include approval processes for new contexts.

Visit the following resources to learn more:

- [@article@Logo Usage Best Practices](https://99designs.com/blog/tips/logo-usage-guidelines/)
- [@article@Brand Guidelines Development](https://designsystem.digital.gov/design-tokens/logo/)
- [@article@Trademark and Logo Legal Guidelines](https://www.uspto.gov/trademarks-getting-started/trademark-basics)
- [@article@Brand Identity Protection](https://www.brandfolder.com/blog/brand-guidelines)
- [@feed@Explore top posts about Brand Management](https://app.daily.dev/tags/branding?ref=roadmapsh)

## User Onboarding

# User Onboarding

How you onboard your users to your product or a new feature and give them a great experience from the start.

- [@video@What is user onboarding? ](https://www.youtube.com/watch?v=PatIqbGEQe4)

## Version Control

# Version Control

Having your design versioned with semantic versioning will allow you to easily align design with development, roll back faulty changes and release changes in code and design at the same time.

## Vision

# Vision

Brand vision serves as the foundation for design system decisions, providing purpose and direction. An effective vision should articulate organizational purpose, identify core values, visualize future success, prioritize user needs, clarify brand uniqueness, account for cultural considerations, and connect to measurable goals.

Visit the following resources to learn more:

- [@article@Creating Brand Vision](https://www.interaction-design.org/literature/article/branding-in-ux)
- [@article@Vision-Driven Design Systems](https://bradfrost.com/blog/post/the-design-system-ecosystem/)
- [@article@Brand Strategy for Design](https://alistapart.com/article/creating-a-brand-identity/)
- [@article@Purpose-Driven Design](https://designsystem.digital.gov/design-tokens/brand/)
- [@feed@Explore top posts about Brand Strategy](https://app.daily.dev/tags/branding?ref=roadmapsh)

## Visual Forms

# Visual Forms

Visual forms focus on aesthetic and interactive design aspects of form components. Effective design should establish clear information architecture, create consistent field styling, develop harmonious label positioning, design clear error communication, implement progressive enhancement, prioritize mobile-first design, and ensure cross-platform consistency.

## What Is A Design System

# What is Design System

A Design System is the single source of truth which groups all the elements that will allow the teams to design, realize and develop a product.

Visit the following resources to learn more:

- [@article@Everything you need to know about Design Systems](https://uxdesign.cc/everything-you-need-to-know-about-design-systems-54b109851969)
- [@article@Design Systems 101](https://www.nngroup.com/articles/design-systems-101/)
- [@article@A comprehensive guide to design systems](https://www.invisionapp.com/inside-design/guide-to-design-systems/)

## What Is Atomic Design

# Atomic Design

Atomic design (by Brad Frost) is a mental model to help you think of user interfaces as a cohesive whole and a collection of parts at the same time. Through the comparison to atoms, molecules, and organisms, we can think of the design of our UI as a composition of self-containing modules put together.

Visit the following resources to learn more:

- [@article@Atomic Design Principles & Methodology 101](https://xd.adobe.com/ideas/process/ui-design/atomic-design-principles-methodology-101/)
- [@article@Atomic Design Methodology](https://atomicdesign.bradfrost.com/chapter-2/)
- [@article@Atomic Design and UI Components: Theory to Practice](https://blog.bitsrc.io/atomic-design-and-ui-components-theory-to-practice-f200db337c24)

## Writing Guidelines

# Writing Guidelines

Every consistent experience needs watertight writing. Laying down the foundations for your house style early keeps everything in line with consistent grammar, style choices and action-oriented language to help your design.
