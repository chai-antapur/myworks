import websocket
import websockets
import json 
# Define the WebSocket URL (replace with your WebSocket server URL)
websocket_url = "ws://localhost:9010"


async def send_requests():
    print("send requests")
    async with websockets.connect(websocket_url) as websocket:
        while True:  # Loop indefinitely
            # Define the JSON message to send, alternating between true and false
            json_message = {
                "type": "CustomRequest",
                "data": "true"  # Send "true" in the first request
            }
            await websocket.send(json.dumps(json_message))
            print("Sent WebSocket request with 'true'")

            # Receive and print the response
            response = await websocket.recv()
            print(f"Received response: {response}")

            # Toggle the value for the next request
            json_message["data"] = "false"  # Send "false" in the next request

            # Send the JSON message with "false" value
            await websocket.send(json.dumps(json_message))
            print("Sent WebSocket request with 'false'")

            # Receive and print the response
            response = await websocket.recv()
            print(f"Received response: {response}")

def on_message(ws, message):
    try:
        json_message = json.loads(message)

        # Check if the "type" field exists in the JSON
        if "type" in json_message:
            message_type = json_message["type"]
            print(f"Received message with type: {message_type}")
            if message_type == "LoginResponse":
                send_requests()                
                
        else:
            print("Received JSON message, but it does not contain a 'type' field.")
    except json.JSONDecodeError:
        print("Received message is not valid JSON.")

def on_error(ws, error):
    print(f"Error: {error}")

def on_close(ws, close_status_code, close_msg):
    print("Closed WebSocket connection")

def on_open(ws):
    print("Opened WebSocket connection")
    # Send a message after the WebSocket connection is opened
    #ws.send("Hello, WebSocket!")
    json_message = {
        "type": "LoginRequest",
        "email_id": "chaitra@br.com",
        "password": "123456"
    }

    # Send the JSON message as a string
    ws.send(json.dumps(json_message))

if __name__ == "__main__":
    # Create a WebSocket connection
    ws = websocket.WebSocketApp(websocket_url, on_message=on_message, on_error=on_error, on_close=on_close)
    ws.on_open = on_open

    # Run the WebSocket client
    ws.run_forever()
