# crawl4AI

Installation: See https://docs.crawl4ai.com/core/installation/

## Local installation

### Virtual environment using uv
- Install: curl -LsSf https://astral.sh/uv/install.sh | sh
- Create a virtual environment in current dir in folder .venv.
	- `uv venv`
- Activate environment
	- `source .venv/bin/activate`
- Deactivate environment
	- `deactivate`


### Install

- uv pip install crawl4ai
- crawl4ai-setup
- crawl4ai-doctor


## Docker installation
- change keys in .env
- docker-compose up


# Chrome mit persistent context laden (Cookies etc) => gespeicherte Logins für Crawling verwenden

Nutzbar z. B. in
- Playwright: https://playwright.dev/python/docs/api/class-browsertype#browser-type-launch-persistent-context
- CrawlAI: https://docs.crawl4ai.com/advanced/identity-based-crawling/


## 1. Chromium starten und neues, leeres Context-Verzeichnis anlagen

Voraussetzung: CrawlAI (und damit auch Playwright) lokal installiert, inkl. Chromium-Browser

Chromium-Browser ist beim Mac hier: `~/Library/Caches/ms-playwright/chromium-1161/chrome-mac/Chromium.app/Contents/MacOS/Chromium`

Start Chromium und anlegen neues Context-/Datenverzeichnis 'my_chrome_profile' : `~/Library/Caches/ms-playwright/chromium-1161/chrome-mac/Chromium.app/Contents/MacOS/Chromium --user-data-dir=/test/my_chrome_profile/` 


## 2. In Webseite(n) einloggen

Cookies etc. werden im Context-/Datenverzeichnis gespeichert.

Test: 
- Chromium beenden
- Chromium starten (mit 'my_chrome_profile', siehe oben)
- Webseiten sollten ohne Login direkt aufrufbar sein


## 3. Aufrufen mit Context-/Datenverzeichnis

1. Per Terminal (wie oben)
`~/Library/Caches/ms-playwright/chromium-1161/chrome-mac/Chromium.app/Contents/MacOS/Chromium --user-data-dir=/test/my_chrome_profile/`


2. Per Playwright / Pyhton
user_dir = '/test/my_chrome_profile'
user_dir = os.path.join(os.getcwd(), user_dir)

with sync_playwright() as p:
    browser = p.chromium.launch_persistent_context(user_dir, headless=True)
    page = browser.new_page()
    page.goto("https://www.domain.com)


3. Per CrawlAI
siehe https://docs.crawl4ai.com/advanced/identity-based-crawling/

from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig
browser_config = BrowserConfig(
    headless=True,
    use_managed_browser=True,
    user_data_dir="/test/my_chrome_profile",
    browser_type="chromium"
)