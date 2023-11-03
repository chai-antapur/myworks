import websocket

# Define the WebSocket URL (replace with your WebSocket server URL)
websocket_url = "ws://localhost:9010"

def on_message(ws, message):
    print(f"Received message: {message}")

def on_error(ws, error):
    print(f"Error: {error}")

def on_close(ws, close_status_code, close_msg):
    print("Closed WebSocket connection")

def on_open(ws):
    print("Opened WebSocket connection")
    # Send a message after the WebSocket connection is opened
    ws.send("Hello, WebSocket!")

if __name__ == "__main__":
    # Create a WebSocket connection
    ws = websocket.WebSocketApp(websocket_url, on_message=on_message, on_error=on_error, on_close=on_close)
    ws.on_open = on_open

    # Run the WebSocket client
    ws.run_forever()
