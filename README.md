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
3. **Navigate to the Server Directory**:
    ```sh
    cd server
    ```
    
4. **Install Dependencies**:
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

The project directory structure is as follows:

    jsdoodu/
    ├── CODE_OF_CONDUCT.md
    ├── CONTRIBUTING.md
    ├── LICENSE
    ├── README.md
    ├── package-lock.json
    ├── server/
    │ ├── node_modules/
    │ ├── package-lock.json
    │ ├── package.json
    │ └── server.js
    └── website/
    ├── client.js
    ├── favicon.ico
    ├── index.html
    ├── script.js
    └── styles.css


### Directories and Files

- **`server/`**: Contains the Node.js server files.
  - `node_modules/`: Directory for Node.js dependencies.
  - `package-lock.json`, `package.json`: Node.js package management files.
  - `server.js`: Main server script.

- **`website/`**: Contains the client-side files for the web application.
  - `client.js`: Client-side JavaScript file.
  - `favicon.ico`: Favicon for the website.
  - `index.html`: Main HTML file for the application.
  - `script.js`: Additional JavaScript functionality for the website.
  - `styles.css`: CSS styles for the website.

## Contributing

- **Code of Conduct**: Please adhere to our [Code of Conduct](CODE_OF_CONDUCT.md) when contributing.
- **Contributing Guidelines**: Read the [Contributing Guidelines](CONTRIBUTING.md) before submitting pull requests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
