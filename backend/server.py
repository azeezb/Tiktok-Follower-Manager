from playwright.async_api import async_playwright
from TikTokApi import TikTokApi
import asyncio


async def fetch_ms_token():
    """Fetch ms_token dynamically using Playwright."""
    async with async_playwright() as p:
        # Launch the browser (ensure headless is False for debugging)
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        # Navigate to TikTok profile page (or any page where ms_token is generated)
        await page.goto('https://www.tiktok.com/@therock')
        await page.wait_for_timeout(3000)  # Wait for the page to load

        # Get ms_token dynamically from Playwright cookies
        cookies = await page.context.cookies()
        ms_token = None
        for cookie in cookies:
            if cookie['name'] == 'msToken':
                ms_token = cookie['value']
                break

        if not ms_token:
            print("ms_token could not be retrieved.")
            await browser.close()
            return None

        print(f"ms_token found: {ms_token}")
        await browser.close()
        return ms_token


async def user_profile_check(ms_token, username="therock"):
    print('we got this far')
    """Use TikTokApi to fetch user profile and follower count."""
    async with TikTokApi() as api:
        # Create session using the fetched ms_token
        await api.create_sessions(ms_tokens=[ms_token], num_sessions=1, sleep_after=3)
        
        # Get user info for the specified username
        # user = api.user(username)
        # user_data = await user.info()
        
        # print(user_data)



if __name__ == "__main__":
    # Fetch ms_token using Playwright
    ms_token = asyncio.run(fetch_ms_token())

    if ms_token:
        # Once ms_token is fetched, pass it to the TikTokApi user profile check function
        asyncio.run(user_profile_check(ms_token, username="therock"))
