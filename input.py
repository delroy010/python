import requests
import json
import time

def send_command(tv_ip, port, command):
    url = f"http://{tv_ip}:{port}/roap/api"
    headers = {'Content-Type': 'application/json'}

    try:
        response = requests.post(url, data=json.dumps(command), headers=headers)
        response.raise_for_status()
        print("Response:", response.text)
    except requests.exceptions.RequestException as e:
        print(f"Error sending command: {e}")

if __name__ == "__main__":
    tv_ip = "192.168.18.13"  # TV IP Address
    port = 9080  # Default TV port

    # 1. Switch to Live TV
    live_tv_command = {
        "id": 1,
        "method": "ssap://tv/switchInput",
        "params": {
            "inputId": "TV"  # Try variations if this doesn't work
        }
    }

    send_command(tv_ip, port, live_tv_command)
    time.sleep(5)  # Allow time for the TV to switch inputs

    # 2. Launch Netflix
    netflix_command = {
        "id": 1,
        "method": "ssap://system.launcher/launch",
        "params": {
            "id": "com.webos.app.netflix"  # Try variations if this doesn't work
        }
    }

    send_command(tv_ip, port, netflix_command)

    # 3. Check current input (optional)
    current_input_command = {
        "id": 1,
        "method": "ssap://com.webos.service.tv/getCurrentInput"
    }

    send_command(tv_ip, port, current_input_command)
