import requests
import json
import time
import sys

class Crawl4AiTester:
    def __init__(self, base_url: str = "http://localhost:11235"):
        self.base_url = base_url

    def submit_and_wait(self, request_data: dict, timeout: int = 300) -> dict:
        # Submit crawl job
        headers = {"Authorization": "Bearer YOURKEYHERE&fhjdk"}
        response = requests.post(f"{self.base_url}/crawl", headers=headers, json=request_data)
        task_id = response.json()["task_id"]
        print(f"Task ID: {task_id}")

        # Poll for result
        start_time = time.time()
        while True:
            if time.time() - start_time > timeout:
                raise TimeoutError(f"Task {task_id} timeout")

            result = requests.get(f"{self.base_url}/task/{task_id}", headers=headers)
            status = result.json()

            if status["status"] == "completed":
                return status

            time.sleep(2)


tester = Crawl4AiTester()

# Test basic crawl
request = {
    "urls": "https://www.nbcnews.com/business",
    "priority": 10
}

result = tester.submit_and_wait(request)
print("Basic crawl successful!")
print(f"Content length: {len(result['result']['markdown'])}")
print(result['result']['markdown'])

