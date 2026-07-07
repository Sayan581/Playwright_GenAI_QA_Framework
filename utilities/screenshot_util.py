from datetime import datetime
import os


def capture_screenshot(page, test_name):

    folder = "screenshots"

    if not os.path.exists(folder):
        os.makedirs(folder)

    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    path = (
        f"{folder}/"
        f"{test_name}_{timestamp}.png"
    )

    page.screenshot(
        path=path,
        full_page=True
    )

    return path