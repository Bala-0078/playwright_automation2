from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch(headless=True)  # headless=False opens real browser
    context = browser.new_context()
    page = context.new_page()

    # Step 1: Go to the website
    page.goto("https://example.com")

    # Step 2: Check if the title contains "Example Domain"
    assert "Example Domain" in page.title()
    print("✅ Page title is correct")

    # Step 3: Click on the link and wait for navigation
    page.click("text=More information")
    page.wait_for_load_state("networkidle")

    # Step 4: Verify new page contains expected text
    assert "IANA" in page.inner_text("body")
    print("✅ Navigation successful and text found")

    # Close browser
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
