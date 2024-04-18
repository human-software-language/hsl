const { execSync } = require('child_process');
const { context, build } = require('esbuild');

/**
 * @type {import('esbuild').Plugin}
 */
const esbuildProblemMatcherPlugin = {
  name: 'esbuild-problem-matcher',
  setup(build) {
    build.onStart(() => {
      console.log('[watch] build started');
      // Run `gulp copy-files` before build
    });
    build.onEnd((result) => {
      if (result.errors.length) {
        result.errors.forEach((error) =>
          console.error(
            `> ${error.location?.file}:${error.location?.line}:${error.location?.column}: error: ${error.text}`,
          ),
        );
      } else {
        console.log('[watch] build finished');
      }
    });
  },
};

/**
 * @type {import('esbuild').BuildOptions}
 */
const extensionConfig = {
  entryPoints: ['./src/extension.ts'],
  bundle: true,
  minify: true,
  sourcemap: true,
  outfile: './out/extension.js',
  target: 'es2020',
  format: 'cjs',
  external: ['vscode'],
  platform: 'node',
};


const defaultDocument = {
  readyState: 'ready',
};

const defaultWindow = {
  document: {
    currentScript: {
      dataset: {},
    },
  },
  location: {
    protocol: 'https:',
  },
  less: {
    onReady: false,
    async: false,
  },
};
async function main() {
  try {
    if (process.argv.includes('--watch')) {
      const extensionContext = await context({
        ...extensionConfig,
        plugins: [esbuildProblemMatcherPlugin],
      });
      await Promise.all([extensionContext.watch()]);
    } else {
      await Promise.all([build(extensionConfig)]);
    }
  } catch (error) {
    console.error(error);
  }
}

main();
