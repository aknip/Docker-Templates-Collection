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



## Local chromium (Mac local)

~/Library/Caches/ms-playwright/chromium-1161/chrome-mac/Chromium.app/Contents/MacOS/Chromium

~/Library/Caches/ms-playwright/chromium-1161/chrome-mac/Chromium.app/Contents/MacOS/Chromium --user-data-dir=/Users/aknipschild/Documents/my_chrome_profile
