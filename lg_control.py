import requests
import json

def send_command(tv_ip, port):
    url = f"http://{tv_ip}:{port}/roap/api"
    headers = {'Content-Type': 'application/json'}
    
    # Example: Power On the TV
    command = {
        "id": 1,
        "method": "ssap://com.webos.service/system/powerOn",
        "params": {}
    }

    try:
        response = requests.post(url, data=json.dumps(command), headers=headers)
        response.raise_for_status()
        print("Response:", response.text)
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    tv_ip = "192.168.18.13"  # Replace with your TV's IP address
    port = 3000              # Replace with the correct port
    send_command(tv_ip, port)
