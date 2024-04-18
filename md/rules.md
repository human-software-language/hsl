# Human Software Language (HSL) Rules

## Introduction

Human Software Language (HSL) is a markdown-based language that enables both technical and non-technical users to build complex software systems. It leverages large language models (LLMs) to translate human instructions into executable code, abstracting away low-level coding details.

## File Structure

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

### Component Definition

```
# Component Name

## Description

Brief description of the component's purpose and functionality.

## Context (optional)

Additional context or scenario in which the component is used.

## Secrets (optional)

- `secretVariable: type` - Description of the secret variable (e.g., API keys, passwords).
- ...

## Steps

1. Describe the component's logic as a series of steps.
2. Use indentation to represent control structures (conditionals, loops).
3. Reference other components using backticks, e.g., `Another Component`.
4. Inline data transformations can be performed within the steps.
```

### Variables

- Variables are automatically inferred and constructed by LLMs based on the program context and component interactions.
- Use backticks to reference variables within the component steps, e.g., `variableName`.
- Variables can be referenced across multiple files, but must be unique within the program.
- Variable types and scopes are inferred automatically based on the surrounding context.

### Control Structures

- Use indentation to represent control structures like conditionals and loops.
- Express conditionals and loops using natural language, e.g., "If condition is true, do this. Otherwise, do that."
- Advanced natural language processing techniques can be employed to handle complex control flow scenarios.

### Component Composition

- Components can be dynamically composed and nested within other components.
- To compose a new component from existing ones, define a new component and reference the other components within its Steps section.

## Execution Environments

HSL supports modular and extensible execution environments:

- `Browser`: For web applications and websites.
- `OS`: For operating system interactions and command-line utilities.
- `Supabase`: For Supabase platform (databases, storage, user management).
- `Frontend`: For frontend components (React, Vue, etc.).
- `Mobile`: For mobile platforms (iOS, Android).
- `Custom`: For custom platforms and frameworks, defined by the user.

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
