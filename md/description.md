# Human Software Language (HSL)

HSL introduces a new level of abstraction in programming, seamlessly merging human language with code via advanced Language Models (LLMs) and intuitive markdown syntax. This  approach effortlessly transforms ideas into powerful software, eliminating complex syntax and steep learning curves. HSL streamlines development across various platforms, making it fast, accessible, and scalable. It's a redefined programming paradigm shift that fosters innovation through collaboration, pushing the boundaries of what's possible. With HSL, your imagination sets the pace.

## Vision

To democratize programming and empower individuals from all backgrounds to create powerful software using natural language, making software development more accessible, collaborative, and efficient for everyone.

## Mission

- Develop a robust and intuitive programming paradigm that allows users to express their ideas and requirements using plain English or other human languages.
- Leverage advanced language models and machine learning techniques to intelligently transpile human language instructions into production-ready source code across various platforms and frameworks.
- Provide a seamless and iterative development experience that enables users to rapidly prototype, refine, and optimize their software based on real-world feedback and insights.
- Foster a vibrant community of developers, domain experts, and end-users who collaborate, share knowledge, and contribute to the growth and improvement of HSL.
- Continuously evolve and expand HSL to support emerging technologies, platforms, and use cases, ensuring its relevance and effectiveness in a rapidly changing software landscape.
- Promote inclusivity, diversity, and innovation in software development by removing barriers to entry and enabling individuals from diverse backgrounds to unleash their creativity and problem-solving skills.
- Collaborate with industry partners, academic institutions, and open-source communities to drive the adoption, standardization, and ecosystem development around HSL.
- Empower businesses, startups, and organizations to accelerate their digital transformation journeys by leveraging HSL to build scalable, maintainable, and future-proof software solutions.
- Advocate for responsible and ethical use of AI and language models in software development, ensuring transparency, accountability, and alignment with societal values.
- Revolutionize the way software is conceived, developed, and maintained, ushering in a new era of human-centric programming that puts the power of software creation in the hands of everyone.

## Key Features

- **Natural Language Programming**: HSL allows users to express their ideas and requirements using plain English or other human languages, making programming accessible to both technical and non-technical users.
- **Markdown-based Syntax**: HSL code is written using a familiar markdown syntax, enabling users to structure their programs using headers, bullet points, and other formatting elements.
- **Intelligent Transpilation**: HSL employs LLMs to intelligently transpile human language instructions into production-ready source code in popular programming languages and frameworks.
- **Multi-Platform Support**: HSL programs can target various execution environments, including web browsers, operating systems, mobile devices, and cloud platforms, through platform-specific components.
- **Component-based Architecture**: HSL promotes code reusability and modularity through the use of components, which encapsulate specific functionalities and can be composed to create complex systems.
- **Iterative Refinement**: HSL supports an iterative development process, allowing users to refine and optimize their programs based on execution results and user feedback.
- **Seamless Integration**: HSL seamlessly integrates with modern technologies and frameworks such as React, Supabase, Flutter enabling the creation of modern applications.

## Benefits

- **Accelerated Development**: HSL significantly speeds up the software development process by abstracting away low-level implementation details and enabling rapid iteration.
- **Increased Productivity**: By focusing on high-level logic and business requirements, HSL boosts overall productivity and allows users to deliver software faster.
- **Collaborative Development**: HSL fosters collaboration between technical and non-technical team members by providing a common language for expressing ideas and requirements.
- **Accessibility**: HSL makes programming accessible to a broader audience, empowering non-technical users to actively participate in software development.
- **Versatility**: HSL's versatility allows it to handle a wide range of use cases, from simple scripts to complex enterprise applications.

HSL represents a paradigm shift in software development, combining the expressiveness of human language with the precision and efficiency of traditional programming. It unlocks the potential for rapid prototyping, iterative development, and seamless collaboration, making software development more accessible, efficient, and enjoyable for everyone involved.

## Workflow

1. **Specification**: The user provides a natural language specification or prompt describing the desired software functionality.
2. **Program Generation**: HSL generates a high-level program structure based on the user's prompt, outlining the main components and their interactions.
3. **Refinement**: The user validates and refines the generated program structure, providing additional details and constraints.
4. **Dependency Resolution**: HSL intelligently resolves dependencies between components, ensuring proper data flow and control flow.
5. **Transpilation**: The refined HSL program is transpiled into executable source code in the target programming languages and frameworks.
6. **Execution**: The transpiled code is executed within the specified execution environments, such as web browsers, operating systems, or mobile devices.
7. **Testing and Validation**: HSL automatically generates test cases and validates the program's behavior against the user's requirements.
8. **Iterative Improvement**: Based on the execution results and user feedback, the program is iteratively refined and optimized using LLMs and machine learning techniques.

## Execution Environments

HSL supports multiple execution environments through platform-specific components:

- **Browser**: Components for web automation, website interaction, and browser-based functionality.
- **Operating System**: Components for OS-level operations, file manipulation, and command-line utilities.
- **Backend**: Components for database management, storage, and user authentication using the Supabase platform.
- **Frontend**: Components for building user interfaces and interactive web applications using frameworks like React and Vue.
- **Mobile**: Components for developing mobile applications for iOS and Android platforms using frameworks like Flutter.
- **Custom**: Extensibility for defining custom components and execution environments.

## Syntax and Semantics

HSL code is written using a markdown-based syntax with specific semantic rules:

- **Program Structure**: HSL programs are organized into independent sections, each focusing on a specific feature or workflow. Sections are defined within the `<program.md>` file or in separate files for better organization.
- **Components**: Components are the building blocks of HSL programs and can be defined inline within `<program.md>` files or in separate `<component.md>` files. Components encapsulate specific functionalities and can be composed to create more complex systems.
- **Variables**: Variables are automatically inferred and constructed by LLMs based on the program context and component interactions. They can be referenced using backticks (`variableName`) within the component steps.
- **Control Structures**: Control structures like conditionals and loops are represented using indentation and natural language expressions. LLMs handle the interpretation and generation of appropriate control flow constructs.
- **Component Composition**: Components can be dynamically composed and nested within other components to create new functionalities. Composition is achieved by referencing existing components within the steps of a new component.

## Example HSL Code

Here's an example HSL program that automates the process of analyzing search results from Google and sending a summary via email:

```markdown
# OS: Analyze Results and Send Them by Email

This component automates the process of analyzing search results from Google and sending a summary via email.

## Input

- `request: text` - The query to search on Google.

## Output

- `emailConfirmation: text` - Confirmation that the email with the search results summary has been sent successfully.

## Steps

1. Use the `<Browser: Google search>` component to search Google with `request`.
2. Use the `<OS: OpenAI Analyze Table>` component to analyze the search result. Specify the analysis type as "Summary".
3. Format `analysisResults` into `emailContent`: Extract top insights and create a summary paragraph. Include `summaryParagraph`, `topInsightsList`, and `relevantLinks` in `emailContent`.
4. Extract and format the top 5 insights from `analysisResults`, including a brief summary of each insight, the main keywords identified, and a link to the source. Combine these elements into a structured email body, starting with an introduction that states the purpose of the email and followed by a bullet-point list of insights and summaries.
5. Prompt user for `[email]` where to send report.
6. Use the `<Browser: Send Gmail Message>` component to send the analysis.
7. Return `emailSentConfirmation` as the output of this component, confirming the email dispatch.
```

This program leverages multiple components, such as Browser: Google search, OS: OpenAI Analyze Table, and Browser: Send Gmail Message, to accomplish the task of analyzing search results and sending a summary email.

## Platforms

HSL supports modular and extensible execution environments through platform-specific components. These components encapsulate the functionality and interactions specific to each platform, allowing HSL programs to seamlessly integrate with various technologies and frameworks.

### Browser

- HSL can generate a set of browser-specific components that enable web automation and interaction with websites.
- Browser components can perform actions such as navigating to URLs, filling forms, clicking buttons, extracting data from web pages or make more complex workflows.
- Example components:
- `Browser: Google Search`: Performs a Google search and retrieves the search results.
- `Browser: Send Gmail Message`: Composes and sends an email message through Gmail.

### Operating System (OS)

- HSL includes OS-specific components that facilitate interaction with the operating system and execution of command-line utilities.
- OS components can perform tasks such as file manipulation, process management, and system configuration.
- Example components:
- `OS: OpenAI Analyze Table`: Uses OpenAI to analyze data from a table and generate insights or summaries.
- `OS: Compress Files`: Compresses a set of files into a zip archive.

### Supabase

- HSL provides Supabase-specific components that integrate with the Supabase platform for database management, storage, and user authentication.
- Supabase components can perform operations such as querying databases, managing storage buckets, and handling user authentication flows.
- Example components:
- `Supabase: Create User`: Creates a new user in the Supabase authentication system.
- `Supabase: Query Database`: Executes a database query and retrieves the results.

### Frontend

- HSL offers frontend-specific components that facilitate the development of user interfaces and interactive web applications.
- Frontend components can generate React components, integrate with popular frontend frameworks, and handle user interactions.
- Example components:
- `Frontend: Create Login Form`: Generates a login form component with input fields and validation.
- `Frontend: Fetch Data from API`: Retrieves data from an API and renders it in the frontend.

### Mobile

- HSL includes mobile-specific components that enable the development of mobile applications for iOS and Android platforms.
- Mobile components can generate Flutter widgets, handle platform-specific functionality, and interact with mobile device features.
- Example components:
- `Mobile: Create Navigation Menu`: Generates a navigation menu component for mobile apps.
- `Mobile: Access Camera`: Accesses the device's camera for capturing photos or videos.

### Custom

- HSL allows users to define custom components for specific platforms or frameworks not covered by the built-in components.
- Custom components can be created by writing custom interpreters, validators, and executors that adhere to the HSL component specification.
- Example custom components:
- `Custom: Slack Bot`: Implements a Slack bot that responds to user commands and interactions.
- `Custom: IoT Device Control`: Controls an IoT device through a custom protocol or API.

By leveraging platform-specific components, HSL programs can seamlessly integrate with various technologies and frameworks, enabling the development of applications that span across different platforms. These components abstract away the complexities of each platform and provide a unified and intuitive way to interact with them using natural language instructions.

## Transpilation

1. User writes HSL code in a markdown format, specifying the program structure, components, and logic using natural language.
2. The HSL transpiler, powered by a Language Model (LLM), analyzes the markdown code and generates an Abstract Syntax Tree (AST) using the Lark parsing library.
3. The AST represents the program structure and components in a machine-readable format.
4. The transpiler traverses the AST and generates target source code in the appropriate programming languages and frameworks based on the specified execution environments (e.g., frontend, backend, browser, OS, mobile).
5. The generated source code is syntactically correct and follows the conventions and best practices of the target languages and frameworks.
6. LLMs assist in generating idiomatic and optimized code snippets for the target languages and frameworks.

## Execution

1. The transpiled source code is executed within the respective execution environments.
2. The HSL runtime provides a unified interface for managing the execution across different environments.
3. The runtime handles the orchestration of component interactions, data flow, and control flow based on the program structure defined in the HSL code.
4. Runtime errors and exceptions are caught and handled gracefully, providing informative error messages and suggestions for resolving issues.
5. LLMs analyze the runtime behavior and provide intelligent suggestions for optimizing performance and resource utilization.
6. The execution results are captured and made available for further analysis and refinement.

## Testing

1. HSL emphasizes automated testing to ensure the correctness and reliability of the generated software.
2. The transpiler generates test cases based on the component descriptions, input/output specifications, and example scenarios provided in the HSL code.
3. LLMs enhance the test case generation process by creating comprehensive test suites that cover various edge cases, boundary conditions, and potential error scenarios.
4. The generated test cases cover various aspects of the program, including unit tests, integration tests, and end-to-end tests.
5. The HSL runtime executes the test cases and reports the results, highlighting any failures or discrepancies.
6. Test coverage metrics are generated to assess the thoroughness of the testing process and identify areas that require additional testing.
7. LLMs validate the generated test cases against the component's expected behavior and suggest improvements to the test coverage.

## Refinement

1. The execution results and test outcomes are analyzed to identify opportunities for refinement and optimization.
2. The HSL transpiler and runtime employ machine learning techniques, including LLMs, to suggest improvements and optimizations based on patterns and best practices learned from previous iterations.
3. LLMs analyze the code structure, runtime behavior, and test results to provide targeted recommendations for enhancing performance, scalability, and maintainability.
4. Users can review the suggested refinements and provide feedback to guide the system towards generating more efficient and effective code.
5. The refinement process is iterative, allowing for continuous improvement of the generated software.
6. LLMs learn from user feedback and adapt their suggestions over time to align with project-specific requirements and preferences.

## Software Components

### HSL Transpiler

The HSL Compiler is the core component responsible for transpiling HSL code into executable code in various target languages and frameworks. It consists of the following sub-components:

- Lexical Analyzer: Tokenizes the HSL code and identifies the individual elements of the language.
- Parser: Parses the tokens and generates an Abstract Syntax Tree (AST) representing the structure of the HSL program.
- Semantic Analyzer: Performs semantic analysis on the AST, checking for type consistency, variable scoping, and other language-specific rules.
- Code Generator: Traverses the AST and generates target code in the specified languages and frameworks based on the execution environments.
- Optimizer: Applies optimization techniques to the generated code to improve performance and efficiency.

### HSL Runtime

The HSL Runtime provides the execution environment for HSL programs. It includes the following components:

- Interpreter: Executes the transpiled code in the target languages and frameworks, managing the program flow and component interactions.
- Environment Manager: Manages the execution environments (e.g., Browser, OS, Supabase, Frontend, Mobile) and handles the communication and data flow between components.
- Runtime Library: Provides a set of built-in functions, utilities, and APIs that can be used by HSL programs during execution.
- Error Handling: Implements error handling mechanisms to catch and handle runtime errors and exceptions gracefully.

### HSL IDE Plugin

The HSL IDE Plugin integrates HSL development capabilities into popular IDEs. It includes the following features:

- Syntax Highlighting: Provides syntax highlighting for HSL code, making it easier to read and understand.
- Code Completion: Offers intelligent code completion suggestions based on the HSL language grammar and component definitions.
- Error Highlighting: Highlights syntax errors and provides meaningful error messages to assist in debugging.
- Interactive Playground: Provides an interactive environment for executing HSL code and visualizing program flow and intermediary results.
- Debugging Tools: Integrates debugging capabilities, allowing developers to set breakpoints, step through the code, and inspect variable values.

### HSL Testing Framework

The HSL Testing Framework enables automated testing of HSL components and programs. It includes the following components:

- Test Case Generator: Generates test cases based on the component descriptions, input/output specifications, and example scenarios provided in the HSL code.
- Test Runner: Executes the generated test cases and reports the results, highlighting any failures or discrepancies.
- Test Coverage Analyzer: Measures the test coverage of HSL programs and identifies areas that require additional testing.
- Test Reporting: Generates comprehensive test reports, including test results, code coverage, and performance metrics.

### HSL Build System

The HSL Build System automates the build process for HSL programs. It includes the following components:

- Dependency Manager: Manages the dependencies between HSL components and ensures that the required libraries and frameworks are available.
- Build Configuration: Allows developers to define build configurations, specifying target platforms, optimization levels, and other build-related settings.
- Build Scheduler: Schedules and orchestrates the build process, ensuring that the necessary steps are executed in the correct order.
- Artifact Generator: Generates the final executable artifacts (e.g., binaries, packages) based on the build configuration.

## Automatic Data Flow

1. When an HSL program is executed, the runtime analyzes the program structure and identifies the data dependencies between components.
2. The runtime automatically infers the data types and formats based on the component definitions and the context in which they are used.
3. As the program execution progresses, the runtime manages the data flow between components, ensuring that the output of one component is correctly passed as input to the next component in the sequence.
4. If components are executed in different execution environments (e.g., Browser, OS, Supabase), the runtime handles the necessary data serialization and deserialization to ensure compatibility.
5. The transpiler generates the necessary code to facilitate data transfer and transformation between components, taking into account the specific requirements of each execution environment.

## Data Transformations

1. HSL supports inline data transformations within component steps, allowing for seamless data manipulation and adaptation.
2. The transpiler employs LLMs to intelligently generate code snippets for data transformations based on the component descriptions and the surrounding context.
3. Common data transformations, such as filtering, sorting, aggregation, and formatting, can be expressed using natural language instructions within the component steps.
4. The LLMs analyze the natural language instructions and generate the appropriate code to perform the desired data transformations, leveraging the capabilities of the target programming languages and frameworks.
5. Data transformations can be applied to various data types, including tables, text, images, and structured data, depending on the requirements of the components and the execution environments.

## Data Validation

1. HSL incorporates data validation mechanisms to ensure the integrity and consistency of data flowing between components.
2. The transpiler generates code to validate input data against the specified data types and constraints defined in the component definitions.
3. If data validation fails, the runtime raises appropriate errors or exceptions, providing informative error messages to assist in debugging and troubleshooting.
4. Error handling logic can be defined within components to gracefully handle and recover from data-related errors, ensuring the robustness and reliability of the program execution.

## HSL Semantic and rules

### `<program.md>`

The `<program.md>` file defines the overall program structure, with multiple independent sections that encompass global business logic, platform-specific logic, component usage, and data transformations.

In the `<program.md>` file, you can:

- Define the initial program state and global variables.
- Organize the program into multiple independent sections, each representing a specific feature or workflow.
- Outline the sequence of steps or actions that the section should execute.
- Specify the execution environments (e.g., `Browser`, `OS`, `Supabase`, `Frontend`, `Mobile`) required for each step.
- Define and describe the components specific to each execution environment.
- Outline the steps or operations that each component performs within its respective execution environment.
- Handle data transformations between components, both within and across execution environments.
- Implement error handling and exception management at the section and component levels.
- Define conditional logic and control flows that govern the section's execution and component behavior.
- Compose and nest components to create more complex functionalities.

The `<program.md>` file serves as a unified source of truth, combining the high-level program flow, global business logic, and platform-specific details into a single cohesive file organized into independent sections.

### `<component.md>`

The `<component.md>` file encapsulates reusable units of functionality that can be shared across multiple execution environments or programs. Components are the building blocks of HSL programs and can be composed and nested to create more complex functionalities.

In the `<component.md>` file, you can:

- Define the component's purpose and functionality.
- Outline the steps or operations that the component performs.
- Handle data transformations within the component, if necessary.
- Implement component-level error handling and exception management.
- Define conditional logic and control flows that govern the component's execution.
- Provide examples and test cases for the component.

Components promote code reusability and maintainability by encapsulating specific functionalities that can be shared across different execution environments or programs. They can be referenced and invoked from within `<program.md>` files, enabling a modular and composable approach to building software systems.

### Components

Components are the building blocks of HSL programs, and they can be defined inline within `<program.md>` files or in separate `<component.md>` files.

```markdown
# Component Name

Brief description of the component's purpose and functionality.

## Input

- `inputVariable1: type` - Description of the input variable.
- `inputVariable2: type` - Description of the input variable.
- ...

## Output

- `outputVariable1: type` - Description of the output variable.
- `outputVariable2: type` - Description of the output variable.
- ...

## Context (optional)

Additional context or scenario in which the component is used.

## Secrets (optional)

- `secretVariable1: type` - Description of the secret variable (e.g., API keys, passwords).
- `secretVariable2: type` - Description of the secret variable.
- ...

## Steps

1. Describe the component's logic as a series of steps.
2. Use numbered lists or bullet points to represent the sequence of steps.
3. Highlight important actions, conditions, or decision points within the steps.
4. Reference other components using backticks, e.g., `Another Component`.
5. Inline data transformations can be performed within the steps.
   - Provide clear descriptions of data transformations.
   - Use specific libraries, functions, or techniques for data manipulation.
6. Handle errors and exceptions gracefully.
   - Include clear error messages and meaningful error codes.
   - Provide examples of handling common error scenarios or edge cases.
7. Use indentation to represent control structures (conditionals, loops).
   - Clearly indicate the conditions or loop criteria.
   - Indent the steps within the control structure.

## Examples (optional)

- Provide examples or sample code snippets illustrating how to use the component.
- Include examples of input and output data formats.

## Notes (optional)

- Include any additional notes, considerations, or best practices related to the component.
- Provide guidelines for customization or extension of the component.
```

### Variables

- Variables are automatically inferred and constructed by LLMs based on the program context and component interactions.
- Use `<importName>` for importing external libraries, modules, or components.
- Use `variableName` to reference variables within the component steps.
- Use `[variableName]` for platform-specific variables, such as selectors in web browsers, or for prompting user input inside the `program`.
- Use `(variableName)` for global variables that are accessible across the entire program.
- Variable types and scopes are inferred automatically based on the surrounding context.
- Nesting of variables can be represented using `<parentVariable.childVariable>` syntax.

### Control Structures

- Use indentation to represent control structures like conditionals and loops.
- Express conditionals and loops using natural language, e.g., "If condition is true, do this. Otherwise, do that."
- Advanced natural language processing techniques can be employed to handle complex control flow scenarios.

### Component Composition

- Components can be dynamically composed and nested within other components.
- To compose a new component from existing ones, define a new component and reference the other components within its Steps section.

## Program Structure

- Programs are organized into independent sections, each focusing on a specific feature or workflow.
- Sections can be defined within the `<program.md>` file or in separate files for better organization.
- Sections should have a clear purpose and a sequence of steps to accomplish their goals.
- Each step within a section can reference components specific to different execution environments.
- Data flow between components is automatically managed by LLMs based on the program context and component interactions.
- Error handling and exception management should be implemented at both the section and component levels.
- Conditional logic and control flows can be used to govern the execution of sections and components.

## Best Practices

- Decompose complex functionalities into smaller, reusable components.
- Use descriptive names for components, variables, and sections to enhance code readability.
- Provide clear descriptions and context for each component to facilitate understanding and maintainability.
- Utilize the appropriate execution environments for each component based on its functionality and requirements.
- Handle errors and exceptions gracefully to ensure a robust and reliable software system.
- Use consistent formatting and indentation to improve code readability and maintainability.
- Test components and sections thoroughly to validate their functionality and identify potential issues.
- Document the program structure, components, and usage instructions to facilitate collaboration and future maintenance.

## Examples

```markdown
# OS: Analyze Results and Send Them by Email

This component automates the process of analyzing search results from Google and sending a summary via email.

## Input

- `request: text` - The query to search on Google.
- `email: text` - The email where send report to.

## Output

- `emailConfirmation: text` - Confirmation that the email with the search results summary has been sent successfully.

## Steps

1. Use the `<Browser: Google search>` component to search Google with `request`

2. Use the `<OS: OpenAI Analyze Table>` component to analyze the `searchResults`. Specify the `analysisType` as "Summary" and use the `searchResults` as `dataTable`.

3. Prepare the email content based on the `analysisResults`. The email content should include key insights, top results, or any relevant summary information obtained from the analysis.

4. Use the `<Browser: Send Gmail Message>` component to send the analysis.

5. Return `emailSentConfirmation` as the output of this component, confirming the email dispatch.
```

```markdown
# Browser: Google search

This process streamlines the task of retrieving information from the web based on a user's query, covering various content types like text, images, news, and videos. It is designed to efficiently collect data or references pertinent to a specific topic.

## Input

- `searchQuery: text` - The user-provided query to search for. This is the main input from the user.
- `contentType: text` - Default is "General". Specifies the content type to be searched options like "General", "Images", "News", "Videos".
- `count: number` - Default is 10. The quantity of search results the user requests.

## Output

- `searchResults: table` - A compilation of search results, detailing titles, links, snippets and content types

## Steps

1. Open the search page at `https://google.com`.
2. In the search box `[search box]`, enter your query `searchQuery`.
3. Initiate the search by clicking `[search button]`.
4. If `contentType` is not "General":
   - Look for `[contentType tab/button]`. If it exists, select it to filter results accordingly.
   - Otherwise, note that the specific content type is not available.
5. Set a variable `resultsCollected` to 0 for tracking the number of results.
6. Collect results until reaching `count`:
   - Find `[titles]`, `[links]` and `[snippets]` in `[results area]`and add them to`searchResults`.
   - Update `resultsCollected` with the number of items found.
   - If `resultsCollected` is less than `count`, proceed to the next page by `[scroll]` for more results.
7. Finalize the search by organizing all collected information into `searchResults`.
```

```markdown
# OS: OpenAI Analyze Table

This component uses OpenAI to turn data from a table into actionable insights, summaries, or predictions, making complex data easy to understand.

## Input

- `dataTable: table` - The table with data to be analyzed. Must have headers for context.
- `analysisType: text` - Specifies the analysis needed, such as "Summary", "Trend Analysis", etc.
- `parameters: text optional` - Additional instructions to narrow down the focus of the analysis.

## Output

- `analysisResults: text` - Insights, summaries, or predictions derived from the table data.

## Secret

- `openaiApiKey: text` - The API key for authenticating requests to OpenAI. This key should be securely stored and used only as needed for API requests.

## Steps

1. Convert `dataTable` to a structured text or JSON that includes headers and data points, suitable for analysis by OpenAI.

2. Build a detailed prompt that includes `analysisType` and incorporates `parameters` if provided. The prompt should clearly direct OpenAI to perform the specified analysis on the table data.

3. If `parameters` are specified, integrate them into the prompt to ensure the analysis focuses on the desired aspects of the table, such as specific columns or data points.

4. Format and send an API request to OpenAI with the prepared prompt and table data. The request should adhere to OpenAI's API guidelines, including authentication and the appropriate configuration for the analysis task.

5. Await the response from OpenAI, then extract and process the `analysisResults`. This may involve parsing OpenAI's output to identify the main insights, trends, or predictions relevant to the requested analysis.

6. Clean up and format the `analysisResults` to ensure they are clear and directly address the analysis objectives. The results should be ready for presentation or further action.

7. Provide the `analysisResults` as the output, delivering a comprehensive analysis of the table data according to the specified type and focus of the analysis.
```

```markdown
# Browser: Send Gmail Message

This process automates the task of composing and sending an email message through Gmail. It is designed to simplify communication by allowing users to quickly send emails to one or more recipients, with optional attachments, subject lines, and message bodies.

## Context

Activated when a user needs to send an email via Gmail, whether for personal or professional communication. This includes sending updates, files, or any information to contacts efficiently.

## Input

- `recipientEmail: text` - The email address of the recipient. Multiple email addresses can be separated by commas for multiple recipients.
- `subject: text` - The subject line of the email. This is optional; if not provided, the email will have no subject.
- `messageBody: text` - The main content of the email. This is optional; if not provided, the email will be sent with an empty body.
- `attachments: text` - Files locations to be attached to the email. This is optional; if not provided, the email will be sent without attachments.

## Output

- `emailSentConfirmation: table` - Confirmation that the email has been sent successfully, including the time of sending.

## Steps

1. Navigate to `https://mail.google.com/` and ensure you are logged in to your Gmail account.
2. Click on the `[compose button]` to open a new message window.
3. In the `To` field `[to field]`, enter the recipient's email address `recipientEmail`. For multiple recipients, separate each email address with a comma.
4. If `subject` is provided:
   - Find the `Subject` field `[subject field]` and enter `subject`.
5. If `messageBody` is provided:
   - Locate the `Message body` area `[message body area]` and enter `messageBody`.
6. If `attachments` are provided:
   - Click on the `[attach files button]` and select the files from your computer to attach to the email.
7. Once all information is entered, click the `[send button]` to send the email.
8. Confirm that the email has been sent by checking for a "Message sent" notification `[message sent notification]` and log the confirmation and time of sending as `emailSentConfirmation`.
```


## Notes from talks

```
- How will the paradigm of clicking a button in a web browser be implemented? Vision interface?
- I would narrow it down, lay the foundation for modularity, but start with a small, single direction, a simple concept (make an automaton around the browser, browsers are now custom on all platforms, it seems) and expand it. But I would present it through a general model, like we will expand in general, like you have.
```

Vision models are slower and more expensive and will always be that way, and there is enough semantic data in the DOM tree. I started working on this with the idea that software doesn't have to operate with hardware through the same interfaces as humans to achieve the same goals more simply/efficiently. The advantage of operating the browser through code is speed and cost-effectiveness. That is, in this case, we take up the time of generation/validation/regeneration, but after that, the code is executed without referring to the LLM, which can nevertheless be done for content analysis and decision making.

In general, the idea of DSL came when it was possible to confirm the hypothesis with the help of R&D that current LLMs have the cognitive ability to write and adapt code to achieve the expected result in a dynamic external environment.

Experiment(without man in the middle):

1. There is a YML config generated with the help of GPT-4 and a template from the prompt - "Parse 30 kitesurfing spots in Fortaleza, Brazil" which describes how to operate the browser. As a result, it describes the logic of parsing results and page-by-page navigation with clicks that do not imply lazy loading (LLM was mistaken) (50 lines).

2. There is a js algorithm that builds a simplified DOM tree for LLM with deterministic IDs on all important elements that do not change when translating content, new neighbors of the element, and changes to elements at other levels of the DOM tree (popups do not affect). It works with complex DOM cases like Facebook and Gmail (context length allows). Example for Google's main page:

```
- html[did="4q3f"] data-lt-installed: true
  - body[did="1c6f"] data-dt: 1
    - div[did="3p30"] data-hveid: 1
      - div[did="734h"] role: navigation
        - div[did="216g"] id: gb
          - div[did="3c0m"] data-ogsr-up: 
            - div[did="164m"] data-ogbl: 
              - a[did="5o42"] aria-label: Mail (opens in a new tab), data-pid: 23text: "Mail" 
              - a[did="2z37"] aria-label: Image search (opens in a new tab), data-pid: 2text: "Images"
            - div[did="3426"] data-ogsr-fb: true, data-ogsr-alt: , id: gbwa
              - a[did="5143"] aria-label: Google Apps, aria-expanded: false, role: button
            - a[did="4l4q"] aria-label: Google Account: MindsightsAI
(m@hslang.ai), role: button
              - img[did="1l4l"] alt: , aria-hidden: true, data-noaft: , data-atf: 1, data-frt: 0
      - img[did="2027"] alt: Google, data-atf: 1, data-frt: 0        
      - form[did="0n4z"] role: search
        - div[did="5p6y"] data-alt: false, data-biboe: false, data-efaql: false, data-hp: true
          - div[did="0d0l"] data-hpmde: false, data-mnr: 10  
            - textarea[did="531l"] aria-controls: Alh6id, aria-owns: Alh6id, title: Search, value: , aria-label: Find, aria-autocomplete: both, aria-expanded: false, aria-haspopup: false, id: APjFqb, role: combobox, data-ved: 0ahUKEwi2hqHchseFAxWnpZUCHRCKDbEQ39UDCAw
          - div[did="2z57"] aria-label: Onscreen keyboard, role: button   
          - div[did="1y47"] aria-label: Voice search, role: button, data-ved: 0ahUKEwi2hqHchseFAxWnpZUCHRCKDbEQvs8DCA4
          - div[did="340x"] data-base-lens-url: https://lens.google.com, data-image-processor-enabled: true, data-is-images-mode: false, data-preferred-mime-type: image/jpeg, data-propagated-experiment-ids: , aria-label: Search by image, role: button, data-ved: 0ahUKEwi2hqHchseFAxWnpZUCHRCKDbEQhqEICA8     
          - div[did="1l3o"] data-ved: 0ahUKEwi2hqHchseFAxWnpZUCHRCKDbEQ4d8ICBs
          - input[did="6l32"] value: Google Search, aria-label: Google Search, role: button, type: submit, data-ved: 0ahUKEwi2hqHchseFAxWnpZUCHRCKDbEQ4dUDCBw  
          - input[did="2w4g"] value: I'm Feeling Lucky, aria-label: I'm Feeling Lucky, type: submit, data-ved: 0ahUKEwi2hqHchseFAxWnpZUCHRCKDbEQ19QECB0
      - div[did="3o5k"] id: gws-output-pages-elements-homepage_additional_languages__als  
        - div[did="583z"] id: SIvCobtext: "Google services are available in these languages:"
          - a[did="2f6g"] text: "Português (Brasil)"
      - div[did="3j4k"] role: contentinfo
        - div[did="585f"] text: "Brazil"
        - div[did="3d2z"] data-sfe: false, data-sfsw: 1380
          - a[did="2v67"] text: "About Google" 
          - a[did="5j19"] text: "Advertising"
          - a[did="0w25"] text: "Business"  
          - a[did="4h6b"] text: "How Google Search works"
          - a[did="2s54"] text: "Privacy" 
          - a[did="4d36"] text: "Terms"  
          - span[did="4d4k"] data-ffp: false
            - g-popup[did="3e5c"]
              - div[did="1b6b"] aria-expanded: false, aria-haspopup: true, role: button  
                - div[did="1a5h"] aria-controls: _npkeZra_FKfL1sQPkJS2iAs_6, aria-haspopup: truetext: "Settings"
```

3. Using GPT-4 with [DSPY](https://github.com/stanfordnlp/dspy), the LLM program further writes the browser control function code based on the YAML config (python + playwright).
4. We get code with errors from the compiler (python).  
5. GPT-4 from the summer of 2024 fixes the errors on the first try.
6. We run it again, part of the code is executed, we see the SERP results, but click errors occur to go to the next page (as described in yaml).
7. We feed the yaml file, the current simplified DOM diff(item 2) and the run errors into the LLM program.
8. We get a changed YAML config with lazy load logic that looks valid.  
9. We send the new config and the LLM program generates and then the executor executes the code with the expected result on the first try.
10. We get the output with SERP in the format described in the YAML config, as a TXT file as described in the config.

That is, the plan and path is the same as you described, to start with the browser (or rather now a level lower with python, which can generate OS-specific python code), to work out and think through the dev flow in DSL: Semantic, Runtime, AST Tree, [Language Server Protocol](https://microsoft.github.io/language-server-protocol/), [Debug Adapter Protocol](https://microsoft.github.io/debug-adapter-protocol/), Playground inside IDE (streamlit app). The playground content allows you to control transpiling and code execution with buttons depending on the cursor position in the MD file mixed with a chatgpt-like experience for generating/modifying HSL programs. The next big step is to transfer the experience from the browser experiment into the language.

```
- How to integrate certain programs into the OS, their launch API for start, stop, switching between windows, and so on. Need tighter OS integration, which can be time-consuming. Write a lot of serialization/deserialization.  
```

There are different options here, but the fact is that a huge number of people are working on solving this problem, mostly using vision models, for example [Open Interpreter](https://github.com/OpenInterpreter/open-interpreter) or [OSWorld](https://github.com/xlang-ai/OSWorld)

The easiest way is to use "Custom components can be created by writing custom interpreters, validators, and executors that adhere to the HSL component specification." At the same time, the transpiler must take into account the current OS (different OS - different platforms into which HSL can be transpiled).

That is, it seems that HSL should easily adapt and strengthen over time not only from the improvement of models, but also with the release of new agents/platforms that can themselves be new levels of abstraction over current technologies.  

```
- Querying the DB - also needed in metrics. How to get into the code level if the DB code (query) is incorrect? This is the paradigm that we write code in a simple language (natural), it is based on statistical models. And there will be errors and we need an interface and a set of rules and approaches for debugging and interacting with how the interpreter (LLM) behaved. It would be cool to loop this so that people fix the interpreter's behavior, and you retrain the LLM, resulting in a collective model.
```

For Supabase, metrics are stored in Prometheus. It works [like this](https://supabase.com/blog/supabase-reports-and-metrics) [github](https://github.com/supabase/supabase-grafana)  

But if at the level of the development process - then in the playground the user controls the process of transpilation, testing and launching, this also includes displaying the DAG, in general the topic of graphs is hot and applicable in many places, there is a lot of research, but personally I do not yet understand how to solve the problem of updating large graphs for reasonable resources (need help).

Here comes the first stage where collaboration can be set up to gather shared knowledge. In addition, the transpilation process is validated by a person, which are ready-made examples for the dataset in [dspy](https://github.com/stanfordnlp/dspy) and a way to obtain [metrics](https://github.com/stanfordnlp/dspy/blob/main/examples/tweets/tweet_metric.py) from the text in order to optimize prompts or fine-tune models with approximately the same codebase.

```
- Metrics of various plugins are needed, what will be the usability of the whole concept if the plugins do not work (click on a button in the browser)  
```

After transpiling the code, the HSL should describe the deployment process, and the playground (in the IDE or web) should also allow controlling production and be a Human in the Loop interface in the same paradigm as for the dev flow. Infrastructure, like processing, can be the main sources of cash flow here.

```
- I saw that you wrote about improving models through interaction with user feedback in the refinement.
```

It follows from all this that collaboration and the transfer of value between users and into the model as a result of DSL transpilation can be the main intellectual property in the paradigm of an open source project. We need to think about how this process can work many more times to be legally and technically protected while getting the maximum value and bringing the maximum benefit to users.

## Contact

For any questions or discussions please contact using [Twitter](https://twitter.com/minsightsai) or m@hslang.ai