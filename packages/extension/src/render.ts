import path from 'path';
import * as vscode from 'vscode';
import { getNonce } from './utils/getNonce';
import { getUri } from './utils/getUri';
import { outputChannel } from './output';

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
      const streamlitAppUri = webviewPanel.webview.asWebviewUri(
        vscode.Uri.parse('http://localhost:8501'),
      );

      const csp = [
        `default-src 'none';`,
        `frame-src ${streamlitAppUri.toString()};`,
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
          <iframe id="hslPreviewIframe" src="${streamlitAppUri}" allowfullscreen></iframe>
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
                if (event.origin === "${streamlitAppUri}") {
                  // Message is from iframe, forward it to VSCode
                  vscode.postMessage(event.data);
                } else {
                  // Assuming any other message is from VSCode
                  // Forward it to the iframe
                  iframeElement.contentWindow.postMessage(event.data, "${streamlitAppUri}");
                }
              }, false);
            });
          </script>
        </body>
        </html>      
      `;

      // Listen for selection changes in the active text editor and send to streamlit
      vscode.window.onDidChangeTextEditorSelection(
        (event) => {
          webviewPanel.webview.postMessage(event);
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
