import { test, expect } from '@playwright/test';
import { WebGLHelper } from '../utils/webgl-helper';

test.describe('Hell Park: Merge Festival Game Tests', () => {
  let webglHelper: WebGLHelper;

  test.beforeEach(async ({ page }) => {
    webglHelper = new WebGLHelper(page);

    // Check WebGL support
    const webGLSupport = await webglHelper.isWebGLSupported();
    expect(webGLSupport.hasWebGL).toBeTruthy();

    // Navigate to the game - Hell Merge
    await page.goto('/games/app/359515?lang=ru');
  });

  test('should load game and verify WebGL content', async ({ page }) => {
    // Verify and click play button
    await expect(page.getByRole('button', { name: 'Играть' })).toBeVisible();
    await page.getByRole('button', { name: 'Играть' }).click();

    // Wait for modal and verify
    await expect(page.locator('.play-modal__inner')).toBeVisible();
    await page.waitForTimeout(5000);

    // Click fullscreen button
    await page.getByTestId('YandexFullscreenRender-Button').click();

    //

    await expect(
      page
        .locator('iframe[name="\\31 736792013377304-14470665605180390922-nrf233k6ba3y5k2k-BAL"]')
        .contentFrame()
        .locator('#unityContainerCanvas')
    ).toBeVisible();

    // // Wait for WebGL context in the game frame
    // const frameSelector = 'iframe[name*="jpbmxilbmqp7hk24-BAL"]';
    // await webglHelper.waitForWebGLContext(frameSelector);
  });
});
