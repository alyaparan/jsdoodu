# JS.Doodu

## Version 1.0.1

JS.Doodu is a sophisticated web application designed to capture detailed browser and system information from the client and send it to a Node.js server for storage and analysis. This tool is perfect for web developers, data analysts, cybersecurity enthusiasts, and ethical hackers looking to gain deep insights into client-side environments.

## Features

- **IP Address Detection**: Automatically fetches and logs the client's IP address.
- **Browser Information**: Collects comprehensive browser details such as name, version, language, and more.
- **System Information**: Gathers data about the client's operating system, platform, and hardware.
- **Network Information**: Logs network-related information like connection type and downlink speed.
- **Geolocation**: Captures the client's geographic location (latitude and longitude).
- **Device Capabilities**: Detects available device features such as battery status, media devices, and sensors.
- **Performance Metrics**: Logs navigation timing and other performance-related metrics.

## Installation

1. **Clone the Repository**:
    ```sh
    git clone https://github.com/alyaparan/jsdoodu.git
    ```
2. **Navigate to the Project Directory**:
    ```sh
    cd jsdoodu
    ```
3. **Install Dependencies**:
    ```sh
    npm install
    ```

## Usage

1. **Start the Server**:
    ```sh
    node server.js
    ```
2. **Open `index.html` in Your Browser**: This will capture and send data to the server.

## File Structure

