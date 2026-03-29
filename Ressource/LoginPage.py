from robot.libraries.BuiltIn import BuiltIn

class LoginPage:
    """This class represents the login page of a web application."""
    
    # Locators for the login page elements
    USERNAME_FIELD = "id=user-name"
    PASSWORD_FIELD = "id=password"
    LOGIN_BUTTON = "id=login-button"
    ERROR_MESSAGE = "css=[data-test='error']"
    
    def __init__(self):
        self.selenium = BuiltIn().get_library_instance('SeleniumLibrary')

    def enter_username(self, username):
        """Enters the username into the username field."""
        self.selenium.input_text(self.USERNAME_FIELD, username)
    
    def enter_password(self, password):
        """Enters the password into the password field."""
        self.selenium.input_text(self.PASSWORD_FIELD, password)
    
    def click_login_button(self):      
        """Clicks the login button."""
        self.selenium.click_button(self.LOGIN_BUTTON)
    
    def login(self, username, password):
        """Performs the login action."""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
    
    def get_error_message(self):
        """Retrieves the error message displayed."""
        return self.selenium.get_text(self.ERROR_MESSAGE)
    
    def input_invalid_credentials(self, username, password):
        """Input invalid credentials and click login"""
        self.selenium.input_text(self.USERNAME_FIELD, username)
        self.selenium.input_text(self.PASSWORD_FIELD, password)
        self.selenium.click_button(self.LOGIN_BUTTON)
    
    def verify_login_failed_message(self):
        """Verifies that error message is displayed."""
        error_msg = self.get_error_message()
        assert "Epic sadface" in error_msg, f"Expected error message, got: {error_msg}"