from playwright.sync_api import Page, expect


class LoginPage:
    """
    Page Object Model for SauceDemo Login Page
    Encapsulates all interactions with the login page elements
    """

    # URL of the login page
    BASE_URL = "https://www.saucedemo.com/"

    # Page element locators
    USERNAME_INPUT = "input[data-test='username']"
    PASSWORD_INPUT = "input[data-test='password']"
    LOGIN_BUTTON = "input[data-test='login-button']"
    LOGIN_ERROR = "[data-test='error']"

    def __init__(self, page: Page):
        """
        Initialize the LoginPage with a Playwright Page object
        
        Args:
            page (Page): Playwright page object
        """
        self.page = page

    def navigate(self):
        """Navigate to the SauceDemo login page"""
        self.page.goto(self.BASE_URL)

    def enter_username(self, username: str):
        """
        Enter username in the username field
        
        Args:
            username (str): The username to enter
        """
        self.page.fill(self.USERNAME_INPUT, username)

    def enter_password(self, password: str):
        """
        Enter password in the password field
        
        Args:
            password (str): The password to enter
        """
        self.page.fill(self.PASSWORD_INPUT, password)

    def click_login(self):
        """Click the login button"""
        self.page.click(self.LOGIN_BUTTON)

    def login(self, username: str, password: str):
        """
        Complete login flow with username and password
        
        Args:
            username (str): The username to login with
            password (str): The password to login with
        """
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def is_error_displayed(self) -> bool:
        """
        Check if error message is displayed on login page
        
        Returns:
            bool: True if error is displayed, False otherwise
        """
        return self.page.is_visible(self.LOGIN_ERROR)

    def get_error_message(self) -> str:
        """
        Get the error message text displayed on login page
        
        Returns:
            str: The error message text
        """
        return self.page.text_content(self.LOGIN_ERROR)
