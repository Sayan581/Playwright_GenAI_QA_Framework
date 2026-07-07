import pytest
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from utilities.screenshot_util import capture_screenshot


@pytest.fixture(scope="function")
def page(request):

    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=False,
            slow_mo=500
        )

        context = browser.new_context()

        page = context.new_page()

        yield page


        # Capture screenshot for EVERY test case
        capture_screenshot(
            page,
            request.node.name
        )

        context.close()
        browser.close()


@pytest.fixture(scope="function")
def login_page(page):

    return LoginPage(page)