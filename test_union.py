import os
import requests
from typing import Any

# Same shared secret the server reads. Export WORKWISE_ENDPOINT_TOKEN, or copy
# the throwaway token the server prints at startup when it is unset.
token = os.environ.get("WORKWISE_ENDPOINT_TOKEN", "")

url = "http://localhost:8000/v1/workwise/unions"
headers = {"Content-Type": "application/json", "X-Endpoint-Token": token}
data: dict[str, Any] = {
    "register_num": "REG-2025-008",
    "sector_info": "Education",
    "membership_size": 12,
    "is_active_council": False
}

response = requests.post(url, json=data, headers=headers)
print(f"Status: {response.status_code}")
print(f"Body: {response.json() if response.ok else response.text}")