from playwright.sync_api import sync_playwright

def run(playwright):
    # Run in headless mode since GitHub Actions has no GUI
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()

    # Step 1: Go to the website
    page.goto("https://example.com")

    # Step 2: Check title
    assert "Example Domain" in page.title()
    print("✅ Page title is correct")

    # 📸 Take a screenshot of homepage
    page.screenshot(path="homepage.png")

    # Step 3: Click link and wait for navigation
    page.click("text=More information")
    page.wait_for_load_state("networkidle")

    # Step 4: Verify text on new page
    assert "IANA" in page.inner_text("body")
    print("✅ Navigation successful")

    # 📸 Take a screenshot of second page
    page.screenshot(path="iana.png")

    browser.close()

with sync_playwright() as playwright:
    run(playwright)
