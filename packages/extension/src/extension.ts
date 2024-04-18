import * as path from 'path';
import * as vscode from 'vscode';
import * as net from 'net';

import {
  LanguageClient,
  LanguageClientOptions,
  ServerOptions,
  StreamInfo,
  TransportKind,
} from 'vscode-languageclient/node';
import { renderHSLCommand } from './render';

import { outputChannel } from './output';

let client: LanguageClient;

class DAPDebugAdapterDescriptorFactory
  implements vscode.DebugAdapterDescriptorFactory
{
  createDebugAdapterDescriptor(
    session: vscode.DebugSession,
  ): vscode.ProviderResult<vscode.DebugAdapterDescriptor> {
    // Assuming your DAP server is running on localhost:5678
    const host = '127.0.0.1';
    const port = 5678;

    // Connect to the DAP server
    return new vscode.DebugAdapterServer(port, host);
  }
}

export function activate(context: vscode.ExtensionContext) {
  outputChannel.appendLine('Activating HSL extension...');
  // HSL debugger
  context.subscriptions.push(
    vscode.debug.registerDebugAdapterDescriptorFactory(
      'hsl',
      new DAPDebugAdapterDescriptorFactory(),
    ),
  );

  // Determine if the extension host was launched with the debug flag
  const isDebugMode = process.env.DEBUG_MODE === 'true';

  const serverOptions: ServerOptions = (): Promise<StreamInfo> => {
    const socket = net.connect({ port: 2087, host: '127.0.0.1' });

    const result: StreamInfo = {
      writer: socket,
      reader: socket,
    };

    return Promise.resolve(result);
  };

  const clientOptions: LanguageClientOptions = {
    documentSelector: [{ scheme: 'file', language: 'hsl' }],
    synchronize: {
      fileEvents: vscode.workspace.createFileSystemWatcher('**/*.hsl'),
    },
    // Add this line to enable tracing of the client-server communication
    traceOutputChannel: outputChannel,
    // Enable logging
    outputChannel: outputChannel,
    // Enable verbose logging
    initializationOptions: {
      logLevel: 'verbose',
    },
  };

  client = new LanguageClient(
    'hslLanguageServer',
    'Human Software Language Server',
    serverOptions,
    clientOptions,
  );

  client.start().then(
    () => {
      outputChannel.appendLine(
        'Client has successfully started and presumably connected to the server.',
      );
    },

    (error) => {
      outputChannel.appendLine(`Client failed to start: ${error}`);
    },
  );

  context.subscriptions.push(client);
  outputChannel.appendLine('HSL Language Server started.');

  // Register the command to render HSL
  const disposable = vscode.commands.registerCommand('hsl.renderHSL', () =>
    renderHSLCommand(context, client),
  );

  context.subscriptions.push(disposable);
}

export function deactivate(): Thenable<void> | undefined {
  return;
}
