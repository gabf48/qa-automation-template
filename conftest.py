"""
Global pytest configuration and fixtures.
"""

import os
import pytest
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright


# Load environment variables
load_dotenv()


# ===============================
# CONFIGURATION FROM .ENV
# ===============================

BROWSER = os.getenv("BROWSER", "chromium")
HEADLESS = os.getenv("HEADLESS", "true").lower() == "true"


# ===============================
# PLAYWRIGHT FIXTURES
# ===============================

@pytest.fixture(scope="session")
def playwright_instance():
    """Starts Playwright instance."""
    with sync_playwright() as playwright:
        yield playwright


@pytest.fixture(scope="session")
def browser(playwright_instance):
    """Launch browser based on environment configuration."""
    browser_type = getattr(playwright_instance, BROWSER)

    browser = browser_type.launch(
        headless=HEADLESS
    )

    yield browser
    browser.close()


@pytest.fixture(scope="function")
def context(browser):
    """Creates new browser context for each test."""
    context = browser.new_context()
    yield context
    context.close()


@pytest.fixture(scope="function")
def page(context):
    """Creates new page for each test."""
    page = context.new_page()
    yield page
    page.close()