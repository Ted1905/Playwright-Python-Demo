from playwright.sync_api import sync_playwright

def run_login_test():
    """
    Test Scenario:
    1. Navigate to 'saucedemo.com'
    2. Login with valid credentials
    3. Verify that the user is redirected to the inventory page
    """
    with sync_playwright() as p:
        # Launch browser in headed mode to visualize the test execution
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()

        print("--- Test Started: Navigating to SauceDemo ---")
        page.goto("https://www.saucedemo.com/")

        # Define selectors for better maintainability
        username_input = "#user-name"
        password_input = "#password"
        login_button = "#login-button"

        # Perform Login Action
        page.fill(username_input, "standard_user")
        page.fill(password_input, "secret_sauce")
        page.click(login_button)

        # Assertion / Validation
        # Check if the URL contains 'inventory' to confirm successful login
        try:
            assert "inventory" in page.url
            print("✅ SUCCESS: Login successful, redirected to Inventory page.")
        except AssertionError:
            print("❌ FAILED: Login failed or URL did not change.")
            # Take a screenshot for debugging purposes
            page.screenshot(path="login_error.png")

        # Cleanup
        browser.close()
        print("--- Test Finished ---")

if __name__ == "__main__":
    run_login_test()