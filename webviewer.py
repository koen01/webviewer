import webview
import paho.mqtt.client as mqtt

# MQTT broker configuration
broker_address = "broker"  # Replace with your broker's address
broker_port = 1883  # Replace with your broker's port
topic = "webview/url"  # Topic to subscribe for URL updates

# Create a global variable to store the window instance
window = None

# MQTT callback function
def on_message(client, userdata, msg):
    global window

    url = msg.payload.decode()
    print("Received URL:", url)

    # Create the window if it doesn't exist
    if window is None:
        window = webview.create_window(
            "Web View",
            url,
            fullscreen=True,
        )
    else:
        # Load the new URL in the existing window
        window.load_url(url)

# Create MQTT client and set up callback
client = mqtt.Client()
client.on_message = on_message

# Connect to MQTT broker and subscribe to topic
client.connect(broker_address, broker_port, 60)
client.subscribe(topic)

# Create an initial window with a placeholder URL
window = webview.create_window(
    "Web View",
    "about:blank",
    fullscreen=True,
)

# Start MQTT loop
client.loop_start()

# Start web view
webview.start()
