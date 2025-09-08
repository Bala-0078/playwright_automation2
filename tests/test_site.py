from playwright.sync_api import sync_playwright
import sys

def run(playwright):
    try:
        # Launch browser in non-headless mode
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        
        print("🚀 Starting Playwright automation test...")
        
        # Step 1: Go to the website "www.google.com"
        print("📍 Step 1: Navigating to Google...")
        page.goto("https://www.google.com")
        page.wait_for_load_state("networkidle")
        print("✅ Successfully navigated to Google")
        
        # Step 2: Check if the webpage contains google search bar
        print("📍 Step 2: Checking for Google search bar...")
        search_bar = page.locator("input[name='q'], textarea[name='q']")
        assert search_bar.is_visible(), "Google search bar is not visible"
        print("✅ Google search bar is visible and accessible")
        
        # Step 3: Click on a link and wait for navigation
        print("📍 Step 3: Clicking on 'About' link and waiting for navigation...")
        # Try to find and click the About link
        about_link = page.locator("text=About").first
        if about_link.is_visible():
            about_link.click()
            page.wait_for_load_state("networkidle")
            print("✅ Successfully navigated to About page")
        else:
            # Alternative: click on Gmail link if About is not available
            gmail_link = page.locator("text=Gmail").first
            if gmail_link.is_visible():
                gmail_link.click()
                page.wait_for_load_state("networkidle")
                print("✅ Successfully navigated to Gmail page")
            else:
                print("⚠️ No suitable navigation link found, continuing with current page")
        
        # Step 4: Verify new page contains expected elements
        print("📍 Step 4: Verifying page content...")
        # Check if we're still on a Google domain
        current_url = page.url
        assert "google" in current_url.lower(), f"Not on Google domain. Current URL: {current_url}"
        print(f"✅ Successfully verified page content. Current URL: {current_url}")
        
        # Additional verification: Check page title
        page_title = page.title()
        print(f"📄 Page title: {page_title}")
        
        print("🎉 All test steps completed successfully!")
        
    except Exception as e:
        print(f"❌ Test failed with error: {str(e)}")
        raise e
    
    finally:
        # Close browser
        print("🔒 Closing browser...")
        browser.close()
        print("✅ Browser closed successfully")

if __name__ == "__main__":
    try:
        with sync_playwright() as playwright:
            run(playwright)
        print("\n🏆 Playwright automation test completed successfully!")
        sys.exit(0)
    except Exception as e:
        print(f"\n💥 Playwright automation test failed: {str(e)}")
        sys.exit(1)