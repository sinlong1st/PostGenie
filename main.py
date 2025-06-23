import dotenv
import os
from seleniumbase import SB
from dotenv import load_dotenv


# Load credentials from .env
load_dotenv()
USERNAME = os.getenv("SOCIAL_USERNAME")
PASSWORD = os.getenv("SOCIAL_PWD")
SOCIAL_URL = os.getenv("SOCIAL_URL")
# todo: Add error handling for missing environment variables
# todo: Add Utils for boot up env, encryption
# todo: Learn and research target website to avoid detection
# todo: stealth mode, headless mode, etc.

def main():
    with SB(uc=True, headed=True) as sb:
        sb.open(SOCIAL_URL)

        # Enter email/phone
        sb.type('input[name="email"]', USERNAME)

        # Enter password
        sb.type('input[name="pass"]', PASSWORD)

        # Click login
        sb.click('button[name="login"]')

        # Optional: wait to confirm login success
        sb.sleep(35)

        # Optional: screenshot after login
        sb.save_screenshot("fb_logged_in.png")

if __name__ == "__main__":
    main()
    print("Login script executed successfully.")