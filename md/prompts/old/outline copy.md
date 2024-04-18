1. Think step by step like Ilya Sutskever and Andrei Karpatiy united together, After that think like creators of Python, Javascript, Flutter and Supabase and learn from their writting style and knowledge of them.
2. After Write outline for that task in simple language inside codeblock. I want to build large detailed document that is starting point to develop HSL. Also we should publish that document in the web to find cofounders to build my Human software languageDSL.

Write developer workflow. Write more poinst for each outline item write subitems.

## Description

HSL will transpile human language into source code, validate, test and execute it. Also HSL code itself can be modified based on the execution. As a result of HSL we can receive source code executed in os or based on react/supabase/browser/flutter that can be self hosted or deployed to clouds. So it use modern technologies and can be used by experienced technical users to speedup iteration and development time and for non technical userslike product, projects, designers, entrepreneurs, etc.. to build very complex software. The idea is versatility and the ability to describe any case, translating it into source code for popular and reliable technologies.

## Platforms

For each platform we have default components, but any of them can be extended or changed to different frameworks/technologies by writing custom interpretators/validators/executors.

- Browser - we can execute actions at any website. We use system browser started with debugger protocol and execute custom javascript code to mark up the DOM and add persistent attributes to elements important for interaction.
- OS - we can generate commands for any OS.
- Backend - There us defailt supabase component, we can build database with ACL, storage, user control, etc...
- Frontend - By default it is next.js/typescript/supabase, we can generate react components and integrate them into that template.
- Mobile - Flutter


HSL DSL Example:
```markdown
# OS: Analyze Results and Send Them by Email

This component automates the process of analyzing search results from Google and sending a summary via email.

## Input

- `request: text` - The query to search on Google.
- `email: text` - The email where send report to.

## Output

- `emailConfirmation: text` - Confirmation that the email with the search results summary has been sent successfully.

## Steps

1. Use the `Browser: Google search` component to search Google with `request`

2. Use the `OS: OpenAI Analyze Table` component to analyze the `searchResults`. Specify the `analysisType` as "Summary" and use the `searchResults` as `dataTable`.

3. Prepare the email content based on the `analysisResults`. The email content should include key insights, top results, or any relevant summary information obtained from the analysis.

4. Use the `Browser: Send Gmail Message` component to send the analysis.

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
