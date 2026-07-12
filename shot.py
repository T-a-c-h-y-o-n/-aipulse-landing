import os, asyncio
from playwright.async_api import async_playwright

SRC = "/home/ali/Belgeler/OpenClaude/AI_News_Dashboard - Personal/dashboard-v3.html"
OUT = "/home/ali/Belgeler/OpenClaude/aipulse marketing/assets"
os.makedirs(OUT, exist_ok=True)

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            executable_path="/snap/bin/chromium",
            args=["--no-sandbox","--disable-gpu"])
        page = await browser.new_page(viewport={"width":1366,"height":900}, device_scale_factor=2)
        await page.goto("file://"+SRC, wait_until="load")
        await page.wait_for_timeout(3500)
        await page.screenshot(path=f"{OUT}/dashboard-top.png")
        await browser.close()
    print("shot done")

asyncio.run(main())
