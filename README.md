# MQTT-Controlled Web View using pywebview and paho-mqtt

This script opens a web view that can be controlled by receiving MQTT messages. The messages contain the URL that has to be loaded in the web view. It uses the `paho-mqtt` library for MQTT communication and the `pywebview` library for creating the web view.

## Installation

1. Clone the repository or download the script file.

2. Install the required dependencies by running the following command:

   ```bash
   pip install -r dependencies.txt
   ```

   Make sure to have Python and pip installed on your system.

## Usage

1. Update the script with your MQTT broker configuration:

   ```python
   # MQTT broker configuration
   broker_address = "mqtt.broker.com"  # Replace with your broker's address
   broker_port = 1883  # Replace with your broker's port
   topic = "webview/url"  # Topic to subscribe for URL updates
   ```

   Replace `"mqtt.broker.com"` with the address of your MQTT broker, and `1883` with the appropriate port number if different. Set the `topic` variable to the desired topic for receiving URL updates.

2. Run the script using the following command:

   ```bash
   python mqtt_webview.py
   ```

   The script will connect to the MQTT broker, subscribe to the specified topic, and open a web view window. It will wait for MQTT messages containing URLs to load in the web view.

3. To control the web view, publish MQTT messages with the desired URL to the specified topic from another client. For example, using the `paho-mqtt` library, you can publish a message like this:

   ```python
   import paho.mqtt.publish as publish

   # MQTT broker configuration
   broker_address = "mqtt.broker.com"  # Replace with your broker's address
   broker_port = 1883  # Replace with your broker's port
   topic = "webview/url"  # Topic to publish URL updates

   # URL to open
   url = "http://example.com"

   # Publish URL to the MQTT topic
   publish.single(topic, payload=url, hostname=broker_address, port=broker_port)
   ```

   Replace `"mqtt.broker.com"` with the address of your MQTT broker, `1883` with the appropriate port number, and set the `topic` variable to the desired topic for URL updates. Modify the `url` variable with the URL you want to load in the web view.

4. The script will receive the MQTT message, load the URL in the web view, and display the webpage.

## Dependencies

The following dependencies are required:

- paho-mqtt
- pywebview

You can install the dependencies by running the following command:

```bash
pip install -r dependencies.txt
```

Make sure to run the command in the same directory where the `dependencies.txt` file is located.
