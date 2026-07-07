import pytest
from pages.login_page import LoginPage


@pytest.fixture(scope="function")
def login_page(page: Page) -> LoginPage:
    """Fixture to create and return a LoginPage instance"""
    return LoginPage(page)


class TestLoginValidation:
    """Test suite for SauceDemo login page validation"""

    def test_login_page_navigation(self, login_page: LoginPage):
        """
        Test Case 1: Verify login page can be navigated to
        
        Expected:
            - Page loads successfully at the SauceDemo URL
        """
        login_page.navigate()
        assert "saucedemo.com" in login_page.page.url
        assert login_page.page.title() != ""

    def test_successful_login_with_valid_credentials(self, login_page: LoginPage):
        """
        Test Case 2: Verify successful login with valid credentials
        
        Expected:
            - User successfully logs in with valid username and password
            - Page redirects to inventory/products page
        """
        login_page.navigate()
        login_page.login("standard_user", "secret_sauce")
        
        # Wait for redirect to inventory page
        login_page.page.wait_for_url("**/inventory.html")
        assert "/inventory.html" in login_page.page.url

    def test_login_with_locked_user(self, login_page: LoginPage):
        """
        Test Case 3: Verify error message for locked user
        
        Expected:
            - Error message is displayed when trying to login with locked user
        """
        login_page.navigate()
        login_page.login("locked_out_user", "secret_sauce")
        
        # Verify error message is displayed
        assert login_page.is_error_displayed()
        error_msg = login_page.get_error_message()
        assert "locked out" in error_msg.lower()

    def test_login_with_invalid_password(self, login_page: LoginPage):
        """
        Test Case 4: Verify error message for invalid password
        
        Expected:
            - Error message is displayed when password is incorrect
        """
        login_page.navigate()
        login_page.login("standard_user", "wrong_password")
        
        # Verify error message is displayed
        assert login_page.is_error_displayed()
        error_msg = login_page.get_error_message()
        assert "username and password do not match" in error_msg.lower()

    def test_login_with_invalid_username(self, login_page: LoginPage):
        """
        Test Case 5: Verify error message for invalid username
        
        Expected:
            - Error message is displayed when username does not exist
        """
        login_page.navigate()
        login_page.login("invalid_user", "secret_sauce")
        
        # Verify error message is displayed
        assert login_page.is_error_displayed()
        error_msg = login_page.get_error_message()
        assert "username and password do not match" in error_msg.lower()

    def test_login_with_empty_username(self, login_page: LoginPage):
        """
        Test Case 6: Verify error message when username is empty
        
        Expected:
            - Error message is displayed when username field is empty
        """
        login_page.navigate()
        login_page.enter_password("secret_sauce")
        login_page.click_login()
        
        # Verify error message is displayed
        assert login_page.is_error_displayed()
        error_msg = login_page.get_error_message()
        assert "username" in error_msg.lower()

    def test_login_with_empty_password(self, login_page: LoginPage):
        """
        Test Case 7: Verify error message when password is empty
        
        Expected:
            - Error message is displayed when password field is empty
        """
        login_page.navigate()
        login_page.enter_username("standard_user")
        login_page.click_login()
        
        # Verify error message is displayed
        assert login_page.is_error_displayed()
        error_msg = login_page.get_error_message()
        assert "password" in error_msg.lower()

    def test_login_with_both_fields_empty(self, login_page: LoginPage):
        """
        Test Case 8: Verify error message when both fields are empty
        
        Expected:
            - Error message is displayed when both username and password are empty
        """
        login_page.navigate()
        login_page.click_login()
        
        # Verify error message is displayed
        assert login_page.is_error_displayed()
        error_msg = login_page.get_error_message()
        assert "username" in error_msg.lower()

    def test_enter_username_separately(self, login_page: LoginPage):
        """
        Test Case 9: Verify username can be entered separately
        
        Expected:
            - Username input field accepts and retains user input
        """
        login_page.navigate()
        username = "standard_user"
        login_page.enter_username(username)
        
        # Verify username is entered in the field
        username_value = login_page.page.input_value("input[data-test='username']")
        assert username_value == username

    def test_enter_password_separately(self, login_page: LoginPage):
        """
        Test Case 10: Verify password can be entered separately
        
        Expected:
            - Password input field accepts and retains user input
        """
        login_page.navigate()
        password = "secret_sauce"
        login_page.enter_password(password)
        
        # Verify password is entered in the field
        password_value = login_page.page.input_value("input[data-test='password']")
        assert password_value == password

    def test_login_with_performance_glitch_user(self, login_page: LoginPage):
        """
        Test Case 11: Verify login with performance glitch user
        
        Expected:
            - User successfully logs in with performance_glitch_user
            - Page may have delayed loading but user redirects to inventory
        """
        login_page.navigate()
        login_page.login("performance_glitch_user", "secret_sauce")
        
        # Wait for redirect to inventory page with longer timeout
        login_page.page.wait_for_url("**/inventory.html", timeout=30000)
        assert "/inventory.html" in login_page.page.url

    def test_login_with_problem_user(self, login_page: LoginPage):
        """
        Test Case 12: Verify login with problem user
        
        Expected:
            - User successfully logs in with problem_user
            - Page redirects to inventory
        """
        login_page.navigate()
        login_page.login("problem_user", "secret_sauce")
        
        # Wait for redirect to inventory page
        login_page.page.wait_for_url("**/inventory.html")
        assert "/inventory.html" in login_page.page.url


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])
