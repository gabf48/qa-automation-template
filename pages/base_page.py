"""
Base Page class with shared functionality.
"""

import os
from datetime import datetime


class BasePage:
    """Base class for all page objects."""

    def __init__(self, page):
        self.page = page

    def navigate(self, url: str):
        """Navigate to a specific URL."""
        self.page.goto(url)

    def get_title(self):
        """Return page title."""
        return self.page.title()

    def take_screenshot(self, test_name: str):
        """
        Takes a screenshot only when explicitly called.
        Saves it inside /screenshots/<test_name>/
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        folder_path = os.path.join("screenshots", test_name)

        os.makedirs(folder_path, exist_ok=True)

        file_path = os.path.join(folder_path, f"{timestamp}.png")
        self.page.screenshot(path=file_path)

        return file_path