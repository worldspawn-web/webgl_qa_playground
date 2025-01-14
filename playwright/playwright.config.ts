import { defineConfig, devices } from '@playwright/test';

export default defineConfig({
  testDir: './tests',
  fullyParallel: true,
  forbidOnly: !!process.env.CI,
  retries: process.env.CI ? 2 : 0,
  workers: process.env.CI ? 1 : undefined,
  reporter: 'html',
  use: {
    baseURL: 'https://yandex.ru',
    trace: 'on-first-retry',
    // Enable WebGL
    launchOptions: {
      args: [
        '--use-gl=egl',
        '--enable-webgl',
        '--no-sandbox',
        '--disable-setuid-sandbox',
        '--disable-gpu-sandbox',
        '--ignore-gpu-blocklist',
        '--enable-gpu-rasterization',
        '--enable-zero-copy',
      ],
    },
    viewport: { width: 1280, height: 720 },
    actionTimeout: 60000,
  },
  projects: [
    {
      name: 'chromium',
      use: { ...devices['Desktop Chrome'] },
    },
  ],
});
