# Humans software language (DSL)

Build AI Agents, Backend, Frontent rapidly in human natively understandable language.

We have two examples of AI Agents functions, brainstorm how program outline can look like.

```hsl
# Browser: Google search

This process streamlines the task of retrieving information from the web based on a user's query, covering various content types like text, images, news, and videos. It is designed to efficiently collect data or references pertinent to a specific topic.

## Input

- `searchQuery: text` - The user-provided query to search for. This is the main input from the user.
- `contentType: text` - Default is "General". Specifies the content type to be searched (options like "General", "Images", "News", "Videos").
- `count: number` - Default is 10. The quantity of search results the user requests.

## Output

- `searchResults: table` - A compilation of search results, detailing titles and links and content types

## Steps

1. Open the search page at `https://google.com`.
2. In the search box `[search box]`, enter your query `(searchQuery)`.
3. Initiate the search by clicking `[search button]`.
4. If `(contentType)` is not "General":
   - Look for `[contentType tab/button]`. If it exists, select it to filter results accordingly.
   - Otherwise, note that the specific content type is not available.
5. Set a variable `resultsCollected` to 0 for tracking the number of results.
6. Collect results until reaching `(count)`:
   - Find `[titles]` and `[links]` in `[results area]` and add them to `searchResults`.
   - Update `resultsCollected` with the number of items found.
   - If `resultsCollected` is less than `(count)`, proceed to the next page by `[scroll]` for more results.
7. Finalize the search by organizing all collected information into `searchResults`.
```

```hsl
# Browser: Send Gmail Message

This process automates the task of composing and sending an email message through Gmail. It is designed to simplify communication by allowing users to quickly send emails to one or more recipients, with optional attachments, subject lines, and message bodies.

## Context

Activated when a user needs to send an email via Gmail, whether for personal or professional communication. This includes sending updates, files, or any information to contacts efficiently.

## Input

- `recipientEmail: text` - The email address of the recipient. Multiple email addresses can be separated by commas for multiple recipients.
- `subject: text` - The subject line of the email. This is optional; if not provided, the email will have no subject.
- `messageBody: text` - The main content of the email. This is optional; if not provided, the email will be sent with an empty body.
- `attachments: files` - Files locations to be attached to the email. This is optional; if not provided, the email will be sent without attachments.

## Output

- `emailSentConfirmation: table` - Confirmation that the email has been sent successfully, including the time of sending.


## Steps

1. Navigate to `https://mail.google.com/` and ensure you are logged in to your Gmail account.
2. Click on the `[compose button]` to open a new message window.
3. In the `To` field `[to field]`, enter the recipient's email address `(recipientEmail)`. For multiple recipients, separate each email address with a comma.
4. If `(subject)` is provided:
   - Find the `Subject` field `[subject field]` and enter `(subject)`.
5. If `(messageBody)` is provided:
   - Locate the `Message body` area `[message body area]` and enter `(messageBody)`.
6. If `(attachments)` are provided:
   - Click on the `[attach files button]` and select the files from your computer to attach to the email.
7. Once all information is entered, click the `[send button]` to send the email.
8. Confirm that the email has been sent by checking for a "Message sent" notification `[message sent notification]` and log the confirmation and time of sending as `(emailSentConfirmation)`.

```
