import requests
import time

url = 'http://localhost:8080/'

for _ in range(100):
    response = requests.get(url)
    print(f"Status Code: {response.status_code}")
    time.sleep(0.1)  # Simulate bursty traffic by delaying slightly
