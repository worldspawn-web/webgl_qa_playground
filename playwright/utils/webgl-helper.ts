import { Page, Frame, FrameLocator } from '@playwright/test';

interface WebGLSupportInfo {
  hasWebGL: boolean;
  extensions: string[] | null;
}

export class WebGLHelper {
  constructor(private page: Page) {}

  async isWebGLSupported(): Promise<WebGLSupportInfo> {
    return await this.page.evaluate(() => {
      const canvas = document.createElement('canvas');
      const gl = (canvas.getContext('webgl') ||
        canvas.getContext('experimental-webgl')) as WebGLRenderingContext | null;

      if (!gl) {
        return {
          hasWebGL: false,
          extensions: null,
        };
      }

      return {
        hasWebGL: true,
        extensions: gl.getSupportedExtensions(),
      };
    });
  }

  async waitForUnityLoaded(): Promise<void> {
    await this.page.waitForFunction(
      () => {
        const unityInstance = (window as any).unityInstance;
        return unityInstance && unityInstance.Module && unityInstance.Module.IsRunning;
      },
      { timeout: 30000 }
    );
  }

  async waitForUnityCanvas(): Promise<void> {
    await this.page.waitForSelector('#unity-canvas', {
      state: 'visible',
      timeout: 30000,
    });

    const hasWebGL = await this.page.evaluate(() => {
      const canvas = document.querySelector('#unity-canvas') as HTMLCanvasElement;
      if (!canvas) return false;

      const gl = (canvas.getContext('webgl') ||
        canvas.getContext('experimental-webgl')) as WebGLRenderingContext | null;
      return !!gl;
    });

    if (!hasWebGL) {
      throw new Error('WebGL context not available on Unity canvas');
    }
  }

  async waitForWebGLContext(frameSelector: string): Promise<void> {
    const frame = this.page.frameLocator(frameSelector);

    // Wait for the frame to be available
    await frame.locator('#unityContainerCanvas').waitFor({
      state: 'visible',
      timeout: 30000,
    });

    // Verify WebGL context in the frame
    const hasWebGL = await this.page.evaluate((selector) => {
      const frameElement = document.querySelector(selector) as HTMLIFrameElement;
      if (!frameElement?.contentWindow) return false;

      const canvas = frameElement.contentWindow.document.querySelector('#unityContainerCanvas') as HTMLCanvasElement;
      if (!canvas) return false;

      const gl = (canvas.getContext('webgl') ||
        canvas.getContext('experimental-webgl')) as WebGLRenderingContext | null;
      return !!gl;
    }, frameSelector);

    if (!hasWebGL) {
      throw new Error('WebGL context not available in frame');
    }
  }
}
