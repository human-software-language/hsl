import * as vscode from 'vscode';
import { exec } from 'child_process';

// Consolidate the use of exec to minimize shell command overhead
async function executeShellCommand(
  command: string,
): Promise<{ success: boolean; stdout: string; stderr: string }> {
  return new Promise((resolve) => {
    exec(command, (error, stdout, stderr) => {
      resolve({ success: !error, stdout, stderr });
    });
  });
}

// Use VS Code API more efficiently and minimize shell executions
async function checkAndInstallDependencies(
  outputChannel: vscode.OutputChannel,
) {
  const pythonExtension = vscode.extensions.getExtension('ms-python.python');
  if (!pythonExtension) {
    vscode.window.showWarningMessage(
      'Python extension is not installed. Please install it to use this feature.',
    );
    return;
  }

  await pythonExtension.activate();
  const pythonPath = pythonExtension.exports.settings.getExecutionDetails
    ? pythonExtension.exports.settings.getExecutionDetails().execCommand[0]
    : await vscode.commands.executeCommand<string>('python.interpreterPath');

  if (!pythonPath) {
    vscode.window.showErrorMessage(
      'Python interpreter path could not be determined.',
    );
    return;
  }

  // Optimizing by checking all dependencies at once (if possible) and then installing all missing in one go
  const dependencies = ['python-lsp-server', 'lark'];
  const checkCmd = `${pythonPath} -m pip list`;

  try {
    const { success, stdout } = await executeShellCommand(checkCmd);
    if (!success) {
      outputChannel.appendLine('Failed to list installed packages.');
      return;
    }

    const missingDeps = dependencies.filter((dep) => !stdout.includes(dep));
    if (missingDeps.length > 0) {
      const installCmd = `${pythonPath} -m pip install ${missingDeps.join(' ')}`;
      outputChannel.appendLine(
        `Installing missing dependencies: ${missingDeps.join(', ')}`,
      );
      const { success: installSuccess } = await executeShellCommand(installCmd);
      if (installSuccess) {
        vscode.window.showInformationMessage(
          `Successfully installed missing dependencies.`,
        );
      } else {
        vscode.window.showErrorMessage(
          `Failed to install one or more dependencies. Please install them manually.`,
        );
      }
    } else {
      outputChannel.appendLine(`All dependencies are already installed.`);
    }
  } catch (error) {
    vscode.window.showErrorMessage(`An error occurred: ${error}`);
  }
}

// Exporting the more optimized function
export { checkAndInstallDependencies };
