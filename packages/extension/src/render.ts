import path from 'path';
import * as vscode from 'vscode';
import { getNonce } from './utils/getNonce';
import { getUri } from './utils/getUri';
import { outputChannel } from './output';
import axios from 'axios';

import {
  LanguageClient,
  LanguageClientOptions,
  ServerOptions,
  StreamInfo,
  TransportKind,
} from 'vscode-languageclient/node';

export async function renderHSLCommand(
  context: vscode.ExtensionContext,
  languageClient: LanguageClient,
) {
  const activeEditor = vscode.window.activeTextEditor;
  if (activeEditor && activeEditor.document.languageId === 'hsl') {
    const hslContent = activeEditor.document.getText();
    try {
      const webviewPanel = vscode.window.createWebviewPanel(
        'hslPreview',
        'HSL Preview',
        vscode.ViewColumn.Beside,
        {
          enableScripts: true,
          localResourceRoots: [
            vscode.Uri.joinPath(context.extensionUri),
            vscode.Uri.joinPath(context.extensionUri, '..', 'playground'),
          ],
        },
      );

      const nonce = getNonce();

      // Convert the localhost URL to a webview URI
      const solaraAppUri = webviewPanel.webview.asWebviewUri(
        vscode.Uri.parse('http://localhost:8501'),
      );

      const csp = [
        `default-src 'none';`,
        `frame-src ${solaraAppUri.toString()};`,
        `script-src 'nonce-${nonce}';`,
        `style-src ${webviewPanel.webview.cspSource};`,
        `font-src ${webviewPanel.webview.cspSource};`,
      ];

      webviewPanel.webview.html = `<!DOCTYPE html>
        <html lang="en">
        <head>
          <meta charset="UTF-8" />
          <meta http-equiv="Content-Security-Policy" content="${csp.join('; ')}">
          <meta name="viewport" content="width=device-width, initial-scale=1.0" />
          <title>HSL Preview</title>
          <style>
            html, body, iframe {
              width: 100% !important;
              height: 100% !important;
              margin: 0 !important;
              padding: 0 !important;
              overflow: hidden !important;
              position: absolute !important;
              top: 0 !important;
              left: 0 !important;
              border: none !important;
            }
          </style>
        </head>
        <body>
          <iframe id="hslPreviewIframe" src="${solaraAppUri}" allowfullscreen></iframe>
          <script nonce="${nonce}">
            const vscode = acquireVsCodeApi();

            document.addEventListener('DOMContentLoaded', (event) => {
              const iframeElement = document.querySelector('#hslPreviewIframe');

              // Set styles directly to the iframe
              iframeElement.style.width = "100%";
              iframeElement.style.height = "100%";
              iframeElement.style.margin = "0";
              iframeElement.style.padding = "0";
              iframeElement.style.overflow = "hidden";
              iframeElement.style.position = "absolute";
              iframeElement.style.top = "0";
              iframeElement.style.left = "0";
              iframeElement.style.border = "none";
              
              // Listen for messages coming from any source
              window.addEventListener('message', event => {
                console.log(event);
                // Check if the message came from the iframe
                if (event.origin === "${solaraAppUri}") {
                  // Message is from iframe, forward it to VSCode
                  vscode.postMessage(event.data);
                } else {
                  // Forward it to the iframe
                  iframeElement.contentWindow.postMessage(event.data, "${solaraAppUri}");
                }
              }, false);
            });
          </script>
        </body>
        </html>      
      `;

      const endpointUrl = 'http://localhost:8501/update_state';

      vscode.workspace.onDidChangeTextDocument(
        async (event) => {
          if (event.document === activeEditor.document) {
            const cursorPosition = activeEditor.selection.start;
            const lineText = event.document.lineAt(cursorPosition.line).text;
            const vscodeState = {
              file_path: event.document.uri.path,
              cursor_location: {
                line: cursorPosition.line,
                column: cursorPosition.character,
              },
              line_text: lineText,
            };

            try {
              // Send the POST request using axios
              const response = await axios.post(endpointUrl, vscodeState, {
                headers: {
                  'Content-Type': 'application/json',
                },
              });
              console.log('Response from the server:', response.data);
            } catch (error: unknown) {
              // Assume error is of type any to access common properties like message
              const message =
                (error as any).message || 'An unknown error occurred';
              console.error('Error making the request:', error);
              vscode.window.showErrorMessage(`Error sending data: ${message}`);
            }
          }
        },
        null,
        context.subscriptions,
      );

      webviewPanel.webview.onDidReceiveMessage(
        async (message) => {
          try {
            outputChannel.appendLine('Extension receive message: ' + message);
            const startTime = Date.now();

            const endTime = Date.now();
            const timing = endTime - startTime;

            interface WebviewResponse {
              command: string;
              response: string;
            }
          } catch (error) {
            console.error('Error handling webview message:', error);
            vscode.window.showErrorMessage(
              'An error occurred while handling the message.',
            );
          }
        },
        undefined,
        context.subscriptions,
      );
    } catch (error: any) {
      console.error('Error rendering HSL:', error);
      vscode.window.showErrorMessage(`Error rendering HSL: ${error.message}`);
    }
  } else {
    const message =
      'Rendering is only functional for files with a .hsl extension.';
    outputChannel.appendLine(message);
    vscode.window.showErrorMessage(message);
  }
}
