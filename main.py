from playwright.sync_api import sync_playwright

def run_login_tests():
    """
    Test Suite:
    1. Scenario A: Negative Test (Invalid Credentials) -> Expect Error Message
    2. Scenario B: Positive Test (Valid Credentials) -> Expect Redirection to Inventory
    """
    with sync_playwright() as p:
        # Launch browser
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()

        print("--- 🚀 TEST SUITE STARTED ---")
        page.goto("https://www.saucedemo.com/")

        # Define Selectors
        username_input = "#user-name"
        password_input = "#password"
        login_button = "#login-button"
        error_message_locator = "h3[data-test='error']"

        # ---------------------------------------------------------
        # SCENARIO 1: NEGATIVE TEST (Invalid Login)
        # ---------------------------------------------------------
        print("\n--- 1. Running Negative Test (Invalid Password) ---")
        page.fill(username_input, "standard_user")
        page.fill(password_input, "wrong_pass_123") # Invalid password
        page.click(login_button)

        # Validation: Check if error message is visible
        if page.locator(error_message_locator).is_visible():
            print("✅ SUCCESS: Error message displayed for invalid credentials.")
        else:
            print("❌ FAILED: System did not show error message!")
            page.screenshot(path="negative_test_fail.png")

        # ---------------------------------------------------------
        # SCENARIO 2: POSITIVE TEST (Valid Login)
        # ---------------------------------------------------------
        print("\n--- 2. Running Positive Test (Valid Password) ---")
        
        # Note: Playwright's fill() automatically clears the input field before typing
        page.fill(username_input, "standard_user")
        page.fill(password_input, "secret_sauce") # Valid password
        page.click(login_button)

        # Validation: Check URL for success
        if "inventory" in page.url:
            print("✅ SUCCESS: Login successful, redirected to Inventory page.")
        else:
            print("❌ FAILED: Could not login with valid credentials.")
            page.screenshot(path="positive_test_fail.png")

        # Cleanup
        browser.close()
        print("\n--- 🏁 ALL TESTS FINISHED ---")

if __name__ == "__main__":
    run_login_tests()
