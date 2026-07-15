# Css Roadmap

---
renderer: editor
---

---

## Absolute Vs Relative

# Absolute vs. Relative Units

Absolute units in CSS represent fixed measurements, like pixels (px) or inches (in), and will always render at the same size regardless of screen size or other factors. Relative units, on the other hand, are based on other values, such as the font size of the parent element (em), the viewport width (vw), or the root element's font size (rem), allowing for more flexible and responsive layouts.

Visit the following resources to learn more:

- [@article@What are Absolute and Relative Units in CSS? Explained with Examples](https://www.freecodecamp.org/news/absolute-and-relative-css-units)

## Absolute

# Absolute Positioning

Absolute positioning in CSS allows you to precisely place an element relative to its nearest positioned ancestor (an ancestor with a position value other than `static`). If no such ancestor exists, the element is positioned relative to the initial containing block, which is typically the `<html>` element. Elements with `position: absolute` are removed from the normal document flow, meaning they don't affect the positioning of other elements around them.

Visit the following resources to learn more:

- [@video@CSS position deep dive](https://www.youtube.com/watch?v=fF_NVrd1s14)

## Accessibility

# Accessibility

Accessibility in CSS focuses on creating web content that is usable by everyone, regardless of their abilities or disabilities. This involves using semantic HTML, providing alternative text for images, ensuring sufficient color contrast, and designing layouts that are navigable with assistive technologies like screen readers. By following accessibility best practices, developers can build inclusive websites that provide a better experience for all users.

Visit the following resources to learn more:

- [@article@CSS and JavaScript accessibility best practices](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Accessibility/CSS_and_JavaScript)
- [@article@CSS Accessibility Styling](https://www.w3schools.com/css/css_accessibility.asp)
- [@article@How to Use CSS to Improve Web Accessibility](https://www.freecodecamp.org/news/how-to-use-css-to-improve-web-accessibility/)

## Attribute Selectors

# Attribute Selectors

Attribute selectors in CSS target HTML elements based on the presence or value of their attributes. They allow you to style elements more precisely than using just tag names or classes. For example, you can select all elements with a specific attribute, or only those where the attribute's value matches a certain string.

Visit the following resources to learn more:

- [@article@Attribute Selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/Attribute_selectors)
- [@article@Attribute Selectors | CSS Tricks](https://css-tricks.com/almanac/selectors/a/attribute/)
- [@video@Attribute Selectors in detail - CSS Tutorial](https://www.youtube.com/watch?v=m_upHrxjR8s)

## Background Attachment

# Background Attachment

Background attachment in CSS controls how a background image behaves when the page is scrolled. It determines whether the background image scrolls along with the content or remains fixed in place. This property is useful for creating visual effects like parallax scrolling or keeping a watermark visible regardless of the user's scroll position.

Visit the following resources to learn more:

- [@article@Background Attachment](https://developer.mozilla.org/en-US/docs/Web/CSS/background-attachment)
- [@video@CSS - Background Attachment - W3Schools.com](https://www.youtube.com/watch?v=lXs8BRnrW_M)

## Background Color

# Background Color

Background color in CSS sets the color of an element's background. It fills the entire box of an element, including padding, but not the border or margin. You can specify the color using color names (like "red"), hexadecimal values (like "#FF0000"), RGB values (like "rgb(255, 0, 0)"), or other color formats.

Visit the following resources to learn more:

- [@article@Background Color](https://developer.mozilla.org/en-US/docs/Web/CSS/background-color)
- [@video@CSS - Background Colors - W3Schools.com](https://www.youtube.com/watch?v=-itttmX6HX0&pp=ygUUYmFja2dyb3VuZCBjb2xvciBjc3M%3D)

## Background Gradient

# Background Gradient

Background gradients in CSS allow you to create smooth transitions between two or more colors for the background of an element. Instead of a solid color, you can define a gradient that blends colors together, adding visual depth and interest to your designs. These gradients can be linear (flowing in a straight line), radial (emanating from a center point), or conic (rotating around a center point).

Visit the following resources to learn more:

- [@article@CSS gradients](https://www.w3schools.com/css/css3_gradients.asp)
- [@video@CSS Gradient Background - One Minute Coding ⏱](https://www.youtube.com/watch?v=NINIuzyWZ2c)

## Background Image

# Background Image

A background image in CSS lets you add an image to the background of an HTML element. This image can be a simple pattern, a photograph, or any other visual element you want to display behind the content of your element. You can control how the image is positioned, repeated, and sized within the background area.

Visit the following resources to learn more:

- [@article@MDN – background-image](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-image)
- [@article@CSS-Tricks – A Complete Guide to CSS Backgrounds](https://css-tricks.com/almanac/properties/b/background/)
- [@video@How to include a CSS background image 🏙️](https://www.youtube.com/watch?v=_oFWg_NlKdo)
- [@video@Background images with HTML & CSS](https://www.youtube.com/watch?v=zHZRFwWQt2w)

## Background Position

# Background Position

Background position in CSS controls where a background image is placed within its element. It lets you specify the horizontal and vertical placement of the image, using keywords like `top`, `bottom`, `left`, `right`, and `center`, or with numerical values (pixels, percentages, etc.) to fine-tune the exact location. This property is useful for aligning background images in specific ways, creating visual effects, or ensuring that important parts of the image are always visible.

Visit the following resources to learn more:

- [@article@Background Position](https://developer.mozilla.org/en-US/docs/Web/CSS/background-position)
- [@video@CSS Property : background-position explained !](https://www.youtube.com/watch?v=S_rcA0JKEaE)

## Background

# Background

In CSS, the term "background" refers to the properties that control the visual appearance of an element's background. This includes aspects like the background color, image, its positioning, whether it repeats, and its size. These properties allow you to add visual interest and customize the look of your web pages.

Visit the following resources to learn more:

- [@video@Learn CSS background in 3 minutes](https://www.youtube.com/watch?v=YA8ZciJa64k)

## Bem

# BEM

BEM (Block, Element, Modifier) is a CSS naming convention that helps developers create more modular, reusable, and maintainable code. It structures class names to reflect the relationships between different parts of a user interface. This approach makes it easier to understand the purpose of each CSS rule and how it relates to the HTML structure, leading to more organized and scalable stylesheets.

Visit the following resources to learn more:

- [@official@BEM](https://getbem.com/)
- [@article@BEM 101](https://css-tricks.com/bem-101/)
- [@video@Why I use the BEM naming convention for my CSS](https://www.youtube.com/watch?v=SLjHSVwXYq4)

## Block

# Block Display

The `display: block;` property in CSS makes an element behave like a block-level element. This means it will take up the full width available to it, starting on a new line and pushing subsequent content to a new line as well. Block elements typically define the major structural components of a webpage.

Visit the following resources to learn more:

- [@video@Block, Inline, and Inline-Block explained | CSS Tutorial](https://www.youtube.com/watch?v=x_i2gga-sYg)

## Border

# Border

In CSS, the `border` property defines the line that surrounds an HTML element's content and padding. It controls the border's style (like solid, dashed, or dotted), width (thickness), and color. You can set all these properties at once using the shorthand `border` property, or individually using `border-style`, `border-width`, and `border-color`.

Visit the following resources to learn more:

- [@article@Border](https://developer.mozilla.org/en-US/docs/Web/CSS/border)
- [@article@Learn CSS borders in 4 minutes!](https://www.youtube.com/watch?v=pkNdQ7TmxIw)

## Box Model

# Box Model

The CSS box model describes how elements on a webpage are structured as rectangular boxes. Each box consists of content (text, images, etc.), padding (space around the content), a border (a line around the padding and content), and a margin (space around the border). Understanding the box model is crucial for controlling the size and spacing of elements on a webpage.

Visit the following resources to learn more:

- [@article@The box model](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/Box_model)
- [@video@Learn CSS Box Model In 8 Minutes](https://www.youtube.com/watch?v=rIO5326FgPE)

## Box Shadows

# Box Shadows

Box shadows in CSS are visual effects that add depth and dimension to elements by creating a shadow around their frames. These shadows can be customized in terms of color, offset (horizontal and vertical distance), blur radius, and spread radius, allowing designers to simulate various lighting conditions and create visually appealing interfaces. Box shadows can be applied to almost any HTML element, enhancing the user experience by highlighting important elements or adding a subtle sense of realism.

Visit the following resources to learn more:

- [@article@Box Shadows](https://developer.mozilla.org/en-US/docs/Web/CSS/box-shadow)
- [@video@CSS Box-Shadow tutorial: the basics](https://www.youtube.com/watch?v=-JNRQ5HjNeI)

## Cascading Order

# Cascading Order

Cascading order in CSS determines which styles are applied to an element when multiple conflicting rules target the same element. It's a set of rules that browsers follow to resolve these conflicts, prioritizing styles based on factors like importance, specificity, and source order. Understanding the cascading order is crucial for predicting and controlling how styles are applied to your web pages.

Visit the following resources to learn more:

- [@article@Introduction to the CSS cascade](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_cascade/Cascade)
- [@article@Handling conflicts](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/Handling_conflicts)

## Child

# Child Combinator

The child combinator selector in CSS allows you to target elements that are direct children of a specified parent element. It uses the `>` symbol to denote this direct parent-child relationship. This selector ensures that styles are only applied to elements that are immediately nested within the parent, ignoring any deeper descendants.

Visit the following resources to learn more:

- [@article@Child combinator](https://developer.mozilla.org/en-US/docs/Web/CSS/Child_combinator)
- [@article@Child and Sibling Selectors](https://css-tricks.com/child-and-sibling-selectors/)

## Class

# Class Selectors

Class selectors in CSS are used to select HTML elements based on the `class` attribute. They allow you to apply specific styles to elements that share a common class name. You define a class selector by using a period (`.`) followed by the class name.

Visit the following resources to learn more:

- [@article@Class selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/Class_selectors)
- [@article@The Beginner's Guide to CSS Classes & .class Selectors](https://blog.hubspot.com/website/what-is-css-class)

## Color

# Color

Color in CSS is used to specify the foreground color of text and other elements. It can be defined using various methods, including named colors (like "red" or "blue"), hexadecimal values (like "#FF0000"), RGB values (like "rgb(255, 0, 0)"), RGBA values (which include an alpha channel for transparency), HSL values (hue, saturation, lightness), and HSLA values (which include an alpha channel for HSL).

Visit the following resources to learn more:

- [@article@Text color](https://developer.mozilla.org/en-US/docs/Web/CSS/color)
- [@article@CSS Font Color – How to Style Text in HTML](https://www.freecodecamp.org/news/css-font-color-how-to-style-text-in-html/)

## Combinator Selectors

# Combinator Selectors

Combinator selectors in CSS define the relationship between elements based on their position in the document's structure. They allow you to target elements that are descendants, children, adjacent siblings, or general siblings of another element. This provides a powerful way to apply styles based on the HTML hierarchy, going beyond simple class or ID targeting.

Visit the following resources to learn more:

- [@article@Combinators](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/Combinators)
- [@video@Learn CSS combinators in 4 minutes!](https://www.youtube.com/watch?v=swZFmJsU54s)

## Comments

# Comments

Comments in CSS are notes that you add to your code to explain what it does, or to temporarily disable parts of your code. Browsers ignore these comments, so they don't affect how your website looks. You create a CSS comment by starting with `/*` and ending with `*/`.

Visit the following resources to learn more:

- [@article@CSS Comments](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_syntax/Comments)
- [@video@HTML & CSS for Absolute Beginners: HTML Comments](https://www.youtube.com/watch?v=NTlhOJIy8HY)

## Container Queries

# Container Queries

Container Queries are a CSS feature that allows styles to be applied to an element based on the size or other characteristics of its containing element, rather than the viewport. This enables more granular and context-aware styling, where components can adapt their appearance based on the space available within their parent container, leading to more flexible and reusable designs.

Visit the following resources to learn more:

- [@article@CSS container queries](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_containment/Container_queries)
- [@article@CSS Container Queries Guide](https://css-tricks.com/css-container-queries/)
- [@video@Master CSS container queries and boost your web design skills!](https://www.youtube.com/watch?v=8x8lxX5IGHY)

## Css Basics

# CSS Basics

CSS Basics encompass the fundamental building blocks for styling web pages. This includes understanding selectors (how to target specific HTML elements), properties (the visual characteristics you want to change, like color or font size), and values (the specific settings for those properties, such as "red" or "16px"). Mastering these basics allows you to control the presentation of your website's content.

## Css Functions

# CSS Functions

CSS functions are pre-defined operations that perform specific tasks within your CSS code. They allow you to manipulate values, perform calculations, and generate dynamic results, making your stylesheets more flexible and powerful. These functions are used within CSS property values to modify or create those values based on certain inputs.

Visit the following resources to learn more:

- [@article@CSS value functions](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Values_and_Units/CSS_Value_Functions)
- [@article@Functions](https://web.dev/learn/css/functions)
- [@article@Functions in CSS?!](https://css-tricks.com/functions-in-css/)
- [@video@First look at FUNCTIONS in CSS!!!](https://www.youtube.com/watch?v=fhuYPNlBkyw)

## Css In Js

# CSS-in-JS

CSS-in-JS is a technique where CSS styles are written with JavaScript instead of external CSS files. This approach allows you to use JavaScript's capabilities, like variables, logic, and component-based architecture, to manage and apply styles directly within your JavaScript code. It offers benefits such as scoped styling, dynamic styling based on component state, and easier management of complex CSS projects.

Visit the following resources to learn more:

- [@article@A Thorough Analysis of CSS-in-JS](http://css-tricks.com/a-thorough-analysis-of-css-in-js/)

## Css Modules

# CSS Modules

CSS Modules are a system where CSS class names and animation names are scoped locally by default. This means that the class names you define in your CSS files are automatically transformed to be unique, preventing naming collisions and making it easier to manage styles in large projects. They offer a way to write modular and reusable CSS, ensuring that styles are applied only to the intended components.

Visit the following resources to learn more:

- [@article@What are CSS Modules and why do we need them?](https://css-tricks.com/css-modules-part-1-need/)
- [@video@CSS Modules: Why are they great?](https://www.youtube.com/watch?v=pKMWU9OrA2s)

## Css Specificity

# CSS Specificity

CSS Specificity is the set of rules that browsers use to determine which CSS declarations apply to an element when multiple conflicting rules exist. It's essentially a weighting system that prioritizes certain CSS selectors over others, ensuring that the most relevant style is applied. Understanding specificity is crucial for controlling how your CSS styles are applied and resolving unexpected styling issues.

Visit the following resources to learn more:

- [@article@Specificity](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_cascade/Specificity)
- [@video@CSS Specificity explained](https://www.youtube.com/watch?v=c0kfcP_nD9E)

## Css Units

# CSS Units

CSS units define the size of elements and properties in a webpage. They specify how measurements like width, height, font size, and margins are interpreted by the browser. These units can be absolute, like pixels (px) or centimeters (cm), or relative, like em, rem, or viewport units (vw, vh), allowing for flexible and responsive layouts that adapt to different screen sizes and resolutions.

Visit the following resources to learn more:

- [@article@CSS Units](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/Values_and_units)
- [@video@Learn CSS Units In 8 Minutes](https://www.youtube.com/watch?v=-GR52czEd-0)

## Css Variables

# CSS Variables

CSS Variables, also known as custom properties, are entities defined by CSS authors that contain specific values to be reused throughout a stylesheet. They allow you to store a value in one place and then reference it in multiple other places, making it easier to maintain and update your CSS code. This promotes consistency and reduces repetition, leading to more efficient and manageable stylesheets.

Visit the following resources to learn more:

- [@article@Using CSS custom properties (variables)](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_cascading_variables/Using_CSS_custom_properties)
- [@article@How to use CSS variables like a pro](https://blog.logrocket.com/how-to-use-css-variables/)
- [@video@Learn CSS Variables In 7 Minutes](https://www.youtube.com/watch?v=5wLrz_zUwoU)

## Css

# CSS

CSS (Cascading Style Sheets) is a language used to describe the presentation of a document written in HTML or XML. It controls the layout, colors, fonts, and other visual aspects of web pages, ensuring a consistent and visually appealing user experience across different devices and screen sizes. Essentially, CSS separates the content of a webpage from its design, making websites easier to maintain and update.

Visit the following resources to learn more:

- [@course@Responsive Web Design Certification - Co-Learn HTML & CSS with guided projects](https://www.freecodecamp.org/learn/responsive-web-design-v9/)
- [@course@Web.dev by Google — Learn CSS](https://web.dev/learn/css/)
- [@article@Visit Dedicated JavaScript Roadmap](https://roadmap.sh/css)
- [@video@CSS Complete Course](https://www.youtube.com/watch?v=n4R2E7O-Ngo)
- [@video@HTML & CSS Full Course - Beginner to Pro](https://www.youtube.com/watch?v=G3e-cpL7ofc)
- [@feed@Explore top posts about CSS](https://app.daily.dev/tags/css?ref=roadmapsh)

## Declaration

# Declaration

A declaration in CSS is a single statement that specifies a property you want to style and the value you want to assign to that property. It's the fundamental building block for applying styles to HTML elements. Each declaration consists of a property name (like `color` or `font-size`), followed by a colon (`:`), and then a value (like `red` or `16px`). Declarations are always placed inside a CSS rule set, within the curly braces `{}`.

Visit the following resources to learn more:

- [@article@Introduction to CSS syntax: declarations, rulesets, and statements](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_syntax/Syntax)

## Descendant

# Descendant Combinator

The descendant combinator in CSS is a way to select HTML elements that are descendants of another element. It uses a single space (" ") between two selectors. The selector on the right side of the space will select all elements that are descendants (children, grandchildren, etc.) of the element specified by the selector on the left side.

Visit the following resources to learn more:

- [@article@Descendant combinator](https://developer.mozilla.org/en-US/docs/Web/CSS/Descendant_combinator)
- [@article@Descendant](https://css-tricks.com/almanac/selectors/d/descendant/)

## Direction

# Direction

The `direction` property in CSS sets the text direction of block-level elements, influencing how text, table columns, and inline-level boxes flow. While `direction` can be used to switch between left-to-right (LTR) and right-to-left (RTL) layouts, it's generally better to use the HTML `dir` global attribute. The `dir` attribute semantically indicates the document's or element's text direction, providing better accessibility and separation of concerns compared to styling direction with CSS.

Visit the following resources to learn more:

- [@article@CSS Direction](https://developer.mozilla.org/en-US/docs/Web/CSS/direction)
- [@article@HTML dir global attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/dir)
- [@video@CSS for beginners 60: direction property](https://www.youtube.com/watch?v=LM0yIWmP62Q)
- [@video@HTML Global Attributes - dir Attribute](https://www.youtube.com/watch?v=6hqHM7Ez_Xg)

## Display

# Display

The `display` property in CSS controls how an element is rendered on a webpage, specifically defining its box type and how it interacts with other elements. It determines whether an element is treated as a block-level element (taking up the full width available), an inline element (flowing within the text), or something else entirely, like a table or a grid container. This property is fundamental for controlling the layout and structure of web pages.

Visit the following resources to learn more:

- [@article@Display](https://developer.mozilla.org/en-US/docs/Web/CSS/display)
- [@video@Learn CSS display property in 4 minutes!](https://www.youtube.com/watch?v=9T8uxp5hQ60)

## Element

# Element Selectors

Element selectors in CSS target HTML elements directly by their tag name. They allow you to apply styles to all occurrences of a specific element, such as all `<p>` (paragraph) or `<h1>` (heading) tags on a webpage. This is the most basic type of selector and provides a straightforward way to style common HTML elements.

Visit the following resources to learn more:

- [@article@CSS selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_selectors)
- [@article@CSS Selectors Cheat Sheet](https://www.sitepoint.com/css-selectors/)

## External Css

# External CSS

External CSS involves writing CSS rules in a separate file (with a `.css` extension) and then linking that file to your HTML document. This approach promotes cleaner code, easier maintenance, and reusability of styles across multiple web pages. By separating the styling from the content, you can modify the look and feel of your website without altering the HTML structure.

Visit the following resources to learn more:

- [@article@Types of CSS: inline, external and internal definitions and differences explained](https://www.hostinger.com/tutorials/difference-between-inline-external-and-internal-css)
- [@video@External Style Sheets | CSS](https://www.youtube.com/watch?v=2P_LUPc2HrM)

## Fixed

# Fixed Positioning

Fixed positioning in CSS allows an element to be locked in place relative to the browser window. This means that even when the user scrolls the page, the element remains visible in the same location on the screen. It's often used for navigation bars, footers, or other elements that need to stay persistent.

Visit the following resources to learn more:

- [@article@CSS position deep dive](https://www.youtube.com/watch?v=fF_NVrd1s14)

## Flexbox

# Flexbox

Flexbox is a CSS layout model that provides an efficient way to arrange, align, and distribute space among items in a container, even when their size is unknown or dynamic. It simplifies the creation of complex layouts by offering powerful tools for controlling the direction, order, size, and alignment of elements within a container. Flexbox is particularly useful for designing responsive and adaptable user interfaces.

Visit the following resources to learn more:

- [@article@Flexbox](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout/Flexbox)
- [@article@CSS Flexbox Layout Guide](https://css-tricks.com/snippets/css/a-guide-to-flexbox/)
- [@video@Learn CSS Flexbox in 20 Minutes (Course)](https://www.youtube.com/watch?v=wsTv9y931o8)

## Floating Elements

# Floating Elements

Floating elements in CSS allow you to take an element out of the normal document flow and position it to the left or right of its containing element. Other content will then flow around the floated element. This technique is commonly used to create layouts where text wraps around images or to position elements side-by-side.

Visit the following resources to learn more:

- [@article@Floating elements](https://developer.mozilla.org/en-US/docs/Web/CSS/float)
- [@video@Learn CSS float in 4 minutes! 🎈](https://www.youtube.com/watch?v=oJe8G5XT_v4)

## Flow Layout

# Flow Layout

Flow layout is the default way elements are positioned on a webpage. Elements are displayed one after another, like words in a sentence, following the natural flow of the HTML. Block-level elements take up the full width available and start on a new line, while inline elements flow within the content, only taking up the space they need.

Visit the following resources to learn more:

- [@article@CSS flow layout](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_display/Flow_layout)
- [@article@Block and inline layout in normal flow](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_display/Block_and_inline_layout_in_normal_flow)
- [@article@Flow layout and writing modes](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_display/Flow_layout_and_writing_modes)
- [@video@CSS website layout in 9 minutes! 🗺️](https://www.youtube.com/watch?v=Hsu8uqQTSV8)

## Font Families

# Font Families

Font families in CSS are a way to specify the typeface used to display text on a webpage. They allow you to define a prioritized list of fonts, so if the user's computer doesn't have the first font available, the browser will try the next one in the list, and so on. This ensures that text is always displayed in a readable font, even if the preferred font isn't available.

Visit the following resources to learn more:

- [@article@Font Families](https://developer.mozilla.org/en-US/docs/Web/CSS/font-family)
- [@article@CSS Fonts](https://www.w3schools.com/css/css_font.asp)

## Font Shorthand

# Font Shorthand

The font shorthand property in CSS provides a way to set multiple font-related properties in a single declaration. Instead of specifying `font-style`, `font-variant`, `font-weight`, `font-size`, `line-height`, and `font-family` individually, you can use the `font` property to define them all at once, making your stylesheets more concise and readable.

Visit the following resources to learn more:

- [@article@font shorthand](https://developer.mozilla.org/en-US/docs/Web/CSS/font)

## Font Size

# Font Size

Font size in CSS determines the size of the text on a webpage. It's a fundamental property that controls the visual prominence and readability of text elements. You can specify font sizes using various units like pixels (px), ems (em), rems (rem), percentages (%), and viewport units (vw, vh). Choosing the right font size is crucial for creating a visually appealing and accessible design.

Visit the following resources to learn more:

- [@article@font-size](https://developer.mozilla.org/en-US/docs/Web/CSS/font-size)
- [@video@CSS Tutorial For Beginners - Font Size](https://www.youtube.com/watch?v=799zrGVpfA8)

## Font Style

# Font Style

Font style in CSS is used to select the appearance of a font, primarily to italicize or oblique text. It allows you to specify whether a font should be displayed in its normal, italic, or oblique version. This property is useful for emphasizing text or creating a visual distinction within a design.

Visit the following resources to learn more:

- [@article@font-style](https://developer.mozilla.org/en-US/docs/Web/CSS/font-style)

## Font Variant

# Font Variant

Font variant in CSS allows you to control the display of different variations of a font, such as small caps, oldstyle numerals, and alternate glyphs. It provides a way to access OpenType features within a font, enabling richer typographic control beyond basic font styling like size and weight. This property offers a shorthand for setting several more specific font variant properties.

Visit the following resources to learn more:

- [@article@Font variant](https://developer.mozilla.org/en-US/docs/Web/CSS/font-variant)
- [@article@CSS font-variant Property](https://www.w3schools.com/cssref/pr_font_font-variant.php)

## Font Weight

# Font Weight

Font weight refers to the thickness or boldness of characters in a typeface. In CSS, it's a property that allows you to specify how heavy or light the font should appear. Values can be numeric (like 100, 400, 700) or descriptive (like `normal`, `bold`, `lighter`, `bolder`), offering control over the visual emphasis of text.

Visit the following resources to learn more:

- [@article@Font Weight](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-weight)
- [@article@An Introduction to HTML/CSS Font Weight](https://www.udacity.com/blog/2021/01/html-css-font-weight.html)
- [@article@CSS font-weight Property](https://www.w3schools.com/cssref/pr_font_weight.php)
- [@video@CSS Tutorial For Beginners 30 - Font Weight](https://www.youtube.com/watch?v=qeh4UeaGTnc)

## Frontend Development

# Frontend Development

Frontend development involves crafting the user interface and user experience of a website or web application. It focuses on the parts of a website that users directly interact with, such as buttons, text, images, and navigation. Frontend developers use languages like HTML, CSS, and JavaScript to build these interactive elements and ensure they function correctly across different browsers and devices.

Visit the following resources to learn more:

- [@roadmap@Visit the dedicated Frontend Roadmap](https://roadmap.sh/frontend)
- [@article@Front-End Development: The Complete Guide](https://cloudinary.com/guides/front-end-development/front-end-development-the-complete-guide)
- [@video@Frontend web development - a complete overview](https://www.youtube.com/watch?v=WG5ikvJ2TKA)

## Google Fonts

# Google Fonts

Google Fonts is a free library of over a thousand different font families that you can easily use on your website. Instead of relying on the limited set of fonts that come pre-installed on a user's computer, you can link to Google's servers and use any font they offer. This allows for greater design flexibility and ensures that your website's typography looks consistent across different devices and operating systems.

Visit the following resources to learn more:

- [@article@Using web fonts](https://fonts.google.com/knowledge/using_type/using_web_fonts)
- [@article@CSS Google Fonts](https://www.w3schools.com/css/css_font_google.asp)
- [@video@How to Add Google Fonts to Your Website Including Multiple Fonts](https://www.youtube.com/watch?v=is9Z5HriVtQ)

## Grid

# Grid Layout

Grid Layout is a two-dimensional layout system for CSS, enabling you to control the placement and sizing of elements within a grid container. It divides a webpage into rows and columns, allowing precise positioning of content and creating complex layouts with ease. This method offers flexibility and control over element arrangement, surpassing traditional methods like floats or positioning.

Visit the following resources to learn more:

- [@article@CSS Grid Layout](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_grid_layout)
- [@article@CSS Grid Layout Guide](https://css-tricks.com/snippets/css/complete-guide-grid/)
- [@video@CSS Grid Intro and Basic Layout Tutorial for Beginners](https://www.youtube.com/watch?v=EaWj2AWI5Es)

## Grouping

# Grouping Selectors

Grouping selectors in CSS allows you to apply the same styles to multiple HTML elements simultaneously. Instead of writing the same CSS rules for each element individually, you can list the selectors separated by commas. This makes your CSS code more concise and easier to maintain, as you only need to define the styles once for all the grouped elements.

Visit the following resources to learn more:

- [@article@Grouping Multiple CSS Selectors](https://www.thoughtco.com/grouping-multiple-css-selectors-3467065)
- [@article@Grouping Selectors in CSS](https://www.tutorialspoint.com/grouping-selectors-in-css)

## Hex

# Hex Colors

Hex colors in CSS are a way to specify colors using hexadecimal values. They use a six-digit code, prefixed with a hash symbol (#), to represent the red, green, and blue components of a color. Each pair of digits represents the intensity of one of these primary colors, ranging from 00 (lowest intensity) to FF (highest intensity). For example, #FF0000 is red, #00FF00 is green, and #0000FF is blue.

Visit the following resources to learn more:

- [@article@hex color](https://developer.mozilla.org/en-US/docs/Web/CSS/hex-color)
- [@video@CSS - Colors Hex - W3Schools.com](https://www.youtube.com/watch?v=LLmCr_201GU)

## Hsl

# HSL Colors

HSL (Hue, Saturation, Lightness) is a way to define colors in CSS using three components: Hue, which represents the color type on a color wheel (0-360 degrees); Saturation, which indicates the intensity of the color (0-100%); and Lightness, which determines how bright or dark the color is (0-100%). This model offers a more intuitive way to adjust colors compared to RGB, allowing developers to easily create variations of a color by modifying its hue, saturation, or lightness values.

Visit the following resources to learn more:

- [@article@hsl function](https://developer.mozilla.org/en-US/docs/Web/CSS/color_value/hsl)
- [@article@CSS HSL Colors](https://www.w3schools.com/css/css_colors_hsl.asp)
- [@video@How to Create RELATIVE Colors with hsl(from...) CSS Tutorial](https://www.youtube.com/watch?v=TI-OVY11HD4)

## Html

# HTML

HTML (HyperText Markup Language) is the standard markup language for creating web pages. It provides the structure and content of a website, using elements to define headings, paragraphs, images, links, and other components that are displayed in a web browser. HTML forms the foundation upon which CSS and JavaScript build to create visually appealing and interactive web experiences.

Visit the following resources to learn more:

- [@roadmap@Visit the dedicated HTML roadmap](https://roadmap.sh/html)
- [@article@Responsive Web Design Certification - Co-Learn HTML & CSS with guided projects](https://www.freecodecamp.org/learn/2022/responsive-web-design/)
- [@video@HTML Full Course for Beginners](https://www.youtube.com/watch?v=mJgBOIoGihA)
- [@video@HTML Full Course - Build a Website Tutorial](https://www.youtube.com/watch?v=pQN-pnXPaVg)
- [@feed@Explore top posts about HTML](https://app.daily.dev/tags/html?ref=roadmapsh)

## Id

# ID Selectors

ID selectors in CSS are used to style a single, unique element on a webpage. They target an HTML element based on the value of its `id` attribute. An ID selector is denoted by a hash symbol (`#`) followed by the ID value.

Visit the following resources to learn more:

- [@article@ID Selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/ID_selectors)

## Images And Filters

# Images and Filters

CSS allows you to incorporate images into your web designs and manipulate their appearance. You can use CSS to control image size, positioning, and how they interact with surrounding content. Additionally, CSS filters enable the direct application of visual effects, such as blurring, color adjustments, and transformations, to images, thereby enhancing their aesthetic appeal without requiring external image editing software.

Visit the following resources to learn more:

- [@article@CSS images](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_images)
- [@article@CSS filter effects](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_filter_effects)
- [@video@Dabbling with CSS Filters and Blending Effects](https://www.youtube.com/watch?v=-jy7dac750Q)
- [@video@CSS Background Images and Responsive Image Properties for Beginners](https://www.youtube.com/watch?v=cLyzBfXI0I0)

## Inline Block

# Inline-Block

`inline-block` is a value for the CSS `display` property. It allows an element to flow like an inline element (sitting on the same line as other content) but also allows you to set its width and height, similar to a block-level element. This combines the benefits of both `inline` and `block` elements.

Visit the following resources to learn more:

- [@article@CSS display: inline-block](https://www.w3schools.com/css/css_inline-block.asp)
- [@video@Block, Inline, and Inline-Block explained | CSS Tutorial](https://www.youtube.com/watch?v=x_i2gga-sYg)

## Inline Css

# Inline CSS

Inline CSS involves directly embedding CSS styles within HTML elements using the `style` attribute. This method applies styles to individual elements, overriding external stylesheets or embedded styles. While offering quick and localized styling, it's generally discouraged for larger projects due to maintainability issues and separation of concerns.

Visit the following resources to learn more:

- [@article@Inline Style in HTML – CSS Inline Styles](https://www.freecodecamp.org/news/inline-style-in-html/)

## Inline

# Inline Display

The `display: inline` property in CSS is used to specify that an element should be displayed as an inline element. Inline elements flow along with the surrounding content, similar to how text flows within a paragraph. They only take up as much width as necessary to contain their content, and the width and height properties do not affect them.

Visit the following resources to learn more:

- [@article@Block and inline layout in normal flow](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_display/Block_and_inline_layout_in_normal_flow)
- [@video@Block, Inline, and Inline-Block explained | CSS Tutorial](https://www.youtube.com/watch?v=x_i2gga-sYg)

## Internal Css

# Internal CSS

Internal CSS involves embedding CSS rules directly within an HTML document. This is achieved by using the `<style>` tag, typically placed inside the `<head>` section of the HTML file. The CSS rules defined within the `<style>` tag will then be applied to the elements within that specific HTML document.

Visit the following resources to learn more:

- [@article@Internal CSS](https://codeinstitute.net/global/blog/internal-css/)
- [@video@How to Use Internal CSS [CSS Tutorials for Beginners]](https://www.youtube.com/watch?v=o2hQUHGueXY)

## Introduction

# CSS

CSS (Cascading Style Sheets) is a language used to describe the presentation of a document written in HTML or XML, including colors, layout, and fonts. It allows you to separate the content of your website (HTML) from its visual design, making websites more maintainable and adaptable. CSS uses rules to define how elements should be displayed, targeting specific HTML elements or groups of elements.

Visit the following resources to learn more:

- [@course@CSS Full Course for Beginners](https://www.youtube.com/watch?v=n4R2E7O-Ngo)
- [@course@HTML & CSS Full Course - Beginner to Pro](https://www.youtube.com/watch?v=G3e-cpL7ofc)
- [@course@Responsive Web Design Certification - Co-Learn HTML & CSS with guided projects](https://www.freecodecamp.org/learn/2022/responsive-web-design/)
- [@article@Web.dev by Google — Learn CSS](https://web.dev/learn/css/)
- [@feed@Explore top posts about CSS](https://app.daily.dev/tags/css?ref=roadmapsh)

## Javascript

# JavaScript

JavaScript is a programming language primarily used to create interactive and dynamic content on websites. It allows developers to add features like animations, form validation, and real-time updates without needing to reload the page. It works alongside HTML and CSS to define the behavior of web pages.

Visit the following resources to learn more:

- [@roadmap@Visit Dedicated JavaScript Roadmap](https://roadmap.sh/javascript)
- [@book@JavaScript from Beginner to Professional](https://www.gurukultti.org/admin/notice/javascript.pdf)
- [@article@The Modern JavaScript Tutorial](https://javascript.info/)
- [@article@Build 30 Javascript projects in 30 days](https://javascript30.com/)
- [@video@JavaScript Crash Course For Beginners](https://www.youtube.com/watch?v=hdI2bqOjy3c&t=4s)
- [@feed@Explore top posts about JavaScript](https://app.daily.dev/tags/javascript?ref=roadmapsh)

## Keyframe Animations

# Keyframe Animations

Keyframe animations in CSS allow you to control the intermediate steps in a CSS animation sequence. Instead of just defining the start and end states, you can specify multiple points (keyframes) along the animation timeline, defining the styles an element should have at each point. This provides granular control over how an element's appearance changes over time, enabling complex and visually appealing animations.

Visit the following resources to learn more:

- [@article@@keyframes](https://developer.mozilla.org/en-US/docs/Web/CSS/@keyframes)
- [@article@CSS keyframes](https://css-tricks.com/almanac/rules/k/keyframes/)
- [@video@Learn CSS Animations in 9 Minutes](https://www.youtube.com/watch?v=z2LQYsZhsFw)

## Line Height

# Line Height

Line height in CSS controls the vertical space between lines of text within an element. It essentially defines the distance from the top of one line of text to the top of the next line. A larger line height creates more space, improving readability, while a smaller line height can make text appear cramped.

Visit the following resources to learn more:

- [@article@line-height](https://developer.mozilla.org/en-US/docs/Web/CSS/line-height)
- [@video@HTML & CSS for Absolute Beginners: Line height and spacing](https://www.youtube.com/watch?v=HaTxxAj3cBo)

## Lists

# Lists

Lists in CSS are used to style HTML list elements, such as `<ul>` (unordered list), `<ol>` (ordered list), and `<dl>` (definition list). CSS provides properties to control the appearance of list markers (bullets or numbers), their position, and the overall styling of the list items. This allows you to customize the visual presentation of lists beyond the default browser styles.

Visit the following resources to learn more:

- [@article@CSS lists and counters](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_lists)
- [@video@CSS List Styles Tutorial for Beginners](https://www.youtube.com/watch?v=jcThx0U066w)

## Margin

# Margin

Margin in CSS defines the space around an HTML element's border. It creates a gap between the element and surrounding elements, controlling the spacing and layout of content on a webpage. Margins can be set on all four sides of an element (top, right, bottom, left) and can have positive or negative values.

Visit the following resources to learn more:

- [@article@Margin](https://developer.mozilla.org/en-US/docs/Web/CSS/margin)
- [@video@How CSS Padding and Margin Works](https://www.youtube.com/watch?v=NZEz4yNITd8)

## Media Queries

# Media Queries

Media Queries are a powerful feature that allows you to apply different CSS styles based on characteristics of the device or screen being used to view a webpage. This enables you to create responsive designs that adapt to various screen sizes, resolutions, and orientations, ensuring an optimal viewing experience across a wide range of devices, from desktops to smartphones.

Visit the following resources to learn more:

- [@article@CSS media queries](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_media_queries)
- [@article@CSS Media Queries Guide](https://css-tricks.com/a-complete-guide-to-css-media-queries/)
- [@video@Learn CSS Media Query In 7 Minutes](https://www.youtube.com/watch?v=yU7jJ3NbPdA)

## Multicolumn Layout

# Multicolumn Layout

Multicolumn layout in CSS allows you to divide a block of content into multiple columns, similar to newspaper layouts. This feature enables text and other content to flow automatically from one column to the next, improving readability and making efficient use of screen space, especially for longer articles or lists. You can control the number of columns, the gap between them, and a rule (line) between the columns for visual separation.

Visit the following resources to learn more:

- [@article@CSS multi-column layout](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_multicol_layout)
- [@article@Basic concepts of multi-column layouts](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_multicol_layout/Basic_concepts)
- [@video@CSS Multi Column](https://www.youtube.com/watch?v=uwoX1JQcE-w)

## Named Colors

# Named Colors

Named colors in CSS are predefined color values represented by specific keywords. Instead of using hexadecimal codes or RGB values, you can use names like "red," "blue," "green," or "black" to style elements. These names are understood by browsers and directly translate to specific color values, offering a simple and readable way to apply basic colors to your web pages.

Visit the following resources to learn more:

- [@article@Named colors](https://developer.mozilla.org/en-US/docs/Web/CSS/named-color)
- [@video@CSS Colors Introduction - Color Names](https://www.youtube.com/shorts/lopsN9PCauk)

## Next Sibling

# Next Sibling Combinator

The next-sibling combinator in CSS (represented by the `+` symbol) selects an element that immediately follows another specific element in the HTML structure. It targets the element that is the very next sibling, meaning it shares the same parent and appears directly after the first element in the source code. This allows you to style elements based on their immediate preceding sibling.

Visit the following resources to learn more:

- [@article@Next-sibling combinator](https://developer.mozilla.org/en-US/docs/Web/CSS/Next-sibling_combinator)
- [@article@https://css-tricks.com/child-and-sibling-selectors/](https://css-tricks.com/child-and-sibling-selectors/)

## None

# Display: None

`display: none` is a CSS property value that completely removes an element from the document flow. When applied, the element will not take up any space on the page, and it will not be rendered at all. It's as if the element doesn't exist in the HTML structure for visual purposes.

Visit the following resources to learn more:

- [@article@CSS display:none and visibility:hidden – What's the Difference?](https://www.freecodecamp.org/news/css-display-none-and-visibility-hidden-the-difference/)
- [@video@We can now transition to and from display: none](https://www.youtube.com/watch?v=vmDEHAzj2XE)

## Opacity

# Opacity

Opacity in CSS controls the transparency of an element. It determines how much of the background behind the element is visible. A value of `1` means the element is fully opaque (not transparent), while a value of `0` means it is completely transparent (invisible). Values between `0` and `1` create varying degrees of transparency.

Visit the following resources to learn more:

- [@article@Opacity](https://developer.mozilla.org/en-US/docs/Web/CSS/opacity)
- [@video@CSS Opacity - One Minute Coding](https://www.youtube.com/watch?v=QdkgbodF71k)

## Outline

# Outline

In CSS, the `outline` property draws a line around an element, outside the border. Unlike borders, outlines don't affect the element's dimensions or position in the layout. They are primarily used for highlighting elements, often for accessibility purposes like indicating focus. You can control the style, color, and width of the outline.

Visit the following resources to learn more:

- [@article@Outline](https://developer.mozilla.org/en-US/docs/Web/CSS/outline)
- [@video@CSS Outline vs Border - differences, advantages, and disadvantages](https://www.youtube.com/watch?v=xx_pJ2ouGnc)

## Padding

# Padding

Padding refers to the space between the content of an element (like text or an image) and its border. It essentially creates a cushion around the content within the element's box. You can control the amount of padding on all four sides of an element (top, right, bottom, left) individually or set a uniform padding for all sides.

Visit the following resources to learn more:

- [@article@Padding](https://developer.mozilla.org/en-US/docs/Web/CSS/padding)
- [@video@How CSS Padding and Margin Works](https://www.youtube.com/watch?v=NZEz4yNITd8)

## Performance

# Performance

CSS performance refers to how efficiently CSS code is processed and rendered by a browser, impacting the speed and responsiveness of a website. Optimizing CSS for performance involves techniques like minimizing file sizes, reducing the complexity of selectors, and leveraging browser caching to ensure a smooth user experience.

Visit the following resources to learn more:

- [@article@CSS performance optimization](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Performance/CSS)
- [@article@How to Optimize Your CSS Code for Faster Web Pages](https://www.freecodecamp.org/news/how-to-optimize-your-css-code-for-faster-web-pages/)
- [@article@The Complete Guide to Optimizing CSS for Fast Page Loads](https://www.builder.io/blog/the-complete-guide-to-optimizing-css-for-fast-page-loads)

## Position

# Position

Position in CSS controls how an element is placed within its containing element or the document itself. It allows you to precisely define where an element appears on the page, influencing its relationship with other elements and the overall layout. Different position values offer varying levels of control, from static placement within the normal document flow to fixed positions that remain in place even when the user scrolls.

Visit the following resources to learn more:

- [@article@Position](https://developer.mozilla.org/en-US/docs/Web/CSS/position)
- [@video@Learn CSS Positions in 4 minutes](https://www.youtube.com/watch?v=YEmdHbQBCSQ)

## Postcss

# PostCSS

PostCSS is a tool that uses JavaScript to transform CSS. It acts as a CSS parser and provides an API to analyze and modify the CSS code. It's often used with plugins to automate tasks like adding vendor prefixes, linting CSS, or supporting future CSS syntax.

Visit the following resources to learn more:

- [@official@PostCSS](https://postcss.org/)
- [@opensource@PostCSS](https://github.com/postcss/postcss)
- [@article@What is PostCSS? How to Use Plugins to Automate CSS Tasks](https://www.freecodecamp.org/news/what-is-postcss/)
- [@video@Learn PostCSS In 15 Minutes](https://www.youtube.com/watch?v=Kn2SKUOaoT4&t=573s)

## Properties  Values

# Properties and Values

In CSS, properties are like instructions that tell the browser how to style an HTML element. Each property has a value, which specifies the exact styling to apply. For example, the `color` property determines the text color, and its value could be `red`, `#00FF00`, or `rgb(0, 255, 0)`. The combination of a property and its value is called a declaration, and declarations are the building blocks of CSS rules.

## Pseudo Classes

# Pseudo-Classes

Pseudo-classes in CSS are keywords added to selectors that specify a special state of the selected element(s). They let you style an element based on things like user interaction (e.g., hovering), its position in the document structure (e.g., the first child), or other element characteristics (e.g., being checked). They allow you to apply styles to elements dynamically without needing to modify the HTML or use JavaScript.

Visit the following resources to learn more:

- [@article@Pseudo-classes](https://developer.mozilla.org/en-US/docs/Web/CSS/Pseudo-classes)
- [@article@CSS Pseudo-classes](https://www.w3schools.com/css/css_pseudo_classes.asp)
- [@video@Learn CSS pseudo-classes in 7 minutes!](https://www.youtube.com/watch?v=Nrsy_2ogRfQ)

## Pseudo Elements

# Pseudo-Elements

Pseudo-elements in CSS let you style specific parts of an element. They allow you to add styles to elements that don't actually exist in the HTML structure, like the first line of a paragraph or content before or after an element. This is done using double colons (::) followed by the pseudo-element name.

Visit the following resources to learn more:

- [@article@Pseudo-elements](https://developer.mozilla.org/en-US/docs/Web/CSS/Pseudo-elements)
- [@article@CSS Pseudo-elements](https://www.w3schools.com/css/css_pseudo_elements.asp)
- [@video@Learn CSS pseudo-elements in 5 minutes!](https://www.youtube.com/watch?v=_LxYNxeWpBo)

## Relative

# Relative Positioning

Relative positioning in CSS allows you to shift an element from its normal position in the document flow. Instead of being fixed in place, the element is moved relative to where it _would_ have been if it were statically positioned. This movement doesn't affect the positioning of other elements around it; they behave as if the element were still in its original location. You specify the amount of movement using the `top`, `right`, `bottom`, and `left` properties.

Visit the following resources to learn more:

- [@video@CSS position deep dive](https://www.youtube.com/watch?v=fF_NVrd1s14)

## Responsive Typography

# Responsive Typography

Responsive typography is about making the text on a webpage look good and be easily readable on different screen sizes and devices. It involves adjusting font sizes, line heights, letter spacing, and other text properties to ensure optimal readability, whether someone is viewing the site on a large desktop monitor or a small mobile phone. The goal is to create a consistent and pleasant reading experience across all platforms.

Visit the following resources to learn more:

- [@article@How To Create a Responsive Text](https://www.w3schools.com/howto/howto_css_responsive_text.asp)
- [@article@The elements of responsive typography](https://blog.logrocket.com/elements-responsive-typography/)
- [@video@Responsive Typography with CSS Clamp](https://www.youtube.com/watch?v=erqRw3E-vn4)

## Rgb

# RGB Colors in CSS

RGB in CSS allows you to define colors using the Red, Green, and Blue color model. You specify the intensity of each color component (Red, Green, and Blue) as a value between 0 and 255, or as a percentage from 0% to 100%. By combining different amounts of red, green, and blue, you can create a wide range of colors. For example, `rgb(255, 0, 0)` represents pure red, `rgb(0, 255, 0)` represents pure green, and `rgb(0, 0, 255)` represents pure blue.

Visit the following resources to learn more:

- [@article@Color](https://developer.mozilla.org/en-US/docs/Web/CSS/color_value)
- [@article@rgb function](https://developer.mozilla.org/en-US/docs/Web/CSS/color_value/rgb)
- [@article@CSS RGB Colors](https://www.w3schools.com/css/css_colors_rgb.asp)
- [@video@CSS - Colors RGB & RGBA - W3Schools.com](https://www.youtube.com/watch?v=6tbUo6PXc88)

## Rgba Hsla

# rgba and hsla Colors

`rgba` and `hsla` are color models used in CSS to define colors with added transparency. `rgba` represents colors using Red, Green, Blue, and Alpha (transparency) values, while `hsla` uses Hue, Saturation, Lightness, and Alpha values. The alpha value ranges from 0 (fully transparent) to 1 (fully opaque), allowing for semi-transparent colors.

Visit the following resources to learn more:

- [@article@rgb](https://developer.mozilla.org/en-US/docs/Web/CSS/color_value/rgb)
- [@article@hsl](https://developer.mozilla.org/en-US/docs/Web/CSS/color_value/hsl)

## Rules

# CSS Rules

CSS rules are the fundamental building blocks of CSS stylesheets. Each rule specifies how particular HTML elements should be styled. A rule consists of a selector, which identifies the element(s) to be styled, and a declaration block, which contains one or more property-value pairs that define the styles to be applied. These property-value pairs are separated by semicolons and define the visual presentation of the selected elements.

Visit the following resources to learn more:

- [@article@Introduction to CSS syntax: declarations, rulesets, and statements](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_syntax/Syntax)

## Sass

# Sass

Sass (Syntactically Awesome Style Sheets) is a preprocessor scripting language that is compiled into CSS. It extends the capabilities of basic CSS by allowing you to use features like variables, nesting, mixins, functions, and inheritance. This makes CSS more maintainable, organized, and efficient to write.

Visit the following resources to learn more:

- [@official@Sass](https://sass-lang.com/)
- [@official@Sass Basics](https://sass-lang.com/guide/)
- [@article@Sass Tutorial](https://www.w3schools.com/sass/)
- [@video@Sass Crash Course](https://www.youtube.com/watch?v=nu5mdN2JIwM)

## Selector

# Selector

A selector is a fundamental part of a CSS rule. It's essentially a pattern that identifies which HTML elements the rule should be applied to. Selectors can target elements based on their tag name, class, ID, attributes, or their relationship to other elements in the document.

Visit the following resources to learn more:

- [@article@CSS selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_selectors)
- [@video@Learn Every CSS Selector In 20 Minutes](https://www.youtube.com/watch?v=l1mER1bV0N0)

## Simple Selectors

# Simple Selectors

Simple selectors in CSS are the basic building blocks for targeting HTML elements you want to style. They directly select elements based on their name (like `p` for paragraphs), ID (using `#`), or class (using `.`). These selectors are straightforward and provide a fundamental way to apply styles to specific parts of your webpage.

Visit the following resources to learn more:

- [@article@Basic CSS selectors](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/Basic_selectors)
- [@video@CSS - Simple Selectors | W3Schools](https://www.youtube.com/watch?v=ZNskBxLVOfs)

## Static

# Static Positioning

Static positioning is the default way elements are placed on a webpage. Elements with static positioning are rendered in the order they appear in the HTML, following the normal document flow. You can't move them using the `top`, `right`, `bottom`, or `left` properties.

Visit the following resources to learn more:

- [@article@CSS position deep dive](https://www.youtube.com/watch?v=fF_NVrd1s14)

## Sticky

# Sticky Positioning

Sticky positioning in CSS is a hybrid of relative and fixed positioning. An element with `position: sticky;` is initially positioned relatively, but when the user scrolls to a point where the element would normally scroll off-screen, it becomes fixed, sticking to the specified offset (e.g., `top: 0;`) until the containing block's boundary is reached.

Visit the following resources to learn more:

- [@article@CSS Position Sticky - How It Really Works!](https://elad.medium.com/css-position-sticky-how-it-really-works-54cd01dc2d46)
- [@video@A couple of cool things you can do with CSS position sticky](https://www.youtube.com/watch?v=8TyoihVGErI)
- [@video@CSS position deep dive](https://www.youtube.com/watch?v=fF_NVrd1s14)

## Subsequent Sibling

# Subsequent Sibling Combinator

The subsequent-sibling combinator in CSS is a way to select elements that are siblings (elements sharing the same parent) and appear directly after a specified element. It uses the tilde (~) symbol to denote this relationship. This selector targets all following siblings, not just the immediately adjacent one.

Visit the following resources to learn more:

- [@article@Subsequent-sibling combinator](https://developer.mozilla.org/en-US/docs/Web/CSS/Subsequent-sibling_combinator)

## Tables

# Tables

Tables in CSS are used to format tabular data on a webpage, arranging information into rows and columns. CSS provides properties to control the appearance of tables, including borders, spacing, alignment, and styling of individual cells, rows, and columns. These properties enable developers to create visually appealing and well-structured tables that present data effectively.

Visit the following resources to learn more:

- [@article@Table](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_table)
- [@video@Styling HTML tables with CSS - Web Design/UX Tutorial](https://www.youtube.com/watch?v=biI9OFH6Nmg)

## Text Alignment

# Text Alignment

Text alignment in CSS controls how text is positioned horizontally within its containing element. It determines whether text is aligned to the left, right, center, or justified (spread evenly across the line). This property enhances readability and visual appeal by organizing text in a structured manner.

Visit the following resources to learn more:

- [@article@text-align](https://developer.mozilla.org/en-US/docs/Web/CSS/text-align)
- [@article@text-align | CSS Tricks](https://css-tricks.com/almanac/properties/t/text-align/)

## Text Decoration

# Text Decoration

Text decoration in CSS refers to the styling applied to text to enhance its appearance or convey specific meanings. It primarily involves adding lines above, below, or through the text. Common decorations include underlines, overlines, and line-throughs, which can be customized with different colors, styles, and thicknesses to achieve various visual effects.

Visit the following resources to learn more:

- [@article@text-decoration](https://developer.mozilla.org/en-US/docs/Web/CSS/text-decoration)
- [@video@CSS Tutorial For Beginners - Text Decoration](https://www.youtube.com/watch?v=dm54To0EOpw)

## Text Shadows

# Text Shadows

Text shadows in CSS add depth and visual interest to text by creating a blurred, offset copy of the text behind it. This effect is achieved using the `text-shadow` property, which allows you to specify the shadow's horizontal offset, vertical offset, blur radius, and color. Multiple shadows can be applied to a single text element, creating complex and layered effects.

Visit the following resources to learn more:

- [@article@text-shadow](https://developer.mozilla.org/en-US/docs/Web/CSS/text-shadow)
- [@video@Learn CSS shadows in 3 minutes!](https://www.youtube.com/watch?v=Yqs_61ub1Ng)

## Text Spacing

# Text Spacing

Text spacing in CSS involves adjusting the space between characters, words, and lines of text. This control allows for improved readability and visual appeal by fine-tuning the horizontal and vertical spacing within text elements. Properties like `letter-spacing`, `word-spacing`, and `line-height` are used to manipulate these spaces.

Visit the following resources to learn more:

- [@article@letter-spacing](https://developer.mozilla.org/en-US/docs/Web/CSS/letter-spacing)
- [@article@word-spacing](https://developer.mozilla.org/en-US/docs/Web/CSS/word-spacing)
- [@article@CSS Text Spacing](https://www.codeguage.com/v1/courses/css/text-spacing)
- [@video@HTML & CSS for Absolute Beginners: Line height and spacing](https://www.youtube.com/watch?v=HaTxxAj3cBo)

## Text Styling

# Text Styling

Text styling in CSS involves controlling the visual appearance of text elements on a webpage. This includes properties that affect the font family, size, weight, color, and style of the text. Additionally, it encompasses properties for text alignment, decoration (like underlines), letter spacing, line height, and text transformations (such as capitalization).

Visit the following resources to learn more:

- [@article@Fundamental text and font styling](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Text_styling/Fundamentals)
- [@article@Styling Text in CSS](https://pieces.app/blog/styling-text-in-css)
- [@video@Beginner’s guide to styling text with CSS](https://www.youtube.com/watch?v=Y5TYDo9Qcv4)

## Text Transform

# Text Transform

Text transform in CSS controls the capitalization of text. It allows you to change the case of letters within an element, regardless of how the text is originally written in the HTML. You can transform text to uppercase, lowercase, capitalize (first letter of each word), or keep the original case.

Visit the following resources to learn more:

- [@article@text-transform](https://developer.mozilla.org/en-US/docs/Web/CSS/text-transform)
- [@video@CSS Tutorial For Beginners - Text Transform](https://www.youtube.com/watch?v=j0FS2hCoIjs)

## Transforms

# Transforms

Transforms in CSS allow you to alter the shape and position of elements in a two-dimensional or three-dimensional space. This includes operations like rotating, scaling, skewing, and translating elements, providing a way to create visually engaging effects and manipulate the layout without affecting the underlying document flow.

Visit the following resources to learn more:

- [@article@CSS Animations](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_animations)
- [@article@CSS Transforms](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_transforms)
- [@article@Transform](https://css-tricks.com/almanac/properties/t/transform/)
- [@video@Learn CSS transformations in 9 minutes!](https://www.youtube.com/watch?v=qdeIy9_fbxE)

## Transitions

# Transitions

Transitions in CSS allow you to smoothly change property values over a specified duration. Instead of an abrupt change, a transition creates a gradual effect when a CSS property changes, such as when hovering over an element or when a class is added or removed. This adds visual polish and improves the user experience by making interactions feel more fluid and responsive.

Visit the following resources to learn more:

- [@article@CSS transitions](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_transitions)
- [@article@Using CSS transitions](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_transitions/Using_CSS_transitions)
- [@video@Animating with CSS Transitions - A look at the transition properties](https://www.youtube.com/watch?v=Nloq6uzF8RQ)

## Units With Functions

# Units with Functions

Units with functions in CSS allow you to dynamically calculate values for properties using functions like `calc()`, `min()`, `max()`, and `clamp()`. These functions enable you to perform mathematical operations and comparisons directly within your CSS, making your designs more flexible and responsive by adapting to different screen sizes and contexts. This helps in creating more dynamic and adaptable layouts.

Visit the following resources to learn more:

- [@video@A CSS Unit Deep Dive - Learn CSS Units & When To Use Them](https://www.youtube.com/watch?v=fzZTvLmmTzM)

## Universal

# Universal Selector

The universal selector in CSS is a simple selector that matches any element on a webpage. Represented by an asterisk (\*), it applies a specific style to all elements, regardless of their type or position in the document tree. It's often used to reset or normalize styles across different browsers, ensuring a consistent baseline appearance.

Visit the following resources to learn more:

- [@article@Universal Selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/Universal_selectors)
- [@video@CSS Tutorial For Beginners - The Universal Selector](https://www.youtube.com/watch?v=EO4ToIX-ZQk)

## Visibility

# Visibility

The `visibility` property in CSS controls whether an element is visible or hidden. When an element's visibility is set to `hidden`, it disappears from the page, but the space it would have occupied remains. This is different from `display: none`, which removes the element from the document flow entirely, causing surrounding elements to reflow.

Visit the following resources to learn more:

- [@article@Visibility](https://developer.mozilla.org/en-US/docs/Web/CSS/visibility)
- [@article@CSS display:none and visibility:hidden – What's the Difference?](https://www.freecodecamp.org/news/css-display-none-and-visibility-hidden-the-difference/)

## Width  Height

# Width and Height

Width and height in CSS define the size of an element's content area. The `width` property sets the horizontal space an element occupies, while the `height` property sets the vertical space. These properties can be specified using various units like pixels, percentages, or keywords like `auto`.

Visit the following resources to learn more:

- [@article@CSS Width / Height Properties](https://www.programiz.com/css/width-height)
- [@video@Learn CSS height and width in 6 minutes!](https://www.youtube.com/watch?v=QctF-i4-GuM)

## Z Index  Stacking Context

# Z-Index and Stacking Context

Z-index in CSS controls the vertical stacking order of elements that overlap. Elements with a higher z-index value will appear in front of elements with a lower z-index value. Stacking context is a three-dimensional conceptualization of HTML elements along an imaginary z-axis relative to the viewer, which determines the order in which elements appear in front of or behind each other.

Visit the following resources to learn more:

- [@article@z-index](https://developer.mozilla.org/en-US/docs/Web/CSS/z-index)
- [@video@CSS Z Index Property: What is CSS Z-Index, Stacking Order, and Why Your Z-Index Is Not Working?](https://www.youtube.com/watch?v=vo1JBj-OAa8)
