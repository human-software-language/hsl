# Program: Analyze Results and Send Them by Email

This component automates the process of analyzing search results from Google and sending a summary via email.

## Google analysis

1. Prompt user for `[searchQuery]` and `[contentType]`.
2. Search the web using the `Browser: Google Search`.
3. Analyze search results using the `OS: OpenAI Analyze Table`.
4. Render analysis results using the `Frontend: Render Google results`.
5. Prompt user for `[recipientEmail]`.
6. Send analysis results via email using the `Browser: Send Gmail Message`.
7. Render analysis results using the `Frontend: Render Gmail report`.

## Show weather

1. Search weather using `Browser: Google weather`.
2. Prompt user with result
