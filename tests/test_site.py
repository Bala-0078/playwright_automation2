from playwright.sync_api import sync_playwright
import sys

def run(playwright):
    try:
        # Launch browser in non-headless mode for debugging
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        
        print("🚀 Starting Playwright test automation...")
        
        # Step 1: Go to the website "www.google.com"
        print("📍 Step 1: Navigating to Google.com")
        page.goto("https://www.google.com")
        page.wait_for_load_state("networkidle")
        print("✅ Successfully navigated to Google.com")
        
        # Step 2: Check if the webpage contains google search bar
        print("📍 Step 2: Checking for Google search bar")
        search_bar = page.locator("input[name='q'], textarea[name='q']")
        assert search_bar.is_visible(), "Google search bar is not visible"
        print("✅ Google search bar is visible and accessible")
        
        # Step 3: Interact with search bar and perform a search
        print("📍 Step 3: Performing a test search")
        search_bar.fill("Playwright automation testing")
        search_bar.press("Enter")
        page.wait_for_load_state("networkidle")
        print("✅ Search performed successfully")
        
        # Step 4: Verify search results page contains expected elements
        print("📍 Step 4: Verifying search results page")
        # Check for search results
        results = page.locator("#search")
        assert results.is_visible(), "Search results are not visible"
        
        # Verify search bar is still present on results page
        search_bar_results = page.locator("input[name='q'], textarea[name='q']")
        assert search_bar_results.is_visible(), "Search bar not visible on results page"
        print("✅ Search results page verified successfully")
        
        # Step 5: Navigate back to homepage
        print("📍 Step 5: Navigating back to homepage")
        page.goto("https://www.google.com")
        page.wait_for_load_state("networkidle")
        
        # Verify we're back on the homepage
        homepage_search_bar = page.locator("input[name='q'], textarea[name='q']")
        assert homepage_search_bar.is_visible(), "Homepage search bar not visible"
        print("✅ Successfully returned to homepage")
        
        print("🎉 All test steps completed successfully!")
        
    except Exception as e:
        print(f"❌ Test failed with error: {str(e)}")
        sys.exit(1)
    
    finally:
        # Close browser
        print("🔒 Closing browser...")
        browser.close()
        print("✅ Browser closed successfully")

if __name__ == "__main__":
    with sync_playwright() as playwright:
        run(playwright)